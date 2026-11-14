# swmm5-hy

EPA SWMM 5.2.4 in Hy, written by a translator that reads EPA's C, and judged against EPA itself: the binary `.out`
file byte for byte, and the `.rpt` report line for line except the three lines that print the wall clock.

**Result: all 480 gate models identical to EPA 5.2.4.** 479 in the first full gate (hy_1), where
EPA/72_H&H_Elements(2).inp was not run (timed out after 1800 s); that deck, which routes a dry year at a 10 s step
before its reported storm, was then run on its own with a 90-minute limit and was identical (4,475 s;
hy_long2_72hh). The independent rerun from a clean checkout (hy_v): 478 identical, and two not run in 1800 s,
72_H&H again and Hydrology/SCANLON.inp (1,742 s in hy_1, stopped twice in hy_v with 98.7% and 98.1% of its `.out`
written, identical so far); SCANLON, run on its own with 55 minutes, was identical in 1,897 s. The main session's
check from a clean clone: 48 of 48 (hy_main). Every model that finished, in every run, was identical; Hy runs at the
Python port's speed, about 56 times EPA's (see Speed).

It is not a new engine and not a wrapper: there is no C in it and it imports no other port. Every number it writes
is EPA 5.2.4's, including the results of EPA's own defects wherever EPA's behaviour is defined
(`lessons/02-epa-defects-found.md`). Hy is one of the eight languages of the second wave of Bob Dickinson's Code
Rosetta Stone app.

Hy is a Lisp that compiles to Python's syntax tree, so the engine is Lisp source that runs on CPython: the speed is
the Python port's (see Speed).

## The parity contract

The same as the earlier ports' (see `go/` or the swmm5-go repository): EPA SWMM 5.2.4 built from the USEPA v5.2.4
tag with gcc 13.3 `-O2` on x86-64 Linux with glibc 2.39 (`ref/Makefile`), on a processor with FMA and AVX2; each
model run in its own folder; pass = `.out` byte-identical (when EPA writes one) and `.rpt` identical after removing
`Analysis begun on`, `Analysis ended on` and `Total elapsed time`, the exit code the same (EPA's command line always
exits 0). When an input error stops EPA before it writes results, the engine must not write a results file either.
Corpus: the 480 gate models of `gate/models_all.tsv` from SWMMBobSWMM6/1729-SWMM5-Models-2030.

## Run

Requires CPython 3.13 and Hy 1.3.1 (`pip install hy==1.3.1`, which brings funcparserlib 1.0.1); tested with
**Python 3.13.18** (`/usr/local/bin/python3`, built with clang 23.1.3) and **Hy 1.3.1**. Nothing else: the engine
uses Python's standard library only.

```sh
hy/build.sh                                          # once: Hy compiles the modules to bytecode (about 15 s)
hy/runswmm model.inp model.rpt model.out             # = python3 -I -m hy hy/runswmm.hy ...
```

Without `build.sh` the first run compiles the engine itself and caches the bytecode in `hy/swmm5/__pycache__`.
`-I` keeps the model's folder off Python's module search path.

To regenerate the engine: `python3 tools/c2x/emit_hy.py hy/swmm5 --check` from the repository root (needs
`pip install libclang==18.1.1` and the clang 18 headers at `/usr/lib/llvm-18/lib/clang/18/include`; about 30 s, and
15 s more for the check).

## How it was made

`tools/c2x/front.py` parses EPA's 54 C files with libclang. Hy's data model is Python's, so every question a
translation of C into Python has to answer (a C pointer to a number, C's integer division and 32-bit wraparound,
rounding to `float` after each float operation, a `switch` with fall-through, a `for` loop with `continue`, division
by zero) was already answered by the Python back end, `tools/c2x/emit_py.py`, whose engine was checked against EPA.
`tools/c2x/emit_hy.py` (431 lines) reuses those answers and changes only the syntax: it runs the Python back end in
memory, parses the Python it would have written with Python's own `ast` module, and writes each node as the Hy form
that compiles back to that node (`x = e` is `(setv x e)`, `a[i][j]` is `(get a i j)`, `if/elif/else` is `cond`,
`def` is `defn`, `class` is `defclass`, `~x` is `(bnot x)`, a list comprehension is `lfor`, and so on; the table is
in the emitter's header). So the Hy engine is the Python port's translation in Lisp syntax, as the JavaScript port is
the TypeScript port's without its types. The engine, `hy/swmm5/engine.hy`, is 31,116 lines, generated; nothing in it
is edited by hand.

Three rules keep the Hy program the same program:

- **Hy returns the value of a function's last form.** Every `defn` ends with `None` unless its last statement is a
  `return`, so no function hands back a value its C original does not return (and `__init__` returns nothing).
- **Names Hy would read as something else.** A name in call position that is one of Hy's core macros is that macro,
  not a call: SWMM has a function called `match`, which would be Hy's pattern-matching form. Hy's reader also turns
  the symbols `NaN` and `Infinity` into numbers. Such names get the suffix `__h` everywhere (only `match` occurs).
- **`pass`** has no Hy form; an empty body is `None`.

**The check that the re-spelling changed nothing.** `emit_hy.py --check` compiles the written Hy with Hy's own
compiler and compares the resulting syntax tree with the tree of the Python text, statement by statement, after
removing what Hy adds: `import hy`, the temporaries `_hy_anon_N` in which Hy keeps the value of every `if` (an `if`
is an expression in Hy), the `if True:` of a `cond`'s last branch, a final `return None`, and Hy's habit of writing
an `if` whose branches are single expressions as a conditional expression. Result: **3,529 top-level statements, 0
differ** (the classes, constants and 1,157 functions of the engine). The temporaries are real work at run time (a
store of `None` or of a call's value in each branch), but small beside the engine's own.

## The runtime and the math library

The runtime, `hy/swmm5/crt.hy` (1,064 lines), the hand ports of `odesolve.c`, `mempool.c` and six helpers that use
pointer arithmetic, `hy/swmm5/overrides.hy` (210 lines), and the command line, `hy/runswmm.hy` (50 lines, EPA's
`run/main.c`), are written in Hy. They follow the Python port's runtime in design (C strings as a bytearray and an
offset, a Box or an element reference for a C pointer to a number), and differ where the checks below found the
Python port's behaviour different from glibc's.

- **printf/snprintf**: Python's `%` operator for the digits of `%f`, `%e` and `%g` (correctly rounded, as glibc's
  are); signs, `nan`/`inf`, padding and every integer conversion are written in the runtime, which honours C's
  length modifiers (`%u` and `%x` of a negative `int` print its 32-bit pattern, of a `long` its 64-bit one).
- **strtod/atof/sscanf**: glibc's syntax written out (decimal, hexadecimal with `p` exponent, `inf`, `infinity`,
  `nan` and `nan(n-char-sequence)` with its payload, as glibc's `__strtod_nan` reads it); the value of a decimal
  number is Python's `float()`, correctly rounded as glibc's `strtod` is; a hexadecimal one is `float.fromhex`, also
  correctly rounded. sscanf's `%f` into a C `float` rounds once, as glibc's `strtof` does (exact rational arithmetic
  where converting the double would round twice).
- Checked against glibc 2.39 by `hy/test/run_crtcheck.sh` (the 1,394,252 cases from `tools/crt/test/mkfmt.c` the
  other runtimes replay): **1 differs**, `%#g` of 999999.5 (glibc `1.e+06`, the port `1.00000e+06`), the case every
  runtime reports; SWMM never uses `%#g`. And 200,000 cases of sscanf's `%f` into a float, most of them next to a
  midpoint between two floats (`hy/test/mkstrtof.c`, written for this port): **0 differ**; converting the double
  instead would differ on 53,993 of them. Output: `hy/results/crtcheck_result.txt`.
- **Math.** The engine calls CPython's `math.fabs` and `math.atan` directly and the runtime's wrappers for the
  rest. CPython's `math` module calls glibc's libm, but this CPython 3.13.18 binary imports `exp`, `log` and `pow`
  at their old GLIBC_2.2.5 versions, where EPA imports GLIBC_2.29 (`hy/results/libm_imports.txt`): the old versions
  are glibc's SVID compatibility wrappers, which call the same routines and differ only in how they report errors.
  CPython also decides some cases itself (`math.log` of a NaN returns its argument; `math.pow` handles NaN and
  infinite arguments by C99's table) and raises where C returns an infinity or a NaN. So each wrapper calls
  `math.<f>` for ordinary arguments and glibc's own function through `ctypes` for every argument where Python raises
  or decides by itself (`ctypes` looks the name up with `dlsym`, which gives the symbol's default version: exactly
  the versions EPA imports, `exp@GLIBC_2.29` and so on, recorded in the same file). `floor` and `ceil` are written in
  the runtime, because `math.floor` returns a Python integer, which has no -0.0: `floor(-0.0)` must stay -0.0 and
  `ceil(-0.5)` is -0.0 in C. `sqrt` is `math.sqrt`, with `ctypes` for negative and NaN arguments.
- Checked bit for bit, NaN signs and payloads included, by `hy/test/run_libm_tests.sh`, each function as the engine
  calls it: 10,000,416 random arguments over SWMM's ranges plus special values (`tools/libm/test/mkvectors.c`),
  3,300,000 edge cases (`mkedge.c`: huge trigonometric arguments, negative bases, overflow, underflow, subnormals) and
  8,000,360 cases (`hy/test/mkexact.c`) for `sqrt`, `floor`, `ceil`, `fabs`, negation, `(float)`, `(int)` and
  `(long)`: **0 differ** (`hy/results/libm_tests.txt`).
- **stdio**: Python binary files with C's end-of-file flag and `fgets` semantics; REAL4 values of the `.out` file
  are written with `struct`'s `f`, which is C's `(float)` cast (a finite double that rounds to infinity is written
  as the infinity, as `cvtsd2ss` does).

## How it was checked

| Run | Models | Engine | Result |
|---|---|---|---|
| development | 40 drawn at random (seed 7) from the decks the Python port ran in under 8 s, each in a scratch copy of its folder | the engine while it was being built | 40 identical |
| **hy_1a** | **224 of the 448 fast models** | **commit a06fe10** | **224 identical** |
| **hy_1b** | **the other 224** | **the same** | **224 identical** |
| **hy_1c** | **7 of the 30 slower models** | **the same** | **7 identical** |
| **hy_1d** | **7 more** | **the same** | **7 identical** |
| **hy_1e** | **8 more** | **the same** | **8 identical** |
| **hy_1f** | **the last 8** | **the same** | **8 identical** |
| **hy_1g** | **Hydrology/SCANLON.inp** | **the same** | **identical (1,742 s)** |
| **hy_1h** | **EPA/72_H&H_Elements(2).inp** | **the same** | **not run (timed out after 1800 s)** |
| hy_v_a | the chunk of hy_1a | a06fe10 from a clean checkout (below) | 224 identical |
| hy_v_b | the chunk of hy_1b | the same | 224 identical |
| hy_v_c | the chunk of hy_1c | the same | 7 identical |
| hy_v_d | the chunk of hy_1d | the same | 7 identical |
| hy_v_e | the chunk of hy_1e | the same | 8 identical |
| hy_v_f | the chunk of hy_1f | the same | 8 identical |
| hy_v_g | Hydrology/SCANLON.inp | the same, checkout made again after the restart (below) | not run (timed out after 1800 s; 98.7% of the `.out` written, identical to EPA's so far) |
| hy_v_g2 | Hydrology/SCANLON.inp once more | the same | not run (timed out after 1800 s; 98.1% written, identical so far) |
| hy_v_h | EPA/72_H&H_Elements(2).inp | the same | not run (timed out after 1800 s) |
| hy_main | 48: 45 drawn at random from the 479 of hy_1, plus the three decks that SAVE and USE `cho.txt` | a clean `git clone` of commit b988548, `engine.hy` regenerated there (byte-identical) | 48 identical |
| hy_long_scanlon | Hydrology/SCANLON.inp, on a copy of the deck, time limit 3300 s | that clone | identical (1,897 s) |
| hy_long_72hh | EPA/72_H&H_Elements(2).inp, on a copy of the deck, time limit 3300 s | that clone | not run (timed out after 3300 s; the 65,531 bytes of `.out` written, header and the first 20 of 145 reporting periods, identical to EPA's) |
| **hy_long2_72hh** | **EPA/72_H&H_Elements(2).inp, on a copy of the deck, time limit 5400 s** | **that clone** | **identical (4,475 s)** |

hy_1a to hy_1h cover the 480 models once each and are the result; hy_v_a to hy_v_h are the independent full rerun
(478 identical, 2 not run).
For hy_v, `git archive a06fe10` was unpacked into `/dev/shm/hy_v`, the engine was regenerated there from EPA's C with
that checkout's `emit_hy.py --check` (0 problems, conversion check 0 differ, `engine.hy` byte-identical to the
committed one: `hy/results/hy_v_regen.txt`), its modules were compiled to bytecode, and the gate ran that checkout's
`runswmm_saves.sh`. A first hy_v_g (started 20:47 on 9 November) and hy_v_h (still queued) were lost when the
container restarted at about 21:00, which emptied `/dev/shm` (the checkout and the results folder); the checkout was
made again the same way (engine regenerated, identical again: the second record in `hy_v_regen.txt`) and the two
chunks were run from it. SCANLON.inp ran at most 58 s inside the limit in hy_1, so how far it gets in 1800 s depends
on the machine's other load; when it was stopped in hy_v_g, one more run of it was made (hy_v_g2), stopped likewise.
Both are reported as not run. A stopped model is counted as nothing but not run; what each had written when it was
stopped is compared with EPA's in `hy/results/stopped_runs.txt` (SCANLON: the first 98.1 to 98.7% of the `.out`,
identical; both models: the input summary at the head of the report, identical). Records: `hy/results/hy_1*.json`,
`hy_v_*.json` and their logs (`*_run.txt`); queue, start and end times in `hy/gate/*_times.txt`. Before the gate,
`emit_hy.py --check` (above) and the runtime and math checks (below) were the tests.

All runs: `python3 gate/gate.py NAME "$PWD/hy/runswmm_saves.sh" --ids IDS -j 1 --timeout 1800 --prune`, inside
`flock` on the shared corpus lock, with the output folder in `/dev/shm` (`lessons/22`), through
`hy/gate/run_chunk.sh`. `runswmm_saves.sh` (the Ruby port's wrapper with the engine changed) backs up every file a
deck SAVEs (listed by the swmm6-rust repository's `gate/savefiles.py`, called read-only), including the backslash
spelling of `[LID_USAGE]` report files (`lessons/29`), and restores them after the run; a deck with nothing to back
up runs the engine with `exec`, so the gate's timeout stops the engine itself. The chunks (`hy/gate/ids_*.txt`) were
cut so that each background job, queue included, stayed inside the session's two-hour limit: the 448 models
estimated (from the Python port's gate times, or the Ruby port's for the decks the Python port never ran) at two
minutes or less in two chunks, the 30 slower decks in four, and the two longest each on its own.
`Hydrology/cho.txt` was 1,114,474 bytes, md5 5b0ca1fe78588202fa779dbfa417b089, before and after.

The main session then checked the result itself: a clean `git clone` of commit b988548, `tools/c2x/emit_hy.py hy/swmm5
--check` run again there (0 problems, conversion check 0 differ, `engine.hy` byte-identical to the committed one), its
modules compiled with `hy/build.sh`, and gate run hy_main from that clone on 48 models: 45 drawn at random (seed
20261109) from the 479 of hy_1, plus `Hydrology/save_rtk_long.inp`, `one_sub_one_rdii_node.inp` and
`Use_SeasonalRDIIn.inp`, the decks that SAVE and USE `cho.txt`. All 48 identical, exit code 0 on each, 1,049 s of
engine time (the longest Hydrology/sewer_rdii_problem.inp, 455 s); ids in `hy/gate/ids_main_check.txt`, record in
`hy/results/hy_main.json`. `cho.txt` was unchanged afterwards.

The two decks the rerun did not finish were then given longer, each on its own. Neither reads or writes any other
file, so each was copied to a scratch folder in memory and run there, outside the corpus and its lock, with
`gate.py`'s own run-and-compare function (`hy/gate/run_long.py`; records `hy/results/hy_long_*.json`, which name
the corpus path the copy came from). SCANLON.inp, given 3300 s, finished in 1,897 s, identical.
72_H&H_Elements(2).inp routes a dry year (19 August 2012 to 19 August 2013, 10 s routing step) before its 36 hours of reported storm, so nothing but the input summary
reaches the report until the very end; given 3300 s, it was stopped with the header and the first 20 of its 145
reporting periods written to the `.out` (65,531 of 440,275 bytes, identical to EPA's), that is, within the last 31
simulated hours of 367.5 days. Given 5400 s (hy_long2_72hh), it finished in 4,475 s: `.out` byte-identical, `.rpt`
identical apart from the clock lines, exit code 0. The machine was shared with two other agents' work during all
three runs, so these times are not the engine's speed alone.

## Speed

The gate's clock: in hy_1 the 479 models that finished took 10,750 s of engine time (median 0.95 s), and the one
that was stopped 1,800 s more; the eight runs took 3 h 29 min of wall time (not counting their waits for the corpus
lock). The longest that finished were Hydrology/SCANLON.inp (1,742 s, 58 s inside the limit) and
EPA/attenuation_DW_High_CE.inp (542 s). Against EPA's own times from the reference run (made earlier, on a
differently loaded machine, so a rough guide only), the median ratio is 56 (102 models where EPA took 0.1 s or more;
range 9 to 113). EPA itself takes 1.11 times as long on EPA/72_H&H_Elements(2).inp as on SCANLON.inp, and the Lua,
PHP and TypeScript ports took 1.2 to 1.5 times as long, so the Hy engine was expected to need roughly 1,900 to
2,700 s for it, beyond the 1,800 s the brief allows a model; run on its own (above), it took 4,475 s while two other
agents' work shared the machine. Against the Python port's stored gate times (also made earlier, under
other load), the median ratio is 0.89 (98 models it took 5 s or more on; range 0.22 to 1.01): the Hy engine runs at
the Python port's speed, as it should, being nearly the same Python syntax tree; the two were not run side by side.
In hy_v the 478 models that finished took 9,787 s (the six chunks 2 h 43 min of wall time), but other sessions'
work shared the machine's two processors for part of it: EPA/attenuation_DW_High_CE.inp took 1,065 s there against
542 s in hy_1. Start-up (`hy/runswmm --version`, bytecode compiled) takes 0.12 s. No interleaved benchmark was run
(lessons/07), so these are the gate's numbers, not a measurement of speed.

## What this does not show

- That SWMM is right: identical to EPA means EPA's answers, good or bad.
- EPA/72_H&H_Elements(2).inp and Hydrology/SCANLON.inp inside the gate's 1800 s: both are identical only when given
  longer, each on its own, outside the gate's chunks (hy_long2_72hh, hy_long_scanlon); 72_H&H has been identical
  once, SCANLON twice (hy_1 and hy_long_scanlon).
- Other platforms: the port calls the system libm through CPython and `ctypes`, so on another machine it should
  follow EPA built there; only x86-64 Linux with glibc 2.39 was run, with Python 3.13.18 and Hy 1.3.1.
- That the Python port's translation choices are right beyond the gate. The Hy engine is the Python back end's
  translation re-spelled; where that translation keeps a C `int` value in a variable C declares `double` (Python's
  `/` gives a float either way, and small whole numbers are exact in both), the Hy engine does the same. A
  difference would need a whole-number value beyond 2**53 or the sign of a zero computed from two such integers,
  and on the gate models it would have shown.
- Paths no gate model exercises: streets and inlets (one deck, which stops on input errors), climate files,
  USE HOTSTART, USE INFLOWS, USE RUNOFF; the stepping API is translated but only the command line was gated.
- A checked run in C's sense: Python is memory-safe, but a C overrun that stays inside a Python list's bounds
  would not show; the gate would see it only if it changed an output.
- Speed beyond the gate's own clock: no interleaved benchmark against EPA was run (lessons/07).
- No person has reviewed the generated code line by line; the evidence is the gate and the runtime checks.

## Licence and credit

EPA SWMM is a work of the U.S. Environmental Protection Agency and is in the public domain; its engine is Lewis
Rossman's design, and this port keeps every algorithm as he wrote it. The port contains no glibc code: CPython and
`ctypes` call the system's libm (glibc, LGPL-2.1-or-later, `ref/LGPL-2.1.txt`; see the swmm5-go repository's
`LICENSES`) as a shared library at run time, as EPA's own build does. Hy is distributed under the MIT licence. No
licence has been chosen yet for the translator and the runtime.

## AI use

The translator back end (`tools/c2x/emit_hy.py`), the runtime (`hy/swmm5/crt.hy`, `hy/swmm5/overrides.hy`,
`hy/runswmm.hy`), the generated engine, the launcher, gate wrapper and chunk runner, the runtime and math checks,
lesson 44 and this README were written by Claude (Anthropic's AI model, Claude Opus 5.5) in a Claude Code session on
9 November 2026, for Robert (Bob) Dickinson, who asked for Hy in his Code Rosetta Stone app and set the
byte-for-byte standard. The design of the runtime follows the Python port's (also Claude's work). Claude ran every
gate and check reported here. The checks are mechanical; no person has yet reviewed the code.

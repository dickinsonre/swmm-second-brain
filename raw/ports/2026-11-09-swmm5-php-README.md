# swmm5-php

EPA SWMM 5.2.4 in PHP, written by a translator that reads EPA's C, and judged against EPA itself: the binary
`.out` file byte for byte, and the `.rpt` report line for line except the three lines that print the wall clock.

**Result: 480 of 480 models identical**, twice: the first full gate (php_1a, php_1b, php_1s1, php_1s2, php_1g,
8 November 2026) and an independent rerun from a clean checkout with the engine regenerated (php_v_a, php_v_b,
php_v_s1, php_v_s2, php_v_g): every `.out` byte-identical, every `.rpt` identical except the three clock lines, exit
code 0 on every model, as EPA's. No model timed out; the longest took 620 s.

It is not a new engine and not a wrapper: there is no C in it and it calls no other port. Every number it writes
is EPA 5.2.4's, including the results of EPA's own defects wherever EPA's behaviour is defined
(`lessons/02-epa-defects-found.md`). PHP is one of the eight languages of the second wave of Bob Dickinson's Code
Rosetta Stone app.

## The parity contract

The same as the earlier ports' (see `go/` or the swmm5-go repository): EPA SWMM 5.2.4 built from the USEPA v5.2.4
tag with gcc 13.3 `-O2` on x86-64 Linux with glibc 2.39 (`ref/Makefile`), on a processor with FMA and AVX2; each
model run in its own folder; pass = `.out` byte-identical (when EPA writes one) and `.rpt` identical after removing
`Analysis begun on`, `Analysis ended on` and `Total elapsed time`, the exit code the same (EPA's command line always
exits 0). When an input error stops EPA before it writes results, the engine must not write a results file either.
Corpus: the 480 gate models of `gate/models_all.tsv` from SWMMBobSWMM6/1729-SWMM5-Models-2030.

## Run

Requires PHP 8.3 with OPcache and FFI (tested with **PHP 8.3.6**, `PHP 8.3.6 (cli) (built: Oct 19 2026) (NTS)`,
Zend Engine 4.3.6, the Ubuntu build at `/usr/bin/php`) and nothing else: no Composer packages. There is nothing to
build.

```sh
php/runswmm model.inp model.rpt model.out
```

`php/runswmm` is a shell launcher: `php` with OPcache's tracing JIT switched on (off by default for the command
line), the JIT's trace limits raised (the engine is 35,000 lines; on one model the larger limits took a quarter off
the time), and one optimizer pass switched off (below). `php php/runswmm.php ...` runs the same engine without
OPcache, about twice as slow (4.8 s of CPU against 2.3 s on EPA/master_extran_with_storage.inp, where EPA takes
0.11 to 0.17 s; start-up, compiling the engine, takes 0.13 s).

To regenerate the engine: `python3 tools/c2x/emit_php.py php/swmm5` from the repository root (needs
`pip install libclang==18.1.1` and the clang 18 headers at `/usr/lib/llvm-18/lib/clang/18/include`; about 30 s).

## How it was made

`tools/c2x/front.py` parses EPA's 54 C files with libclang; `tools/c2x/emit_php.py` (1,374 lines, built on the
Python back end's analysis in `emit_py.py` and `emit_cs.py`: pointer modes, names, literals) writes the engine as one
file in namespace `SWMM5`, `php/swmm5/engine.php` (35,225 lines, generated). Hand-written:
`php/swmm5/crt.php` (1,540 lines, the C library pieces SWMM uses), `php/swmm5/overrides.php` (291 lines,
ports of `odesolve.c`, `mempool.c` and six helpers that use pointer arithmetic, as in the Python and Ruby ports) and
`php/runswmm.php` (60 lines, EPA's `run/main.c`). When the port disagreed with EPA, the fix went into the
translator or the runtime, never into the generated file.

PHP looks like C and keeps most of C's statements (`lessons/31-php-keeps-c-statements-and-changes-its-data.md`): `if`,
`while`, `do`, `for`, `switch` with fall-through, `break` and `continue` come through unchanged (a `continue` inside a
`switch` becomes `continue 2`, since PHP counts a switch as a loop). The differences are in the data and the numbers
(each in the emitter's header):

- **Arrays are values.** Assigning or passing a PHP array copies it, where copying a C pointer shares the memory.
  Every C array, malloc'd or fixed, of numbers, records or pointers, is an object, `Arr`, whose property `a` holds a
  PHP array: `$Node->a[$j]->newDepth`. A struct's own arrays and structs are copied by its `__clone`, as C's struct
  assignment copies them. `char*` is a `CPtr` (a shared byte buffer and an offset, with `ArrayAccess` for `p[i]`),
  because PHP strings are values too.
- **Pointers to numbers are references.** A scalar pointer that is only dereferenced is a by-reference parameter
  (`&$h1`), as the C# port uses `ref`; `findSurfArea($j, $qLast, $length, $h1, $h2, $y1, $y2)` reads as the C does.
  No local needs a box.
- **Integers and doubles.** `6 / 2` is the int 3 and `7 / 2` the float 3.5 in PHP: C's integer `/` is
  `\intdiv`, every int-to-double conversion clang records is written out (`(float)$n`, literals as `1.0`), and
  `(int)` of a double goes through `rt_d2i` (x86's answer, INT_MIN, outside the range). Unsigned results are masked
  to 32 bits.
- **Division by zero throws.** PHP 8's `/` throws `DivisionByZeroError` even for floats, so a division whose divisor
  is not a nonzero constant is `($b == 0.0 ? \fdiv($a, $b) : $a / $b)`; `\fdiv` gives IEEE's infinities and, for
  0/0, x86's default NaN (sign bit set, printed "-nan"), as C does.
- **Negation.** PHP's `-$x` is a multiplication by -1, which leaves a NaN's sign bit alone; C's negation flips it:
  doubles are negated by `rt_neg`.
- **Globals** are PHP globals, bound with `global $Node, $Link;` in each function that uses them. A binding costs a
  hash lookup each time it runs, so each sits in the innermost block that holds all the uses of its global, never
  inside a loop: `xsect_getAofY` binds `$A_Circ` in its `case CIRCULAR:`, not 26 cross-section tables on every call.
  Function statics are globals named `function_variable`. Enum values and macros are written as literals (a PHP
  constant costs a lookup each time).
- **Names.** PHP functions are case-insensitive (the emitter checks that no two of EPA's differ only in case) and a
  keyword such as `match` cannot name a function; PHP's own functions are called fully qualified (`\exp`).

## The runtime, the math library and the PHP settings

- **printf/snprintf** (`crt.php`, `rt_fmt_float`, `rt_fmt_int`): PHP's `sprintf` writes `%e` as `1.5e+3` (C:
  `1.5e+03`), loses the sign of -0.0, prints NaN as "NaN", has its own `%g`, and its ' ' flag is a padding character,
  not C's sign flag. Only the digits of `%f` and `%e` come from PHP (zend_dtoa, correctly rounded, ties to even, as
  glibc's printf), with everything around them, and all of `%d`, `%u`, `%x`, `%c`, `%s`, written here.
- **strtod/atof/atoi/sscanf**: glibc's syntax (decimal, hexadecimal floats, `inf`, `infinity`, `nan`, `nan(...)` with
  its payload) scanned here; the decimal text it accepts is converted by PHP's `(float)` (zend_strtod, David Gay's
  correctly rounded strtod); hexadecimal floats are rounded here with integers.
- Checked against glibc 2.39 by `php/test/run_crtcheck.sh` (the 1,394,252 cases from `tools/crt/test/mkfmt.c` the
  other runtimes replay): **1 differs**, `%#g` of 999999.5 (glibc `1.e+06`, the port `1.00000e+06`), the case every
  runtime reports; SWMM never uses `%#g`. Output: `php/results/crtcheck_result.txt`.
- **Math.** PHP's `exp`, `log`, `log10`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan` and `**` call glibc: `/usr/bin/php`
  imports `exp@GLIBC_2.29`, `log@GLIBC_2.29`, `pow@GLIBC_2.29`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `log10`
  and `sqrt`, the versioned symbols EPA imports (`nm -D /usr/bin/php` against `nm -D ref/runswmm`), so the port
  follows EPA, FMA routines included, on any machine both run on. `**` on two floats calls `pow()`; on two ints PHP
  uses its own integer power, so the engine never gives it two ints (clang converts every argument of `pow` to
  double, and so does the translator). `\abs` of a float is `fabs`. PHP's `floor` and `ceil` return a signaling NaN
  unchanged where glibc's quiet it, so the engine calls `rt_floor`/`rt_ceil`, which quiet a NaN first.
- Checked bit for bit, NaN signs and payloads included, by `php/test/run_libm_tests.sh`, with the tracing JIT and
  again with the plain interpreter: 10,000,416 random arguments over SWMM's ranges plus special values
  (`tools/libm/test/mkvectors.c`), 3,300,000 edge cases (`mkedge.c`: huge trigonometric arguments, negative bases,
  overflow, underflow, subnormals) and 8,000,360 cases (`php/test/mkexact.c`) for `sqrt`, `floor`, `ceil`, `fabs`
  and the runtime's C operations `rt_neg`, `rt_f32`, `rt_d2i` and `rt_d2l`: **0 differ** in either mode
  (`php/results/libm_tests.txt`).
- **No fused multiply-add.** `php/test/run_fma_check.sh` computes `a*b + c` where fusing would change the answer, in
  loops hot enough for the JIT: 0 fused results with the interpreter, the tracing JIT and the function JIT, on this
  FMA-capable CPU (`php/results/fma_check.txt`).
- **float.** `(float)x` is a store into a C float and a load back through an FFI cell (`rt_f32`): PHP's FFI
  converts with C's cast (`cvtsd2ss`, round to nearest, a NaN's sign kept); `pack('g')` does the same four times
  slower. The REAL4 values of the `.out` file are packed with `pack('g*')`, the same cast.
- **FFI as storage.** A double array of more than 100,000 elements is an FFI `double[n]` (zero-filled), 8
  bytes an element where a PHP array element is a 16-byte zval: Hydrology/sewer_rdii_problem.inp allocates 3.4 GB of
  RDII rain history in C, in arrays of about 600,000, which as PHP arrays would not fit in this machine's 7 GB. The
  generated code reads and writes such an array as it does a PHP array. FFI calls no C code here.
- **stdio**: PHP streams in binary mode with C's end-of-file flag and `fgets` semantics. PHP writes a plain file
  without buffering (one `write()` per call); EPA writes its results a few numbers at a time, so the runtime buffers
  64 KB as stdio does and empties the buffer before any read, seek, tell or close and at exit.
- **One optimizer pass off.** OPcache's SCCP pass (bit 0x80 of `opcache.optimization_level`) treats 0.0 and -0.0 as
  the same constant: with it on, `$neg ? -0.0 : 0.0` returned -0.0 for a false `$neg` in the runtime's strtod. The
  engine and every check run with `opcache.optimization_level=0x7FFEBF7F`, the default with that bit cleared
  (`lessons/32-phps-optimizer-takes-minus-zero-for-zero.md`).
- Any PHP warning or notice (an undefined array index or property, a string offset past the end) stops the run with
  a stack trace (`runswmm.php` turns them into exceptions): in a translation from C, each would be a bug.

## How it was checked

| Run | Models | Engine | Result |
|---|---|---|---|
| php_1a | 208 (the first half of all but the 19 slowest, in corpus order) | working tree, commit 9e9ff14's files | 208 identical |
| php_1b | the other 253 of them | the same | 253 identical |
| php_1s1, php_1s2 | 17 of the 19 slowest (9 and 8) | the same | 17 identical |
| php_1g | Hydrology/SCANLON.inp and EPA/72_H&H_Elements(2).inp | the same | 2 identical |
| **php_v_a, php_v_b, php_v_s1, php_v_s2, php_v_g** | **the same five lists, all 480 once** | **a clean checkout of commit 9e9ff14, engine regenerated by its emitter (byte-identical to the committed file)** | **480 identical** |
| php_main | 45 drawn at random from the 480, plus the three decks that SAVE and USE `cho.txt` | a clean clone of the working repository at commit 37f0acd (the PHP files as committed in 2e3efa2): the main session's check | 48 identical |

php_1a to php_1g are the first full gate: 480 of 480 identical, exit code 0 on every model, as EPA's. The php_v runs
(2,930 s of engine time) are the independent rerun the brief asks for, from `git archive` of the committed tree into
a scratch folder, with `tools/c2x/emit_php.py` run again there and its `engine.php` compared with the committed one
before the run; they used that checkout's launcher and wrapper. No gate run failed a model. The failures came earlier,
in development runs on 190 decks copied to a scratch folder and compared with `gate/ref_outputs`: `time(&t)`
translated as a call that dropped the store, a deprecated static `FFI::new()` call stopping every run, and
Hydrology/sewer_rdii_problem.inp killed for memory before big double arrays moved to FFI storage. All 190 matched
before the first gate, apart from three whose reports print the absolute path of the scratch folder. The id lists
are in `php/gate/`, the records (JSON, logs, queue and run times) in `php/results/` and `php/gate/`. A container
restart killed the first php_v_g while it was running (its queue record is `php/gate/php_v_g_times_killed.txt`); it
was run again from the start, from the same checkout.

The main session then checked the result itself: run php_main, ids in `php/gate/ids_main_check.txt`, record in
`php/results/php_main.json`. `cho.txt` was unchanged after it.

All runs: `python3 gate/gate.py NAME "$PWD/php/runswmm_saves.sh" --ids IDS -j 1 --timeout 1800 --prune`, inside
`flock` on the shared corpus lock, with the output folder in `/dev/shm` (`lessons/22`). `runswmm_saves.sh` (the Ruby
port's wrapper with the engine changed) backs up every file a deck SAVEs (listed by the swmm6-rust repository's
`gate/savefiles.py`, called read-only), including the backslash spelling of `[LID_USAGE]` report files
(`lessons/29`), and restores them after the run. `Hydrology/cho.txt` was 1,114,474 bytes, md5
5b0ca1fe78588202fa779dbfa417b089, before and after.

## Speed

The gate's clock: the first full gate took 3,315 seconds of engine time for the 480 models (55 min; php_1a and php_1b:
955 s for 461 models; the 19 slowest: 2,361 s), one at a time; the longest were EPA/72_H&H_Elements(2).inp, 620 s, and
Hydrology/SCANLON.inp, 431 s (the two models the Ruby port could not finish in 1,800 s). Against EPA's own times from
the reference run (made earlier, on a differently loaded machine, so a rough guide only), the median ratio is 13.9
(103 models where EPA took 0.1 s or more; range 3.6 to 25.7); against the Ruby port's stored gate times, 0.20 (median
of the 108 models the Ruby port took 5 s or more on; range 0.15 to 0.28). Three changes made before the gate, none of
them in what is computed, were for speed: writing through a 64 KB buffer (PHP writes a plain file unbuffered; a
profile put 18% of EPA/HRSDtest_cim_7.inp's time in the results writer), C's float cast through an FFI cell instead of
`pack`/`unpack` (four times faster in isolation), and binding each global only where it is used. The model took 122 s
before them and 66 s after, but the machine was less loaded the second time, so not all of that is theirs. Start-up
(compiling the 35,225-line engine; `php/runswmm --version`) takes 0.13 s of CPU. Peak memory on
Hydrology/sewer_rdii_problem.inp, which allocates 3.38 GB of RDII rainfall history in C: 3.36 GB resident (EPA: 3.11
GB).

## What this does not show

- That SWMM is right: identical to EPA means EPA's answers, good or bad.
- Other platforms: the port calls the system libm through PHP, so on another machine it should follow EPA built
  there; only x86-64 Linux with glibc 2.39 was run, with PHP 8.3.6. A PHP whose JIT fused multiply-adds, or whose
  optimizer folded floating-point expressions, would need the checks again.
- Paths no gate model exercises: streets and inlets (one deck, which stops on input errors), climate files,
  USE HOTSTART, USE INFLOWS, USE RUNOFF; the stepping API is translated but only the command line was gated.
- A checked run in C's sense: PHP is memory-safe, and every out-of-range read raises a warning that stops the run,
  but a C overrun that stays inside a PHP array's bounds (or writes past an array's end, which PHP grows) would not
  show; the gate would see it only if it changed an output.
- Speed beyond the gate's own clock: no interleaved benchmark against EPA was run (lessons/07).
- No person has reviewed the generated code line by line; the evidence is the gate and the runtime checks.

## Licence and credit

EPA SWMM is a work of the U.S. Environmental Protection Agency and is in the public domain; its engine is Lewis
Rossman's design, and this port keeps every algorithm as he wrote it. The port contains no glibc code: PHP calls the
system's libm (glibc, LGPL-2.1-or-later, `ref/LGPL-2.1.txt`) as a shared library at run time, as EPA's own build
does. PHP is distributed under the PHP License 3.01. No licence has been chosen yet for the translator and the
runtime.

## AI use

The translator back end (`tools/c2x/emit_php.py`), the runtime (`php/swmm5/crt.php`, `php/swmm5/overrides.php`,
`php/runswmm.php`), the generated engine, the launcher, gate wrapper and chunk runner, the runtime, math and FMA
checks, lessons 31 and 32 and this README were written by Claude (Anthropic's AI model, Claude Opus 5.5) in a Claude
Code session on 8 November 2026, for Robert (Bob) Dickinson, who asked for PHP in his Code Rosetta Stone app and set the
byte-for-byte standard. Claude ran every gate and check reported here. The checks are mechanical; no person has yet
reviewed the code.
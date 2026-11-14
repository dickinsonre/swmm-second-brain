---
name: SWMM Engine What If
file: swmm-engine-what-if.html
version: 1.4
date: 2026-11-12
author: Robert Dickinson
links: {netlify: none yet, artifact: "https://claude.ai/artifact/9zoq9We9sPLvkKR7TJzoVw (private)", repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4, license: public domain, role: "reference for 20 translations and 4 extended engines; built and run for the re-run of 2026-11-12; not embedded"}
  - {name: OpenSWMM 1D engine, branch: swmm6_rel, commit: 88329d6, license: Apache-2.0, role: "reference for 12 translations; not embedded or run"}
embedded_code:
  - {name: glibc 2.39 pow, as translated by swmm5-typescript tools/libm, license: LGPL-2.1-or-later}
  - {name: gif.js 0.2.0 worker, license: MIT}
units: US customary (cfs, ft, in/hr) in the two-model toy; none elsewhere
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM Engine What If: which language, for which job, by which road

## What it does

It answers one question for someone deciding how to put SWMM into another language or change what it computes: what do I gain, what do I pay, and what evidence exists. The user picks a goal (7), a road (wrap EPA's C, translate it, or extend it) and a language (21) or extended engine (4). The app returns a fit judgment with its reason, the measured cost and gate result copied from the engine's repository, the trap that engine had to beat, and a next step. It runs no SWMM engine. Its live calculations are floating-point and integer demonstrations of the traps.

## How it computes

- **Fleet numbers** are constants copied from each repository's README at the commit listed below, read on 30 October 2026 (first 8 ports) and 11 November 2026 (all 36).
- **Re-run numbers** (the Re-run tab, the Re-run column, figures 10 and 11) come from one session on 12 November 2026: the 20 SWMM 5 ports cloned at the commits below, built from source and run in the sandbox that builds this app. `tools_v14/collect.py` writes them into the page from the raw results in `evidence/v14/`.
- **Fit judgments** are a table: goal x language x road, level 1 to 3 (poor, fair, strong) with a one-sentence reason. 21 x 7 x 2 = 294 cells, plus 7 for the extend road. They are editorial judgment, not measurement.
- **Speed basis** is one of three: `interleaved` (a benchmark with EPA run in the same shuffled order), `rough` (the gate's own clock against EPA's stored times from a differently loaded machine), or `none` (no ratio claimed).
- **Live calculations**, all in the browser:
  - Fused multiply-add: exact `x*y+z` in BigInt rationals, rounded once to nearest-even, against `x*y+z` in doubles.
  - Go constant folding: the exact product of two decimal literals rounded once, against C's round, round, multiply, round. A product that overflows float64 is reported as a compile error, as Go does.
  - pow census: glibc 2.39 `pow` (translated JavaScript) against the browser's `Math.pow` on 4 argument classes, seeded generator (mulberry32, seed 20261030).
  - `gage.c:251`: `floor(dxMin*86400 + 0.5)` and what each language's own float-to-int conversion gives. In range all truncate; out of range each follows its own rule; x86 gives INT_MIN.
  - Negative zero, NaN sign bit, integer division (C truncates, Python floors).
  - Perl integer path: `(2^53 + 1) + 1` as doubles and as 64-bit integers.
  - Two-model toy: one nonlinear-reservoir subcatchment, `Q = W*(1.49/n)*(d - dp)^(5/3)*S^(1/2)`, `dd/dt = i - Q/A`, Heun's method, dt = 30 s, 720 steps, written once with file-scope state and once with state in an object, stepped round-robin with a second model. It is not SWMM.

## Inputs and outputs

No files are read. Outputs: CSV of the current tab (fit matrix, fleet by family, two-model series, hazard results, gage line table, parity checklist), a GIF or WebM recording, the essay as .docx, and this file.

## The fleet: 20 translations of EPA SWMM 5.2.4

Gate: 480 models from SWMMBobSWMM6/1729-SWMM5-Models-2030. Pass = `.out` byte-identical and `.rpt` identical after removing three wall-clock lines. Reference build: gcc 13.3 at -O2, x86-64 with FMA and AVX2, glibc 2.39.

| Engine | Language | Class | Commit | Gate (480) | Speed vs EPA | Basis | Model state | Lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPA SWMM 5.2.4 | C | ref | v5.2.4 tag | the reference | 1x | interleaved | file and program scope (415 mutable variables) |  |
| swmm5-cplus | C++17 | native | 9a0ef3d | 480 of 480 | 1.003x | interleaved | per model: class Project | 53615 |
| swmm5-rust | Rust (safe) | native | c2af2d3 | 480 of 480 | 1.12x | interleaved | per model: one Project structure | 56158 |
| swmm5-fortran | Fortran 2008 | native | cda06e9 | 480 of 480 | 1.26x (1.13 to 1.4) | interleaved | module level, as EPA keeps it | 50570 |
| swmm5-go | Go 1.22+ | native | 318c8ba | 480 of 480 | 1.72x (1.47 to 2.14) | interleaved | package-level variables, as EPA keeps them | 47848 |
| swmm5-zig | Zig 0.15 | native | 5d5c405 | 480 of 480 | not measured | none | file-scope variables in C's own layout, as EPA keeps them | 40856 |
| swmm5-pascal | Free Pascal | native | 9f11c2f | 480 of 480 | not measured | none | unit-level variables, as EPA keeps its globals | 54588 |
| swmm5-mojo | Mojo 1.2 | native | d941c4a | 480 of 480, twice | ~0.73x (rough: 0.33 to 5.81) | rough | one Globals struct holding all 626 of EPA's globals and static locals, passed to every function by pointer | 40327 |
| swmm5-csharp | C# (.NET 8) | managed | 522a62c | 480 of 480 | 5.19x (2.9 to 27.67) | interleaved | static fields, as EPA keeps it | 42567 |
| swmm5-java | Java 17+ | managed | 1101e2f | 480 of 480 | 9.18x (4.28 to 93.97) | interleaved | static fields, as EPA keeps it | 50991 |
| swmm5-kotlin | Kotlin 2.0 (JVM) | managed | dbde139 | 480 of 480 | 1.31x to 2.63x | interleaved | static JVM fields, as EPA keeps its globals | 43396 |
| swmm5-fsharp | F# (.NET) | managed | 37688c9 | 480 of 480, twice | not measured | none | module-level values, as EPA keeps its globals | 34749 |
| swmm5-groovy | Groovy 3.0 (JVM) | managed | 5be6082 | 480 of 480, twice | not measured | none | static fields, as EPA keeps its globals | 41620 |
| swmm5-python | Python 3.10+ | script | e49f9a0 | 465 identical (451 of 451 fast models, 14 of a 14-model sample of the 29 slow ones) | 81.63x (57.02 to 99.04) | interleaved | module globals, as EPA keeps them | 32822 |
| swmm5-typescript | TypeScript | script | 5ccd409 | 480 of 480 | 19.24x (11.44 to 73.66) | interleaved | module-level variables, as EPA keeps them | 47400 |
| swmm5-javascript | JavaScript | script | 56d8eb2 | 480 of 480, twice | not measured | none | module-level variables, as EPA keeps its globals | 47703 |
| swmm5-php | PHP 8.3 | script | 6e3f3cd | 480 of 480, twice | ~13.9x (rough: 3.6 to 25.7) | rough | PHP globals, as EPA keeps them | 37116 |
| swmm5-ruby | Ruby 3.3 | script | 0c97906 | 478 of 478 run; 2 not run (1,800 s limit) | ~70x (rough: 11 to 147) | rough | Ruby $ globals, as EPA keeps them | 37121 |
| swmm5-lua | Lua 5.4 | script | 8c756c3 | 480 of 480, twice | not measured | none | fields of one table G in the Lua state | 45173 |
| swmm5-hy | Hy 1.3 (on Python) | script | d1474f7 | all 480 identical: 478 within the gate's 1,800 s, the 2 longest run alone | ~56x (rough: 9 to 113) | rough | Python module globals, as the Python port keeps them | 32442 |
| swmm5-perl | Perl 5.38 | script | c533e8f | 478 of 478 run; 2 not run (1,800 s limit) | ~146x (rough: 17 to 291) | rough | package variables, as EPA keeps its globals | 35473 |

Empty repositories: swmm5-scala, swmm5-r.

Controls (from the swmm5-go, swmm5-rust READMEs and lesson 09): EPA run twice (null control): 0 of 40; Fortran with -mfma (positive control): 87 of 480; EPA on glibc's generic math: 43 of 480; TS and Java on their own Math: 38 of 480; EPA as WebAssembly vs native: 21 of 221.

## The re-run of 12 November 2026

Machine: Intel Xeon, 2.10 GHz, 2 cores, with FMA, AVX2 and AVX-512; 8 GB; Ubuntu 24.04, glibc 2.39. Corpus: 1729-SWMM5-Models-2030 at 9ee63bd. EPA 5.2.4 was built from the source vendored in swmm5-go (`ref/epa524`) with the reference flags and run on all 480 gate models (190 s; 39 write no .out). Each port ran through swmm5-go's `gate/gate.py`. Speed: `mybench.py`, the method of the repositories' `gate/bench.py`: 12 models (EPA 0.007 to 0.688 s each), each repetition in a fresh random order, EPA twice per visit, CPU time of the process including start-up; per model the ratio of median times, then median and range over models.

| Engine | Built or run with | Models run | Identical | Speed here: median (range) | Reps |
| --- | --- | --- | --- | --- | --- |
| EPA C (null control) | gcc 13.3.0 -O2, _FORTIFY_SOURCE off | 480 | 480 | 1.005x (0.819 to 1.181) |  |
| C++ | g++ 13.3.0 -O2 -flto | 480 | 480 | 0.94x (0.843 to 1.058) | 5 |
| Rust | rustc 1.97.0, release profile | 480 | 480 | 1.163x (0.952 to 1.349) | 5 |
| Fortran | gfortran 13.3.0 -O2 -ffp-contract=off | 480 | 480 | 1.281x (1.048 to 1.373) | 5 |
| Go | go 1.24.7, GOAMD64=v1 | 480 | 480 | 1.542x (1.281 to 2.478) | 5 |
| Zig | zig 0.15.2 ReleaseFast, -fno-compiler-rt | 480 | 480 | 1.033x (0.757 to 1.17) | 5 |
| Pascal | fpc 3.2.2 -O2 | 480 | 480 | 1.59x (1.435 to 1.872) | 5 |
| Mojo | Mojo 1.2.0, contract=off | 480 | 480 | 1.082x (0.991 to 1.754) | 5 |
| C# | .NET SDK 8.0.134, runtime 8.0.34 | 480 | 480 | 5.353x (2.883 to 30.304) | 5 |
| Java | OpenJDK 21.0.12, ParallelGC, 75% heap | 480 | 480 | 9.847x (4.931 to 91.986) | 5 |
| Kotlin | Kotlin 2.0.21 (from Gradle 8.14.3), OpenJDK 21 | 480 | 480 | 13.648x (6.679 to 138.029) | 5 |
| F# | F# 8 (fsc from SDK 8.0.134), runtime 8.0.34 | 480 | 480 | 6.79x (3.377 to 40.696) | 5 |
| Groovy | Groovy 3.0.24 (from Gradle), OpenJDK 21 | 480 | 480 | 22.974x (9.987 to 328.551) | 5 |
| Python | CPython 3.13.18 | 393 | 393 | 87.397x (69.58 to 111.754) | 2 |
| TS | TypeScript 5.6.3, node 22.23.4 | 480 | 480 | 19.323x (10.879 to 73.145) | 5 |
| JS | node 22.23.4 | 480 | 480 | 17.281x (9.156 to 73.841) | 5 |
| PHP | PHP 8.3.6, OPcache tracing JIT | 451 | 451 | 21.947x (15.083 to 49.978) | 2 |
| Ruby | ruby 3.3.6 | 393 | 393 | 101.653x (85.489 to 129.881) | 2 |
| Lua | Lua 5.4 in lupa 2.8 | 451 | 451 | 47.401x (42.136 to 74.726) | 2 |
| Hy | Hy 1.3.1 on CPython 3.13.18 | 393 | 393 | 96.839x (80.638 to 129.125) | 2 |
| Perl | perl 5.38.2 | 393 | 393 | 249.478x (209.797 to 339.114) | 2 |

Model sets: all 480; the 393 models EPA runs in 0.1 s or less; the 451 models EPA runs in 1 s or less.

Against the READMEs: the 8 figures from interleaved benchmarks (C++, Rust, Fortran, Go, C#, Java, Python, TypeScript) reproduced within 11 percent. The 5 rough guides (Mojo, PHP, Ruby, Hy, Perl) came back 1.45 to 1.73 times higher; the guides used about 100 models with EPA at 0.1 s or more, this benchmark 12 models of which 4 are shorter. No README figure existed for Zig, Pascal, F#, Groovy, JavaScript, Lua. Inside EPA's own band (0.819 to 1.181): C++, Rust, Zig, Mojo. Kotlin's README range (1.31 to 2.63, six longer models) was not repeated.

Generic-math experiment: `GLIBC_TUNABLES=glibc.cpu.hwcaps=-AVX2,-FMA,-FMA4` makes glibc use its non-FMA math routines. EPA's output then changes on 43 of 480 models (15 OUTDIFF, 5 RPTDIFF, 23 RPTDIFF+OUTDIFF), the same count lesson 09 reports. Each port was then run the same way on those models (fast engines: all 43 plus 40 unaffected controls; interpreters: the 21 that EPA runs in 0.3 s or less plus 10 controls) and compared with both EPA references. Follow EPA to the generic answers on every affected model run: C++, Rust, Fortran, Zig, Pascal, Mojo, C#, F#, Python, PHP, Ruby, Lua, Hy, Perl. Keep the FMA answers on every one: Go, Java, Kotlin, Groovy, TS, JS.

Probes: 24 language traps from the lessons re-run in a few lines each (sources in `evidence/v14/probes/`); 24 reproduced. Lessons catalogued: 54 (44 numbered, 10 from swmm5-rust).

## The fleet: 12 translations of the OpenSWMM 6 1D engine

Reference: OpenSWMM 6 1D engine, HydroCouple/openswmm.engine, branch swmm6_rel, commit 88329d6, built here and run on one thread (OMP_NUM_THREADS=1). Gate: the same 480 corpus models, plus 452 extra decks: the input files in the upstream tests folder and the synthetic decks of swmm6-rust's gate, which probe the finite-volume solver, structure coupling, the newer hydrology and the input checks.

| Engine | Language | Commit | Translated from | 480 corpus | 452 extra | Median s per model in gate |
| --- | --- | --- | --- | --- | --- | --- |
| swmm6-rust | Rust (safe) | a7327ca | the C++, directly | 480 of 480 | 452 of 452 |  |
| swmm6-csharp | C# (.NET) | 4faf746 | the C++, through clang's AST | 480 of 480 | 452 of 452 | 0.76 |
| swmm6-go | Go | 0e24a52 | the C# | 480 of 480 | 452 of 452 | 0.14 |
| swmm6-fortran | Fortran | ab29113 | the C# | 480 of 480 | 452 of 452 | 0.25 |
| swmm6-fsharp | F# | 5330098 | the C# | 480 of 480 | 452 of 452 | 0.95 |
| swmm6-javascript | JavaScript | fa9658c | the C# | 480 of 480 | 452 of 452 | 1.33 |
| swmm6-java | Java | 9cf974b | the C# | 480 of 480 | 452 of 452 | 1.92 |
| swmm6-typescript | TypeScript | 901b5ed | the C# | 480 of 480 | 452 of 452 | 2.02 |
| swmm6-kotlin | Kotlin | 5687f4e | the C#; runtime from the Java port's | 480 of 480 | 452 of 452 | 2.96 |
| swmm6-groovy | Groovy | 054f76d | the C#; runtime from the Java port's | 480 of 480 | 452 of 452 | 3.04 |
| swmm6-python | Python | bd14784 | the C# | 412 of 413 run; 1 not finished in 7,000 s | 450 of 452; 2 not finished | 1.92 |
| swmm6-hy | Hy | a2b8361 | the Python port, re-spelled | 478 of 480; 2 not finished in 1,800 s | 450 of 452; 2 not finished | 2.38 |

Empty repositories: swmm6-r, swmm6-php, swmm6-ruby, swmm6-pascal, swmm6-zig, swmm6-perl, swmm6-lua, swmm6-mojo.

## The fleet: 4 engines that extend EPA's C

### swmm5-kw (b592d43)
- Option: swmm_setKwOptions(split, loop), off by default
- Adds: Kinematic wave and steady flow that split a junction among its outlets and iterate directed loops. Stock SWMM stops on both, with ERROR 133 and ERROR 131.
- Change: One new file, kwmod.c, and edits to six: 622 lines added, 4 removed.
- Option off: With the extension off or with nothing to split or loop: 3,737 of 3,759 corpus models identical to stock, 0 different, 10 where stock crashes and it crashes the same way, 11 inconclusive, 1 that stock refuses.
- Option on: No reference engine. Conservation at every split (largest gap 6e-14 cfs), results unchanged when the input order is shuffled (7 of 7 networks), and 14 of 14 stock refusals now run.
- Limits: Kinematic wave cannot run a pipe backwards, surcharge it or see backwater. In both shipped loop networks dynamic wave runs the relief pipe the other way. Its own README: treat loop results as screening, never design.

### swmm524-perched (6f253a4)
- Option: a SOIL2 line in the LID control
- Adds: A perched two-layer soil for bio-retention cells: a 4 in decompacted topsoil over a compacted subsoil that admits water only as fast as its own conductivity allows.
- Change: 310 lines added and 2 changed in lid.c, lid.h and lidproc.c.
- Option off: With no SOIL2 line: 598 of 598 test inputs write the same .out bytes as EPA 5.2.4, every stock LID case among them.
- Option on: No reference engine. A limiting case: with a subsoil conductivity of 1,000 in/hr the interface no longer limits, and runoff equals the stock result to 0.000 in across 64 recovery cases.
- Limits: No observed data and no HYDRUS comparison yet.

### swmm5-raspipe (dfd7984)
- Option: FLOW_ROUTING RASPIPE
- Adds: A semi-implicit pipe solver built from the published HEC-RAS pipe network method: no Preissmann slot and no EXTRAN switch at the crown.
- Change: One new file, raspipe.c, and a patch to EPA's files.
- Option off: Without the option: .out byte-identical to a stock build on 4 of 4 control decks.
- Option on: No reference engine: it has not been compared with a run of HEC-RAS. Closed-form answers (Manning, a pump curve, Stoker's dam break, the U-tube period), a separately written Saint-Venant solver, a volume ledger, and 1,600 corpus models through both engines: median routing continuity error 0.795% stock against 0.005%, at 2.6 times stock's run time.
- Limits: No field data. The reference solver came from the same AI session as the engine. Where the engines disagree in the corpus, nobody has sorted out which is right.

### swmm5-infosewer (12492d6, private repository)
- Option: FLOW_ROUTING INFOSEWER
- Adds: InfoSewer's steady-state and extended-period calculations as a routing option: loads by type, peaking, flow splits, pipe-by-pipe hydrograph routing, wet wells, pump stations and force mains.
- Change: 99 lines added and 3 changed in 13 EPA files, plus 3 new files.
- Option off: Null test: 14 models, .out byte-identical to EPA 5.2.4 and .rpt identical except the clock lines.
- Option on: It has a reference engine: InfoSewer itself. On 71 test models 11,408,158 of 11,894,156 output values are identical in every bit; the rest, all in six models that use LPS or MLD, differ by at most 4.2e-11.
- Limits: Not supported yet: open channels, rational-method loads, curve-based flow splits, pump controls, design mode and water quality. No model outside the test set has been run. The repository is private.

## Fit matrix, translate road

| Goal | C | C++ | Rust | Fortran | Go | Zig | Pascal | Mojo | C# | Java | Kotlin | F# | Groovy | Python | TS | JS | PHP | Ruby | Lua | Hy | Perl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Teach the equations in a browser | fair | fair | fair | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | fair | strong | strong | poor | poor | poor | poor | poor |
| Run 1,000 scenarios as a service | strong | strong | strong | poor | strong | fair | poor | fair | fair | strong | strong | fair | fair | poor | poor | poor | poor | poor | poor | poor | poor |
| Embed SWMM in a larger application | fair | strong | strong | fair | fair | fair | fair | fair | strong | strong | strong | fair | fair | fair | strong | strong | fair | fair | poor | poor | poor |
| Calibrate and explore in notebooks | fair | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | fair | fair | fair | poor | poor | poor | poor | poor |
| Hold several models in one process | poor | strong | strong | poor | poor | poor | poor | fair | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor |
| Stop at a bad array index | poor | poor | strong | fair | strong | fair | poor | poor | strong | strong | strong | strong | strong | strong | poor | poor | fair | poor | fair | strong | fair |
| Try a new numerical method | strong | strong | fair | strong | poor | poor | poor | fair | poor | poor | poor | poor | poor | fair | fair | fair | poor | poor | poor | poor | poor |

## Fit matrix, wrap road

| Goal | C | C++ | Rust | Fortran | Go | Zig | Pascal | Mojo | C# | Java | Kotlin | F# | Groovy | Python | TS | JS | PHP | Ruby | Lua | Hy | Perl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Teach the equations in a browser | fair | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | fair | fair | poor | poor | poor | poor | poor |
| Run 1,000 scenarios as a service | strong | fair | fair | poor | strong | fair | poor | fair | strong | fair | fair | strong | fair | strong | fair | fair | fair | fair | poor | fair | fair |
| Embed SWMM in a larger application | fair | fair | fair | fair | fair | fair | strong | fair | strong | fair | fair | strong | fair | strong | fair | fair | fair | fair | fair | fair | fair |
| Calibrate and explore in notebooks | fair | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | strong | fair | fair | poor | poor | poor | fair | poor |
| Hold several models in one process | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | fair | fair | poor | poor | poor | poor | poor |
| Stop at a bad array index | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor |
| Try a new numerical method | strong | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor | poor |

## Fit, extend road

- Teach the equations in a browser: fair. An extended engine compiles to WebAssembly and runs in a page like stock EPA; swmm5-kw ships that way. The new physics is still C a student must read.
- Run 1,000 scenarios as a service: strong. It is still EPA's C, one process per model, at EPA's speed when the option is off. swmm5-raspipe ran 1,600 corpus models through both engines.
- Embed SWMM in a larger application: fair. It drops in wherever EPA's library does, globals and all, but the host must ship your build in place of EPA's.
- Calibrate and explore in notebooks: fair. Driven from Python like EPA; the new options live in the .inp, so no wrapper needs to know them.
- Hold several models in one process: poor. Still EPA's 415 globals: one model per process.
- Stop at a bad array index: poor. Still C, with unchecked reads, and new code that has seen far less use than EPA's.
- Try a new numerical method: strong. This is the road for new physics: a new option behind a normal .inp, with the old path left byte-identical.

## Checks

Mechanical, run by `tests/check.js`, `tests/review.js`, `tests/v13.js` and `tests/v14.js` on this build:

- Exact FMA matched Python `math.fma` (glibc) on 200000 of 200000 triples.
- Exact constant-product rounding matched Python `Fraction` on 50,000 of 50,000 products; `0.1 * 3.0` gives `3fd3333333333334` the C way and `3fd3333333333333` the Go way.
- The bundled glibc pow matched the build machine's glibc 2.39 (FMA build) on 300,000 of 300,000 arguments.
- pow census in node 22: m53 9.52%, m23 10.13%, sq 0.07%, any 9.85% of 50,000 arguments differ from glibc, each by one unit in the last place. Chromium 153 agreed on every class but one (0.09%).
- Two-model toy: 0 of 1,440 steps differ with per-model state; 694 of 720 with file-scope state.
- Cast rules: every rule gives 899 at 899; at -3,000,000,000 each keeps its own out-of-range rule.
- `1e300 * 1e300` is refused as a Go constant; `1e400 * 1e-100` is Infinity in C and 1e300 in Go.
- Data completeness: 147 goal-language cells each with a wrap and a translate judgment; 7 extend judgments; 21 engines each with gate, speed basis, state and a gage.c:251 line; 12 SWMM6 ports with both gate results; 4 extended engines with off-switch and on-path evidence.
- Headless Chromium: every tab, three roads, three fleet families, both themes, 390 px width; no console error, no horizontal overflow.
- Contrast: 94 colour pairs at or above target in both themes.
- Re-run of 12 November 2026: see the table above. The app's published speed medians and ranges for C#, Python, TypeScript, Java, Go and Fortran equal those in swmm5-go `results/summary.json` to the digits shown; the generic-math control reproduced the repository's 43 models exactly.

Human review: one outside review of v1.1 (82/100, five findings, fixed in v1.2). No person has reviewed v1.3 or v1.4, and no person has repeated the re-run.

## What this does not show

- The re-run used the same kind of sandbox the ports were built in: the same compiler and interpreter versions (two patch levels differ for .NET), on x86-64 with FMA. It shows the commits rebuild and still match. It is not a test on other hardware, another libc or another compiler.
- In the re-run the six interpreters ran only the models EPA finishes quickly, so their longest models were not repeated. The README columns remain the repositories' own numbers.
- The re-run benchmark uses 12 short models; start-up time is inside every figure, which is most of what the JVM, .NET and interpreter figures on the smallest models measure.
- The OpenSWMM 6 ports and the four extended engines were not re-run.
- Byte identity is relative to the reference build above. On a CPU without FMA, EPA's own output changes on 43 of 480 models; which ports follow it there is now measured (the generic-math experiment above), by forcing glibc's generic routines on an FMA machine, not on a processor without FMA.
- Speed marked rough is not a benchmark. Benchmarks used short models (EPA 0.01 to 0.72 s) except Kotlin's six longer ones. No long continuous run was timed.
- For translator-built ports only the command line was gated; the stepping API is untested. 49 of the 480 gate decks stop on an input error.
- The OpenSWMM 6 family covers the 1D engine on one thread.
- The extended engines' new paths are judged by weaker tests than a byte gate; three have no reference engine.
- The 294 + 7 fit judgments are Claude's; the 175 added in v1.3 have had no human review.
- swmm5-infosewer is a private repository; it was read on 11 November 2026 while public for a day.

## How to reproduce

`node tests/check.js` (arithmetic and data), `node tests/review.js` , `node tests/v13.js` and `node tests/v14.js` (browser behaviour), `node tests/contrast.js` (colour). Fleet numbers: read the README of each repository at the commit in the tables. Re-run: clone a port and the corpus, build EPA with `make -C ref`, run `gate/make_ref.sh`, build the port as its README says, then `python3 gate/gate.py NAME "ENGINE COMMAND"`; the scripts used here (engine table, benchmark, second gate, collector) are in `tools_v14/` and `evidence/v14/`.

## Credits and licenses

- EPA SWMM 5.2.4: US EPA, public domain.
- OpenSWMM Engine: Copyright 2026 HydroCouple Developers, Apache-2.0. This product refers to software developed by the OpenSWMM authors (https://github.com/HydroCouple/openswmm.engine); none of it is included.
- The 36 engine repositories and the model corpus: Robert Dickinson, github.com/SWMMBobSWMM6.
- glibc pow: the GNU C Library authors, LGPL-2.1-or-later, translated by swmm5-typescript's tools/libm.
- gif.js 0.2.0 (Johan Nordberg, MIT), html2canvas 1.4.1 (Niklas von Hertzen, MIT). Fonts: IBM Plex, Source Serif 4 (OFL).

## AI use

Built with Claude, Anthropic's AI model, in October and November 2026, under the direction of Robert (Bob) Dickinson, who asked the question, supplied the earlier discussion and the outside review, and owns the engine repositories. Responsibility for the app is his. Claude read the repositories and copied their reported numbers; for v1.4 it cloned the 20 SWMM 5 ports, built them, ran the gates, the benchmark, the generic-math experiment and the probes, and read the 54 lessons; wrote the exact-arithmetic routines, the two-model toy, the figures, the page, the essay and this file; and wrote every fit judgment. The checks above are mechanical. No person has reviewed the fit judgments, the essay, the re-run, or whether a repository number has changed since the commits listed.

## Changes

- `1.4 (2026-11-12)`: deep dive. All 20 SWMM 5 ports rebuilt and re-run on the gate models; one interleaved benchmark for all 20; generic-math experiment; 24 probes; catalogue of 54 lessons; list of faults a passing gate did not show; Re-run tab, Re-run column on Fleet, figures 10 and 11.
- `1.3 (2026-11-11)`: 12 newer SWMM 5.2.4 ports (Zig, Pascal, Mojo, Kotlin, F#, Groovy, JavaScript, PHP, Ruby, Lua, Hy, Perl); OpenSWMM 6 family view (12 ports); third road, extend EPA's C (4 engines); speed basis shown; colour by runtime class; this file.
- `1.2 (2026-10-31)`: outside-review fixes. Fit depends on the road; wrapper claims name the reference build; cast table correct in range; invalid input clears exports; Go constant overflow is an error; benchmark scope beside each verdict.
- `1.1 (2026-10-30)`: renamed SWMM Engine What If.
- `1.0 (2026-10-30)`: first build, 9 engines, two roads.

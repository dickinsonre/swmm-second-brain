---
title: "S70: SWMM Engine What If, technical summary (app .md, v1.4)"
type: source
raw: raw/apps/swmm-engine-what-if-v1.4.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-14
tags: [apps, swmm5, swmm6, translation, verification, benchmarks]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary carried inside the SWMM Engine What If page, version 1.4. The app answers one question: to put SWMM into another language or change what it computes, what do I gain, what do I pay, and what evidence exists. Raw file: [raw/apps/swmm-engine-what-if-v1.4.md](../../raw/apps/swmm-engine-what-if-v1.4.md).

**How it got here.** Extracted byte for byte on 14 November 2026 from the `script#app-md` block of Bob's published artifact. Its front matter says "netlify: none yet"; a Netlify site does exist and serves v1.1 of 30 October 2026 (Q45).

**How it was written.** By Claude (Anthropic) in October and November 2026 under Bob's direction. For v1.4 Claude cloned the 20 SWMM 5 ports, built them, ran the gates, the benchmark and the probes, and wrote every fit judgment. One outside review of v1.1 gave 82/100. "No person has reviewed v1.3 or v1.4, and no person has repeated the re-run."

**Claims worth keeping**
- Three roads: wrap EPA's C, translate it, or extend it. 7 goals, 21 languages, 4 extended engines. 294 fit cells plus 7 for the extend road, each poor, fair or strong: "editorial judgment, not measurement".
- The app runs no SWMM engine. Its live calculations are demonstrations of floating-point and integer traps.
- The re-run of 12 November 2026, one machine (2-core Xeon with FMA and AVX2, Ubuntu 24.04, glibc 2.39): all 20 SWMM 5 translations rebuilt from their commits. Fourteen ran all 480 gate models and matched EPA on 480. Six interpreters ran reduced sets and matched on every model run: Python, Ruby, Hy and Perl 393 of 393; PHP and Lua 451 of 451.
- One interleaved benchmark for all 20, 12 models, median CPU ratio to EPA: C++ 0.94, Zig 1.033, Mojo 1.082, Rust 1.163, Fortran 1.281, Go 1.542, Pascal 1.59, C# 5.353, F# 6.79, Java 9.847, Kotlin 13.648, JavaScript 17.281, TypeScript 19.323, PHP 21.947, Groovy 22.974, Lua 47.401, Python 87.397, Hy 96.839, Ruby 101.653, Perl 249.478. EPA against itself: 1.005 (0.819 to 1.181). C++, Rust, Zig and Mojo fall inside EPA's own band.
- Against the READMEs: the 8 interleaved figures reproduced within 11 percent; the 5 "rough" figures came back 1.45 to 1.73 times higher.
- Generic-math experiment: with glibc forced to its non-FMA routines, EPA's output changes on 43 of 480 models. Following EPA to the generic answers: C++, Rust, Fortran, Zig, Pascal, Mojo, C#, F#, Python, PHP, Ruby, Lua, Hy, Perl. Keeping the FMA answers: Go, Java, Kotlin, Groovy, TypeScript, JavaScript.
- 24 language traps from the lessons were rerun as probes; 24 reproduced. 54 lessons catalogued.
- EPA's model state: file and program scope, 415 mutable variables, so one model per process. swmm5-cplus and swmm5-rust hold state per model.
- OpenSWMM 6 family, 12 translations at commit 88329d6: ten pass 480 of 480 and 452 of 452; Python 412 of 413 run and 450 of 452; Hy 478 of 480 and 450 of 452. Not re-run for this app.
- Four engines that extend EPA's C: swmm5-kw (622 lines added; 3,737 of 3,759 corpus models identical to stock with the option off), swmm524-perched (598 of 598 inputs identical with no SOIL2 line), swmm5-raspipe (median routing continuity error 0.795 % stock against 0.005 % on 1,600 models, at 2.6 times the run time; no comparison with HEC-RAS), swmm5-infosewer (on 71 models 11,408,158 of 11,894,156 values bit-identical to InfoSewer; the rest differ by at most 4.2e-11; private repository).
- Empty repositories when read on 11 November: swmm5-scala, swmm5-r, and eight swmm6 names (r, php, ruby, pascal, zig, perl, lua, mojo).
- Checks on the app's own arithmetic: exact FMA matched glibc on 200,000 of 200,000 triples; the bundled glibc `pow` matched on 300,000 of 300,000 arguments; a two-model toy differs on 694 of 720 steps with file-scope state and on 0 of 1,440 with per-model state.

**Limits it states.** The re-run used the same kind of sandbox the ports were built in, so it shows the commits rebuild and still match, not a test on other hardware. The benchmark uses 12 short models with start-up inside every figure. The SWMM6 ports and the extended engines were not re-run. Three of the four extended engines have no reference engine. The fit judgments are Claude's; 175 of them have had no human review.

**Checked at ingest.** 21 x 7 x 2 = 294. The fleet table has 20 translations and the SWMM6 table 12.

**Feeds:** [SWMM Engine What If (app)](../entities/swmm-engine-what-if.md), [Wrap, translate or extend](../concepts/wrap-translate-or-extend.md), [SWMM5 language translations](../entities/swmm5-language-ports.md), [SWMM6 language translations](../entities/swmm6-language-ports.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [EPA SWMM 5](../entities/swmm-5.md), [swmm524-perched](../entities/swmm524-perched.md).

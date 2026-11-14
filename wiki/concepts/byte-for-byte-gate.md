---
title: Byte-for-byte gate
type: concept
updated: 2026-11-14
sources: [S23, S28, S29, S30, S34, S35, S41, S70, S71]
tags: [verification, method, translation]
reviewed: no
---
The test every SWMM5 and SWMM6 translation is held to: run the translation and the original engine on the same decks and compare the files they write, byte for byte [S23](../sources/S23-swmm6-csharp-readme.md) [S41](../sources/S41-swmm5-go-readme.md).

**What passes** [S23](../sources/S23-swmm6-csharp-readme.md)
- The `.out` file is byte-identical to the reference's, when the reference writes one.
- The `.rpt` is identical after three lines are removed: "Analysis begun", "Analysis ended" and "Total elapsed time".
- The exit code is the same. SWMM6's command line exits nonzero when a model stops on an input error, so an input error must be caught the same way.

**For SWMM5** the reference is EPA SWMM 5.2.4 from the USEPA v5.2.4 tag, built with gcc 13.3 `-O2` and `_FORTIFY_SOURCE` off on x86-64 Linux with glibc 2.39. When an input error stops EPA before it writes results, the translation must not write a results file either; 49 of the 480 stop that way. "Nothing else is excused" [S41](../sources/S41-swmm5-go-readme.md). Controls and checked builds test the gate itself: see [What the gate cannot see](gate-blind-spots.md).

**For SWMM6 the reference.** The C++ engine built from the same commit and run on one thread (`OMP_NUM_THREADS=1`). Results with OpenMP threads "can differ in the last bits", so the parallel runs are not what is matched [S23](../sources/S23-swmm6-csharp-readme.md).

**The decks.** 480 models drawn from [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), and 452 extra decks: upstream's own test inputs and synthetic decks that reach the finite-volume solver, structure coupling, the newer hydrology and the input checks, which the corpus cannot reach [S23](../sources/S23-swmm6-csharp-readme.md).

**What counts as not run.** A model stopped at its time limit is "untested, not failed" [S28](../sources/S28-swmm6-python-readme.md). The Ruby port went one step further: for each stopped run it recorded how much of the `.out` was written and whether that much matched (from 53.6 % of the file down to 0.5 %, "next to no evidence"). No longer limit was tried [S35](../sources/S35-swmm6-ruby-readme.md).

**Rechecks.** Later ports added two: an independent rerun from a clean copy, with the engine regenerated and compared with the committed files before it is gated, and a second check from a clean clone on a random sample (seed 20261110) plus the three decks that SAVE and USE `cho.txt` [S30](../sources/S30-swmm6-kotlin-readme.md). Slow ports reran a sample instead of the full set [S34](../sources/S34-swmm6-hy-readme.md).

**A stronger form.** [swmm6-rust](../entities/swmm6-rust.md) adds a state gate: every member of the engine's context, dumped as hex bits after each routing step and compared, because "a float32 `.out` can hide" a difference. It also checks leaf functions against upstream's own code [S29](../sources/S29-swmm6-rust-readme.md).

**Where the verdicts can be read.** [SWMM Engines, Byte for Byte (app)](../entities/swmm-engines-byte-for-byte.md) stores every model's verdict and fingerprints for eight SWMM 5 translations [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md). All twenty were gated again on 12 November 2026 [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**What a pass does not show.** Agreement on models outside the 480 and the 452: "a feature no gate model or deck uses is untested" [S23](../sources/S23-swmm6-csharp-readme.md).

**Not in the sources.** That either engine is right: the gate compares the translation with the original, not with measurements or theory. And how this compares with the number-by-number scoring on [Verification against printed runs](verification-against-printed-runs.md), which allows a few digits of difference because the old machines rounded differently [S01](../sources/S01-swmm1-engine-app-md.md). A byte-for-byte gate is only possible when both engines run on the same arithmetic.

See [SWMM6 language translations](../entities/swmm6-language-ports.md), [Matching glibc math in a translation](glibc-math-in-translation.md), [Continuity is not validation](continuity-is-not-validation.md).

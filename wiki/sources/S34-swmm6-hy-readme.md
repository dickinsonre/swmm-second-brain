---
title: "S34: swmm6-hy, the OpenSWMM 6 1D engine in Hy (README)"
type: source
raw: raw/ports/2026-11-10-swmm6-hy-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-10
ingested: 2026-11-14
tags: [swmm6, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm6-hy, as published on 2026-11-10: a translation of the OpenSWMM 6 1D engine into Hy, "held to the same output as the C++ engine". It says of itself: "It is not SWMM6 and not a HydroCouple or EPA release; it is a translation checked against SWMM6." Raw file: [raw/ports/2026-11-10-swmm6-hy-README.md](../../raw/ports/2026-11-10-swmm6-hy-README.md).

**How it was written.** By Claude (Anthropic's AI model) for Bob: the README's AI-use section says the translators, the runtime, the gate and the notes are Claude's work, directed by Robert Dickinson, and that the engine is OpenSWMM's, translated mechanically. Every count below rests on this AI-written text and on the gate records it points to (`gate/evidence/`, one SHA-256 per `.out` and `.rpt`); no person has rechecked them.

**Claims worth keeping**
- 478 of 480 (`hy6_c01` to `hy6_c14`); `Hydrology/SCANLON.inp` and `EPA/72_H&H_Elements(2).inp` did not finish within 1,800 s ("untested, not failed"). 450 of 452 extra decks; `legacy_small.inp` and `refactored_small.inp` did not finish.
- Independent rerun of a sample (100 corpus models drawn from those that passed, the three `cho.txt` decks, 40 extra decks; "a sample, not the full set, because Hy runs at Python's speed"): 142 of 142. Main session's check 48 of 48 and 12 of 12.
- Method: the Python back end writes Python; `tools/cs2x/py2hy.py` writes each node of that Python syntax tree as the Hy 1.3.1 form that compiles back to it. `--check` compiles the Hy back and compares: engine 6,935 top-level statements, 0 differ.
- Math: CPython's `math` (glibc) plus ctypes calls into glibc at the GLIBC_2.29 symbol versions the C++ engine binds where CPython would decide a result itself. `crtmath.hy` is written by hand to match glibc on signalling NaNs.
- Needs CPython 3.13 and Hy 1.3.1. Median 2.38 s per model.

**Shared with every port README of this family**
- The reference is the C++ engine built from HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, run on one thread (`OMP_NUM_THREADS=1`).
- A model passes when its `.out` is byte-identical to the reference's, its `.rpt` is identical after removing "Analysis begun", "Analysis ended" and "Total elapsed time", and its exit code is the same.
- The 452 extra decks are the input files in the upstream `tests` folder at 88329d6 and the synthetic decks of swmm6-rust's gate (finite-volume solver, structure coupling, newer hydrology, input checks).
- Not shown: models outside the 480 and the 452; the reference's parallel runs (results with OpenMP threads can differ in the last bits); the 2D and other modules beyond the 1D engine.
- Times "were measured on a shared two-core cloud machine while other runs were going": a rough guide, not a benchmark.

**Feeds:** [SWMM6 language translations](../entities/swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

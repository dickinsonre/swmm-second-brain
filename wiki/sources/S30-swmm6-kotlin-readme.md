---
title: "S30: swmm6-kotlin, the OpenSWMM 6 1D engine in Kotlin (README)"
type: source
raw: raw/ports/2026-11-10-swmm6-kotlin-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-10
ingested: 2026-11-14
tags: [swmm6, translation, verification]
reviewed: no
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm6-kotlin, as published on 2026-11-10: a translation of the OpenSWMM 6 1D engine into Kotlin, "held to the same output as the C++ engine". It says of itself: "It is not SWMM6 and not a HydroCouple or EPA release; it is a translation checked against SWMM6." Raw file: [raw/ports/2026-11-10-swmm6-kotlin-README.md](../../raw/ports/2026-11-10-swmm6-kotlin-README.md).

**How it was written.** By Claude (Anthropic's AI model) for Bob: the README's AI-use section says the translators, the runtime, the gate and the notes are Claude's work, directed by Robert Dickinson, and that the engine is OpenSWMM's, translated mechanically. Every count below rests on this AI-written text and on the gate records it points to (`gate/evidence/`, one SHA-256 per `.out` and `.rpt`); no person has rechecked them.

**Claims worth keeping**
- 480 of 480 (`kt6_a`, `kt6_b`); 452 of 452 (`kt6_x_a`, `kt6_x_b`).
- Independent rerun from a clean `git archive`: translator rebuilt, engine regenerated from `cs/gen` and runtime from `java/src/cpp` (both byte-identical to the committed files), 480 of 480 (`kt6_v_a`, `kt6_v_b`).
- Main session's check from a clean `git clone`: 48 of 48 (45 corpus models drawn with seed 20261110 plus the three decks that SAVE and USE `cho.txt`) and 12 of 12 extra decks. In a second clean clone the math was regenerated from glibc 2.39's source, compiled to GIMPLE only, and came out identical.
- `tools/cs2x/Cs2Kotlin.cs` was begun from the Java translator. The runtime is the Java port's runtime translated into Kotlin by `kotlin/tools/J2Kt.java`; nothing of the Java port is on the class path.
- The 19 math functions are translated from GCC's compiled form of glibc 2.39 by `tools/libm/gim2x.py` (`Glibm*.kt`), LGPL 2.1 or later.
- Needs JDK 21 and Kotlin 2.0.21. Median 2.96 s per model.

**Shared with every port README of this family**
- The reference is the C++ engine built from HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, run on one thread (`OMP_NUM_THREADS=1`).
- A model passes when its `.out` is byte-identical to the reference's, its `.rpt` is identical after removing "Analysis begun", "Analysis ended" and "Total elapsed time", and its exit code is the same.
- The 452 extra decks are the input files in the upstream `tests` folder at 88329d6 and the synthetic decks of swmm6-rust's gate (finite-volume solver, structure coupling, newer hydrology, input checks).
- Not shown: models outside the 480 and the 452; the reference's parallel runs (results with OpenMP threads can differ in the last bits); the 2D and other modules beyond the 1D engine.
- Times "were measured on a shared two-core cloud machine while other runs were going": a rough guide, not a benchmark.

**Feeds:** [SWMM6 language translations](../entities/swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

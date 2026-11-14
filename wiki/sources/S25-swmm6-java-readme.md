---
title: "S25: swmm6-java, the OpenSWMM 6 1D engine in Java (README)"
type: source
raw: raw/ports/2026-11-04-swmm6-java-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-04
ingested: 2026-11-14
tags: [swmm6, translation, verification]
reviewed: no
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm6-java, as published on 2026-11-04: a translation of the OpenSWMM 6 1D engine into Java, "held to the same output as the C++ engine". It says of itself: "It is not SWMM6 and not a HydroCouple or EPA release; it is a translation checked against SWMM6." Raw file: [raw/ports/2026-11-04-swmm6-java-README.md](../../raw/ports/2026-11-04-swmm6-java-README.md).

**How it was written.** By Claude (Anthropic's AI model) for Bob: the README's AI-use section says the translators, the runtime, the gate and the notes are Claude's work, directed by Robert Dickinson, and that the engine is OpenSWMM's, translated mechanically. Every count below rests on this AI-written text and on the gate records it points to (`gate/evidence/`, one SHA-256 per `.out` and `.rpt`); no person has rechecked them.

**Claims worth keeping**
- 480 of 480 (`java2`); 452 of 452 (`java_x2`).
- `tools/cs2x/Cs2Java.cs` translates the C# through Roslyn (`java/gen`; mapping in `tools/cs2x/JAVA.md`). The runtime `java/src/cpp` specialises the primitive containers (`VecD`, `PtrI`, ...).
- Bit-exact translations of the 19 glibc math functions (`Glibm.java`, `Glibm2.java`), LGPL 2.1 or later; same million-argument test.
- Needs JDK 21. Median 1.92 s per model.

**Shared with every port README of this family**
- The reference is the C++ engine built from HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, run on one thread (`OMP_NUM_THREADS=1`).
- A model passes when its `.out` is byte-identical to the reference's, its `.rpt` is identical after removing "Analysis begun", "Analysis ended" and "Total elapsed time", and its exit code is the same.
- The 452 extra decks are the input files in the upstream `tests` folder at 88329d6 and the synthetic decks of swmm6-rust's gate (finite-volume solver, structure coupling, newer hydrology, input checks).
- Not shown: models outside the 480 and the 452; the reference's parallel runs (results with OpenMP threads can differ in the last bits); the 2D and other modules beyond the 1D engine.
- Times "were measured on a shared two-core cloud machine while other runs were going": a rough guide, not a benchmark.

**Feeds:** [SWMM6 language translations](../entities/swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

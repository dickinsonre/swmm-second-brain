---
title: "S24: swmm6-go, the OpenSWMM 6 1D engine in Go (README)"
type: source
raw: raw/ports/2026-11-04-swmm6-go-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-04
ingested: 2026-11-14
tags: [swmm6, translation, verification]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm6-go, as published on 2026-11-04: a translation of the OpenSWMM 6 1D engine into Go, "held to the same output as the C++ engine". It says of itself: "It is not SWMM6 and not a HydroCouple or EPA release; it is a translation checked against SWMM6." Raw file: [raw/ports/2026-11-04-swmm6-go-README.md](../../raw/ports/2026-11-04-swmm6-go-README.md).

**How it was written.** By Claude (Anthropic's AI model) for Bob: the README's AI-use section says the translators, the runtime, the gate and the notes are Claude's work, directed by Robert Dickinson, and that the engine is OpenSWMM's, translated mechanically. Every count below rests on this AI-written text and on the gate records it points to (`gate/evidence/`, one SHA-256 per `.out` and `.rpt`); no person has rechecked them.

**Claims worth keeping**
- 480 of 480 (`go5`); 452 of 452 (`go_x3`).
- `tools/cs2x/Cs2Go.cs` reads the C# engine through Roslyn's semantic model, one operation tree per method, and prints Go (`go/engine`); `go/cpp` is the runtime in Go.
- `go/glibm` holds bit-exact translations of 19 glibc math functions (`tools/libm`), tested against the system's glibc 2.39 on about a million arguments each, special values and NaN payloads included, with no difference: "a test, not a proof".
- The translated math stays under glibc's licence, LGPL 2.1 or later.
- Needs Go 1.24. Median 0.14 s per model (C#: 0.76 s).

**Shared with every port README of this family**
- The reference is the C++ engine built from HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, run on one thread (`OMP_NUM_THREADS=1`).
- A model passes when its `.out` is byte-identical to the reference's, its `.rpt` is identical after removing "Analysis begun", "Analysis ended" and "Total elapsed time", and its exit code is the same.
- The 452 extra decks are the input files in the upstream `tests` folder at 88329d6 and the synthetic decks of swmm6-rust's gate (finite-volume solver, structure coupling, newer hydrology, input checks).
- Not shown: models outside the 480 and the 452; the reference's parallel runs (results with OpenMP threads can differ in the last bits); the 2D and other modules beyond the 1D engine.
- Times "were measured on a shared two-core cloud machine while other runs were going": a rough guide, not a benchmark.

**Feeds:** [SWMM6 language translations](../entities/swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

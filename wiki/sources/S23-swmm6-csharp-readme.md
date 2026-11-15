---
title: "S23: swmm6-csharp, the OpenSWMM 6 1D engine in C# (README)"
type: source
raw: raw/ports/2026-11-04-swmm6-csharp-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-04
ingested: 2026-11-14
tags: [swmm6, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm6-csharp, as published on 2026-11-04: a translation of the OpenSWMM 6 1D engine into C#, "held to the same output as the C++ engine". It says of itself: "It is not SWMM6 and not a HydroCouple or EPA release; it is a translation checked against SWMM6." Raw file: [raw/ports/2026-11-04-swmm6-csharp-README.md](../../raw/ports/2026-11-04-swmm6-csharp-README.md).

**How it was written.** By Claude (Anthropic's AI model) for Bob: the README's AI-use section says the translators, the runtime, the gate and the notes are Claude's work, directed by Robert Dickinson, and that the engine is OpenSWMM's, translated mechanically. Every count below rests on this AI-written text and on the gate records it points to (`gate/evidence/`, one SHA-256 per `.out` and `.rpt`); no person has rechecked them.

**Claims worth keeping**
- 480 of 480 corpus models byte-identical (gate run `cs8`); 452 of 452 extra decks (`cs_x4`).
- The C++ engine was translated to C# first: `tools/cpp2x` reads clang's AST of every engine source file and writes C# (`cs/gen`). The other languages are translated from this C#, not from the C++.
- `cs/runtime` is the small C++ standard library the generated code calls, written to reproduce libstdc++ and glibc where the output depends on them (printf rounding, strtod, sscanf, hash-table node order, introsort swaps); `tests/` compares it case by case.
- Nothing in the generated engine is edited by hand.
- Needs the .NET 8 SDK. Median time per model in the gate run: 0.76 s, including .NET start-up and JIT compilation.
- The README does not say how the C# port reaches glibc's math.

**Shared with every port README of this family**
- The reference is the C++ engine built from HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, run on one thread (`OMP_NUM_THREADS=1`).
- A model passes when its `.out` is byte-identical to the reference's, its `.rpt` is identical after removing "Analysis begun", "Analysis ended" and "Total elapsed time", and its exit code is the same.
- The 452 extra decks are the input files in the upstream `tests` folder at 88329d6 and the synthetic decks of swmm6-rust's gate (finite-volume solver, structure coupling, newer hydrology, input checks).
- Not shown: models outside the 480 and the 452; the reference's parallel runs (results with OpenMP threads can differ in the last bits); the 2D and other modules beyond the 1D engine.
- Times "were measured on a shared two-core cloud machine while other runs were going": a rough guide, not a benchmark.

**Feeds:** [SWMM6 language translations](../entities/swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

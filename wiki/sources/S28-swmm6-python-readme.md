---
title: "S28: swmm6-python, the OpenSWMM 6 1D engine in Python (README)"
type: source
raw: raw/ports/2026-11-06-swmm6-python-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-06
ingested: 2026-11-14
tags: [swmm6, translation, verification]
reviewed: 2026-11-15
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm6-python, as published on 2026-11-06: a translation of the OpenSWMM 6 1D engine into Python, "held to the same output as the C++ engine". It says of itself: "It is not SWMM6 and not a HydroCouple or EPA release; it is a translation checked against SWMM6." Raw file: [raw/ports/2026-11-06-swmm6-python-README.md](../../raw/ports/2026-11-06-swmm6-python-README.md).

**How it was written.** By Claude (Anthropic's AI model) for Bob: the README's AI-use section says the translators, the runtime, the gate and the notes are Claude's work, directed by Robert Dickinson, and that the engine is OpenSWMM's, translated mechanically. Every count below rests on this AI-written text and on the gate records it points to (`gate/evidence/`, one SHA-256 per `.out` and `.rpt`); no person has rechecked them.

**Claims worth keeping**
- 412 of the 413 corpus models run are byte-identical (gate run `py2`). `EPA/72_H&H_Elements(2).inp` did not finish within 7,000 s ("untested, not failed"). The other 67 of the 480, the slowest for this port, were not run on this build: "stopped there by choice, not by a failure".
- 450 of 452 extra decks byte-identical (`py_x2`); `legacy_small.inp` and `refactored_small.inp` did not finish within the time limit (the limit for the extra decks is not stated).
- `tools/cs2x/Cs2Py.cs` writes `py/gen/engine.py` (mapping in `tools/cs2x/PY.md`); `py/cpp` is the runtime in Python. CPython's math module calls the system's glibc, so its results are glibc's.
- Needs CPython 3.13 and nothing else; no build step. Median 1.92 s per model.

**Shared with every port README of this family**
- The reference is the C++ engine built from HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, run on one thread (`OMP_NUM_THREADS=1`).
- A model passes when its `.out` is byte-identical to the reference's, its `.rpt` is identical after removing "Analysis begun", "Analysis ended" and "Total elapsed time", and its exit code is the same.
- The 452 extra decks are the input files in the upstream `tests` folder at 88329d6 and the synthetic decks of swmm6-rust's gate (finite-volume solver, structure coupling, newer hydrology, input checks).
- Not shown: models outside the 480 and the 452; the reference's parallel runs (results with OpenMP threads can differ in the last bits); the 2D and other modules beyond the 1D engine.
- Times "were measured on a shared two-core cloud machine while other runs were going": a rough guide, not a benchmark.

**Feeds:** [SWMM6 language translations](../entities/swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

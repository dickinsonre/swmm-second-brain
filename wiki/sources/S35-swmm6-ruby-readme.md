---
title: "S35: swmm6-ruby, the OpenSWMM 6 1D engine in Ruby (README)"
type: source
raw: raw/ports/2026-11-12-swmm6-ruby-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-14
tags: [swmm6, translation, verification]
reviewed: no
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm6-ruby, as published on 2026-11-12: a translation of the OpenSWMM 6 1D engine into Ruby, "held to the same output as the C++ engine". It says of itself: "It is not SWMM6 and not a HydroCouple or EPA release; it is a translation checked against SWMM6." Raw file: [raw/ports/2026-11-12-swmm6-ruby-README.md](../../raw/ports/2026-11-12-swmm6-ruby-README.md).

**How it was written.** By Claude (Anthropic's AI model) for Bob: the README's AI-use section says the translators, the runtime, the gate and the notes are Claude's work, directed by Robert Dickinson, and that the engine is OpenSWMM's, translated mechanically. Every count below rests on this AI-written text and on the gate records it points to (`gate/evidence/`, one SHA-256 per `.out` and `.rpt`); no person has rechecked them.

**Claims worth keeping**
- 478 of 480 (`rb6_c01` to `rb6_c06b`); `Hydrology/SCANLON.inp` and `EPA/72_H&H_Elements(2).inp` did not finish within 1,800 s. 450 of 452 extra decks; `legacy_small.inp` and `refactored_small.inp` did not finish.
- What the four stopped runs had written was identical to the reference: `SCANLON.inp` 42,334,342 of 78,975,850 bytes (53.6 %), `legacy_small.inp` 17,545,557 of 155,158,965 (11.3 %), `refactored_small.inp` 17,600,169 of 155,158,965 (11.3 %), `72_H&H_Elements(2).inp` 2,351 of 440,275 (0.5 %, "next to no evidence"). No longer limit was tried.
- The README says the Python port took 4,056 s on `SCANLON.inp` and did not finish the other three in 7,000 s.
- Independent rerun of a sample: 142 of 142 (`rb6_v_a`, `rb6_v_b`, `rb6_vx`). Main session's check 48 of 48 and 12 of 12.
- `tools/cs2x/Cs2Rb.cs`, begun from the Python back end, writes one Ruby file (`ruby/gen/engine.rb`); the runtime is written by hand from the Python port's. Math: MRI's `Math` where it calls glibc directly, glibc through Fiddle where MRI decides a result itself or has no function (`cbrt`, `expm1`, `log1p`, `fmod`, `remainder`, `nextafter`, `pow` of a negative base, `acos`, `asin` and the logarithms outside their domains).
- Needs Ruby 3.3 (run with 3.3.6, no YJIT); no build step. Median 2.89 s per model.

**Shared with every port README of this family**
- The reference is the C++ engine built from HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, run on one thread (`OMP_NUM_THREADS=1`).
- A model passes when its `.out` is byte-identical to the reference's, its `.rpt` is identical after removing "Analysis begun", "Analysis ended" and "Total elapsed time", and its exit code is the same.
- The 452 extra decks are the input files in the upstream `tests` folder at 88329d6 and the synthetic decks of swmm6-rust's gate (finite-volume solver, structure coupling, newer hydrology, input checks).
- Not shown: models outside the 480 and the 452; the reference's parallel runs (results with OpenMP threads can differ in the last bits); the 2D and other modules beyond the 1D engine.
- Times "were measured on a shared two-core cloud machine while other runs were going": a rough guide, not a benchmark.

**Feeds:** [SWMM6 language translations](../entities/swmm6-language-ports.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

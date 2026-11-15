---
title: "S65: World Rainfall Pattern Painter, technical summary (app .md, v3.2.0)"
type: source
raw: raw/apps/rain-canvas-studio-v2026.1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-14
tags: [apps, rainfall, design-storms, verification, lovable, icm, swmm5]
reviewed: 2026-11-15
---
**What it is.** The technical summary that ships with the World Rainfall Pattern Painter, version 3.2.0, a Lovable app at https://rain-canvas-studio.lovable.app. The app and its public API build synthetic design-storm hyetographs from a depth, a duration, a time step and a temporal pattern. Raw file: [raw/apps/rain-canvas-studio-v2026.1.2.md](../../raw/apps/rain-canvas-studio-v2026.1.2.md).

**The file name is wrong and the content is right.** The name says v2026.1.2, the version of another app. Until 14 November 2026 this file was a second copy of the Rules for Responsible Modeling summary ([S62](S62-rules-for-responsible-modeling-app-md.md)); Bob replaced its content that day with this summary. Its `file: rain-canvas-studio` line is this app's own identifier. See Q35 in [Open questions](../open-questions.md).

**How it was written.** By Lovable (the AI app builder) on 14 November 2026 from the source at commit bb672ea8, two fresh test runs, a measurement script and live API calls. It says it "removed unsupported review attribution" and marked missing evidence "not checked". It records no human check of the results or of the summary itself. It says Bob's task-by-task part in the development is not recorded in the project source.

**Claims worth keeping**
- 339 predefined patterns and 1 separate Custom editor. Another 234 old pattern IDs remain as aliases. The app catalogue and the API use one shared calculator and the same 339 IDs.
- Confidence registry: 3 High, 57 Medium, 279 Low. High is limited to the uniform block and SCS Types IA and II, the only patterns benchmarked against published ordinates. Euler Type II is Medium: its arrangement is checked against DWD KOSTRA examples, but its block heights use a generic curve.
- Checks, 14 November 2026: Vitest, 18 files, 1,496 passed; Deno live API tests, 1 file, 6 passed; total 19 files, 1,502 passed, 0 failed.
- Largest per-file counts: `coarseStorms` 1,017 (339 patterns at 3 coarse-step cases), `volumeConservation` 340, `exportReimport` 36, `singleInterval` 28 (over 9,153 generated cases), `methodFidelity` 18.
- Volume: over all 339 patterns the largest depth difference was 1.776e-15 in. Through the live API, with intensities rounded to 4 decimals, the largest was 0.0002 in (0.005 %), on the block pattern.
- A real API request, SCS Type II, 4.00 in (101.6 mm), 6 h, 15 min: 24 intervals totalling 4.0000 in, fallback "none".
- Defaults: 2.00 in (50.8 mm), 6 h, 15 min. US customary first.
- Method: intensity for an interval is the depth times the rise of the dimensionless mass curve over that interval, divided by the interval length. A raw series is accepted when every value is finite and non-negative and its depth is within 0.02 (relative) of the target; it is then rescaled to the exact depth. Otherwise the generator tries finer grids (240, 1,440, 6,000 substeps), then rescales what is positive, then falls back to a uniform storm. Each result carries a label: `none`, `depth_adjusted`, `single_interval`, `refined_grid`, `rescaled` or `uniform`.
- Fixed approximations it names: Chicago storm with peak position r = 0.4 and exponent 0.6, "not site IDF constants"; triangular peak at r = 0.33; Euler Type II peak at 0.3 of the duration with exponents 0.45 and 0.25, "a generic KOSTRA-like curve, not site KOSTRA data".
- Climate uplift: effective depth = depth times a factor. 19 factors in four sets: Singapore PUB 1.00, 1.12, 1.26, 1.40; UK FEH 1.00, 1.10, 1.20, 1.40 and an "upper end" of 1.20; Australian ARR 2019 1.00, 1.05, 1.09, 1.09, 1.16; Canadian CDA 1.00, 1.10, 1.15, 1.20, 1.30. "Transcribed from the app, not independently checked against the cited guidance."
- API limits: depth above 0 and up to 100 in, duration up to 72 h, time step 1 to 360 min.
- Exports: CSV, EPA SWMM, InfoWorks ICM (event CSV, type=RED), XP-SWMM, HEC-HMS. Export headers carry pattern, depth, duration, step, units, source, confidence and fallback. No import into any of the four desktop programs was checked by a person.
- An in-app Storm Assistant uses `google/gemini-3-flash-preview`. It and the NOAA IDF proxy have 0 test files.
- Review: a "method fidelity review" on 2026-11-02 graded B-; the reviewer and tool are not recorded.
- Versions: 1.0.0 on 2025-11-09 as Rainfall Pattern Painter; 2.0.0 on 2026-02-24, renamed World Rainfall Pattern Painter; 2.1.0 on 2026-02-27, public API; 2.3.0 on 2026-03-27, about 180 added storms; 2.4.0 on 2026-05-30, 38 added patterns; 3.0.1 on 2026-10-22, one shared calculator and 339-storm parity; 3.1.0 on 2026-11-01, source notes and confidence; 3.2.0 on 2026-11-02.
- License: MIT, Robert Dickinson.

**Limits it states.** A source note on a pattern "is not proof that its original table was read". 336 of 339 patterns are not High. "A single request or volume test does not validate the hydrologic suitability of a pattern for a particular site or regulatory requirement."

**Checked at ingest.** The per-file counts sum to 1,502. 3 + 57 + 279 = 339. 339 times 3 is 1,017 and 339 times 27 is 9,153. 4 in is 101.6 mm. Two things in the climate table do not sit right (Q43).

**Feeds:** [World Rainfall Pattern Painter (app)](../entities/world-rainfall-pattern-painter.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [InfoWorks ICM](../entities/infoworks-icm.md).

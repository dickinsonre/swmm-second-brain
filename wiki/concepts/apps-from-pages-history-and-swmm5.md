---
title: "Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5"
type: concept
updated: 2026-11-19
sources: [S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S384]
tags: [apps, swmm5, history, verification]
reviewed: no
---
Eighteen app summaries that Bob uploaded on 17 November 2026, on the history of SWMM and the insides of SWMM5. All eighteen were written by Claude (Anthropic) that day from the published pages, at Bob's request, with nothing rerun (Q108). Bob deployed all eighteen to Netlify the same day [S205](../sources/S205-note-netlify-addresses.md).

| App | Version | Date | Source |
|---|---|---|---|
| [The Runoff Block (app)](../entities/runoff-block.md) | 1.1 | 2026-11-03 | [S206](../sources/S206-runoff-block-summary.md) |
| [Visual SWMM (app)](../entities/visual-swmm.md) | 0.1.0 | 2026-11-14 | [S207](../sources/S207-visual-swmm-summary.md) |
| [SWMM Canon (app)](../entities/swmm-canon.md) | 1.4 | 2026-11-02 | [S208](../sources/S208-swmm-canon-summary.md) |
| [The Rigid Column Test (app)](../entities/rigid-column-test.md) | 2026-09-30 | 2026-09-30 | [S209](../sources/S209-rigid-column-test-summary.md) |
| [SWMM5 Implicit Box Solver Test Bench (app)](../entities/swmm5-implicit-box-bench.md) | 2026-10-02 | 2026-10-30 | [S210](../sources/S210-swmm5-implicit-box-bench-summary.md) |
| [SWMM5 Self-Regeneration (app)](../entities/swmm5-self-regeneration.md) | 1.0.0 | 2026-10-26 | [S211](../sources/S211-swmm5-self-regeneration-summary.md) |
| [SWMM5 Residual Walk (app)](../entities/swmm5-residual-walk.md) | 1.0 | 2026-11-04 | [S212](../sources/S212-swmm5-residual-walk-summary.md) |
| [Low-Spot Census (app)](../entities/low-spot-census.md) | 1.0 | 2026-11-05 | [S213](../sources/S213-low-spot-census-summary.md) |
| [Lead Pump Pointer (app)](../entities/lead-pump-pointer.md) | 1.1 | 2026-11-03 | [S214](../sources/S214-lead-pump-pointer-summary.md) |
| [SWMM Trouble Graph (app)](../entities/swmm-trouble-graph.md) | 1.3 | 2026-11-04 | [S215](../sources/S215-swmm-trouble-graph-summary.md) |
| [SWMM Rhythm Detector (app)](../entities/swmm-rhythm-detector.md) | 1.0 | 2026-11-06 | [S216](../sources/S216-swmm-rhythm-detector-summary.md) |
| [SWMM Run Supervisor (app)](../entities/swmm-run-supervisor.md) | 2026-10-24 | 2026-10-24 | [S217](../sources/S217-swmm-run-supervisor-summary.md) |
| [SWMM Claim Frontier (app)](../entities/swmm-claim-frontier.md) | 1.0 | 2026-09-30 | [S218](../sources/S218-swmm-claim-frontier-summary.md) |
| [SWMM Clean Repro (app)](../entities/swmm-clean-repro.md) | 1.0 | 2026-10-13 | [S219](../sources/S219-swmm-clean-repro-summary.md) |
| [swmm5-rs Side by Side (app)](../entities/swmm5-rs-side-by-side.md) | 1.2 | 2026-10-19 | [S220](../sources/S220-swmm5-rs-side-by-side-summary.md) |
| [swmm5-rust in RustGIS (app)](../entities/swmm5-rust-rustgis.md) | 0.1.0 | 2026-11-01 | [S221](../sources/S221-swmm5-rust-rustgis-summary.md) |
| [SWMM5+ Bench (app)](../entities/swmm5plus-bench.md) | 1.0 | 2026-10-24 | [S222](../sources/S222-swmm5plus-bench-summary.md) |
| [SWMM5+ Branch Atlas (app)](../entities/swmm5plus-branch-atlas.md) | 2026-10-26 | 2026-10-26 | [S223](../sources/S223-swmm5plus-branch-atlas-summary.md) |

Since then: Visual SWMM 0.1.1 (19 November 2026) fits a 390 px phone screen; nothing else changed [S384](../sources/S384-visual-swmm-summary-v0-1-1.md).

**What runs.** Nine run an engine in the page, EPA SWMM 5.2.4 compiled to WebAssembly in each: [The Runoff Block (app)](../entities/runoff-block.md), [SWMM5 Implicit Box Solver Test Bench (app)](../entities/swmm5-implicit-box-bench.md), [SWMM5 Self-Regeneration (app)](../entities/swmm5-self-regeneration.md), [SWMM5 Residual Walk (app)](../entities/swmm5-residual-walk.md), [Lead Pump Pointer (app)](../entities/lead-pump-pointer.md), [SWMM Run Supervisor (app)](../entities/swmm-run-supervisor.md), [SWMM Clean Repro (app)](../entities/swmm-clean-repro.md), [swmm5-rust in RustGIS (app)](../entities/swmm5-rust-rustgis.md) and [SWMM5+ Bench (app)](../entities/swmm5plus-bench.md). The others read files, show recorded runs, or measure source code.

**Browser against native.** Six report the same check with different results: 36 of 36 inputs byte-identical [S206](../sources/S206-runoff-block-summary.md), 16 of 16 against a musl build [S210](../sources/S210-swmm5-implicit-box-bench-summary.md), 46 of 60 [S211](../sources/S211-swmm5-self-regeneration-summary.md), 89 of 100 [S212](../sources/S212-swmm5-residual-walk-summary.md), 32 of 33 [S222](../sources/S222-swmm5plus-bench-summary.md), and one model of 2,661,597 bytes [S214](../sources/S214-lead-pump-pointer-summary.md). See [WebAssembly builds against native builds](wasm-against-native-builds.md).

**Findings in EPA's code, at the pages' word.** "All links are stable." printed when the least stable link is the first in the file, report.c line 994 [S216](../sources/S216-swmm-rhythm-detector-summary.md); a seconds-to-int conversion C leaves undefined, gage.c:251 [S220](../sources/S220-swmm5-rs-side-by-side-summary.md); a run that ends with no error at -11,199 % continuity when the last link at a free outfall is 0.073 ft long [S212](../sources/S212-swmm5-residual-walk-summary.md). None has been checked by a person.

**Results that went against the app.** The SWMM Trouble Graph did not beat the right single report list on 296 planted errors [S215](../sources/S215-swmm-trouble-graph-summary.md). The Run Supervisor quotes no live Claude run, and its rules were written with hindsight on one storm [S217](../sources/S217-swmm-run-supervisor-summary.md).

**Reviews.** Two were graded by an outside review before a revision, 75 of 100 [S206](../sources/S206-runoff-block-summary.md) and 77 of 100 [S214](../sources/S214-lead-pump-pointer-summary.md); the second review was itself AI-assisted. Others were reviewed by an OpenAI model [S215](../sources/S215-swmm-trouble-graph-summary.md) or a second Claude agent [S221](../sources/S221-swmm5-rust-rustgis-summary.md). Four say no person has reviewed them [S206](../sources/S206-runoff-block-summary.md) [S207](../sources/S207-visual-swmm-summary.md) [S212](../sources/S212-swmm5-residual-walk-summary.md) [S213](../sources/S213-low-spot-census-summary.md). Three pages carry no AI-use note [S209](../sources/S209-rigid-column-test-summary.md) [S218](../sources/S218-swmm-claim-frontier-summary.md) [S219](../sources/S219-swmm-clean-repro-summary.md).

See [SWMM5+ (CIMM finite-volume engine)](../entities/swmm5plus.md), [The SWMM findings register](findings-register.md), [Byte-for-byte gate](byte-for-byte-gate.md).

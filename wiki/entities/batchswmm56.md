---
title: BatchSWMM56 (app)
type: entity
updated: 2026-11-15
sources: [S23, S117, S119]
tags: [apps, replit, swmm5, swmm6, engines, wasm, comparison]
reviewed: no
---
Bob's Replit app BatchSWMM56: an app that runs SWMM input models singly or in batches through several engines and compares status, continuity, flooding, flows, timing and time series. Version 1.1.0, at `batch-swmm-runner-robertdickinson.replit.app` [S117](../sources/S117-batchswmm56-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S117](../sources/S117-batchswmm56-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S117](../sources/S117-batchswmm56-replit-summary.md)
- Seven engine entries: EPA SWMM 5.2.4 as a native executable and API; SWMM5 WASM 5.2.4; SWMM5 Extended, the 5.2.4 KW/SF extension, on EPA base commit `7952ca837988b1c32f791812eccc9fd64547e093`; OWA SWMM of the 5.1 lineage (MIT); SWMM6 stable 6.0.0-alpha.4 at commit `9976efc815d5242e52a07a9d7c799e535b65fcaa` (Apache-2.0); SWMM6 develop 6.0.0-alpha.3 at commit `19a1bc42074eac8cdf46e2edafe6fc5849adf6da` (MIT); and Hydra 12.1.0 from neeraip/hydra at commit `2a75372531b981c3a8f6668cbb846a0366cf062d` (AGPL-3.0).
- The commits of the EPA native engine, the SWMM5 WASM engine and OWA SWMM are given as unknown.
- Six browser engine records and one native bundle record. The native bundle runs as an executable or, through Koffi, as an API.
- `npm test` exited with status 1. Vitest: 549 tests passed and 1 failed of 550; 57 test files passed and 1 failed of 58. The failure is `tests/hydraEngine.test.ts:110`, `ReferenceError: performance is not defined` in the worker's VM test context.
- 113 `.inp` sample files and eight page routes; `curl` got HTTP 200 from all eight on the development preview.
- ReSWMM estimates wave celerity as `c = sqrt(g * hydraulicDiameter)`, with gravity 32.174 ft/s² for US models, and splits a conduit into `max(1, ceil(length / targetLength))` segments.
- Comparison statistics use Bland-Altman: bias is the average difference and the agreement limits are `bias +/- 1.96 * sampleSD`.
- The Extended engine's KW/SF allocation and loop iteration do not provide dynamic wave backwater or pressure physics.
- Timing comparisons have different engine and machine boundaries; the file says no universal speed ranking follows.
- It calls OpenAI's `gpt-4o` for report discussion. Application license MIT. ReSWMM is credited to the ecotecnologias/ReSWMM project.

**What it does not show.** Browser rendering and the interactive workflows were not checked; the page checks were server responses only. TypeScript and production-build checks were not run in this inspection. No independent hydraulic validation and no run of every sample model. Source-to-binary reproducibility of the engines was not checked. [S117](../sources/S117-batchswmm56-replit-summary.md)

**Noted at ingest.** The EPA base commit `7952ca837988b1c32f791812eccc9fd64547e093` is the same one [S119](../sources/S119-code-rosetta-stone-replit-summary.md) pins as its EPA reference. The SWMM6 stable commit here is not the `88329d6` that the swmm6 translations start from [S23](../sources/S23-swmm6-csharp-readme.md); both are called 6.0.0-alpha.4 (Q79).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [EPA SWMM 5](swmm-5.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

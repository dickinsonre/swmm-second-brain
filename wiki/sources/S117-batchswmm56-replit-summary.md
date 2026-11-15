---
title: "S117: BatchSWMM56, summary written by Replit Agent (v1.1.0)"
type: source
raw: raw/apps/batch-swmm-runner-robertdickinson-v1.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-09-12
ingested: 2026-11-15
tags: [apps, replit, swmm5, swmm6, engines, wasm, comparison]
reviewed: no
---
**What it is.** A technical summary of BatchSWMM56, version 1.1.0: an app that runs SWMM input models singly or in batches through several engines and compares status, continuity, flooding, flows, timing and time series. It is one of Bob's Replit apps, at `batch-swmm-runner-robertdickinson.replit.app`. Raw file: [raw/apps/batch-swmm-runner-robertdickinson-v1.1.0.md](../../raw/apps/batch-swmm-runner-robertdickinson-v1.1.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the code and documentation do not establish a tool-by-tool implementation history. The copy here was read out of the editor of the Replit project named BatchSWMMRunner on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** Browser rendering and the interactive workflows were not checked; the page checks were server responses only. TypeScript and production-build checks were not run in this inspection. No independent hydraulic validation and no run of every sample model. Source-to-binary reproducibility of the engines was not checked.

**Checked at ingest.** The EPA base commit `7952ca837988b1c32f791812eccc9fd64547e093` is the same one [S119](S119-code-rosetta-stone-replit-summary.md) pins as its EPA reference. The SWMM6 stable commit here is not the `88329d6` that the swmm6 translations start from [S23](S23-swmm6-csharp-readme.md); both are called 6.0.0-alpha.4 (Q79).

**Feeds:** [BatchSWMM56 (app)](../entities/batchswmm56.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [EPA SWMM 5](../entities/swmm-5.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

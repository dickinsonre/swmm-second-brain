---
title: SWMM5 Lego Model (app)
type: entity
updated: 2026-11-15
sources: [S99]
tags: [apps, replit, swmm5, wasm, teaching]
reviewed: no
---
Bob's Replit app SWMM5 Lego Model: an app in which the user paints surfaces, nodes and links on a grid, picks a storm, and runs the layout either in a simplified JavaScript simulation or in EPA SWMM5 compiled to WebAssembly. Version 0.0.0, at `swmm-lego-model.replit.app` [S99](../sources/S99-swmm5-lego-model-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S99](../sources/S99-swmm5-lego-model-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S99](../sources/S99-swmm5-lego-model-replit-summary.md)
- Two engines: Quick Sim, in `hydraulics.js`, and EPA SWMM5 5.2.4 as WebAssembly, whose upstream commit and license are not recorded.
- Quick Sim uses a Curve Number equation with `S = 1000/CN - 10` and `Ia = 0.2 × S`, Manning-based flow, and a route timestep of 15 seconds. The summary says it is not the EPA engine's dynamic-wave calculation.
- 54 built-in storm profiles, 5 of them marked continuous, and 13 demo models.
- Tests: 79 passed, 0 failed, in 6 unit-test files.
- Named model slots are limited to 5 and kept in the browser's `localStorage`.
- The editor works in US customary units or SI.
- It downloads `.INP`, `.JSON`, `.CSV`, an `.HTML` graph report and the engine's `.RPT`.

**What it does not show.** Quick Sim was not compared with EPA SWMM5. The tests did not run an end-to-end simulation or exercise import and export in the browser. Only the tutorial screen was loaded. [S99](../sources/S99-swmm5-lego-model-replit-summary.md)

**Noted at ingest.** The version is 0.0.0 although the change list records the app being published on 25 March 2026 (Q68).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [EPA SWMM 5](swmm-5.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

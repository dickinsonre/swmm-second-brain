---
title: "S99: SWMM5 Lego Model, summary written by Replit Agent (v0.0.0)"
type: source
raw: raw/apps/swmm-lego-model-v0.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, wasm, teaching]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 Lego Model, version 0.0.0: an app in which the user paints surfaces, nodes and links on a grid, picks a storm, and runs the layout either in a simplified JavaScript simulation or in EPA SWMM5 compiled to WebAssembly. It is one of Bob's Replit apps, at `swmm-lego-model.replit.app`. Raw file: [raw/apps/swmm-lego-model-v0.0.0.md](../../raw/apps/swmm-lego-model-v0.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says no project record names the AI tools used to build it. The copy here was read out of the editor of the Replit project named SWMM Lego Model on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Two engines: Quick Sim, in `hydraulics.js`, and EPA SWMM5 5.2.4 as WebAssembly, whose upstream commit and license are not recorded.
- Quick Sim uses a Curve Number equation with `S = 1000/CN - 10` and `Ia = 0.2 × S`, Manning-based flow, and a route timestep of 15 seconds. The summary says it is not the EPA engine's dynamic-wave calculation.
- 54 built-in storm profiles, 5 of them marked continuous, and 13 demo models.
- Tests: 79 passed, 0 failed, in 6 unit-test files.
- Named model slots are limited to 5 and kept in the browser's `localStorage`.
- The editor works in US customary units or SI.
- It downloads `.INP`, `.JSON`, `.CSV`, an `.HTML` graph report and the engine's `.RPT`.

**Limits it states.** Quick Sim was not compared with EPA SWMM5. The tests did not run an end-to-end simulation or exercise import and export in the browser. Only the tutorial screen was loaded.

**Checked at ingest.** The version is 0.0.0 although the change list records the app being published on 25 March 2026 (Q68).

**Feeds:** [SWMM5 Lego Model (app)](../entities/swmm5-lego-model.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [EPA SWMM 5](../entities/swmm-5.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

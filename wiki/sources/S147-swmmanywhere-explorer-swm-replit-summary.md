---
title: "S147: SWMManywhere Explorer (swm-explorer), summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swm-explorer-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmmanywhere, model-generation, wasm]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMManywhere Explorer (swm-explorer), version 1.0.0: an app that explains the SWMManywhere workflow, sends a bounding box to a Python backend that runs SWMManywhere 0.1.17 to generate an urban drainage model, and runs `.inp` files in a SWMM5 engine compiled to WebAssembly in the browser. It is one of Bob's Replit apps, at `swm-explorer.replit.app`. Raw file: [raw/apps/swm-explorer-v1.0.0.md](../../raw/apps/swm-explorer-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the project records do not identify an AI tool used to build it; Git attributes 37 commits to Robert Dickinson. The copy here was read out of the editor of the Replit project named SWMManywhere-App on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Two `engines:` entries: SWMManywhere 0.1.17, an installed Python package with a BSD License classifier, and an EPA SWMM5 WebAssembly engine whose version was not checked. No commit is recorded for either.
- The backend estimates box width as `abs(east - west) * 111 * abs(cos(mid-latitude))` kilometers and height as `abs(north - south) * 111` kilometers, and rejects boxes wider or taller than 10 km.
- Rainfall depth in millimeters becomes precipitation in meters per hour as `depth_mm / 1000 / (duration_min / 60)`. Rainfall can follow uniform, triangular, Chicago or SCS Type II distributions.
- Quick Mode writes a constant-value raster with elevation `100.0` and a default slope of `0.005`; it is a flat DEM, not terrain sampled for the selected area.
- The network quality score is a heuristic of five checks, each scored out of 20, not an independent hydraulic validation.
- The what-if analysis runs six scenarios with depth multipliers `0.54`, `0.75`, `1.00`, `1.25`, `1.50` and `1.79`, the UI's configured factors, not verified return-period estimates.
- Job metadata and results go to SQLite; records older than 24 hours are removed when the store initializes.
- 247 city presets, 8 pipeline stages, 19 graph-function catalog entries, 6 parameter sensitivity records and 4 validation city records; eight tab views.
- `npm run build` passed. `npm run check` failed with one TypeScript error. No test script. `GET /api/swm/health` returned HTTP 200.
- It cites the 2025 SWMManywhere paper by Dobson, Jovanovic, Alonso-Álvarez and Chegini. `package.json` declares MIT. `units: SI`.

**Limits it states.** No model-generation job or SWMM simulation was run, so the checks do not establish hydraulic validity. The tab views, downloads and failure cases were not checked, and the production app was not loaded. The WASM engine's runtime version was not checked.

**Checked at ingest.** It carries the same app name as the [SWMManywhere Explorer (app)](../entities/swmmanywhere-explorer.md) [S122](S122-swmmanywhere-explorer-replit-summary.md), but a different `file:`, swm-explorer against swmmanywhere-explorer, and it runs engines where that one gives `engines: none` (Q77). The manifest keeps them as two apps. The `date:` is the day of the summary; the change list runs from 6 to 8 March 2026 (Q75). Neither engine commit is recorded (Q79).

**Feeds:** [SWMManywhere Explorer at swm-explorer (app)](../entities/swmmanywhere-explorer-swm.md), [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [SWMManywhere Explorer (app)](../entities/swmmanywhere-explorer.md).

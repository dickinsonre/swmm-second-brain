---
title: "SWMManywhere Explorer at swm-explorer (app)"
type: entity
updated: 2026-11-15
sources: [S122, S147]
tags: [apps, replit, swmmanywhere, model-generation, wasm]
reviewed: 11/16/2026
---
Bob's Replit app SWMManywhere Explorer (swm-explorer): an app that explains the SWMManywhere workflow, sends a bounding box to a Python backend that runs SWMManywhere 0.1.17 to generate an urban drainage model, and runs `.inp` files in a SWMM5 engine compiled to WebAssembly in the browser. Version 1.0.0, at `swm-explorer.replit.app` [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md)
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

**What it does not show.** No model-generation job or SWMM simulation was run, so the checks do not establish hydraulic validity. The tab views, downloads and failure cases were not checked, and the production app was not loaded. The WASM engine's runtime version was not checked. [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md)

**Noted at ingest.** It carries the same app name as the [SWMManywhere Explorer (app)](swmmanywhere-explorer.md) [S122](../sources/S122-swmmanywhere-explorer-replit-summary.md), but a different `file:`, swm-explorer against swmmanywhere-explorer, and it runs engines where that one gives `engines: none` (Q77). The manifest keeps them as two apps. The `date:` is the day of the summary; the change list runs from 6 to 8 March 2026 (Q75). Neither engine commit is recorded (Q79).

See [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [SWMManywhere Explorer (app)](swmmanywhere-explorer.md).

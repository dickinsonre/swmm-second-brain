---
title: Green-Ampt Infiltration Calculator (app)
type: entity
updated: 2026-11-15
sources: [S107]
tags: [apps, replit, hydrology, infiltration, green-ampt, horton, curve-number]
reviewed: no
---
Bob's Replit app Green-Ampt Infiltration Calculator: a browser calculator that estimates infiltration and runoff from soil, rainfall and storm-duration inputs by four methods. Version 1.0.0, at `green-infiltration--robertdickinson.replit.app` [S107](../sources/S107-green-ampt-calculator-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S107](../sources/S107-green-ampt-calculator-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S107](../sources/S107-green-ampt-calculator-replit-summary.md)
- Four methods, Green-Ampt, Modified Green-Ampt, Horton and SCS Curve Number, run in the app's own TypeScript with a default timestep of `0.1` hours. The app describes them as SWMM5 methods; no SWMM engine is invoked.
- Green-Ampt starts cumulative infiltration `F` at `0.001` and computes capacity as `f = K * (1 + suctionHead * initialDeficit / F)`.
- Curve Number uses `S = 1000 / CN - 10`.
- 8 built-in scenarios, 6 soil presets and 13 rainfall distributions.
- Read from the code and not tested: the metric selector changes labels, but Green-Ampt and Horton inputs are not converted.
- Read from the code and not tested: the Modified Green-Ampt branch records cumulative infiltration before adding the timestep's infiltration, so the series may lag by one timestep.
- Read from the code and not tested: the Curve Number branch does not add rainfall to `cumulativeRainfall`, from which the returned total rainfall is taken.
- Horton has no rainfall input, and its calculation writes zero runoff.
- `npm run check` passed. There is no test script: 0 tests ran.

**What it does not show.** Interactive controls, exports, presets and comparisons were not exercised. Numerical agreement with EPA SWMM was not checked. The date in the front matter is the inspection date, not a release date. [S107](../sources/S107-green-ampt-calculator-replit-summary.md)

**Noted at ingest.** The three readings of the code are Replit Agent's. The file gives them no status beyond "not tested"; they are unconfirmed here (Q69).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [Infiltration methods](../concepts/infiltration-methods.md), [SWMM5 Runoff and Infiltration (app)](swmm5-runoff-and-infiltration.md).

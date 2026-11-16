---
title: "S107: Green-Ampt Infiltration Calculator, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/green-infiltration-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, hydrology, infiltration, green-ampt, horton, curve-number]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of Green-Ampt Infiltration Calculator, version 1.0.0: a browser calculator that estimates infiltration and runoff from soil, rainfall and storm-duration inputs by four methods. It is one of Bob's Replit apps, at `green-infiltration--robertdickinson.replit.app`. Raw file: [raw/apps/green-infiltration-v1.0.0.md](../../raw/apps/green-infiltration-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says no AI tool is identified in the inspected project records. The copy here was read out of the editor of the Replit project named Green Infiltration on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Four methods, Green-Ampt, Modified Green-Ampt, Horton and SCS Curve Number, run in the app's own TypeScript with a default timestep of `0.1` hours. The app describes them as SWMM5 methods; no SWMM engine is invoked.
- Green-Ampt starts cumulative infiltration `F` at `0.001` and computes capacity as `f = K * (1 + suctionHead * initialDeficit / F)`.
- Curve Number uses `S = 1000 / CN - 10`.
- 8 built-in scenarios, 6 soil presets and 13 rainfall distributions.
- Read from the code and not tested: the metric selector changes labels, but Green-Ampt and Horton inputs are not converted.
- Read from the code and not tested: the Modified Green-Ampt branch records cumulative infiltration before adding the timestep's infiltration, so the series may lag by one timestep.
- Read from the code and not tested: the Curve Number branch does not add rainfall to `cumulativeRainfall`, from which the returned total rainfall is taken.
- Horton has no rainfall input, and its calculation writes zero runoff.
- `npm run check` passed. There is no test script: 0 tests ran.

**Limits it states.** Interactive controls, exports, presets and comparisons were not exercised. Numerical agreement with EPA SWMM was not checked. The date in the front matter is the inspection date, not a release date.

**Checked at ingest.** The three readings of the code are Replit Agent's. The file gives them no status beyond "not tested"; they are unconfirmed here (Q69).

**Feeds:** [Green-Ampt Infiltration Calculator (app)](../entities/green-ampt-infiltration-calculator.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [Infiltration methods](../concepts/infiltration-methods.md), [SWMM5 Runoff and Infiltration (app)](../entities/swmm5-runoff-and-infiltration.md).

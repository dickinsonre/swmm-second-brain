---
title: "BlueSky-ICM (app)"
type: entity
updated: 2026-11-18
sources: [S328]
tags: [apps, swmm5, wasm, report-parsing, flooding]
reviewed: no
---
Bob's app BlueSky-ICM: five blue-sky tools for SWMM5 and ICM on EPA SWMM 5.2.4 in the browser. Version 1.0.0, 2026-10-21 [S328](../sources/S328-bluesky-icm-summary.md). Its `links:` line names no live Netlify address [S328](../sources/S328-bluesky-icm-summary.md).

**A caution about its source.** The page ships no technical summary. [S328](../sources/S328-bluesky-icm-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S328](../sources/S328-bluesky-icm-summary.md)
- One HTML file holding the five tools of Bob's Lovable bluesky-scaffolder (ModelDiff, RainLab, CalibrationCopilot, FloodLens, ScenarioStudio) with EPA SWMM 5.2.4 compiled to WebAssembly underneath all five. The scaffolder's Lite engine stays beside the real one as a foil, with its units corrected.
- The scaffolder's report readers were wrong as shipped: its continuity regex captured the dot leaders, so every report read 0.00% (the demo reads -0.033 and -0.041%), and its node flooding parser counted days and hh:mm as one token, so flood volume read 0. The wasm engine's .out is byte-identical (168,018 bytes) and its .rpt line-identical to a native gcc build on both demo models.
- Library suite in Node on real engine output: 34 passed, 0 failed (engine identity, report and .out readers against printed values, all 12 node depth maxima equal to the report's Reported Max Depth, the diff, the storm tables, the Lite engine).
- Engine identity: return code, version 52004, .rpt line-identical and .out byte-identical to a native gcc build on both demo models.
- Headless Chromium 1194, 2026-10-21: all eight tabs and every tool run in both themes, 0 console errors, no text below WCAG contrast targets, no horizontal scroll at 375 px; theme changes no computed number; worker and main-thread paths give the same 82.06 cfs outfall peak.
- The Huff table checked against ISWS Circular 173 and the hazard thresholds against the Defra/EA 2008 note. The NRCS Type II table was not checked row by row.

**How to use it, as the summary puts it.** Use it to try the five ideas on a real engine with two scripted demo models. Ponded depth is a 1D stand-in for surface depth, the damage and cost numbers are assumptions, and nothing reads InfoWorks ICM networks despite the name. [S328](../sources/S328-bluesky-icm-summary.md)

**What it does not show.** As the page lists it: ponded depth at a node is a 1D stand-in for surface depth; velocity, the damage curve and every capex number are assumptions; synthetic gauges come from the model itself; the copilot is a local search; nothing reads InfoWorks ICM networks. [S328](../sources/S328-bluesky-icm-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md).

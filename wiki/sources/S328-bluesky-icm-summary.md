---
title: "S328: BlueSky-ICM, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/bluesky-icm-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-21
ingested: 2026-11-18
tags: [apps, swmm5, wasm, report-parsing, flooding]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app BlueSky-ICM, version 1.0.0: five blue-sky tools for SWMM5 and ICM on EPA SWMM 5.2.4 in the browser. Raw file: [raw/apps/bluesky-icm-v1.0.0.md](../../raw/apps/bluesky-icm-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/K1JHyyGw9KtiesAufdFs2m, version 1792639915-3de0 (index.html, 1,833,843 bytes, SHA-256 4f6fc096db59cca71bf4d84107f4b325ea8a49d675a63db5e3fbb91cdb821b8f), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who wrote the original scaffolder, asked for this app and is responsible for it."

**Claims worth keeping** (all copied from the file)
- One HTML file holding the five tools of Bob's Lovable bluesky-scaffolder (ModelDiff, RainLab, CalibrationCopilot, FloodLens, ScenarioStudio) with EPA SWMM 5.2.4 compiled to WebAssembly underneath all five. The scaffolder's Lite engine stays beside the real one as a foil, with its units corrected.
- The scaffolder's report readers were wrong as shipped: its continuity regex captured the dot leaders, so every report read 0.00% (the demo reads -0.033 and -0.041%), and its node flooding parser counted days and hh:mm as one token, so flood volume read 0. The wasm engine's .out is byte-identical (168,018 bytes) and its .rpt line-identical to a native gcc build on both demo models.
- Library suite in Node on real engine output: 34 passed, 0 failed (engine identity, report and .out readers against printed values, all 12 node depth maxima equal to the report's Reported Max Depth, the diff, the storm tables, the Lite engine).
- Engine identity: return code, version 52004, .rpt line-identical and .out byte-identical to a native gcc build on both demo models.
- Headless Chromium 1194, 2026-10-21: all eight tabs and every tool run in both themes, 0 console errors, no text below WCAG contrast targets, no horizontal scroll at 375 px; theme changes no computed number; worker and main-thread paths give the same 82.06 cfs outfall peak.
- The Huff table checked against ISWS Circular 173 and the hazard thresholds against the Defra/EA 2008 note. The NRCS Type II table was not checked row by row.

**Limits it states.** As the page lists it: ponded depth at a node is a 1D stand-in for surface depth; velocity, the damage curve and every capex number are assumptions; synthetic gauges come from the model itself; the copilot is a local search; nothing reads InfoWorks ICM networks.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [BlueSky-ICM (app)](../entities/bluesky-icm.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md).

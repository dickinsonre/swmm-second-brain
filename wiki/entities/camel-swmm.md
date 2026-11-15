---
title: Camel_SWMM (app)
type: entity
updated: 2026-11-15
sources: [S100, S103]
tags: [apps, replit, swmm5, pyswmm, ai-agents]
reviewed: no
---
Bob's Replit app Camel_SWMM: a Flask web app, with a Tkinter desktop path, for managing SWMM input files, validating them, running EPA SWMM and inspecting the results. Version 1.0.0, at `swmm-pilot-robertdickinson.replit.app` [S100](../sources/S100-camel-swmm-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S100](../sources/S100-camel-swmm-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S100](../sources/S100-camel-swmm-replit-summary.md)
- The engine is called through `swmm.toolkit.solver.swmm_run`, from swmm-toolkit 0.17.0. The running application reported EPA SWMM version `5.2.4` at startup.
- It reports the largest absolute continuity error parsed from the report.
- Optional AI features call the OpenAI API with `gpt-5` for report review, model drafting, what-if answers and anomaly analysis. They were not tested.
- Tests: 29 passed, 0 failed.
- 5 example `.inp` files, all with `FLOW_UNITS CFS`, and 10 translation files.
- No license is stated for the project.
- The date 18 August 2025 is where the app version first appears in the dated Git history.

**What it does not show.** The published pages and API were not loaded. Calls to the OpenAI API were not tested. The desktop interface was not started. Input in units other than CFS was not checked. [S100](../sources/S100-camel-swmm-replit-summary.md)

**Noted at ingest.** Three names again: Camel_SWMM on the page, Swmm5AppEngine for the project, swmm-pilot-robertdickinson for the site. [S103](../sources/S103-legacy-model-reader-replit-summary.md) has an optional "SWMM Pilot handoff" to a separate service; neither file says whether that service is this app (Q70).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [EPA SWMM 5](swmm-5.md), [InfoSewer and InfoSWMM Legacy Model Reader (app)](infosewer-infoswmm-legacy-model-reader.md).

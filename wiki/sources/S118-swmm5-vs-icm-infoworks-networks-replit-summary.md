---
title: "S118: SWMM5 vs ICM InfoWorks Networks, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-icm-st-venant--robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-07-22
ingested: 2026-11-15
tags: [apps, replit, swmm5, icm, comparison, hydraulics]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 vs ICM InfoWorks Networks, version 1.0.0: a reference app that sets EPA SWMM 5 beside InfoWorks ICM for unsteady flow: a comparison summary, topic pages, tables, source snippets, diagrams and calculators. It is one of Bob's Replit apps, at `swmm-icm-st-venant--robertdickinson.replit.app`. Raw file: [raw/apps/swmm-icm-st-venant--robertdickinson-v1.0.0.md](../../raw/apps/swmm-icm-st-venant--robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says Git history names Replit Agent and Robert Dickinson as commit authors. The copy here was read out of the editor of the Replit project named SWMM ICM StVenant on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- The app does not call or embed the EPA SWMM 5 or InfoWorks ICM engines. It renders authored comparison data and educational visualizations. `engines: none`.
- 118 diagram registry entries across 16 diagram categories, 13 comparison topics, two comparison records (`swmm5` and `icm`) and five guided-tour steps.
- The interface labels its reference engines SWMM5 v5.2.4 and ICM v2025.1 and shows "Last updated: Feb 2026". The file calls these app labels, not proof of installed engine versions.
- Calculators: a Courant number `Cr = (V + c) * Δt / Δx`; a Preissmann slot width of `pipe diameter * width factor / 100` with wave speed `sqrt(g * full-pipe area / slot thickness)`; Manning as `Q = (1.49 / n) * A * Rh^(2/3) * sqrt(S)`; a Froude number `Fr = V / sqrt(gD)`.
- The Manning calculator shows a comparison value with a small code-defined adjustment; the file calls these illustrative values, not outputs from the engines.
- ICM computational points are estimated as `max(2, ceil(conduit length / 200))`; the SWMM5 side is drawn as conduit endpoints.
- The timestep estimator applies code-defined bounds and factors; the component itself warns that real runtime depends on hardware, model and solver settings.
- Unit labels default to US customary, with SI display conversions.
- `npm run check` passed. No test script exists. The four dashboard views rendered; the Topic view logged an HTML error for a `button` inside a `button`.
- Git history credits Replit Agent with publication, the review document, a refactor and search and navigation changes, and `robertdickinson` with earlier documentation, unit-display and accessibility changes.

**Limits it states.** The formulas and example outputs were not validated against runs of SWMM 5 or ICM. Only the first viewport of four views was loaded. The package version has no recorded release date; the `date:` is the latest publication entry in Git.

**Checked at ingest.** [S20](S20-li-edition-54-two-solvers.md), Bob's article on the app, gives twelve tabs and 117 animations. This file, written from the source on 15 November 2026, gives 13 topics, 16 diagram categories and 118 diagram entries (Q78). It settles one thing the app page had left open: the app runs neither engine.

**Feeds:** [SWMM and ICM St. Venant comparison (app)](../entities/swmm-icm-st-venant-app.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [InfoWorks ICM](../entities/infoworks-icm.md).

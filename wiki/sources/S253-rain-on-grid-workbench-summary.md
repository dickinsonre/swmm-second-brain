---
title: "S253: Rain-on-Grid Workbench, summary written from the page (v1.0)"
type: source
raw: raw/apps/rain-on-grid-workbench-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-06
ingested: 2026-11-17
tags: [apps, swmm6, 2d, rain-on-grid, flooding]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Rain-on-Grid Workbench, version 1.0: a map of the seven numbered algorithms of UrbanSystemsLab/urban-flood-modeling-workflows (Shrestha, Mustafa, Kennedy and McPhearson 2026, Environmental Modelling and Software 206, 107169) onto SWMM6, with the ones it ports run in the browser and the step the repository lacks added: writing a model file. Raw file: [raw/apps/rain-on-grid-workbench-v1.0.md](../../raw/apps/rain-on-grid-workbench-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1791287157-1272, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The published page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session. The summary says the Netlify copy adds a one-line AI-use note.

**Claims worth keeping** (all copied from the file)
- On a synthetic site, native OpenSWMM 6 (develop, commit 19a1bc42) at 6.6 ft cells: the paper's rainfall reduction factor removed 56.5 % of the rain and still left a closed street sag 1.06 ft deep, while a real pipe took the full storm and held the sag to 0.37 ft.
- The engine numbers are recorded from one native run; they do not move with the sliders.
- Buildings burned into the terrain is ported and matches the repository's rasterio output at four cell sizes; ported algorithms are marked as checked against the repository's own Python.
- Algorithm 5 turns an NOAA Atlas 14 depth table into a Chicago storm; the page shows that the repository's discretisation does not always conserve the storm total.
- The repository (bcab42e, 3 May 2026, Apache-2.0) stops at rasters and tables and never mentions SWMM, PCSWMM or CityCAT.

**Limits it states.** The site is synthetic, so nothing validates the paper's four cities. Flow paths are not WhiteboxTools output; algorithms 1 and 7 are described, not run. One site, one storm, one cell size; no HEC-RAS or CityCAT run.

**Checked at ingest.** 6.6 ft is 2 m (our conversion). The summary gives no figure for how far the storm total departs under algorithm 5. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://rain-on-grid-workbench.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Rain-on-Grid Workbench (app)](../entities/rain-on-grid-workbench.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM 2D: rainfall and infiltration on the mesh](../concepts/icm-2d-rainfall-and-infiltration.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).

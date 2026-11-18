---
title: "Rain-on-Grid Workbench (app)"
type: entity
updated: 2026-11-17
sources: [S205, S253]
tags: [apps, swmm6, 2d, rain-on-grid, flooding]
reviewed: no
---
Bob's app Rain-on-Grid Workbench: a map of the seven numbered algorithms of UrbanSystemsLab/urban-flood-modeling-workflows (Shrestha, Mustafa, Kennedy and McPhearson 2026, Environmental Modelling and Software 206, 107169) onto SWMM6, with the ones it ports run in the browser and the step the repository lacks added: writing a model file. Version 1.0, 2026-10-06 [S253](../sources/S253-rain-on-grid-workbench-summary.md). Netlify address: https://rain-on-grid-workbench.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S253](../sources/S253-rain-on-grid-workbench-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S253](../sources/S253-rain-on-grid-workbench-summary.md)
- On a synthetic site, native OpenSWMM 6 (develop, commit 19a1bc42) at 6.6 ft cells: the paper's rainfall reduction factor removed 56.5 % of the rain and still left a closed street sag 1.06 ft deep, while a real pipe took the full storm and held the sag to 0.37 ft.
- The engine numbers are recorded from one native run; they do not move with the sliders.
- Buildings burned into the terrain is ported and matches the repository's rasterio output at four cell sizes; ported algorithms are marked as checked against the repository's own Python.
- Algorithm 5 turns an NOAA Atlas 14 depth table into a Chicago storm; the page shows that the repository's discretisation does not always conserve the storm total.
- The repository (bcab42e, 3 May 2026, Apache-2.0) stops at rasters and tables and never mentions SWMM, PCSWMM or CityCAT.

**What it does not show.** The site is synthetic, so nothing validates the paper's four cities. Flow paths are not WhiteboxTools output; algorithms 1 and 7 are described, not run. One site, one storm, one cell size; no HEC-RAS or CityCAT run. [S253](../sources/S253-rain-on-grid-workbench-summary.md)

**Noted at ingest.** 6.6 ft is 2 m (our conversion). The summary gives no figure for how far the storm total departs under algorithm 5.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM 2D: rainfall and infiltration on the mesh](../concepts/icm-2d-rainfall-and-infiltration.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).

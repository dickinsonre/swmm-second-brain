---
name: Rain-on-Grid Workbench
file: rain-on-grid-workbench.html
version: "1.0"
date: 2026-10-06
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/8wArnRMuHgsuxgs4wEE1ph", repo: none named in the page}
engines:
  - {name: OpenSWMM 6, branch: develop, commit: 19a1bc42, note: "results recorded from a native run, fixed, not live"}
units: US customary with a US/SI switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/8wArnRMuHgsuxgs4wEE1ph, version 1791287157-1272 (index.html, 202,575 bytes, SHA-256 b67788ac9f3a672d11caceaf445289caaa839bb5c84407cbce9389a3bdec58c0), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Rain-on-Grid Workbench: seven Urban Systems Lab flood-modelling algorithms, run in the browser and carried to a SWMM6 input file

## In three points
- **What:** Maps the seven numbered algorithms of UrbanSystemsLab/urban-flood-modeling-workflows (Shrestha, Mustafa, Kennedy and McPhearson 2026) to SWMM6, runs the ones it ports in the browser, and adds the step the repository lacks: writing a model file.
- **So what:** On a synthetic site the paper's rainfall reduction factor removed 56.5% of the rain and still left a closed street sag 1.06 ft deep, while a real pipe in a native OpenSWMM 6 run took the full storm and held the sag to 0.37 ft.
- **Now what:** Model the drains rather than scaling the rain when a site has closed low points. The site is synthetic, algorithms 1 and 7 are described not run, and the engine numbers do not move with the sliders.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); the date is the artifact's. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Pipeline, Storm, Reduction, Terrain, Parameters, Flow paths, SWMM6, Paper, Checks. Each algorithm card says what the code writes, where it would land in a SWMM6 input file, and whether the app runs it (for example, buildings into the terrain is ported and matches the repository's rasterio output at four cell sizes). The repository stops at rasters and tables and never mentions SWMM, PCSWMM or CityCAT. Algorithm 5 turns an Atlas 14 depth table into a Chicago storm; the page shows that the repository's discretisation does not always conserve the storm total.

## Checks (as stated on the page)

- Same site, same storm, native OpenSWMM 6 at 6.6 ft cells: the factor removed 56.5% of the rain and still left the closed street sag 1.06 ft deep; the pipe took the full storm and held it to 0.37 ft.
- Ported algorithms are marked "matches the repo's own Python, checked on this page"; engine numbers are marked "recorded from a native OpenSWMM 6 run; fixed, not live".
- The SWMM6 comparison is one site, one storm, 6.6 ft cells.

## What this does not show

- The site is synthetic, so nothing validates the paper's four cities.
- Flow paths are not WhiteboxTools output; algorithms 1 and 7 are described, not run.
- Engine numbers are for one default site at one cell size; no HEC-RAS or CityCAT run.

## How to reproduce

Open the page and work through the tabs; the SWMM6 tab writes the input file.

## Credits and licenses

UrbanSystemsLab/urban-flood-modeling-workflows at bcab42e (May 3, 2026), Apache-2.0. Shrestha, Mustafa, Kennedy and McPhearson (2026), Environmental Modelling and Software 206, 107169. OpenSWMM engine, develop at 19a1bc42. NOAA Atlas 14 Volume 1 Version 5 point values. No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.

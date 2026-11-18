---
name: Geo Flow Population Calculator
file: geo-flow-population-calculator.html
version: "2"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/La5qqP7RUfXa3xvLwzCPbe", original: "SWMMEnablement/geo-flow-ruby (React 18, Vite, Tailwind, shadcn/ui; about 5,000 lines), the GIS Population Calculator", repo: none named for this edition}
engines:
  - {name: EPA SWMM, version: 5.2.4, build: "USEPA v5.2.4 tag, Emscripten 3.1.51 -O2, single-file module 677,858 bytes; payload SHA-256 411d0bc8434a326d2ddefd57a0cb6ace8b23bd16badbb9ee54fb384bcff060ef, re-hashed in the browser before each run", license: public domain}
units: US customary by default (ft, gal/cap/day, cfs), SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in two sessions in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/La5qqP7RUfXa3xvLwzCPbe, version 1792937621-cbc3 (index.html, 1,380,088 bytes, SHA-256 8a67e5f6b2f1f33bc285fa2b809de6a4ea9b2c8fbfdb766459fc7499916bf50c), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Geo Flow Population Calculator: households to subcatchments to dry weather flow in SWMM5

## In three points
- **What:** A single-file rebuild of Bob's geo-flow-ruby project: it assigns household points to SWMM5 subcatchments with a point-in-polygon ray cast (PNPOLY), totals persons per subcatchment, and writes that population into the model as dry weather flow at each subcatchment's outlet node, then runs the export in EPA SWMM 5.2.4 inside the page.
- **So what:** On the real-data check, 1,782 households fall inside a subcatchment for 3,140.1 persons, an independent Shapely overlay agrees point for point, and the exported model runs in EPA SWMM 5.2.4 with no errors; mean system DWF equals Σ persons x q to 3.8 x 10^-8. Version 2 fixed what driving version 1 through every workflow found, such as an unassigned-household fix that used the median stray distance (191 ft on the sample, which rescues half of any strays) and now uses a fixed 30 ft (9 m).
- **Now what:** Use it to turn address points into DWF baselines. It shows the counting is right, not that the populations are: an address point a few dozen feet off can land in the next subcatchment, and on the sample 9% of assigned households lie within 30 ft of a boundary.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("version 2 (2026-10-25)"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Map, Results, Ray Cast (a step-through of the crossing test), Validate, Defects, About, Doc. Load a SWMM5 .inp and household points (CSV or shapefile), set the per-capita flow and units, count, check for overlaps and strays, merge neighbouring subcatchments (a true polygon union with polygon-clipping 0.15.7), and export the .inp with [DWF] at outlet nodes.

Version 2 changes, each shown with the version 1 code it replaced: the stray-household fix (30 ft instead of the median); the nearest-boundary search, which measured every subcatchment (10.0 s for 60,000 households in 1,600 subcatchments, now 0.32 s) and with a tolerance could name the wrong one; the per-capita slider no longer re-runs every ray cast; overlaps along a shared line are now found and their area reported; merge no longer needs identical vertices; Windows-1252 files are read.

## Checks (as stated on the page)

- Version 1: 43 core tests on parsing, allocation, validation, merge, unit conversion and export, including runs of the exported files in native EPA SWMM 5.2.4 (zero errors; mean system DWF equals Σ persons x q to 3.8 x 10^-8; every one of 672 report periods checked).
- Version 2: 37 core tests holding version 2 to version 1 (allocation, nearest distance and validation identical household by household on the sample, on 6,000 random households in 108 polygons with holes, and on 60,000 households in 1,600 polygons).
- The real-data allocation checked against Shapely; the overlap area checked against Shapely's make_valid (both 195.5 sq ft); the registration search checked against a control it had to find.
- The original's defects (GF-2, GF-3, GF-4 among them) reproduced by running its utilities unchanged, with the code shown on the Defects tab.

## What this does not show

As the page lists it: that the populations are right, which depends on the data; the biggest risk is position, since a geocoding error can move a household across a boundary (on the sample, 0% of assigned households lie within 15 ft of a boundary, 9% within 30 ft, 30% within 50 ft; the synthetic lots were set back).

## Credits and licenses

EPA SWMM 5.2.4 (public domain); PNPOLY (W. Randolph Franklin); polygon-clipping 0.15.7; Shapely and GEOS for the independent check; SWMMEnablement/geo-flow-ruby. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in two Claude sessions in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the geo-flow-ruby source, asked for an HTML app, chose the four version 2 improvements and owns the result. Version 1: Claude read the original source, bundled its utilities unchanged and wrote the reproductions behind the defect register, wrote the allocation, validation, merge, import and export code, compiled EPA SWMM 5.2.4 to WebAssembly, generated the synthetic sample, and wrote the page, the Doc essay and figures, and the tests. Version 2: Claude drove version 1 through every workflow and made the fixes above. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2 (2026-10-25): fixes from driving version 1 through every workflow (the version read).
- 1 (October 2026): first single-file rebuild.

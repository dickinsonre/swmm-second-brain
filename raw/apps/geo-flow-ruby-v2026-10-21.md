---
name: Geo Flow Ruby
file: geo-flow-ruby.html
version: 2026-10-21
date: 2026-10-21
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Vig2igKDHQjNbNNMSYtCxX", original: "SWMMEnablement/geo-flow-ruby (React and TypeScript, the GIS Population Calculator)", repo: none named for this edition}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "loaded from a public CDN only when the run feature is used; the page's SWMM counts come from 5.2.4 built from the USEPA source"}
units: US customary by default (gal/cap/day, cfs), SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 21 October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Vig2igKDHQjNbNNMSYtCxX, version 1792637435-70b9 (index.html, 255,535 bytes, SHA-256 ba78d64fca27e206f3a74cdc2a50f1e0c58bc2fe33f2f72f8dbf6eaacffe965b), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Geo Flow Ruby: household points to subcatchment population to SWMM dry-weather flow

## In three points
- **What:** An earlier single-file rebuild of SWMMEnablement/geo-flow-ruby (see also Geo Flow Population Calculator, a later and larger rebuild of the same project). It assigns household points to SWMM subcatchments with the ray-crossing test, sums persons, routes them to the node each subcatchment drains to, and writes dry-weather FLOW baselines into [DWF]. Files never leave the page.
- **So what:** The original's own utilities, run unchanged in Node on the sample, read 0 of 12 polygons from an EPA-written .inp (its header test accepted only capitals), assigned 0 of 329 households (polygons rescaled to an 800 x 600 canvas, households left in model coordinates), wrote CFS baselines 100.0001 times too large (1.547 cfs for 100 persons at 100 gal/cap/day, against 0.01547 cfs), and produced 22 ERROR 209 lines in EPA SWMM 5.2.4 by writing [DWF] against subcatchments and inventing a pollutant called Population. The rebuild reads 12 of 12 and assigns 325 of 329.
- **Now what:** Use it to make DWF baselines from address points. A household is a point, so a 40-unit building on a boundary goes wholly to one side; the output is a baseline, with no RDII and no peaking factor.

This summary was written after the fact. The page ships no technical summary of its own. It gives no version number; the date is the build date the page names (21 October 2026). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Map, Results, Checks, About, Doc. Workflow kept from the original: load, configure, count, check, export, and the step-through ray animation. Left out: validation history, polygon merging and the mini-map. EPA SWMM, proj4, shpjs and the GIF encoder load from public CDNs only when the feature that needs them is used.

## Checks (as stated on the page)

- The original's TypeScript utilities bundled and run unchanged in Node against the sample model and households; every defect reproduced, nothing inferred from reading code alone. Original against rebuilt: polygons read 0 of 12 against 12 of 12; households assigned 0 of 329 against 325 of 329; SWMM 5.2.4 errors on the exported .inp 22 (ERROR 209) against none; FLOW for 100 persons at 100 gal/cap/day 1.547 against 0.01547 cfs; overlap alarms on a tiling with no overlaps 29 of 66 pairs in the original; distance to nearest subcatchment measured to the nearest corner in pixels in the original, to the nearest edge in feet now.
- The new engine checked against Shapely 2.2.0 (GEOS) on all 329 households. Two households planted exactly on shared boundaries go to S06 and S03, one owner each, where GEOS reports each as touching two subcatchments.

## What this does not show

As the page lists it: a household is a point, so a building that straddles a line goes to whichever side its geocode falls on; a snap radius can miss an edge and leave a household uncounted; census block centroids are not homes; the output is a baseline, with no RDII and no peaking factor.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); proj4, shpjs; Shapely 2.2.0 and GEOS; SWMMEnablement/geo-flow-ruby. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the original source and asked for the app; responsibility is his. Claude read and reproduced the original's defects by running its code, compiled EPA SWMM 5.2.4 to test exports, and wrote the sample data, engine, interface, checks, figures and documentation. The checks are mechanical: Shapely/GEOS agreement on all 323 interior households and zero-error EPA SWMM 5.2.4 runs of the exports. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2026-10-21: first single-file rebuild (the version read).

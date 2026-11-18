---
title: "S213: Low-Spot Census, summary written from the page (v1.0)"
type: source
raw: raw/apps/low-spot-census-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-05
ingested: 2026-11-17
tags: [apps, swmm5, inlets, 2d, surfaces]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Low-Spot Census, version 1.0: an app that finds every place a surface (grid, LandXML TIN or GeoTIFF) can hold water, checks each low spot against the inlets in a SWMM model or CSV, and shows what a 2D mesh does to it. It runs no engine in the page. Raw file: [raw/apps/low-spot-census-v1.0.md](../../raw/apps/low-spot-census-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793909074-527b, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in November 2026 under Bob's direction: Bob chose the problem from a road designer's post about checking falls and dips by eye in Civil 3D; Claude wrote all the code, the synthetic sample road and its SWMM model, chose the noise test and its thresholds by measurement and read EPA's inlet.c. No person has reviewed the code or the essay.

**Claims worth keeping** (all copied from the file)
- On the sample road the last 55 ft of gutter before the low point climbs 2.1 inches, which no contour plot shows. A 12 ft lane at 2 percent crossfall drops 0.24 ft.
- Five verdicts: Orphan (no inlet in the low spot), Stranded (the inlet rim sits above the low point), Cut off (a high spot separates the dip from the inlet serving the sag), Noise (gone after a 3 by 3 median) and Drained.
- Method named: Priority-Flood, Barnes, Lehman and Mulla (2014), Computers & Geosciences 62. Grids are capped at 6 million cells and coarsened above that.
- 20 of 20 exact-answer checks pass and run live on its Verify tab; among them a paraboloid bowl matches its exact volume to 0.003 percent.
- Planted defects: 4 of 4 found on the design surface with 0 false finds; 7 of 9 on the as-built scan with 1 false find; 0 of 9 on QL2 with 0.
- A mesh as fine as the surface reproduces the census exactly.
- The exported input files run in EPA SWMM 5.2.4 with no errors (swmm-toolkit 0.17.0), with byte-identical controls for AUTOMATIC inlet placement in both directions and for a repeat run.

**Limits it states.** No real road has been through the app; every surface is synthetic. The test noise is uncorrelated from cell to cell, where real lidar noise is partly correlated, so the QL2 result is a worst case. It finds where water can stand, not how much an inlet captures.

**Checked at ingest.** 12 ft x 0.02 = 0.24 ft, 2.9 in. The engine runs were made outside the page. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://low-spot-census.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Low-Spot Census (app)](../entities/low-spot-census.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).

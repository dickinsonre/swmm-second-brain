---
title: "Low-Spot Census (app)"
type: entity
updated: 2026-11-17
sources: [S205, S213]
tags: [apps, swmm5, inlets, 2d, surfaces]
reviewed: no
---
Bob's app Low-Spot Census: an app that finds every place a surface (grid, LandXML TIN or GeoTIFF) can hold water, checks each low spot against the inlets in a SWMM model or CSV, and shows what a 2D mesh does to it. It runs no engine in the page. Version 1.0, 2026-11-05 [S213](../sources/S213-low-spot-census-summary.md). Netlify address: https://low-spot-census.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S213](../sources/S213-low-spot-census-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S213](../sources/S213-low-spot-census-summary.md)
- On the sample road the last 55 ft of gutter before the low point climbs 2.1 inches, which no contour plot shows. A 12 ft lane at 2 percent crossfall drops 0.24 ft.
- Five verdicts: Orphan (no inlet in the low spot), Stranded (the inlet rim sits above the low point), Cut off (a high spot separates the dip from the inlet serving the sag), Noise (gone after a 3 by 3 median) and Drained.
- Method named: Priority-Flood, Barnes, Lehman and Mulla (2014), Computers & Geosciences 62. Grids are capped at 6 million cells and coarsened above that.
- 20 of 20 exact-answer checks pass and run live on its Verify tab; among them a paraboloid bowl matches its exact volume to 0.003 percent.
- Planted defects: 4 of 4 found on the design surface with 0 false finds; 7 of 9 on the as-built scan with 1 false find; 0 of 9 on QL2 with 0.
- A mesh as fine as the surface reproduces the census exactly.
- The exported input files run in EPA SWMM 5.2.4 with no errors (swmm-toolkit 0.17.0), with byte-identical controls for AUTOMATIC inlet placement in both directions and for a repeat run.

**What it does not show.** No real road has been through the app; every surface is synthetic. The test noise is uncorrelated from cell to cell, where real lidar noise is partly correlated, so the QL2 result is a worst case. It finds where water can stand, not how much an inlet captures. [S213](../sources/S213-low-spot-census-summary.md)

**Noted at ingest.** 12 ft x 0.02 = 0.24 ft, 2.9 in. The engine runs were made outside the page.

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).

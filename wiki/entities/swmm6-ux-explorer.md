---
title: "SWMM6 UX Explorer (app)"
type: entity
updated: 2026-11-18
sources: [S284]
tags: [apps, swmm6, user-interface, design-storms, atlas-14, usgs]
reviewed: no
---
Bob's app SWMM6 UX Explorer: a single-file browser copy of the SWMMVis desktop workspace for OpenSWMM 6 alpha.4 around a small live model (59 junctions, 59 conduits, 58 subcatchments on 222 ac), with NOAA Atlas 14, USGS and 3DEP data tools and three candidate design storms; it also reads and writes a SWMM5 file. Version and date 2026-11-03 [S284](../sources/S284-swmm6-ux-explorer-summary.md). Netlify address, from its `links:` line: https://swmm6-ux-explorer.netlify.app [S284](../sources/S284-swmm6-ux-explorer-summary.md).

**A caution about its source.** The page ships no technical summary. [S284](../sources/S284-swmm6-ux-explorer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S284](../sources/S284-swmm6-ux-explorer-summary.md)
- Atlas 14 gives 4.82 in for the 10-year, 24-hour storm at 38.9 N, 77.0 W, the 122 mm (122.4 mm) in the SWMMVis alpha.4 release graphic.
- Three storms of the same 4.82 in: SCS Type II 315.7 cfs, alternating block 296.9, triangle 47.1 at the outfall in the demo engine, each with 2,080,214 ft3 of runoff; EPA SWMM 5.2.4 on the exported files gives 373.4, 357.9 and 49.6.
- The alternating block matches Atlas 14 at 9 of 10 durations up to 24 hours and runs 1.7% high at 3 hours.
- All 58 subcatchment outlines match their modeled areas (largest relative error 9 x 10^-13) with zero overlap across 1,653 pairs.
- The USGS Water Data API path returned the same 888 daily values, 18 ice days and two peaks as the older WaterServices snapshot.

**What it does not show.** No SWMMVis code runs; its look follows the manual's screenshots, not SWMMVis on Windows; the demo engine is not SWMM; the storm ranking speaks for this network at this location; outlines true in area, invented in shape; elevation is a 40 x 40 sample, about 295 ft per cell. [S284](../sources/S284-swmm6-ux-explorer-summary.md)

**Noted at ingest.** 4.82 x 25.4 = 122.4 mm (our arithmetic, as the Doc states).

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [Subcatchment width](../concepts/subcatchment-width.md).

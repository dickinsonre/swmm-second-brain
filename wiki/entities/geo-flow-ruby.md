---
title: "Geo Flow Ruby (app)"
type: entity
updated: 2026-11-18
sources: [S337]
tags: [apps, dry-weather-flow, population, gis, swmm5]
reviewed: no
---
Bob's app Geo Flow Ruby: household points to subcatchment population to SWMM dry-weather flow. Version and date 2026-10-21 [S337](../sources/S337-geo-flow-ruby-summary.md). Its `links:` line names no live Netlify address [S337](../sources/S337-geo-flow-ruby-summary.md).

**A caution about its source.** The page ships no technical summary. [S337](../sources/S337-geo-flow-ruby-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S337](../sources/S337-geo-flow-ruby-summary.md)
- An earlier single-file rebuild of SWMMEnablement/geo-flow-ruby (see also Geo Flow Population Calculator, a later and larger rebuild of the same project). It assigns household points to SWMM subcatchments with the ray-crossing test, sums persons, routes them to the node each subcatchment drains to, and writes dry-weather FLOW baselines into [DWF]. Files never leave the page.
- The original's own utilities, run unchanged in Node on the sample, read 0 of 12 polygons from an EPA-written .inp (its header test accepted only capitals), assigned 0 of 329 households (polygons rescaled to an 800 x 600 canvas, households left in model coordinates), wrote CFS baselines 100.0001 times too large (1.547 cfs for 100 persons at 100 gal/cap/day, against 0.01547 cfs), and produced 22 ERROR 209 lines in EPA SWMM 5.2.4 by writing [DWF] against subcatchments and inventing a pollutant called Population. The rebuild reads 12 of 12 and assigns 325 of 329.
- The original's TypeScript utilities bundled and run unchanged in Node against the sample model and households; every defect reproduced, nothing inferred from reading code alone.
- The new engine checked against Shapely 2.2.0 (GEOS) on all 329 households. Two households planted exactly on shared boundaries go to S06 and S03, one owner each, where GEOS reports each as touching two subcatchments.

**How to use it, as the summary puts it.** Use it to make DWF baselines from address points. A household is a point, so a 40-unit building on a boundary goes wholly to one side; the output is a baseline, with no RDII and no peaking factor. [S337](../sources/S337-geo-flow-ruby-summary.md)

**What it does not show.** As the page lists it: a household is a point, so a building that straddles a line goes to whichever side its geocode falls on; a snap radius can miss an edge and leave a household uncounted; census block centroids are not homes; the output is a baseline, with no RDII and no peaking factor. [S337](../sources/S337-geo-flow-ruby-summary.md)

**Noted at ingest.** Geo Flow Ruby and [Geo Flow Population Calculator (app)](geo-flow-population-calculator.md) are two single-file editions of the same Lovable project, SWMMEnablement/geo-flow-ruby, built in different sessions; they are kept as two pages.

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [Geo Flow Population Calculator (app)](geo-flow-population-calculator.md).

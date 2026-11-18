---
title: "Geo Flow Population Calculator (app)"
type: entity
updated: 2026-11-18
sources: [S338]
tags: [apps, dry-weather-flow, population, gis, swmm5]
reviewed: no
---
Bob's app Geo Flow Population Calculator: households to subcatchments to dry weather flow in SWMM5. Version 2, 2026-10-25 [S338](../sources/S338-geo-flow-population-calculator-summary.md). Its `links:` line names no live Netlify address [S338](../sources/S338-geo-flow-population-calculator-summary.md).

**A caution about its source.** The page ships no technical summary. [S338](../sources/S338-geo-flow-population-calculator-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S338](../sources/S338-geo-flow-population-calculator-summary.md)
- A single-file rebuild of Bob's geo-flow-ruby project: it assigns household points to SWMM5 subcatchments with a point-in-polygon ray cast (PNPOLY), totals persons per subcatchment, and writes that population into the model as dry weather flow at each subcatchment's outlet node, then runs the export in EPA SWMM 5.2.4 inside the page.
- On the real-data check, 1,782 households fall inside a subcatchment for 3,140.1 persons, an independent Shapely overlay agrees point for point, and the exported model runs in EPA SWMM 5.2.4 with no errors; mean system DWF equals Σ persons x q to 3.8 x 10^-8. Version 2 fixed what driving version 1 through every workflow found, such as an unassigned-household fix that used the median stray distance (191 ft on the sample, which rescues half of any strays) and now uses a fixed 30 ft (9 m).
- Version 1: 43 core tests on parsing, allocation, validation, merge, unit conversion and export, including runs of the exported files in native EPA SWMM 5.2.4 (zero errors; mean system DWF equals Σ persons x q to 3.8 x 10^-8; every one of 672 report periods checked).
- Version 2: 37 core tests holding version 2 to version 1 (allocation, nearest distance and validation identical household by household on the sample, on 6,000 random households in 108 polygons with holes, and on 60,000 households in 1,600 polygons).
- The real-data allocation checked against Shapely; the overlap area checked against Shapely's make_valid (both 195.5 sq ft); the registration search checked against a control it had to find.
- The original's defects (GF-2, GF-3, GF-4 among them) reproduced by running its utilities unchanged, with the code shown on the Defects tab.

**How to use it, as the summary puts it.** Use it to turn address points into DWF baselines. It shows the counting is right, not that the populations are: an address point a few dozen feet off can land in the next subcatchment, and on the sample 9% of assigned households lie within 30 ft of a boundary. [S338](../sources/S338-geo-flow-population-calculator-summary.md)

**What it does not show.** As the page lists it: that the populations are right, which depends on the data; the biggest risk is position, since a geocoding error can move a household across a boundary (on the sample, 0% of assigned households lie within 15 ft of a boundary, 9% within 30 ft, 30% within 50 ft; the synthetic lots were set back). [S338](../sources/S338-geo-flow-population-calculator-summary.md)

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [Geo Flow Ruby (app)](geo-flow-ruby.md).

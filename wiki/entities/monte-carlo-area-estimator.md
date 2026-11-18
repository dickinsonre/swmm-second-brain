---
title: "Monte Carlo Area Estimator (app)"
type: entity
updated: 2026-11-18
sources: [S367]
tags: [apps, mathematics, monte-carlo]
reviewed: no
---
Bob's app Monte Carlo Area Estimator: throw random points at a box to measure a shape. Version 1.0.0, 2026-10-24 [S367](../sources/S367-monte-carlo-area-estimator-summary.md). Its `links:` line names no live Netlify address [S367](../sources/S367-monte-carlo-area-estimator-summary.md).

**A caution about its source.** The page ships no technical summary. [S367](../sources/S367-monte-carlo-area-estimator-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S367](../sources/S367-monte-carlo-area-estimator-summary.md)
- A single-file rebuild of Bob's Lovable app on Monte Carlo area estimation: eight preset shapes, freehand drawing with symmetry, photo tracing, four animation modes, bulk throws, a heatmap, saved comparisons, and Buffon's needle. The fraction of random points that land inside a shape measures its area, with seeded, repeatable throws and Wilson 95% intervals.
- The original judged presets by screen pixels and had the wrong exact areas for the triangle, star and heart, estimated π from the circle as 4·p̂ instead of p̂/0.4², and stopped by comparing with the known answer. The rebuild judges presets by exact geometry, and its stop rule asks only whether the 95% interval is narrow enough; each preset thrown 4,000,000 times lands within 3.5 standard errors of exact (largest |z| 2.94).
- Polygon areas of the triangle, pentagon, hexagon and star match their closed forms to machine precision; the 2,048-edge heart matches the exact Bézier area to 1.7 parts in a million.
- Each preset thrown 4,000,000 times with seed 1946: every estimate within 3.5 standard errors of exact; largest |z| 2.94, on the square.
- Generator: 60 seeds of 1,000,000 throws on the square and circle; z-scores averaged 0.07 with standard deviations 0.97 and 1.07.
- Wilson interval coverage 95.6% over 4,000 runs of 500 throws at the star.

**How to use it, as the summary puts it.** Use it to teach sampling error and why small shapes are expensive: the points needed for a given precision grow as (1 - p)/p, so a shape covering a hundredth of the box costs about a hundred times more than one covering half. [S367](../sources/S367-monte-carlo-area-estimator-summary.md)

**What it does not show.** As the page lists it: small shapes are expensive (the cost grows as (1 - p)/p); no person has reviewed the historical account in the Doc against its sources line by line. [S367](../sources/S367-monte-carlo-area-estimator-summary.md)

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).

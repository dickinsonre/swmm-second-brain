---
name: Monte Carlo Area Estimator
file: monte-carlo-area-estimator.html
version: 1.0.0
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/7PSv59aicFr3QME5k8TnXF", original: "Lovable project monte-carlo-area-estimator (Monte Carlo Area Estimation Methods)", repo: none named in the page}
engines: none (a seeded Monte Carlo engine written for the page)
units: US customary by default, metric behind a switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 24 October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/7PSv59aicFr3QME5k8TnXF, version 1792897839-2cd1 (index.html, 1,079,424 bytes, SHA-256 86150699f392344abcb9a75ecf725d7f5e19b21e3837ec7b7294288a304a1e3e), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Monte Carlo Area Estimator: throw random points at a box to measure a shape

## In three points
- **What:** A single-file rebuild of Bob's Lovable app on Monte Carlo area estimation: eight preset shapes, freehand drawing with symmetry, photo tracing, four animation modes, bulk throws, a heatmap, saved comparisons, and Buffon's needle. The fraction of random points that land inside a shape measures its area, with seeded, repeatable throws and Wilson 95% intervals.
- **So what:** The original judged presets by screen pixels and had the wrong exact areas for the triangle, star and heart, estimated π from the circle as 4·p̂ instead of p̂/0.4², and stopped by comparing with the known answer. The rebuild judges presets by exact geometry, and its stop rule asks only whether the 95% interval is narrow enough; each preset thrown 4,000,000 times lands within 3.5 standard errors of exact (largest |z| 2.94).
- **Now what:** Use it to teach sampling error and why small shapes are expensive: the points needed for a given precision grow as (1 - p)/p, so a shape covering a hundredth of the box costs about a hundred times more than one covering half.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0.0 · 2026-10-24"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Estimate, Buffon's needle, Findings, About, Doc. Drawings use a fixed 600 x 600 mask, so results do not depend on the screen. Exact areas: triangle √3·r², star 5·r·0.4r·sin 36°, heart (21/25)·h² with h = 0.9r. Buffon's needle uses π ≈ 2·L·n/(d·c), valid for any L ≤ d. Every animation mode updates the statistics and honours the stop rules. The Findings tab repeats the checks in the browser.

## Checks (as stated on the page)

- Polygon areas of the triangle, pentagon, hexagon and star match their closed forms to machine precision; the 2,048-edge heart matches the exact Bézier area to 1.7 parts in a million.
- Each preset thrown 4,000,000 times with seed 1946: every estimate within 3.5 standard errors of exact; largest |z| 2.94, on the square.
- Generator: 60 seeds of 1,000,000 throws on the square and circle; z-scores averaged 0.07 with standard deviations 0.97 and 1.07.
- Wilson interval coverage 95.6% over 4,000 runs of 500 throws at the star.
- Buffon: crossing probability at L/d = 0.3, 0.7 and 1.0 with 4,000,000 needles each; all |z| below 2.
- The original built and driven in headless Chromium: a preset plus Done Drawing produced no Theoretical Area panel and a stray notice; 100,000 points washed the canvas out; its drawing code measured at several pixel ratios.

## What this does not show

As the page lists it: small shapes are expensive (the cost grows as (1 - p)/p); no person has reviewed the historical account in the Doc against its sources line by line.

## Credits and licenses

N. Metropolis and S. Ulam (1949); R. Eckhardt, Los Alamos Science No. 15 (1987); G.-L. Leclerc, Comte de Buffon (1777, problem posed 1733); Wilson's score interval. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, on 24 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for the rebuild; responsibility is his. Claude read the original source, built it and drove it in a headless browser, measured its pixel bias and stopping rule, wrote the engine, the page, the figures, the Doc essay and its Word copy, and chose the Wilson interval and the precision stop rule. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.0 (2026-10-24): first single-file release from the Lovable source zip (the version read).

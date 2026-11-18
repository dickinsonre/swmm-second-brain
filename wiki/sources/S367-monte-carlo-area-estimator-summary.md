---
title: "S367: Monte Carlo Area Estimator, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/monte-carlo-area-estimator-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, mathematics, monte-carlo]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Monte Carlo Area Estimator, version 1.0.0: throw random points at a box to measure a shape. Raw file: [raw/apps/monte-carlo-area-estimator-v1.0.0.md](../../raw/apps/monte-carlo-area-estimator-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/7PSv59aicFr3QME5k8TnXF, version 1792897839-2cd1 (index.html, 1,079,424 bytes, SHA-256 86150699f392344abcb9a75ecf725d7f5e19b21e3837ec7b7294288a304a1e3e), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, on 24 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for the rebuild; responsibility is his. Claude read the original source, built it and drove it in a headless browser, measured its pixel bias and stopping rule, wrote the engine, the page, the figures, the Doc essay and its Word copy, and chose the Wilson interval and the precision stop rule."

**Claims worth keeping** (all copied from the file)
- A single-file rebuild of Bob's Lovable app on Monte Carlo area estimation: eight preset shapes, freehand drawing with symmetry, photo tracing, four animation modes, bulk throws, a heatmap, saved comparisons, and Buffon's needle. The fraction of random points that land inside a shape measures its area, with seeded, repeatable throws and Wilson 95% intervals.
- The original judged presets by screen pixels and had the wrong exact areas for the triangle, star and heart, estimated π from the circle as 4·p̂ instead of p̂/0.4², and stopped by comparing with the known answer. The rebuild judges presets by exact geometry, and its stop rule asks only whether the 95% interval is narrow enough; each preset thrown 4,000,000 times lands within 3.5 standard errors of exact (largest |z| 2.94).
- Polygon areas of the triangle, pentagon, hexagon and star match their closed forms to machine precision; the 2,048-edge heart matches the exact Bézier area to 1.7 parts in a million.
- Each preset thrown 4,000,000 times with seed 1946: every estimate within 3.5 standard errors of exact; largest |z| 2.94, on the square.
- Generator: 60 seeds of 1,000,000 throws on the square and circle; z-scores averaged 0.07 with standard deviations 0.97 and 1.07.
- Wilson interval coverage 95.6% over 4,000 runs of 500 throws at the star.

**Limits it states.** As the page lists it: small shapes are expensive (the cost grows as (1 - p)/p); no person has reviewed the historical account in the Doc against its sources line by line.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Monte Carlo Area Estimator (app)](../entities/monte-carlo-area-estimator.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md).

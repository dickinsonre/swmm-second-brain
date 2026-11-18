---
title: "Pengu Climate Watch (app)"
type: entity
updated: 2026-11-18
sources: [S294]
tags: [apps, climate, antarctica, teaching, lovable]
reviewed: no
---
Bob's app Pengu Climate Watch: Bob's Lovable app on Antarctic weather, ice and penguin habitat (four React pages) rebuilt as one HTML file and fact-checked, treating the ice sheet as a reservoir and a glacier's flux gate like a culvert. Version 1.1, 2026-10-25 [S294](../sources/S294-pengu-climate-watch-summary.md). Netlify address, from its `links:` line: https://pengu-cllimate-watch.netlify.app [S294](../sources/S294-pengu-climate-watch-summary.md).

**A caution about its source.** The page ships no technical summary. [S294](../sources/S294-pengu-climate-watch-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S294](../sources/S294-pengu-climate-watch-summary.md)
- GRACE and GRACE-FO: about 135 Gt (about 149 billion US tons) of ice lost a year from 2002 to 2025; IMBIE's 2026 assessment: 4,780 Gt lost from 1979 to 2023, 13.3 mm (0.52 in, the summary's conversion) of sea level.
- The Fixes tab lists 23 code defects and 26 numbers that did not match their sources in the Lovable project, and 30 defects in the port fixed in 1.1, each with the code as it was.
- Weather requests fell from about 27 on page load to five.
- The simulator's melt factor is f = 1.15^(T + 2) above -2 °C, else 1; scaling the net loss rather than the gross discharge gives about 84 mm (3.3 in) of sea level by 2100 at the slider's far end where a strict mass balance would give about a metre (3.3 ft).

**What it does not show.** Air temperature does not melt most Antarctic ice; the habitat tolerances and warmings are the original app's assumptions; Open-Meteo is model output; the ten colony counts are unchecked, at least one about ten times too low. [S294](../sources/S294-pengu-climate-watch-summary.md)

**Noted at ingest.** The summary was written with d3 supplied from a local copy, because cdnjs was not reachable from the reading machine, so it does not say how the page behaves when d3 cannot load (Q112).

See [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Negative results](../concepts/negative-results.md).

---
title: SWMM App Complexity Meter (app)
type: entity
updated: 2026-11-15
sources: [S01, S02, S73, S75]
tags: [apps, measurement]
reviewed: 2026-11-15
---
Bob's browser app that reads a program's source (one .html, a folder, a .zip or a GitHub repository) and grades it against the HydroCouple GitHub organization, fixed at 100 [S02](../sources/S02-complexity-meter-app-md.md). Version 1.9.1, 11 November 2026; analyzer `meter-core.js` 1.7.0 [S02](../sources/S02-complexity-meter-app-md.md). The method is on [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md).

**What it reports beside the index** [S02](../sources/S02-complexity-meter-app-md.md)
- what size alone would score, and a score against one HydroCouple peer
- 36 metrics in six families
- a map of which of 16 SWMM processes the code names, from 226 SWMM 5.2.4 terms
- nine software-sustainability indicators (Nyenah, Doell, Katz and Reinecke, 2024)
- 12 months of history from a git log

**Checks on this build** [S02](../sources/S02-complexity-meter-app-md.md)

| Check | Result |
|---|---|
| Lexer cases worked by hand | 13 of 13 |
| Regression cases | 83 of 83 |
| Fixtures with expected counts | 66 of 66 |
| Browser cases, headless Chromium | 109 of 109 |
| Second full measurement from the packaged scripts | every count reproduced |

**History.** Nine versions from 1.0.0 (31 October 2026) to 1.9.1. Five outside reviews, produced with ChatGPT and supplied by Bob, were each answered by reproducing the finding as a failing test before fixing it [S02](../sources/S02-complexity-meter-app-md.md).

**Used by.** The SWMM 1 Engine's complexity box runs the same analyzer from the command line [S01](../sources/S01-swmm1-engine-app-md.md); at v3.13 it reads 72.6 [S73](../sources/S73-swmm1-engine-app-md-v3-13.md). The St. Venant Solver Rosetta Stone page was handed to the meter page itself and reads 51.5 [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**Limits.** Routine counts come from pattern rules, not parsers. No license has been set for the meter. No person has checked the dimensions, the weights or the anchor's evidence item by item [S02](../sources/S02-complexity-meter-app-md.md).

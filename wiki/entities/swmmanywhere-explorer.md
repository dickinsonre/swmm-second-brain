---
title: SWMManywhere Explorer (app)
type: entity
updated: 2026-11-15
sources: [S122, S147]
tags: [apps, replit, swmm5, model-generation]
reviewed: no
---
Bob's Replit app SWMManywhere Explorer: a browser guide to the separate SWMManywhere Python project, which generates urban drainage network models from a geographic area and global datasets. Version 1.0.0, at `swmmanywhere-explorer.replit.app` [S122](../sources/S122-swmmanywhere-explorer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S122](../sources/S122-swmmanywhere-explorer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S122](../sources/S122-swmmanywhere-explorer-replit-summary.md)
- The app generates and simulates nothing. It displays static TypeScript data. `engines: none`.
- Contents: 5 repository sections with 43 listed entries, 8 pipeline stages, 19 graph functions, 3 data sources, 9 key parameters and 4 metric tiers with 18 metric labels.
- The upstream workflow it describes runs from configuration and data acquisition through graph transformations, topology derivation and hydraulic design to SWMM model generation and validation.
- The equation `Q = C·i·A` is shown as explanatory text and is not evaluated.
- The server registers no application API endpoints.
- `npm run check` and `npm run build` passed. No test script exists.
- The page credits SWMManywhere to Imperial College London and identifies it as BSD-3-Clause. This app declares MIT.

**What it does not show.** The upstream workflow, equation and dataset descriptions are static reference content, not validated by running SWMManywhere. Tab navigation, search and theme persistence were not checked. The `date:` is the newest date in Git, an entry reading "Published your App." [S122](../sources/S122-swmmanywhere-explorer-replit-summary.md)

**Noted at ingest.** Nothing on the page is computed, so there was no result to check beyond the counts.

**Added 15 November 2026: a second app with the same name.** [SWMManywhere Explorer at swm-explorer (app)](swmmanywhere-explorer-swm.md) has the same app name and a different `file:`, and it runs SWMManywhere 0.1.17 and a SWMM5 WebAssembly engine [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md) (Q77).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [EPA SWMM 5](swmm-5.md), [SWMM5 Explorer (app)](swmm5-explorer.md).

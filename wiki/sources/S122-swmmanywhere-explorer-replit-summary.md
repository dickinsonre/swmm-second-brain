---
title: "S122: SWMManywhere Explorer, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmmanywhere-explorer-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-05-13
ingested: 2026-11-15
tags: [apps, replit, swmm5, model-generation]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMManywhere Explorer, version 1.0.0: a browser guide to the separate SWMManywhere Python project, which generates urban drainage network models from a geographic area and global datasets. It is one of Bob's Replit apps, at `swmmanywhere-explorer.replit.app`. Raw file: [raw/apps/swmmanywhere-explorer-v1.0.0.md](../../raw/apps/swmmanywhere-explorer-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says no AI use is documented in the project source. The copy here was read out of the editor of the Replit project named Swmmanywhere Explorer on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- The app generates and simulates nothing. It displays static TypeScript data. `engines: none`.
- Contents: 5 repository sections with 43 listed entries, 8 pipeline stages, 19 graph functions, 3 data sources, 9 key parameters and 4 metric tiers with 18 metric labels.
- The upstream workflow it describes runs from configuration and data acquisition through graph transformations, topology derivation and hydraulic design to SWMM model generation and validation.
- The equation `Q = C·i·A` is shown as explanatory text and is not evaluated.
- The server registers no application API endpoints.
- `npm run check` and `npm run build` passed. No test script exists.
- The page credits SWMManywhere to Imperial College London and identifies it as BSD-3-Clause. This app declares MIT.

**Limits it states.** The upstream workflow, equation and dataset descriptions are static reference content, not validated by running SWMManywhere. Tab navigation, search and theme persistence were not checked. The `date:` is the newest date in Git, an entry reading "Published your App."

**Checked at ingest.** Nothing on the page is computed, so there was no result to check beyond the counts.

**Feeds:** [SWMManywhere Explorer (app)](../entities/swmmanywhere-explorer.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [EPA SWMM 5](../entities/swmm-5.md), [SWMM5 Explorer (app)](../entities/swmm5-explorer.md).

---
title: MapSWMMSewer Code Repository (app)
type: entity
updated: 2026-11-15
sources: [S111]
tags: [apps, replit, code-library]
reviewed: no
---
Bob's Replit app MapSWMMSewer - Code Repository: a private app that stores code files associated with SWMM, sewer analysis and h2oCalc as text, and lets its user search, filter, view, add, edit and delete them. Version 1.0.0, at `sewer-code-search.replit.app` [S111](../sources/S111-mapswmmsewer-code-repository-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S111](../sources/S111-mapswmmsewer-code-repository-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S111](../sources/S111-mapswmmsewer-code-repository-replit-summary.md)
- It runs none of the stored code and no simulation engine.
- The development database held 16 records: 6 SWMM, 3 Sewer and 7 h2oCalc, in 4 distinct language values and 2,759 code lines. The API returned 84 distinct tags.
- The content sources named in `server/seed.ts` are EPA SWMM 5.2, ICM SWMM, InfoSWMM, InfoSewer, InfoAsset and h2oCalc. Their licenses are not stated, and the correctness of the stored code was not checked.
- Deployment metadata reports a private deployment.
- `npm run check` passed. No test script exists.

**What it does not show.** The production database was not queried and the production page was not loaded. Create, update, delete, search and filter were not covered by tests. [S111](../sources/S111-mapswmmsewer-code-repository-replit-summary.md)

**Noted at ingest.** 6 + 3 + 7 = 16. This file was held back when the others were committed, because the app is private; Bob said on 15 November 2026 that it may go into the public repository (log).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md).

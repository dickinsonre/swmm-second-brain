---
title: "S111: MapSWMMSewer - Code Repository, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/sewer-code-search-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-03-09
ingested: 2026-11-15
tags: [apps, replit, code-library]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of MapSWMMSewer - Code Repository, version 1.0.0: a private app that stores code files associated with SWMM, sewer analysis and h2oCalc as text, and lets its user search, filter, view, add, edit and delete them. It is one of Bob's Replit apps, at `sewer-code-search.replit.app`. Raw file: [raw/apps/sewer-code-search-v1.0.0.md](../../raw/apps/sewer-code-search-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says build-time AI use is not documented. The copy here was read out of the editor of the Replit project named Sewer Code Search on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It runs none of the stored code and no simulation engine.
- The development database held 16 records: 6 SWMM, 3 Sewer and 7 h2oCalc, in 4 distinct language values and 2,759 code lines. The API returned 84 distinct tags.
- The content sources named in `server/seed.ts` are EPA SWMM 5.2, ICM SWMM, InfoSWMM, InfoSewer, InfoAsset and h2oCalc. Their licenses are not stated, and the correctness of the stored code was not checked.
- Deployment metadata reports a private deployment.
- `npm run check` passed. No test script exists.

**Limits it states.** The production database was not queried and the production page was not loaded. Create, update, delete, search and filter were not covered by tests.

**Checked at ingest.** 6 + 3 + 7 = 16. This file was held back when the others were committed, because the app is private; Bob said on 15 November 2026 that it may go into the public repository (log).

**Feeds:** [MapSWMMSewer Code Repository (app)](../entities/mapswmmsewer-code-repository.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md).

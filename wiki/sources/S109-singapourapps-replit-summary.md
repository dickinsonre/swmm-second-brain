---
title: "S109: SingaPourApps, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/singa-pour-site-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2025-12-24
ingested: 2026-11-15
tags: [apps, replit, swmm5, inp-format]
reviewed: no
---
**What it is.** A technical summary of SingaPourApps, version 1.0.0: an app that parses a SWMM `.inp` file into three views: rainfall time series, subcatchment parameters, and drainage nodes and conduits. It is one of Bob's Replit apps, at `singa-pour-site--robertdickinson.replit.app`. Raw file: [raw/apps/singa-pour-site-v1.0.0.md](../../raw/apps/singa-pour-site-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says no AI tool use is recorded in the inspected source or documentation. The copy here was read out of the editor of the Replit project named SingaPour Site on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It parses and summarizes; it runs no runoff simulation and no SWMM engine.
- Rainfall: it adds the time-series values for a total depth and takes the largest sample as peak intensity. It does not calculate intensity from elapsed time.
- Discharge: it flags nodes with positive surcharge depth, and nodes whose parsed maximum depth is greater than zero and less than `2`.
- Uploaded model text and analysis results are stored in PostgreSQL.
- Counts: 5 browser routes, 3 analysis tools, 3 database tables, 8 API routes. The development database held 0 model records.
- On the published site the home page returned HTTP `200` and `GET /api/models` returned HTTP `404`. Deployment metadata reports a `static` deployment; `.replit` specifies `autoscale` for the next one.
- `npm run check` passed. No test cases ran.

**Limits it states.** No model was uploaded and no analysis was run. Why the published API route is unavailable is not established. The date is the latest in the Git history, not a release date.

**Checked at ingest.** A static deployment would explain an API route that answers 404; the file does not draw that conclusion and neither does this page.

**Feeds:** [SingaPourApps (app)](../entities/singapourapps.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [EPA SWMM 5](../entities/swmm-5.md).

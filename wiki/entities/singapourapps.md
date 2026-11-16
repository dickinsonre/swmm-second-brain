---
title: SingaPourApps (app)
type: entity
updated: 2026-11-15
sources: [S109]
tags: [apps, replit, swmm5, inp-format]
reviewed: 11/16/2026
---
Bob's Replit app SingaPourApps: an app that parses a SWMM `.inp` file into three views: rainfall time series, subcatchment parameters, and drainage nodes and conduits. Version 1.0.0, at `singa-pour-site--robertdickinson.replit.app` [S109](../sources/S109-singapourapps-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S109](../sources/S109-singapourapps-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S109](../sources/S109-singapourapps-replit-summary.md)
- It parses and summarizes; it runs no runoff simulation and no SWMM engine.
- Rainfall: it adds the time-series values for a total depth and takes the largest sample as peak intensity. It does not calculate intensity from elapsed time.
- Discharge: it flags nodes with positive surcharge depth, and nodes whose parsed maximum depth is greater than zero and less than `2`.
- Uploaded model text and analysis results are stored in PostgreSQL.
- Counts: 5 browser routes, 3 analysis tools, 3 database tables, 8 API routes. The development database held 0 model records.
- On the published site the home page returned HTTP `200` and `GET /api/models` returned HTTP `404`. Deployment metadata reports a `static` deployment; `.replit` specifies `autoscale` for the next one.
- `npm run check` passed. No test cases ran.

**What it does not show.** No model was uploaded and no analysis was run. Why the published API route is unavailable is not established. The date is the latest in the Git history, not a release date. [S109](../sources/S109-singapourapps-replit-summary.md)

**Noted at ingest.** A static deployment would explain an API route that answers 404; the file does not draw that conclusion and neither does this page.

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [EPA SWMM 5](swmm-5.md).

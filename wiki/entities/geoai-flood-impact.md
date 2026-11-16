---
title: GeoAI Flood Impact (app)
type: entity
updated: 2026-11-15
sources: [S113]
tags: [apps, replit, flood-exposure, not-swmm]
reviewed: 11/16/2026
---
Bob's Replit app GeoAI Flood Impact: a decision-support app that presents stored flood-exposure information for communities and infrastructure. It runs no flood model and is not about SWMM. Version 2.4.1_b, at `spatial-impact-insight.replit.app` [S113](../sources/S113-geoai-flood-impact-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S113](../sources/S113-geoai-flood-impact-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S113](../sources/S113-geoai-flood-impact-replit-summary.md)
- Exposure scores, impact categories and component scores are stored values; the database schema defines no formula for them.
- The development database held 5 districts, 30 communities, 22 infrastructure records and 8 workflow-step records.
- Priority areas are the first eight communities by exposure score, leaving out those whose response is complete.
- A community's nearby infrastructure is the first five assets in the same district by a coordinate-space ordering, not a geodesic distance.
- No live satellite, geospatial or simulation service was found in the code; the workflow view displays database descriptions.
- Quantities stay metric, in square kilometers and meters, with no conversion to US customary units.
- `pnpm run typecheck` passed. No test script was found.

**What it does not show.** Data provenance, the validity of the stored scores and agreement with observed floods were not checked. Production records and pages were not tested. The status update route was not exercised. [S113](../sources/S113-geoai-flood-impact-replit-summary.md)

**Noted at ingest.** The version string is `2.4.1_b` (Q68).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [City Temperature Explorer (app)](city-temperature-explorer.md).

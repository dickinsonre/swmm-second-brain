---
title: "S113: GeoAI Flood Impact, summary written by Replit Agent (v2.4.1_b)"
type: source
raw: raw/apps/spatial-impact-insight-v2.4.1_b.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, flood-exposure, not-swmm]
reviewed: 11/16/2026
---
**What it is.** A technical summary of GeoAI Flood Impact, version 2.4.1_b: a decision-support app that presents stored flood-exposure information for communities and infrastructure. It runs no flood model and is not about SWMM. It is one of Bob's Replit apps, at `spatial-impact-insight.replit.app`. Raw file: [raw/apps/spatial-impact-insight-v2.4.1_b.md](../../raw/apps/spatial-impact-insight-v2.4.1_b.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says Git history attributes the application and documentation commits to Replit Agent. The copy here was read out of the editor of the Replit project named Spatial Impact Insight on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Exposure scores, impact categories and component scores are stored values; the database schema defines no formula for them.
- The development database held 5 districts, 30 communities, 22 infrastructure records and 8 workflow-step records.
- Priority areas are the first eight communities by exposure score, leaving out those whose response is complete.
- A community's nearby infrastructure is the first five assets in the same district by a coordinate-space ordering, not a geodesic distance.
- No live satellite, geospatial or simulation service was found in the code; the workflow view displays database descriptions.
- Quantities stay metric, in square kilometers and meters, with no conversion to US customary units.
- `pnpm run typecheck` passed. No test script was found.

**Limits it states.** Data provenance, the validity of the stored scores and agreement with observed floods were not checked. Production records and pages were not tested. The status update route was not exercised.

**Checked at ingest.** The version string is `2.4.1_b` (Q68).

**Feeds:** [GeoAI Flood Impact (app)](../entities/geoai-flood-impact.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [City Temperature Explorer (app)](../entities/city-temperature-explorer.md).

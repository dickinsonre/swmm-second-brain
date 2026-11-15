---
title: City Temperature Explorer (app)
type: entity
updated: 2026-11-15
sources: [S112]
tags: [apps, replit, climate, not-swmm]
reviewed: no
---
Bob's Replit app City Temperature Explorer: an app that compares monthly city temperatures across decades, an urban place with a rural one, and sample cities against preferred summer and winter ranges. It is not about SWMM. Version 1.0.0, at `temp-monitor-1.replit.app` [S112](../sources/S112-city-temperature-explorer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S112](../sources/S112-city-temperature-explorer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S112](../sources/S112-city-temperature-explorer-replit-summary.md)
- Four tools: Climate Shift, Heat Island, Climate Match and Explorer. Daily data come from the Open-Meteo archive and are averaged by calendar month.
- Seven decade options, from the 1960s through the 2020s; thirty sample cities for Climate Match; three preset comparisons.
- Server values are Celsius; display defaults to Fahrenheit by `°F = °C × 9/5 + 32`.
- Responses are cached in server memory for 30 minutes.
- When the pages were loaded, Climate Shift and Heat Island received HTTP 429 rate-limit responses from the data API.
- When a month has no values, the averaging helper returns zero, which may look like a measured zero.
- `npm run check` passed. No test script.

**What it does not show.** City autocomplete, CSV downloads and the Climate Match search were not checked. Live data was not consistently available during the checks. [S112](../sources/S112-city-temperature-explorer-replit-summary.md)

**Noted at ingest.** Nothing to cross-check: no other source here covers this app.

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [GeoAI Flood Impact (app)](geoai-flood-impact.md).

---
title: "S112: City Temperature Explorer, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/temp-monitor-1-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-03-16
ingested: 2026-11-15
tags: [apps, replit, climate, not-swmm]
reviewed: no
---
**What it is.** A technical summary of City Temperature Explorer, version 1.0.0: an app that compares monthly city temperatures across decades, an urban place with a rural one, and sample cities against preferred summer and winter ranges. It is not about SWMM. It is one of Bob's Replit apps, at `temp-monitor-1.replit.app`. Raw file: [raw/apps/temp-monitor-1-v1.0.0.md](../../raw/apps/temp-monitor-1-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says project records do not identify an AI tool used to build it. The copy here was read out of the editor of the Replit project named Temp Monitor on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Four tools: Climate Shift, Heat Island, Climate Match and Explorer. Daily data come from the Open-Meteo archive and are averaged by calendar month.
- Seven decade options, from the 1960s through the 2020s; thirty sample cities for Climate Match; three preset comparisons.
- Server values are Celsius; display defaults to Fahrenheit by `°F = °C × 9/5 + 32`.
- Responses are cached in server memory for 30 minutes.
- When the pages were loaded, Climate Shift and Heat Island received HTTP 429 rate-limit responses from the data API.
- When a month has no values, the averaging helper returns zero, which may look like a measured zero.
- `npm run check` passed. No test script.

**Limits it states.** City autocomplete, CSV downloads and the Climate Match search were not checked. Live data was not consistently available during the checks.

**Checked at ingest.** Nothing to cross-check: no other source here covers this app.

**Feeds:** [City Temperature Explorer (app)](../entities/city-temperature-explorer.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [GeoAI Flood Impact (app)](../entities/geoai-flood-impact.md).

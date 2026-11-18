---
name: Des Moines Sewer to SWMM5
file: des-moines-sewer-swmm5.html
version: "1.0"
date: 2026-10-18
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://des-moines-sewer-swmm5.netlify.app", artifact: "https://claude.ai/artifact/2YiGfcdDKaWtVbBvz64Sr7", data: "City of Des Moines open data hub, data.dsm.city", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4", note: "compiled natively with gcc and to wasm32-wasi with zig cc for the page"}
units: US customary (ft, in, ac, cfs)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Opus 5.5) in October 2026 at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/2YiGfcdDKaWtVbBvz64Sr7, version 1792405935-f728 (index.html, 1,299,521 bytes, SHA-256 00c0ed9679c59fb11c20242640671f5bde50944e2ea55dc5b08f2d04f7d14a1e), its tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Des Moines Sewer to SWMM5: from a city's public sewer GIS to an EPA SWMM5 model, checked in the browser

## In three points
- **What:** A working bridge from the City of Des Moines' public sewer GIS (sanitary and storm pipe and structure layers) to an EPA SWMM 5.2 input file, by a fixed, documented set of import rules, with EPA SWMM 5.2.4 running in the page. It ships two samples from real city records: the whole sewershed above manhole CCH030 (34 pipes, 35 structures, 10,869 ft of 8 to 15 in sewer built 1918 to 1979) and a 54-pipe storm box with placeholder subcatchments.
- **So what:** It shows what public GIS gives a modeler and what it does not. The sanitary sample as published has adverse nodes that put routing continuity at 6.184%; with two documented repairs it is -0.040%. 29 of 35 manhole depths are estimated from assumed cover, there are no pump or force-main data, and loads, Manning n and the storm parameters are placeholders.
- **Now what:** Use it as a pattern for importing a city's open sewer layers into SWMM5, and treat the samples' flows as meaningless until the placeholders are replaced. Which record is wrong at the adverse nodes is a question for the city.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-18"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Model, Results, City data, Import, Import log, Data & rules, .inp, Docs, About. Live mode queries the city's services when the page is opened from a web host or local disk (live queries are blocked inside the Claude viewer, where the file route is explained). The City data tab charts whole-city statistics from 83 grouped-statistics and count queries run on the city's server on 18 October 2026. Results show a themed map, profile, time series, scatter, system, continuity and summary charts, and the engine's own .rpt.

## Checks (as stated on the page)

- Sample records read twice through different queries and compared by script: sanitary 34 pipes and 35 structures, no disagreements; storm 54 pipes and 48 structures, one disagreement (the downstream structure of OBJECTID 9402), settled by a third read and the geometry.
- Projection: three manholes in EPSG:4326 and EPSG:3418 agree within 0.06 ft after the measured datum shift; four pipe ends within 0.05 ft.
- Engine: native and wasm builds give byte-identical .out files on the sanitary sample; on the storm sample the largest difference is 0.06% of a peak, from different math libraries.
- The .out reader matches the report for all 69 sanitary elements and all 49 storm subcatchments.
- Continuity (native 5.2.4): sanitary repaired -0.040%, as published 6.184%; storm runoff -0.443%, routing 0.621%.
- Citywide groupings add up exactly to each layer's record count (22,815; 22,406; 31,285; 33,329) and length (5,550,394.5 and 3,224,209.5 ft).
- The 49 storm cells add up to 41.0170 ac, the exact area of the padded box: no gaps or overlaps.

## What this does not show

As the page lists it: loads, the diurnal pattern, Manning n, storm subcatchment parameters and the test storm are placeholders; elevations are on the city's local datum and unchecked against survey; force mains import as gravity conduits; the two adverse-node repairs are a modeling convenience; sample pipes are straight lines between end vertices (live imports keep every vertex); the City data map shows only the records in the model. No person has reviewed the import rules against the city's records.

## How to reproduce

Data & rules lists the import rules; Import runs a live import from the city's services; .inp shows the written file.

## Credits and licenses

City of Des Moines open data (Sanitary Sewer Pipes, Sanitary Sewer Structures, Storm Sewer Pipes, Storm Sewer Structures): data © City of Des Moines, Iowa 2025, all rights reserved, reference only; the two samples are small extracts kept for demonstration, with credit. EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model (Claude Opus 5.5), in October 2026 at the request of Robert (Bob) Dickinson, who chose the data source and the goal. Claude found the four city layers, read their schemas and terms, cross-checked the samples, designed the import rules and wrote the importer, the WebAssembly build, the readers, the graphics, the citywide queries, the page and the Docs essay "Downhill All the Way" in the manner of Isaac Asimov. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-18): first version (the version read).

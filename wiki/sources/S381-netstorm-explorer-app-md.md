---
title: "S381: NetSTORM Explorer, app .md (v1.0.0)"
type: source
raw: raw/apps/netstorm-explorer.md
kind: app-md
author: Robert Dickinson
published: 2026-11-18
ingested: 2026-11-19
tags: [apps, history, netstorm, rainfall, storm]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app NetSTORM Explorer, version 1.0.0: a searchable map of CDM Smith's NetSTORM web page. Raw file: [raw/apps/netstorm-explorer.md](../../raw/apps/netstorm-explorer.md).

**How it was written.** The app ships this file. Its AI-use section says it "was built with Claude, Anthropic's AI model, in one session on November 18, 2026, at the request of Robert (Bob) Dickinson." Claude read the NetSTORM page through a web text reader, wrote every index entry, tagged each release note by module and kind, and supplied 50 web addresses and all the one-line notes from general knowledge. The checks are mechanical; no person has compared the entries with the page or opened any of the 50 supplied addresses. The file says CDM Smith had no part in the app. It does not open with an In three points block.

**Claims worth keeping** (all copied from the file)
- NetSTORM is CDM Smith's free Windows program for storage-treatment-overflow modeling (after HEC-STORM), rainfall IDF analysis, time series aggregation and disaggregation, weather data import, and SWMM and MOUSE calibration reporting.
- The app indexes one web page, http://www.dynsystem.com/netstorm/, read on November 18, 2026, into five views: Map, Resources, Changelog, Modules and Index. It has no engine and no numerical method.
- Two separate reads of the page agreed on 79 link labels in 10 categories and on 13 release groups. They disagreed by one on the entry count, 138 against 137, from bullet splitting on multi-bullet lines; the app uses 138.
- Link addresses read from the page: 0, because the reader dropped them. 50 addresses were supplied by Claude from general knowledge, unverified; 29 links are search-only.
- Release notes by module, tagged by Claude: CSReporter 36, IDF 22, STORM 18, Read 20, Transform 18, SWMM5 Simplification 6, CSInterfacer 2, Platform 16.
- An open point from the page itself: its introduction credits NetSTORM with multi-structure STORM modeling, while the release note for the C# rewrite (group 7) says multi-structure modeling was omitted. The page does not say whether it returned.
- 63 of 63 app tests pass in headless Chromium. The SWMM App Complexity Meter was not run.

**Limits it states.** The page's own link addresses are missing. The page gives no release dates or version numbers for its 13 groups; dating clues are inference. Every entry is reworded. No NetSTORM run was made. A second copy of the page at http://dynsystem.com/netstorm/ differs from the one indexed.

**Checked at ingest.** The counts add up (our arithmetic): the 13 groups' entries (2, 4, 12, 7, 12, 3, 19, 11, 11, 14, 17, 13, 13) sum to 138, as do the module counts and the kind counts (64 + 43 + 25 + 3 + 2 + 1); the categories' links sum to 79, and 50 + 29 = 79. The page's open point is Q123. The `links:` line names no Netlify address and no artifact address. The file name carries no version.

**Feeds:** [NetSTORM Explorer (app)](../entities/netstorm-explorer.md).

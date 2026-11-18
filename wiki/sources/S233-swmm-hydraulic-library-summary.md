---
title: "S233: SWMM Hydraulic Library, summary written from the page (v2.0)"
type: source
raw: raw/apps/swmm-hydraulic-library-v2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-21
ingested: 2026-11-17
tags: [apps, swmm5, swmm6, icm, st-venant, teaching]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Hydraulic Library, version 2.0: 70 library entries, each an equation with a SWMM 5, ICM and SWMM 6 note, and 119 interactive diagrams and calculators from Bob's SWMM-ICM-StVenant project, rebuilt from his Lovable app into one file. No engine runs; the diagrams and calculators are teaching models. Raw file: [raw/apps/swmm-hydraulic-library-v2.0.md](../../raw/apps/swmm-hydraulic-library-v2.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792597788-50a9, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says Bob built the original in Lovable and supplied its source; version 2.0 was rebuilt with Claude in a session on 21 October 2026 under his direction. Claude ported it to one client-only file, replaced the server, sign-in and AI gateway, and ran eight audits, seven in parallel sub-agents.

**Claims worth keeping** (all copied from the file)
- The physics is Saint-Venant's (1871); the page puts the disagreement among EPA SWMM 5, InfoWorks ICM and SWMM 6 in the arithmetic: where each keeps its unknowns, when it evaluates them, and what it does when the arithmetic fails.
- Each of the 119 diagrams is one React component in one of 26 files; entries and diagrams are linked when they share words.
- Eight audits read all 26 diagram files, the 70 entries and the benchmark page and fixed 199 defects, units errors the commonest; they flagged 114 more without changing them; 197 pages were swept headless with 0 console errors after.
- The Lovable original sent questions to an OpenAI model through Lovable's gateway; version 2.0 asks Claude, inside a Claude artifact on the viewer's account or elsewhere with the viewer's own Anthropic API key kept in memory only.
- The OpenSWMM reference manual is cited at swmm6_rel @ fbd1d7b0.

**Limits it states.** No engine runs. On Netlify, Ask AI and shared saving fall back to the viewer's own API key and the browser.

**Checked at ingest.** Nothing in the summary can be checked by arithmetic. The three-engine comparison the library teaches is the subject of [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md) and [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm-hydraulic-library.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM Hydraulic Library (app)](../entities/swmm-hydraulic-library.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [SWMM and ICM St. Venant comparison (app)](../entities/swmm-icm-st-venant-app.md).

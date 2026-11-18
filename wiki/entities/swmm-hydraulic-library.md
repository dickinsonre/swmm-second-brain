---
title: "SWMM Hydraulic Library (app)"
type: entity
updated: 2026-11-17
sources: [S205, S233]
tags: [apps, swmm5, swmm6, icm, st-venant, teaching]
reviewed: no
---
Bob's app SWMM Hydraulic Library: 70 library entries, each an equation with a SWMM 5, ICM and SWMM 6 note, and 119 interactive diagrams and calculators from Bob's SWMM-ICM-StVenant project, rebuilt from his Lovable app into one file. No engine runs; the diagrams and calculators are teaching models. Version 2.0, 2026-10-21 [S233](../sources/S233-swmm-hydraulic-library-summary.md). Netlify address: https://swmm-hydraulic-library.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S233](../sources/S233-swmm-hydraulic-library-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S233](../sources/S233-swmm-hydraulic-library-summary.md)
- The physics is Saint-Venant's (1871); the page puts the disagreement among EPA SWMM 5, InfoWorks ICM and SWMM 6 in the arithmetic: where each keeps its unknowns, when it evaluates them, and what it does when the arithmetic fails.
- Each of the 119 diagrams is one React component in one of 26 files; entries and diagrams are linked when they share words.
- Eight audits read all 26 diagram files, the 70 entries and the benchmark page and fixed 199 defects, units errors the commonest; they flagged 114 more without changing them; 197 pages were swept headless with 0 console errors after.
- The Lovable original sent questions to an OpenAI model through Lovable's gateway; version 2.0 asks Claude, inside a Claude artifact on the viewer's account or elsewhere with the viewer's own Anthropic API key kept in memory only.
- The OpenSWMM reference manual is cited at swmm6_rel @ fbd1d7b0.

**What it does not show.** No engine runs. On Netlify, Ask AI and shared saving fall back to the viewer's own API key and the browser. [S233](../sources/S233-swmm-hydraulic-library-summary.md)

**Noted at ingest.** Nothing in the summary can be checked by arithmetic. The three-engine comparison the library teaches is the subject of [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md) and [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md).

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [SWMM and ICM St. Venant comparison (app)](swmm-icm-st-venant-app.md).

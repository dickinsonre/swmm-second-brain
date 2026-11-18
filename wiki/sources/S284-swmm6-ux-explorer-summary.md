---
title: "S284: SWMM6 UX Explorer, summary written from the page (v2026-11-03)"
type: source
raw: raw/apps/swmm6-ux-explorer-v2026-11-03.md
kind: app-md
author: Robert Dickinson
published: 2026-11-03
ingested: 2026-11-18
tags: [apps, swmm6, user-interface, design-storms, atlas-14, usgs]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM6 UX Explorer, version 2026-11-03: a single-file browser copy of the SWMMVis desktop workspace for OpenSWMM 6 alpha.4 around a small live model (59 junctions, 59 conduits, 58 subcatchments on 222 ac), with NOAA Atlas 14, USGS and 3DEP data tools and three candidate design storms; it also reads and writes a SWMM5 file. Raw file: [raw/apps/swmm6-ux-explorer-v2026-11-03.md](../../raw/apps/swmm6-ux-explorer-v2026-11-03.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/L9wrbfR7L97GDMYwWXZNvB, version 1793763272-a53c (index.html, 1,046,093 bytes, SHA-256 d69ce79d29109a519690c7dc96d81a00fe4899ac21615f583526fbfbe532b755), every tab read in headless Chromium on 2026-11-18. The page gives no version number; the version above is the date of its last revision as the Doc states it. Nothing was run to write this file." The page says it was made with Claude in sessions on 31 October and 2 and 3 November 2026 under Bob's direction, extending his August app, with two outside reviews.

**Claims worth keeping** (all copied from the file)
- Atlas 14 gives 4.82 in for the 10-year, 24-hour storm at 38.9 N, 77.0 W, the 122 mm (122.4 mm) in the SWMMVis alpha.4 release graphic.
- Three storms of the same 4.82 in: SCS Type II 315.7 cfs, alternating block 296.9, triangle 47.1 at the outfall in the demo engine, each with 2,080,214 ft3 of runoff; EPA SWMM 5.2.4 on the exported files gives 373.4, 357.9 and 49.6.
- The alternating block matches Atlas 14 at 9 of 10 durations up to 24 hours and runs 1.7% high at 3 hours.
- All 58 subcatchment outlines match their modeled areas (largest relative error 9 x 10^-13) with zero overlap across 1,653 pairs.
- The USGS Water Data API path returned the same 888 daily values, 18 ice days and two peaks as the older WaterServices snapshot.

**Limits it states.** No SWMMVis code runs; its look follows the manual's screenshots, not SWMMVis on Windows; the demo engine is not SWMM; the storm ranking speaks for this network at this location; outlines true in area, invented in shape; elevation is a 40 x 40 sample, about 295 ft per cell.

**Checked at ingest.** 4.82 x 25.4 = 122.4 mm (our arithmetic, as the Doc states). The `links:` line gives Netlify as https://swmm6-ux-explorer.netlify.app.

**Feeds:** [SWMM6 UX Explorer (app)](../entities/swmm6-ux-explorer.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Subcatchment width](../concepts/subcatchment-width.md).

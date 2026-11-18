---
title: "S351: SWMM Guide Buddy, summary written from the page (v1.0)"
type: source
raw: raw/apps/swmm-guide-buddy-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, swmm5, manuals, calculators]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Guide Buddy, version 1.0: a companion to the EPA SWMM Applications Manual, with checked calculators. Raw file: [raw/apps/swmm-guide-buddy-v1.0.md](../../raw/apps/swmm-guide-buddy-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/JrtpowoQUHnJJ5J7YT62Cp, version 1792896871-5240 (index.html, 3,403,171 bytes, SHA-256 8a6f5b99a6f28c6a475fee360438a90cbafb4122828ae47ab2f33722f08ab56a), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: the original app was generated with Lovable, an AI app builder, under Bob Dickinson's direction. This edition was built with Claude, Anthropic's AI model, in October 2026 at his request; he chose the project and supplied the source, and responsibility is his."

**Claims worth keeping** (all copied from the file)
- A companion to the EPA Storm Water Management Model Applications Manual (EPA/600/R-09/000, 2009) as adapted for InfoSWMM: nine worked-example pages and a bench of hydraulic calculators (normal and critical depth, pipe capacity, culverts by FHWA HDS-5, a 3D profile viewer, a routing advisor). A single-file edition of Bob's Lovable project.
- The Lovable calculators reported a surcharged pipe as 99% full, drew the profile from a formula instead of solving the energy equation, and did not use the real HDS-5 equations; the edition fixes these and seventeen defects are listed with their original code. 447 mechanical comparisons against independent Python re-computations pass, for example normal and critical depth against scipy's brentq to 2.5 x 10^-10. Examples 1 and 3 now quote the manual's tables; invented numbers elsewhere are tagged amber.
- Normal and critical depth, 49 checks over rectangular, trapezoidal, triangular and circular sections, against scipy.optimize.brentq (circular geometry from the chord): worst relative difference 2.5 x 10^-10.
- Pipe capacity: Qfull and the 0.938·D hump by brute-force scan, 12 cases, worst 3.5 x 10^-8.
- Culvert inlet control, 170 cases: the app computes headwater from flow; a Python port of SWMM 5.2's culvert.c computes flow from that headwater; the round trip returns the starting flow to 3 x 10^-13 for every case across all ten inlet codes.
- Culvert outlet control, 170 cases, worst 2.4 x 10^-11; a sweep shows headwater rising monotonically with flow for every inlet code.

**Limits it states.** As the page lists it: no SWMM run (the examples quote published results; the manual's hydrographs, its Example 3 pond design and with-pond peaks, and its Example 9 statistics are not in the app); single-section, steady-flow hand methods, with one rectangular reach and one control in the profile viewer, and no network model; HDS-5 inlet and full-flow outlet control only, with no partly full backwater, multiple barrels, overtopping or improved inlets (SWMM applies its culvert codes only under dynamic wave and switches to its transition zone at 0.95·D).

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM Guide Buddy (app)](../entities/swmm-guide-buddy.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [SWMM5 Manual Search (app)](../entities/swmm5-manual-search.md), [Six quality markers for app-building work](../concepts/app-quality-markers.md).

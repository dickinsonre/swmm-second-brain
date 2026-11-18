---
title: "SWMM Guide Buddy (app)"
type: entity
updated: 2026-11-18
sources: [S351]
tags: [apps, swmm5, manuals, calculators]
reviewed: no
---
Bob's app SWMM Guide Buddy: a companion to the EPA SWMM Applications Manual, with checked calculators. Version 1.0, 2026-10-24 [S351](../sources/S351-swmm-guide-buddy-summary.md). Its `links:` line names no live Netlify address [S351](../sources/S351-swmm-guide-buddy-summary.md).

**A caution about its source.** The page ships no technical summary. [S351](../sources/S351-swmm-guide-buddy-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S351](../sources/S351-swmm-guide-buddy-summary.md)
- A companion to the EPA Storm Water Management Model Applications Manual (EPA/600/R-09/000, 2009) as adapted for InfoSWMM: nine worked-example pages and a bench of hydraulic calculators (normal and critical depth, pipe capacity, culverts by FHWA HDS-5, a 3D profile viewer, a routing advisor). A single-file edition of Bob's Lovable project.
- The Lovable calculators reported a surcharged pipe as 99% full, drew the profile from a formula instead of solving the energy equation, and did not use the real HDS-5 equations; the edition fixes these and seventeen defects are listed with their original code. 447 mechanical comparisons against independent Python re-computations pass, for example normal and critical depth against scipy's brentq to 2.5 x 10^-10. Examples 1 and 3 now quote the manual's tables; invented numbers elsewhere are tagged amber.
- Normal and critical depth, 49 checks over rectangular, trapezoidal, triangular and circular sections, against scipy.optimize.brentq (circular geometry from the chord): worst relative difference 2.5 x 10^-10.
- Pipe capacity: Qfull and the 0.938·D hump by brute-force scan, 12 cases, worst 3.5 x 10^-8.
- Culvert inlet control, 170 cases: the app computes headwater from flow; a Python port of SWMM 5.2's culvert.c computes flow from that headwater; the round trip returns the starting flow to 3 x 10^-13 for every case across all ten inlet codes.
- Culvert outlet control, 170 cases, worst 2.4 x 10^-11; a sweep shows headwater rising monotonically with flow for every inlet code.

**How to use it, as the summary puts it.** Use it beside the manual to work its examples and check hand calculations. No SWMM run happens in the page; the calculators are single-section, steady-flow hand methods, and the culvert tool covers HDS-5 inlet and full-flow outlet control only. [S351](../sources/S351-swmm-guide-buddy-summary.md)

**What it does not show.** As the page lists it: no SWMM run (the examples quote published results; the manual's hydrographs, its Example 3 pond design and with-pond peaks, and its Example 9 statistics are not in the app); single-section, steady-flow hand methods, with one rectangular reach and one control in the profile viewer, and no network model; HDS-5 inlet and full-flow outlet control only, with no partly full backwater, multiple barrels, overtopping or improved inlets (SWMM applies its culvert codes only under dynamic wave and switches to its transition zone at 0.95·D). [S351](../sources/S351-swmm-guide-buddy-summary.md)

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [SWMM5 Manual Search (app)](swmm5-manual-search.md), [Six quality markers for app-building work](../concepts/app-quality-markers.md).

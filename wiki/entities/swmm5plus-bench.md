---
title: "SWMM5+ Bench (app)"
type: entity
updated: 2026-11-17
sources: [S192, S205, S222]
tags: [apps, swmm5plus, swmm5, finite-volume, comparison]
reviewed: no
---
Bob's app SWMM5+ Bench: one SWMM model run through two dynamic-wave engines side by side: CIMM's finite-volume SWMM5+ 1.0.3 through Ehsan Madadi's swmm5plus-capi C interface (recorded runs, or a Live bridge to a local library), and EPA SWMM 5.2.4 compiled into the page; 34 models recorded. Version 1.0, 2026-10-24 [S222](../sources/S222-swmm5plus-bench-summary.md). Netlify address: https://swmm5plus-bench.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S222](../sources/S222-swmm5plus-bench-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S222](../sources/S222-swmm5plus-bench-summary.md)
- SWMM5+ is about 88,000 lines of modern Fortran built around coarrays and HDF5, usually run in a container; swmm5plus-capi v0.2.1 builds it as an ordinary shared library (interface version 2, EPA SWMM 5.1.13 parser). SWMM5+ is CIMM-ORG/SWMM5plus at afd44de (2024-11-25).
- EXTRAN4 as shipped: EPA floods 178 ac-ft (21.9 ha-m), 15.0 % of the inflow, at two nodes (an upstream end and a node with two links); in SWMM5+ both are faces and cannot flood.
- Changing one weir's Surcharge flag from NO to YES gives both engines the same equivalent-orifice formula above the crown, and the weir peaks come back within 1.9 %.
- Example 1 at five-minute reporting: the SWMM5+ record shows 279,414 ft3 of lateral inflow and 294,105 ft3 of outflow (5.3 % more out than in); subtracting the 14,421 ft3 that subcatchment 8 sends straight to outfall 18 closes the budget to 0.1 %.
- SWMM5+ is explicit: on EXTRAN4 a mean step of 0.119 s and 241,021 steps for eight hours.
- The four Linux files of the v0.2.1 release match the SHA-256 values in its SHA256SUMS. The page's EPA engine wrote a .out byte-identical to native on 32 of 33 models.
- 34 models recorded on Linux x86-64 (2 cores) on 24 October 2026 through s5p_run.py, the driver the bridge uses.

**What it does not show.** No field data, so it cannot say which engine is right on a real system. SWMM5+ does not run in the browser. [S222](../sources/S222-swmm5plus-bench-summary.md)

**Noted at ingest.** 294,105 - 14,421 = 279,684 ft3 against 279,414 in, a 0.1 % difference (our arithmetic). 241,021 x 0.119 s = 28,681 s, about eight hours. The weir surcharge flag is the same one that moves EXTRAN4 node 82309 from 12.03 ft to 20.28 ft on [SWMM QA Report Bench (app)](swmm-qa-report-bench.md) [S192](../sources/S192-swmm-qa-report-bench-app-md.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [SWMM5+ (CIMM finite-volume engine)](swmm5plus.md), [Mirab Test Bench (app)](mirab-test-bench.md), [Weirs and outlets](../concepts/weirs-and-outlets.md), [SWMM QA Report Bench (app)](swmm-qa-report-bench.md).

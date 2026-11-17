---
title: SWMM QA Report Bench (app)
type: entity
updated: 2026-11-17
sources: [S192, S185]
tags: [apps, swmm4, swmm5, dynamic-wave, verification, comparison]
reviewed: no
---
Bob's app that carries EPA's 2006 quality assurance report, turns its figures into data, and runs [EPA SWMM 5](swmm-5.md) 5.2.4 on the same twenty models beside them. Version 2.0.0, 12 November 2026 [S192](../sources/S192-swmm-qa-report-bench-app-md.md). The report itself is digested on [SWMM 4 against SWMM 5: the 2006 quality assurance tests](../concepts/swmm4-versus-swmm5-qa-2006.md) [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md).

**What it holds** [S192](../sources/S192-swmm-qa-report-bench-app-md.md)
- The full 115-page PDF, with a page viewer and text search.
- 122 time series charts and 19 scatter figures (852 markers) measured off the PDF's vector content, each axis fitted to its tick labels.
- 46 runs of EPA SWMM 5.2.4 built from source: the 20 models with the report's Table 3.1 options, the 20 as distributed, and 6 large-step variants. Input files from OpenWaterAnalytics/swmm-nrtestsuite.
- A scorecard of 5.2.4 against the 2006 SWMM 5 curve at 111 locations.

**What it found** [S192](../sources/S192-swmm-qa-report-bench-app-md.md)
- 100 of 111 peaks within 5 % of the 2006 SWMM 5 figure; 75 within 1 %; median difference 0.51 %.
- Six over 10 %, 2006 SWMM 5 against 5.2.4: EXTRAN10 link 90002, 40.26 against 56.69 cfs (+40.8 %); TEST4 outfall at a 10 s step, 129.3 against 100.2 cfs (-22.5 %; inflow 100 cfs); EXTRAN4 node 82309, 14.21 against 12.03 ft (-15.4 %); USER5 node 5SB6, 6.09 against 5.27 ft (-13.4 %); EXTRAN10 link 90004, 25.64 against 22.66 cfs (-11.6 %); TEST5 node 9, 4.58 against 4.11 ft (-10.2 %). The summary says four of the six are at pumps, a weir and a siphon.
- At the report's large steps SWMM 4's continuity errors were 34.4 %, over 800 % and 619 %; 5.2.4's are -0.174 %, 0.003 % and -2.226 %.
- Four register items: a caption swap in the report (E1), a build-only buffer abort in `swmm5.c` (B1), a weir surcharge flag that moves EXTRAN4's peak depth from 12.03 to 20.28 ft (O1), and its own first version's synthetic curves (A1). See [The SWMM findings register](../concepts/findings-register.md).

**How it began.** The first version drew synthetic curves. Bob asked where the chart values came from when they did not match the paper; version 2.0.0 removed every generator and the unsourced ICM overlay [S192](../sources/S192-swmm-qa-report-bench-app-md.md).

**What it does not show.** That 5.2.4 is correct: the agreement is between versions of one program. SWMM 4.4h and 5.0.006 were not run. Digitized values carry about 1 % of axis span in error. No person has checked the digitized charts or the element matches by hand [S192](../sources/S192-swmm-qa-report-bench-app-md.md).

**Related.** [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [Weirs and outlets](../concepts/weirs-and-outlets.md), [Lewis A. (Lew) Rossman](lew-rossman.md).

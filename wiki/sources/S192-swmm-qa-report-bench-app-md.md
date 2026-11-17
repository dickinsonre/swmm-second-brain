---
title: "S192: SWMM QA Report Bench, technical summary (app .md, v2.0.0)"
type: source
raw: raw/apps/swmm-qa-report-bench-v2.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-17
tags: [apps, swmm4, swmm5, dynamic-wave, verification, comparison, primary-document, findings]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: no
---
**What it is.** The technical summary that ships with SWMM QA Report Bench, version 2.0.0 (12 November 2026). The app carries EPA's 2006 quality assurance report, which compared SWMM 4.4h with SWMM 5.0.006 on 20 dynamic wave models, turns the report's figures into data, and runs EPA SWMM 5.2.4 on the same 20 input files beside them. Raw file: [raw/apps/swmm-qa-report-bench-v2.0.0.md](../../raw/apps/swmm-qa-report-bench-v2.0.0.md).

**How it was written.** By Claude (Anthropic) under Bob's direction, from the build's own runs. The file says Claude wrote the first version "including the synthetic chart generators that Bob caught", then read the curves out of the PDF, compiled SWMM 5.2.4, ran 46 simulations and wrote the app, essay, .docx and this file. Checks are mechanical. No person has compared the 122 digitized charts with the printed figures, reviewed the 111 element matches by hand, or edited the essay.

**Claims worth keeping**
- The report: Lewis A. Rossman, EPA/600/R-06/097, September 2006, 115 pages, public domain. Its 20 cases are EXTRAN1 to 10, TEST1 to 5 and USER1 to 5. Input files from OpenWaterAnalytics/swmm-nrtestsuite, commit e609fdbb (2023-03-01).
- Digitized from the PDF's vector content: 122 time series charts (worst axis fit r2 0.99921) and 19 scatter figures with 852 markers (every r2 at or above 0.99998; the printed 1:1 line recovered within 0.443 % of axis span). About 15 comparison charts and the Appendix A figures are not digitized.
- SWMM 5.2.4 from tag v5.2.4 (commit 7952ca83), built with gcc 13.3.0, `-O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0`. 46 runs: 20 with the report's Table 3.1 options, 20 as distributed, 6 variants. All exit code 0.
- The Table 3.1 option set written into each file: `INERTIAL_DAMPING NONE`, `NORMAL_FLOW_LIMITED SLOPE`, `LENGTHENING_STEP 0`, `MIN_SURFAREA 0` (engine default 12.566 ft2, `dynwave.c:62`), `MAX_TRIALS 4`, `VARIABLE_STEP 0.00`, `THREADS 1`; `HEAD_TOLERANCE` left at its default 0.005 ft (`dynwave.c:63`).
- Scorecard, SWMM 5.2.4 against the 2006 SWMM 5 curve at 111 locations: peak within 1 %: 75; within 2 %: 88; within 5 %: 100; within 10 %: 105; over 10 %: 6. Median absolute peak difference 0.51 %. NSE at or above 0.99: 57; 0.95: 101; 0.90: 102. Median NRMSE 3.12 % of range.
- The six over 10 % (2006 SWMM 5 against 5.2.4): EXTRAN10 link 90002, 40.26 against 56.69 cfs (+40.8 %); TEST4 outfall at a 10 s step, 129.3 against 100.2 cfs (-22.5 %; inflow is 100 cfs; SWMM 4 gave 258.5); EXTRAN4 node 82309, 14.21 against 12.03 ft (-15.4 %); USER5 node 5SB6, 6.09 against 5.27 ft (-13.4 %); EXTRAN10 link 90004, 25.64 against 22.66 cfs (-11.6 %); TEST5 node 9, 4.58 against 4.11 ft (-10.2 %). The summary says four of the six are at pumps, a weir and a siphon.
- Options as distributed against Table 3.1: the largest change in any conduit peak is 3.12 % (USER5).
- Routing continuity of 5.2.4 with the Table 3.1 options: all within 0.72 % except EXTRAN2 (-4.085 %) and USER5 (-2.352 %).
- Continuity at the report's large steps, 2006 SWMM 4 / 2006 SWMM 5 / 5.2.4: TEST3 at 30 s, 34.4 % / 0.02 % / -0.174 %; TEST5 at 10 s, over 800 % / 0.05 % / 0.003 %; USER5 at 5 s, 619 % / 1.29 % / -2.226 %.
- Solver facts cited from 5.2.4: `dynwave.c:61 OMEGA = 0.5`, `dynwave.c:66 DEFAULT_MAXTRIALS = 8`, `dwflow.c:37 MAXVELOCITY = 50.`, `link.c:2046` weir canSurcharge default 1. From the report: SWMM 5.0.006 used 4 trials (report p. 9).
- Register: E1, report erratum: Figures 4.18 and 4.19 (EXTRAN3, p. 25) carry each other's captions. B1, build only: `swmm5.c:1593` calls `realpath` with a 260-byte buffer and fortified glibc builds abort; worked around with `-D_FORTIFY_SOURCE=0`, no effect on results. O1, observation: EXTRAN4 node 82309 peaks at 12.03 ft with the weir's surcharge flag YES (the default) and 20.28 ft with NO; weir peak flow 28.11 against 12.47 cfs; the 2006 figure shows 14.21 ft. A1, the app's own defect, fixed in 2.0.0: version 1 drew synthetic curves (`generateFlowData`) and mislabelled EXTRAN4, 5 and 6.
- Credits: the Extran test cases to "Roesner, Aldrich and Dickinson, SWMM Version 4 Extran Addendum, 1992"; the Challenge test cases to "a suite of test cases compiled by Robert E. Dickinson of CDM" (report p. 13).

**Limits it states.** Agreement is between two versions of one program, not proof that 5.2.4 is right. SWMM 4.4h and SWMM 5.0.006 were not run. 11 digitized locations have no 5.2.4 curve. Digitized values carry about 1 % of axis span in error, and 19 charts are flagged where the report's own SWMM 4 and SWMM 5 peaks differ by more than 15 %. Runoff is compared only through continuity totals. No ICM or SWMM 6 results.

**Checked at ingest.** 105 + 6 = 111; 20 + 20 + 6 = 46. The six percentages, recomputed from the rounded peaks printed, are +40.81, -22.51, -15.34, -13.46, -11.62 and -10.26; three of them differ in the last digit from the printed -15.4, -13.4 and -10.2, presumably because the app computed them from unrounded values. The report's own text, read for [S185](S185-epa-swmm5-qa-report-dynamic-wave-2006.md), also gives 5.0.006 four trials, credits the Challenge cases to Bob, and puts the user systems at 59 to 273 conduits, matching USER1's 59 and USER5's 273 here. The large-step continuity figures come from report chapters not yet read for S185 (Chapters 5 and 6). The "1992" for the Extran Addendum follows the report's reference list, so it is not separate evidence for Q94.

**Feeds:** [SWMM QA Report Bench (app)](../entities/swmm-qa-report-bench.md), [SWMM 4 against SWMM 5: the 2006 quality assurance tests](../concepts/swmm4-versus-swmm5-qa-2006.md), [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [Weirs and outlets](../concepts/weirs-and-outlets.md), [The SWMM findings register](../concepts/findings-register.md), [Open questions](../open-questions.md).

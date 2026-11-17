---
name: SWMM QA Report Bench
file: swmm-qa-report-bench.html
version: 2.0.0
date: 2026-11-12
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: published privately on claude.ai, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: USEPA/Stormwater-Management-Model tag v5.2.4, commit: 7952ca83, license: public domain}
models: OpenWaterAnalytics/swmm-nrtestsuite, commit e609fdbb (2023-03-01)
source_document: EPA/600/R-06/097, Rossman, September 2006, 115 pages, public domain
units: US customary (cfs, ft) for 17 cases; EXTRAN9, USER1 and USER3 are in cms and m as distributed
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM QA Report Bench: the 2006 SWMM 4 vs SWMM 5 dynamic wave QA report, with its figures as data and SWMM 5.2.4 run beside them

## In three points
- **What:** The 2006 EPA report comparing SWMM 4.4h with SWMM 5.0.006 on 20 dynamic wave models, with its 122 time series charts and 19 scatter figures turned into data and SWMM 5.2.4 run beside them.
- **So what:** At 100 of 111 plotted locations the SWMM 5.2.4 peak is within 5% of the 2006 SWMM 5 figure; the largest difference is EXTRAN10 link 90002, 56.69 against 40.26 cfs (+40.8%).
- **Now what:** Read it as agreement between versions of one program, not proof of correctness. SWMM 4.4h and 5.0.006 were not run, and digitized values carry about 1% of axis span in error.

In one sentence: SWMM QA Report Bench sets the 2006 EPA report comparing SWMM 5 with SWMM 4 beside fresh runs of SWMM 5.2.4; at 100 of 111 plotted locations the new peak is within 5% of the 2006 figure.

In one paragraph: In 2006 Lewis Rossman ran SWMM 4.4h and SWMM 5.0.006 on the same 20 dynamic wave models and published 115 pages of comparison. This app carries that report whole. Its curves were measured off the report's own figures: 122 time series charts and 19 scatter figures. The same 20 input files were then run on EPA SWMM 5.2.4, built from source, and scored against the 2006 SWMM 5 curves at 111 locations. The median peak difference is 0.51%, and 75 locations agree within 1%. Six differ by more than 10%, four of them at pumps, a weir and a siphon. The app contains no generated data. It does not show that any of the three programs is right, only how far apart they are.

## What it does

- Shows, for each of the report's 20 test cases (EXTRAN1 to 10, TEST1 to 5, USER1 to 5), the time series the report plotted: SWMM 4.4h (2006) and SWMM 5.0.006 (2006) as digitized from the PDF, and SWMM 5.2.4 computed for this app.
- Shows the report's 19 scatter figures (peak conduit flow, maximum node elevation) as measured markers: 852 in all.
- Scores SWMM 5.2.4 against the 2006 SWMM 5 curve at 111 locations (peak difference, NSE, NRMSE).
- Embeds the full PDF (page viewer, text search, save) and lets the user overlay one pasted series per chart and scores it.
- Tabs: Cases, Scorecard, Method, Report, Verify, About, Doc.

## How it computes

2006 curves (digitized):
- Source is the vector content of the PDF. For each chart frame: collect stroked paths (SWMM 5 line) and filled marker shapes (SWMM 4), find the numeric tick labels, fit page position to axis value linearly in x and y, convert every vertex.
- Scatter figures: markers are filled shapes 2 to 8 pt across in the two series colors; axes fitted the same way; the printed 1:1 line is used as a self-check. Points are stored as (SWMM 4, SWMM 5). Coincident markers are kept.

SWMM 5.2.4 runs:
- Built from source: `gcc -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -fopenmp src/run/main.c src/solver/*.c -lm` (gcc 13.3.0, Linux x86-64).
- "Table 3.1" option set written into each .inp: `INERTIAL_DAMPING NONE`, `NORMAL_FLOW_LIMITED SLOPE`, `LENGTHENING_STEP 0`, `MIN_SURFAREA 0` (engine default 12.566 ft2, dynwave.c:62), `MAX_TRIALS 4`, `VARIABLE_STEP 0.00`, `THREADS 1`, `HEAD_TOLERANCE` not written (default 0.005 ft, dynwave.c:63).
- Control set: each model exactly as distributed (`NORMAL_FLOW_LIMITED BOTH`, default 8 trials).
- Large time step trials from the report: TEST3 at 30 s, TEST4 at 10 s, TEST5 at 10 s, USER3 at 5 s, USER5 at 5 s.
- EXTRAN8 uses the hot start file written by this build's own first-stage run.
- 46 runs in total (20 Table 3.1, 20 as distributed, 6 variants). All exit code 0.
- Series are read from the binary .out file: link flow, node depth, or node total inflow (for charts of flow at a node or outfall).

Matching a chart to a model element:
- By element ID parsed from the chart title (109 locations): "Link X", "Conduit X", "Node X", "Between Nodes A and B" (the unique link A to B), "Upstream End of X" (upstream node of link X), "Outfall" (total inflow at the outfall node).
- By map label (2 locations, USER4 "P2"): nearest conduit to the [LABELS] entry, accepted only when its distance is under half the next nearest.

Scoring (SWMM 5.2.4 vs 2006 SWMM 5 curve):
- The 5.2.4 series is subsampled at the model's original REPORT_STEP (the step the 2006 figures were printed from), then interpolated to the digitized times.
- Peak difference % = (peak524 - peak2006) / peak2006 x 100.
- NSE = 1 - sum((sim - ref)^2) / sum((ref - mean(ref))^2).
- NRMSE % = RMSE / (max(ref) - min(ref)) x 100.
- The display series is the fine (1 minute) output, simplified with Ramer-Douglas-Peucker at 0.3% of range.

Solver facts cited in the app:
- Report Eq. 4: Q(t+dt) = (Q(t) + dQ_gravity + dQ_inertial) / (1 + dQ_friction + dQ_losses).
- Report Eq. 5: H(t+dt) = H(t) + dVol / (A_store + sum(A_s)).
- Report Eq. 6 (surcharged node): dH = -sum(Q) / sum(dQ/dH).
- SWMM 4: modified Euler, half step then full step. SWMM 5: successive approximation, relaxation 0.5, tolerance 0.005 ft, 4 trials in 5.0.006 (report p. 9).
- 5.2.4 source: `dynwave.c:61 OMEGA = 0.5`, `dynwave.c:66 DEFAULT_MAXTRIALS = 8`, `dwflow.c:37 MAXVELOCITY = 50.`, `link.c:2046` weir canSurcharge default 1.

## Inputs and outputs

- Reads nothing from disk except an optional user-pasted or user-loaded two-column series (time in hours, value) per chart. It is kept in memory only.
- Writes on request: CSV of the current chart (all series, long format), CSV of the scorecard, the report PDF, this .md, the essay .docx, and a GIF (or WebM) of the current case.
- External scripts, loaded only on use, from cdnjs: pdf.js 3.11.174, html2canvas 1.4.1, gif.js 0.2.0.

## Checks

Mechanical:
- Axis calibration, 122 time series charts: worst r2 0.99921.
- Axis calibration, 19 scatter figures: every r2 at or above 0.99998; printed 1:1 line recovered within 0.443% of axis span.
- Scatter marker count vs model conduit count: USER1 59 of 59, USER3 134 of 134, USER4 209 of 209; USER2 78 of 83; USER5 244 of 273 (the report omits Detail A conduits).
- Binary reader vs engine text report: EXTRAN1 link 1602 peak 71.991 vs 71.99 cfs; node 82309 max depth 21.834 vs 21.83 ft.
- Option control (Table 3.1 vs as distributed): largest change in any conduit peak 3.12% (USER5).
- Scorecard, 111 locations: peak within 1%: 75; within 2%: 88; within 5%: 100; within 10%: 105; over 10%: 6. Median absolute peak difference 0.51%. NSE at or above 0.99: 57; 0.95: 101; 0.90: 102. Median NRMSE 3.12% of range.
- Routing continuity, 5.2.4, Table 3.1 options: all within 0.72% except EXTRAN2 (-4.085%) and USER5 (-2.352%).
- Large step continuity (2006 SWMM 4 / 2006 SWMM 5 / 5.2.4): TEST3 at 30 s 34.4% / 0.02% / -0.174%; TEST5 at 10 s over 800% / 0.05% / 0.003%; USER5 at 5 s 619% / 1.29% / -2.226%.

Largest peak differences (2006 SWMM 5 vs 5.2.4): EXTRAN10 link 90002 40.26 vs 56.69 cfs (+40.8%); TEST4 outfall at 10 s 129.3 vs 100.2 cfs (-22.5%; inflow is 100 cfs; SWMM 4 gave 258.5); EXTRAN4 node 82309 14.21 vs 12.03 ft (-15.4%); USER5 node 5SB6 6.09 vs 5.27 ft (-13.4%); EXTRAN10 link 90004 25.64 vs 22.66 cfs (-11.6%); TEST5 node 9 4.58 vs 4.11 ft (-10.2%).

Human review: none yet of individual digitized charts or element matches.

## What this does not show

1. It does not show that SWMM 5.2.4 is correct. Agreement is between two versions of one program.
2. About 15 comparison charts in the report are not digitized: p. 26 (1), 54 (1), 58 (1), 59 (2), 61 (1), 75 (3), 76 (4), 82 (1), 109 (1). Appendix A figures (p. 114) are not digitized.
3. 11 digitized locations have no 5.2.4 curve: USER4 P1, P3, P4 (6 charts; map labels, nearest conduit ambiguous), USER3 Fig. 6.22 (edited model not distributed), USER5 Detail A (4 charts; titles name no element).
4. SWMM 4.4h and SWMM 5.0.006 were not run.
5. No InfoWorks ICM, SWMM 6 or other engine results are included.
6. Digitized values carry about 1% of axis span in error. 19 charts are flagged where the 2006 SWMM 4 and SWMM 5 peaks differ by more than 15% in the report itself.
7. Runoff is compared only through continuity totals.

Defect and errata register:
- E1 (report): Figures 4.18 and 4.19 (EXTRAN3, p. 25) carry each other's captions. The plot captioned peak flows holds 10 node elevations (92.3 to 132.6); the plot captioned maximum water elevations holds 7 conduit flows (46.5 to 134.9).
- B1 (engine, build only): `swmm5.c:1593` calls `realpath(fname, absPath)` with a 260 byte buffer (`InpDir[MAXFNAME+1]`, `MAXFNAME 259`); glibc fortified builds abort with "buffer overflow detected". Worked around with `-D_FORTIFY_SOURCE=0`. No effect on results.
- O1 (observation): EXTRAN4 node 82309 max depth is 12.03 ft with the weir's surcharge flag YES (default) and 20.28 ft with NO; weir peak flow 28.11 vs 12.47 cfs. The 2006 figure shows 14.21 ft.
- A1 (this app, fixed in 2.0.0): version 1 drew synthetic curves from `generateFlowData` (rise as t^1.8 to a peak at 35% of the run, exponential decay, seeded noise) and mislabelled EXTRAN4, 5 and 6. All generators and the unsourced ICM comparison were removed.

## How to reproduce

1. Clone `USEPA/Stormwater-Management-Model` at tag v5.2.4 and build with the command above.
2. Clone `OpenWaterAnalytics/swmm-nrtestsuite` at e609fdbb; take the 20 models named in the report (extran1 to 10, test1 to 5, user1 to 5).
3. Write the Table 3.1 option lines into copies of each .inp; run both sets and the 6 variants.
4. Read link flow, node depth and node total inflow from each .out at the elements named in the chart titles.
5. Digitize the report figures from the PDF vector content with tick-label calibration.
6. Subsample each 5.2.4 series at the model's original REPORT_STEP and score against the digitized 2006 SWMM 5 curve.

## Credits and licenses

- Lewis A. Rossman, Storm Water Management Model Quality Assurance Report: Dynamic Wave Flow Routing, EPA/600/R-06/097, U.S. EPA, September 2006. Public domain.
- Extran test cases: Roesner, Aldrich and Dickinson, SWMM Version 4 Extran Addendum, 1992.
- Challenge test cases: "a suite of test cases compiled by Robert E. Dickinson of CDM" (report p. 13).
- User test cases: contributed by SWMM users, not named in the report.
- EPA SWMM 5.2.4: U.S. EPA, public domain.
- Input files: OpenWaterAnalytics swmm-nrtestsuite.
- pdf.js (Mozilla, Apache-2.0), html2canvas (MIT), gif.js (MIT).
- App: Robert Dickinson.

## AI use

This app was built with Claude, Anthropic's AI model, in November 2026, under the direction of Robert (Bob) Dickinson. He chose the report, asked where the first version's chart values came from when they did not match the paper, and asked for the app to be updated and improved. Responsibility for the work is his.

What Claude did: it wrote the first version, including the synthetic chart generators that Bob caught. It then read the curves and scatter markers out of the PDF's vector graphics, compiled EPA SWMM 5.2.4 from source, prepared and ran the 46 simulations, wrote the binary results reader, matched chart titles to model elements, computed the scores, wrote the app, the essay in the Doc tab, the .docx and this file.

How the results were checked: mechanically, as listed under Checks. What no person has checked: the 122 digitized charts have not been compared to the printed figures one by one, the 111 element matches have not been reviewed by hand, and the essay has not been edited by a person.

## Changes

- 2.0.0 (2026-11-12): rebuilt as a single HTML file; SWMM 5.2.4 runs of all 20 models; scorecard of 111 locations; 19 scatter figures digitized; all generated data and the ICM overlay removed; case descriptions corrected; Verify, Doc, .md and .docx added.
- 1.2 (2026-11): charts replaced by curves digitized from the report; PDF embedded.
- 1.1: dark mode.
- 1.0: React app with synthetic charts.

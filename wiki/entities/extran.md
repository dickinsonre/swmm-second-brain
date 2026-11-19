---
title: EXTRAN
type: entity
updated: 2026-11-19
sources: [S05, S07, S08, S19, S20, S21, S22, S55, S60, S74, S75, S76, S81, S180, S181, S182, S183, S185, S379]
tags: [swmm-history, hydraulics, engine]
reviewed: 2026-11-15
changed_after_review: "2026-11-16 (S180 to S187 ingest): one paragraph added at the end on the test models, S185 and the Addendum date (Q94); 2026-11-19 (S377 to S382 ingest): a paragraph added at the end, headed Added 19 November 2026 (S379)"
---
The Extended Transport block: SWMM's dynamic-wave hydraulics before SWMM 5, and the ancestor of SWMM 5's [dynamic wave routing](../concepts/dynamic-wave-routing.md) [S20](../sources/S20-li-edition-54-two-solvers.md).

- **Authors on the 1988 addendum.** Roesner, L.A., Aldrich, J.A. and Dickinson, R.E., "Storm Water Management Model User's Manual Version 4: Extran Addendum", EPA/600/3-88/001b, August 1988 [S19](../sources/S19-li-edition-29-engine-speed.md).
- **The 1981 manual.** CDM published the Extran manual in 1981 with 7 test files that Bob still uses [S55](../sources/S55-swmm-brain-readme.md).
- **When it arrived.** Dynamic wave modeling was first introduced in SWMM 3, in 1981, as the separate module EXTRAN (Extended Transport); the node-link method came from the Sacramento-San Joaquin Delta Model of 1965 and the WRE Transport Model of 1975 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- **How it integrated in time.** Explicitly, by the two-step Modified Euler method; SWMM 5 replaced that with an implicit backward Euler step [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- **Method.** A node-link formulation [S20](../sources/S20-li-edition-54-two-solvers.md).
- **What SWMM 5 kept.** Conduit lengthening, minimum surface area, inertial damping, the surcharge iteration [S22](../sources/S22-li-ten-problems.md), and the EXTRAN surcharge method [S20](../sources/S20-li-edition-54-two-solvers.md).
- **The test models.** The EXTRAN 3 test model of 1981 is Extran1.INP in the OWA-Extran set and has run in SWMM 3, 4 and 5 [S19](../sources/S19-li-edition-29-engine-speed.md). Bob's swmm5.org pages carry Extran1 and Extran2, a SWMM3 orifice test and a SWMM3 weir test as modern files [S07](../sources/S07-swmm5org-topic-swmm-history.md).
- **Rebuilt.** EXTRAN III was rebuilt from the 1981 printed listing and runs in the browser ("EXTRAN III, Alive Again", October 2026) [S07](../sources/S07-swmm5org-topic-swmm-history.md). Per Bob's notes, 139 doubtful listing lines are not yet confirmed against page images [S05](../sources/S05-swmm5org-article-facts.md).

**Disagreements**
- Q14, settled by the EPA reference manual: EXTRAN arrived with SWMM 3 in 1981 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md), as [S55](../sources/S55-swmm-brain-readme.md) also has it. [S21](../sources/S21-li-edition-56-swmm-history.md), which gives SWMM 2 (1975), is the one in error. The October 1971 listing has no such block; see [SWMM 1 (1971)](swmm-1.md).
- Q12, settled: EXTRAN was explicit and SWMM 5's descendant of it is implicit in time but uncoupled in space [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). See [Dynamic wave routing](../concepts/dynamic-wave-routing.md).

**Still not in the sources.** The EXTRAN manual's own derivation of the equations. Queued: six articles on the EXTRAN manual's test files (2024 to 2025) and Edition 38, "Seven Classic SWMM5 Hydraulics Test Files".

**The 1981 program, from its listing.** EXTRAN III is the Extended Transport block of SWMM Version III, by Larry A. Roesner, Robert P. Shubinski and John A. Aldrich of Camp Dresser & McKee, user's manual of April 1981; the listing is dated 20-MAY-81 and has 15 program units [S74](../sources/S74-extran3-workbench-app-md.md). Its solver, TRANSX, is an explicit link-node solution by modified Euler, a half step then a full step, and treats a junction above 0.96 of the depth to its highest crown as surcharged. It holds 187 junctions and 187 links [S74](../sources/S74-extran3-workbench-app-md.md). Ten faults in the listing as printed are fixed in a second build of the [EXTRAN III Workbench (app)](extran-iii-workbench.md), which reproduces 2,253 of 2,424 printed 1981 values exactly [S74](../sources/S74-extran3-workbench-app-md.md).

**In SWMM 4.** By SWMM 4.4H the Extran block carried three solvers, XROUTE, YROUTE and ZROUTE. SWMM 5 kept XROUTE's momentum terms and its surcharge rule [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). See [EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE](../concepts/extran-solvers-xroute-yroute-zroute.md) and [The crown cap at mid-pipe](../concepts/crown-cap-at-mid-pipe.md).

**The manual examples in use.** Bob's apps run them constantly: Example 1 in six solvers [S75](../sources/S75-st-venant-rosetta-stone-app-md.md), Examples 1, 2, 7 and 80 beside a CFD solver [S76](../sources/S76-inside-the-network-cfd-app-md.md), and the 1981 engine on a Danish sewer in the [Bellinge (app)](bellinge-app.md) [S81](../sources/S81-bellinge-summary.md).

**Added 16 November 2026, from the EXTRAN and QA ingest.** The manual's ten examples, what each adds to Example 1, and what the runs have shown are on [The EXTRAN manual test models](../concepts/extran-manual-test-models.md). EPA's 2006 quality assurance report ran all ten on SWMM 4.4h and SWMM 5.0.006 [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md); Bob's four articles of April 2025 describe Examples 1, 2, 5, 6 and 7 and say they are used in ICM SWMM daily build validation [S180](../sources/S180-li-extran1-extran2-test-files.md). The report cites the Extran Addendum as EPA/600/3-88/001b, October 1992 [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md); Edition 29 gives the same number with August 1988 [S19](../sources/S19-li-edition-29-engine-speed.md) (Q94).

**Added 19 November 2026.** The [SWMM5 to SWMM6 EXTRAN Features Upgrader](swmm5-to-swmm6-extran-upgrader.md) switches on, in a SWMM5 input file, the four features OpenSWMM 6 inherited from the EXTRAN line: SURCHARGE_METHOD DYNAMIC_SLOT, NODE_CONTINUITY SEMI_IMPLICIT, ANDERSON_ACCEL and [VIRTUAL_JUNCTIONS]. On alpha.3, all four together lifted its demo chain's peak from 14.38 to 19.29 cfs (+34.1 %) [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md). Its embedded fleet is exam1, extran1 to extran7, extran9, extran10, user1, user2_slot, user3, user4 and user5_slot [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md).

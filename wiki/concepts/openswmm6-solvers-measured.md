---
title: OpenSWMM 6 solvers, measured
type: concept
updated: 2026-11-19
sources: [S75, S80, S81, S186, S196, S198, S199, S209, S29, S280, S281, S282, S286, S300, S301, S307, S378, S379, S389]
tags: [swmm6, hydraulics, dynamic-wave, finite-volume, engine-comparison]
reviewed: 2026-11-15
changed_after_review: "2026-11-16 (S180 to S187 ingest): one paragraph added at the end on Register 33 (S186); 2026-11-17 (S192 to S202 ingest): one paragraph added at the end on three more apps (S196, S198, S199); 2026-11-17 (S205 to S223 ingest): a paragraph added near the end, headed Added 17 November 2026 (S209, S29); 2026-11-18 (S268 to S299 ingest): a paragraph added near the end, headed Added 18 November 2026 (S280, S281, S282, S286); 2026-11-18 (S300 to S375 ingest): a paragraph added near the end, headed Added 18 November 2026 (S300, S301, S307); 2026-11-19 (S377 to S382 ingest): a paragraph added at the end, headed Added 19 November 2026 (S378, S379); 2026-11-19 (S384 to S391 ingest): a paragraph added at the end, headed Added 19 November 2026 (S389)"
---
OpenSWMM 6 has two hydraulic solvers: a dynamic wave solver that extends SWMM 5's, and an explicit finite-volume solver (FV) [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). Three of Bob's apps have run them beside EPA SWMM 5.2.4. This page collects what they measured. Every run is on an alpha build, and none is compared with a measurement. For the program see [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).

**With SWMM 5's options, the dynamic wave is SWMM 5.**
- On EXTRAN Example 1 with SURCHARGE_METHOD EXTRAN, flooding, peak, time of peak, maximum head and continuity are identical to EPA 5.2.4 at six time steps, 30 of 30 values [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).
- On the [Control Section Lab (app)](../entities/control-section-lab.md) channel, node depths are identical on three cases: the null control, the defaults and the split-in-4 case [S80](../sources/S80-control-section-lab-summary.md).

**Its own options change the answer.** EXTRAN Example 1, 20-second step [S75](../sources/S75-st-venant-rosetta-stone-app-md.md):

| Options | Lost to flooding, ft³ |
|---|---|
| EXTRAN (SWMM 5 parity) | 114,824 |
| SLOT | 89,559 |
| DYNAMIC_SLOT | 91,781 |
| DYNAMIC_SLOT + SEMI_IMPLICIT + ANDERSON_ACCEL | 90,866 |
| TPA | 44,083 |
| EXTRAN + SEMI_IMPLICIT | 6,534 |

- SLOT gives 89,559 where EPA 5.2.4's SLOT gives 78,582. The difference is by design: in OpenSWMM the slot area does not convey flow.
- The 6,534 is measured; its cause was read from the code and not isolated. The TPA result is not explained.

**The finite-volume solver depends on its mesh.** By default it uses four cells per conduit. On Example 1 [S75](../sources/S75-st-venant-rosetta-stone-app-md.md):

| FV_CELL_LENGTH | Lost to flooding, ft³ | Run time, s |
|---|---|---|
| not set (4 cells) | 0 | 0.10 |
| 200 ft | 58,980 | 0.38 |
| 50 ft | 78,147 | 2.71 |
| 25 ft | 80,673 | 8.63 |

Flooding was still rising at 25 ft. Its continuity error prints 0.000 % at every mesh. On a single pipe with n 0.034 at 20 cfs, four cells give a depth of 1.626 ft where Manning's normal depth is 2.385 ft; forty cells give 2.299 ft [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**Where the finite volume does better.** On the Control Section Lab channel it is the only engine in that app that finds the choke at a throat (5.47 ft upstream against a reference of 5.47, where SWMM 5 has 4.1179) and holds a chute crest near critical depth (2.59 ft against 2.32). The essay's caution: "that is one channel and one pre-release commit" [S80](../sources/S80-control-section-lab-summary.md).

**On a real network.** The Bellinge model, 1,020 nodes, a 48-hour base run [S81](../sources/S81-bellinge-summary.md):

| Engine and mode | Routing continuity | Flooding nodes | Wall time |
|---|---|---|---|
| EPA SWMM 5.2.4, as written | 0.35 % | 466 | 2.5 min |
| OpenSWMM alpha.1, SWMM 6 dynamic wave | -0.38 % | 643 | 25.8 min |
| OpenSWMM alpha.2, SWMM 6 dynamic wave | 2.79 % | 62 | 12.8 min |
| OpenSWMM alpha.3, SWMM 6 dynamic wave | 1.64 % | 62 | 11.6 min |
| OpenSWMM swmm6_rel, SWMM 6 dynamic wave | 0.09 % | 61 | 14.4 min |
| OpenSWMM swmm6_rel, finite volume | -0.79 % | 520 | 99 min |

- alpha.1 also shows a runoff continuity error of -43.9 %, which the later tags do not.
- From alpha.2 to swmm6_rel the routing continuity tightens with each tag.
- The later dynamic wave runs agree with each other at about sixty flooding nodes and differ from EPA 5.2.4's 466. The [Bellinge (app)](../entities/bellinge-app.md) essay: "The app does not tell you which to believe."

**Commits differ between the apps.** swmm6_rel at 64d517f (16 October 2026) in [S80](../sources/S80-control-section-lab-summary.md), 3c30f1e6c2 (17 October) in [S81](../sources/S81-bellinge-summary.md), 0071c5f in [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). Results from one may not hold on another.

**Not run anywhere here.** Virtual junctions, unsteady friction, FV_ORDER 2, and the implicit pressurized option [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

See [EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE](extran-solvers-xroute-yroute-zroute.md), [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md), [Continuity is not validation](continuity-is-not-validation.md).

**Added 16 November 2026, from the EXTRAN and QA ingest.** Register 33 [S186](../sources/S186-st-venant-rosetta-stone-app-md-v2-6-2.md): the finite volume solver pumps 39.00 cfs on Example 7 through a pump curve that ends at 20 cfs, and 28.87 cfs on a one-junction test deck where the curve gives 5.00. The dynamic wave solver with DYNAMIC_SLOT alone pumps 30.00 cfs on the same deck, with 11.84 percent continuity error. The cause is the dry-node limiter at HydStructures.cpp:539, `q = std::max(nodes.inflow[un1], 0.0);`, which can raise the curve flow; a build copy with `q = std::min(q, std::max(nodes.inflow[un1], 0.0));` pumps 5.00 on the test deck and 10.00 on Example 7. Not reported to the OpenSWMM authors.

**Added 17 November 2026: three more apps.**
- [Seven SWMM Engines](../entities/seven-swmm-engines.md), on EPA's Example 1: outfall peaks of 75.94 cfs (alpha.1 SWMM6 DW), 73.76 (alpha.4 SWMM6 DW) and 71.69 (alpha.4 FV) against EPA 5.2.4's 73.9. Flow continuity within 0.03 percent everywhere, but TSS continuity -58.54 %, -53.43 % and -53.20 % in the SWMM6 DW runs of alpha.1 to alpha.3, -1.65 % in alpha.4, -85.40 % in alpha.3 FV and -3.70 % in alpha.4 FV, against EPA's -1.96 % [S199](../sources/S199-seven-swmm-engines-summary.md).
- [SWMM5 RASPIPE](../entities/swmm5-raspipe.md), on 87 corpus models every engine finished: SWMM6's modified DW (slot, semi-implicit and Anderson acceleration together) had a median continuity error of 0.701 % against EPA's 0.941 %. One option at a time over the sample: EXTRAN alone 0.763 %, DYNAMIC_SLOT 0.734 %, ANDERSON_ACCEL 0.696 %, the two together 0.619 %, SEMI_IMPLICIT 0.909 %, all three 0.516 %. On one deck the modified DW sent none of the 0.26 ac-ft out the outfall, where EPA and SWMM6's EXTRAN sent 0.24 [S196](../sources/S196-swmm5-raspipe-summary.md).
- [Two Engines, One Town](../entities/two-engines-one-town.md) tried openswmm 6.0.0a3 as a drop-in engine on one model and reports "three SWMM engines produce identical numbers"; none of SWMM6's new features was exercised [S198](../sources/S198-two-engines-one-town-summary.md).

**Added 17 November 2026.** On an exact pressurised transient, the stock dynamic slot runs a factor of the square root of 2 (1.414) fast, and the two virtual-junction runs fail on initial conditions rather than on the slot [S209](../sources/S209-rigid-column-test-summary.md). The summary does not name the engine of the dynamic slot; DYNAMIC_SLOT is an OpenSWMM 6 method [S29](../sources/S29-swmm6-rust-readme.md). One pipe geometry, builds of 30 September 2026; a summary Claude wrote from the page (Q108).

**Added 18 November 2026.** Five more summaries measure OpenSWMM 6 alpha 4.
- On a three-conduit model with SWMM 5's options it matches EPA 5.2.4 bit for bit in node depths and link flows at all 360 reporting periods, but its surcharge tables say no node surcharged where EPA gives J1 1.08 h; one added line moves the J1 peak: EXTRAN 5.36 ft, SLOT 5.31, DYNAMIC_SLOT 5.40, NODE_CONTINUITY SEMI_IMPLICIT 4.91 [S280](../sources/S280-run-swmm6-ten-minutes-summary.md).
- On a ponded eight-pipe chain, DYNAMIC_SLOT took steps not converging from 2.99% to 0.00% and continuity from 0.091% to 0.008% but cut the average step from 6.51 s to 1.28 s; SEMI_IMPLICIT made continuity worse on both ponded chains (-0.316% to -2.998% on chain B); Anderson acceleration left 2.51 trials per step unchanged; FV held continuity at 0.000% and ran about 7 times slower, and with ponding reported -158% and -133% [S281](../sources/S281-swmm6-in-diagrams-summary.md).
- On an unponded four-pipe chain the two engines agree with SWMM 5 options (C1 peak 16.0 cfs in both, continuity -0.092% in both), but on ponded chain A EPA 5.2.4 peaked at 14.45 cfs and SWMM6's SWMM5 path at 11.67 cfs [S281](../sources/S281-swmm6-in-diagrams-summary.md). The page does not say why (Q115).
- On a still pool, DYNAMIC_SLOT books slot water as storage (+25.5% in one pipe) and FV moves water where none should move (link flows to 74 cfs) [S282](../sources/S282-forma-swmm6-summary.md).
- FV reported 103.4 ft at a 12.75 ft junction on one generated network of 24, with continuity 0.0% (DR-2, undiagnosed) [S286](../sources/S286-exam-first-swmm-harness-summary.md).

**Added 18 November 2026.** Three more pages measure OpenSWMM 6:
- The 2D Flood Lab's double-precision port matches the compiled alpha.4 surface solver to rounding on four cases and on Merewether at 13 ft squares (3.4e-12 ft); with the default LTS_TIERS 4 the Merewether flood reaches point S1 between 400 and 500 s instead of 200 and 300 s and stores 15% more water at 1,000 s, every run closing its volume balance [S300](../sources/S300-swmm6-2d-flood-lab-summary.md).
- On a 13-conduit demo, OpenSWMM 6 alpha.2 stays within 0.30% of EPA 5.2.4 at every reporting period while its continuity line reads -29.401%, because its report counts almost none of the water already in the system as initial storage [S301](../sources/S301-st-venant-term-budget-summary.md).
- On EPA Example 1, alpha.4 dynamic wave gives 73.76 cfs in C11 against 73.90, and alpha.4 finite volume puts the deepest water at J1 at 0.24 ft against 0.72 ft [S307](../sources/S307-swmm-front-door-summary.md).

**Added 19 November 2026.** Two more apps add to this page, one with runs and one with quotations. The [SWMM5 to SWMM6 EXTRAN Features Upgrader](../entities/swmm5-to-swmm6-extran-upgrader.md) ran OpenSWMM 6.0.0-alpha.3 (pre-tag commit 1610516) on a demo chain: base 14.38 cfs, DYNAMIC_SLOT 16.32, SEMI_IMPLICIT 13.82, ANDERSON_ACCEL 14.38 (bit-identical to base), virtual junctions 14.39, all four 19.29 (+34.1 %) [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md). Making every engine-eligible junction virtual took user4's continuity from 0.054 to -24.946 % [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md). Upstream withdrew VIRTUAL_JUNCTION_MOMENTUM FULL on 2026-08-14, after a sign-inverted cross-junction term destroyed 224-325 % of routed volume on one SWASHES case; engines now warn and run BASIC [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md). The [Four-Engine Pipe Comparator](../entities/four-engine-pipe-comparator.md) quotes, without measuring, two sets of upstream figures for the finite-volume solver: an August set it marks superseded (peak deviation 37.1 / 15.3 / 7.2 percent, wall clock about 7x to 34x dynamic wave) and a November set (about 3 percent at every resolution, wall clock at parity with dynamic wave or better) [S378](../sources/S378-four-engine-pipe-comparator-app-md.md). It warns that SWMM6 reports conduit flow as the mean face mass flux over the reporting step: upstream found a force main delivering 25 cfs whose cell momentum state held 18.4 [S378](../sources/S378-four-engine-pipe-comparator-app-md.md).

**Added 19 November 2026.** Bellinge 2.4 gives its whole 48-hour run in full [S389](../sources/S389-bellinge-app-md-v2-4.md). With SWMM 6 dynamic wave, alpha.1 floods 643 nodes (it loses 43.9 per cent of the runoff, a defect of that tag) against 62, 62 and 61 for alpha.2, alpha.3 and swmm6_rel; EPA 5.2.4 floods 466 and the finite-volume solver 520. Routing continuity is 0.35 per cent for 5.2.4, -0.38 for alpha.1 and -0.79 for finite volume. Wall time is 25.8, 12.8, 11.6 and 14.4 min for the four dynamic wave runs, against 2.5 for 5.2.4 and 99 for finite volume [S389](../sources/S389-bellinge-app-md-v2-4.md).

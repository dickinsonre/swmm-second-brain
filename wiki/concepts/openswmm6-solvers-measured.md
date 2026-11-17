---
title: OpenSWMM 6 solvers, measured
type: concept
updated: 2026-11-16
sources: [S75, S80, S81, S186]
tags: [swmm6, hydraulics, dynamic-wave, finite-volume, engine-comparison]
reviewed: 2026-11-15
changed_after_review: "2026-11-16 (S180 to S187 ingest): one paragraph added at the end on Register 33 (S186)"
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

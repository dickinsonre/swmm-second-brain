---
title: "SWMM5 to SWMM6 EXTRAN Features Upgrader (app)"
type: entity
updated: 2026-11-19
sources: [S379]
tags: [apps, swmm6, swmm5, extran, virtual-junctions]
reviewed: no
---
Bob's app SWMM5 → SWMM6 EXTRAN Features Upgrader switches on, in a SWMM5 .inp, the four features OpenSWMM 6 inherited from the [EXTRAN](extran.md) line: the dynamic Preissmann slot, semi-implicit node continuity, Anderson acceleration and virtual junctions. It downloads a SWMM6 file, or a SWMM5 file free of SWMM6-only keywords, each of which is a fatal ERROR 205 in stock 5.2.4. Version 2.0.0, 2026-11-18; first delivered 2026-08-08 [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md). It carries 15 models, a four-engine compatibility matrix with verbatim messages and a release ladder measured with git [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md).

**What it measured** [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md)
- 16 of 16 all-features-then-stripped files run in stock EPA 5.2.4 with continuity matching the baseline to a few hundredths.
- App-eligible virtual junctions equal engine-eligible on all 15 models, under the engine's four rules (ERRORs 609, 611, 613, 617).
- On the demo chain, all four features together lifted the peak from 14.38 to 19.29 cfs (+34.1 %); Anderson alone left it bit-identical.
- Converting every engine-approved virtual junction took user4's continuity from 0.054 to -24.946 %.

**Its engine pin** [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md). OpenSWMM 6.0.0-alpha.3 pre-tag at commit 1610516, which the 2026-08-11 history rewrite left an ancestor of no ref; 142 commits were orphaned. The alpha.3 tag is 86c28a88.

**What it does not show** [S379](../sources/S379-swmm5-to-swmm6-extran-upgrader-app-md.md). Anderson acceleration's 25-50 % iteration cut is unmeasured. The app measures difference and compatibility, not correctness. No runs after 2026-08-09, including FLOW_ROUTING FV.

See [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md).

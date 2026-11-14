---
title: EPA SWMM 5
type: entity
updated: 2026-11-14
sources: [S02, S04, S08, S11, S15, S17, S19, S20, S21, S22, S59]
tags: [swmm5, engine]
reviewed: no
---
The C rewrite of SWMM, first released as 5.0 build 001 on 29 October 2004 [S22](../sources/S22-li-ten-problems.md). Written and carried for about twenty years by Lewis A. Rossman of EPA [S22](../sources/S22-li-ten-problems.md), [S21](../sources/S21-li-edition-56-swmm-history.md). See [Lewis A. (Lew) Rossman](lew-rossman.md).

**How it came about.** EPA and CDM signed a Cooperative Research and Development Agreement in 2001 [S21](../sources/S21-li-edition-56-swmm-history.md). Bob joined CDM in late 2000 and worked on the upgrade with Lew Rossman and Trent Schade at EPA and CDM's Jim Smullen, Ted Burgess, Carl Chan, Charles Rowney and Khalid Khan [S11](../sources/S11-li-my-history-with-swmm.md). The team's paper is Rossman, Dickinson, Schade, Chan, Burgess, Lai and Sullivan, WEFTEC 2003 [S19](../sources/S19-li-edition-29-engine-speed.md).

**Releases.** 42 builds from 5.0.001 to 5.2.4 [S22](../sources/S22-li-ten-problems.md). Dated ones are in [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md). The current stable release is 5.2.4 [S21](../sources/S21-li-edition-56-swmm-history.md).

**Status.** Public domain, open source [S11](../sources/S11-li-my-history-with-swmm.md), [S20](../sources/S20-li-edition-54-two-solvers.md). The EPA repository's default branch shows 0 commits in the 12 months to 1 November 2026 [S02](../sources/S02-complexity-meter-app-md.md).

**What the wiki holds on its insides**
- Routing: [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Conduit lengthening](../concepts/conduit-lengthening.md), [Force main friction](../concepts/force-main-friction.md).
- Hydrology: [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [Subcatchment width](../concepts/subcatchment-width.md), [Infiltration methods](../concepts/infiltration-methods.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md). Function names are from [S15](../sources/S15-li-hydrology-code-story.md).
- Output: [Reading SWMM output](../concepts/reading-swmm-output.md).
- Documentation: [The missing specification](../concepts/the-missing-specification.md).

**Bob's variants.** A fork with branches for a staggered grid, a Preissmann box, node surface area and six Curve Number changes; swmm5-kw; [swmm524-perched](swmm524-perched.md); and versions in C++, Rust, Fortran, C#, Python, TypeScript, Java and Go [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

**Inside other products.** InfoSWMM uses the SWMM 5 C code as its engine [S11](../sources/S11-li-my-history-with-swmm.md). ICM SWMM runs the SWMM5 dynamic wave [S17](../sources/S17-li-routing-options.md).

**Defects in 5.2.4 found by one study.** D1, Modified Horton with MaxInfil (`infil.c` line 545; see [Infiltration methods](../concepts/infiltration-methods.md)), and D2, a drain on a bio-retention cell with no storage layer (see [LID bio-retention layers](../concepts/lid-bioretention-layers.md)) [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**Back-compatibility hazard.** SWMM 5.2.4 stops with ERROR 205 on SWMM6 `[OPTIONS]` keywords; legacy 5.3 silently ignores them (F-0005, partly unconfirmed) [S04](../sources/S04-findings-register-seed.md).

**Complexity index.** 69.2 with HydroCouple = 100 [S02](../sources/S02-complexity-meter-app-md.md).

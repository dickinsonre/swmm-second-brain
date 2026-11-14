---
title: Runoff surfaces and subarea routing
type: concept
updated: 2026-11-14
sources: [S01, S13, S14, S15, S22]
tags: [hydrology, swmm5, icm]
reviewed: no
---
A SWMM5 subcatchment is three subareas: impervious with depression storage, impervious without depression storage, and pervious with depression storage [S13](../sources/S13-li-three-runoff-surfaces.md). Two inputs set them: percent impervious, and the percent of the impervious area with no depression storage [S13](../sources/S13-li-three-runoff-surfaces.md).

**The idea is from 1971.** The Runoff Block of [SWMM 1 (1971)](../entities/swmm-1.md) already modeled each subarea as a nonlinear reservoir on three planes with Horton infiltration [S01](../sources/S01-swmm1-engine-app-md.md).

**Routing between subareas** [S14](../sources/S14-li-subarea-routing.md)

| SWMM5 option | What it does |
|---|---|
| OUTLET | Both subareas drain straight to the outlet |
| IMPERV | Pervious runoff drains to the impervious area |
| PERV | Impervious runoff drains to the pervious area |

Percent Routed sets the rerouted share: at 20 %, 20 % goes to the other subarea and 80 % to the outlet [S14](../sources/S14-li-subarea-routing.md).

**In the code.** The subarea methods are `getSubareaRunoff`, `getSubareaInfil`, `findSubareaRunoff`, `updatePondedDepth` and `adjustSubareaParams`, and the runoff equation is integrated by `odesolve_integrate` with adaptive Runge-Kutta steps [S15](../sources/S15-li-hydrology-code-story.md). (Function names from an AI-written passage, not checked against the code.)

**In InfoWorks ICM.** The same subcatchment becomes three runoff surfaces tied together by a Land Use ID. Example: 23 % impervious with 25 % of that having no depression storage becomes surfaces of 17.250 %, 5.750 % and 77.00 % [S13](../sources/S13-li-three-runoff-surfaces.md). ICM's routing choices are Direct, To pervious and To impervious, added in version 6.5 of November 2015 [S14](../sources/S14-li-subarea-routing.md).

**One width for all three.** The three subareas share a single width, which Bob has long objected to [S22](../sources/S22-li-ten-problems.md). See [Subcatchment width](subcatchment-width.md).

**Disagreements**
- The caption of section 5 in [S14](../sources/S14-li-subarea-routing.md) pairs SWMM's IMPERV with InfoWorks "Impervious to Pervious". Open question Q07 in [Open questions](../open-questions.md).

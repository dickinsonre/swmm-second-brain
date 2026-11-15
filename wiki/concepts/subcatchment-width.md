---
title: Subcatchment width
type: concept
updated: 2026-11-14
sources: [S10, S22, S63]
tags: [hydrology, swmm5, calibration]
reviewed: 2026-11-15
---
Subcatchment width is a fitting parameter that the documentation presents as a length you can measure [S22](../sources/S22-li-ten-problems.md).

- One width W is shared by the pervious and impervious subareas, two very different surfaces. This is Bob's long-standing objection [S22](../sources/S22-li-ten-problems.md).
- Overland Manning's n and depression storage are "close behind" as calibration knobs explained as physics [S22](../sources/S22-li-ten-problems.md).
- The cost to users: careful people measured the values, got bad hydrographs and blamed themselves [S22](../sources/S22-li-ten-problems.md).
- Where it came from, in Bob's words: "This goes back to the SWMM1 and the street models used in SWMM1 - the width makes sense if you are only modeling one street." [S22](../sources/S22-li-ten-problems.md)

**An old teaching aid.** [William (Bill) James](../entities/william-james.md) and Mark Robinson had an expert system that quizzed the user on the width parameter of SWMM 3 [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md).

**How often it is asked.** "Subcatchment parameters as fitting knobs" tags 128 of Bob's 2,879 OpenSWMM thread titles [S10](../sources/S10-openswmm-top25-problems.md).

See also [Runoff surfaces and subarea routing](runoff-surfaces-and-subarea-routing.md) and [The missing specification](the-missing-specification.md).

**Not in the sources yet.** The equation in which width appears, a worked sensitivity, and Bob's proposed alternative.

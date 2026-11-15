---
title: Weirs and outlets
type: concept
updated: 2026-11-15
sources: [S60]
tags: [hydraulics, swmm5, regulators, primary-document]
reviewed: no
---
Weirs and outlets are, with [orifices](orifices.md), SWMM 5's flow regulator links [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). This page is sections 6.3 and 6.4 of the EPA hydraulics manual, a primary document, in digest. The equations did not survive the conversion of the raw file, so they are given in words [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Weir kinds.** A transverse weir is a barrier with a cut-out across the conduit; its opening is rectangular, triangular or trapezoidal. A side weir is a cut-out along the side wall, and only a rectangle is allowed [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Orifices normally run with the inlet submerged; weirs normally keep a free surface [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Setting.** The fraction of the full opening height left after the crest is moved, as with a weir gate or an inflatable dam. At 1 the crest is at its lowest. At 0 nothing passes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Free flow.** Flow goes with the head over the crest to the power 3/2 for a rectangular weir and 5/2 for a triangular one. A trapezoidal weir is computed as a rectangle plus two half triangles [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). End contractions (0, 1 or 2) shorten the effective crest of a rectangular weir [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Coefficients, in ft^0.5/s**

| Weir | Value in the manual |
|---|---|
| Sharp-crested rectangular | 3.33 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Triangular | 2.5, with measured values from 2.5 to 2.8 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Broad-crested rectangular | Table 6-3: 2.34 to 3.32, by head and breadth of crest [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Side weir, in the original Engels equation | 3.32 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |

A broad crest acts as sharp-crested, 3.32, once the head is more than about twice the crest breadth, and the coefficient approaches 2.63 below a ratio of 0.5 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). For weirs that stand for levees or roadways along natural channels the manual passes on Brunner's (2014) range of 1.5 to 2.6 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Side weirs.** The empirical Engels equation: crest length to the power 0.83 and head to the power 1.67. The manual notes that "previous versions of SWMM used an incorrect form of this equation" with the exponent on the length equal to 1.0 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Reverse flow through a side weir uses the ordinary rectangular formula [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Submerged.** When the downstream water is above the crest, the free flow is multiplied by Villemonte's (1947) factor [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Surcharged.** When the weir sits in a closed structure and the upstream head rises above the top of the opening, it is computed as an orifice, with an equivalent coefficient worked out again each time the setting changes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Under dynamic wave.** A weir adds no surface area to its end nodes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md); compare [orifices](orifices.md). Under [kinematic wave](kinematic-wave-and-steady-flow.md) analysis its inlet must be a storage node [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Outlets.** A generic regulator for cases the orifice and weir formulas do not fit: the user gives a rating curve of flow against head, as a power function or a table [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Head is either the depth at the upstream node or the difference across the link [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Below the first table entry the first flow is used, and above the last entry the last flow [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). A setting between 0 and 1 multiplies the flow [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). The manual's examples are a side orifice by the Smith and Coleman equation, a perforated riser with a grate, and a vortex regulator [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Not in the sources yet.** Section 6.3.6 and steps 3 to 6 of the weir summary are missing from the raw file (Q60 in [Open questions](../open-questions.md)).

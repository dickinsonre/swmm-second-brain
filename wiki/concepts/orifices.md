---
title: Orifices
type: concept
updated: 2026-11-15
sources: [S60]
tags: [hydraulics, swmm5, regulators, primary-document]
reviewed: no
---
An orifice is one of SWMM 5's three flow regulator links, with [weirs and outlets](weirs-and-outlets.md) [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). This page is sections 2.1.7 and 6.2 of the EPA hydraulics manual, a primary document, in digest. The equations did not survive the conversion of the raw file, so they are given in words [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**What it is for.** Releases from detention ponds and other storage, sluice gates in channels, diversions from interceptors to overflows, and storm drain inlets [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Properties.** A link between two nodes. The opening is circular or rectangular, in a vertical plane (a side orifice) or a horizontal plane (a bottom orifice), at some height above the inlet node's invert, with a discharge coefficient and an optional flap gate [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Its setting is the fraction of the full height left open. Control rules change it, and a time to open or close fully can be given [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Where it may sit.** Under [kinematic wave](kinematic-wave-and-steady-flow.md) analysis the inlet node must be a storage node, the only node with a true hydraulic head. Under [dynamic wave](dynamic-wave-routing.md) analysis it can be any node [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Inlet submerged.** Torricelli's equation: flow goes with the opening area and the square root of the effective head [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). For a side orifice the effective head is measured to the middle of the opening unless the downstream water is above that level; then it is the head difference across the orifice [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Discharge coefficient.** 0.6 is the value most often cited and 0.4 is recommended for ragged edges. Experiments reviewed by Brater and others (1996) put it between 0.59 and 0.67 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Inlet not submerged.** The orifice is computed as a weir [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Side orifice: whenever the inlet water level is below the top of the opening [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Bottom orifice: below the head at which the orifice formula and the weir formula give the same flow, with a weir coefficient of 3.33 ft^0.5/s and the perimeter of the opening as the crest length [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- If the downstream water is above the bottom of the opening, the weir flow is reduced by Villemonte's submergence factor [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Reverse flow and flap gates.** If the head is higher at the nominal downstream node, the flow reverses. With a flap gate it is 0 instead [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). A flap gate also adds a small head loss in the forward direction, from an empirical formula published by Armco (1978) after experiments at Iowa State University in the 1930s [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**A surface area for a link with no length.** Under dynamic wave, a node's head is updated from the surface area of the links attached to it. An orifice has no length, so it should add none. But "in older versions of SWMM an orifice was represented as an equivalent pipe that contributed surface area to its end nodes", and "to maintain compatibility with previous versions" SWMM 5 still computes one [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Half goes to each end node that is not a storage unit and whose head is not below the opening [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). The equivalent length in the converted equation is at least 200 ft; check the PDF before quoting it [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Not in the sources yet.** The orifice code (`link.c`), and which older versions used the equivalent pipe. The SWMM 3 manual and the 2006 quality assurance report, both queued in `raw/manuals/`, use the phrase.

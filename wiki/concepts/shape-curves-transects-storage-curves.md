---
title: Shape curves, transects and storage curves
type: concept
updated: 2026-11-16
sources: [S60]
tags: [hydraulics, swmm5, primary-document, geometry]
reviewed: no
---
Three kinds of geometry in SWMM 5 come from the user rather than from the catalog of [built-in conduit shapes](conduit-cross-sections.md). This page is sections 5.2 to 5.4 of the EPA hydraulics manual, a primary document, in digest [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Shape curves (custom closed conduits)** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)
- A Shape Curve gives width against height for a closed cross-section, both scaled by the full height, so one curve serves conduits of any size.
- SWMM builds area, width and hydraulic radius tables of 51 entries by stepping up the curve in depth segments of 0.02 (1/50), each a trapezoid inside the section. The tables are then used like the ellipsoid and arch tables.
- Full area and full hydraulic radius come from the last table entry; maximum width is the largest width entry. Area from section factor uses the Newton-Raphson-Bisection method.

**Transects (irregular natural channels)** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)
- A transect runs from the top of the left bank, looking downstream, across to the top of the right bank, as stations with bed elevations.
- One transect stands for the whole length of a channel, so "longer channels with varying cross section profiles" may need to be broken into more uniform pieces.
- Each side may have an overbank with its own Manning's n. An overbank boundary must fall on a station.
- Full depth is the highest station elevation minus the lowest. If needed, SWMM adds a station at an end so both ends reach the highest elevation.
- Tables of 51 depths are built by walking the transect at each depth. The hydraulic radius comes from summing the conductance of compound segments, which are separated where the roughness changes or where valleys occur in the profile, and applying the main channel's n. The width at zero depth is set equal to the width of the first increment.
- A meander modifier is the length of the meandering main channel over the length of the overbank around it. The user enters the longer main channel length; SWMM computes with the shorter overbank length and raises the main channel's n by the square root of the modifier.

**Storage curves (storage units)** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)
- A [storage unit](swmm5-network-objects.md) needs only surface area and volume against depth, not its shape. The user gives a Storage Curve of surface area against depth, functional or tabular.
- Functional: three user constants (c0, c1 and c2) set area against depth. Volume comes from integrating it. Depth from volume, needed for kinematic wave analysis, is found by Newton-Raphson-Bisection over the full depth with a tolerance of 0.001 ft.
- Tabular: pairs of depth and area joined by straight lines. Volume is the area under the curve by the trapezoidal rule (Atkinson, 1989). Depth from volume adds segment volumes until they pass the target, then solves inside that segment.

**Equations.** The manual gives each procedure in words and equations. The equations did not survive the conversion to markdown, so none is copied here until someone checks it against the PDF; Equation 5-26 is missing altogether (Q92).

---
title: "Conduit cross-sections: the built-in shapes"
type: concept
updated: 2026-11-17
sources: [S60, S262]
tags: [hydraulics, swmm5, primary-document, geometry]
reviewed: no
---
Every routing method in SWMM 5 needs the geometry of a partly full conduit. This page is section 5.1 and section 5.5 of the EPA hydraulics manual, a primary document, in digest [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Shapes the user draws are on [Shape curves, transects and storage curves](shape-curves-transects-storage-curves.md).

**What the solvers ask of a shape.** Area, top width and hydraulic radius as functions of depth; depth as a function of area; the section factor and its derivative as functions of area; and area as a function of section factor. The section factor is the area times the hydraulic radius to the 2/3 power. Each shape also carries its full area, maximum width, full hydraulic radius, full and maximum section factor, and the area where the section factor peaks [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**The catalog** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)

| Group | Shapes | How SWMM 5 computes them |
|---|---|---|
| Open | rectangular, trapezoidal, triangular, parabolic, power law | Formulas (Tables 5-1 to 5-3). The parabolic shape is the power law with exponent 2. The power law's wetted perimeter is summed over 50 line segments per side |
| Closed pipe | circular, rectangular, ellipsoid, arch | Circular: tables of 51 entries based on Chow (1959), with analytical functions below 4% of full area. Ellipsoid and arch: tables of 26 entries |
| Masonry | basket handle, egg, horseshoe, catenary, gothic, semi-circular, semi-elliptical | Tables from Metcalf and Eddy (1914) and Davis (1952) |
| Composite | sediment-filled circular, rectangular-triangular, rectangular-round, modified basket handle | Built from the circular, triangular and rectangular functions (Tables 5-8 to 5-12) |

- Tables replace formulas for the circle because the formulas need trigonometric functions "that are time consuming to compute". Values between entries are interpolated linearly [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Ellipsoid and arch pipes come in 23 and 102 standard sizes from the American Concrete Pipe Association and the American Iron and Steel Institute manuals, or in the user's own rise and span in feet [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- The masonry shapes are those "used primarily in older masonry sewers built over a century ago" [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- The sediment in the sediment-filled circle stays at its depth: "SWMM does not model how it might change over time" [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Why Manning flow peaks before a closed conduit is full.** In a closed shape the section factor, and with it the Manning equation flow, rises with area, peaks, and falls until the conduit is full. Kinematic wave analysis needs the area at that peak ([Kinematic wave and steady flow routing](kinematic-wave-and-steady-flow.md)). For a closed rectangle SWMM sets the peak at 97% full and lets the section factor fall linearly to its full value, because the top width joining the wetted perimeter would otherwise make a jump [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

Table 5-13, area at maximum flow over full area [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md):

| Ratio | Shapes |
|---|---|
| 0.9756 | circular |
| 0.97 | rectangular |
| 0.98 | catenary, semi-elliptical, rectangular-triangular, rectangular-round |
| 0.96 | elliptical, basket handle, egg, horseshoe, gothic, semi-circular, modified basket handle |
| 0.92 | arch |

For open shapes the area at maximum flow is the full area [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Area from section factor.** Circular and masonry shapes use a reverse table lookup. The others use the Newton-Raphson-Bisection method of Appendix A, converged to 0.01 percent of the full area [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Critical and normal depth.** [Dynamic wave routing](dynamic-wave-routing.md) needs them when a conduit meets a free outfall or a free fall at a node [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Critical depth is where the Froude number is 1. Rectangular and triangular shapes have explicit formulas (French, 1985), as do parabolic and power law shapes (Swamee, 1993). Other shapes use interval enumeration ("SWMM 5 currently uses N = 25" intervals of the full depth) or Ridder's method (Press and others, 1992) [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Normal depth: the section factor from the flow, then the area for that section factor, then the depth for that area [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Not in the raw file.** Page 80, with the graphs of the circular tables, and page 102, which says when interval enumeration beats Ridder's method and gives the normal-depth equation (Q92).

**Added 17 November 2026, fourth batch.** [SWMM5 · SWMM6 Curve Sections (app)](../entities/swmm5-swmm6-curve-sections.md) replaces the lookup tables with arcs and lines. In a Gothic sewer in dry weather the tables make the last conduit ring between about 0.46 and 0.98 cfs and hand the outfall a peak 29 % bigger than the 0.76 cfs that ever entered; with curves it climbs to 0.760. The Horseshoe's width table describes another outline than its other four, about 12 % apart at y/H = 0.08 [S262](../sources/S262-swmm5-swmm6-curve-sections-summary.md). A summary Claude wrote from the page (Q108).

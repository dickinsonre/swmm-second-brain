---
title: "Quasi-2D Mesh Maker for SWMM5 (app)"
type: entity
updated: 2026-11-17
sources: [S205, S241, S242]
tags: [apps, swmm5, quasi-2d, overland-flow, mesh]
reviewed: no
---
Bob's app Quasi-2D Mesh Maker for SWMM5: a generator that takes a flood boundary, obstructions and a ground surface (planes, a street valley, a sag, rolling ground, a DEM or survey points) and writes a PCSWMM-style quasi-2D overland mesh as a SWMM5 .inp, with links to a 1D sewer. No engine runs in the page. Version 1.0, 2026-10-04 [S241](../sources/S241-quasi-2d-mesh-maker-summary.md). Netlify address: https://quasi-2d-mesh-maker.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S241](../sources/S241-quasi-2d-mesh-maker-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S241](../sources/S241-quasi-2d-mesh-maker-summary.md)
- Its storage-exact mesh, with half-width links that hold exactly the cell area, measured stored area / plan area = 1.000 in EPA SWMM 5.2.4 built from source on 4 October 2026.
- Sheet flow, 4 in/hr on a 1 % plane of 200 x 400 ft at n = 0.03: both width rules reach the same steady depth; only the storage-exact mesh gets there on time (kinematic time of concentration 9.5 min). Its link velocities show twice the sheet-flow velocity.
- Continuity, rain as subcatchments or as direct inflow: hexagonal 286 cells -0.07 % and 0.00 %; rectangular 256 cells -0.08 % and -0.02 %.
- Whole cells cover 97 % of the area inside the boundary; cells are not clipped. A 2D conduit is dropped when the line between two cell centres crosses an obstruction edge.
- 20,000 random points: none inside more than one subcatchment polygon.

**What it does not show.** No comparison with PCSWMM's own width rule or a 2D shallow-water solver, and no test of diagonal flow. [S241](../sources/S241-quasi-2d-mesh-maker-summary.md)

**Noted at ingest.** [Walk the Mesh (app)](walk-the-mesh.md) reports the same storage doubling on the plain mesh and a different fix, Manning's n times 0.841 [S242](../sources/S242-walk-the-mesh-summary.md); this page's fix is the half-width link. Both are pages Claude summarized; neither cites the other.

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Walk the Mesh (app)](walk-the-mesh.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md), [Subcatchment width](../concepts/subcatchment-width.md).

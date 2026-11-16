---
title: "ICM 2D: terrain, mesh and subgrid sampling"
type: concept
updated: 2026-11-16
sources: [S166, S167, S172]
tags: [icm, 2d, mesh, terrain, subgrid]
reviewed: no
---
How an InfoWorks ICM 2D zone becomes a mesh, and how subgrid sampling changes what one element can hold. These pages rest on notes written by the GPT plugin for Autodesk [S166](../sources/S166-note-icm-notes-from-gpt-plugin.md): AI-written text whose facts about ICM are reported from Autodesk's 2027 help and were not checked against ICM, and whose tests have not been run (Q90).

**From zone to mesh.** The 2D zone sets the area to mesh. ICM forms triangular elements from the meshing inputs and takes their elevations from the selected ground model [S167](../sources/S167-note-icm-2d-terrain-and-mesh.md).

**The inputs, and what to check on each** [S167](../sources/S167-note-icm-2d-terrain-and-mesh.md)

| Input | Check |
|---|---|
| Ground model | source, coordinate system, vertical datum, survey date; critical elevations against surveyed levels |
| 2D zone | what is included; where the outer boundary cuts flow paths |
| Mesh zone | refinement around a channel, gutter or entrance |
| Break line | mesh edges follow the line; a hydraulic crest needs terrain levels or a structure |
| Mesh level zone | which element elevations it changes |
| Roughness zone | the resistance, and whether its edge acts as a break line |
| Void, building or wall | whether it removes area, changes levels or controls cross-flow |

The note's advice: choose mesh controls by how water will move, and check the mesh in section near kerbs, road crowns, banks, building gaps and low points. A first test compares a baseline mesh and a locally refined one on one street reach: crest and gutter elevations, inundation timing at fixed points, and discharge across one results line [S167](../sources/S167-note-icm-2d-terrain-and-mesh.md).

**Subgrid sampling** [S172](../sources/S172-note-icm-2d-subgrid-sampling.md)
- Finer terrain is used to build a volume-level table inside each element and to sample the terrain profile along each face; the face profile enters the mass and momentum fluxes.
- A crest that runs through the middle of an element can be bypassed (so, in our reading, mesh alignment still matters).
- Autodesk's 2027 help calls it a Tech Preview, needing a license with unlimited elements to mesh or run.
- In GeoPlan the subgrid speed theme shows the parent element's speed on wetted subtriangles.

**The proposed comparison** [S172](../sources/S172-note-icm-2d-subgrid-sampling.md): a corridor with an embankment and one gap, run four ways (fine mesh aligned to the crest as reference; coarser mesh; coarser mesh with subgrid; subgrid with edges aligned to the crest), comparing storage, arrival on both sides, flow through the gap and volume over the crest. The note links it to "the SWMM2D work". It is case 3 on [ICM 2D: three benchmark cases](icm-2d-benchmark-cases.md).

**Related.** [ICM 2D: boundaries and 1D-2D exchange](icm-2d-boundaries-and-exchange.md), [InfoWorks ICM](../entities/infoworks-icm.md).

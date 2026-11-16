# Test ICM subgrid storage and flow across faces separately

**Status:** seed
**Date:** 2026-11-16

## The idea

ICM subgrid sampling uses finer terrain to form volume–level tables within 2D elements and to sample the terrain profile along their faces. The face profile enters the mass and momentum flux calculations. Autodesk also documents that a crest through the middle of an element can be bypassed. Its 2027 help describes the feature as a Tech Preview and says that meshing or running it requires a license with unlimited elements.

## Proof / from scratch

Build a small corridor with an embankment and a single surveyed gap. Use the same ground model, event, boundary settings, and result locations in each run.

| Run | What it tests |
|---|---|
| Fine conventional mesh aligned to the crest | Reference result for the chosen terrain and opening |
| Coarser conventional mesh | Sensitivity to the hydraulic mesh resolution |
| Coarser mesh with subgrid sampling | Storage and face-sampling behavior at the same coarser resolution |
| Subgrid with the mesh edges aligned to the crest | Effect of alignment where the coarser mesh crossed the raised feature |

Compare upstream storage, arrival at both sides of the crest, flow through the gap, and volume crossing the embankment. Preserve fixed-point hydrographs and the mesh geometry. In GeoPlan, check whether results are shown on elements or on subgrid triangles. Autodesk describes the subgrid speed theme as using the parent-element speed on wetted subtriangles.

Record the exact ICM build, mesh and subgrid triangle areas, supported options, and license. This is a proposed comparison for the SWMM2D work.

## Links

- [Autodesk Subgrid Sampling Methodology](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-65E3FF30-A990-423A-8C83-1E7925DB9C5F.htm)
- [Autodesk Using Subgrid Sampling and supported items](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-0AB4AD8A-99DD-4AB1-9E27-083F538B3AE0.htm)
- [2D terrain and mesh](./icm-2d-terrain-and-mesh.md)
- [2D results and hazard](./icm-2d-results-and-hazard.md)

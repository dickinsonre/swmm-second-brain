# Build the ICM 2D mesh around the flow paths that matter

**Status:** seed
**Date:** 2026-11-16

## The idea

The 2D zone defines the area to mesh. InfoWorks ICM forms triangular elements from the meshing inputs and takes elevations from the selected ground model. Choose mesh controls based on how water will move across the site. Check the resulting geometry in section near kerbs, road crowns, banks, building gaps, and low points.

## Proof / from scratch

| Input | What to check |
|---|---|
| Ground model | Record source, horizontal coordinate system, vertical datum, and survey date. Compare critical elevations to surveyed levels. |
| 2D zone | Check which areas are included and where the outer boundary intercepts flow paths. |
| Mesh zone | Refine around a channel, gutter, or entrance. Inspect the generated element sizes and alignment. |
| Break line | Verify that mesh edges follow the intended line. Use terrain levels or a structure where a hydraulic crest is required. |
| Mesh level zone | Inspect which element elevations the polygon changes and the resulting cross section. |
| Roughness zone | Check the assigned resistance and whether the boundary is used as a break line. |
| Void, building, or wall | Record whether the feature removes area, changes levels, or controls cross-flow. Use the treatment that represents the site. |

For a first check, pick one street reach. Build a baseline mesh and a locally refined mesh with the same terrain and event. Compare the crest and gutter elevations, inundation timing at fixed coordinates, and discharge across one results line. Record the mesh generation method, element count, and meshing log. Use the same points and line in both runs.

## Links

- [Autodesk 2D mesh generation methodology](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-24EB7F2A-778D-4815-8F54-4DE299B8D532.htm)
- [Autodesk creating 2D meshes](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-2FCDC59C-8636-46C1-A65C-FCB282B393E1.htm)
- [Autodesk structure and 2D tutorials](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-A15E3F2C-54BA-468E-B100-EA18C7EFEA00.htm)
- [Subgrid sampling and barrier alignment](./icm-2d-subgrid-sampling.md)

# Keep ICM flood maps tied to the result definition and its time

**Status:** seed
**Date:** 2026-11-16

## The idea

Specify the quantity and time basis for each exported 2D result. Depth, level, speed, time to first inundation, and hazard answer different questions. InfoWorks documents results for depth and speed at the first maximum hazard. Use that matched pair to explain a hazard map at a selected location.

## Proof / from scratch

| Output | What to record |
|---|---|
| Depth or level | Units, terrain reference or vertical datum, timestep or maximum, and wet/dry threshold |
| Speed and direction | Location, units, and the same time used for the plotted depth when comparing the two |
| First inundation | The depth threshold that defines arrival |
| Hazard | The hazard definition, time basis, and associated depth and speed fields |
| Flow across a transect | The physical line and sign convention, with a hydrograph and event volume |

Pick three fixed points and a transect such as a street crossing. Use Network Results objects to capture results at those locations. Repeat the same geometry after remeshing. Export the map and the hydrograph together so the timing and flow direction can be checked. Use the documented `Depth at first max hazard` and `Speed at first max hazard` fields when reviewing maximum hazard. Record the ICM build, scenario, and mesh version with the export.

## Links

- [Autodesk 2D zone results data fields](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-1128CF97-0DB4-4583-B3C9-109EB9C8C2F8.htm)
- [Autodesk network results object data fields](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-17CA706F-D4CC-49F3-A8BC-EB61F8267408.htm)
- [Autodesk extracting results from the 2D domain](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Extracting-results-from-the-2D-domain-in-InfoWorks-ICM.html)
- [Subgrid sampling and barrier alignment](./icm-2d-subgrid-sampling.md)

# Check water volume for the 2D domain and the combined ICM model

**Status:** seed
**Date:** 2026-11-16

## The idea

Balance each control volume over the same interval. For the 2D mesh by itself, sewer or river exchange crosses its boundary. For the combined 1D and 2D hydraulic model, the same transfer is internal and cancels. Use the PRN volume summary alongside local checks near important exchanges and boundaries.

## Proof / from scratch

Record starting and ending volume, input, and output using one unit system and a stated sign convention. Calculate the residual as starting storage plus inputs, minus outputs and ending storage.

| Control volume | Terms to gather for the run |
|---|---|
| 2D mesh | Direct rain, boundary flows, signed transfer with 1D, applied losses, and change in surface volume |
| Combined 1D and 2D hydraulics | External inflows, delivered subcatchment runoff, direct mesh rain, external discharges, external losses, and change in combined storage |

Include each transfer once for the domain being checked. If infiltration is routed into 1D through a permeable zone, track its destination so it is treated as a transfer in the combined balance.

For a first independent check, run the closed rainfall box in the benchmark note. Compare the rain volume from depth times area with stored water. In a subgrid case, extract the documented element volume result where available. The volume–level table provides the storage for subgrid elements.

If the reported and independently checked volumes disagree, compare the time window, units, boundary sign, and results used before changing solver controls.

## Links

- [Autodesk support on reviewing PRN volume and dynamic storage](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-assess-dynamic-storage-volume-in-InfoWorks-ICM.html)
- [Autodesk 2D zone results data fields](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-1128CF97-0DB4-4583-B3C9-109EB9C8C2F8.htm)
- [Autodesk 2D mesh methodology and permeable zones](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-24EB7F2A-778D-4815-8F54-4DE299B8D532.htm)
- [2D benchmark cases](./icm-2d-benchmark-cases.md)

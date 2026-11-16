# Use bank crest profiles to check river–floodplain exchange in ICM

**Status:** seed
**Date:** 2026-11-16

## The idea

An InfoWorks River Reach can spill to a connected 2D zone over a bank. Autodesk documents the bank calculation as a segmented irregular weir with forward and reverse modes. The bank crest, adjoining mesh elevations, and the water levels on each side determine when a bank segment flows.

## Proof / from scratch

1. For a short reach, record cross sections, left and right bank lines, bank crest profiles, and the receiving 2D zone. Use one vertical datum for the section survey and floodplain terrain.
2. After meshing, view a section across each important low point. Verify the bank vertices and adjacent mesh faces. Capture the run's `Adjust bank levels based on adjacent element ground levels` setting. Autodesk documents that it can raise low bank sections to match the adjoining mesh elevation.
3. Drive one hydrograph past the bank crest and down again. Record river stage, floodplain stage, and signed bank discharge. Test return flow where the floodplain level remains above the river with a wet path across the bank.
4. Compare the time of first spill and the integrated exchange volume at the same segment under a local mesh refinement. Preserve screenshots or plots at the initial spill and recession.

If validation flags E10553 during clip meshing, inspect the cited bank geometry and nearby vertices. Keep the corrected line geometry with the run record so subsequent remeshing can reproduce the connection.

## Links

- [Autodesk River Reach bank flows](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-50940862-CDB2-4364-A74D-004982072B63.htm)
- [Autodesk 2D Parameters dialog](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-251BAAB1-AC3C-4F9D-8EE4-585FFBF51CF3.htm)
- [Autodesk support on E10553 during clip meshing](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/E10553-Bank-connection-for-2D-zone-is-invalid-Bank-geometry-between-vertices-1-and-2-incompatible-with-2D-mesh-when-validating-a-network-in-InfoWorks-ICM.html)
- [2D terrain and mesh](./icm-2d-terrain-and-mesh.md)

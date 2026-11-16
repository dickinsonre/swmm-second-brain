# Give each ICM 2D boundary segment a physical purpose

**Status:** seed
**Date:** 2026-11-16

## The idea

The 2D zone has a default boundary condition. A 2D Boundary line can assign a different condition along a portion of the edge. Keep a segment inventory so that an intended valley outlet or tidal connection is easy to distinguish from a closed edge in the run.

## Proof / from scratch

| Boundary type | Use or behavior to verify |
|---|---|
| Vertical Wall | Closed edge. Verify zero crossing flow in a closed-domain benchmark. |
| Critical Depth | Outward discharge when the 2D level is above the boundary face, using the documented weir calculation. |
| Supercritical | Outward discharge under the documented supercritical and outward-flow conditions. |
| Normal Depth | Outflow using the documented normal-flow assumption. Check its suitability for the outlet location. |
| Inflow | Flow is prescribed by the matching profile in an Inflow Event. Confirm the sign and total integrated volume. |
| Level | Stage is prescribed by the matching profile in a Level Event. Verify the event datum against the boundary face elevations. |

For each edge record its type, length, connected faces, ground levels, event profile, and expected flow direction. In a small sloping test, start with three closed edges and one outlet. Run a known inflow and compare downstream stage, outlet hydrograph, and net boundary volume. If changing the outlet condition alters interior results materially, test the outlet location and document the sensitivity.

## Links

- [Autodesk 2D boundary data fields for InfoWorks](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-0FEF709A-E03D-4210-9252-163FC0C05534.htm)
- [Autodesk 2D zone data fields for InfoWorks](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-111E1710-4BA5-4F49-8596-E5B00C4F6CE6.htm)
- [River reach and floodplain bank exchange](./icm-2d-river-bank-exchange.md)
- [2D volume balance](./icm-2d-volume-balance.md)

# Compare node level and node depth on the same reference elevation

**Status:** seed
**Date:** 2026-11-16

## The idea

The result name is only part of the mapping. Autodesk labels `DEPNOD` as level at the current timestep in an InfoWorks network. ICM SWMM documents `HEAD` as hydraulic head elevation and `DEPTH` as water depth above the node inlet elevation. Record the quantity, unit, reference elevation, and whether the value is a time series or a summary.

## Proof / from scratch

| Quantity | InfoWorks results | ICM SWMM results | Comparison |
|---|---|---|---|
| Node water level | `DEPNOD` | `HEAD` | Compare elevations on a common vertical datum |
| Node water depth above inlet | Compute from level and the corresponding inlet elevation | `DEPTH` | Check that the same inlet elevation is used |

For an illustrative wet node with an inlet elevation of 106.00 ft, a level of 109.25 ft corresponds to a depth of 3.25 ft. Try the check on one known timestep before comparing hydrographs.

Log the network type, scenario, simulation ID, object ID, result attribute, timestamp, and units. Confirm the available fields in the loaded simulation. Align time series by time, and record the flow sign convention before extending the comparison to link flows or runoff.

## Links

- [Autodesk Node Results Data Fields for InfoWorks](https://help.autodesk.com/cloudhelp/2025/ENU/ICM-Help/files/GUID-18FD4962-1E97-491A-AD6E-6DF35191301D.htm)
- [Autodesk Node Results Data Fields for SWMM](https://help.autodesk.com/cloudhelp/2025/ENU/ICM-Help/files/GUID-19396381-A60F-4586-90FA-F258221203C3.htm)
- [Bob's IWR guide already queued for ingest](https://github.com/dickinsonre/swmm-second-brain/blob/main/raw/linkedin/2023-11-12-mastering-icm-swmm-infoworks-ruby-guide-iwr-results-file-dickinson-5z9se.md)
- [ICM Exchange run lifecycle](./icm-exchange-run-lifecycle.md)

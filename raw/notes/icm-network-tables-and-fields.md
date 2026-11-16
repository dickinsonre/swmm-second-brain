# Look up the ICM network type before choosing Ruby table and field names

**Status:** seed
**Date:** 2026-11-16

## The idea

InfoWorks and SWMM networks use different model data tables. Autodesk's Network Data Fields index pairs each object type with its table and a detailed field reference. For the Smart Table Exporter, identify the network type first, then resolve the exact database field for that table. Keep the UI label with the database field so an exported column can be traced back to GeoPlan.

## Proof / from scratch

| Object | InfoWorks network table | ICM SWMM network table |
|---|---|---|
| Node | `hw_node` | `sw_node` |
| Conduit | `hw_conduit` | `sw_conduit` |
| Subcatchment | `hw_subcatchment` | `sw_subcatchment` |

1. Choose a small network with a node, conduit, and subcatchment. Record the ICM build and the network type.
2. For one property per object, open the detailed data field help and record the grid label, database field, unit, and permitted values if enumerated.
3. Read the property on a known object. Compare the script's value to the grid or a native export using the same unit settings.
4. Repeat for the other network type and record any missing field as unavailable. Then extend the same lookup to other tables, including the tables the exporter skips.

For each exported value keep the network type, table, object ID, database field, and unit. Put simulation variables in the accompanying results field guide.

## Links

- [Autodesk Network Data Fields](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-8F131349-1247-477B-97A5-62B9AF41D9E4.htm)
- [Ruby database reference](https://github.com/innovyze/Open-Source-Support/blob/main/01%20InfoWorks%20ICM/01%20Ruby/03%20Context/InfoWorks_ICM_Ruby_Database_Reference.md)
- [Ruby database fields guide](https://github.com/innovyze/Open-Source-Support/blob/main/01%20InfoWorks%20ICM/01%20Ruby/03%20Context/InfoWorks_ICM_Ruby_Database_Fields_Guide.md)
- [ICM results field crosswalk](./icm-results-field-crosswalk.md)

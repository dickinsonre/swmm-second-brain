---
title: ICM network tables and result fields
type: concept
updated: 2026-11-17
sources: [S162, S163, S17, S166, S178, S179, S243]
tags: [icm, ruby, data-model, results, comparison]
reviewed: no
---
InfoWorks ICM keeps its two network types in different tables and reports their results under different names. Two notes Bob supplied on 16 November 2026 map the first few. ChatGPT drafted them from Autodesk Help [S179](../sources/S179-note-icm-notes-drafted-by-chatgpt.md), so they are AI-written; their Autodesk facts are reported from Autodesk's help and not checked here, and nothing in them has been run (Q90).

**Two network types.** An InfoWorks network, solved by ICM's own St. Venant scheme, and an ICM SWMM network, which runs the SWMM5 dynamic wave [S17](../sources/S17-li-routing-options.md). See [InfoWorks ICM](../entities/infoworks-icm.md).

**Model data tables** [S162](../sources/S162-note-icm-network-tables-and-fields.md)

| Object | InfoWorks network | ICM SWMM network |
|---|---|---|
| Node | `hw_node` | `sw_node` |
| Conduit | `hw_conduit` | `sw_conduit` |
| Subcatchment | `hw_subcatchment` | `sw_subcatchment` |

Infiltration Surface (2D) objects, in an InfoWorks network, are stored in `hw_2d_infil_surface` [S178](../sources/S178-li-cnswmm-on-the-icm-2d-mesh.md).

The note's rule for a Ruby exporter: find the network type first, then the exact database field in that table, from Autodesk's Network Data Fields index. Keep the interface label beside the database field so an exported column can be traced to GeoPlan. For each exported value keep the network type, table, object ID, database field and unit, and record a field missing from one network type as unavailable [S162](../sources/S162-note-icm-network-tables-and-fields.md).

**Node results** [S163](../sources/S163-note-icm-results-field-crosswalk.md)

| Quantity | InfoWorks result | ICM SWMM result | How to compare |
|---|---|---|---|
| Water level | `DEPNOD`, level at the current timestep | `HEAD`, hydraulic head elevation | on a common vertical datum |
| Depth above the inlet | computed from level and the inlet elevation | `DEPTH` | check both use the same inlet elevation |

Worked example from the note: an inlet at 106.00 ft and a level of 109.25 ft give a depth of 3.25 ft [S163](../sources/S163-note-icm-results-field-crosswalk.md).

**Before comparing hydrographs** [S163](../sources/S163-note-icm-results-field-crosswalk.md): log network type, scenario, simulation ID, object ID, result attribute, timestamp and units; confirm the field exists in the loaded simulation; align the series by time; and record the flow sign convention before going on to link flows or runoff.

**Related.** [ICM Ruby: UI scripts and Exchange scripts](icm-ruby-ui-and-exchange.md); [SWMM 5 versus ICM InfoWorks](swmm5-versus-icm-infoworks.md); [Checking a SWMM5 model's conversion into ICM](swmm5-to-icm-conversion-checks.md).

**Not in the sources yet.** Link and subcatchment result fields, and the rest of the tables. The note points to Bob's queued article on the IWR results file as the next source [S163](../sources/S163-note-icm-results-field-crosswalk.md).

**Added 17 November 2026, third batch.** A Ruby schema dump of ICM printed 91 tables, 6,823 fields and 385 blob sub-fields; 21 tables start with hw_2d. Against Autodesk's help, eight field names appear only in the help and seven only in the dump. The ICM version of the dump was not recorded [S243](../sources/S243-icm-2d-table-atlas-summary.md).

**Relations**

| Subject | Relation | Object | Note | Source |
|---|---|---|---|---|
| `icm:InfoWorksNetwork`, `icm:SWMMNetwork` | `is_a` | `sb:NetworkType` |  | [S17](../sources/S17-li-routing-options.md) |
| `icm:InfoWorksNetwork`, `icm:SWMMNetwork` | `part_of` | `icm:ICM` |  | [S17](../sources/S17-li-routing-options.md) |
| `icm-iw:hw_node`, `icm-iw:hw_conduit`, `icm-iw:hw_subcatchment`, `icm-swmm:sw_node`, `icm-swmm:sw_conduit`, `icm-swmm:sw_subcatchment` | `is_a` | `sb:DataTable` |  | [S162](../sources/S162-note-icm-network-tables-and-fields.md) |
| `icm-iw:hw_node`, `icm-iw:hw_conduit`, `icm-iw:hw_subcatchment` | `part_of` | `icm:InfoWorksNetwork` |  | [S162](../sources/S162-note-icm-network-tables-and-fields.md) |
| `icm-swmm:sw_node`, `icm-swmm:sw_conduit`, `icm-swmm:sw_subcatchment` | `part_of` | `icm:SWMMNetwork` |  | [S162](../sources/S162-note-icm-network-tables-and-fields.md) |
| `icm-iw:hw_node` | `close_match` | `icm-swmm:sw_node` | `condition: the fields differ by network type; find each in Autodesk's Network Data Fields index` `verification: documented` both hold nodes | [S162](../sources/S162-note-icm-network-tables-and-fields.md) |
| `icm-iw:hw_conduit` | `close_match` | `icm-swmm:sw_conduit` | `condition: the fields differ by network type; find each in Autodesk's Network Data Fields index` `verification: documented` both hold conduits | [S162](../sources/S162-note-icm-network-tables-and-fields.md) |
| `icm-iw:hw_subcatchment` | `close_match` | `icm-swmm:sw_subcatchment` | `condition: the fields differ by network type; find each in Autodesk's Network Data Fields index` `verification: documented` both hold subcatchments | [S162](../sources/S162-note-icm-network-tables-and-fields.md) |
| `icm-iw:hw_2d_infil_surface` | `is_a` | `sb:DataTable` |  | [S178](../sources/S178-li-cnswmm-on-the-icm-2d-mesh.md) |
| `icm-iw:hw_2d_infil_surface` | `part_of` | `icm:InfoWorksNetwork` |  | [S178](../sources/S178-li-cnswmm-on-the-icm-2d-mesh.md) |
| `icm-iw:InfiltrationSurface2D` | `stored_in` | `icm-iw:hw_2d_infil_surface` |  | [S178](../sources/S178-li-cnswmm-on-the-icm-2d-mesh.md) |
| `icm-iw:DEPNOD`, `icm-swmm:HEAD`, `icm-swmm:DEPTH` | `is_a` | `sb:ResultField` |  | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
| `icm-iw:DEPNOD` | `part_of` | `icm:InfoWorksNetwork` |  | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
| `icm-swmm:HEAD`, `icm-swmm:DEPTH` | `part_of` | `icm:SWMMNetwork` |  | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
| `icm-iw:DEPNOD` | `reports` | `qty:WaterLevel` | `verification: documented` level at the current timestep | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
| `icm-swmm:HEAD` | `reports` | `qty:WaterLevel` | `verification: documented` hydraulic head elevation | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
| `icm-swmm:DEPTH` | `reports` | `qty:DepthAboveInlet` | `verification: documented` water depth above the node inlet elevation | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
| `icm-iw:DEPNOD` | `close_match` | `icm-swmm:HEAD` | `condition: on a common vertical datum` `verification: pending` no run has compared them (Q90) | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
| `qty:DepthAboveInlet` | `derived_from` | `qty:WaterLevel`, `qty:InletElevation` | `condition: both sides use the same inlet elevation` depth = level - inlet elevation; 109.25 ft - 106.00 ft = 3.25 ft | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |
| `qty:WaterLevel`, `qty:DepthAboveInlet`, `qty:InletElevation` | `is_a` | `sb:Quantity` |  | [S163](../sources/S163-note-icm-results-field-crosswalk.md) |

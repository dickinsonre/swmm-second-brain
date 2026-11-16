---
title: "ICM 2D: boundaries and 1D-2D exchange"
type: concept
updated: 2026-11-16
sources: [S166, S168, S170, S171]
tags: [icm, 2d, boundary-conditions, 1d-2d, river]
reviewed: no
---
Where water enters and leaves an InfoWorks ICM 2D zone: its edges, its manholes and its river banks. These pages rest on notes written by the GPT plugin for Autodesk [S166](../sources/S166-note-icm-notes-from-gpt-plugin.md): AI-written text whose facts about ICM are reported from Autodesk's 2027 help and were not checked against ICM, and whose tests have not been run (Q90).

**Edges** [S168](../sources/S168-note-icm-2d-boundary-conditions.md). The zone has a default boundary condition, and a 2D Boundary line can set a different one along part of the edge.

| Type | Behavior to verify |
|---|---|
| Vertical Wall | closed: zero crossing flow |
| Critical Depth | outward flow when the 2D level is above the face, by the documented weir calculation |
| Supercritical | outward flow under the documented supercritical conditions |
| Normal Depth | outflow on a normal-flow assumption |
| Inflow | flow from the matching profile of an Inflow Event; check sign and total volume |
| Level | stage from the matching profile of a Level Event; check the datum |

Keep an inventory of each edge: type, length, faces, ground levels, event profile, expected direction. If changing the outlet type changes interior results materially, document that sensitivity [S168](../sources/S168-note-icm-2d-boundary-conditions.md).

**Manholes** [S170](../sources/S170-note-icm-1d-2d-node-exchange.md). The node's flood type sets the exchange relation:
- 2D: a weir, with the node ground level as crest and the shaft circumference as length.
- Gully 2D: a user-given head-discharge relationship.
- Inlet 2D: user-given inlet parameters.
- Outfall 2D and Connect 2D are further node types with their own rules.

Warning 1053 says one or more nodes had their flow from the 2D zone limited; record the nodes and the limited flow with the run [S170](../sources/S170-note-icm-1d-2d-node-exchange.md). The reversing-manhole test is case 2 on [ICM 2D: three benchmark cases](icm-2d-benchmark-cases.md).

**River banks** [S171](../sources/S171-note-icm-2d-river-bank-exchange.md). A River Reach spills to a connected 2D zone over its banks, computed as a segmented irregular weir with forward and reverse modes. Bank crest, adjoining mesh elevations and the levels on each side decide when a segment flows. The option `Adjust bank levels based on adjacent element ground levels` can raise low bank sections to the mesh. Error E10553 during clip meshing flags bank geometry incompatible with the mesh between two vertices.

**What to plot.** For every exchange, both water levels and the signed flow on one time axis, through a rise and a fall, so the crest, sign and timing can be read [S170](../sources/S170-note-icm-1d-2d-node-exchange.md) [S171](../sources/S171-note-icm-2d-river-bank-exchange.md).

**Related.** [ICM 2D: terrain, mesh and subgrid sampling](icm-2d-mesh-and-subgrid.md), [ICM 2D: timestep, volume balance and results](icm-2d-runs-and-checks.md).

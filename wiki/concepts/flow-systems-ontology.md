---
title: Flow Systems Ontology (FSO)
type: concept
updated: 2026-11-16
sources: [S191, S60]
tags: [ontology, vocabulary, method]
reviewed: no
---
The Flow Systems Ontology is a published vocabulary for describing how a flow system is put together: which components it has, how they connect, and which way water, air, heat or electricity moves between them [S191](../sources/S191-paper-kukkonen-2022-flow-systems-ontology.md). It was written for building HVAC, by Kukkonen and five co-authors, and is published at https://w3id.org/fso [S191](../sources/S191-paper-kukkonen-2022-flow-systems-ontology.md). It matters to this wiki as an outside vocabulary for network objects, which `ONTOLOGY.md` does not yet have.

**What it holds** [S191](../sources/S191-paper-kukkonen-2022-flow-systems-ontology.md)
- 14 classes and 23 object properties.
- Systems and components. A system is a virtual collection of components and may belong to several supersystems; a component is a tangible object in the flow.
- Eight component classes: Segment (pipes, ducts, cables), Fitting (pipe junctions), FlowController (valves, dampers), FlowMovingDevice (pumps, fans), StorageDevice (tanks), Terminal (where a system meets the environment), TreatmentDevice (filters), EnergyConversionDevice (motors, heat exchangers).
- Flow relations under the symmetric `connectedWith`: `feedsFluidTo` gives the order of the fluid, and its subproperties `suppliesFluidTo` and `returnsFluidTo` split a loop into its two sides; `exchangesHeatWith` and `exchangesElectricChargeWith` cover heat and power.
- Source and consumer are relations to a system, not properties of a component.

**Why it is of use here.** Its competency question CQ5, "What components are up/downstream of a component, and in what order?", is a drainage question too [S191](../sources/S191-paper-kukkonen-2022-flow-systems-ontology.md). The EPA hydraulics manual already describes a SWMM 5 junction as "a manhole, a fitting, a confluence" and a storage unit as "the only node with storage volume" [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md), which reads close to FSO's Fitting and StorageDevice. `ONTOLOGY.md` sets out a proposed alignment of SWMM 5 and ICM network objects to FSO's classes, so that objects of different programs can be compared by kind. It is the wiki's proposal, not a claim of either source, and waits for Bob (Q98). See also [SWMM 5 network objects](swmm5-network-objects.md).

**Limits** [S191](../sources/S191-paper-kukkonen-2022-flow-systems-ontology.md)
- Built and tested for HVAC; other flow domains were not investigated.
- Topology only. It does not describe component properties, so it cannot by itself describe a simulation's inputs or outputs.
- Validated mostly on two example models with hand-written triples.

**Not in the sources.** `feedsFluidTo` names one direction. A drainage model's link has a defined direction, from its inlet node to its outlet node, and its flow can run against it; whether the relation would mean the defined direction or the flow is part of Q98.

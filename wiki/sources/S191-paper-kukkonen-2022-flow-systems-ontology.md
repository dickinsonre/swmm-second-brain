---
title: "S191: Kukkonen and others (2022), An ontology to support flow system descriptions from design to operation of buildings"
type: source
raw: raw/papers/kukkonen-2022-flow-systems-ontology.pdf
kind: journal-paper
author: Ville Kukkonen, Ali Kücükavci, Mikki Seidenschnur, Mads Holten Rasmussen, Kevin Michael Smith and Christian Anker Hviid
published: 2021-12-09
ingested: 2026-11-16
drafted_by: "the six named authors (a peer-reviewed journal paper, 2021; it states no AI use)"
tags: [ontology, vocabulary, method]
reviewed: no
---
**What it is.** A peer-reviewed paper in *Automation in Construction* 134 (2022) 104067, https://doi.org/10.1016/j.autcon.2021.104067. Received 18 November 2020, accepted 23 November 2021, available online 9 December 2021. It proposes the Flow Systems Ontology (FSO), published at https://w3id.org/fso. Open access under CC BY 4.0. Raw file: [raw/papers/kukkonen-2022-flow-systems-ontology.pdf](../../raw/papers/kukkonen-2022-flow-systems-ontology.pdf), the publisher's PDF, 15 pages. Bob supplied it on 16 November 2026 and said to add it.

**How it was written.** By six authors at Aalto University, Granlund, the Technical University of Denmark, Ramboll and NIRAS. The paper declares that four of them work for or were sponsored by industry firms while writing their doctoral dissertations. It is about buildings: heating, ventilation and air conditioning (HVAC). It never mentions sewers, storm drainage or SWMM. It is read here as a vocabulary the wiki might borrow, not as a source about drainage models.

**Claims worth keeping**
- The gap it fills: existing building ontologies (ifcOWL, BOT, Brick, SEAS, SAREF4SYST, SAREF4BLDG, RealEstateCore) describe devices, spaces and data points, but none describes the energy and mass flow between systems and components. Brick leaves out passive components such as pipes and ducts; SEAS lets a system belong to at most one supersystem; SAREF4BLDG leaves out pipes, ducts and their connections.
- FSO has 14 classes and 23 object properties, with a Description Logic expressivity of ALRI.
- Seven competency questions set its scope, among them: what components and subsystems a flow system contains; which components are sources or consumers; what components share a fluid loop; and "What components are up/downstream of a component, and in what order?" (CQ5).
- Two top classes. An `fso:System` is a virtual collection of components that can carry properties such as design requirements; a system may have subsystems and may belong to more than one supersystem. An `fso:Component` is a tangible object in the flow of energy or mass. `fso:SupplySystem` and `fso:ReturnSystem` are subclasses of `fso:DistributionSystem`.
- Eight component classes, based on the IFC class `IfcDistributionFlowElement`: EnergyConversionDevice (motors, heat exchangers), Fitting ("component used to connect segments to other segments, or to other components", such as pipe junctions), FlowController (valves, dampers), FlowMovingDevice (pumps, fans), Segment (pipes, ducts, cables), StorageDevice (a battery, a water tank), Terminal ("a device through which a system interacts with the environment", such as air terminals and water taps), TreatmentDevice (air filters).
- Being a source or a consumer is a relation to a system, not a property of the component: `fso:hasSourceComponent`, `fso:hasConsumerComponent`. A heating coil is a source of heat for a ventilation system and a consumer of heat for the heating system.
- Flow relations form a hierarchy under the symmetric `fso:connectedWith`: `exchangesFluidWith`, `exchangesHeatWith` and `exchangesElectricChargeWith`, all symmetric. Under `exchangesFluidWith`, `feedsFluidTo` and its inverse `hasFluidFedBy` give the order of the fluid; `suppliesFluidTo` and `returnsFluidTo` are subproperties of `feedsFluidTo` that split a loop into a supply side and a return side. Heat has `transfersHeatTo` and `transfersHeatFrom`.
- Why the split: following only `feedsFluidTo` around a closed loop reaches every component, so a query cannot tell one branch from another; supply and return break the loop.
- Reasoning: property chains infer system-level connections from component connections. If a pipe in a heating system supplies fluid to a coil in an air handling unit, the heating system is inferred to supply fluid to the air handling unit. A water-to-water heat exchanger is best modeled as two components that exchange heat, so the two fluid circuits stay separate.
- Alignments: FSO's System and Component are subclasses of `s4syst:System`, and its composition and connection properties are subproperties of SAREF4SYST's. SAREF4BLDG's device classes are declared subclasses of FSO's.
- Example models: an active chilled beam system for one room, and a heating system in a two-storey house with a heat exchanger, a pump, six radiators in four rooms and manual balancing valves, 76 components in all. Supply-side links use `suppliesFluidTo`, return-side links `returnsFluidTo`. The Turtle and SPARQL files are on Zenodo (https://doi.org/10.5281/zenodo.4492645).
- Queries on the heating model: the components serving one room in one system, 27 of the 76; the supply-side mass flow of each component, from m = Φ / (cp × ΔT), for example 560.13 lb/h at 20,132 Btu/h of downstream heat demand for the heat exchanger (254.07 kg/h at 5900 W; conversion ours); the flow-control components in one radiator's loop (one pump and three valves); the components upstream of a radiator, ordered by distance (12 steps back to the heat exchanger); and a CONSTRUCT query that drops segments and fittings to give a simplified logical topology.
- Limits the authors state: no formal ontology development method; validation mostly on the two example models with hand-written triples; definitions mainly from the authors' own experience; use outside HVAC "theorized" but "not investigated"; and FSO describes topology only, so "FSO alone is not sufficient for describing the inputs or outputs of simulation tools".
- Roadmap: stage 1 the ontology; stage 2 tools to convert IFC into FSO linked data; stage 3 domain ontologies extending FSO and parsers to applications, among them numerical flow analysis and fault detection. The authors say they are working to apply FSO "as a part of a new hydraulic simulation process".

**Not in the source.** The paper names no drainage object. Any match between SWMM5 or ICM objects and FSO classes is the wiki's own proposal, set out in `ONTOLOGY.md` and open as Q98.

**Feeds:** [Flow Systems Ontology (FSO)](../concepts/flow-systems-ontology.md), [Open questions](../open-questions.md) (Q98), and `ONTOLOGY.md`.

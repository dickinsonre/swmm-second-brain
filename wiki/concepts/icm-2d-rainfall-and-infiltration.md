---
title: "ICM 2D: rainfall and infiltration on the mesh"
type: concept
updated: 2026-11-16
sources: [S166, S169, S177, S178]
tags: [icm, 2d, rainfall, infiltration, curve-number]
reviewed: no
---
Rain on an InfoWorks ICM 2D mesh, where it overlaps subcatchments, and the infiltration it loses, including the history of the Curve Number on the mesh from Bob's own articles.

**Rain in two domains** [S169](../sources/S169-note-icm-2d-rainfall-and-infiltration.md). A rainfall event can fall on subcatchments and directly on 2D mesh elements. With direct mesh rainfall on, an area that is both can receive rain twice. The 2D zone's setting `outside subcatchments` keeps direct mesh rain off the overlap, and rainfall percentages on the zone and on infiltration zones set the allocation. This note is AI-written, from the GPT plugin for Autodesk, and was not checked against ICM [S166](../sources/S166-note-icm-notes-from-gpt-plugin.md).

**Infiltration surfaces in 2023** [S177](../sources/S177-li-curve-number-approximations-icm-2d.md). Subcatchments could use CN and CNSWMM on a pervious runoff surface, but a 2D infiltration surface had four choices: Horton, Green-Ampt, Constant Infiltration and Fixed. Bob approximated the Curve Number with them on a test model of 23 subcatchments whose IDs equal their CN, three storms of 0.065, 0.65 and 6.5 in (1.65, 16.5 and 165 mm; conversion ours), and parameters set by SQL. His findings:
- In 1D, lower CN gave a higher peak infiltration rate and a larger total volume.
- With a constant loss rate set from the CN peak, Horton, Green-Ampt and ConstInf matched CN closely in peak and volume, almost exactly for small storms.
- On the 2D mesh, for the smaller storm, Constant, Green-Ampt and Horton gave the same effective rate and Fixed did not; varying depths across the mesh make 2D differ from 1D.

**CNSWMM on the mesh from ICM 2025.1** [S178](../sources/S178-li-cnswmm-on-the-icm-2d-mesh.md). CNSWMM, the curve number model with initial losses, became an Infiltration Surface (2D) type, with Initial abstraction factor, Curve number and Drying time as properties, and a CNSWMM antecedent moisture condition among the 2D initial conditions. The types listed are Fixed, Horton, ConstInf, Green-Ampt, DefConLoss and CNSWMM; the data sits in `hw_2d_infil_surface`. The 2027 help still lists the method and its parameters [S169](../sources/S169-note-icm-2d-rainfall-and-infiltration.md).

**The check the note proposes** [S169](../sources/S169-note-icm-2d-rainfall-and-infiltration.md). A closed, flat zone with no infiltration, then the same with one infiltration surface: with no boundary flow or evaporation, applied rain equals final surface storage plus infiltrated volume. The no-infiltration version is case 1 on [ICM 2D: three benchmark cases](icm-2d-benchmark-cases.md).

**Related.** [Infiltration methods](infiltration-methods.md) for SWMM5's own Curve Number; [ICM 2D: timestep, volume balance and results](icm-2d-runs-and-checks.md).

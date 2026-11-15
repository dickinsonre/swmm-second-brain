---
title: SWMM 5 versus ICM InfoWorks
type: concept
updated: 2026-11-14
sources: [S13, S14, S17, S20]
tags: [comparison, swmm5, icm]
reviewed: 2026-11-15
---
Where the two engines differ, from the four comparison sources ingested so far. ICM also contains a SWMM network type ("ICM SWMM") that runs the SWMM5 dynamic wave [S17](../sources/S17-li-routing-options.md); this page compares SWMM 5 with the InfoWorks engine.

| Aspect | SWMM 5 | ICM InfoWorks | Source |
|---|---|---|---|
| Space | One element per conduit; head at nodes, flow in the link | Several segments per conduit, typically one every 150 to 200 ft | [S20](../sources/S20-li-edition-54-two-solvers.md) |
| Scheme | Node-link, EXTRAN lineage, relaxation | Preissmann four-point implicit, Newton-Raphson, adaptive time step | [S20](../sources/S20-li-edition-54-two-solvers.md) |
| Surcharge | EXTRAN method; SLOT optional since 5.1.013 | Preissmann slot from the beginning | [S20](../sources/S20-li-edition-54-two-solvers.md) |
| Typical continuity error | 0.1 to 0.5 % | 0.01 to 0.1 % | [S20](../sources/S20-li-edition-54-two-solvers.md) |
| Steady state | Yes | Quasi-steady only, from a saved state | [S17](../sources/S17-li-routing-options.md) |
| Kinematic wave | Yes | No | [S17](../sources/S17-li-routing-options.md) |
| Force main friction | User picks Manning, Hazen-Williams or Darcy-Weisbach | Built into a dedicated link type | [S20](../sources/S20-li-edition-54-two-solvers.md) |
| Dry or intermittent flow | Handled natively | Keeps a minimum base flow | [S20](../sources/S20-li-edition-54-two-solvers.md) |
| 2D surface flooding | No | Yes, mesh-based | [S20](../sources/S20-li-edition-54-two-solvers.md) |
| LID and water quality | Dedicated [LID](lid-bioretention-layers.md) module; the source calls SWMM 5 "the only platform with built in LID and water quality modeling" | Not described in the source. Queued articles on SUDS and buildup and washoff in ICM InfoWorks suggest otherwise: open question Q13 | [S20](../sources/S20-li-edition-54-two-solvers.md) |
| Runoff surfaces | Three subareas from two percentages | Three runoff surfaces tied by a Land Use ID | [S13](../sources/S13-li-three-runoff-surfaces.md) |
| Subarea routing | OUTLET, IMPERV, PERV | Direct, To pervious, To impervious | [S14](../sources/S14-li-subarea-routing.md) |
| Cost and source | Free, public domain, open source | Commercial | [S20](../sources/S20-li-edition-54-two-solvers.md) |

**How far apart are the answers?** On a five-node network in a moderate storm, peaks differ by 2 to 3 % and timing by one or two time steps. They diverge at the extremes: heavy surcharge, rapid flow reversal, hydraulic jumps inside a pipe, very long conduits with short pulses, and loops [S20](../sources/S20-li-edition-54-two-solvers.md). These figures come from the calculators in the [SWMM and ICM St. Venant comparison (app)](../entities/swmm-icm-st-venant-app.md), not from runs of the two engines.

**Geometry.** The two compute the area, hydraulic radius and top width of a partly full circular pipe by different approximations; the flow difference is typically under 1 % [S20](../sources/S20-li-edition-54-two-solvers.md).

**Not in the sources yet.** Most of Bob's SWMM5-and-ICM writing. Of the 216 queued LinkedIn articles, 139 name ICM or InfoWorks in the title, among them the 2023 "Top 100 Reasons" list.

See [InfoWorks ICM](../entities/infoworks-icm.md), [EPA SWMM 5](../entities/swmm-5.md), [Dynamic wave routing](dynamic-wave-routing.md), [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md).

---
title: SWMM 5 versus ICM InfoWorks
type: concept
updated: 2026-11-16
sources: [S13, S14, S17, S20, S80, S165, S166, S179, S184, S188]
tags: [comparison, swmm5, icm]
reviewed: 2026-11-15
changed_after_review: "2026-11-16 (S159 to S165 ingest): one paragraph added at the end, headed Added 16 November 2026, on the two-pipe benchmark design (S165); 2026-11-16 (S179 ingest): the drafter of the seven ICM notes named as ChatGPT (S179); 2026-11-16 (S180 to S187 ingest): one paragraph added at the end on the 2023 2D comparison (S184); 2026-11-16 (S188 to S190 ingest): one paragraph added at the end on the 2021 Water Talks webinar (S188)"
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

**Added 15 November 2026.** One app draws an "ICM rule" line beside SWMM 5 without running ICM: the steady profile that ICM's documented settings imply (a free outfall at the lesser of normal and critical depth, inertia phased out between a Lower Froude number of 0.8 and an Upper of 1.0, one water level per node). Its essay calls the line "a prediction waiting for a test in ICM", and no person has compared it with an ICM run [S80](../sources/S80-control-section-lab-summary.md). See [Control Section Lab (app)](../entities/control-section-lab.md). Like the comparison numbers questioned in Q16, it is not a run of ICM.

See [InfoWorks ICM](../entities/infoworks-icm.md), [EPA SWMM 5](../entities/swmm-5.md), [Dynamic wave routing](dynamic-wave-routing.md), [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md).

**Added 16 November 2026.** A test design to separate engine differences from conversion differences: one two-pipe model run first in EPA SWMM 5.2.4 and the Ruby translation, then in ICM SWMM, then in ICM InfoWorks, with the acceptable differences agreed before running [S165](../sources/S165-note-epa-swmm-ruby-icm-benchmark.md). It has not been run, and the note was drafted by ChatGPT [S179](../sources/S179-note-icm-notes-drafted-by-chatgpt.md) (Q16, Q90). See [Checking a SWMM5 model's conversion into ICM](swmm5-to-icm-conversion-checks.md).

**Added 16 November 2026, from the EXTRAN and QA ingest.** Bob's 2023 comparison on ICM's one 2D engine: an InfoWorks 1D and 2D network converted to ICM SWMM flooded more, which he put down to hydrology, SWMM hydrology in the ICM SWMM network against the Wallingford option in InfoWorks [S184](../sources/S184-li-unified-2d-engine-icm.md). The results are in screenshots, not numbers.

**Added 16 November 2026, from Bob's 2021 webinar.** Bob compared the two engines inside ICM in an Innovyze Water Talks webinar, from experience with about 100 models run both ways [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). Spoken claims, no run files here:
- Points per link: SWMM 5 computes one flow, at the link's midpoint; ICM at least five points, more on long links between a minimum and a maximum space step [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).
- Losses: SWMM 5 puts entrance, exit and other losses in the links and none at nodes; ICM computes a head loss at each node by one of six types (none, normal, high, fixed, user defined, FHWA), tied in its matrix solution to the depths in the links on either side. "Fixed" uses SWMM 5's values [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).
- ICM has three 1D solutions, conduit, pressure and force main; pressure and force main drop the unsteady and nonlinear terms [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).
- Time steps: ICM halves a step that does not converge and climbs back; SWMM 5 does not halve. See [Time stepping in ICM and SWMM 5](time-stepping-icm-and-swmm5.md) [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).
- Graphs: ICM shows the two ends of a link and SWMM 5 the midpoint, so a graphical comparison sets an end against a midpoint [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).
- For a fair comparison Bob advises SLOT in SWMM 5; see [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md) [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).
- He also says ICM contains SWMM 5 water quality and SWMM 5 LIDs (called SUDS in ICM) [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md), against the table row above that rests on [S20](../sources/S20-li-edition-54-two-solvers.md) (Q13).

---
title: Time stepping in ICM and SWMM 5
type: concept
updated: 2026-11-17
sources: [S188, S20, S265]
tags: [time-step, icm, swmm5, stability, comparison]
reviewed: no
---
How the two 1D engines choose their time step, as Bob and Nathan described them in a 2021 webinar [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). Everything on this page is spoken experience from that talk unless another source is cited; no run file from it is in this wiki.

**SWMM 5.** The user gives a routing step; the engine shortens it by the CFL condition and "never goes below" what the CFL condition gives. It does not halve a step that fails to converge [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). Each step is a Picard successive iteration, each node and link solved apart, normally four to eight iterations [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). In practice the step must suit the worst moment of the run: Nathan sees SWMM 5 models below one second [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).

**ICM.** The user gives a step, for example 60 s. ICM takes the CFL step, say 10 s; where nodes or links do not converge it halves to 5 s, then 2.5 s; once it converges easily it climbs back, 5, 10, then 60 s [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). Its scheme is the Preissmann four-point implicit scheme with an adaptive step [S20](../sources/S20-li-edition-54-two-solvers.md); Bob points to the ICM help, which says an implicit scheme can use a step much longer than the CFL step [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). The log reports the steps used, each halving and the node or link that did not converge; a diagnostics page turns on a time step log, RTC rule changes, mode switches and output state [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).

**XP SWMM** halves its step, as ICM does and SWMM 5 does not [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).

**One example: an inverted siphon, started dry** [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md)

| Engine | Step while the siphon filled | Step afterwards |
|---|---|---|
| ICM | 7.5 s | back to 60 s |
| SWMM 5 | about 1 s | 1 to 2 s for the whole run |

SWMM 5 was unstable at the start, with no continuity error, and ran better with SLOT than with EXTRAN; the flows "basically match", the velocities differ more. Bob gives this as one reason ICM runs faster: it returns to the long step [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).

**Starting state.** SWMM 5 starts dry unless given a hot start file, which Bob advises for force mains; ICM initializes every run to a steady state, "a super hot start" [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).

**Status.** These are statements from a webinar, not runs held here [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).

**Added 17 November 2026, fourth batch.** [Selective Fidelity (app)](../entities/selective-fidelity.md) patches 5.2.4 dynamic wave to solve only the conduits a question depends on: on a 24-conduit demo where one 18 ft conduit set the step in 99.99 % of 12,018 steps, it took 2,894 steps and kept the target node's peak at 1.537 ft [S265](../sources/S265-selective-fidelity-summary.md).

See [SWMM 5 versus ICM InfoWorks](swmm5-versus-icm-infoworks.md), [Dynamic wave routing](dynamic-wave-routing.md), [InfoWorks ICM](../entities/infoworks-icm.md), [EPA SWMM 5](../entities/swmm-5.md).

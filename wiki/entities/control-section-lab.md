---
title: Control Section Lab (app)
type: entity
updated: 2026-11-15
sources: [S80]
tags: [apps, hydraulics, open-channel, swmm5, swmm6, icm, findings]
reviewed: no
---
Bob's app on one question of open-channel hydraulics: which section of a channel sets the water surface, and which engines find it. Version 1.2, 18 October 2026 [S80](../sources/S80-control-section-lab-summary.md).

**A caution about its source.** The page ships no technical summary. [S80](../sources/S80-control-section-lab-summary.md) was written by Claude on 14 November 2026 from the page's source and build record, with nothing rerun, and Bob has not yet read it (Q52).

**The reach.** Eight rectangular open conduits, 2,650 ft long. All are 30 ft wide except a 14 ft throat. The bed slope is 0.001 except on a chute at 0.02. Defaults: 600 cfs, Manning n 0.022, FREE outfall. Four features compete for control: a sill, the throat, the chute crest and the outfall [S80](../sources/S80-control-section-lab-summary.md).

**What runs.** A reference solver (a steady mixed-flow profile with jumps placed by specific force, 1,333 sections), EPA SWMM 5.2.4, and OpenSWMM 6 as dynamic wave and as finite volume, all in the page. No ICM engine runs; a line drawn from ICM's documented defaults stands in for it [S80](../sources/S80-control-section-lab-summary.md).

**Nine recorded findings** [S80](../sources/S80-control-section-lab-summary.md)

| ID | Finding |
|---|---|
| F1 | With the tailwater in control on a prismatic reach, SWMM 5 and the reference agree to 0.0003 ft |
| F2 | SWMM 5 does not see the choke at the throat: 4.1179 ft upstream where the reference has 5.4682 ft |
| F3 | At the chute crest SWMM 5 carries normal depth, 1.6232 ft, not critical depth, 2.3160 ft |
| F4 | With NORMAL_FLOW_LIMITED NONE and the chute toe drowned, flow in the chute swings 1,574.8 cfs in a 600 cfs run |
| F5 | Shorter conduits do not converge on the reference |
| F6 | A damped-momentum profile reproduces both misses: 1.6233 ft at the crest, 4.2814 ft upstream |
| F7 | An entry loss K of 2.675 at 600 cfs stands in for the choke, but the K changes with flow: 2.247 at 300 cfs, 2.89 at 900 cfs |
| F8 | OpenSWMM 6 dynamic wave matches SWMM 5.2.4 at the nodes on three cases; on a fourth, where neither engine settles, they differ by up to 1.4249 ft |
| F9 | OpenSWMM 6 finite volume finds the choke (5.47 ft against 5.47) and holds the crest nearer critical depth (2.59 ft against 2.32) |

F6 is the explanation the page offers for F2 and F3: a profile integrated from the damped momentum equation lands on SWMM 5's depths, not the reference's. Inertial damping is described on [Dynamic wave routing](../concepts/dynamic-wave-routing.md). F8 and F9 are on [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).

**The ICM line.** Drawn from documented rules: a free outfall at the lesser of normal and critical depth, inertia phased out between a Lower Froude number of 0.8 and an Upper of 1.0, one water level per node. The essay calls it "a prediction waiting for a test in ICM" [S80](../sources/S80-control-section-lab-summary.md). See [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).

**Checks.** Three suites run against the shipped file: 29 physics checks, 33 SWMM 5 engine checks, 24 SWMM6 engine checks. A button reruns every case in the browser, about 70 engine runs [S80](../sources/S80-control-section-lab-summary.md).

**What it does not show.** Unsteady flow; contraction and expansion losses; the real length of a jump; ICM's own discretization; any OpenSWMM 6 build but the one pinned. The essay's caution on F9: "that is one channel and one pre-release commit" [S80](../sources/S80-control-section-lab-summary.md).

**Credit.** The idea comes from the Control Section Lab at Vasslab, which this app rebuilds around a SWMM-style channel [S80](../sources/S80-control-section-lab-summary.md).

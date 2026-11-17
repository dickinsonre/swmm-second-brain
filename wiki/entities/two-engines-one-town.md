---
title: Two Engines, One Town (app)
type: entity
updated: 2026-11-17
sources: [S198]
tags: [apps, swmm5, epanet, coupling]
reviewed: no
---
Bob's app of working code for driving [EPA SWMM 5](swmm-5.md) 5.2.4 and [EPANET](epanet.md) 2.3 from Python and JavaScript, with a Coupling Lab that sends a town's delivered water into a sewer. Built 2 November 2026, with no version number of its own [S198](../sources/S198-two-engines-one-town-summary.md).

**A caution about its source.** The page ships no technical summary. [S198](../sources/S198-two-engines-one-town-summary.md) was written by Claude on 16 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q99).

**Why it exists.** It replaces an earlier answer, none of whose code ran; the page says every snippet in it was run and every number measured [S198](../sources/S198-two-engines-one-town-summary.md).

**The Coupling Lab** [S198](../sources/S198-two-engines-one-town-summary.md)
- The town is EPANET's Net1. The sewer under it is invented: nine manholes and nine pipes of 12 to 24 in at 0.2 percent.
- Each manhole receives a fraction R of the water delivered at the junction above it. Demand is fixed or pressure-dependent.
- With R = 0.85, the plant peaks at 1,455.9 GPM at 8:00. Over day 3 the water sent and the water received both average 935.0 GPM, 0.0004 percent apart.
- Running the engines in sequence or in lock-step every 60 seconds differs by at most 0.057 GPM.
- At four times normal demand with fixed demand, the lowest pressure is -861 psi; with pressure-dependent demand at three times, the town receives 78 % of what it asks.

**The checks** [S198](../sources/S198-two-engines-one-town-summary.md)
- Six routes to EPANET agree on 225 pressures to within 9.6e-05 psi of owa-epanet. The page puts the spread down to float32 storage.
- The same check caught the page's own first WNTR snippet using the wrong pressure conversion, off by up to 0.07 psi.

**What it does not show.** One teaching network and one invented sewer. No rain, infiltration or lateral travel time. The coupling runs one way. OpenSWMM 6 was tried only as a drop-in engine [S198](../sources/S198-two-engines-one-town-summary.md).

**Related.** [ForceMain SWMM5 EPANET Comparison (app)](forcemain-swmm5-epanet-comparison.md), [EPANET for SWMM5 Experts (app)](epanet-for-swmm5-experts.md).

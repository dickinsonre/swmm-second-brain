---
title: People as Pollutants (app)
type: entity
updated: 2026-11-15
sources: [S76, S83]
tags: [apps, swmm5, water-quality, pumps, storage, findings]
reviewed: 2026-11-15
---
Bob's app that writes a three-level transit station as an EPA SWMM 5.2.4 input file and runs it with the unmodified engine, reading the water as a crowd. Version 1.0.0, 29 October 2026. The question is Bob's: could SWMM 5 show that station if the water quality were people? [S83](../sources/S83-people-as-pollutants-summary.md)

**A caution about its source.** The page ships no technical summary. [S83](../sources/S83-people-as-pollutants-summary.md) was written by Claude on 14 November 2026 from the page's source and embedded records, with nothing rerun, and Bob has not yet read it (Q52).

**The mapping** [S83](../sources/S83-people-as-pollutants-summary.md)

| Station | SWMM object |
|---|---|
| One person | One cubic foot of water; 1 cfs is one person per second |
| A floor zone | A storage unit, with area equal to the floor area divided by 100 |
| A walkway, stair, escalator, gate, lift or train door | A TYPE4 pump, whose flow depends on the depth at its inlet |
| Arrivals from the street | Rain on three fully impervious subcatchments |
| Trains | Outfalls, with doors opened and closed by control rules |
| Kinds of traveler, and where they came from | Pollutants |
| Waiting | A pollutant, PATIENCE, that decays at 1 per 600 seconds |

The station has twelve floor zones and twenty-two pumps. Each pump curve is the rising half of a pedestrian fundamental diagram [S83](../sources/S83-people-as-pollutants-summary.md).

**The stored baseline.** A two-hour morning peak: 23,241.8 people walk in, 4,200 and 7,000 get off 70 trains, none are lost to flooding, and the people census closes to 2.86 people (0.008 percent). The pinch is a 16-foot entrance stair at the critical density [S83](../sources/S83-people-as-pollutants-summary.md).

**Two SWMM defaults it ran into** [S83](../sources/S83-people-as-pollutants-summary.md)

| ID | Where | What happens | What the app does |
|---|---|---|---|
| D-1 | `qualrout.c` line 41, `ZeroDepth = 0.003281` (1 mm in ft) | A node shallower than 1 mm with no inflow has its concentrations set to zero. With depth read as density one to one, one tracer's quality continuity error was -30.395 percent | Scales depth by 100 |
| D-2 | `dynwave.c`, `setNodeDepth()`, `surfArea = MAX(surfArea, MinSurfArea)` | A storage unit smaller than MIN_SURFAREA (default 12.566 ft²) changes depth as if it had that area, while its volume comes from its own curve. The census missed by 0.573 percent | Sets MIN_SURFAREA 0.01 |

The page calls them "two SWMM defaults" that leak into a crowd model, and does not call them errors in SWMM for water [S83](../sources/S83-people-as-pollutants-summary.md). The same default area, given as 12.57 ft², is what [Inside the Network (app)](inside-the-network-cfd.md) compares its chambers with [S76](../sources/S76-inside-the-network-cfd-app-md.md). Minimum surface area is one of the stability options on [Dynamic wave routing](../concepts/dynamic-wave-routing.md).

**Checks.** The census, SWMM's own continuity tables, and a test that the five traveler types sum to 100 percent at every node holding at least 5 people (within 0.767 percent across 13,289 node-periods). A null-effect run and a determinism run are offered in the page; their results are not stored [S83](../sources/S83-people-as-pollutants-summary.md).

**What it does not show.** Water has no destination: at a fork every pollutant splits in the flow ratio, so no traveler chooses a route. Storage units are mixed tanks, not queues. No field data; the geometry is drawn, not surveyed [S83](../sources/S83-people-as-pollutants-summary.md).

**Credit.** Prompted by Gavin Nicholls' LinkedIn post about Throng, his pedestrian simulator. The page says it is not affiliated with Throng and uses none of its code or data. Its speeds come from Weidmann (1993) and Fruin (1971) [S83](../sources/S83-people-as-pollutants-summary.md).

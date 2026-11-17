---
title: InfoSewer_2009 (app)
type: entity
updated: 2026-11-17
sources: [S201]
tags: [apps, infosewer, 3d, pumps]
reviewed: no
---
Bob's 3D viewer of one 2009 InfoSewer sewer model, colored with steady-state and 24-hour extended-period results from [swmm5-infosewer](swmm5-infosewer.md). Version 1.2.0, 12 November 2026. The page runs no engine; the results are packed into it [S201](../sources/S201-infosewer-2009-app-md.md).

**Kept private by design.** The model is a real utility's network, and the summary asks that the app stay private unless the utility agrees. Version 1.2.0 renamed the app and removed the utility's name and the map offsets, so positions are relative to the network's center [S201](../sources/S201-infosewer-2009-app-md.md). This wiki names neither.

**The network** [S201](../sources/S201-infosewer-2009-app-md.md)
- 2,250 gravity pipes (125.5 mi) and 5 force mains (5.85 mi), 131.3 mi in all.
- 2,231 loading manholes, 5 wet wells, 3 outfalls, 9 pumps in 5 stations.
- Diameters 7.0 to 60 in; 492 ft of fall.

**What the results show** [S201](../sources/S201-infosewer-2009-app-md.md)
- Steady state: 33 of 2,250 gravity pipes surcharged; 11,987 gpm to the outfalls.
- Over the 24 hours, 12 to 44 pipes surcharged at the 25 report times. The largest outfall peaks at 10,850 gpm at hour 18, against 7,970 in steady state.
- The largest station lifts 10,960 gpm against 283.63 ft of head through a 30 in force main 20,249 ft long.
- InfoSewer's own mass balance leaves 339,295 ft3 unaccounted, printed as 14.6 percent of the inflow (Q101).

**What it does not show.** Hourly snapshots only. Exaggerated elevations and pipe sizes. No terrain or basemap. The 2009 model has not been compared with the system as it is today. One pipe in the source data has inverts of 0.00 ft, and the engine used them as given [S201](../sources/S201-infosewer-2009-app-md.md).

**Related.** [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md).

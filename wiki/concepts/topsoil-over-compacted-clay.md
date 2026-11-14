---
title: Topsoil over compacted clay
type: concept
updated: 2026-11-14
sources: [S08, S23]
tags: [hydrology, infiltration, lid, swmm5]
reviewed: no
---
**The question.** How much of a storm does 4 in of decompacted, amended topsoil over 24 in of compacted sandy clay capture in SWMM, in the dormant and the growing season, and how much does the answer depend on which SWMM setup describes the soil? It is studied on the [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md) [S23](../sources/S23-topsoil-recovery-check-app-md.md), which compares Horton with the LID two-layer soil in EPA SWMM 5.2.4 [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

**The soils** (assumptions, not measurements) [S23](../sources/S23-topsoil-recovery-check-app-md.md)

| Layer | Thick (in) | Porosity | FC | WP | Ksat (in/hr) |
|---|---|---|---|---|---|
| Decompacted, amended topsoil | 4 | 0.50 | 0.30 | 0.15 | 1.0 |
| Compacted sandy clay | 24 | 0.430 | 0.321 | 0.221 | 0.01 |

**The setups disagree.** Capture of storms of 0.75 in and larger over synthetic seasons, dormant / growing [S23](../sources/S23-topsoil-recovery-check-app-md.md):

| Setup | Dormant | Growing |
|---|---|---|
| Modified Horton | 76.6 % | 77.9 % |
| Modified Horton, impermeable clay | 70.8 % | 72.7 % |
| LID, clay as the storage layer | 100.0 % | 100.0 % |
| LID, no storage layer, seepage = clay Ksat | 79.3 % | 95.0 % |
| [swmm524-perched](../entities/swmm524-perched.md) | 83.0 % | 97.1 % |
| swmm524-perched with van Genuchten | 67.1 % | 96.9 % |
| Clay 5 times tighter, perched / perched with VG | 53.7 / 44.4 % | 95.2 / 94.5 % |

Modified Horton recovers on a drying-time clock, `Fe <- Fe exp(-kr dt)` with `kr = -ln(0.02)/DryTime` [S23](../sources/S23-topsoil-recovery-check-app-md.md); its two seasons in the table differ by 1.3 points (our arithmetic). The storage-layer and no-storage setups are on [LID bio-retention layers](lid-bioretention-layers.md).

**What moves the van Genuchten result.** Restoring one perched rule at a time, dormant capture: full VG 67.1 %; field-capacity floors or direct SOIL2 ET, 0.1 point or less; no upward flow 71.1 %; field-capacity head 68.3 %; the outline's step rule 59.4 %; all five perched rules 72.3 % [S23](../sources/S23-topsoil-recovery-check-app-md.md).

**Ideas from the SWMM-USERS list** (Experiment H) [S23](../sources/S23-topsoil-recovery-check-app-md.md)
- Depression storage as the topsoil bowl (Horton, f0 = fmin = 0.01 in/hr): dormant capture 27.6 % at 0.2 in, 75.2 % at 0.8 in, 95.5 % at 1.4 in. It equals the perched engine's 83.0 % at 0.99 in and the VG option's 67.1 % at 0.68 in.
- A 3 in/hr infiltration test on the two-layer profile falls below 0.1 in/hr after 20 to 82 minutes, depending on setup and starting moisture; mean rate in hours 4 to 6 is 0.010 in/hr in the stock LID setup and 0.035 to 0.048 in/hr in the perched engine.
- Evaporation off during rain: see [Evaporation during rain (DRY_ONLY)](evaporation-during-rain.md).
- A curb-cut drain: defect D2 on [LID bio-retention layers](lid-bioretention-layers.md).
- Bulk density: the clay's porosity 0.43 implies 1.51 g/cc (94 lb/ft³) at a particle density of 2.65; compacted urban soils near 1.9 g/cc would be tighter.

**Limits the source states.** No calibration to a site, one soil pair, synthetic storms with rain in 3.5 % of hours, and no matched HYDRUS comparison yet [S23](../sources/S23-topsoil-recovery-check-app-md.md).

See also [Infiltration methods](infiltration-methods.md).

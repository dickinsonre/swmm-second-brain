---
title: LID bio-retention layers
type: concept
updated: 2026-11-14
sources: [S10, S20, S21, S23]
tags: [hydrology, lid, swmm5, swmm6]
reviewed: no
---
SWMM 5 added LID controls in 5.0.019 (2010) [S21](../sources/S21-li-edition-56-swmm-history.md). "LID" is the fourth most common subject in Bob's forum thread titles, 216 threads [S10](../sources/S10-openswmm-top25-problems.md). The source that calls SWMM 5 "the only platform with built in LID and water quality modeling" is [S20](../sources/S20-li-edition-54-two-solvers.md) (see Q13 in [Open questions](../open-questions.md)).

What follows is what one study learned about the bio-retention cell when its layers are asked to hold a soil over a compacted clay ([Topsoil over compacted clay](topsoil-over-compacted-clay.md)) [S23](../sources/S23-topsoil-recovery-check-app-md.md).

**The clay as the storage layer.** With the clay as the 24 in storage layer, void ratio from total porosity (0.43) or drainable porosity (0.109) and seepage 0.01 in/hr, the cell captures 100.0 % of the big storms in both seasons [S23](../sources/S23-topsoil-recovery-check-app-md.md).

**No storage layer.** With no storage layer and the seepage set to the clay's Ksat, 0.01 in/hr, the clay throttles topsoil drainage: 79.3 % dormant, 95.0 % growing [S23](../sources/S23-topsoil-recovery-check-app-md.md).

**Soil evaporation stops while water infiltrates.** `lidproc.c getEvapRates()` sets SoilEvap to 0 whenever SurfaceInfil > 0; OpenSWMM 6 keeps the rule at `LID.cpp` line 907 [S23](../sources/S23-topsoil-recovery-check-app-md.md). See [Evaporation during rain (DRY_ONLY)](evaporation-during-rain.md).

**Defect D2: a drain with no storage layer makes water.** In `lidproc.c biocellFluxRates()`, StorageDrain is computed, the `storageThickness == 0.0` branch never limits it, and `f[STOR] = 0.0` never removes it. Winter season, drain coefficient 0.1: 232.85 in of drain flow from 20.55 in of rain, runoff continuity error -1,100.9 %. Same in EPA 5.2.4, OpenSWMM 5.3.0-beta.3 and 6.0.0-alpha.4. The made-up flow is proportional to the coefficient: 2.3 in at 0.001. Not fixed in any engine on the page [S23](../sources/S23-topsoil-recovery-check-app-md.md). The source numbers it D2, not with a register ID (Q20 in [Open questions](../open-questions.md)).

**The perched engine ignores drains.** [swmm524-perched](../entities/swmm524-perched.md) sets `StorageDrain = 0.0` in its flux routine, so a DRAIN line has no effect there [S23](../sources/S23-topsoil-recovery-check-app-md.md).

**An unknown layer keyword.** OpenSWMM 6.0.0-alpha.4 ignores an unknown LID layer keyword (SOIL2) instead of reporting it; an issue was drafted with a tested patch [S23](../sources/S23-topsoil-recovery-check-app-md.md).

See also [Continuity is not validation](continuity-is-not-validation.md), [Infiltration methods](infiltration-methods.md).

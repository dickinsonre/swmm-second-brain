---
title: Evaporation during rain (DRY_ONLY)
type: concept
updated: 2026-11-17
sources: [S59, S255]
tags: [hydrology, evaporation, lid, swmm5, swmm6]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S243 to S255 ingest): a paragraph added near the end, headed Added 17 November 2026 (S255)"
---
**The question.** Whether evaporation should stop while it rains is one of the ideas from the SWMM-USERS list that [S59](../sources/S59-topsoil-recovery-check-app-md.md) tested (its Experiment H). SWMM's switch is `DRY_ONLY` in `[EVAPORATION]`; the study's default is `DRY_ONLY NO` [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**The test.** Setups from [Topsoil over compacted clay](topsoil-over-compacted-clay.md), run with `DRY_ONLY NO`, with `DRY_ONLY YES`, and with `DRY_ONLY YES` plus a scaled-up dry-hour PET. Rain falls in 3.5 % of the hours of the synthetic seasons [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**Results** [S59](../sources/S59-topsoil-recovery-check-app-md.md)
- Big-storm capture changes by at most 1.3 points (Standard Horton with MaxInfil, growing season, 72.7 to 71.4 %), and by at most 0.4 in the LID and perched setups.
- Horton summer evaporation falls 24 to 40 %, and the scaled-up dry-hour PET does not restore it: Modified Horton 0.49 in by default, 0.29 in with DRY_ONLY, 0.30 in scaled.

**Why so small.** In an LID the soil was already dry-only: `lidproc.c getEvapRates()` sets SoilEvap to 0 whenever SurfaceInfil > 0, and OpenSWMM 6 keeps the rule (`LID.cpp` line 907) [S59](../sources/S59-topsoil-recovery-check-app-md.md). See [LID bio-retention layers](lid-bioretention-layers.md).

**Not in the sources.** The wiki has no source yet on the share of wet hours in real rain records, and none of the list replies themselves; they would come in with the OpenSWMM full-text export.

**Added 17 November 2026, third batch.** [IFS Analysis Explorer (app)](../entities/ifs-analysis-explorer.md) builds SWMM5 climate files from ECMWF's 6-hourly analysis: from 6-hourly values Tmax averages -3.5 F and Tmin +0.9 F off the true extremes, and a year's Hargreaves PET comes out at 84 % of the true value (30.5 against 36.1 in) [S255](../sources/S255-ifs-analysis-explorer-summary.md).

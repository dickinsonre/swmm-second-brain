---
title: Infiltration methods
type: concept
updated: 2026-11-14
sources: [S01, S03, S08, S10, S15, S55, S59]
tags: [hydrology, swmm5, infiltration]
reviewed: no
---
SWMM5's infiltration methods, as named in its code [S15](../sources/S15-li-hydrology-code-story.md):

| Method | Entry point | State the source names |
|---|---|---|
| Curve Number | `curvenum_getInfil` | capacity `S`, inter-event time `Tmax`, cumulative precipitation `P`, cumulative infiltration `F`, effective saturation `Se` |
| Horton | `horton_getInfil` | maximum rate `f0`, minimum rate `fmin`, regeneration `kr`, `Fmax`, time on the curve `tp` |
| Modified Horton | `modHorton_getInfil` | the same, with different handling of saturated and drying soil |
| Green-Ampt | `grnampt_getInfil` | splits into `grnampt_getUnsatInfil` and `grnampt_getSatInfil` |

The table is from [S15](../sources/S15-li-hydrology-code-story.md), an AI-written passage that was not checked against the code.

**History.** The 1971 Runoff Block used Horton infiltration on each of three planes [S01](../sources/S01-swmm1-engine-app-md.md).

**Converting to the 1971 form.** The [SWMM 1 Engine (app)](../entities/swmm-1-engine-app.md) imports SWMM 5 files. For a Green-Ampt subcatchment it sets Horton's minimum rate to the conductivity and the maximum rate to three times the conductivity, which its summary calls a rule of thumb [S01](../sources/S01-swmm1-engine-app-md.md).

**Findings and apps**
- `MODIFIED_HORTON` and MaxInfil behavior is a register candidate with status confirmed; no detail is given [S03](../sources/S03-findings-register-format.md). [S59](../sources/S59-topsoil-recovery-check-app-md.md) gives the detail as its defect D1: in EPA 5.2.4, `infil.c` line 545 uses MAX where MIN is meant (`infil->Fe = MAX(infil->Fe, infil->Fmax)`), and 4.0 in of rain infiltrates 0.002 in. On an 8 in storm with a 3 in cap the capped Modified Horton infiltrates 0.001 in, and 3.00 in with OpenSWMM 5.3.0's fix ported to 5.2.4 [S59](../sources/S59-topsoil-recovery-check-app-md.md).
- All of these treat the soil as one uniform layer. Bob's [two-layer proposal](two-layer-infiltration.md) adds a second layer through the LID soil machinery [S55](../sources/S55-swmm-brain-readme.md). ([S55](../sources/S55-swmm-brain-readme.md) counts three built-in methods, leaving out Modified Horton.)
- Bob's fork of EPA SWMM has a branch with six Curve Number changes [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).
- [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md) compares Horton with the LID two-layer soil for decompacted topsoil in EPA SWMM 5.2.4, and The Bowl Is Full expresses compaction as an apparent Curve Number [S08](../sources/S08-swmm5org-topic-inside-swmm5.md). Its results are on [Topsoil over compacted clay](topsoil-over-compacted-clay.md) [S59](../sources/S59-topsoil-recovery-check-app-md.md).
- Modified Horton recovers on a drying-time clock, `Fe <- Fe exp(-kr dt)` with `kr = -ln(0.02)/DryTime` [S59](../sources/S59-topsoil-recovery-check-app-md.md).
- [swmm524-perched](../entities/swmm524-perched.md) adds a second soil layer to the LID with a Green-Ampt cap on flow into it [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**How often it is asked.** "Infiltration methods" tags 146 of Bob's 2,879 OpenSWMM thread titles [S10](../sources/S10-openswmm-top25-problems.md).

---
title: Infiltration methods
type: concept
updated: 2026-11-16
sources: [S01, S03, S08, S10, S15, S55, S59, S67, S107, S108, S177, S178]
tags: [hydrology, swmm5, infiltration]
reviewed: 11/16/2026
changed_after_review: "2026-11-16 (S166 to S178 ingest): one paragraph added at the end, headed Added 16 November 2026, on the Curve Number on the ICM 2D mesh (S177, S178)"
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
- Green-Ampt: a candidate finding in `grnampt_getF2`, `infil.c` lines 847 to 856. The Newton correction is tested before it is applied, and one clay test lost 21 % of its infiltration at a 15 s wet step and nothing at 5, 30, 60 or 300 s. Status in the note: working, not rerun [S67](../sources/S67-note-green-ampt-newton-test-order.md). See [Green-Ampt Newton test order](green-ampt-newton-test-order.md).
- All of these treat the soil as one uniform layer. Bob's [two-layer proposal](two-layer-infiltration.md) adds a second layer through the LID soil machinery [S55](../sources/S55-swmm-brain-readme.md). ([S55](../sources/S55-swmm-brain-readme.md) counts three built-in methods, leaving out Modified Horton.)
- Bob's fork of EPA SWMM has a branch with six Curve Number changes [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).
- [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md) compares Horton with the LID two-layer soil for decompacted topsoil in EPA SWMM 5.2.4, and The Bowl Is Full expresses compaction as an apparent Curve Number [S08](../sources/S08-swmm5org-topic-inside-swmm5.md). Its results are on [Topsoil over compacted clay](topsoil-over-compacted-clay.md) [S59](../sources/S59-topsoil-recovery-check-app-md.md).
- Modified Horton recovers on a drying-time clock, `Fe <- Fe exp(-kr dt)` with `kr = -ln(0.02)/DryTime` [S59](../sources/S59-topsoil-recovery-check-app-md.md).
- [swmm524-perched](../entities/swmm524-perched.md) adds a second soil layer to the LID with a Green-Ampt cap on flow into it [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**How often it is asked.** "Infiltration methods" tags 146 of Bob's 2,879 OpenSWMM thread titles [S10](../sources/S10-openswmm-top25-problems.md).

**Added 15 November 2026: two calculators outside the engine.** Two of Bob's Replit apps compute these methods in their own TypeScript and call no SWMM engine: [Green-Ampt Infiltration Calculator (app)](../entities/green-ampt-infiltration-calculator.md) [S107](../sources/S107-green-ampt-calculator-replit-summary.md) and [SWMM5 Runoff and Infiltration (app)](../entities/swmm5-runoff-and-infiltration.md) [S108](../sources/S108-runoff-and-infiltration-replit-summary.md). Both use `S = 1000 / CN - 10` for the Curve Number storage. Replit Agent, reading the first app's code, reported that its unit selector does not convert the Green-Ampt and Horton inputs and that its Curve Number branch does not accumulate rainfall; neither was tested (Q69).

**Added 16 November 2026: Curve Number on the ICM 2D mesh.** In 2023 an ICM 2D infiltration surface offered only Horton, Green-Ampt, Constant and Fixed, so Bob approximated the Curve Number with them: with a constant loss rate set from the CN peak, Horton, Green-Ampt and ConstInf came close to CN in peak and volume [S177](../sources/S177-li-curve-number-approximations-icm-2d.md). ICM 2025.1 added CNSWMM to the 2D mesh, with an initial abstraction factor, curve number and drying time [S178](../sources/S178-li-cnswmm-on-the-icm-2d-mesh.md). See [ICM 2D: rainfall and infiltration on the mesh](icm-2d-rainfall-and-infiltration.md).

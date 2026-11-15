---
title: "EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE"
type: concept
updated: 2026-11-15
sources: [S60, S74, S75]
tags: [hydraulics, extran, swmm4, swmm5, swmm6, dynamic-wave]
reviewed: 2026-11-15
---
SWMM 4.4H's Extran block carries three solvers for the St. Venant equations, chosen by the input value ISOL: XROUTE (ISOL 0), YROUTE (ISOL 1) and ZROUTE (ISOL 2). SWMM 5.2.4 has one dynamic-wave solver and OpenSWMM 6 has two [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). The [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md) reads all six side by side and runs them. This page is the Fortran half; the SWMM6 half is on [OpenSWMM 6 solvers, measured](openswmm6-solvers-measured.md).

**How they differ** [S75](../sources/S75-st-venant-rosetta-stone-app-md.md)

| | XROUTE | YROUTE | ZROUTE |
|---|---|---|---|
| Stepping | A half step and a full step | The same | A Courant-limited sub-step, halved at most twice on failure |
| Iteration | Surcharged junctions only | Surcharged junctions only | All links and nodes, relaxation 0.75 on the first pass and 0.50 after |
| Inertial terms | Added to the numerator | Moved into the denominator | Time-weighted 0.6 new and 0.4 old; local inertia V dA where EXTRAN has 2 V dA |
| Surcharge | EXTRAN's head adjustment at a junction above its crown | The same | One node equation with a Preissmann slot |

The half step and full step are the modified Euler method of the 1981 program [S74](../sources/S74-extran3-workbench-app-md.md), [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**What SWMM 5 kept.** XROUTE's momentum terms. SWMM 5.2.4's update at `dwflow.c:213-240` has `dq3 = 2 v (aMid - aOld) sigma` and `dq4 = dt v^2 (a2 - a1)/L sigma`, the two inertial terms of XROUTE.FOR:332-338. Its EXTRAN surcharge method is "the same rule" as XROUTE's, at `dynwave.c:720-734`. SWMM 5 iterates all links and nodes up to 8 trials with a relaxation of 0.5. OpenSWMM 6's dynamic wave is "the SWMM5 line with conveyance areas" [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**On one network.** Example 1 of the EXTRAN manual, 20-second step, 1,458,000 ft³ of inflow [S75](../sources/S75-st-venant-rosetta-stone-app-md.md):

| Solver | Lost to flooding, ft³ | Continuity, % |
|---|---|---|
| XROUTE | 114,714 | 0.06 |
| YROUTE | 114,644 | 0.06 |
| SWMM 5.2.4, EXTRAN | 114,824 | 0.011 |
| ZROUTE as distributed | 0 | -1.05 |
| ZROUTE, slot freed | 84,349 | -0.31 |
| SWMM 5.2.4, SLOT | 78,582 | -0.186 |

The three with the EXTRAN surcharge rule agree within 180 ft³ (our subtraction). Why ZROUTE reports no flooding at all is on [The crown cap at mid-pipe](crown-cap-at-mid-pipe.md).

**Time step.** XROUTE fails at a 120-second step (continuity prints asterisks, peak 2,720 cfs); YROUTE gives -8.01 %. With the EXTRAN surcharge rule, the maximum head at one junction grows as the step shrinks: 133.84 ft at 20 s and 155.00 ft, the ground, at 5 s in XROUTE; 134.62 and 153.61 ft in SWMM 5.2.4. The slot and finite-volume solutions show no such spike [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**Faults found, by solver** [S75](../sources/S75-st-venant-rosetta-stone-app-md.md)
- YROUTE: line 215 lacks a 0.5 that line 219 and XROUTE have (measured); its denominator 1 + AKON goes negative when a dry pipe wets (measured).
- XROUTE and YROUTE: junction surface area accumulates over surcharge iterations, 367,400 ft² where one pass gives 13,800 (measured; flooding unchanged).
- ZROUTE: work arrays with no SAVE; a relaxed head returned on convergence; a failed sub-step restored to the wrong state; unconverged steps accepted and left out of the printed count; three steep-drop decks it fails in every form.

Thirty items in all, each marked measured or read. The file says they are "the AI's reading of the code at the lines cited" and that no person has checked them [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**Across 50 example decks.** Median absolute continuity error: XROUTE 0.50 %, YROUTE 0.54 %, ZROUTE as distributed 1.42 %, ZROUTE with eleven kept changes 0.38 %. YROUTE's mean is 11.11 % because of one deck at 452.48 %, not investigated [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**Limits.** No measured flood volume says which solver is right. The lineage "is inferred from code and comments", not documented. SWMM 5.2.4 and SWMM6 were run on Example 1 and a single pipe only [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

See [EXTRAN](../entities/extran.md), [Dynamic wave routing](dynamic-wave-routing.md), [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md).

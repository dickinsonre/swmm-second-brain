---
name: St. Venant Solver Rosetta Stone
file: st-venant-solver-rosetta-stone.html
version: 2.4.0
date: 2026-11-13
author: Robert E. Dickinson
links: {netlify: none yet, artifact: private Claude artifact, repo: none}
engines:
  - {name: SWMM 4.4H Extran block (XROUTE, YROUTE, ZROUTE), source: github.com/SWMMEnablement/WCH_2004_SWMM44H, commit: 9dd9f6c, compiler: gfortran 13.3.0 via build_swmm44h.sh, license: public domain}
  - {name: SWMM 4.4H build copies (45 experiments; listed in build_copies.csv in the reproduction bundle), source: same with one change each or a named combination; see How to reproduce, license: public domain}
  - {name: EPA SWMM 5.2.4 build copy (one experiment switch in dwflow.c), source: commit 07c371f, license: public domain}
  - {name: EPA SWMM, version: 5.2.4, source: github.com/USEPA/Stormwater-Management-Model, commit: 07c371f, compiler: gcc Release with _FORTIFY_SOURCE=0, license: public domain}
  - {name: OpenSWMM, version: 6.0.0-alpha.4 (legacy engine reports 5.3.0), source: github.com/HydroCouple/openswmm.engine, branch: swmm6_rel, commit: 0071c5f, compiler: "gcc Release, GeoPackage, HDF5, 2D and GPU plugin off, _FORTIFY_SOURCE=0", license: Apache-2.0}
units: US customary (cfs, ft, ft3, seconds)
complexity: {meter: SWMM App Complexity Meter v1.9.1, baseline: HC-2026-11-10-h, index: 51.5, scale: HydroCouple = 100}
ai_use: built with Claude (Anthropic); see AI use
---

# St. Venant Solver Rosetta Stone: six dynamic-wave solvers from SWMM4, SWMM5 and SWMM6, with engine runs

In one sentence: In 1,157 engine runs, SWMM5 and SWMM6 still carry XROUTE's momentum terms, ZROUTE's missing flooding traces to one cap on pipe depth, and eleven changes cut its median continuity error from 1.42 to 0.38 percent on 50 non-steep decks.

In one paragraph: SWMM 4.4H carries three solvers for the St. Venant equations, SWMM 5.2.4 one and OpenSWMM 6 two. This app sets their source lines side by side and runs all six on Example 1 of the EXTRAN manual. Three solutions with the EXTRAN surcharge rule lose about 114,700 cubic feet to flooding. Four with a working slot lose 78,582 to 90,866. Build copies changed one line at a time trace ZROUTE's difference to how a pipe surcharged at one end is described at mid-length. A line-by-line pass found nine more faults around ZROUTE. Eleven changes cut its median continuity error on 50 non-steep example decks from 1.42 to 0.38 percent; three steep decks defeat it. The evidence is 1,157 runs. It is not a validation of any engine.

## What it does

It answers four questions. How do XROUTE (ISOL 0), YROUTE (ISOL 1) and ZROUTE (ISOL 2) differ, and what did SWMM5 keep? What do the two OpenSWMM 6 solvers, the expanded dynamic wave solver and the finite volume solver, do on the same network? Are there more bugs in YROUTE and ZROUTE? Why is ZROUTE different, and what else is wrong with it? It shows the momentum and surcharge lines of each solver with file and line numbers, the results of 1,157 engine runs, and a register of thirty findings marked measured or read. Nothing is simulated in the browser except a one-pipe calculator of the momentum equation.

## How it computes

Full-step momentum update for one conduit. F = friction factor, P = pressure term, dA = area change over the step, Aup and Adn = end areas.

| Solver | Flow update | Source |
|---|---|---|
| XROUTE | Q = (Qold - P + 2 V dA + dt V^2 (Adn - Aup)/L) / (1 + F + losses) | XROUTE.FOR:332-338 |
| YROUTE | Q = (Qold - P) / (1 + F + losses - 2 dA/A - dt Q (Adn - Aup)/(AT A L)) | YROUTE.FOR:342-348 |
| ZROUTE | Q = (Qold - 0.6 P - 0.4 (P + F Q + c Q)old + Vbar dA) / (1 + 0.6 (F + c + losses)), c = dt Q (1/Adn - 1/Aup)/L | ZROUTE.FOR:110-128 |
| SWMM 5.2.4 | q = (qOld - dq2 + dq3 + dq4 + dq6) / (1 + dq1 + dq5), dq3 = 2 v (aMid - aOld) sigma, dq4 = dt v^2 (a2 - a1)/L sigma | dwflow.c:213-240 |
| SWMM6 dynamic wave | the SWMM5 line with conveyance areas (slot area removed): dq3 = 2 v (aMidConv - aOld) sig, dq4 = dt v^2 (a2Conv - a1Conv)/L sig, denom = 1 + dq1 + dq5 | DynamicWave.cpp:3139-3265 |
| SWMM6 finite volume | no per-conduit flow update. Cell flux F = (Q, Q u + g I1); HLL face flux for the two hydraulic equations (the RIEMANN option HLLC, the default, changes only the upwinding of transported scalars; FvKernels.hpp:373-377, 447; FvOptions.hpp:57, 175); friction q/(1 + dt k abs(u)/R^(4/3)) | fv/FvKernels.hpp:339-342, 416-417, 485-491 |

Surcharge at a junction above its crown:

- XROUTE, YROUTE: Y = YT + CORR * SUMQS / DENOM, DENOM = SUMAL + (ASFULL/DELT - SUMAL) exp(-15 (YT - YCROWN)/YCROWN), CORR = 1.00 or 0.60 at a dead end. XROUTE.FOR:509-514. DQDH = g DELT AT / LEN / (1 + AKON), XROUTE.FOR:409.
- SWMM 5.2.4, SURCHARGE_METHOD EXTRAN: the same rule. dynwave.c:720-734, dwflow.c:243.
- ZROUTE: one node equation, Y = YO + SUMQ DELT / ((AS + AOLD)/2), ZROUTE.FOR:275-276, with a Preissmann slot. ISOL 2 sets JSLOT = 1 (INDAT1.FOR:383). Slot width in HYDRAD.FOR:246-258: WIDTH = ALF + (SLOT - ALF)/0.0625 (FDEPTH - 1)^2 below 1.25 depths, SLOT = 0.005 DEEP above; ALF = TWNORM(26,NTYPE) WIDE, which is 0.3919 WIDE for a circular pipe.
- SWMM 5.2.4, SURCHARGE_METHOD SLOT: width = 0.5423 wMax exp(-(y/yFull)^2.4), 0.01 wMax above 1.78. dwflow.c:584-587. Slot area conveys flow (dwflow.c:617).
- SWMM6 dynamic wave: SURCHARGE_METHOD EXTRAN, SLOT, DYNAMIC_SLOT or TPA. Dynamic slot width Ts = g A / c^2 times P^2 (DynamicWave.cpp:253-256), c = DPS_CELERITY, default 25 m/s. Slot area does not convey flow in SLOT or DYNAMIC_SLOT (getConveyArea, src/legacy/engine/dwflow.c:780). NODE_CONTINUITY EXPLICIT is the SWMM5 two-branch rule; SEMI_IMPLICIT is dH = dV / max(As + 0.5 dt sum(dQ/dH), Asmin) at every node (DynamicWave.cpp:4415-4419, manual equation 3-45).
- SWMM6 finite volume: slot width T = g Afull / c^2, c = FV_SLOT_CELERITY, default 100 ft/s (fv/NetworkMeshBuilder.cpp:240-241).

Mid-pipe section (Register 20). NHEAD.FOR:95 and 98 cap each end depth at DEEP(N) + 2 FUDGE for all three Fortran solvers; NHEAD.FOR:348 then sets YMID = YNH + (YNL - YNH) FACTOR, and with NAVER = 2 (the default, INDAT1.FOR:133) AREA and HRAD in the momentum equation are the mid-section values alone (NHEAD.FOR:388-389). SWMM 5.2.4 does the same when SurchargeMethod is not SLOT: y1 = MIN(y1, yFull), y2 = MIN(y2, yFull) (dwflow.c:125-129), yMid = 0.5 (y1 + y2) (dwflow.c:150); OpenSWMM has the cap at DynamicWave.cpp:1937-1941. A conduit surcharged at one end only is therefore given a partly full mid-section. With JSLOT = 1 and the cap lifted, YMID comes from the uncapped heads.

Iteration and stepping: XROUTE and YROUTE take a half step and a full step and iterate surcharged junctions only (ITMAX, SURTOL). ZROUTE iterates all links and nodes with OMEGA = 0.75 on the first pass and 0.50 after (ZROUTE.FOR:63-64), on a Courant-limited sub-step that TRANSX halves at most twice on failure (TRANSX.FOR:704). SWMM5 and SWMM6 dynamic wave iterate all links and nodes up to MaxTrials = 8 with OMEGA = 0.5 (dynwave.c:61, 66; Constants.hpp:124). SWMM6 finite volume is explicit and sub-steps to FV_CFL = 0.5; mesh is max(FV_MIN_CELLS = 4, ceil(L / FV_CELL_LENGTH)) cells per conduit, and FV_CELL_LENGTH defaults to 0, which means four cells (fv/FvOptions.hpp:126-150).

## Inputs and outputs

Input to SWMM 4.4H: swmm4_EXAM1.DAT (EXTRAN User's Manual Example Problem 1) from SWMMBobSWMM6/1729-SWMM5-Models-2030, folder january5_2003_examples, commit 9ee63bd. Nine conduits, ten junctions, inflows of 45, 50 and 40 cfs ramped 0 to 0:15, held to 3:00, off at 3:15, 8-hour run. Per run only the control lines change: B0 ISOL; B1 NTCYC, DELT, JNTER; B2 ITMAX and SURTOL (30 and 0.05 for ISOL 0 and 1; 10 and 0.0025 for ISOL 2); print selections. KSUPER = 0, NEQUAL = 0. swmm4_EXAM4.DAT (weir) and swmm4_EXAM7.DAT (in-line pump) from the same folder are used for Register item 11 only.

SWMM5 and SWMM6 input: a hand conversion written for this app. Junction MaxDepth = ground minus invert; conduit 8060 outlet offset 2.2 ft; conduit 1600 entered from 16109 to 16009; trapezoids 9 ft deep, zero bottom width, 3:1 slopes; FLOW_ROUTING DYNWAVE, VARIABLE_STEP 0, LENGTHENING_STEP 0, INERTIAL_DAMPING NONE, NORMAL_FLOW_LIMITED SLOPE, MIN_SURFAREA 12.566, MAX_TRIALS 8, HEAD_TOLERANCE 0.005, ALLOW_PONDING NO, THREADS 1.

SWMM6 configurations plotted: "SWMM6 DW expanded" = SURCHARGE_METHOD DYNAMIC_SLOT, NODE_CONTINUITY SEMI_IMPLICIT, ANDERSON_ACCEL YES. "SWMM6 FV, 25 ft cells" = FLOW_ROUTING FV, FV_CELL_LENGTH 25. "SWMM6 FV, default mesh" = FLOW_ROUTING FV only. FV runs drop INERTIAL_DAMPING, NORMAL_FLOW_LIMITED and SURCHARGE_METHOD and leave every FV_ option at its default.

The app reads no user files. It exports two CSV tables, each one rectangle with one header row and quoted fields: the 54-run summary with a run_status column, and the series on screen.

## Checks

All mechanical. No human review yet. 1,157 runs: 973 for the ZROUTE deep dive (below), and 184 others: 54 sweep (9 configurations at 6 time steps), 20 with 10-second output, 6 SWMM6 EXTRAN parity, 7 SWMM6 option sets, 6 finite volume meshes, 2 OpenSWMM legacy engine, 20 single pipe, 21 SWMM 4.4H build-copy experiments for the bug hunt, and 48 for the why-ZROUTE question (28 at a 20-second step, 20 repeats at 10 and 30 seconds). 158 of those 184 are Example 1; 290 of the 1,157 are Example 1, 847 are 52 other example decks, 20 are a single pipe.

Flooding, peak and continuity at a 20-second step:

| Solution | Flooding, ft3 | 80608 flooded, min | Peak in conduit 1030, cfs | at h:mm | Max head 82309, ft | Continuity, % |
|---|---|---|---|---|---|---|
| XROUTE | 114,714 | 146.7 | 124 | 1:35 | 133.84 | 0.06 |
| YROUTE | 114,644 | 146.7 | 124 | 1:35 | 133.83 | 0.06 |
| SWMM 5.2.4 EXTRAN | 114,824 | 144.6 | 122.35 | 1:48 | 134.62 | 0.011 |
| ZROUTE as distributed | 0 | 0.0 | 120 | 3:11 | 132.58 | -1.05 |
| ZROUTE, slot freed | 84,349 | 133.7 | 127 | 1:32 | 134.78 | -0.31 |
| SWMM 5.2.4 SLOT | 78,582 | 134.4 | 125.55 | 1:47 | 133.83 | -0.186 |
| SWMM6 DW expanded | 90,866 | 137.4 | 124.24 | 1:47 | 133.72 | -0.118 |
| SWMM6 FV, 25 ft cells | 80,673 | 143.4 | 125.50 | 3:00 | 133.55 | 0.000 |
| SWMM6 FV, default mesh | 0 | 0.0 | 135.00 | 3:01 | 117.28 | 0.000 |

Total inflow 1,458,000 ft3. SWMM 4.4H prints peak flow to three figures. The finite volume peak is a flat plateau; its time is the last sample at the maximum.

Water lost to flooding, ft3, against time step:

| Solution | 5 s | 10 s | 20 s | 30 s | 60 s | 120 s |
|---|---|---|---|---|---|---|
| XROUTE | 114,947 | 114,761 | 114,714 | 113,969 | 112,960 | 6,624,120 |
| YROUTE | 114,964 | 114,690 | 114,644 | 113,851 | 112,460 | 122,270 |
| SWMM 5.2.4 EXTRAN | 115,303 | 115,565 | 114,824 | 114,868 | 113,169 | 110,033 |
| ZROUTE as distributed | 0 | 0 | 0 | 0 | 0 | 0 |
| ZROUTE, slot freed | 83,455 | 84,236 | 84,349 | 84,495 | 84,199 | 84,564 |
| SWMM 5.2.4 SLOT | 78,103 | 78,277 | 78,582 | 79,018 | 86,075 | 395,438 |
| SWMM6 DW expanded | 91,432 | 91,345 | 90,866 | 89,646 | 84,332 | 70,044 |
| SWMM6 FV, 25 ft cells | 80,630 | 80,630 | 80,673 | 80,673 | 80,717 | 80,760 |
| SWMM6 FV, default mesh | 0 | 0 | 0 | 0 | 0 | 0 |

Maximum head at junction 82309 (crown 118.5 ft, ground 155.0 ft) against time step:

| Solution | 5 s | 10 s | 20 s | 30 s | 60 s | 120 s |
|---|---|---|---|---|---|---|
| XROUTE | 155.00 | 139.70 | 133.84 | 133.93 | 133.73 | 136.36 |
| YROUTE | 154.10 | 137.98 | 133.83 | 133.93 | 133.70 | 133.64 |
| SWMM 5.2.4 EXTRAN | 153.61 | 146.41 | 134.62 | 134.35 | 134.18 | 133.98 |
| ZROUTE as distributed | 131.29 | 132.39 | 132.58 | 132.64 | 132.65 | 132.65 |
| ZROUTE, slot freed | 134.45 | 134.61 | 134.78 | 134.64 | 134.54 | 134.49 |
| SWMM 5.2.4 SLOT | 133.70 | 133.79 | 133.83 | 133.91 | 134.85 | 155.00 |
| SWMM6 DW expanded | 133.73 | 133.78 | 133.72 | 133.66 | 133.55 | 133.50 |
| SWMM6 FV, 25 ft cells | 133.55 | 133.55 | 133.55 | 133.55 | 133.51 | 133.43 |
| SWMM6 FV, default mesh | 117.28 | 117.28 | 117.28 | 117.28 | 117.30 | 117.30 |

Continuity error, percent:

| Solution | 5 s | 10 s | 20 s | 30 s | 60 s | 120 s |
|---|---|---|---|---|---|---|
| XROUTE | 0.12 | 0.13 | 0.06 | 0.13 | 0.02 | failed (asterisks; peak 2,720 cfs) |
| YROUTE | 0.10 | 0.13 | 0.06 | 0.14 | 0.25 | -8.01 |
| SWMM 5.2.4 EXTRAN | -0.070 | -0.076 | 0.011 | -0.039 | -0.025 | -0.097 |
| ZROUTE as distributed | 1.01 | -1.65 | -1.05 | 0.21 | 0.36 | -0.97 |
| ZROUTE, slot freed | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | 0.01 |
| SWMM 5.2.4 SLOT | -0.077 | -0.106 | -0.186 | -0.248 | 0.936 | -18.390 |
| SWMM6 DW expanded | -0.068 | -0.072 | -0.118 | -0.096 | -0.093 | -0.379 |
| SWMM6 FV, 25 ft cells | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| SWMM6 FV, default mesh | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

SWMM6 dynamic wave, SURCHARGE_METHOD EXTRAN, against EPA SWMM 5.2.4: flooding, peak outfall flow, time of peak, maximum head at 82309 and continuity error are identical at 5, 10, 20, 30, 60 and 120 s (30 of 30 values), including 153.61 and 146.41 ft at 5 and 10 s.

SWMM6 dynamic wave option sets, 20-second step:

| Options | Flooding, ft3 | 80608 flooded, min | Peak, cfs | at h:mm | Max head 82309, ft | Continuity, % | Iterations per step |
|---|---|---|---|---|---|---|---|
| EXTRAN (SWMM5 parity) | 114,824 | 144.6 | 122.35 | 1:48 | 134.62 | 0.011 | 2.37 |
| SLOT | 89,559 | 135.6 | 124.24 | 1:47 | 133.98 | -0.201 | 2.19 |
| DYNAMIC_SLOT | 91,781 | 138.6 | 124.24 | 1:47 | 133.87 | -0.101 | 2.19 |
| TPA | 44,083 | 69.6 | 121.98 | 3:03 | 133.63 | -0.400 | 2.27 |
| EXTRAN + SEMI_IMPLICIT | 6,534 | 16.2 | 121.06 | 3:10 | 133.34 | -0.207 | 2.01 |
| DYNAMIC_SLOT + SEMI_IMPLICIT | 90,866 | 137.4 | 124.24 | 1:47 | 133.72 | -0.114 | 2.18 |
| DYNAMIC_SLOT + SEMI_IMPLICIT + ANDERSON | 90,866 | 137.4 | 124.24 | 1:47 | 133.72 | -0.118 | 2.18 |

Same input, SURCHARGE_METHOD SLOT: EPA SWMM 5.2.4 78,582 ft3; OpenSWMM legacy engine 5.3.0 89,559; OpenSWMM 6.0.0-alpha.4 89,559. With EXTRAN all three give 114,824.

SWMM6 finite volume against FV_CELL_LENGTH, 20-second routing step:

| FV_CELL_LENGTH | Flooding, ft3 | 80608 flooded, min | Peak, cfs | Max head 82309, ft | Continuity, % | Substeps per 20 s | Run time, s |
|---|---|---|---|---|---|---|---|
| not set (4 cells per conduit) | 0 | 0.0 | 135.00 | 117.28 | 0.000 | 4.3 | 0.10 |
| 500 ft | 0 | 0.0 | 135.00 | 131.89 | 0.000 | 5.5 | 0.15 |
| 200 ft | 58,980 | 139.2 | 127.81 | 133.12 | 0.000 | 10.1 | 0.38 |
| 100 ft | 72,832 | 142.2 | 126.35 | 133.37 | 0.000 | 17.9 | 0.81 |
| 50 ft | 78,147 | 142.8 | 125.77 | 133.49 | 0.000 | 35.6 | 2.71 |
| 25 ft | 80,673 | 143.4 | 125.50 | 133.55 | 0.000 | 70.6 | 8.63 |

Finite volume substeps per routing step at 25 ft cells: 18.1, 35.5, 70.6, 105.8, 211.2, 421.7 at 5, 10, 20, 30, 60, 120 s.

Single pipe (circular 5 ft, 5,000 ft, slope 0.0019, steady inflow, normal-depth outfall), depth at end of run, ft:

| Case | Manning normal depth | SWMM6 dynamic wave | FV, 4 cells | FV, 40 cells |
|---|---|---|---|---|
| n 0.034, 20 cfs | 2.385 | 2.384 | 1.626 | 2.299 |
| n 0.015, 20 cfs | 1.530 | 1.529 | 1.450 | 1.553 |
| n 0.034, 40 cfs | 3.785 | 3.786 | 2.720 | 3.682 |

SWMM 4.4H build-copy experiments (Register 11, 12, 13, 15):

| Item | Change in the build copy | Stock | Changed | Reference |
|---|---|---|---|---|
| 11, Example 7 flooding, ft3 | YROUTE.FOR:215 `- (QT(N)+QO(N))` to `- 0.5*(QT(N)+QO(N))` | 37,026 | 36,658 | XROUTE 36,662 |
| 11, Example 7, 80608 flooded, min | same | 140.3 | 139.0 | XROUTE 139.0 |
| 11, Example 4 max head 80408, ft | same | 132.79 | 132.92 | XROUTE 132.90 |
| 11, Example 1 | same | 114,644 ft3 | 114,644 ft3 | summary identical |
| 12, YROUTE 1+AKON below 0.5 / negative, 20 s | one WRITE added | 12 / 10, lowest -3.00 | n/a | XROUTE denominator is at least 1 |
| 12, same, 120 s | one WRITE added | 105 / 102, -56.1 cfs in conduit 1602 at cycle 1 | n/a | |
| 13, ZROUTE peak outfall flow, cfs | ZROUTE.FOR compiled without -fno-automatic | 120 | 0.0 | |
| 13, ZROUTE flooding, ft3 | same | 0 | 1,477,890 | inflow 1,458,000 |
| 13, ZROUTE continuity, % and ITMAX exceeded | same | -1.05, 2 | -15.37, 86 | |
| 15, XROUTE max junction area 16109, ft2 | AS(J) accumulated on the first pass only | 367,400 | 13,800 | ZROUTE 13,760 |
| 15, same, 82309 and 80608 | same | 237,900 and 109,200 | 15,710 and 11,840 | ZROUTE 15,710 and 11,820 |
| 15, flooding, head, continuity | same | 114,714; 133.84; 0.06 | identical | |

Why ZROUTE differs (Register 1, 8, 20, 21). Every row is a build copy with one change, Example 1, 20-second step; flows and head are the 2:00 values.

Conduit 1602 (5 ft, 5,000 ft, n 0.034) at 2:00, from instrumented builds: XROUTE uses depths 5.000 (capped) and 2.969 ft, mid depth 3.985 ft, A 16.77 ft2, R 1.521 ft, flow 72.03 cfs. ZROUTE with the slot freed uses 21.186 and 3.020 ft, mid depth 12.103 ft, A 19.81 ft2 (full 19.63 plus slot), R 1.250 ft, flow 74.38 cfs. A R^(2/3) relative to the full pipe: 0.974 capped, 1.009 freed. Head at 82309 is 133.63 ft, crown 117.3 ft; a straight grade line is 7.1 ft above the crown at mid-length.

ZROUTE as distributed, cap kept, slot width at the crown changed (HYDRAD.FOR:255, 257):

| Slot width at the crown | Flooding, ft3 | 80608 flooded, min | Continuity, % |
|---|---|---|---|
| 0.3919 D (as distributed) | 0 | 0.0 | -1.05 |
| 0.3 D | 8,341 | 19.7 | -1.09 |
| 0.2 D | 25,156 | 43.0 | -0.82 |
| 0.1 D | 42,969 | 65.3 | -0.16 |
| 0.05 D | 51,944 | 76.7 | -0.78 |
| 0.02 D | 57,472 | 84.0 | -0.25 |
| 0.01 D | 59,447 | 86.7 | -0.39 |
| 0.005 D | 60,433 | 87.7 | -0.22 |
| 0.002 D | 61,078 | 88.7 | -0.46 |

From ZROUTE as distributed to XROUTE:

| Build | Flooding, ft3 | 80608 flooded, min | Flow in 1602, cfs | Flow in 8060, cfs | Head at 82309, ft | Continuity, % |
|---|---|---|---|---|---|---|
| ZROUTE as distributed | 0 | 0.0 | 63.24 | 37.64 | 128.37 | -1.05 |
| Crown slot narrowed from 0.3919 D to 0.005 D | 60,433 | 87.7 | 71.88 | 32.45 | 133.60 | -0.22 |
| Plus mid-section surface width at the uncapped depth | 108,445 | 139.7 | 71.97 | 31.97 | 133.63 | -0.15 |
| XROUTE | 114,714 | 146.7 | 72.03 | 32.03 | 133.63 | 0.06 |

From XROUTE to ZROUTE with the slot freed:

| Build | Flooding, ft3 | 80608 flooded, min | Flow in 1602, cfs | Flow in 8060, cfs | Head at 82309, ft | Continuity, % |
|---|---|---|---|---|---|---|
| XROUTE | 114,714 | 146.7 | 72.03 | 32.03 | 133.63 | 0.06 |
| XROUTE, mid depth from the uncapped heads | 97,217 | 146.3 | 73.84 | 33.84 | 133.47 | -0.22 |
| YROUTE, mid depth from the uncapped heads | 97,181 | 146.0 | 73.84 | 33.84 | 133.47 | -0.20 |
| ZROUTE, slot freed | 84,349 | 133.7 | 74.38 | 34.38 | 133.49 | -0.31 |
| ZROUTE, slot freed, geometry capped at the crown | 106,913 | 137.7 | 71.97 | 31.97 | 133.63 | -0.25 |

XROUTE to slot-freed ZROUTE is 30,365 ft3: 17,497 from the mid-pipe section (measured); the remaining 12,868 is about 4,300 from slot area carrying flow (0.54 cfs for 133.7 min) and about 8,400 from 12.6 fewer flooded minutes (arithmetic on these rows, not a separate run).

Slot-freed ZROUTE with its numerics changed:

| Change | Flooding, ft3 | Peak outfall, cfs | at h:mm | ITMAX exceeded | Continuity, % |
|---|---|---|---|---|---|
| ZROUTE, slot freed (reference) | 84,349 | 127 | 1:32 | 0 | -0.31 |
| Local inertia term doubled to 2 V dA | 83,907 | 126 | 1:36 | 12 | -0.37 |
| Both inertia terms removed | 80,121 | 127 | 1:34 | 3 | 0.33 |
| Time weights 1.0 new, 0.0 old | 84,328 | 127 | 1:35 | 3 | -0.14 |
| Time weights 0.5 and 0.5 | 84,591 | 127 | 1:33 | 7 | -0.25 |
| Relaxation 0.50 on every pass | 84,361 | 127 | 1:34 | 3 | -3.09 |

EPA SWMM 5.2.4 build copy with the switch (ZWHY=A: EXTRAN with aMid = aFull, rMid = rFull when the mean of the uncapped end depths is at or above yFull; ZWHY=C: SLOT with y1, y2 capped at yFull after findSurfArea):

| Build | Flooding, ft3 | 80608 flooded, min | Flow in 1602, cfs | Flow in 8060, cfs | Head at 82309, ft | Continuity, % |
|---|---|---|---|---|---|---|
| EXTRAN | 114,824 | 144.6 | 71.99 | 31.99 | 133.63 | 0.01 |
| EXTRAN, mid section from the uncapped heads | 94,264 | 142.2 | 73.85 | 33.85 | 133.47 | -0.01 |
| SLOT, geometry capped at the crown | 109,161 | 139.8 | 71.99 | 31.99 | 133.63 | -0.25 |
| SLOT | 78,582 | 134.4 | 75.16 | 35.16 | 133.48 | -0.19 |

Flooding, ft3, at three time steps:

| Build | 10 s | 20 s | 30 s |
|---|---|---|---|
| XROUTE | 114,761 | 114,714 | 113,969 |
| XROUTE, mid depth from the uncapped heads | 97,391 | 97,217 | 96,828 |
| ZROUTE, slot freed | 84,236 | 84,349 | 84,495 |
| ZROUTE, slot freed, geometry capped | 106,590 | 106,913 | 106,892 |
| ZROUTE, cap kept, crown slot 0.005 D | 58,675 | 60,433 | 62,678 |
| the same plus mid-section width at the uncapped depth | 108,410 | 108,445 | 108,879 |
| SWMM5 EXTRAN | 115,565 | 114,824 | 114,868 |
| SWMM5 EXTRAN, mid section from the uncapped heads | 94,874 | 94,264 | 94,220 |
| SWMM5 SLOT, geometry capped | 108,464 | 109,161 | 109,815 |
| SWMM5 SLOT | 78,277 | 78,582 | 79,018 |

ZROUTE deep dive (Register 4, 22 to 30). 973 runs: 16 builds at six time steps on Example 1 (96); 16 configurations on the 53 example decks that read under this build (848); 29 supporting runs (failure counts 12, tolerance 4, the two BOUND lines apart 6, negative-depth resets 4, the alternative continuity line 3). Base for every change is the slot-freed build.

Continuity error, percent, Example 1, one change at a time, then together ("ZROUTE improved" = the eleven kept changes):

| Change | 5 s | 10 s | 20 s | 30 s | 60 s | 120 s | Flooding at 20 s, ft3 | Decks changed, of 53 |
|---|---|---|---|---|---|---|---|---|
| ZROUTE, slot freed (reference) | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | +0.01 | 84,349 |  |
| Final head taken unrelaxed on convergence | +0.09 | +0.05 | +0.06 | +0.13 | +0.24 | +1.84 | 84,562 | 44 |
| Failed substep restored to its own start | -0.71 | -0.43 | -0.31 | -0.42 | -0.33 | +0.07 | 84,349 | 29 |
| Outfall volume booked with the average flow | -0.70 | -0.49 | -0.31 | -0.43 | -0.64 | -0.32 | 84,349 | 37 |
| Junction volume booked once per step, with DELT | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | +0.01 | 84,349 | 0 |
| Slot stores water but carries no flow | -0.73 | -0.47 | -0.36 | -0.44 | -0.61 | +0.25 | 89,784 | 36 |
| Stall no longer counted as success | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | +0.01 | 84,349 | 0 |
| SAVE for the time weights | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | +0.01 | 84,349 | 0 |
| Gate call moved out of the iteration | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | +0.01 | 84,349 | 0 |
| Orifice class test set to 50 | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | +0.01 | 84,349 | 0 |
| Wet-well inflow kept; alias guarded | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | +0.01 | 84,349 | 2 |
| Entrance and exit loss ends swapped back | -0.69 | -0.49 | -0.31 | -0.43 | -0.55 | +0.01 | 84,349 | 0 |
| Convergence tested on the residual (not kept) | -0.59 | -0.20 | -0.13 | -0.16 | -0.09 | +1.08 | 84,577 |  |
| Up to four halvings (not kept) | -0.69 | -0.49 | -0.31 | -0.46 | -0.55 | -0.08 | 84,349 |  |
| All of the above except the slot change | -0.11 | +0.11 | +0.13 | +0.14 | +0.16 | +0.15 | 84,562 |  |
| ZROUTE improved: all eleven kept changes | +0.10 | +0.10 | +0.16 | +0.12 | +0.11 | +0.11 | 90,007 |  |

ZROUTE improved floods 90,007 to 90,322 ft3 on Example 1 at the six time steps. XROUTE: 0.12, 0.13, 0.06, 0.13, 0.02 percent and failed at 120 s. ZROUTE as distributed: 1.01, -1.65, -1.05, 0.21, 0.36, -0.97.

ZROUTE iteration failures on Example 1 (one WRITE in TRANSX after CALL ZROUTE):

| Count | 5 s | 10 s | 20 s | 30 s | 60 s | 120 s |
|---|---|---|---|---|---|---|
| As distributed: failures | 4 | 2 | 3 | 33 | 24 | 30 |
| accepted unconverged | 0 | 0 | 1 | 18 | 17 | 21 |
| restored to the wrong state | 0 | 0 | 0 | 14 | 15 | 25 |
| printed as ITMAX exceeded | 4 | 2 | 2 | 15 | 7 | 9 |
| Slot freed: failures | 5 | 4 | 0 | 5 | 2 | 8 |
| restored to the wrong state | 0 | 1 | 0 | 0 | 1 | 5 |

Tolerance (slot freed, 20 s): continuity -0.31 percent at SURTOL 0.0025 (ITMAX 10), +0.05 at 0.001 (30), +0.13 at 0.00025 (50), +0.14 at 0.00005 (100).

50 example decks (61 named swmm4_*; 8 stop on input errors; 3 steep-drop decks listed apart), absolute continuity error:

| Solver | Median, % | Mean, % | Decks over 1% | Decks over 5% | Largest, % |
|---|---|---|---|---|---|
| XROUTE | 0.50 | 1.45 | 17 | 5 | 10.65 |
| YROUTE | 0.54 | 11.11 | 20 | 8 | 452.48 |
| ZROUTE as distributed | 1.42 | 4.80 | 27 | 12 | 50.09 |
| ZROUTE, slot freed | 0.73 | 2.04 | 19 | 5 | 25.02 |
| ZROUTE improved | 0.38 | 1.21 | 16 | 3 | 8.79 |

The same over all 53 decks that read, the three steep-drop decks included:

| Solver | Median, % | Mean, % | Decks over 1% | Decks over 5% | Largest, % |
|---|---|---|---|---|---|
| XROUTE | 0.47 | 1.38 | 17 | 5 | 10.65 |
| YROUTE | 0.53 | 10.50 | 20 | 8 | 452.48 |
| ZROUTE as distributed | 2.21 | 7.34 | 30 | 14 | 136.03 |
| ZROUTE, slot freed | 0.93 | 4.98 | 22 | 8 | 128.00 |
| ZROUTE improved | 0.42 | 1.69 | 18 | 5 | 16.78 |

Deck by deck, absolute continuity error of ZROUTE improved against another build. This is a comparison of aggregates and counts, not a claim that the improved build matches XROUTE on any stated number of decks:

| Compared with | Decks | Lower | Same | Higher | Within 0.25 point | Improved better by more | Other better by more |
|---|---|---|---|---|---|---|---|
| XROUTE | 50 | 19 | 6 | 25 | 31 | 7 | 12 |
| XROUTE | 53 | 19 | 6 | 28 | 31 | 7 | 15 |
| ZROUTE as distributed | 50 | 36 | 3 | 11 | 20 | 28 | 2 |
| ZROUTE as distributed | 53 | 38 | 3 | 12 | 20 | 30 | 3 |

The 53-deck extension is SWMM 4.4H only. SWMM 5.2.4 and SWMM6 were not run on these decks.

Independent mass balance, Example 1, percent of the deck inflow of 1,458,000 ft3: inflow - trapezoid integral of the printed conduit 1030 hydrograph (2-minute samples) - printed flooding - printed volume left. Each cell is "engine's own figure / independent figure". The two agree within 0.03 point in 55 of the 59 runs that print a continuity figure; the others are ZROUTE at 60 s (+0.36 printed, +0.30 independent); ZROUTE at 120 s (-0.97 printed, -1.16 independent); ZROUTE, slot freed at 60 s (-0.55 printed, -0.65 independent); ZROUTE, slot freed at 120 s (+0.01 printed, -0.31 independent) (Register 25).

| Engine | 5 s | 10 s | 20 s | 30 s | 60 s | 120 s |
|---|---|---|---|---|---|---|
| XROUTE | +0.12 / +0.13 | +0.13 / +0.14 | +0.06 / +0.06 | +0.13 / +0.13 | +0.02 / +0.02 | failed / -1160.34 |
| YROUTE | +0.10 / +0.11 | +0.13 / +0.13 | +0.06 / +0.06 | +0.14 / +0.14 | +0.25 / +0.25 | -8.01 / -8.01 |
| ZROUTE | +1.01 / +1.01 | -1.65 / -1.66 | -1.05 / -1.06 | +0.21 / +0.21 | +0.36 / +0.30 | -0.97 / -1.16 |
| ZROUTE, slot freed | -0.69 / -0.69 | -0.49 / -0.49 | -0.31 / -0.31 | -0.43 / -0.43 | -0.55 / -0.65 | +0.01 / -0.31 |
| ZROUTE improved | +0.10 / +0.10 | +0.10 / +0.10 | +0.16 / +0.15 | +0.12 / +0.12 | +0.11 / +0.12 | +0.11 / +0.10 |
| SWMM5 EXTRAN | -0.07 / -0.08 | -0.08 / -0.08 | +0.01 / +0.02 | -0.04 / -0.03 | -0.03 / -0.04 | -0.10 / -0.10 |
| SWMM5 SLOT | -0.08 / -0.07 | -0.11 / -0.10 | -0.19 / -0.20 | -0.25 / -0.25 | +0.94 / +0.94 | -18.39 / -18.39 |
| SWMM6 DW expanded | -0.07 / -0.06 | -0.07 / -0.07 | -0.12 / -0.13 | -0.10 / -0.10 | -0.09 / -0.09 | -0.38 / -0.38 |
| SWMM6 FV, 25 ft cells | +0.00 / -0.02 | +0.00 / -0.02 | +0.00 / -0.02 | +0.00 / -0.01 | +0.00 / -0.01 | +0.00 / -0.02 |
| SWMM6 FV, default mesh | +0.00 / +0.02 | +0.00 / -0.03 | +0.00 / -0.03 | +0.00 / -0.02 | +0.00 / +0.00 | +0.00 / -0.01 |

Decks where ZROUTE as distributed is worst, continuity error, percent:

| Deck | XROUTE | ZROUTE as distributed | Slot freed | Improved |
|---|---|---|---|---|
| EXAM61 | -10.65 | +50.09 | +1.58 | +1.89 |
| EXAM30 | -0.52 | +25.02 | +25.02 | -0.66 |
| HIGH_BC_CRITICAL_UPSTREAM_DOWNSTREAM_EXAMPLE | -0.29 | +22.22 | +2.86 | +2.83 |
| EXAM75 | +0.45 | +17.37 | -1.00 | -0.42 |
| CRITICAL_DOWNSTREAM_EXAMPLE | +3.44 | +12.07 | +3.71 | +3.28 |
| EXAM60 | -1.33 | +11.03 | +0.58 | +0.24 |
| EXAM12 | +1.18 | +10.28 | +10.28 | +2.25 |
| EXAM58 | -3.60 | +10.05 | +2.50 | -0.16 |
| EXAM2 | -8.88 | -9.90 | -9.08 | -8.79 |
| EXAM59 | -2.25 | +8.85 | +0.52 | +0.33 |
| eXAM15 | -5.90 | -5.99 | -5.96 | -5.92 |
| EXAM46 | +5.97 | +5.35 | +5.35 | +6.14 |

Steep-drop decks (70 ft drop in 100 ft of 2 ft pipe, 1-second step), continuity error, percent, and the printed ITMAX count for ZROUTE as distributed, slot freed and improved:

| Deck | XROUTE | As distributed | Slot freed | Improved | ITMAX printed (three builds) |
|---|---|---|---|---|---|
| STEEP_adverse_flat_example_1 | +0.47 | -4.30 | -6.21 | -16.78 | 35, 83, 72 |
| STEEP_drop_example_1 | +0.23 | -136.03 | -27.79 | -11.87 | 7964, 11822, 11856 |
| STEEP_drop_example_2 | +0.08 | -8.97 | -128.00 | -0.66 | 7960, 11745, 611 |

EXAM12 (pump stations) with the two BOUND changes apart: BOUND.FOR:467 changed alone, continuity 10.28 to 2.23 percent, outflow 1,137,700 to 1,277,700 ft3 of 1,350,000; BOUND.FOR:502 guarded alone, no change. Alternative continuity line on Example 1 at 20 s as distributed: -81.15 (XROUTE), -80.66 (YROUTE), -25.03 (ZROUTE); main figures 0.06, 0.06, -1.05.

Other checks:

- The XROUTE.FOR supplied by the author is identical to the copy in the WCH_2004 repository (diff).
- SWMM 4.4H built here runs EXTRAN44.doc.txt to completion with 0.01 percent continuity error, the figure in the repository README.
- SWMM 5.2.4 Release build aborted on this input under glibc fortification; an AddressSanitizer build ran it clean; the build used has _FORTIFY_SOURCE=0.
- Head spike at 82309 at 10-second output and a 5-second step: one sample at 155.0 (XROUTE), 154.1 (YROUTE) and 153.5 ft (SWMM5 EXTRAN), then about 121.5 ft. SWMM6 DW expanded and SWMM6 FV at 25 ft show none.
- ZROUTE "Number of times ITMAX exceeded" as distributed: 4, 2, 2, 15, 7, 9 at 5, 10, 20, 30, 60, 120 s.
- The YROUTE zero-denominator message did not appear in any YROUTE run.

## What this does not show

1. A real system. 290 of 1,157 runs are Example 1, which is small and near capacity; the other 52 decks are small manual examples.
2. Which engine is right. There is no measured flood volume.
3. A released SWMM6. OpenSWMM 6.0.0-alpha.4 is an alpha; defaults may change. Nothing here has been reported to its authors.
4. Finite volume mesh convergence. Flooding was still rising at 25 ft cells (72,832, 78,147, 80,673 at 100, 50, 25 ft). FV_ORDER 2, RK2, HLL, FV_PRESSURE_CLOSURE TPA and the implicit pressurized option were not run.
5. Why the finite volume runs report an external inflow that grows with the mesh: 1,457,953 ft3 at the default, 1,461,090 at 25 ft, input 1,458,000. Not investigated.
6. The cause of Register 18 (SWMM6 EXTRAN + SEMI_IMPLICIT). The effect is measured; the cause is read from DynamicWave.cpp:1956 and 4415-4419 and was not isolated in a build. The TPA result (44,083 ft3) is not explained.
7. SWMM6 virtual junctions and unsteady friction. ANDERSON_ACCEL was run on one network where its documented skip rules apply.
8. Register 14 (OGATES per iteration) and 16 (NKLASS .LE.51): read, not run. Example 1 has no orifices.
9. Local losses (NEQUAL 4 or 5): the ENTK/EXITK pairing (Register 5) was read, not run.
10. An OpenMP build: the shared FF1, FF2, ITEST (Register 6) were read, not run.
11. The half-weight local inertia term in ZROUTE (Register 8) beyond one run on one network, where doubling it moved flooding by about half a percent.
12. That any changed build copy is a safe fix. The version 2.1 and 2.2 copies were tested on one to three decks; the version 2.3 copies on Example 1 and up to 53 decks.
13. The original Compaq Fortran build of 4.4H.
14. A reviewed SWMM5 conversion of Example 1.
15. A documented lineage. It is inferred from code and comments.
16. A timing benchmark. Run times are single runs on one machine.
17. The spike in the 2-minute series; maximum heads are from each engine's summary table.
18. Which mid-pipe description is right (Register 20). The capped and uncapped-head sections give different answers; a straight grade line favors the full section; nothing was compared with a measurement. The finding rests on one conduit, 1602, in one network.
19. The split of the last 12,868 ft3 between slot conveyance and slot storage: arithmetic, not a run. The OpenSWMM cap (DynamicWave.cpp:1937-1941) was read and not changed.
20. Nothing here has been reported to EPA or to the OpenSWMM authors.
21. That ZROUTE improved is a fix. It is eleven experiments in one build. Four of them (gate call, orifice class, loss ends, stall test) changed nothing on any deck and rest on reading.
22. A ZROUTE that survives steep drops (Register 28). Cause not found.
23. That ZROUTE improved matches XROUTE deck by deck. On the 50 non-steep decks its aggregate continuity error is lower and XROUTE is closer on 25 of them; over all 53 its mean and worst case are worse than XROUTE's.
24. Equal coverage of the six solvers. The 53-deck extension is SWMM 4.4H only; SWMM 5.2.4 and SWMM6 ran Example 1 and a single pipe.
25. An independent mass balance beyond Example 1. The 53-deck statistics rest on each build's own continuity figure, and two of the eleven changes alter how that figure is booked. The common balance uses a 2-minute hydrograph, the trapezoid rule and each engine's own printed flooding and final volume.
26. Raw reports for the 20 single-pipe runs (not kept; the scripts are in the bundle). 1,365 other raw reports are in rosetta-stone-raw-reports.zip.
27. The surcharge formula dH = dQ/(0.3215 dt) on the Surcharge tab as a general law: it assumes a junction at least 1.25 crown depths up, full pipes, no friction in dQ/dH and a fixed imbalance; nearer the crown the denominator blends toward A_old/dt (XROUTE.FOR:510-511, dynwave.c:728-732).
28. A visual, mobile or accessibility review by a person. The outside review of version 2.3 did not include one.
23. Eight of 61 example decks (input errors under this gfortran build). YROUTE's -452 percent on EXAM58 was not investigated.
24. No person has yet reviewed any of the thirty Register items or rerun the engines.

Register (m = measured in a run, r = read in the source): 1 m NHEAD clamp holds the ZROUTE slot at 0.3919 D. 2 m EXTRAN surcharge head spike grows as dt shrinks. 3 m XROUTE diverges at 120 s. 4 m ZROUTE.FOR:278 VOL = VOL + SUMQ, no DELT, inside the iteration; with OUTPUT.FOR:108 the alternative continuity line is wrong for every solver. 5 r ENTK applied to the downstream velocity, EXITK to the upstream. 6 r FF1, FF2, ITEST not PRIVATE. 7 r YROUTE guard sets AKON = -1.0000001. 8 m ZROUTE local inertia V dA where EXTRAN has 2 V dA; doubling it changes flooding 0.5 percent. 9 m ZROUTE accepts unconverged steps after two halvings. 10 r reversal substitute 0.001 has no units. 11 m YROUTE.FOR:215 lacks the 0.5 that YROUTE.FOR:219 and XROUTE.FOR:198 have. 12 m YROUTE 1+AKON goes negative when a dry pipe wets (YROUTE.FOR:342-348). 13 m ZROUTE WD, WT, OLDFLW, OLDDEP have no SAVE (ZROUTE.FOR:26-41). 14 r ZROUTE calls OGATES(DELT,...) inside the iteration loop (ZROUTE.FOR:62-68). 15 m XROUTE and YROUTE accumulate AS(J) over surcharge iterations (XROUTE.FOR:426-430, 531-538). 16 r ZROUTE.FOR:209 NKLASS .LE.51 where XROUTE and YROUTE have .LE.50. 17 m SWMM6 finite volume default mesh reports no flooding; documented behavior. 18 m SWMM6 EXTRAN + SEMI_IMPLICIT: 6,534 ft3 against 114,824; cause read. 19 m SLOT differs between EPA 5.2.4 and OpenSWMM by design (getConveyArea). 20 m the crown cap makes a conduit surcharged at one end partly full at mid-length (NHEAD.FOR:95, 98, 348; dwflow.c:125-129, 150): worth 17,497 ft3 in XROUTE and 20,560 in SWMM 5.2.4. 21 m ZROUTE credits that mid-section's free surface to a surcharged junction (NHEAD.FOR:362-363; ZROUTE.FOR:275-276): with item 1 it accounts for ZROUTE's missing flooding (0, 60,433, 108,445, against 114,714). 22 m ZROUTE returns a relaxed head (ZROUTE.FOR:276-281, 328): EXAM30 25.02 to -0.66 percent. 23 m BOUND.FOR:467 drops wet-well inflow under ISOL 2: EXAM12 10.28 to 2.23. 24 m TRANSX.FOR:704-717 restores a failed substep to the start of the whole step. 25 m TRANSX.FOR:749 books outfall volume with the end-of-substep flow. 26 m the printed ITMAX count (TRANSX.FOR:712, 1636) omits accepted failures: 15 printed, 33 counted, 18 accepted at 30 s. 27 m HYDRAD.FOR:262 slot area is width times height and conveys: 84,349 to 89,784 ft3 when it does not. 28 m ZROUTE fails on the three steep-drop decks in every form. 29 r BOUND.FOR:502 writes SUMQS, which ZROUTE.FOR:29 aliases to Q0. 30 r ZROUTE.FOR:143, 161 overwrite ANL and ANH before the normal-flow limit uses them.

## How to reproduce

The reproduction bundle (rosetta-stone-reproduce.zip) holds the scripts, the input decks (Example 1 in every form run, the hand conversions for SWMM5 and SWMM6, and the 61 swmm4_* example decks), the note for each changed build copy, the build settings, the parsed results and manifest.csv. The manifest has one row for each of 1,365 retained raw reports: run, engine, source revision, build copy, change note, solver or options, deck, time step, input file, report file, the continuity figure the report prints, and the script that made it. rosetta-stone-raw-reports.zip holds those inputs and reports, the 128 runs that stop on input errors included. More reports are retained than the 1,157 runs counted because 36 runs of six intermediate combinations, the input-error stops and some repeats are kept; the 20 single-pipe reports are not.

1. Clone SWMMEnablement/WCH_2004_SWMM44H; run build_swmm44h.sh WCH_2004 build. On a case-sensitive file system, link include files whose names differ in case.
2. Clone USEPA/Stormwater-Management-Model; cmake and make with -D_FORTIFY_SOURCE=0.
3. Clone HydroCouple/openswmm.engine at branch swmm6_rel, commit 0071c5f; cmake with -DOPENSWMM_WITH_GEOPACKAGE=OFF -DOPENSWMM_WITH_HDF5=OFF -DOPENSWMM_BUILD_2D=OFF -DOPENSWMM_BUILD_GPU_PLUGIN=OFF and fortification off.
4. run_engines.py and run_spike.py: SWMM 4.4H at ISOL 0, 1, 2 and SWMM 5.2.4 with EXTRAN and SLOT, DELT 5, 10, 20, 30, 60, 120.
5. run_swmm6.py: the SWMM6 sweep, option sets, meshes and spike runs. The SWMM6 CLI writes no time series to the report; swmmout.py reads the binary .out file.
6. run_bugs.py: the SWMM 4.4H build copies. Slot freed: NHEAD.FOR lines 95 and 98 prefixed with `IF(JSLOT.EQ.0)`. Item 11: `0.5*` restored at YROUTE.FOR:215. Item 15: `IF(IT.EQ.0) AS(J) = AS(J) + (AS1(J) - ASL(J))`. Item 13: ZROUTE.FOR compiled without -fno-automatic. Item 12: one WRITE of 1.0+AKON to unit 97 when it is below 0.5.
7. run_zwhy.py, run_zwhy2.py, run_zwhy3.py with zbuild.py: the why-ZROUTE build copies and runs. Each copy's change is in patches/zwhy/<name>.txt; the SWMM5 switch is patches/zwhy/dwflow_switch.diff.
8. run_zdeep.py, run_zdeep2.py and zdiff.py: the deep-dive builds (each change is in patches/zdeep/<name>.txt) and the 53-deck differential test.
9. indep_balance.py works the independent mass balance from the retained reports; manifest.py writes manifest.csv. pack.py, pack6.py, pack7.py, pack8.py, pack9.py build the data the app embeds; mkmd.py fills the tables in this file from the same data; set_complexity.py and meter.js grade the built page on the SWMM App Complexity Meter.
10. Flooding for 4.4H is the sum of "JUNCTION OUTFLOW, FT3" for junctions other than the outfall 10208; for SWMM5 and SWMM6 it is Flooding Loss in acre-feet times 43,560.

## Credits and licenses

Extran: Larry Roesner, Robert Shubinski, John Aldrich (Camp Dresser & McKee), with later work by Robert Dickinson. SWMM 4.4H: Wayne Huber, Oregon State University. Source revisions named in NHEAD.FOR: Chuck Moore and Brett Cunningham (CDM). EPA SWMM5 dynamic wave routing: Lewis Rossman and Michael Tryby (EPA) and Robert Dickinson (CDM), per the header of dwflow.c. OpenSWMM Engine: the HydroCouple project, Caleb Buahin project lead, with the contributors in its AUTHORS.md. Testing method (measured against read, and a statement of what is not shown): after Corinne Wiesner-Friedman. App: Robert E. Dickinson, SWMM Enablement.

SWMM 4.4H as held in WCH_2004 and EPA SWMM5 are public domain. OpenSWMM Engine, Copyright 2026 HydroCouple Developers, is licensed under the Apache License, Version 2.0 (https://www.apache.org/licenses/LICENSE-2.0); its NOTICE reads "This product includes software developed by the OpenSWMM authors (https://github.com/HydroCouple/openswmm.engine)." This app ships results and short quoted source lines. It does not ship or modify the OpenSWMM engine.

## Complexity

Each of these apps now says how complicated it is, on a scale anyone can check. The scale is the SWMM App Complexity Meter, version 1.9.1. It counts eight things in a program's source and compares each with the same count over the 43 repositories of github.com/HydroCouple, which are fixed at 100. The delivered file, st-venant-solver-rosetta-stone.html, was handed to the meter page itself. The meter read 36,292 code tokens on 1,798 code-bearing lines and returned an index of 51.5. Against HydroCouple's SWMM engine alone, set to 100, the same page reads 60.5.

Read the number for what it is. It measures source footprint: how much code, branching and vocabulary sits in the page. It does not say the page is right. The engines, the 45 changed copies of SWMM 4.4H, the one of SWMM 5.2.4 and the scripts that made the runs are not in the page and are not counted. Test markers score zero because the page carries no tests of its own; its checks ran in the build.

| Dimension | This page | HydroCouple | Score |
|---|---|---|---|
| Bulk | 36,292 code tokens | 6,607,205 | 43.7 |
| Decisions | 289 estimated decision points | 123,080 | 34.7 |
| Routines | 261 callable units | 38,818 | 45.8 |
| Test markers | 0 test and assertion markers | 27,339 | 0.0 |
| Stack | 6 languages + technology signals | 31.57 | 82.0 |
| Dependencies | 2 outside libraries | 77 | 60.4 |
| Formats | 5 file formats | 43 | 76.6 |
| SWMM vocabulary | 26 SWMM 5.2.4 terms in code | 226 | 76.5 |
| Complexity index |  | 100 | 51.5 |

## AI use

This app and this essay were built with Claude, Anthropic's AI model, in November 2026, under the direction of Robert (Bob) Dickinson. He asked the question, pointed to the WCH_2004 repository, supplied XROUTE.FOR when it was missing, asked for the app, asked that the two SWMM6 solutions be added and that YROUTE and ZROUTE be searched for bugs, asked why ZROUTE is different, asked for a deep dive on ZROUTE for bugs and improvements, and for this version supplied an outside review of version 2.3 to be answered. Responsibility for the published work is his. What Claude did. It read XROUTE, YROUTE, ZROUTE, NHEAD, HYDRAD, TRANSX, INDAT1, BOUND and OGATES from SWMM 4.4H, dwflow.c and dynwave.c from SWMM 5.2.4, and DynamicWave.cpp, the finite volume kernels and the hydraulics manual from OpenSWMM 6. It built all three engines, wrote the SWMM5 version of Example 1, chose the SWMM6 options and meshes to run, designed the one-change experiments and made 45 changed copies of the SWMM 4.4H build and one of SWMM 5.2.4 for them, chose which changes to keep in the improved ZROUTE and which to drop, ran the 1,157 simulations, wrote the scripts that parse the outputs, wrote the app, the charts and diagrams, this essay, the .docx and the .md file. The review. Version 2.4 answers a written review of version 2.3 that Bob Dickinson supplied. Going by the link it carries, the review was produced with ChatGPT, OpenAI's AI model. Its author exercised the app's JavaScript and recalculated the embedded statistics; it did not rerun the engines, and said so. Claude checked each finding against the code and the data, found that each one held, and made the corrections. No finding was accepted on the review's word alone. How the results were checked. The checks are mechanical: engine runs, file comparisons, and scripts that read numbers out of engine output. The source findings are the AI's reading of the code at the lines cited. The independent mass balance is another script of Claude's, not a person's check. No person has yet rerun the engines, checked the thirty Register items against the source, or reviewed the SWMM5 conversion of Example 1. Neither the OpenSWMM authors nor EPA have seen these results.

## Changes

`2.4.0 (2026-11-13)`: corrections after an outside review of 2.3.0; no new engine runs. Fixed: CSV export wrote unquoted commas (18 of 54 summary rows had 9 fields under 8 headings; the series header had 13 names over 10 columns), now two quoted rectangular tables with a run_status column. Fixed: the Terms calculator floored a negative previous area at 0.01 ft2 without saying so; the floor is gone and an impossible state suspends the comparison. Restated: "matching XROUTE's continuity on 50 of 53 decks" becomes aggregate statistics on the 50 non-steep decks, with all 53 and deck-by-deck counts shown (XROUTE median corrected from 0.49 to 0.50, which is 0.495 rounded). Corrected: the finite volume hydraulic flux is HLL, not HLLC; the reversal rule limits a reversed flow to 0.001 with the new sign and the four solvers compare different pairs of flows; the surcharge formula is labeled as an idealized case; "true mid depth" becomes "uncapped mid depth"; Register 8 is described as measured everywhere. Added: off-scale markers on clipped charts, failed runs flagged and left out of the summary ranges, an independent mass balance on 60 Example 1 runs, manifest.csv and the raw reports. The count of changed SWMM 4.4H build copies is corrected from 44 to 45: the version 2.2 set is nineteen copies, not eighteen. Run count unchanged at 1,157.

`2.3.0 (2026-11-13)`: ZROUTE deep dive. Nine more Register items (22 to 30); item 4 moved from read to measured; items 5, 9, 14 and 16 annotated. Eleven changes tested alone and together as "ZROUTE improved" on Example 1 at six time steps and on 53 example decks. Two more figures, new cards on the Why ZROUTE tab, a Doc section. Runs 184 to 1,157.

`2.2.0 (2026-11-13)`: answered why ZROUTE is different with 48 runs of one-change build copies. Added the Why ZROUTE tab, three figures (conduit 1602 profile, slot-width sweep, one-change ladder), a Doc section, Register items 20 and 21, and measured results for items 1 and 8. Item 8 moved from read to measured. Runs 136 to 184. Added a complexity grade at the end of the Doc. The one-sentence summary now leads with the crown cap.

`2.1.0 (2026-11-12)`: added the two OpenSWMM 6.0.0-alpha.4 solvers (expanded dynamic wave and finite volume) as three plotted configurations, a SWMM6 tab (parity with EPA 5.2.4, seven option sets, six meshes, one-pipe check), SWMM6 source rows and slot curves, and a ninth figure. Added Register items 11 to 19: six from a second pass through YROUTE and ZROUTE, three from the SWMM6 runs. Runs 48 to 136. Extended answer on YROUTE's denominator: the guard never fired, but the denominator went negative in an instrumented build.

`2.0.0 (2026-11-12)`: rebuilt as single-file HTML, dark by default. Replaced the invented transient with 48 runs of the compiled engines. Added the Time step, Surcharge, Register, About and Doc tabs, the .docx and this file. Corrected version 1: ZROUTE does have a surcharge treatment (a Preissmann slot), and the terms it saves on its first pass are the old-time terms of a time-weighted scheme, not stale values. Removed the claim that YROUTE's denominator form damps the flow.

`1.0 (2026)`: React component with a one-pipe momentum calculator, a made-up transient, surcharge curves, a genealogy diagram and a code comparison.

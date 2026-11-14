---
name: Inside the Network
file: inside-the-network-cfd.html
version: 1.1.0
date: 2026-11-12
author: Robert Dickinson
links: {netlify: not deployed yet, artifact: "https://claude.ai/artifact/L4nBLXcxovRfsQoCvf7Qed", repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4 plus the Dickinson KW/SF patch, extension off (modes 0/0)", build: "wasm32-wasi reactor, 853,130 bytes, sha256 e62aa56968febce741d56de2f6e73660ead09fa700bad5071117b962b4939918", license: public domain}
  - {name: netcfd, version: 1.1, source: written for this app (inline in the HTML), license: same as the app}
  - {name: browser_wasi_shim, version: 0.4.2, source: bjorn3, license: MIT or Apache-2.0}
models:
  - {file: EXAM1_no_adverse_slopes_SW5.INP, role: "EXTRAN Example 1: basic pipe system", change: "REPORT_STEP set to 00:01:00"}
  - {file: EXAM2_WITH_TIDE_SW5.inp, role: "EXTRAN Example 2: tide gate at the outfall", change: "REPORT_STEP set to 00:01:00"}
  - {file: EXAM7_with_pump3_SW5.INP, role: "EXTRAN Example 7: pump station at 16109", change: "REPORT_STEP set to 00:01:00"}
  - {file: EXAM80a.INP, role: "EXTRAN Example 80: flow through constricting pipes", change: "REPORT_STEP set to 00:01:00"}
units: US customary (ft, s, cfs); g = 32.174 ft/s2
ai_use: built with Claude (Anthropic); see AI use
---

# Inside the Network: a free-surface CFD along a path of a SWMM5 network, run beside EPA SWMM 5.2.4

## What it does

It runs two models of one sewer in the browser and shows where they differ. One is a 2D vertical-slice (x along the sewer, z up) free-surface CFD solver that moves particles of water through chambers and box conduits. The other is EPA SWMM 5.2.4.

There are two kinds of model. (a) Four EXTRAN manual examples supplied by Bob Dickinson as SWMM5 files. SWMM5 runs each whole file; the CFD follows one path of conduits from the top of a branch to the outfall, with lengths compressed 100, 50 or 25 to 1 (a distorted model) and everything that joins or leaves the path taken from the SWMM5 results. (b) A 150 ft section built for the app, run at true scale, with a SWMM5 twin .inp written from the same table.

Output: an animated long section with the SWMM5 line overlaid, node-depth and conduit-flow time series for both models, the grade line at any time, a plateau comparison table, CSV, and the .inp. It is for people who use SWMM5 and want to see a second, different kind of solver on the same network. It is a demonstration, not a design tool.

## How it computes

CFD (netcfd 1.1), true scale:

1. Equations: width-averaged incompressible Navier-Stokes in the x-z plane with a free surface at p = 0. Continuity du/dx + dw/dz = 0. Momentum Du/Dt = -(1/rho) dp/dx + d/dz(nu_t du/dz) - (2/B) Cs |V| u, and the same for w with -g.
2. Discretization: PIC/FLIP. Particles (4 per cell at rest) carry velocity; a staggered MAC grid carries u and w on faces and p at centres. FLIP ratio 0.99 (1 % PIC).
3. Step order: particles to grid (bilinear), mark wet cells, gravity and wall forces on the grid, pressure projection, grid to particles, then particles advected through the projected grid field with the midpoint rule. Step size dt = min(0.02 s, 0.8 h / vmax).
4. Walls: cut cells. A signed distance to the wall is stored at grid nodes; each face keeps its open fraction; the pressure equation is the area-weighted (variational) form of Batty, Bertails and Bridson (2007). Particles that cross a wall are pushed back along the distance gradient and lose their normal velocity.
5. Free surface: a cell is wet when its fill fraction f (splatted particle density over the density a full cell would read) is at least 0.5. The surface position inside the cell comes from f through the tent-kernel relation d = 1 - sqrt(2(1 - f)), and the pressure boundary is applied there (ghost-fluid, second order). Projected velocities are extrapolated two faces into the air.
6. Pressure solve: conjugate gradients with a modified incomplete Cholesky MIC(0) preconditioner, warm start, tolerance 2e-4 ft/s on the residual, 400 iterations maximum.
7. Volume control: a divergence term proportional to (f - 1) with a relaxation time of max(20 dt, 0.15 s), two-sided in buried cells, one-sided at the surface.
8. Wall shear: rough-wall log law u_tau = kappa u_t / ln(30 y / ks), kappa = 0.41, applied implicitly to the first layer of faces within one cell of a wall; y is taken as 0.6 of the layer thickness because the face value is a tent-kernel average.
9. Roughness: ks = 11 R / exp(kappa 1.486 R^(1/6) / (n sqrt(g))) with R the conduit's full-flow hydraulic radius, so the log law carries the same velocity as Manning at full flow. For n = 0.013, B = 4 ft, height 2 ft: ks = 0.00325 ft.
10. Turbulence: Prandtl mixing length, nu_t = lm^2 |du/dz + dw/dx|, lm = min(kappa d_wall, 0.09 H), capped at 0.15 h^2/dt.
11. Side walls (width averaging): drag -(2/B) Cs |V| V with Cs = (kappa / ln(11 (B/2) / ks))^2.
12. Inflows: node inflows are volume sources. MH1 wells up from the floor with no momentum; the MH3 lateral falls from a stub 2.6 ft above the invert.
13. Outfall: FREE deletes particles that leave the conduit end. FIXED holds a reservoir at the stage through a prescribed hydrostatic pressure on the reservoir cells, and both models start with still water at the stage (SWMM5 through the storage InitDepth).
14. Measures: chamber depth = median over the chamber's columns of the height of the water standing on the floor (surface placed inside its cell from the fill fraction); particle volume / plan area is also recorded and exported. Conduit flow = particles crossing the mid-length section, smoothed over about 1 s. Grade line = free surface where part full, piezometric head at the invert where full; smoothed over 0.4 s.

CFD at compressed scale (opt.distort = lambda, used for the EXTRAN examples). Items 1 to 7 above still hold; 8 to 11 are switched off and replaced:

15. Scaling: conduit length L' = L / lambda, time t' = t / lambda, bed slope S' = lambda S. Heights, depths, velocities and flows are unscaled. Under x -> x / lambda, t -> t / lambda the Saint-Venant momentum equation du/dt + u du/dx + g dh/dx = g (S0 - Sf) is unchanged if S0 and Sf are both multiplied by lambda. Volumes scale by 1 / lambda.
16. Friction: a body drag on every wet face in a conduit column, du/dt = -K |V| u, K = lambda g n^2 / (2.208 R^(4/3)), applied implicitly, with R the hydraulic radius of the real cross-section (CIRCULAR, TRIANGULAR, TRAPEZOIDAL, rectangular) at the column's current depth (D/4 for a circular pipe at or above 0.96 D).
17. Slice width varies along x. Each conduit is a box with the real height and width B = area / depth: pi D / 4 for a circular pipe (full area), area at the SWMM5 peak depth over that depth for an open channel. The projection uses face areas weighted by B(x); particles have volume Bmin h^2 / 4.
18. Nodes: a base chamber 4 ft long, as high as the highest connected crown plus 0.5 ft, with a 2 ft wide riser to the rim. The rim is the lower of the file's rim and the SWMM5 peak head plus 5 ft. Water that passes the rim is removed and counted as flooding. Chambers are not compressed.
19. Inflows at each path node = SWMM5 lateral inflow at that node plus the signed flow of every link not on the path that touches it (conduits, pumps), read from the .out at one-minute steps and interpolated. Negative totals remove particles from the chamber floor.
20. Outfall: FREE or NORMAL as FREE. FIXED, TIDAL and TIMESERIES outfalls follow the outfall head SWMM5 reports through the fixed-stage boundary of item 13. Tide gates (flaps) are not modelled.
21. Measures at compressed scale: riser level read from the top down (highest cell with water in it and in the two cells below), median over the riser columns. Grade line averaged over 7 columns of the same conduit and 1.5 s of model time. Step size dt = min(0.03 s, 0.8 h / vmax).

SWMM5 for the EXTRAN examples: the file as supplied, with REPORT_STEP set to 00:01:00; run whole with the in-page engine; the first 4.5 h of the record are used.

SWMM5 twin of the short section (written by the app, run unmodified by the engine):

- [OPTIONS] FLOW_UNITS CFS, FLOW_ROUTING DYNWAVE, ROUTING_STEP 0.1, VARIABLE_STEP 0.75, MINIMUM_STEP 0.01, REPORT_STEP 00:00:01, INERTIAL_DAMPING PARTIAL, NORMAL_FLOW_LIMITED BOTH, SURCHARGE_METHOD EXTRAN, END_TIME 00:01:40.
- [STORAGE] FUNCTIONAL 0 0 16 for each chamber (4 ft x 4 ft plan). [XSECTIONS] RECT_CLOSED 2 4. C1 outlet offset 3.05 ft.
- [LOSSES] is written only when Kentry or Kexit is above zero.
- Results are read from the binary .out (node depth and head, link flow and depth).

## Inputs and outputs

- Input, EXTRAN examples: example (1, 2, 7, 80), path (north or south branch for 1, 2 and 7), compression (100, 50, 25), grid (8 or 10 cells across the smallest conduit). The four .inp files are embedded in the page. No file is read from disk in this version.
- Input, short section: the section table on the Network tab (inverts, depths, lengths, heights, offsets, Manning n) and the sliders (base and peak inflow, lateral peak, outfall type and stage, cell size 0.25 / 0.20 / 0.15 ft, Kentry, Kexit).
- Output: the .inp as run (example file or twin), inside-the-network-run.csv (event time, inflow, CFD level, CFD volume over area and SWMM5 depth per node, CFD and SWMM5 flow per conduit, CFD water volume in real ft3), inside-the-network-tour.webm (recorded tour). Inside a claude.ai artifact each save asks the viewer first and the model is saved as .inp.txt, because the artifact frame does not allow the .inp extension.
- Example 1 paths: north 8040, 8060, 1602, 1600, 1630, 1030 (80408 to outfall 10208); south 8100, 8130, 1570, 1630, 1030 (81009 to outfall). Example 80: conduits 1 to 5.
- Short section: MH1 invert 112.00, MH2 108.60, MH3 107.90, MH4 107.80, outfall 107.65 ft. C1 35 ft at 1.0 %, C2 35 ft at 2.0 %, C3 50 ft at 0.2 %, C4 30 ft at 0.5 %. Storm: MH1 15 to 40 cfs, MH3 lateral 4 to 10 cfs, ramp 20 to 35 s, plateau to 60 s, back by 75 s, end 100 s.

## Checks

All mechanical, run in Node 22 on 2026-11-12 with the solver file that is inline in the HTML.

| Check | Reference | Result |
|---|---|---|
| Still water 20 s, 0.2 ft cells, fill 103.30 ft | zero motion, head = level | rms speed 0.012 ft/s, fastest particle 0.35 ft/s, head error 0.005 ft |
| Still water 20 s, 0.2 ft cells, fill 101.30 ft | zero motion, head = level | rms speed 0.010 ft/s, fastest particle 0.25 ft/s, head error 0.001 ft |
| Still water 20 s, 0.125 ft cells, fill 101.25 ft | zero motion, head = level | rms speed 0.008 ft/s, fastest particle 0.22 ft/s, head error 0.000 ft |
| Still water 20 s, 0.2 ft cells, fill 103.30 ft (ghost-fluid off, for comparison) | zero motion, head = level | rms speed 0.016 ft/s, fastest particle 0.36 ft/s, head error 0.113 ft |
| Dam break, h0 = 2 ft, 0.2 ft cells, t = 1 s | Ritter depth at dam 0.889 ft | 0.950 ft (+6.9 %), mean abs error over the fan 0.054 ft |
| Dam break, h0 = 2 ft, 0.1 ft cells, t = 1 s | Ritter depth at dam 0.889 ft | 0.900 ft (+1.3 %), mean abs error over the fan 0.047 ft |
| Uniform flow 40 cfs, S = 0.02, n = 0.013, 0.2 ft cells, 160 ft reach, read at 136 ft | Manning normal depth 0.866 ft (4 ft wide rectangle) | 0.882 ft (+1.9 %), 4.4 cells deep |
| Uniform flow 25 cfs, S = 0.01, n = 0.013, 0.2 ft cells, 160 ft reach, read at 136 ft | Manning normal depth 0.796 ft (4 ft wide rectangle) | 0.812 ft (+2.0 %), 4.1 cells deep |
| Uniform flow 60 cfs, S = 0.01, n = 0.013, 0.2 ft cells, 160 ft reach, read at 136 ft | Manning normal depth 1.467 ft (4 ft wide rectangle) | 1.489 ft (+1.5 %), 7.4 cells deep |
| Uniform flow 40 cfs, S = 0.02, n = 0.02, 0.2 ft cells, 160 ft reach, read at 136 ft | Manning normal depth 1.167 ft (4 ft wide rectangle) | 1.153 ft (-1.1 %), 5.8 cells deep |
| Uniform flow 40 cfs, S = 0.02, n = 0.013, 0.125 ft cells, 160 ft reach, read at 136 ft | Manning normal depth 0.866 ft (4 ft wide rectangle) | 0.893 ft (+3.2 %), 7.1 cells deep |
| Compressed 50 to 1: uniform flow 30 cfs, 5 ft circular pipe as a 3.93 ft box, n = 0.034, real S = 0.0019, 0.5 ft cells | Manning on the box with the circle's hydraulic radius: 3.167 ft (true circular normal depth 3.056 ft) | 3.248 ft (+2.6 %), 6.5 cells deep |
| Compressed 50 to 1: uniform flow 15 cfs, 5 ft circular pipe as a 3.93 ft box, n = 0.034, real S = 0.0019, 0.5 ft cells | Manning on the box with the circle's hydraulic radius: 1.943 ft (true circular normal depth 2.028 ft) | 2.024 ft (+4.2 %), 4.0 cells deep |
| Compressed 50 to 1: uniform flow 30 cfs, 5 ft circular pipe as a 3.93 ft box, n = 0.034, real S = 0.0019, 0.4 ft cells | Manning on the box with the circle's hydraulic radius: 3.167 ft (true circular normal depth 3.056 ft) | 3.242 ft (+2.4 %), 8.1 cells deep |
| Compressed 50 to 1: still water in two shafts and two sloping full pipes, 20 s | all heads = 112.00 ft | shafts 112.01 and 112.04 ft; pipe grade line 111.66 to 111.98 ft |
| Compressed 50 to 1: 32 cfs through two full 4 ft pipes, 2000 ft each, n = 0.015, shaft to shaft to fixed-stage outfall | Manning 1.32 ft per pipe; velocity head 0.10 ft | 1.63 ft shaft to shaft, 1.65 ft shaft to outfall stage |
| Compressed 50 to 1: 45 cfs through two full 4 ft pipes, 2000 ft each, n = 0.015, shaft to shaft to fixed-stage outfall | Manning 2.61 ft per pipe; velocity head 0.20 ft | 3.09 ft shaft to shaft, 2.97 ft shaft to outfall stage |
| Hydraulic jump, 40 cfs, level bed, tailwater 2.2 ft, 0.2 ft cells | Belanger sequent depth 2.267 ft from y1 = 0.873 ft, Fr1 = 2.16 | 2.181 ft (-3.8 %); toe 3.2 ft past the slope break |
| Fixed-stage outfall passing 40 cfs, stage 2.0 ft above invert | depth near exit = stage | 2.16 ft (+0.16 ft) |
| Fixed-stage outfall passing 40 cfs, stage 2.6 ft above invert | depth near exit = stage | 2.73 ft (+0.13 ft) |
| Same input twice (demo, 0.25 ft cells, 12 s) | identical particle positions | identical, sha256 prefix e76878c0c3ed2786:3649 |
| Volume, demo storm, 0.2 ft cells | in - out - stored = 0 | residual 0.00 ft3 of 3140 ft3 in; packing (particle volume / wet area) 1.003 to 1.047 |
| WASM engine vs native EPA engine (swmm-toolkit 0.17.0, EPA SWMM 5.2 (Build 5.2.4)) | byte-identical .out | 3 of 3 twin models identical, 27263 bytes each (free outfall; free with Kentry 0.5 and Kexit 1.0; fixed stage 109.4 ft) |
| WASM engine vs native engine, EXAM1_no_adverse_slopes_SW5.INP | byte-identical .out | identical over the 479 records both wrote; WASM 479 records, native 480 (see note); routing continuity 0.02 % |
| WASM engine vs native engine, EXAM2_WITH_TIDE_SW5.inp | byte-identical .out | identical over the 479 records both wrote; WASM 479 records, native 480 (see note); routing continuity 0.733 % |
| WASM engine vs native engine, EXAM7_with_pump3_SW5.INP | byte-identical .out | identical over the 479 records both wrote; WASM 479 records, native 480 (see note); routing continuity 0.124 % |
| WASM engine vs native engine, EXAM80a.INP | byte-identical .out | identical, 112811 bytes; routing continuity -0.001 % |
| In-page .out reader vs EPA output API | equal values | 3600 values (node depth, node head, link flow, link depth; 2 models), 0 different |

Note on the one-record difference. The three files that differ start 01/01/1988 and end at 08:00. Stock EPA SWMM 5.2.4 computes the run length in project.c as `TotalDuration = floor((EndDateTime - StartDateTime) * SECperDAY);`. In double precision that product is 28799.999999895 for this date and hour, so TotalDuration is 28799 s and the run stops one report short. The native reference is the OWA fork inside swmm-toolkit, which subtracts dates and times separately and gets 28800. The WASM build follows stock EPA. EXAM80a ends at 06:00 (exact in binary) and is byte-identical. Only the first 4 h are used by the CFD.

EXTRAN examples, complete 4 h CFD runs at 50 to 1, 8 cells across the smallest conduit, against SWMM5 on the unmodified file. Plateau means (2:00 to 2:45 of the event; Example 80 uses 2:15 to 3:00). These are comparisons, not gates; no pass mark was set.

EXTRAN Example 1: basic pipe system, North branch: 80408 to the outfall (0.5 ft cells, up to 30400 particles, 10187 steps, packing 1.01 to 1.03):

| Node | CFD depth, ft | SWMM5 depth, ft | CFD minus SWMM5, ft |
|---|---|---|---|
| 80408 | 13.37 | 12.75 | +0.61 |
| 80608 | 16.72 | 16.70 | +0.02 |
| 82309 | 21.39 | 21.33 | +0.06 |
| 16109 | 2.69 | 2.96 | -0.27 |
| 16009 | 3.18 | 2.94 | +0.24 |
| 10309 | 2.71 | 2.75 | -0.04 |

| Conduit | CFD flow, cfs | SWMM5 flow, cfs |
|---|---|---|
| 8040 | 43.8 | 45.0 |
| 8060 | 32.2 | 32.0 |
| 1602 | 72.2 | 72.0 |
| 1600 | 72.2 | 72.0 |
| 1630 | 122.2 | 122.0 |
| 1030 | 122.2 | 122.0 |

Water over the rim, whole event: CFD 102622 ft3, SWMM5 114210 ft3.

EXTRAN Example 1: basic pipe system, South branch: 81009 to the outfall (0.5 ft cells, up to 23862 particles, 9995 steps, packing 1.01 to 1.05):

| Node | CFD depth, ft | SWMM5 depth, ft | CFD minus SWMM5, ft |
|---|---|---|---|
| 81009 | 3.17 | 2.27 | +0.90 |
| 81309 | 2.84 | 3.15 | -0.31 |
| 15009 | 2.23 | 2.11 | +0.12 |
| 16009 | 3.34 | 2.94 | +0.40 |
| 10309 | 2.70 | 2.75 | -0.06 |

| Conduit | CFD flow, cfs | SWMM5 flow, cfs |
|---|---|---|
| 8100 | 50.0 | 50.0 |
| 8130 | 50.0 | 49.9 |
| 1570 | 50.0 | 50.0 |
| 1630 | 121.9 | 122.0 |
| 1030 | 121.9 | 122.0 |

Water over the rim, whole event: CFD 0 ft3, SWMM5 0 ft3.

EXTRAN Example 2: tide gate at the outfall, North branch: 80408 to the outfall (0.5 ft cells, up to 35091 particles, 10714 steps, packing 1.01 to 1.05):

| Node | CFD depth, ft | SWMM5 depth, ft | CFD minus SWMM5, ft |
|---|---|---|---|
| 80408 | 13.34 | 12.75 | +0.59 |
| 80608 | 16.73 | 16.70 | +0.03 |
| 82309 | 21.31 | 21.39 | -0.07 |
| 16109 | 2.94 | 2.87 | +0.07 |
| 16009 | 3.48 | 2.58 | +0.90 |
| 10309 | 0.82 | 1.76 | -0.94 |

| Conduit | CFD flow, cfs | SWMM5 flow, cfs |
|---|---|---|
| 8040 | 43.7 | 45.0 |
| 8060 | 32.2 | 31.3 |
| 1602 | 72.1 | 71.3 |
| 1600 | 72.1 | 71.3 |
| 1630 | 122.2 | 121.4 |
| 1030 | 122.1 | 121.4 |

Water over the rim, whole event: CFD 103515 ft3, SWMM5 120910 ft3.

EXTRAN Example 2: tide gate at the outfall, South branch: 81009 to the outfall (0.5 ft cells, up to 28198 particles, 10396 steps, packing 1.01 to 1.08):

| Node | CFD depth, ft | SWMM5 depth, ft | CFD minus SWMM5, ft |
|---|---|---|---|
| 81009 | 3.23 | 2.62 | +0.61 |
| 81309 | 2.80 | 2.99 | -0.19 |
| 15009 | 2.26 | 2.44 | -0.18 |
| 16009 | 3.56 | 2.58 | +0.98 |
| 10309 | 0.82 | 1.76 | -0.94 |

| Conduit | CFD flow, cfs | SWMM5 flow, cfs |
|---|---|---|
| 8100 | 50.0 | 50.0 |
| 8130 | 50.0 | 50.0 |
| 1570 | 50.0 | 50.0 |
| 1630 | 121.3 | 121.4 |
| 1030 | 121.3 | 121.4 |

Water over the rim, whole event: CFD 0 ft3, SWMM5 0 ft3.

EXTRAN Example 7: pump station at 16109, North branch: 80408 to the outfall (0.5 ft cells, up to 30322 particles, 10181 steps, packing 1.01 to 1.02):

| Node | CFD depth, ft | SWMM5 depth, ft | CFD minus SWMM5, ft |
|---|---|---|---|
| 80408 | 13.39 | 12.75 | +0.63 |
| 80608 | 16.72 | 16.70 | +0.02 |
| 82309 | 21.37 | 21.63 | -0.25 |
| 16109 | 2.44 | 2.50 | -0.07 |
| 16009 | 3.36 | 2.87 | +0.49 |
| 10309 | 2.71 | 2.72 | -0.01 |

| Conduit | CFD flow, cfs | SWMM5 flow, cfs |
|---|---|---|
| 8040 | 43.8 | 45.0 |
| 8060 | 32.4 | 28.3 |
| 1602 | 72.4 | 68.3 |
| 1600 | 53.0 | 49.0 |
| 1630 | 122.4 | 118.3 |
| 1030 | 122.4 | 118.4 |

Water over the rim, whole event: CFD 100904 ft3, SWMM5 148270 ft3.

EXTRAN Example 7: pump station at 16109, South branch: 81009 to the outfall (0.5 ft cells, up to 24840 particles, 10024 steps, packing 1.01 to 1.04):

| Node | CFD depth, ft | SWMM5 depth, ft | CFD minus SWMM5, ft |
|---|---|---|---|
| 81009 | 3.18 | 2.62 | +0.56 |
| 81309 | 2.84 | 2.80 | +0.04 |
| 15009 | 3.21 | 2.99 | +0.22 |
| 16009 | 3.13 | 2.87 | +0.26 |
| 10309 | 2.68 | 2.72 | -0.03 |

| Conduit | CFD flow, cfs | SWMM5 flow, cfs |
|---|---|---|
| 8100 | 50.0 | 50.0 |
| 8130 | 50.0 | 50.0 |
| 1570 | 69.3 | 69.3 |
| 1630 | 118.3 | 118.3 |
| 1030 | 118.3 | 118.4 |

Water over the rim, whole event: CFD 0 ft3, SWMM5 0 ft3.

EXTRAN Example 80: flow through constricting pipes, Node 1 to the outfall (0.375 ft cells, up to 62989 particles, 9810 steps, packing 0.99 to 1.02):

| Node | CFD depth, ft | SWMM5 depth, ft | CFD minus SWMM5, ft |
|---|---|---|---|
| 1 | 9.53 | 11.03 | -1.51 |
| 2 | 10.07 | 11.53 | -1.46 |
| 3 | 5.28 | 5.60 | -0.32 |
| 4 | 5.84 | 6.08 | -0.24 |
| 5 | 1.51 | 2.30 | -0.79 |

| Conduit | CFD flow, cfs | SWMM5 flow, cfs |
|---|---|---|
| 1 | 36.3 | 37.2 |
| 2 | 32.6 | 34.7 |
| 3 | 30.3 | 32.2 |
| 4 | 28.1 | 29.5 |
| 5 | 27.8 | 29.3 |

Water over the rim, whole event: CFD 0 ft3, SWMM5 0 ft3.

Rising limb, Example 1 north: node 82309 first reached 18 ft at 0:39 (h:mm) in SWMM5 and 0:44 in the CFD.

Files supplied and not used: EXAM1_SW5.inp (ERROR 361, needs ../DataFiles/v15_time_series_file.dat, not supplied); EXAM2_WITH_Fixed_Stage.inp (all inflows zero, no [INFLOWS]; routing continuity -99.965 %); exam1_negative_flow_examples.inp (routing continuity -17.407 %).

Short section result, plateau means 45 to 60 s, 0.2 ft cells, SWMM5 with no losses:

| Chamber | CFD level, ft | CFD volume / area, ft | SWMM5 depth, ft | Level minus SWMM5, ft | SWMM5 with Kentry 0.5, Kexit 1.0, ft |
|---|---|---|---|---|---|
| MH1 | 2.35 | 2.33 | 1.06 | +1.29 | 1.92 |
| MH2 | 1.82 | 2.36 | 1.48 | +0.34 | 2.58 |
| MH3 | 2.06 | 2.14 | 2.21 | -0.15 | 2.66 |
| MH4 | 1.60 | 1.61 | 1.80 | -0.19 | 1.97 |

| Conduit | CFD flow, cfs | SWMM5 flow, cfs |
|---|---|---|
| C1 | 40.0 | 41.7 |
| C2 | 39.9 | 43.7 |
| C3 | 49.8 | 54.6 |
| C4 | 47.6 | 46.7 |

SWMM5 is not steady over this window (MH1 falls from 1.36 ft toward 1.0 ft at constant inflow; routing continuity error -1.4 %). Critical depth for 40 cfs in a 4 ft box is 1.46 ft; specific energy at critical is 2.19 ft. Human review: none yet (see AI use).

## What this does not show

1. L-1 Two dimensions. Conduits are boxes of the real height and the real full area; chambers are rectangular. No true pipe shape, benching, bends or plan-view junction effects. Surface width, and so part-full storage, is wrong for circular pipes.
2. L-2 Air has no pressure. Trapped pockets fill; no air cushion, no geysering.
3. L-3 Thin water. Below about three cells of depth the answer drifts. Not gated below 4.0 cells. The start and end of every EXTRAN storm are thinner.
4. L-4 Turbulence at true scale is a mixing length with a log-law wall. No air entrainment, no surface tension. At compressed scale there is no wall law; friction is a body force.
5. L-5 Inflows carry no momentum. At compressed scale every side branch and the Example 7 pump enter or leave at the SWMM5 rate, so the CFD cannot disagree with SWMM5 about them.
6. L-6 Particle noise: about a quarter cell on a free surface; in a full conduit at compressed scale, pressure noise of a foot or more, averaged as in item 21.
7. L-7 No measured data anywhere. Checks are against analytical solutions and against SWMM5.
8. L-8 The .out reader is a minimal one written for this page, not the shared swmm-results-parser library. Replace it when the app is next opened.
9. L-9 No .inp loading. Four examples with fixed paths are built in.
10. L-10 The fixed-stage outfall holds the level 0.13 to 0.16 ft above the stage while 40 cfs leaves through it (true scale). Example 2's tide uses the same boundary; the flap gate is not modelled.
11. L-11 The jump gate was read with the toe 3.2 ft past the slope break, so y1 was taken at the break itself. A jump held well down the level reach has not been gated.
12. L-12 Engine parity covers seven DYNWAVE models (three twins, four examples).
13. L-13 Run without failure but compared with no reference: at true scale, the Draft and Fine grids, the Big storm, Low flow and Drowned outfall presets and the slider extremes. At compressed scale: Example 1, north branch, was also run at 100 to 1 for the whole event (levels over 2:00 to 2:45 within 0.30 ft of the standard run, largest at 16109), at 25 to 1 as far as 1:02 of the event (levels over 0:52 to 1:02 within 0.24 ft of the standard run, largest at 82309), at 50 to 1 on the fine grid as far as 1:20 of the event (levels over 1:10 to 1:20 within 0.05 ft of the standard run, largest at 16109). No other path was run at those settings. Not run at all: browsers other than Chromium.
14. L-14 Grade line in a full conduit is read from pressure near the invert. Version 1.0 misread it in surcharged conduits (see Changes).
15. L-15 Compressed lengths. Saint-Venant quantities carry over (item 15). Vertical accelerations, surface curvature at structures, jump lengths and anything depending on the true slope do not. Compressed slopes reach about 124 % (Example 2 outfall line at 50 to 1), far outside the small-slope assumption behind the friction term.
16. L-16 Chambers are not compressed. Scaled back, a riser stores what a shaft of 310 to 940 ft2 would, against 12.57 ft2 for a SWMM5 junction.
17. L-17 The CFD has a wetting front and fills later than SWMM5 on the rising limb. Which is closer to a real sewer has not been tested.
18. L-18 Inlet and outlet offsets are honoured; conduits traversed against their file direction are flipped. Initial depths, ponding and minor-loss columns of the example files are not used by the CFD.

## How to reproduce

1. Open inside-the-network-cfd.html. The default is EXTRAN Example 1, north branch, 50 to 1, standard grid. Let it run to 4:00:00 of the event (a few minutes), open Compare, read the plateau table.
2. Verify tab: the three Rerun buttons repeat the still-water gate, the dam-break gate and the engine null test (same .inp twice; [LOSSES] with K = 0 against no [LOSSES]) in the browser.
3. For native numbers: press .inp to save the example file as run, run it with EPA SWMM 5.2.4, and compare the .out with the SWMM5 columns of the CSV.

## Credits and licenses

- EPA SWMM 5: Lewis Rossman and the U.S. EPA, public domain. KW/SF extension build and app direction: Robert Dickinson.
- EXTRAN and its example problems: Roesner, Aldrich and Dickinson, SWMM 4 User's Manual, EXTRAN Addendum (U.S. EPA, 1988), after Shubinski and Roesner (Water Resources Engineers). SWMM5 versions of the example files supplied by Robert Dickinson.
- Distorted-scale modelling: standard hydraulic laboratory practice (for example the U.S. Army Corps of Engineers Mississippi Basin Model, horizontal 1:2000, vertical 1:100).
- browser_wasi_shim 0.4.2: bjorn3, MIT or Apache-2.0.
- Methods: Harlow (1955) and Harlow and Welch (1965), particle-in-cell and marker-and-cell; Brackbill and Ruppel (1986), FLIP; Zhu and Bridson (2005); Batty, Bertails and Bridson (2007), cut-cell pressure solve; Enright and others (2003), ghost-fluid free surface; Hestenes and Stiefel (1952), conjugate gradients; Prandtl (1925), mixing length; Nikuradse (1933) and Keulegan (1938), rough-wall log law.
- References for the gates: Ritter (1892), Belanger (1838), Manning (1891).

## AI use

This app was built with Claude, Anthropic's AI model, in November 2026, at the direction of Robert (Bob) Dickinson. He asked for a CFD water simulation of a SWMM5 network, then supplied seven EXTRAN example files, chose the compressed whole-path approach over true-scale windows, and chose which files to use. He is responsible for publishing it. Claude chose the numerical method, wrote the CFD solver and its compressed-scale extension, the code that builds a CFD section from an example file and its SWMM5 results, the SWMM5 twin generator, the results reader, the page, the Doc-tab essay, the .docx and this file, designed the gates and ran them. It did not write the SWMM5 engine, the WASI shim or the example files. The checks listed above are mechanical. No person has yet reviewed the solver code or the essay, rerun the gates independently, or compared any of it with measured data.

## Changes

1.1.0 (2026-11-12): the demo models are now four EXTRAN manual examples at compressed scale (netcfd 1.1: variable slice width, body friction, risers, sinks, time-varying tail stage). The short true-scale section stays as a second group of presets. Two measurement faults found while testing surcharged runs and fixed; neither changes the water, only what is read from it. (a) Grade line in a surcharged conduit. Version 1.0 decided a column was full from the particle count alone, `if (colOwner[i] > 0 && dv >= 0.985 * (colRoof[i] - colFloor[i]))`, and otherwise reported `hg = colFloor[i] + dv`; a full column whose count dipped under 98.5 % was therefore read as crown level, and the time-averaged line sagged toward the crown. Now the piezometric head near the invert is used whenever it stands above the crown. (b) Level in a tall shaft was read upward from the floor and stopped at the first thin cell, `while (jj2 < nz - 1 && type[i + jj2 * nx] === 1) { jt = jj2; jj2++; }`, which under-read surcharged shafts by feet during development of 1.1; risers are now read from the top down. The true-scale gates were rerun on the 1.1 solver and reproduce the 1.0 values, including the determinism hash.

1.0.0 (2026-11-11): first build.

---
name: The Rational Limit
file: rational-limit.html
version: 1.1
date: 2026-11-20
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/W8t35onrYF3yFgRgroyGZz", netlify: "https://the-rational-limit.netlify.app", repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4, USEPA/Stormwater-Management-Model", build: "cmake Release, -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0", license: public domain, role: reference engine run outside the page}
  - {name: in-page solvers, version: 1.1, source: src/model.js, role: shallow-water FV, exact kinematic wave, SWMM nonlinear reservoir port}
units: US customary (ft, in/hr, min, cfs, acres)
complexity: {index: 56.8, shipped_html: 49.7, analyzer: 1.7.0, baseline: HC-2026-11-10-h, scale: HydroCouple org = 100}
ai_use: built with Claude (Anthropic); see AI use
---

# The Rational Limit: Q = CiA as the steady state of overland flow

**In one sentence.** Three overland-flow models on one plane all settle on Q = (i − f)A once the rain outlasts the time of concentration, and EPA SWMM 5.2.4 lands on it within 0.004% in all 9 equilibrium runs.

**In one paragraph.** The Rational Limit puts one rectangular plane in the rain and solves it three ways: the full one-dimensional shallow-water equations, the exact kinematic wave, and the nonlinear reservoir EPA SWMM uses for every subcatchment. Hold the rain past the time of concentration and all three settle on Q = (i − f)A, which is the rational formula with C = 1 − f/i. They disagree about how long that takes. 11 EPA SWMM 5.2.4 runs confirmed the plateau within 0.004% in every equilibrium case and confirmed that a storm shorter than tc never reaches it. The limit is exact. What it does not settle is whether a real catchment reaches equilibrium in a design storm, or which storm to use when the ground absorbs part of the rain.

## What it does

Tests the claim that the rational method is the equilibrium limit of overland flow, not a rival to simulation. One rectangular plane (length L, width W, slope S0, Manning n), constant rain i for duration D, constant loss f. Three solvers run live in the page; a dashed line marks Q = (i - f)A. Tabs: The collapse, Derivation, Why D = tc, Engine check, Research (24 sources), Where it stops, About, Doc.

## How it computes

- Steady state: dh/dt = 0 gives d(uh)/dx = i - f, so q(L) = (i - f)L and Q = (i - f)LW = CiA with C = 1 - f/i. Momentum does not enter.
- Kinematic wave: q = alpha h^(5/3), alpha = 1.49 sqrt(S0)/n. Exact solution by characteristics, celerity (5/3) alpha h^(2/3). tc = [L / (alpha (i - f)^(2/3))]^(3/5); rising limb q(L,t) = alpha ((i - f) t)^(5/3) for t < tc; partial-equilibrium peak (D/tc)^(5/3)(i - f)A for D < tc. 95% of plateau at tc * 0.95^0.6.
- Shallow water: 1D St Venant with rain source, finite volume, HLL fluxes, wall at divide, transmissive outlet, Manning friction solved implicitly (q + dt c q|q| = q*), outflow reported as interval average.
- SWMM reservoir: dd/dt = (i - f) - (alpha/L)(d - ds)^(5/3), Q = W alpha (d - ds)^(5/3), RK4 at 1 s. Constants from EPA SWMM 5.2.4 src/solver/subcatch.c: MCOEFF = 1.49 (line 52), MEXP = 1.6666667 (line 53), alpha (line 406), runoff (line 1029).
- Reservoir time scale h_eq/(i - f) = tc exactly; dimensionless dD/dtau = 1 - D^(5/3) gives 95% at tau95 = 2.3633 tc on any impervious plane.
- Storm choice: IDF i(D) = a/(D + b)^c (illustrative, default a = 100, b = 10, c = 0.85, in/hr with D in min). Peak(D) = alpha((i(D) - f) D)^(5/3) W for D < tc(i(D)), else (i(D) - f)A. Critical duration by log scan plus golden-section search.

## Inputs and outputs

- Inputs: sliders and presets on The collapse tab; IDF parameters on Why D = tc.
- Outputs: hydrograph CSV (SWE, kinematic, SWMM reservoir, CiA), peak-vs-duration CSV, an EPA SWMM 5 .inp for the current plane ([OPTIONS] KINWAVE, CFS; one subcatchment to one outfall; INTENSITY rain gage at 1-min steps; HORTON with f0 = fc for a constant loss; [Polygons] as the plane rectangle), a captioned GIF, this .md, the Doc as .docx.

## Checks

43 mechanical checks in test/verify.js, 0 failing, run on this build. Key results:

- Plateau: every EPA SWMM 5.2.4 run that holds rain past tc (9 of 11) settles on 1.000037 x (i - f)A; the excess equals SWMM's acre constant ratio (1/43560)/2.2956e-5 within 1e-5.
- Pervious, f = 0.5 in/hr: C = 0.750 at 2 in/hr, 0.875 at 4 in/hr (SWMM 5.2.4).
- Partial equilibrium (paved lot, tc 5.470 min): SWMM peak 0.5427 iA at D = 5 min (kinematic 0.8609), 0.8815 at D = 10 min.
- Reservoir clock: SWMM t95/tc = 2.363 to 2.378 on eight runs without depression storage; theory 2.3633. Depression storage 0.1 in at 2 in/hr adds 3.00 min (15.93 vs 12.93).
- App reservoir port vs SWMM: max difference 0.132% of iA over every 1-min step of every case.
- Shallow water, paved lot (kF2 131.6): t95 5.375 min (Richardson, 50-400 cells) vs kinematic 5.304, +1.33%; friction 98.77% of g S0 at equilibrium, pressure 0.44%, convective 0.23%.
- Shallow water, flat rough plane (S 0.1%, n 0.05, L 300 ft, kF2 3.77): t95 35.36 min (50-800 cells) vs kinematic 27.80, +27.2%; outlet at end equals (i - f)A to 1e-10.
- Kinematic: exact vs 400-cell upwind max 0.74% of iA; exact tc vs 0.94 formula 0.23%; volume returned 1.000000 of rain.
- Storm choice, 600 ft grass plane (S 0.5%, n 0.15), f = 1.5 in/hr: critical 31.40 min, 10.072 cfs; D = tc 75.98 min, 5.338 cfs (47.0% low). Impervious lot: critical = tc = 2.716 min.
- Controls: C1 rerun .out byte-identical (true); shipped page carries src/model.js byte for byte; its .inp export reproduces cases C1, C4, C8 exactly in SWMM 5.2.4 (test/bundle.js).
- Complexity: 56.8 on the HydroCouple = 100 scale (analyzer 1.7.0, baseline HC-2026-11-10-h); shipped .html alone 49.7.

| case | (i-f)A cfs | SWMM peak | ratio | port vs SWMM % | t95 SWMM min | t95 KW min |
|---|---|---|---|---|---|---|
| C1_i2 | 4.6296 | 4.62980 | 1.000037 | 0.088 | 12.93 | 5.30 |
| C2_i1 | 2.3148 | 2.31490 | 1.000037 | 0.100 | 17.06 | 7.00 |
| C3_i4 | 9.2593 | 9.25960 | 1.000037 | 0.115 | 9.83 | 4.02 |
| C4_i2_D5 | 4.6296 | 2.51267 | 0.542736 | 0.067 | n/a | n/a |
| C5_i2_D10 | 4.6296 | 4.08121 | 0.881542 | 0.083 | n/a | 5.30 |
| C6_i2_W2 | 4.6296 | 4.62980 | 1.000037 | 0.132 | 8.58 | 3.50 |
| C7_i2_ds | 4.6296 | 4.62980 | 1.000037 | 0.088 | 15.93 | 5.30 |
| C8_perv_i2 | 3.4722 | 3.47235 | 1.000037 | 0.104 | 14.53 | 5.95 |
| C9_perv_i4 | 8.1019 | 8.10215 | 1.000037 | 0.125 | 10.37 | 4.24 |
| C10_i2_n05 | 4.6296 | 4.62980 | 1.000037 | 0.045 | 26.63 | 10.92 |
| C11_flat | 6.9444 | 6.94470 | 1.000036 | 0.020 | 67.74 | 27.80 |

## What this does not show

- No observed flows; model against model only.
- One rectangular plane of uniform slope and roughness; no gutter, pipe, channel, converging surface or network.
- Constant loss only (Horton f0 = fc). Decaying losses make C drift in time.
- Engines: EPA SWMM 5.2.4 and the page's own solvers. Not SWMM 6, ICM, HEC-RAS or 2D.
- Shallow-water solver is first order; timing carries a grid error (extrapolated above).
- IDF curve is illustrative, not NOAA Atlas 14.
- Plateau agreement is partly by construction for any conservative scheme; timing and storm-duration results are the discriminating evidence.
- Research summaries written from abstracts and reference lists, not full papers.
- Known defect, engine: LD-1, src/solver/swmm5.c line 111 `{2.2956e-5, 0.92903e-5}, // LANDAREA (ac, ha --> ft2)`: US acres constant rounded, areas 0.0037% large; SI off 0.43 ppm.

## How to reproduce

1. Build EPA SWMM 5.2.4 from tag v5.2.4 with -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 (the default Ubuntu build aborts at "Retrieving project data").
2. python3 verify/make_cases.py writes 11 .inp files (C1-C11) to verify/cases; run each with runswmm.
3. node test/verify.js reads the .out files and writes test/verify-out.json.
4. node build.js builds the page, the Doc and this file; node tools/rasterize.js and node tools/docx.js build the .docx; node test/bundle.js, test/contrast.js and test/shots.js test the shipped file.

## Credits and licenses

- Author: Robert Dickinson.
- EPA SWMM 5.2.4: US Environmental Protection Agency, public domain.
- Theory: Henderson and Wooding (1964), Woolhiser and Liggett (1967), Akan (1985), Chen and Wong (1993), Richardson and Julien (1994), Beven (2020); full list in the Doc's Sources and the Research tab.
- Complexity analyzer: SWMM App Complexity Meter (Robert Dickinson), meter-core.js 1.7.0.
- Fonts: Archivo, IBM Plex (SIL Open Font License).

## Related apps

- It's the Intensity, Not the Inches (https://its-intensity-not-inches-elango.netlify.app): peak rainfall rates, rolling-window intensity and critical duration, the storm side of the D = tc question.
- The Narrow Band (https://narrow-band.netlify.app): GEV against MEVD for the 200-year rainfall, the frequency gap the rational method assumes away.
- Initial Abstraction and Constant Loss Explorer (https://initial-constant-loss-explorer.netlify.app): the f in C = 1 − f/i, with an initial abstraction added.
- Horton and curve number in SWMM5 (https://bowl-full-horton-cn-swmm5-sclark.netlify.app): losses that decay in time, which make C drift during a storm.
- Hydrograph Fingerprint Lab (https://hydrograph-fingerprint-lab.netlify.app): measures of a hydrograph beyond its peak, where the three models on this plane differ.
- Rain-on-Grid Workbench (https://rain-on-grid-workbench.netlify.app): the full two-dimensional simulation that the rational answer is the limit of.
- SWMM6 2D Flood Lab (https://swmm6-2d-flood-lab.netlify.app): rain on a 2D surface in the browser, the next step past one plane.
- Water Modeling to 3000 (https://water-modeling-in-year-3000.netlify.app): the long timeline that the 2100 claim belongs on.
- SWMM App Complexity Meter (https://swmm-app-complexity-vs-hydrocouple.netlify.app): the scale used in the closing box of this document.

## AI use

This app and its Doc were built with Claude, Anthropic's AI model, in Claude Code sessions on 12 October and 16 to 20 November 2026, under the direction of Robert (Bob) Dickinson. He posed the claim, asked for the app and the research behind it, and asked for this revision. Responsibility for the work is his.

**What Claude did.** It searched the literature and wrote the 24 research summaries, from abstracts and reference lists rather than full papers. It wrote the three solvers, ported EPA SWMM's subcatchment reservoir from subcatch.c, compiled EPA SWMM 5.2.4 from source, wrote the 11 verification models and the test scripts, designed the page and its charts, and wrote the Doc essay, this About tab, the .md and the .docx. It found the acre-constant rounding and the fixed 2.36 tc reservoir clock while writing the checks.

**How it was checked.** Every number in the app and the Doc comes from test/verify.js, which runs 43 mechanical checks against closed-form solutions, a second solver and EPA SWMM 5.2.4 output and writes the results to a file the build reads. The shipped page is tested on its own: its model code is extracted and rerun, its .inp export is run through SWMM, it is rendered in Chromium in both themes, and its colours pass a contrast gate. Not checked by any person, as far as this build records: the research summaries against the full papers, the history in the Doc's opening section, and the shallow-water solver beyond the two planes measured.

## Changes

- 1.1 (2026-11-20): Added the About and Doc tabs, the Doc as a Word file (rational-limit.docx) and as a PDF (rational-limit-doc.pdf), and a technical summary (rational-limit.md), embedded in the page and shipped beside it. The Doc ends with related topics from the Netlify app catalog.
- Added an eleventh EPA SWMM 5.2.4 case (a flat, rough plane) and checks for the reservoir's fixed 2.36 tc clock and the depression-storage delay: 43 checks, up from 36.
- Fixed: the SI area constant in swmm5.c is off by 0.43 parts per million, not the 3.3 that version 1.0 printed. The defect register now shows the line of code.
- Fixed: the kinematic time to 95% now uses the exact value, tc × 0.95^0.6, in every table; version 1.0 mixed in 30-second sampling in places.
- Saved files (CSV, .inp, GIF, .md, .docx) go through the viewer's save prompt inside claude.ai; there an .inp saves as .inp.txt.
- The first tab now quotes the claim in full.
- 1.0 (2026-10-12): First release: three solvers, eight-step derivation, storm-duration tab, ten EPA SWMM 5.2.4 runs, 24 sources, limits.

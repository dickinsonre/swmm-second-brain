---
name: Conformal SWMM
file: conformal-swmm.html
version: 1.0.0
date: 2026-11-14
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: private claude.ai artifact, repo: none}
engines:
  - {name: OpenSWMM legacy engine, version: 5.3.0-beta.3 (reports "5.3.0 (Build 5.3.0)", API 53000), source: github.com/HydroCouple/openswmm.engine, branch: swmm6_rel, commit: 283da75e21a8258af7b82b5222267b5f60057a81, directory: src/legacy/engine, license: Apache-2.0 over public-domain EPA SWMM}
  - {name: EPA SWMM, version: 5.2.4, source: github.com/USEPA/Stormwater-Management-Model tag v5.2.4, role: comparison only (not shipped), license: public domain}
units: US customary (ft, ac, in, cfs)
ai_use: built with Claude (Anthropic); see AI use
---

# Conformal SWMM: one square grid through five complex functions, written as SWMM5 models and run on SWMM 5.3 in the browser

## In three points
- **What:** Bends one square street grid through five complex functions, writes each as a SWMM5 model, and runs it on a SWMM 5.3 engine compiled to WebAssembly in the page.
- **So what:** The browser engine's .out matched a native build of the same source byte for byte in 16 of 16 runs, and five networks draining the same 22.96 ac peaked between 21.20 and 21.88 cfs.
- **Now what:** Use it to make test networks with controlled geometry. They are formula networks, not catchments, from one square and one storm, on a pre-release 5.3.0-beta.3 engine.

**In one sentence.** Conformal SWMM bends one square street grid through five complex functions, writes each result as a SWMM5 model, and runs it in a browser SWMM 5.3 engine that matched the native build byte for byte in 16 of 16 runs.

**In one paragraph.** Conformal SWMM is a model generator. You place a square grid on the complex plane and pick one of five functions: z, z squared, e to the z, a rational function with two poles, or z cubed. The page maps every grid crossing, turns grid lines into pipes and cells into subcatchments, keeps the elevation each junction had in the square, and writes a SWMM5 input file. A SWMM 5.3 engine compiled to WebAssembly runs it in the page. In 16 test runs the browser engine's binary results matched a native build of the same source exactly. On one shared square, five networks draining the same 22.96 acres peaked within 3.2 percent of each other. The main limit: these are test networks, not real catchments.

## What it does
The user places a square on the complex plane and picks a function f. The app maps the N x N grid on that square through f, writes the image as a SWMM5 .inp (junctions, circular conduits, subcatchments, one rain gage, one outfall), runs it on a SWMM 5.3 engine compiled to WebAssembly, and reads back the .rpt and .out. A Five Maps tab runs all five functions on the same square. Squares on which f is not one-to-one are refused.

## How it computes
Functions, derivatives and the "sibling" maps (other points with the same image):

| key | f(z) | f'(z) | siblings of z | bad points |
|---|---|---|---|---|
| id | z | 1 | none | none |
| sq | z^2 | 2z | -z | f'=0 at 0 |
| exp | e^z | e^z | z +/- 2 pi i | none |
| rat | 1/(z+1.3) + 1/(z-1.6) | -1/(z+1.3)^2 - 1/(z-1.6)^2 | 2/f(z) + 0.3 - z | poles -1.3, 1.6; f'=0 at 0.15 +/- 1.45i |
| cube | z^3 | 3z^2 | wz, w^2 z with w = e^(2 pi i/3) | f'=0 at 0 |

Steps (core.js, function build):
1. Grid points z(i,j) = c + s e^(i rot) (u_i + i v_j), u, v in [-1, 1], i, j = 0..N. Image w = f(z).
2. Each grid edge is sampled at K+1 points (default K = 4) for the exported polyline and at 25 points for its length.
3. Equal-area factor k = sqrt((2s)^2 / sum of image cell areas) when the switch is on, else 1. Feet = L k w, shifted to positive coordinates. L default 1000 ft per unit.
4. Invert elevation is set in the square and carried with the junction: Z = 100 + G L s [(u+1) cos(theta) + (v+1) sin(theta)], G = 0.005, theta = 45 deg. Pipe slope is therefore the plain-grid slope divided by k|f'|.
5. Conduits run from the higher-index junction to the lower. Length = arc length. Subcatchment (i,j) drains to junction (i,j). Area = shoelace area of its exported polygon; width = sqrt(area); slope % = 100 G / (k|f'| at the cell centre), clamped to 0.01..50.
6. Sizing: area is accumulated down the grid with an equal split at each junction; Q = C i A with C = 0.2 + 0.7 imperv and i = peak 5-minute intensity; diameter = smallest of 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7, 8, 9, 10, 12 ft with Manning full-flow capacity >= Q at max(slope, 0.0005), n = 0.013. "Reuse the sizes from f(z) = z" sizes the identity network and copies the diameters by conduit name.
7. Storm: triangular hyetograph, 5-minute blocks, peak at 0.375 of the duration, depth 2.0 in over 120 min by default (peak 1.933 in/hr).
8. Options written: FLOW_UNITS CFS, INFILTRATION HORTON (3.0, 0.5 in/hr, decay 4, dry 7), FLOW_ROUTING DYNWAVE, ROUTING_STEP 5 s, VARIABLE_STEP 0.75, MINIMUM_STEP 0.5, INERTIAL_DAMPING PARTIAL, NORMAL_FLOW_LIMITED BOTH, MIN_SLOPE 0, ALLOW_PONDING NO, REPORT_STEP 1 min, THREADS 1, 6-hour run from 01/01/2026 with explicit REPORT_START_DATE. Subareas: n 0.015 and 0.15, storage 0.06 and 0.20 in, 25 % zero storage.

Audits (a model is exported only if all pass):
- Sibling test: 41 x 41 points of the square; fails if any sibling lies in the closed square.
- Winding test (argument principle): the image of the boundary must wind exactly once around f(cell centre) for every cell.
- Every cell polygon has positive signed area.
- The exported boundary polyline has no proper self-crossing.
- Sum of cell areas equals the area inside the boundary to 1e-9 relative.
- No pole within 0.02 half-widths of the square.

Engine: runs in a Web Worker built from a Blob, one fresh module instance per run, step API (swmm_open, swmm_start, swmm_step loop, swmm_end, swmm_report, swmm_close), files in MEMFS, 2-minute timeout. Falls back to the main thread if a worker cannot be made.

## Inputs and outputs
- Writes: .inp (sections TITLE, OPTIONS, EVAPORATION, RAINGAGES, SUBCATCHMENTS, SUBAREAS, INFILTRATION, JUNCTIONS, OUTFALLS, CONDUITS, XSECTIONS, TIMESERIES, REPORT, MAP, COORDINATES, VERTICES, Polygons, SYMBOLS); CSV for hydrograph, conduits, nodes and the five-map comparison; the engine's .rpt; a WebM recording.
- Reads: nothing from the user. Reads back the engine's .rpt (version, continuity, outfall summary, errors) and .out (binary, classic SWMM5 layout, magic 516114522).
- Names: junctions Ji_j, conduits Hi_j and Vi_j, subcatchments Si_j, outfall OUT, outfall pipe OUTPIPE, gage RG1, series STORM.
- Inside claude.ai the .inp and .rpt are saved with a .txt suffix, because the save dialog there does not accept those extensions.

## Checks
All from this build, 2026-11-14. N = 8, K = 4 unless noted.

Engine identity (WebAssembly against native 5.3.0, same source, gcc 13.3 -O2 -ffp-contract=off):
- 16 of 16 .out files byte-identical: 15 files of 2,520,974 bytes, 1 file (N = 16) of 9,428,456 bytes.
- Same model twice on fresh instances: 0 bytes different.

Shared square (centre 0.9 + 1.0i, half-width 0.5, 82 nodes, 145 conduits, 64 subcatchments, 22.96 ac), pipes sized per network:

| f | k | stretch | pipe ft | pipe length ft | slope | cell ac | peak cfs | t peak min | full conduits | routing CE % |
|---|---|---|---|---|---|---|---|---|---|---|
| id | 1.000 | 1.00-1.00 | 18062 | 62-125 | 0.0035-0.0035 | 0.359-0.359 | 21.75 | 53 | 6 | 0.006 |
| sq | 0.356 | 0.46-1.46 | 17695 | 27-179 | 0.0025-0.0073 | 0.097-0.700 | 21.88 | 52 | 2 | 0 |
| exp | 0.375 | 0.56-1.52 | 17429 | 34-190 | 0.0023-0.0063 | 0.128-0.734 | 21.73 | 53 | 4 | 0.001 |
| rat | 1.239 | 0.10-4.12 | 15024 | 13-468 | 0.0009-0.0338 | 0.006-3.463 | 21.20 | 66 | 12 | 0 |
| cube | 0.157 | 0.19-1.98 | 16922 | 11-238 | 0.0019-0.0162 | 0.023-1.182 | 21.84 | 52 | 2 | -0.002 |

Same square, pipe sizes reused from f(z) = z:

| f | peak cfs | t peak min | full conduits | routing CE % |
|---|---|---|---|---|
| id | 21.75 | 53 | 6 | 0.006 |
| sq | 21.90 | 52 | 2 | 0 |
| exp | 21.56 | 67 | 5 | 0.001 |
| rat | 21.18 | 62 | 37 | -0.073 |
| cube | 21.85 | 51 | 0 | -0.002 |

Each function on its own preset square:

| f | centre, half-width | area ac | pipe ft | stretch | peak cfs | t peak min |
|---|---|---|---|---|---|---|
| id | (0, 0), 1 | 91.83 | 36124 | 1.00-1.00 | 85.13 | 57 |
| sq | (1, 0.5), 0.8 | 58.77 | 27365 | 0.17-1.71 | 54.95 | 55 |
| exp | (0, 0), 1 | 91.83 | 32079 | 0.27-2.02 | 84.24 | 58 |
| rat | (0.15, 0), 0.85 | 66.35 | 28606 | 0.31-2.63 | 60.91 | 57 |
| cube | (1.1, 0), 0.6 | 33.06 | 19465 | 0.15-1.98 | 30.89 | 54 |

No junction flooded in any of the 16 runs. Runoff continuity -0.007 to -0.010 %. Rain 2.00 in, runoff 1.10 to 1.15 in.

EPA SWMM 5.2.4 on the same 16 .inp files: 0 errors, 0 warnings; peak in the same minute in 16 of 16; largest peak difference 0.013 cfs; largest outfall-flow difference at any reported minute 0.037 cfs.

Right-angle error at interior crossings from exported chords, worst case in degrees, shared square:

| K | sq | exp | rat | cube |
|---|---|---|---|---|
| 2 | 3.009 | 1.790 | 2.828 | 6.071 |
| 4 | 1.525 | 0.895 | 1.332 | 3.063 |
| 8 | 0.767 | 0.448 | 0.645 | 1.538 |
| 16 | 0.385 | 0.224 | 0.319 | 0.771 |
| 32 | 0.193 | 0.112 | 0.159 | 0.386 |
| 64 | 0.096 | 0.056 | 0.079 | 0.193 |

Fold audit on chosen squares (fold % = share of sample points with a sibling in the square):

| f | centre | half-width | fold % | cells wound != 1 | boundary crossings | exported | Fit result (cx, cy, s) |
|---|---|---|---|---|---|---|---|
| sq | (1, 0.5) | 0.8 | 0.0 | 0 | 0 | yes | (1, 0.5, 0.8) |
| sq | (0.5, 0.3) | 0.8 | 24.7 | 15 | 1 | no | (0.5, 0.3, 0.48) |
| sq | (0, 0) | 0.8 | 100.0 | 64 | 0 | no | (0.31, 0.16, 0.3) |
| cube | (1.1, 0) | 0.6 | 0.0 | 0 | 0 | yes | (1.1, 0, 0.6) |
| cube | (0.5, 0) | 0.6 | 44.3 | 28 | 2 | no | (0.5, 0, 0.3) |
| cube | (0, 0) | 0.6 | 87.2 | 60 | 8 | no | (0.31, 0.16, 0.24) |
| exp | (0, 0) | 1 | 0.0 | 0 | 0 | yes | (0, 0, 1) |
| exp | (0, 0) | 3.1 | 0.0 | 0 | 0 | yes | (0, 0, 3.1) |
| exp | (0, 0) | 3.5 | 24.4 | 16 | 16 | no | (0, 0, 3.04) |
| rat | (0.15, 0.6) | 0.5 | 0.0 | 0 | 0 | yes | (0.15, 0.6, 0.5) |
| rat | (0.15, 1.45) | 0.5 | 81.2 | 52 | 1 | no | (0.46, 1.61, 0.3) |
| rat | (0.15, 0) | 1 | 0.0 | 0 | 0 | yes | (0.15, 0, 1) |
| rat | (0.15, 0) | 0.8 | 0.0 | 0 | 0 | yes | (0.15, 0, 0.8) |
| rat | (0.15, 0) | 1.2 | 9.5 | 4 | 4 | no | (0.15, 0, 0.99) |
| rat | (-1.3, 0) | 0.4 | 0.0 | 64 | 0 | no | (-0.99, 0.16, 0.28) |

Note the sq row centred on (0, 0): fold 100 %, crossings 0. Crossing and area-closure checks alone do not detect an exact double cover.

Largest model tested: sq preset, N = 16, 290 nodes, 545 conduits, 256 subcatchments, 13631 routing steps, 4.6 s under Node 22, peak 55.88 cfs at 70 min, 47 conduits full, 0 flooded.

Page test (Playwright, headless Chromium, 1280 px and 375 px): run of each function, results, five maps, fold refusal, fit, both themes, tour, .inp and CSV downloads, a 13-second 1280 x 720 WebM recording; 0 console errors; no horizontal overflow at 375 px. The downloaded .inp was rerun on the native engine.

## What this does not show
1. Formula networks, not real catchments. Not for design.
2. One shared square, one storm, N = 8. Other squares give other numbers.
3. Elevation riding with the junction is a design choice of this app.
4. Sizing uses an equal flow split and the rational method.
5. Exported pipes are chords; angles at crossings are approximate (table above).
6. The engine is a pre-release label, 5.3.0-beta.3. Agreement with EPA 5.2.4 was checked on 16 files only.
7. The sibling test samples a 41 x 41 lattice; a fold thinner than one lattice spacing could pass it and would then have to be caught by the winding or polygon checks.
8. Not tested: Firefox, Safari, phones, the save dialog inside claude.ai, the EPA SWMM desktop GUI.
9. The .out reader is a local copy in core.js, not the shared results library. It was checked against the .rpt in 16 runs.
10. No person has reviewed the code, the numbers or the text.
11. Not measured with the SWMM App Complexity Meter. Raw counts: core.js 355 lines, page 426 lines, engine 55 C files (about 59,000 lines, not written here).

## How to reproduce
1. git clone -b swmm6_rel https://github.com/HydroCouple/openswmm.engine and check out 283da75e21a8258af7b82b5222267b5f60057a81.
2. Generate legacy_version.h from include/openswmm/legacy/engine/legacy_version.h.in (5, 3, 0, beta.3).
3. Compile src/legacy/engine/*.c with emcc 3.1.6: -O2 -DOS_UNIX -DNO_OPENMP -ffp-contract=off, and -Domp_get_max_threads=omp_gmt_project for project.c only (two files define the same no-OpenMP fallback). Link with MODULARIZE, EXPORT_NAME=createSwmm53, SINGLE_FILE, ALLOW_MEMORY_GROWTH, ENVIRONMENT=web,worker,node. No source file is edited.
4. Build the same sources natively with gcc and the same defines, plus src/legacy/cli/main.c.
5. node test/facts.js regenerates every number in Checks; node test/e524.js runs the EPA 5.2.4 comparison (build v5.2.4 with -D_FORTIFY_SOURCE=0; Ubuntu's default fortify level aborts that build while it reads the file); node test/browser.js drives the page.

## Credits and licenses
- Engine: OpenSWMM Engine, Copyright 2026 HydroCouple Developers, Apache License 2.0. Lead developer Caleb Buahin; developer and documentation Corinne Wiesner-Friedman. The upstream NOTICE and the full license text are reproduced in the app's About tab. Sources unmodified.
- EPA SWMM 5: Lewis Rossman and colleagues, U.S. EPA, public domain. The USEPA does not endorse this product.
- The five functions and the cross: Matheorems, "One Square Grid, Five Complex Functions", X, 14 November 2026.
- App code: Copyright 2026 Robert Dickinson.

## AI use
This app was built with Claude, Anthropic's AI model, in one session on 14 November 2026, under the direction of Robert (Bob) Dickinson. He chose the idea, from a Matheorems post about one square grid and five complex functions, and asked for a SWMM5 generating app that uses a WebAssembly SWMM 5.3 engine. Responsibility for the published work is his.

**What Claude did.** It designed the generator, including the choices that elevation rides with the junction, that the image is rescaled to equal area, and how pipes are sized. It wrote all of the page code, the .inp writer and the .rpt and .out readers. It compiled the OpenSWMM legacy 5.3.0-beta.3 engine to WebAssembly from unmodified source, built native 5.3 and EPA 5.2.4 engines for comparison, wrote and ran the tests, drew the figures from the test output, and wrote this text, the Doc essay and the technical summary.

**How the results were checked.** The checks are mechanical: byte comparison of .out files between the browser engine and the native engine (16 of 16 identical), the same 16 files run on EPA SWMM 5.2.4, the .out reader compared with the .rpt, five overlap audits on every model, and a headless-browser test of the page with no console errors.

**What no person has checked yet.** Bob has not yet reviewed the code, the design choices, the numbers or the essay. The files have not been opened in the EPA SWMM desktop program. The page has not been tried in Firefox, Safari or on a phone, and the save dialogs inside claude.ai have not been tested.

## Changes
1.0.0 (2026-11-14): first version.

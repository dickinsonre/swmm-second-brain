---
name: SWMM5 Walks Downhill
file: swmm5-walks-downhill.html
version: 1.1.0
date: 2026-11-15
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: private Claude artifact, repo: none}
models: [six (built in), extran1, extran2, extran3, extran4, extran5, extran6, extran7, extran9, extran10]
engines:
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4, commit: 7952ca837988b1c32f791812eccc9fd64547e093, license: public domain}
compiler: Emscripten 3.1.6, -O3, MODULARIZE, SINGLE_FILE, unmodified src/solver sources
engine_sha256: 642eb402361f641a8eb1c5a4eb3f64be319963c8530a18526f9ceb05421a417f
units: US customary (cfs, ft, acres, in, in/hr)
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM5 Walks Downhill: gradient descent on two SWMM5 parameters, with the engine in the loop

## In three points
- **What:** Gradient descent on two SWMM5 parameters with EPA SWMM 5.2.4 running in the browser: five engine runs per step give the cost and its slope, and two walkers (step sizes 0.50 and 0.25) fit the %Imperv and Width of a six-subcatchment model to 47 noisy flow readings; nine OWA EXTRAN models can be picked, with an inflow factor and a roughness factor as their knobs.
- **So what:** On the built-in model both walks end near the knobs that made the data (red 45.24 %, 220.5 ft; teal 45.14 %, 223.5 ft; truth 45 %, 220 ft). On the OWA models the longer-step walker reaches the bottom on 8 of 9 and the shorter-step walker on 3 of 9; on extran10 both end pinned at the top of the roughness range with NSE 0.966 and the wrong knobs.
- **Now what:** Use it to teach calibration as a walk downhill, and to see why a good fit is not proof of the right knobs. The observed flow is synthetic, there are two knobs and one storm, and no person has reviewed the code, the knob choices or the essay.

In one sentence: This page fits two knobs of a SWMM5 model to measured flow by walking downhill on the misfit, five EPA SWMM 5.2.4 runs per step; the walk succeeds on the built-in model and on most of nine OWA EXTRAN models.

In one paragraph: A straight line can be fitted by gradient descent because the slope of its error has a formula. A stormwater model has none, so this page asks the engine. It runs EPA SWMM 5.2.4 at the current pair of knobs and at a small nudge up and down on each, gets the cost and its slope, and steps downhill. Two walkers leave one point with different step sizes. On the built-in model one zigzags, one crawls, and both end within 2 percent of the knobs that made the data. On nine published OWA EXTRAN models the hills are rougher: some walks stall, and on one neither walker arrives. The data are synthetic, made by the same engine plus noise, and that is the main limit.

## What it does

It redraws the standard gradient-descent teaching picture (data and fitted line, cost contours with descent paths, cost bowl, cost against step) for a stormwater model. The fitted line is replaced by EPA SWMM 5.2.4 running in the browser. Two parameters of a small model are treated as unknown and recovered from 47 flow readings. Ten models can be picked: one built in, and nine published EXTRAN test models from the OpenWaterAnalytics swmm-nrtestsuite. It is for people learning calibration or gradient descent. Out come the two walks, the cost surface, every hydrograph, CSV tables and the SWMM5 input file at any step.

## How it computes

1. Model: six subcatchments, each 660 ft x 660 ft = 10 ac, tiling a 1,980 ft x 1,320 ft block without overlap; three circular pipes (3.0, 4.0, 4.5 ft; 660 ft each; 0.5 %; n 0.013); one free outfall. Slope 1 %, N-Imperv 0.015, N-Perv 0.24, S-Imperv 0.05 in, S-Perv 0.15 in, 25 % zero-storage, Horton 1.5 to 0.2 in/hr, decay 4 /hr. Storm: 24 five-minute intensities, 1.32 in in 2 hr, peak 3.0 in/hr. DYNWAVE, ROUTING_STEP 5 s, VARIABLE_STEP 0, WET_STEP 1 min, 4 hr run, REPORT_STEP 5 min.
2. Knobs: theta0 = %Imperv of all six subcatchments, 10 to 90. theta1 = Width of all six, 100 to 700 ft. Scaled knobs u in [0,1]: theta0 = 10 + 80 u0; theta1 = 100 * 7^u1 (log scale).
3. For each knob pair the page writes a complete .inp (168 lines) and runs it: swmm_open, swmm_start(1), swmm_step until done, swmm_end. It reads link C3 flow for each of the 47 reporting periods with swmm_getSavedValue(swmm_LINK_FLOW = 410, index, period). No .out bytes and no .rpt text are parsed by the page. A fresh WebAssembly instance is made for every run.
4. Observed flow: y_i = max(0, Q_true,i + sd * z_i), Q_true from the engine at the true knobs (default 45 %, 220 ft), z_i standard normal from mulberry32 seed 1729 with Box-Muller, sd default 2.0 cfs.
5. Cost: J = 1/(2m) * sum(((Q_i - y_i)/s_y)^2), s_y = population standard deviation of y. So J = (1 - NSE)/2 and RMSE = s_y * sqrt(2J).
6. Slope: dJ/du_j = 1/m * sum((Q_i - y_i)/s_y^2 * dQ_i/du_j), with dQ_i/du_j = (Q_i(u + h e_j) - Q_i(u - h e_j)) / (2h), h = 0.01, clipped at the box. Five engine runs per step.
7. Update: u := clamp(u - alpha * dJ/du, 0, 1). Defaults: start 75 %, 520 ft; alpha 0.50 (red) and 0.25 (teal); 40 steps.
8. Surface: J on a 25 x 25 grid of u (625 runs), contoured by marching squares at 12 log-spaced levels. Curvature at the lowest grid point by central differences; stability limit = 2 / largest eigenvalue.
9. OWA EXTRAN models (extran1 to 7, 9, 10; text embedded verbatim from OpenWaterAnalytics/swmm-nrtestsuite public/extran, commit e609fdbb47db410ee95a8c0353f21e4a7d890b58). These are routing-only (inflow hydrographs, no subcatchments). theta0 = inflow factor, 0.5 to 1.5, linear: multiplies the scale-factor column (and baseline, if any) of every FLOW row in [INFLOWS]. theta1 = roughness factor, 0.5 to 2, log scale: multiplies the Manning n column of every row in [CONDUITS] (and NC lines of [TRANSECTS]). extran9 has no conduit, so its theta1 multiplies the discharge coefficient column of [ORIFICES]. Other edits: [REPORT] replaced by NODES ALL / LINKS ALL, [FILES] dropped, one comment line added to [TITLE]. With both factors at 1 no data line changes. Truth = the published file (1, 1). Meter = the link into the outfall (1030 for extran1 to 7, 90001 for extran9, 100 for extran10). Default start (1.35, 1.6). Default noise sd = 0.14 x the spread of the meter flow at truth. Default step sizes = 0.78 and 0.39 x the stability limit measured on that model's surface. extran9 is in SI (CMS) as published and is shown in cubic metres per second.
10. Engine runs go to a pool of Web Workers (blob URL); if workers are unavailable the engine runs on the page. Results are cached by knob pair for the session.

## Inputs and outputs

No file input. Outputs (Export button, copy or download): steps CSV, surface CSV, flows CSV, the .inp at the current step, this .md. The Model tab shows the full .rpt for the current step. Record makes a WebM video of the canvas.

## Checks

All run on the shipped engine file and the shipped single-file page, default scenario. 21 of 21 Node checks and 29 of 29 browser checks (headless Chromium) pass.

| Check | Result |
|---|---|
| Node: engine identifies as EPA SWMM 5.2.4 | getVersion 52004, report header matched |
| Node: flows read by swmm_getSavedValue equal the report file time series | 47 printed values, largest difference 0.00049 cfs (report prints 3 decimals) |
| Node: two runs of one input give identical flows | largest difference 0 |
| Node: slope from flow sensitivities matches slope from differencing J | largest relative gap at 5 points: 1.87 % |
| Node: J = (1 - NSE)/2 | NSE by definition 0.166833, from J 0.166833 |
| Node: both walks end near the true knobs | red 45.24 %, 220.5 ft; teal 45.14 %, 223.5 ft; truth 45 %, 220 ft |
| Node: the fitted cost is no higher than the cost at the truth | J end 0.005659, J at truth 0.005676 |
| Node: a step size 1.5 times the limit fails to settle | limit 0.639, alpha 0.958, lowest J in last 10 steps 0.1193 against 0.0057 |
| Node: log scaling of width rescues a start on the high-width shelf | from 80 %, 650 ft, step size 0.25, 40 steps: straight scale ends at 371 ft, J 0.0165; log scale at 226 ft, J 0.0057 |
| Node: no flooding or surcharge at the four corners of the knob box | largest continuity error at the corners 0.108 % |
| Node: subcatchment polygons do not overlap and match the areas | overlap 0 sq ft, polygon area 60 ac |
| Node: grid Hessian is exact on a known quadratic | hxx 3.000000, hyy 0.500000, hxy 0.200000 |
| Node: contour segment ends lie on the level they claim | largest miss 5.55e-17 |
| Node: knob scaling round-trips | 37.5, 412 |
| Node: with both factors at 1 each OWA input file is the published file | 9 models, 781 data lines compared outside [TITLE] and [REPORT], 0 differ |
| Node: a factor changes only its own column, by exactly that factor | 9 models at factors 1.25 and 1.25: 89 values changed, all in the knob columns and all by 1.25; 0 other changes |
| Node: OWA flows read by swmm_getSavedValue equal the report file time series | 293 values at the meter link over 9 models, largest difference 0.00050 (report prints 3 decimals) |
| Node: the longer-step walker reaches the bottom on most OWA models | within 5 % of the cost at the published values on 8 of 9: extran1, extran2, extran3, extran4, extran5, extran6, extran7, extran9. Shorter-step walker: 3 of 9 (extran5, extran6, extran9) |
| Node: on extran10 neither walker arrives: both end pinned at the top of the roughness range with the slope still pushing outward | red ends at inflow 1.353, roughness 2.00 with slope (-0.0295, -0.4500); J 0.0171 (NSE 0.966) against 0.0072 at the published values |
| Node: where the shorter-step walker is close but not arrived, its cost is still falling at step 40 | extran1 0.0063 to 0.0059 against 0.0055; extran2 0.0064 to 0.0060 against 0.0055; extran7 0.0062 to 0.0058 against 0.0054 |
| Node: where the shorter-step walker has stalled, its cost changes by under 2 % in the last ten steps | extran3 0.0303 to 0.0302, 5.6 times the cost at the published values, ending at factors 1.32, 1.51; extran4 0.0225 to 0.0226, 4.1 times the cost at the published values, ending at factors 1.34, 1.43 |
| Browser: page opens dark | data-theme is dark in the served markup |
| Browser: welcome shows on first load | modal visible |
| Browser: engine runs in a background worker | mode worker |
| Browser: browser numbers equal the Node numbers | 47 observed flows, 82 walk steps and 625 surface values; largest differences 0, 5.7e-14, 0.0e+0 |
| Browser: light theme changes no number | steps CSV identical in both themes (5955 characters) |
| Browser: clicking the contour map moves the start | start is now 26 %, 390 ft |
| Browser: the page warns when a step size is past the limit | Largest stable step near the bottom, 2 / steepest curvature: α = 0.64. Red is past it and should not settle. |
| Browser: the six in-page self-checks pass | PASS PASS PASS PASS PASS PASS |
| Browser: the runs table lists every step | 82 rows |
| Browser: the Model tab shows a real report file | header and flooding summary found, 49016 characters |
| Browser: the .inp export holds a complete model | 168 lines |
| Browser: the embedded .md opens from the page | 17609 characters |
| Browser: the standalone page downloads a CSV file | swmm5-walks-downhill-steps.csv |
| Browser: the Doc tab has its summaries, questions, figures and one-sentence ledes | 10 figures (one repeated in the one-page summary), 15 sections each with its sentence, no hard-coded colours |
| Browser: Doc contents links jump within the Doc tab | answers section scrolled into view |
| Browser: Record produces a captioned video | A 3.2 MB WebM video of the walk you just |
| Browser: no console errors in the whole session | none |
| Browser: the model list offers the built-in model and nine OWA EXTRAN models | 10 options |
| Browser: extran1 in the browser equals extran1 in Node | both end points and 625 surface values; largest differences 0.0e+0, 0.0e+0 |
| Browser: extran10 in the browser equals extran10 in Node | both end points and 625 surface values; largest differences 0.0e+0, 0.0e+0 |
| Browser: the page says so when the walkers stop short on extran10 | Red stopped short: J = 0.0171 after 40 steps, against 0.0072 at the lowest point of the map, and it is pinned  |
| Browser: the in-page self-checks on an OWA model pass, or say plainly that the slope is not well defined at the start | PASS PASS PASS PASS PASS PASS |
| Browser: the Model tab draws the OWA network and shows its input file | 9 links drawn, published title present |
| Browser: exports are named for the model | swmm5-walks-downhill-extran1.inp |
| Browser: switching back to the built-in model gives the same numbers as before | steps CSV identical |
| Browser: no console errors while switching models | none |
| Browser: without Web Workers the engine runs on the page and gives the same numbers | mode main |
| Browser: no sideways scroll at 375 px on any tab, with an OWA model selected | largest overflow 0 px |
| Browser: no console errors at phone width | none |

Default-scenario numbers: m = 47; s_y = 14.20 cfs; J at start 0.417 (NSE 0.167, RMSE 12.96 cfs); J at the true knobs 0.00568; red ends 45.2 %, 221 ft, teal ends 45.1 %, 224 ft, both J = 0.0057 (NSE 0.989, RMSE 1.51 cfs); within 5 % of final J at step 9 (red) and 24 (teal); curvatures 3.13 and 0.47, ratio 6.7; stability limit 0.64; at alpha 0.96 the lowest J in the last 10 of 40 steps is 0.119; lowest grid J 0.0061 at 46.7 %, 207 ft; highest 0.870. Engine runs: 1036 in Node (625 + 1 + 2 x 41 x 5), 1031 in the browser (the two walks share their first five). Mean 12 ms per run in headless Chromium on the build machine.

OWA EXTRAN results, default settings, 40 steps (arrived = J within 5 % of J at the published values; "short" = not arrived):

| Model | m | noise sd | step sizes | limit | red ends (factors), J | teal ends (factors), J | J at file values | floods as published |
|---|---|---|---|---|---|---|---|---|
| extran1 | 32 | 7.3 cfs | 0.76, 0.38 | 0.98 | 0.97, 0.97, 0.0054 | 1.08, 1.05, 0.0059 short | 0.0055 | yes |
| extran2 | 32 | 7.2 cfs | 0.74, 0.37 | 0.95 | 0.98, 0.98, 0.0054 | 1.09, 1.06, 0.0060 short | 0.0055 | yes |
| extran3 | 32 | 8.1 cfs | 0.89, 0.44 | 1.14 | 1.01, 0.99, 0.0053 | 1.32, 1.51, 0.0302 short | 0.0054 | no |
| extran4 | 32 | 8.1 cfs | 0.73, 0.36 | 0.93 | 1.01, 1.01, 0.0054 | 1.34, 1.43, 0.0226 short | 0.0054 | no |
| extran5 | 32 | 6.6 cfs | 0.93, 0.47 | 1.19 | 0.98, 0.98, 0.0055 | 1.02, 1.01, 0.0056 | 0.0055 | yes |
| extran6 | 32 | 6.3 cfs | 0.95, 0.47 | 1.22 | 1.00, 0.99, 0.0055 | 0.99, 0.99, 0.0055 | 0.0055 | yes |
| extran7 | 32 | 7.8 cfs | 0.83, 0.41 | 1.06 | 0.98, 0.97, 0.0051 | 1.07, 1.04, 0.0058 short | 0.0054 | yes |
| extran9 | 39 | 0.012 cms | 0.091, 0.045 | 0.12 | 1.00, 1.00, 0.0074 | 1.00, 1.00, 0.0074 | 0.0074 | no |
| extran10 | 30 | 4.4 cfs | 0.14, 0.07 | 0.18 | 1.35, 2.00, 0.0171 short | 1.35, 2.00, 0.0171 short | 0.0072 | no |

Slope computed two ways at the default start (flow sensitivities with nudge 0.01 against differencing J with nudge 0.005), difference as a share of the slope: six 0.04 %, extran1 0.94 %, extran2 4.30 %, extran3 18.94 %, extran4 5.98 %, extran5 3.16 %, extran6 11.01 %, extran7 2.58 %, extran9 4.56 %, extran10 0.52 %. Over 5 % is shown on the page as a note that the surface has a fold near the start.

Human review: none yet.

Complexity: index on the HydroCouple = 100 scale not computed in this build. Raw counts from the build script (not the Meter's analyzer): 2614 non-blank lines, 658 functions, 857 decision points in 14 hand-written files.

## What this does not show

1. The observed flow is synthetic (same engine plus noise). No real gauge, no model structural error.
2. Two knobs only, applied uniformly to all six subcatchments. No equifinality study.
3. One storm, no validation event.
4. OWA results are for one start, one noise seed and one pair of step sizes per model. On extran10 both walkers end pinned at the top of the roughness range with NSE 0.966 and wrong knobs. No model was shown to have two separate interior minima; that case is untested. The cause of the corners in the pipe-network surfaces (flooding is the guess) was not tested.
5. The stability limit is a local estimate at one grid point.
6. Plain fixed-step gradient descent is a teaching method. No Gauss-Newton, Levenberg-Marquardt, line search or momentum.
7. Only EPA SWMM 5.2.4 was run. No SWMM6, no ICM. extran8a (three saved readings) and extran8b (needs 8a's hot start file) are not offered.
8. Tested in headless Chromium only. Not yet tested inside the Claude artifact frame, in Firefox or in Safari.
9. No person has reviewed the code, the model choices or the essay.

## How to reproduce

Source tree: src/core.js (models, cost, slope), src/inptools.js (reads and rewrites .inp sections), src/owa-models.js (the published OWA texts, generated by tools_models.js), models/ (the OWA files as fetched), src/driver.js (engine calls), src/app.js (page), engine/swmm5.js (the build). `node test/t_node.js` runs the Node checks and writes doc/scenario.json. `node build.js` assembles the page. `node test/t_browser.js` runs the browser checks. `node doc/build-doc.js` writes the Doc tab, the .docx and this file. Engine build: `emcc src/solver/*.c -O3 -s MODULARIZE=1 -s EXPORT_NAME=createSwmmModule -s ENVIRONMENT=web,worker,node -s ALLOW_MEMORY_GROWTH=1 -s SINGLE_FILE=1` with the swmm_* API, _malloc and _free exported.

## Credits and licenses

- Idea for the view: Matheorems (@matheorems on X), a post on gradient descent for a straight-line fit, shared by Robert Dickinson on 15 November 2026. No text or artwork from the post is reproduced.
- EPA SWMM 5.2.4: U.S. Environmental Protection Agency, public domain. Lewis Rossman wrote SWMM5.
- OWA EXTRAN models: OpenWaterAnalytics/swmm-nrtestsuite, public/extran, commit e609fdbb47db410ee95a8c0353f21e4a7d890b58, Creative Commons Attribution 4.0, copyright 2018-2021 its contributors, excluding material in the public domain. Used unmodified except as described in How it computes, item 9.
- Emscripten 3.1.6 (MIT / University of Illinois NCSA).
- Nash, J. E. and Sutcliffe, J. V. (1970). River flow forecasting through conceptual models, part I. Journal of Hydrology 10(3), 282-290.
- Page: Robert Dickinson, SWMM Enablement, MIT License.

## AI use

This page was built with Claude, Anthropic's AI model (Claude Fable 5.2), on 15 November 2026, at the request of Robert (Bob) Dickinson. He supplied the idea, a Matheorems post on gradient descent, asked for the same view of flow in a SWMM5 model with a SWMM5 engine, and then asked for the OWA EXTRAN models to be added. Responsibility for the published work is his.

What Claude did. It chose the built-in test model, the knobs for every model, which link to meter in the OWA models, the cost measure, the scaling and the default settings. It compiled the unmodified EPA SWMM 5.2.4 solver to WebAssembly. It wrote all of the page code, the tests, the figures, this essay, the Word file and the technical summary.

How the results were checked. The checks are mechanical: 21 tests in Node and 29 in a headless browser, run on the shipped file and listed in the Doc tab. Claude also looked at screenshots of the page in both colour themes.

What no person has checked yet. Bob has not yet reviewed the code, the choice of knobs, the essay or the numbers. The complexity index on his Complexity Meter scale was not computed in this build; raw counts are given instead.

## Changes

`1.1.0 (2026-11-15)`: nine OWA EXTRAN models added, with inflow and roughness factors as knobs; model picker; generic map; a note when a walker stops short.
`1.0.0 (2026-11-15)`: first version.

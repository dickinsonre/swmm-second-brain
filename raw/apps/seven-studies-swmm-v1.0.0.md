---
name: Seven Studies for SWMM
file: seven-studies-swmm.html
version: 1.0.0
date: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: private Claude artifact, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.2, source: "npm @fileops/swmm-wasm-web 0.0.4 (prebuilt WebAssembly, Issac Gardner)", license: "engine public domain; package MIT"}
  - {name: EPA SWMM (reference only, not shipped), version: 5.2.4, source: "github.com/USEPA/Stormwater-Management-Model tag v5.2.4, gcc -O2", license: public domain}
units: US customary (cfs, ft, in, acres, million gallons)
ai_use: built with Claude (Anthropic); see AI use
---

# Seven Studies for SWMM: seven habits of thought, each run on one small SWMM model

## In three points
- **What:** Seven habits of thought, from metacognition to intellectual humility, each given one lab on the same four-pipe SWMM model, run by EPA SWMM 5.2.2 compiled to WebAssembly in the page.
- **So what:** Upsizing the pipe below a flooded manhole cut total flooding by only 2.2 percent, because the flood moved downstream; the engine matched a native EPA SWMM 5.2.4 build on 17 models with a largest difference of 0, and 22 of 22 checks pass.
- **Now what:** Use it to teach how a modeler should think before trusting a run. One synthetic network and storm, and the costs and uncertainty ranges are illustrative.

**In one sentence.** Seven habits of thought are each tested on one four-pipe SWMM model in the browser, and the plainest result is that upsizing the pipe below a flooded manhole cut total flooding by only 2.2 percent.

**In one paragraph.** A short list of seven things worth studying first, from metacognition to intellectual humility, is applied to storm sewer modeling. Each idea gets a lab, and every lab runs EPA SWMM 5.2.2 compiled to WebAssembly on the same small model: three towns, four pipes, one 2.37 inch storm that floods 0.727 million gallons. You predict before the engine reveals, split a shared cost, name a fault from its hydrograph, chase a flood downstream, run 200 uncertain cases, rebuild a runoff peak by hand, and calibrate against a gauge. The engine was compared with a native EPA SWMM 5.2.4 over 216,840 values and the largest difference was zero. The model is synthetic and small, so the lessons transfer but the numbers do not.

## What it does
Takes a seven-item list (metacognition, game theory, pattern recognition, systems thinking, probabilistic thinking, first-principles thinking, intellectual humility) and gives each item one lab on the same model. The audience is SWMM modelers and students. Each lab ends in a number from an EPA SWMM run and a statement of what the number means. Tabs: Home, seven labs, About, Doc.

## How it computes
- **Engine.** Each run writes an .inp as text, calls `swmm_run(inp, rpt, out)` in the WebAssembly module, and reads /m.rpt and /m.out from the module's in-memory file system. One module instance is reused; /m.rpt and /m.out are unlinked before every run; a thrown run discards the instance. The engine runs on the main thread (no Web Worker).
- **Base model.** 3 subcatchments (40, 30, 50 ac; 50, 60, 40 % impervious), Horton infiltration (3.0 and 0.5 in/hr, decay 4 /hr), 4 junctions (max depth 8 ft), 4 circular conduits 1,000 ft each (3.0, 3.5, 4.5, 4.5 ft; n 0.013), free outfall, DYNWAVE, ROUTING_STEP 10 s, VARIABLE_STEP 0.75, ALLOW_PONDING NO. Storm: 2-hour hyetograph at 5-minute intervals, 2.37 in, peak 5.6 in/hr.
- **Lab 1.** Eight changes to the base model; truth = percent change in one result, base run against changed run. Score = share of the user's 90% ranges containing the truth.
- **Lab 2.** Seven runs, one per coalition, with only that coalition's subcatchments and 8 ft pipes. Each segment sized as the smallest standard diameter with Qfull = (1.486/n) A R^(2/3) S^(1/2) >= coalition peak; cost/ft = k D(in)^e, defaults k = 4.5, e = 1.3 (illustrative). Allocations: by area, by stand-alone peak flow, Shapley value, SCRB, MCRS (Heaney and Dickinson 1982; closed form for three players). Core test: x_i <= c(i) and x_i + x_j <= c(ij).
- **Lab 3.** Reference model: pipes 4.5, 5.5, 6.5, 6.5 ft, dry-weather flow 2, 1.5, 2.5 cfs, 8 hours. Six conditions: C3 at 3.0 to 4.0 ft without and with ponding; FIXED outfall stage; RDII (RTK unit hydrograph, R = 0.02, 0.05, 0.15) at J1; storage at J3 with a 3 ft outlet; TYPE3 pump with a wet well at J4. Quiz cases use a seeded generator (mulberry32).
- **Lab 4.** Base model with user pipe diameters and optional storage at J1 (FUNCTIONAL, 20,000 ft2).
- **Lab 5.** Monte Carlo, default 200 runs, seed 2026. Triangular: imperviousness -10/0/+10 points, pipe n 0.011/0.013/0.016, storm factor 0.8/1/1.2, Horton minimum 0.2/0.5/1.0 in/hr. Log-uniform: width factor 0.5 to 2. Failure probability p with standard error sqrt(p(1-p)/N). Sensitivity = Spearman rank correlation.
- **Lab 6.** One 100% impervious plane, constant rain, one pipe to a NORMAL outfall. Hand solution: dd/dt = i - alpha (d - ds)^(5/3), alpha = 1.486 W sqrt(S)/(A n), RK4 at 1 s; pipe depth by bisection on Manning.
- **Lab 7.** One 60 ac subcatchment; hidden parameters imperviousness 45 %, width 1,200 ft, Horton 3.0 and 0.4 in/hr. Calibration storm factor 0.4 (0.95 in), test storm factor 1.9 (4.5 in). Fit measure: Nash-Sutcliffe efficiency on 1-minute runoff. Search: 300 uniform random draws, seed 7.

## Inputs and outputs
Reads nothing from disk. Writes, through the Export button: a CSV of the current tab's table and the .inp behind the tab's last run. The .inp files are plain EPA SWMM 5.2 input and run unchanged in EPA SWMM. The GIF button records a WebM walkthrough (needs html2canvas from cdnjs).

## Checks
22 of 22 mechanical checks pass (test/run-all.js, Node, same engine file and same core.js and labs.js as the page; 958 engine runs).

| id | check | result | evidence |
|---|---|---|---|
| T01 | engine identifies itself | pass | report header says Build 5.2.2 |
| T02 | .out reader against the 5.2.4 text tables | pass | 11400 values, 0 mismatches |
| T03 | wasm 5.2.2 against native 5.2.4, every series value | pass | 17 models, 216840 values, largest difference 0 |
| T04 | engine reuse A, B, A gives A back | pass | report text identical after an intervening different run |
| T05 | null-effect control: pervious parameters on a 100% impervious plane | pass | .out files byte-identical, 20500 bytes |
| T06 | hand nonlinear reservoir against engine runoff peak | pass | 4 cases, worst peak difference 0.18% |
| T07 | hand normal depth against engine pipe depth at peak | pass | 4 cases, worst difference 0.010 ft |
| T08 | conservation: long steady rain reaches Q = i A | pass | engine 120.99 cfs against i A = 121.00 cfs |
| T09 | Manning scaling: doubling the diameter | pass | capacity ratio 6.350 = 2^(8/3) |
| T10 | hand full-flow capacity against the report | pass | C1: 36.5 cfs by hand, Max/Full 1.07 against 1.07 printed |
| T11 | prediction cards all run | pass | rain-flood 84%, rain-peak 0%, c1-flood -2.2%, n-peak -13%, width-peak 17.9%, imperv-vol 15.1%, step-flood 0%, big-peak 79.2% |
| T12 | calibration score arithmetic | pass | 1 of 2 intervals hold, mean miss 32 points |
| T13 | every allocation recovers the full cost | pass | 5 methods each sum to $4,441,905 |
| T14 | Shapley and MCRS lie in the core; area split does not | pass | area split breaks C and BC |
| T15 | Shapley on a symmetric textbook game | pass | equal players each pay 4 of 12 |
| T16 | the seven signatures are measurably different | pass | lost: peak 87.4 cfs, rim depth 8 ft; ponded: depth 16.27 ft, no loss; RDII: 16.1 cfs at hour 5 against 6.2 |
| T17 | upsizing C1 moves the flood instead of removing it | pass | J1 0.345 to 0.032 Mgal, J2 0.359 to 0.654 Mgal, total 0.727 to 0.711 |
| T18 | Monte Carlo repeats exactly for a given seed | pass | 200 runs, seed 2026, identical twice |
| T19 | the single run sits inside the Monte Carlo spread | pass | single run 0.727 Mgal; 5th to 95th percentile 0.333 to 1.422 |
| T20 | two fits pass calibration and disagree on the test storm | pass | Fit 1 NSE 0.9953, test peak 228.5 cfs; Fit 2 NSE 0.9966, test peak 276.4 cfs; truth 261.2 |
| T21 | behavioural search finds a spread of equally good fits | pass | 10 of 278 sets fit at NSE 0.99 or better; test peaks 245.7 to 276.3 cfs |
| T22 | continuity errors of the base run are small | pass | runoff -0.011%, routing -0.115% (necessary, not sufficient) |

Browser test (headless Chromium): every tab opens with no console error; a result is identical in dark and light themes.
Human review: none yet.
Complexity: the SWMM App Complexity Meter analyzer was not run for this build. Raw counts: 14 hand-written files, 2,458 lines, 594 functions.

## Key results (base model and defaults)
- Base: storm 2.37 in, runoff 4.36 Mgal, flooded 0.727 Mgal (J1 0.345, J2 0.359, J3 0.023), outfall peak 135.3 cfs.
- Upsize C1 to 4 ft: J1 0.032, J2 0.654, total 0.711 Mgal (-2.2%). Upsize all (4, 5, 6, 6 ft): 0.003 Mgal, outfall 243.1 cfs (+80%). Detention at J1: 0.013 Mgal, outfall 135.3 cfs.
- Game: alone $3,217K, $2,412K, $1,608K; joint $4,442K; saving $2,795K. Area split charges C $1,851K (outside the core). Shapley $2,312K, $1,326K, $804K. MCRS $2,316K, $1,301K, $824K.
- Monte Carlo, as built: P5 0.33, P50 0.76, P95 1.42 Mgal. Upsized trunk: 18% of 200 runs flood more than 0.1 Mgal.
- Hand against engine: 70.31 against 70.43 cfs; Q = iA gives 121.0 cfs.
- Two fits: NSE 0.9953 and 0.9966; design peaks 228.5 and 276.4 cfs; truth 261.2 cfs.

## What this does not show
- One synthetic four-pipe network and one synthetic storm; no real system, no measured data.
- The cost curve and the uncertainty ranges are illustrative judgments.
- Engine is the prebuilt 5.2.2, not Bob's 5.2.4 build (the Emscripten toolchain could not be downloaded in the build session). Parity with native 5.2.4 holds on 17 small models only.
- Main-thread engine; a trapped run needs a page reload.
- The .out reader is local to this app (checked against engine text tables), not the shared results library.
- Lab 7's search samples 300 sets; it does not enumerate every acceptable fit.
- Follows the Bore Shell layout rules but is not stamped, because bore-shell.css was not available in the build session.
- No person has reviewed the text, the lab wording or the numbers.

## How to reproduce
From seven-studies-swmm-source.zip: `node test/run-all.js` regenerates build/facts.json and every number above (set SWMM524 to a native EPA SWMM 5.2.4 command-line binary; GLUE in test/harness.js points at the engine file); `node build.js` rebuilds the .html, this file and the .docx. In the app: Home, Run the base model; lab 4 shortcuts; lab 5 with 200 runs and seed 2026; lab 7 Load Fit 1 and Load Fit 2.

## Credits and licenses
EPA SWMM 5.2 (L. A. Rossman and the U.S. EPA), public domain. @fileops/swmm-wasm-web 0.0.4 (Issac Gardner), MIT. html2canvas (Niklas von Hertzen), MIT, loaded from cdnjs on demand. MCRS: Heaney, J. P., and Dickinson, R. E. (1982), Water Resources Research 18(3), 476-482. The seven-item list: an unattributed social media post. App code: Robert Dickinson, license to be chosen by him.

## AI use
Built with Claude, Anthropic's AI model, in one session in November 2026, at the request and under the direction of Robert (Bob) Dickinson, who supplied the list of seven ideas and whose standing rules set the form of the app and its documents. Claude designed the labs and the base model, wrote all code, tests, figures and text, and chose the cost curve and uncertainty ranges. Results were checked mechanically (engine text tables, native EPA SWMM 5.2.4, hand solution). No person has yet reviewed the app or its text. Responsibility for the published work is Bob's.

## Changes
`1.0.0 (2026-11-17)`: first build.

---
name: SWMM6 Always-On Calibrator
file: swmm6-always-on-calibrator.html
version: 1.0.0
date: 2026-11-18
author: Robert Dickinson
links: {netlify: none yet, artifact: see the published Claude artifact, repo: none}
engines:
  - {name: OpenSWMM Engine, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: 137e65e4e25e9425a489b99d5b7365c8355f8f6b, build: Emscripten 3.1.51 WebAssembly from BatchSWMMRunner client/public/wasm6, sha256: a857f2de88933edb7beb89704fa252e2bd13bf2fc8f35211ce29f161e3bbf463, license: Apache-2.0}
units: US customary (cfs, ft, hours); all four test models use CFS
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM6 Always-On Calibrator: OpenSWMM 6 calibrating test models in a browser tab, without stopping

A browser tab that keeps OpenSWMM 6 calibrating four test models without stopping; in 40 calibrations every fit reached the noise floor, yet only 4 recovered all three hidden multipliers within 5%.

The SWMM6 Always-On Calibrator runs the OpenSWMM 6.0.0-alpha.4 engine, compiled to WebAssembly, in a background thread of the page. It takes four test models in turn, hides three multipliers (impervious percent, subcatchment width, conduit Manning n), makes an observed hydrograph from them with 5% noise, and searches until the step size collapses. A measurement study ran 4,270 engine runs for 40 calibrations: every rerun of a hidden truth gave a byte-identical .out file, and every fit came within 0.001 of the noise floor's NSE. The parameters were another matter. The main limit: the observed flow comes from the same engine, so nothing here checks SWMM6 against SWMM5 or the field.

## What it does

Loads the OpenSWMM 6.0.0-alpha.4 engine (WebAssembly) into a Web Worker and runs a calibration loop until the page closes. Each calibration is a twin experiment on one of four test models: hide three multipliers, make an observed hydrograph at the conduit with the largest as-built peak, add noise, search from the as-built model. Results, checks and a resumable checkpoint stay in the browser. Built as the browser half of an always-on SWMM6 calibrator; a Netlify version would run the same core in 15-minute background-function slices.

## How it computes

- Report step forced to 00:05:00 in [OPTIONS]; nothing else in the model text changes except the three multiplied columns.
- Multipliers: [SUBCATCHMENTS] %Imperv (column 5, capped at 100), Width (column 6), [CONDUITS] Roughness (column 5). Search coordinate u in [0,1] maps to m = exp(ln lo + u (ln hi - ln lo)); ranges imperv 0.6 to 1.5, width 0.4 to 2.5, n 0.67 to 1.5. A multiplier whose values are all zero in the model is held at 1 (the Pressure Network's %Imperv).
- Hidden truth: u drawn uniformly in [0.15, 0.85]; observed = truth flow x (1 + k N(0,1)), floored at 0, k = noise (default 5%).
- Score: NSE = 1 - sum (Qsim - Qobs)^2 / sum (Qobs - mean)^2 at the observed link, all report periods.
- Search: (1+1) evolution strategy. Child u' = clip(u + sigma N(0,1)); keep if 1 - NSE(u') <= 1 - NSE(u); sigma x 1.5 on success, x 1.5^(-1/4) on failure (one-fifth rule); sigma0 = 0.25; stop when sigma < 0.003 or 200 engine runs.
- Every 25 trials the hidden truth is rerun and its .out SHA-256 compared with the first; resuming from a checkpoint does the same.
- Engine call sequence per run (fresh module instance each time): swmm_engine_create, open(inp, rpt, out, 0), initialize, start(h, 1) (the 1 saves results to the .out), step until elapsed = 0, end, report, close, destroy.
- Random numbers: mulberry32, state saved in the checkpoint; checkpoint format swmm6-always-on/1, about 4.3k characters.

## Inputs and outputs

- In: four bundled models (EPA Example 1; BatchSWMMRunner samples Session8_Yarra, Session47_pressure_net, Session30_LID_SUDS), or any .inp the viewer adds (needs [SUBCATCHMENTS] and [CONDUITS]).
- Out: CSV of finished calibrations; checkpoint JSON; a GIF drawn from the live charts. Binary .out files are read in memory and discarded.

## Checks

Study of 2026-11-18 (scripts/study.mjs, Node v22.23.4): 40 calibrations at 5% noise (4,270 engine runs) and 12 with no noise (1,350 runs).

| Model | Median runs | Impervious % | Width | Manning n | ms per run |
|---|---|---|---|---|---|
| EPA Example 1 | 125.5 | 1.1% (0.0%) | 4.3% (0.8%) | 1.8% (0.3%) | 45 |
| Yarra Storm Study | 89 | 1.9% (0.1%) | 49% (0.6%) | 23% (2.8%) | 67 |
| Pressure Network | 68 | held at x1 | 39% (32%) | 17% (7.0%) | 128 |
| LID and SUDS | 128 | 0.9% (0.1%) | 28% (27%) | 20% (15%) | 149 |

Median absolute multiplier error at 5% noise (no noise in brackets). ms per run: median of 30 interleaved runs per model, fresh instance included (scripts/timing.mjs).

- Truth reruns byte-identical: 186 of 186. Hidden truths that changed the .out: 52 of 52.
- Fit: every calibration ended within 0.001 of the hidden truth's own NSE; lowest NSE 0.9922. All three multipliers within 5%: 4 of 40 at 5% noise, 5 of 12 with none.
- Yarra width x n plane (17 x 17 runs, no noise, imperv x1): largest 1 - NSE 3.67e-4; 5% noise floor 1.86e-3.
- scripts/test.mjs: 20 assertions pass, including byte-identical reruns, a resume test with 7 interruptions giving identical results, refusal of a checkpoint from another engine build, and .out header values (version 60000, CFS, 300 s; Example 1 link 16 peak 18.247 cfs).
- Browser: headless Chromium 153.0.8010.12, 3 runs of 30 s: 312 to 364 engine runs, 592 to 691 runs per minute, no page errors, no horizontal scroll at 1280 and 390 px. A separate run drove the tour, GIF, CSV, checkpoint download and reload, the .docx download, an added model, pause and reset.
- Complexity: index 57.0 against HydroCouple = 100 (meter-core.js 1.7.0, baseline HC-2026-11-10-h); shipped .html alone 58.8.
- Human review: none yet.

## What this does not show

- Correctness of SWMM6: observed flow comes from the same engine; no comparison with EPA SWMM 5.2.4, other engines or field data.
- Real calibration conditions: noise is independent Gaussian; no gauge errors, timing offsets or missing data.
- Coverage: four small 1D models, three multipliers, one observed link each; no 2D, quality, controls or long continuous runs.
- Search: local (1+1) evolution strategy; no global optimum claimed.
- Speed: one cloud workspace; Netlify not measured; the Netlify slice version is not built.
- Defects found during the build (fixed): D-1 resume compared a real hash with an empty one when a checkpoint was saved before the truth run; D-2 the impervious multiplier was searched on a model whose subcatchments are all 0% impervious (first study: median error 9.9% on a parameter with no effect).

## How to reproduce

node scripts/test.mjs; node scripts/study.mjs (writes doc/data/study.json); node scripts/timing.mjs 30; node build.mjs; node doc/build-doc.mjs; node scripts/browser-test.cjs out/swmm6-always-on-calibrator.html 30.

## Credits and licenses

- OpenSWMM Engine, Copyright 2026 HydroCouple Developers (lead developer Caleb Buahin; Corinne Wiesner-Friedman), Apache License 2.0; upstream NOTICE reproduced in the About tab with the full license text. Portions derive from USEPA SWMM (public domain, 17 USC 105); the USEPA does not endorse this product.
- EPA SWMM 5: Lewis Rossman and the USEPA.
- Idea: NEER, "HEC-RAS 1D + 2D, in your browser", LinkedIn, November 2026.
- IBM Plex Sans and Mono (SIL OFL), from Google Fonts. No other outside code; the GIF encoder is the app's own.
- This app's own code: Copyright 2026 Robert Dickinson.

## AI use

Built with Claude, Anthropic's AI model, on 18 November 2026, under the direction of Robert (Bob) Dickinson, who proposed the app, chose the browser-first version and is responsible for the work. Claude chose the test models, wrote the calibration core, worker, page, GIF encoder and tests, ran the study, timing and browser runs, and wrote the Doc, .docx and this file. The engine was not changed. Checks are mechanical; no person has reviewed the code line by line yet.

## Changes

- 1.0.0 (2026-11-18): first version.

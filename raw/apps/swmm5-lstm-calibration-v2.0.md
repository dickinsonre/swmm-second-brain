---
name: "LSTM + SWMM5"
file: swmm5-lstm-calibration.html
version: 2.0
date: 2026-10-18
written: 2026-11-16
author: Robert Dickinson
links: {netlify: "https://lstm-swmm5-amin-talei.netlify.app", artifact: none recorded in the page, repo: "none recorded; the page names a release package, lstm-swmm5-v2.0.zip, without saying where it is"}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model tag v5.2.4 (7952ca8)", license: public domain, use: "swmm5.wasm, 517 KB, built with clang 18 for wasm32-wasi (-O2, -ffp-contract=off, wasi-libc); SHA-256 5e50cc3ec35e8e82da200693c7e3a99e256b8ce652c125ba3ea9b4207035cde7"}
  - {name: modpods, version: "dantzert/modpods@dda892d", use: "ported to JavaScript, with the Bayesian optimizer replaced by a pattern search (same bounds, budget and objective)"}
  - {name: LSTM, version: "the page's own code", use: "one layer, 16 cells by default"}
units: US customary (CFS, ft, in, in/hr, ac-ft)
ai_use: "The app was built with Claude (Anthropic) under Bob Dickinson's direction, as its own Use of AI section says. This summary was written by Claude from the published page. See AI use."
written_from: "the page served at https://lstm-swmm5-amin-talei.netlify.app (Netlify deploy 6ad54e3bd425b753ad207085, one index.html dropped on 2026-10-18 at 22:54 UTC; 2,220,095 characters; SHA-256 of the served text 6226a91f99274ede1f309f7a3ae5b150ac3ca83fdf4569c0ad0fe5f941d9689f), read tab by tab in a browser on 2026-11-16. Every number below is from the page's stored build-run results, its tables and its Evidence tab. Nothing was trained or calibrated to write this file. Opening the page runs the base demo model in SWMM once; that timing is not recorded here."
---

# LSTM + SWMM5: can an LSTM read a SWMM model, and can it calibrate one?

This summary was written after the fact. The page ships no technical summary file. It carries its version in its header ("v2.0 · 2026-10-18") and saves itself as `swmm5-lstm-calibration.html`, which is the `file:` above. The Netlify site name, `lstm-swmm5-amin-talei`, is not used anywhere in the page.

## What it does

Header: "EPA SWMM 5.2.4 runs here: calibrate through an LSTM, then confirm in SWMM." Six tabs: Calibrate, Verdict, Head-to-head, Inside the models, Your model, Evidence.

Two questions:
1. **Verdict and Head-to-head.** "Can an LSTM read the rainfall and runoff of a SWMM model?" An LSTM and a port of modpods learn the same SWMM5 response from 120 days of engine output at 15-minute steps, on six small models built to carry, or not carry, a hidden state.
2. **Calibrate.** Your .inp to SWMM5 to an LSTM to calibrated parameters to SWMM5 again: SWMM runs a Latin-hypercube sample of parameter multipliers, an LSTM learns rain plus parameters to flow, an optimizer searches through the LSTM, and SWMM confirms every answer before it is reported.

## How it computes

- LSTM, as the page writes it: forget, input, candidate and output gates; c = f ⊙ c₋ + i ⊙ g; h = o ⊙ tanh(c); ŷ = w · h + b. One layer, 16 cells by default, inputs z-scored on the training steps, backpropagation through time in 192-hour windows with the state carried across windows, Adam, cosine-decayed learning rate, gradient clip 1.0. The LSTM math uses + - × ÷ only, so a rerun "should match to the last bit on any browser".
- The forget gate as a recession constant: holding a cell's forget gate at f, each 15-minute step multiplies c by f, a linear reservoir with τ = -Δt / ln f. f = 0.953 gives τ = 5.2 h; 0.953 is σ(3), where the default bias starts every cell.
- modpods: a JavaScript port of `dantzert/modpods@dda892d` (`train.delay_io_train`, `model.SINDY_delays_MI`) with the Bayesian optimizer replaced by a pattern search; up to 4 transforms. "Conclusions are about that implementation (F-7)."
- Comparison setup: a seeded 120-day rain record with 31 storms (19.7 in), 15-minute steps. LSTM 16 cells, 80 epochs, 192-hour window. Three hold-outs: every 3rd storm, the largest storm, the last third. LSTM figures are the median of 5 seeds.
- Calibration demo: four subcatchments (70 ac, 15 to 80 % impervious, Horton), three conduits to one outfall, 42 days of rain, 4,032 periods at 15 min. Parameters are multipliers on every line they touch: subcatchment width × 0.25 to 4, % impervious × 0.7 to 1.3, pervious and impervious Manning n × 0.5 to 2, depression storage × 0.5 to 2, infiltration rate × 0.5 to 2, conduit Manning n × 0.7 to 1.4, RTK R × 0.5 to 2. The "observation" is a SWMM run with hidden multipliers: width × 0.60, % impervious × 1.15, pervious n × 1.50, infiltration rate × 0.70, conduit n × 1.10.
- Rain for the LSTM is read from the .inp gages as `gage.c` reads them and averaged over each report period.

## Verdict: held-out NSE (LSTM median of 5 seeds / modpods)

| Model | Hidden state | Every 3rd storm | Largest storm | Last third |
|---|---|---|---|---|
| P1 Horton memory | infiltration capacity, recovering between storms | 0.960 / 0.718 | 0.301 / 0.670 | 0.318 / 0.510 |
| P1c control, fast recovery | within-storm decay only | 0.938 / 0.595 | 0.274 / DIV | 0.307 / DIV |
| P2 RTK unit hydrographs | none (IA = 0) | 0.963 / 0.989 | 0.731 / 0.952 | 0.818 / 0.956 |
| P3 pond, orifice + weir | none the outflow does not reveal | 0.967 / -430.014 | 0.619 / 0.163 | 0.662 / -34.509 |
| P4 pump flow | wet-well level and pump state | 0.355 / 0.147 | 0.734 / -47.267 | 0.431 / -21.734 |
| P4 wet-well depth | same model, depth target | -0.050 / -4.457 | 0.022 / -2.778 | -0.431 / -6.207 |
| P5 tidal, rain only | a boundary the rain does not contain | -0.049 / DIV | 0.005 / DIV | -0.020 / -71.650 |
| P5 tidal, rain + tide | tide stage given to both | 0.997 / DIV | 0.843 / DIV | 0.978 / DIV |

DIV: the modpods simulation left the bounds (10 × the observed peak) before the record ended.

The page's readings: a linear response is modpods' home ground (P2); the LSTM wins interpolation on nonlinear responses (P1, P3); the P1c control says P1's gap is not antecedent memory; extrapolation flips the result (largest storm held out); a missing forcing beats both models (P5); the pump earns the cell state partial credit.

## Calibrate: the stored build run

- 1 series, 5 parameters, objective 1 - NSE. 62 SWMM runs, plus 135 for the polish and 477 for the direct search.
- LSTM on unseen parameter sets: median NSE 0.981 of 12; median absolute peak error 7 %.
- NSE on the calibration window: base 0.965 (verification 0.935); LSTM to SWMM 0.996 (0.976); response surface to SWMM 0.99913 (0.997); polished 0.99999 (0.99990); direct 0.99999 (0.99995); refined 0.99974 (0.99913).
- A quadratic response surface (median NSE 0.996) and a linear one (0.986) predict SWMM on unseen parameter sets better than the LSTM (0.981).

## Findings register (Evidence tab)

- F-1: a SWMM5 .out holds, at each report time, the gage intensity of the interval that starts there; on P1 the .out rainfall at period p equals the input for the next interval at 11,520 of 11,520 periods.
- F-2: an .out holds only reported objects; with no SUBCATCHMENTS, NODES or LINKS lines in [REPORT] it carries the 15 system series only.
- F-3: `bibo_stable` is not a stability guarantee; P5 with tide: ξ(q³) = 0, ξ(q²) = +9.72e-3, dq/dt R² 0.935, diverges at step 154.
- F-4: the fitted cubic can have a false stable resting flow; P3: rests at 0, 6.66 cfs (unstable) and 22.40 cfs (stable); held-out volume error 7715 %.
- F-5: near that separatrix the integrator decides the verdict; P3 last third: implicit solver NSE -34.509, fixed-step RK4 0.469.
- F-6: the kernels are not normalised; at shape 1, scale 1, loc 0 the sampled pdf sums to 1.582; at scale 0.1, 10.00.
- F-7: modpods has moved on; on 2026-10-14 the repository head was 3e039da, 101 commits after dda892d.
- F-8: on the calibration demo the WebAssembly engine is close to native, not identical: 56 of 4,032 periods differ, at most 0.102 cfs (0.41 % of peak), NSE 0.999996. The native build disagrees with itself when glibc's FMA code paths are switched off (4 periods, at most 0.047 cfs). The six probe models give byte-identical .out files.
- F-9: SWMM 5.2.4 applies a monthly rainfall adjustment one value late (`gage.c`); the first value of the run gets no adjustment and the first value of each month gets the previous month's factor. Matched by the page's test R-3b to 9 × 10^-8 in/hr.
- C-1 to C-9 (calibration): the LSTM gets a fit, not the parameters (conduit n × 0.70 against truth × 1.10); polishing from the LSTM optimum stalls at NSE 0.99646 after 164 runs in a second basin; the response surface beats the LSTM at interpolation; the LSTM's advantage is new rain (median NSE 0.969 on days 43 to 84, worst 0.938); refinement escapes the false basin (0.99637 to 0.99974 in 18 runs); a second gauge brings the parameters closer (RMS error of log multipliers 0.033 against 0.072 outfall-only and 0.038 direct); seeds matter (0.9932, 0.9952, 0.9937 on three repeats); 197 SWMM runs against 477, 58 s against 58 s on the 0.11 s demo; near-optimal ranges found through the LSTM exclude the truth.
- L-1: the LSTM did not learn the wet-well level (held-out NSE -2.27 to 0.14).

## Checks (as stated on the page)

- .out reader against EPA's `swmm_output` library: 6 files, 2,603,294 values, 0 mismatches.
- Engine reruns of P1, P1c and P4: .out byte-identical.
- LSTM backward pass against finite differences: 76 parameters, worst relative error 2.38e-7.
- exp, log and tanh against Math.*: errors 2.21e-16, 2.22e-16 and 2.22e-16 over 200k samples each.
- modpods kernel and convolution against scipy 1.18.1: 5.09e-14 and 6.92e-13 of peak.
- modpods integration against scipy LSODA (rtol 1e-10): implicit solver within 1.61e-06 of range on P3 last third; RK4 off by 3.48e-01 of range there.
- SWMM 5.2.4 WebAssembly against native: P1, P1c, P2, P3, P4, P5 .out byte-identical; calibration demo as F-8.
- An external AI review of version 1.2 (86/100, nine faults, 21 improvements): each fault reproduced against SWMM 5.2.4 or the shipped code, then fixed (R-1 to R-9); the page shows each faulty line as it was.
- A separate Claude instance that had not written the code checked version 2.0 against that review and found a CSV-import regression and several smaller faults, which were fixed.
- Human review: "No person has yet reviewed every number on the page, and nothing here has been tested against measured flow."

## What this does not show (the page's list, then this summary's)

1. No observed flow: the truth is EPA SWMM 5.2.4 output.
2. One synthetic 120-day rain record and six small models.
3. One LSTM architecture and training recipe; one modpods optimizer that replaces the repository's Gaussian-process step.
4. No forecasting with observed flow fed back, no ensembles, no multi-site training.
5. Uncertainty bounds come through the LSTM, not from a likelihood; big models are slow because every SWMM run is in the browser, one at a time.
6. Of the 21 suggested improvements, seven are only partly done (the page lists them).
7. (This summary.) The page has no About tab, no Doc tab and no technical summary file; its AI-use text is on the Evidence tab.
8. (This summary.) The page does not name Amin Talei, whose name the Netlify site carries.
9. (This summary.) The release package `lstm-swmm5-v2.0.zip` is named but its location is not given.

## Provenance (from the page)

- Engine: EPA SWMM 5.2.4, tag v5.2.4 (7952ca8), gcc -O2 with _FORTIFY_SOURCE off; "SWMM in this page": the swmm5.wasm in the front matter, run on an in-memory file system with the 15 WASI calls it needs.
- Rain record seed 20261014; 120 days at 15 min; 31 storms; 19.71 in; peak 1.412 in/hr.
- Build: node 22.22; scipy 1.18.1 and numpy 2.5.3 for the reference checks; evidence runs 2026-10-14; calibration build run 2026-10-18.
- SHA-256 of each model: P1.inp e85987e4c1d2c3ca0834510063fbf9ed28a63c11f5b00afd56ac588601a31dad; P2.inp 76b94aab3350266606ca959297b6f37cc08ec073d90d216b0255753781fcc35b; P3.inp 35f00ddb8c3c0d1505a590608edb14d6b2485c821ab42d827fab64f76478e49b; P4.inp 473b8fc84ea2a1aac26fa9b7d19bf2f0d27e7a2170a23203d02b27c7ebfe1c5d; P5.inp b3c74a5fa7a5879b7207902ed9ce29d327b98f3e96b3ba3ee2f10ec26070098b; calibration demo 265bf7d8d5ab96397cb8219d4d48af39d45ab832f1213ccabaf86a884bfb76d8 (the page also gives P1c and every .out).

## Inputs and outputs

- Reads: a SWMM5 .inp with its rain in [TIMESERIES] (files the .inp points to are not available); on Your model, a .inp + .out (and .rpt) set or a folder; an observed-flow CSV.
- Writes: a calibrated .inp, `calibration-series.csv`, `your-model-series.csv`, `lstm-vs-modpods-evidence.csv`, `swmm-run-log.csv`, an experiment file `lstm-swmm5-experiment.json`, the page itself, a GIF.
- Browser storage: theme (`lstm_modpods_theme`), welcome seen (`lstm_modpods_seen`).

## How to reproduce

On the Calibrate tab, "Run steps 2–4" at the demo settings; the page says the trained LSTM and the confirming SWMM run should come back bit-identical, compared by SHA-256. On Head-to-head, "Train both". The page says rebuilding from `lstm-swmm5-v2.0.zip` reproduces the page byte for byte.

## Credits and licenses

- EPA SWMM 5.2.4 (USEPA, public domain); EPA's `swmm_output` library.
- modpods: `dantzert/modpods`.
- No license is stated on the page for the app's own code.

## AI use

The page's own Use of AI section says the app was built with Claude, Anthropic's AI model, in Claude Code sessions from 14 to 18 October 2026, under the direction of Robert (Bob) Dickinson, who chose the questions, steered each round and is responsible for the work; Claude compiled the engine, wrote the LSTM, the modpods port, the calibration pipeline, the page, its tests and its text, and ran the build runs. The review of version 1.2 was written by another AI model. This summary was written by Claude on 16 November 2026 at Bob's request, from the published page; nothing was rerun, and no person has reviewed it.

## Changes

- 2.0 (2026-10-18): answers the external review of version 1.2 (R-1 to R-9), adds the calibration pipeline and its stored build run (from the page).

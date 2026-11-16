---
name: "Automatic Rainfall-Runoff Models: Evidence Atlas"
file: automatic-rainfall-runoff-models
version: 2026-08-21
date: 2026-08-21
written: 2026-11-16
author: Robert Dickinson
links: {netlify: "https://automatic-rainfall-runoff-models.netlify.app", artifact: none recorded in the page, repo: none recorded in the page}
engines:
  - {name: modpods fitted models re-run in the page (gamma kernels, convolution, RK4), version: "parameters from the pickled models in dantzert/automatic-rainfall-runoff-models; commit not given on the page", license: not stated in the page}
units: US customary where the data has units (junction invert depth in ft); NSE and the other metrics are ratios or percent
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page carries no AI-use note; one sentence on its Repo & method tab is written in the first person by the program that wrote the page. See AI use."
written_from: "the page served at https://automatic-rainfall-runoff-models.netlify.app (Netlify deploy 6a8838e8e1676b75ab3ff74c, one index.html dropped on 2026-08-21 at 11:39 UTC; 682,767 characters; SHA-256 of the served text 3d547ff9189cf5c2493bcee71564fcd638df5afc291fb432b53223fe542fa5c0), read tab by tab in a browser on 2026-11-16. No export was run. Opening the Live model tab re-runs one stored model in the browser; the numbers it computed then are not recorded here."
---

# Automatic Rainfall-Runoff Models: Evidence Atlas, every fit in the modpods replication package

This summary was written after the fact. The page ships no technical summary and no version number, so the version above is the date of the Netlify deploy. The page's title uses a dash between the two parts of its name; this file uses a colon. Every number below is copied from the page's text.

## What it does

The header: "Every fit in dantzert/automatic-rainfall-runoff-models, re-aggregated from the repo's own result files." That repository is the replication package for Dantzer et al., "Generating interpretable rainfall-runoff models automatically from data" (Advances in Water Resources, doi:10.1016/j.advwatres.2024.104796). The method itself lives in `dantzert/modpods`. The page: "Everything on every tab of this app was re-aggregated from those files. Nothing is quoted from the paper text."

Eight tabs: Overview, CAMELS scoreboard, SWMM surrogate, Live model, Complexity & cost, Selection defect, Atlas (2,476 fits), Repo & method.

## The headline numbers (Overview)

- modpods median NSE on CAMELS, 365 basins, evaluation period: 0.136.
- EA-LSTM median NSE, same basins, ensemble of 8 seeds: 0.751.
- modpods median NSE on SWMM junction depths, 181 junctions: 0.741.
- Total fitting time summed over every reported fit: 869 h.
- 2,476 fitted models across 415 sites in three datasets.
- The page's one sentence: "As a rainfall-runoff model for real catchments it loses to everything; as an emulator of a SWMM model's own output it works." On CAMELS, 130 of 365 basins at NSE ≤ 0, behind all thirteen published benchmarks.
- The page's explanation: on SWMM the target is a deterministic engine's output driven by a rainfall series the surrogate can see; on CAMELS the true forcing is partly unobserved (snow, soil moisture, groundwater, evapotranspiration), and "a convolution-plus-polynomial model has nowhere to put a hidden state".

| Dataset | Target | Sites | Fits | Median eval NSE | NSE ≤ 0 | Best |
|---|---|---|---|---|---|---|
| SWMM (Ann Arbor) | junction invert depth | 181 | 1082 | 0.7406 | 22 | 0.9935 |
| CAMELS basins | streamflow | 201 | 1206 | 0.1938 | 42 | 0.8799 |
| USGS gauges | streamflow | 27 | 188 | -0.0060 | 14 | 0.7382 |

Selection rule: best training NSE among the six configurations (polynomial order 1 to 3 × one or two transforms); the evaluation-period metrics of that configuration are reported.

## CAMELS scoreboard

Median NSE on the 365 basins modeled by modpods and all 13 benchmarks: LSTM (ensemble) 0.7619, EA-LSTM (ensemble) 0.7514, HBV (upper bound) 0.6753, mHM (basin calibrated) 0.6683, LSTM without static attributes (ensemble) 0.6653, FUSE 902 0.6527, FUSE 900 0.6373, FUSE 904 0.6233, SAC-SMA 0.6017, VIC (basin calibrated) 0.5449, mHM (CONUS calibrated) 0.5274, HBV (lower bound) 0.4165, VIC (CONUS calibrated) 0.3116, modpods 0.1358. modpods: 25th percentile -0.333, 75th 0.297, worst -1.20e+12. It beats the LSTM in 1 basin (0.3 %), EA-LSTM in 4 (1.1 %) and VIC (CONUS calibrated) in 108 (29.6 %).

The benchmark values come from the repository's `all_metrics.p`, the pickled metric set of Kratzert et al.'s EA-LSTM study (531 basins, 6 metrics, 13 models). Medians of the other metrics for modpods: alpha 0.782, beta 0.938, FHV 0.732, FLV 0.671, FMS 1.102 (alpha and beta are ratios where 1.0 is perfect; FHV, FLV and FMS are percent biases where 0 is perfect).

## SWMM surrogate

- From `swmm_modpods_eval.py`: an Ann Arbor SWMM model with about 1,200 junctions, read with `pyswmm.output.Output` from a pre-run `train.out` and `test.out`. The target is node invert depth, not flow. Every subcatchment shares one rainfall series.
- Junctions sampled by `[9:-1:30]`, then dropped if any of four held: range under 0.5 ft, first-step derivative over 50, non-zero initial depth, or a wet ending above 20 % of the peak. 181 junctions survive.
- Median evaluation NSE 0.7406; 22 of 181 at NSE ≤ 0; 75th percentile 0.887; best junction 93-80315 at 0.9935. 88 of 181 clear NSE 0.75 and 40 clear 0.9.
- The widest generalization gap: junction 91-51480 (p3t1), training NSE 0.8232, evaluation -6.173. The page's "poster child": 91-51076 (p3t2), training 0.9954, evaluation -4.535.

## Live model

Eleven stored models can be re-run in the browser from the repository's pickled parameters (six SWMM junctions, three CAMELS basins, two USGS gauges). For junction 93-80315 the page shows 7,200 timesteps at Δt = 1 min, two kernels and a degree-3 polynomial: 12 coefficients plus 6 kernel parameters, 18 in all; training NSE as reported by the repository 0.9964. Its static text: the re-run agrees with the stored simulation to 7.22e-3 absolute, 0.154 % of the simulated range at 900 plotted points, and an independent Python check over all 7,199 timesteps gives 0.164 %; the residual is attributed to forcing interpolation (scipy's `odeint` uses a cubic interpolant, the page uses linear RK4). Kernel 1 of that model sums to 1.021648. Slider ranges are the repository's bounds, with scale extended to 12 "because several fitted models sit above the stated bound".

## Complexity & cost (SWMM set)

| Config | Sites fitted | Median training NSE | Median eval NSE | Eval NSE ≤ 0 | Median fit time (min) |
|---|---|---|---|---|---|
| p1t1 | 181 | 0.7874 | 0.4922 | 36 | 17.8 |
| p1t2 | 181 | 0.8092 | 0.3577 | 61 | 17.8 |
| p2t1 | 154 | 0.8640 | 0.5782 | 31 | 19.9 |
| p2t2 | 135 | 0.8666 | 0.3473 | 48 | 19.9 |
| p3t1 | 180 | 0.8728 | 0.3882 | 67 | 21.2 |
| p3t2 | 180 | 0.8950 | 0.5869 | 54 | 21.2 |

Cost: median 19.2 minutes per site per polynomial order; worst single fit 59.8 h; 340 h for this dataset; 869 h across all three. The page: spending an hour instead of ten minutes "buys nothing systematic".

## Selection defect

- Defect 1: `max_so_far` is re-initialised inside the per-file loop, so the highest polynomial order present wins whatever its training NSE. In `non_camels_performance_summaries.py`, `CAMELS_performance_summaries.py`, `usgs_returns_from_training_length.py` and both root-level copies.
- Defect 2: the `p2t1` branch assigns the `p2t2` row and labels it `p2t1`. Present in all five copies; mostly latent.
- Proof on the SWMM set: emulating both defects reproduces the shipped `ensemble.csv` on 177/180 sites (NSE to 1e-4 and the label), 98.3 %.
- Selection rules on the SWMM set: as published 0.6909, 45/180 at NSE ≤ 0; intended (best training NSE over all six) 0.7406, 22/181; oracle (best evaluation NSE, an upper bound only, uses evaluation data) 0.7956, 7/181.
- The page: "This is a note worth sending the author, not a gotcha." There is no evaluation leakage in the intended design.

## Repo & method

- Folders: `camels_modpods_results/` 603 folders (203 basins); `swmm_modpods_results/` 541 folders (181 junctions); `usgs_modpods_results/` 94 folders (31 gauges). The same table calls `for_june2024_revision/revisions-code/` "the live results, 1,258 fitted-model folders".
- The CAMELS `ensemble.csv` covers 366 basins but only 203 basin folders are committed. In the SWMM `ensemble.csv` four junction IDs are cut at the first underscore (1771_PLYMOUTH_2 becomes 1771).
- Parameter count: 3m for the kernels plus degree × (1 + m) coefficients; m = 2 and degree 3 give 6 + 12 = 18.
- Correlations of CAMELS attributes with model parameters (not with skill), 14 rows; for example aridity with the first kernel's median response time 0.421.
- What a SWMM modeler should take from it, in the page's words: "This is an emulator technique, not a rainfall-runoff model"; "Training NSE tells you nothing"; "hold out storms, not timesteps"; "Thresholds alone are survivable; hysteresis and non-causality are not."

## Inputs and outputs

- Reads nothing from the user; all data is embedded.
- Writes: `camels_scoreboard.csv`, `config_sweep.csv`, `arrm_all_fits.csv` and per-table CSVs; `arrm-evidence-atlas.webm` (screen recording).
- Browser storage: theme (`arrm_atlas_theme`) and welcome seen (`arrm_atlas_seen`).

## Checks (as stated on the page)

- Gamma kernels reproducible to 10^-15 from the stored parameters (Overview).
- The re-run agreement above (Live model).
- The defect emulation, 177/180 (Selection defect).
- The page contains a self-test that reports its pass count to the browser console; its result was not read for this file.
- Human review: none recorded on the page.

## What this does not show

1. The folder counts on the Repo & method tab do not add up: 603 + 541 + 94 = 1,238, against the 1,258 stated in the same table.
2. The Overview's 415 sites match the folder counts (203 + 181 + 31); the dataset table's sites (181 + 201 + 27) sum to 409.
3. The page carries no version, no About tab, no Doc tab, no author's name and no AI-use note.
4. The page says of itself: "I do not have search or a bibliographic database here, so verify the DOI and the Kratzert citation against the originals before quoting them." Neither was verified for this file.
5. The 2,476-row Atlas table was not read row by row.

## How to reproduce

Open https://automatic-rainfall-runoff-models.netlify.app. Every table has a CSV button.

## Credits and licenses

- Data: `github.com/dantzert/automatic-rainfall-runoff-models` ("this app's only data source"); method `github.com/dantzert/modpods`; paper Dantzer et al., doi:10.1016/j.advwatres.2024.104796.
- Benchmark metrics in `all_metrics.p` from Kratzert et al.'s EA-LSTM regional modeling study; the repository's scripts credit `kratzert/ealstm_regional_modeling`.
- No license is stated on the page.

## AI use

This file was written by Claude (Anthropic) on 16 November 2026 at Robert Dickinson's request, from the published page, read in a browser. Nothing was rerun on purpose; opening the Live model tab re-runs one stored model automatically, and its live numbers are left out. The page does not say how it was built. No person has reviewed this summary.

## Changes

- 2026-08-21: the deploy read for this summary (Netlify, one index.html).

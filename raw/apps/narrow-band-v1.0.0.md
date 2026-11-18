---
name: The Narrow Band
file: narrow-band.html
version: 1.0.0
date: 2026-11-16
author: Robert Dickinson
links: {netlify: none yet, artifact: private claude.ai artifact, repo: none}
engines:
  - {name: narrow-band engine (JavaScript), version: 1.0.0, source: "port of R/functions.R in arab-fatemeh/Rainfall-Extremes-GEV-MEVD", license: MIT}
units: inches by default, millimetres on a toggle; the engine works in mm
ai_use: built with Claude (Anthropic); see AI use
---

# The Narrow Band: is the narrower uncertainty band the one to trust?

## In three points
- **What:** Refits Fatemeh Arab Sadeghabadi's GEV versus MEVD 200-year daily rain comparison on synthetic rain whose true value is known exactly.
- **So what:** On her Weibull generator the MEVD 90% band was 0.90 in wide against 2.31 in for GEV, yet it held the true 4.82 in in 28.8% of 1,000 records against 75.8% for GEV.
- **Now what:** Do not read a narrow band as a trustworthy one; check coverage against a known answer. Everything here is synthetic, and her R code was ported, not run.

The Narrow Band refits a published GEV-versus-MEVD comparison on synthetic rain whose true 200-year value is known, and finds the MEVD band, 2.6 times narrower, held that value in only 29% of 1,000 records against 76% for GEV.

A November 2026 post by Fatemeh Arab Sadeghabadi compared two ways of estimating a 200-year daily rain from 30 years of record, and found the 90% uncertainty band of the newer method, MEVD, far narrower than that of the classical GEV. Her code includes a synthetic rain generator, so the true answer can be computed exactly. This app rebuilds her analysis in the browser, draws the true value on the chart, and counts how often each band contains it. Across 1,000 independent records the GEV band held the truth 76% of the time and the MEVD band 29%. A third fit, added here, does better on her generator and worse elsewhere. Everything is synthetic; no real gauge was tested.

## What it does
Estimates a T-year daily rain (default 200) from a window of synthetic daily rain (default 30 years) three ways, puts a 90% bootstrap band on each, and compares all three with the exact true value of the generator. It answers one question for engineers who extrapolate design rain from short records: does a narrow band mean a trustworthy estimate. Output: a sliding-window chart, a coverage count over independent records, a diagnosis of the MEVD bias, and CSV tables.

## How it computes
All depths in mm inside the engine. Wet day: rain > 1 mm; fits use the excess above 1 mm and add 1 mm back.

1. Rain models (excess e on a wet day; wet-day probability p_d = 0.25 + 0.10 cos(2 pi (d - 300)/365)):
   - weibull: e = 7 (-ln(1-u))^(1/w), w = 0.8 by default (her generator, example/make_synthetic_data.R)
   - mix: with probability 0.12, Weibull(scale 9, shape 0.62); otherwise Weibull(scale 6.5, shape 0.95)
   - gpd: generalised Pareto, scale 7, xi = 0.12
   - depths rounded to 0.1 mm, as in her generator
2. GEV: L-moment fit to the window's annual maxima (Hosking 1990), k = 7.8590 c + 2.9554 c^2, c = 2/(3 + t3) - ln2/ln3; quantile x = loc + scale/shape ((-ln F)^(-shape) - 1). Source: gev_lmom, gev_quant in R/functions.R.
3. MEVD, per-year fit: Weibull by probability weighted moments on each year's excesses (wei_pwm), then solve (1/n) SUM_j [1 - exp(-(x/C_j)^w_j)]^N_j = F, F = 1 - 1/T (mev_quant). The page solves it by false position on log(-log F); her code uses uniroot.
4. MEVD, pooled fit (added here): one PWM Weibull on all excesses in the window, each year's own N_j in the same formula.
5. Bootstrap: resample the window's years with replacement, same resampled years for all three estimators; band = 5th to 95th percentile (R type 7 quantile).
6. True value: solve PROD_d [1 - p_d S(x - 1)] = F over the 365 days, S = survival function of the excess. No data, no fitting.
7. Coverage: share of independent records whose band contains the true value.

## Inputs and outputs
No input files. Settings: rain model and one tail parameter, return period (50, 100, 200, 500), window (20, 30, 50 years), bootstraps (200, 300, 500), seed, units. Outputs: narrow-band-windows.csv (one row per window), narrow-band-coverage.csv (one row per record), narrow-band-demo.webm (recorded walkthrough).

## Checks
Reference run: tools/refrun.js, 1000 independent 30-year records per model, 300 bootstraps, T = 200, seeds 2026 to 2028. Depths in inches.

| Rain model | True | GEV mean | GEV width | GEV holds | MEVD mean | MEVD width | MEVD holds | Pooled mean | Pooled width | Pooled holds |
|---|---|---|---|---|---|---|---|---|---|---|
| Weibull days | 4.82 | 4.93 | 2.31 | 75.8% | 5.49 | 0.90 | 28.8% | 4.68 | 0.66 | 78.8% |
| Two storm types | 9.55 | 11.16 | 7.31 | 78.7% | 5.54 | 1.52 | 3.8% | 3.95 | 0.77 | 0.0% |
| Pareto-tailed days | 5.20 | 5.26 | 2.79 | 71.7% | 4.35 | 0.71 | 14.1% | 3.65 | 0.51 | 0.0% |

Mechanical checks:
- 14 of 14 engine values match a Python port of her R code (test/ref.json; tolerances 1e-12 to 1e-6). Recomputed in the browser on the Verify tab.
- Two programs, one experiment: the JS engine and the Python port (mevd_check.py, 1,000 records; mevd_diag.py, 600 records for the pooled fit) agree on mean, median width and coverage for all 9 model-and-method pairs within Monte Carlo noise.
- Port against her README: one 150-year Weibull record, 30-year windows, 500 bootstraps: median 90% width GEV 69.2 mm, MEVD 22.9 mm (Python port: 71 and 24 mm; her README: about 75 mm and 20 to 30 mm).
- True value, Weibull days: formula 122.52 mm; 400000 simulated years 122.35 mm.
- MEVD formula with the true parameters and each year's N: mean 122.21 mm against 122.52 mm.
- Single-year Weibull shape: mean 0.824, standard deviation 0.078 (true 0.80). Thirty identical years with that scatter in the shape read 140.8 mm; the reference MEVD mean is 139.5 mm.
- Complexity: the Meter's analyzer could not be run in this build; raw counts only: 10 source files, 1812 non-blank lines, 275 functions.

Human review: none yet.

## What this does not show
1. No real gauge data. Everything is synthetic.
2. Days are independent and the climate does not change from year to year, so per-year fitting has nothing real to follow.
3. Her R code was ported, not executed (no R in the build session).
4. The mix and gpd models are this app's own and were chosen to be hard on a Weibull.
5. Reference numbers cover T = 200, 30-year windows, 300 bootstraps only (her default is 500).
6. Only the percentile bootstrap of years was tried.
7. No person has reviewed the engine or the essay line by line.

## How to reproduce
1. python3 test/make_ref.py (reference vectors from the Python port; needs mevd_check.py)
2. node tools/refrun.js 1000 300 (engine checks, then the reference run to dist/results.json; about one minute)
3. node tools/build.js (page and this file), node tools/docx.js (the essay as .docx)
In the page: Coverage tab, 1000 records, default settings, reproduces the first table row within Monte Carlo noise.

## Credits and licenses
- Fatemeh Arab Sadeghabadi: the R analysis and synthetic generator this app re-implements. https://github.com/arab-fatemeh/Rainfall-Extremes-GEV-MEVD, MIT License, copyright 2026 Fatemeh Arab Sadeghabadi.
- MEVD: Marani and Ignaccolo (2015); Zorzetto, Botter and Marani (2016). L-moments: Hosking (1990). Probability weighted moments: Greenwood, Landwehr, Matalas and Wallis (1979). Bootstrap: Efron (1979).
- This app: MIT License, Robert Dickinson, 2026.

## AI use
This app was built with Claude, Anthropic's AI model, in one session in November 2026, at the direction of Robert (Bob) Dickinson. He chose the post to examine and asked for the app; responsibility for publishing it is his. Claude read the R code, ported the fitting functions to Python and then to JavaScript, designed the truth-known test and the two extra rain models, ran the experiments, and wrote the page, the essay, the .docx and this file. The checks are mechanical (listed above). No person has reviewed the code or the essay line by line, the R code was not executed, and nothing has been tried on a real gauge.

## Changes
1.0.0 (2026-11-16): first version.

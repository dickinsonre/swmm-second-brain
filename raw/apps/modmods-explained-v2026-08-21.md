---
name: "modpods, for a SWMM person"
file: modmods-explained
version: 2026-08-21
date: 2026-08-21
written: 2026-11-16
author: Robert Dickinson
links: {netlify: "https://modmods-explained.netlify.app", artifact: none recorded in the page, repo: none recorded in the page}
engines:
  - {name: modpods method, ported to JavaScript in the page, version: "dantzert/modpods commit dda892dd83850a28428bded12d08c6a58c354569, dated 2026-08-12", license: not stated in the page}
units: timesteps inside the page; T in hours in the [HYDROGRAPHS] exports, after a timestep of 5, 15, 60 or 360 minutes is declared
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page itself carries no AI-use note and does not say who or what built it. See AI use."
written_from: "the page served at https://modmods-explained.netlify.app (Netlify deploy 6a88394348c3fe9b8589b375, one index.html dropped on 2026-08-21 at 11:40 UTC; 96,599 characters; SHA-256 of the served text db4a9d0a47d32b5e274cf54ba18f626dddab3fb5ca1eaae447ea055f84883389), read tab by tab in a browser on 2026-11-16. No fit, probe or export was run to write this file."
---

# modpods, for a SWMM person: Dantzer's gamma-kernel method read as a fitted unit hydrograph

This summary was written after the fact. The page ships no technical summary of its own and no version number, so the version above is the date of the Netlify deploy. Every number below is copied from the page's static text. The page computes its fits live in the browser; no fit was run for this file, so none of the page's live results is recorded here.

The Netlify site name spells the method "modmods". The page's own title, exports and theme key all spell it "modpods".

## What it does

It explains modpods, the method of Dantzer et al. for discovering rainfall-runoff models from data, to a SWMM modeler. The page's one-sentence claim: "modpods replaces the RTK triangle with a gamma PDF and fits its parameters instead of asking you to pick them." The engine in the page is described as a JavaScript port of the repository's own steps. Seven tabs, one idea each:

1. **The kernel.** The gamma PDF as a unit hydrograph, with sliders for shape α, scale θ (in timesteps, capped at the repository's bound of 5.0) and pure delay d, and the moment-matched RTK triangle drawn beside it.
2. **Convolve.** Rainfall convolved with two kernels into two latent states, "two effective subcatchments".
3. **Discover.** dq/dt regressed on powers of the state, the rain and the latent inputs (the SINDy step), for three built-in signals.
4. **Fit.** The outer loop: search the gamma parameters, add a kernel, stop when the next one buys less than 0.5 %; a train and validation split; CSV import.
5. **Where it breaks.** Five signals a SWMM model can produce, fitted in turn ("the smoothness probe").
6. **The repo.** What is in `dantzert/modpods`, read from the repository at a named commit.
7. **The evidence.** Results from the replication package `dantzert/automatic-rainfall-runoff-models`.

## How it computes (as the page states it)

- Kernel: f(t) = (t - d)^(α - 1) · exp(-(t - d)/θ) / (θ^α · Γ(α)) for t ≥ d, sampled at integer timesteps; the page says this is exactly `scipy.stats.gamma.pdf(t, a=α, scale=θ, loc=d)`, as the repository calls it.
- Two readings of the same three numbers. Nash cascade: α is the number of linear reservoirs in series, θ the storage constant of each, d a pure translation; α = 1 is a single linear reservoir with no rising limb. RTK triangle by moment match: T (time to peak) = the gamma mode = (α - 1)θ + d; K = 3·mean/T - 2, so the two centroids agree.
- The kernel is not normalised. The sampled pdf sums near 1 and drifts with the parameters, so the volume gain ends up in the fitted coefficient. To read an RTK R out of a fitted model, multiply the coefficient by the kernel's sum and renormalise.
- Convolution: T_i(p)(t) = Σ over τ = 0..t of f_i(τ) · p(t - τ); the repository's call is `signal.fftconvolve(forcing, kernel, mode='full')[:n]`.
- Regression: dq/dt = Σ over k = 1..P of [a_k q^k + b_k p^k + Σ_i c_i,k T_i(p)^k], with `PolynomialLibrary(degree=P, include_bias=False, include_interaction=False)` and dq/dt from `FiniteDifference()`. BIBO constraint: a_P ≤ 0.
- "SINDy" without the sparsity: the repository's default optimizer is `STLSQ(threshold=0)` and its BIBO path is `ConstrainedSR3(reg_weight_lam=0, regularizer='l2')`. The page: "Both mean ordinary least squares."
- Fit tab defaults: max kernels 3, polynomial order 3, early stop at a minimum R² gain of 0.005, train and validation split 70 %. The page shows R² on dq/dt and the score of the integrated series side by side and says "they are not the same question".

## Repository facts the page records (tab 6)

| Setting | Value | Where |
|---|---|---|
| poly_order | 3 | train.py |
| max_transforms | 4 | train.py |
| early_stopping_threshold | 0.005 | train.py |
| optimization_method | 'bayesian' | train.py |
| bibo_stable | False | train.py |
| include_bias / include_interaction | False / False | train.py |
| search bounds, shape | [1.0, 50.0] | train.py bounds_list |
| search bounds, scale | [0.1, 5.0] | train.py bounds_list |
| search bounds, loc | [0.0, 20.0] | train.py bounds_list |
| first transform seeded at | [1, 1, 0] | train.py |
| an added transform starts at | shape = 10·(m - 1) | train.py |

API named: `delay_io_train`, `delay_io_predict` (scores MAE, RMSE, NSE, alpha, beta, HFV, LFV, FDC), `transform_inputs`, `infer_causative_topology`, `lti_system_gen` / `lti_from_gamma`.

Three things the page says a blog post (not named on the page) and the repository state differently: the paper writes the gamma with a rate β while the repository passes a scale, so scale = 1/β; the kernel is not normalised; and the sparsity is switched off.

The page's mapping to SWMM5, one line each: m kernels against three RTK unit hydrographs per month in `rdii.c`; gamma PDF (α, θ, d) against the triangle (T, K); kernel gain absorbed into the coefficient against R, the fraction of rainfall volume; add kernels until the gain drops below 0.5 % against "you pick 3 and stop"; fitted dq/dt polynomial against dd/dt = i - e - f - q(d) with q from Manning; BIBO imposed as a constraint against "free: outflow is monotone in depth".

## Where it breaks (tab 5, the page's text)

- Fits: the SWMM5 nonlinear reservoir ("a cubic just approximates Manning's 5/3 power") and the weir crest. The page's reason for the weir: with `include_bias=False` every library term is a power of q or of the forcing, so q = 0 with no rain gives dq/dt = 0 "for free".
- Fails: the pump, which "carries a hidden binary state, so the same q means two different futures", and tidal backwater, where "the response depends on a downstream head the model never sees".
- The page's qualification: this formulation cannot represent them "without adding the missing state or the missing downstream forcing". A pump-status input, or the downstream head as a second forcing series, makes both tractable again.
- The page's reading: "Where a fitted low-order model collapses is where the dynamic-wave machinery is actually earning its keep."

The tab shows no stored numbers; the five fits are run live by the "Run all five" button.

## The evidence tab (tab 7), as stated

- The replication package: 5.4 GB, 1,258 fitted-model folders (610 CAMELS basins, 547 SWMM, 101 USGS), each with training and evaluation metrics and a pickled model.
- Median evaluation NSE on 365 CAMELS basins: LSTM 0.762, EA-LSTM 0.751, HBV-ub 0.675, mHM-basin 0.668, SAC-SMA 0.602, VIC-CONUS 0.312, modpods 0.136. modpods: 130 of 365 basins at NSE ≤ 0; worst basin -1.2×10^12. It beats EA-LSTM in 1.1 % of basins and VIC-CONUS in 30 %.
- On SWMM output: median evaluation NSE 0.74, best junction 0.9935. The page's conclusion: "modpods is not competitive as a rainfall-runoff model, but it is competitive as a surrogate for a deterministic engine."
- Two defects in the published summary scripts (`non_camels_performance_summaries.py`, `CAMELS_performance_summaries.py`, `usgs_returns_from_training_length.py` and both root-level copies): `max_so_far = -10e6` is reset inside the per-file loop, so the last folder walked wins; and the `p2t1` branch copies the `p2t2` row. Emulating the buggy rule reproduces the shipped `ensemble.csv`, value and label, on 177/180 SWMM, 193/200 CAMELS and 23/27 USGS sites.
- Correcting the rule: SWMM median evaluation NSE 0.6909 to 0.7406, sites at NSE ≤ 0 45 to 22; CAMELS 0.1695 to 0.1938, 57 to 42. "The correction runs in the paper's favour."
- Overfitting: worst single case named on the page, junction 91-51076, training NSE 0.9954, evaluation NSE -4.54.
- Cost: 340 h of fitting for the SWMM set; median 19 min per junction per order; worst single junction 60 h.
- Reconstruction: gamma kernels rebuilt from stored shape, scale and loc reproduce the package's `precipitation_tr_1/2` columns to 6.7×10^-16; RK4 with linearly interpolated forcing reproduces the stored simulations to 0.04 to 0.9 % of range. One stored kernel sums to 1.0216.

## Inputs and outputs

- Reads: a CSV of time, rain and flow on the Fit tab (the page's control is labeled "my CSV (time, rain, flow)").
- Writes: `modpods_hydrographs_illustrative.inp`, `modpods_hydrographs_fitted.inp` ([HYDROGRAPHS] for SWMM5), `modpods_kernel.csv`, `modpods_fit.csv`, `modpods_smoothness_probe.csv`, `modpods_replication_evidence.csv`, `modpods_validation_report.txt`; a GIF of the screen.
- Browser storage: theme (`modpods_theme`) and whether the welcome has been seen (`modpods_seen`).

## Checks (as stated on the page)

- "Verified here, not asserted." Each step of the port was checked against scipy before it was allowed in: gamma pdf to 1e-12, convolution to 1e-10, the derivative to 1e-12.
- Provenance table: method repository `dantzert/modpods`, commit `dda892dd83850a28428bded12d08c6a58c354569`, commit date 2026-08-12; repository pins numpy ≥ 1.24, scipy ≥ 1.10, pysindy ≥ 2.0; validated against scipy 1.17.1 and numpy 2.4.4 on 2026-08-15.
- The two script defects: "Both lines were re-read directly from the published source when this tab was built."
- Human review: none recorded on the page.

## What this does not show

1. No number from the live tabs (Discover, Fit, Where it breaks) is recorded here, because none was run.
2. The page names no author, carries no version, no About tab, no Doc tab and no AI-use note.
3. The page does not name the people behind the method beyond the repository owner `dantzert` and the paper's DOI, and does not name the blog post it compares against.
4. The page's "Download validation report" is generated live; its contents were not read.
5. Nothing here was checked against the repositories again.

## How to reproduce

Open https://modmods-explained.netlify.app, press Train on the Fit tab and "Run all five" on the Where it breaks tab, and download the validation report from The repo tab.

## Credits and licenses

- The method: `github.com/dantzert/modpods`; the paper doi:10.1016/j.advwatres.2024.104796 (the page footer).
- The replication package: `dantzert/automatic-rainfall-runoff-models`.
- The benchmark set: Kratzert's (the page names "Kratzert's set" and "Kratzert benchmark").
- No license is stated on the page for the page or for the port.

## AI use

This file was written by Claude (Anthropic) on 16 November 2026 at Robert Dickinson's request, from the published page, read in a browser. Nothing was rerun. The page itself carries no statement of how it was built. No person has reviewed this summary.

## Changes

- 2026-08-21: the deploy read for this summary (Netlify, one index.html).

---
title: "Where a surrogate of SWMM breaks: hidden state and missing forcing"
type: concept
updated: 2026-11-16
sources: [S155, S156, S157]
tags: [surrogates, machine-learning, modpods, lstm, dynamic-wave]
reviewed: no
---
A surrogate learns SWMM's response from rain to flow or depth and then runs without SWMM. Bob's three apps on [modpods](../entities/modpods.md) and on LSTMs agree on where that works and where it stops. All three sources are summaries Claude wrote from the app pages, not yet read by Bob (Q84).

**The claim.** A model driven by rain alone fails where the response depends on something the rain does not carry: a hidden state (a pump's on or off, a storage that the outflow does not reveal) or a missing forcing (a tide, a downstream head). Thresholds alone are not the problem [S155](../sources/S155-modpods-explainer-summary.md) [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**Why a threshold survives.** modpods' polynomial has no bias term, so every term is a power of q or of a forcing; with q = 0 and no rain, dq/dt = 0 by construction. A weir crest therefore fits [S155](../sources/S155-modpods-explainer-summary.md).

**Why a pump does not.** A pump "carries a hidden binary state, so the same q means two different futures". Tidal backwater depends on "a downstream head the model never sees". Given the missing state or forcing as an input, both become tractable [S155](../sources/S155-modpods-explainer-summary.md).

**The measurement.** The [LSTM + SWMM5 (app)](../entities/lstm-swmm5-app.md) trained an LSTM and a modpods port on six small SWMM5 models, 120 days of 15-minute output. Held-out NSE with every third storm held out, LSTM median of 5 seeds against modpods [S157](../sources/S157-lstm-swmm5-summary.md):

| Model | What the rain does not carry | LSTM | modpods |
|---|---|---|---|
| P2 RTK unit hydrographs | nothing (linear) | 0.963 | 0.989 |
| P1 Horton memory | infiltration capacity | 0.960 | 0.718 |
| P3 pond, orifice + weir | nothing the outflow hides | 0.967 | -430.014 |
| P4 pump flow | wet-well level, pump state | 0.355 | 0.147 |
| P4 wet-well depth | the same | -0.050 | -4.457 |
| P5 tidal, rain only | the tide | -0.049 | diverged |
| P5 tidal, rain + tide | nothing | 0.997 | diverged |

Three readings the page makes [S157](../sources/S157-lstm-swmm5-summary.md):
- A linear response (the RTK model) is modpods' home ground.
- Extrapolation flips the ranking. With the largest storm held out, the LSTM falls to 0.301 on P1 and modpods keeps 0.670.
- A missing forcing beats both. Given the tide, the LSTM reaches 0.997 and modpods still diverges; its stability-constrained fit has dq/dt R² 0.935 and leaves the bounds at step 154.

**The cell state did not hold the level.** The LSTM did not learn the wet-well level: held-out NSE -2.27 to 0.14 [S157](../sources/S157-lstm-swmm5-summary.md).

**A pond can fail without hidden state.** On P3 the fitted cubic rests at 0, at 6.66 cfs (unstable) and at 22.40 cfs (stable), a false resting flow; the held-out volume error is 7715 %. Near that point the integrator decides the verdict: RK4 gives NSE 0.469 and the implicit solver -34.509 [S157](../sources/S157-lstm-swmm5-summary.md).

**At scale.** On 181 junctions of an Ann Arbor SWMM model, modpods' median evaluation NSE is 0.7406, against 0.1358 on 365 real catchments, where snow, soil moisture and groundwater are part of the forcing and unobserved [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**What it means for a SWMM modeler, as the pages put it.** "Where a fitted low-order model collapses is where the dynamic-wave machinery is actually earning its keep" [S155](../sources/S155-modpods-explainer-summary.md). Training NSE says little: one junction trained at 0.9954 and evaluated at -4.535; hold out storms, not timesteps [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**What none of it shows.** No observed flow in the LSTM comparison; one synthetic rain record and six small models [S157](../sources/S157-lstm-swmm5-summary.md).

**Related.** [A surrogate distilled from SWMM](surrogate-distilled-from-swmm.md), Bob's earlier idea; [Calibrating SWMM through a surrogate](calibrating-through-a-surrogate.md).

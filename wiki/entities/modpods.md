---
title: modpods (Dantzer's method)
type: entity
updated: 2026-11-16
sources: [S155, S156, S157]
tags: [modpods, surrogates, machine-learning, rdii]
reviewed: no
---
A method for discovering rainfall-runoff models from rainfall and runoff alone, by Dantzer et al., "Generating interpretable rainfall-runoff models automatically from data", Advances in Water Resources, doi:10.1016/j.advwatres.2024.104796 [S156](../sources/S156-arrm-evidence-atlas-summary.md). The code is `github.com/dantzert/modpods`; the paper's results are in a separate replication package, `dantzert/automatic-rainfall-runoff-models` [S155](../sources/S155-modpods-explainer-summary.md). Bob's three apps on it are [modpods, for a SWMM person](modpods-explainer-app.md), the [Evidence Atlas](arrm-evidence-atlas.md) and [LSTM + SWMM5](lstm-swmm5-app.md).

**How it works, in the repository's terms** [S156](../sources/S156-arrm-evidence-atlas-summary.md)
1. Transform: convolve rainfall with m gamma-PDF kernels sampled at integer timesteps, three parameters each (shape, scale, loc).
2. Discover: fit dq/dt as a polynomial in q and the transformed forcings, degree 1 to 3, no bias term, no interaction terms.
3. Search: an Optuna outer loop tunes the gamma parameters, stopping when improvement falls below 0.5 %.

With m = 2 and degree 3 the model has 6 + 12 = 18 parameters [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**As a SWMM modeler would read it.** The gamma kernel is a unit hydrograph: as a Nash cascade, shape α counts linear reservoirs and scale θ is each one's storage constant; by moment match it gives an RTK triangle with T = (α - 1)θ + d and K = 3·mean/T - 2 [S155](../sources/S155-modpods-explainer-summary.md). See [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md).

**Three things the name and the paper hide** [S155](../sources/S155-modpods-explainer-summary.md) [S156](../sources/S156-arrm-evidence-atlas-summary.md)
- The sparsity is off. The default optimizer is `STLSQ(threshold=0)` and the stable path `ConstrainedSR3(reg_weight_lam=0, regularizer='l2')`: ordinary least squares.
- The kernel is not normalised; the volume gain sits in the coefficient. One stored kernel sums to 1.0216 [S155](../sources/S155-modpods-explainer-summary.md); at the first seed (shape 1, scale 1, loc 0) the sum is 1.582 [S157](../sources/S157-lstm-swmm5-summary.md).
- The paper writes a rate β; the repository passes scale = 1/β.

**Repository defaults at commit dda892dd (2026-08-12)** [S155](../sources/S155-modpods-explainer-summary.md): poly_order 3, max_transforms 4, early stopping 0.005, `bibo_stable` False, search bounds shape [1.0, 50.0], scale [0.1, 5.0], loc [0.0, 20.0]. On 14 October 2026 the repository head was 3e039da, 101 commits later [S157](../sources/S157-lstm-swmm5-summary.md).

**What the replication package shows** [S156](../sources/S156-arrm-evidence-atlas-summary.md)
- On 365 CAMELS basins its median evaluation NSE is 0.1358, last of 14 models; the LSTM ensemble's is 0.7619.
- On junction depths of an Ann Arbor SWMM model, median 0.7406 (intended selection rule) and best 0.9935.
- Discovery cost: 869 h of fitting across the three datasets.

Both apps built from the package read the gap the same way: a surrogate of a deterministic engine, not a rainfall-runoff model [S155](../sources/S155-modpods-explainer-summary.md) [S156](../sources/S156-arrm-evidence-atlas-summary.md). Why, and where it fails, is on [Where a surrogate of SWMM breaks](../concepts/surrogates-hidden-state-missing-forcing.md).

**Two defects in the package's summary scripts**, found by Bob's apps: a running maximum reset inside the per-file loop, and a `p2t1` branch that copies the `p2t2` row. Fixing them raises the SWMM median from 0.6909 to 0.7406 [S155](../sources/S155-modpods-explainer-summary.md) [S156](../sources/S156-arrm-evidence-atlas-summary.md). Neither page says the authors were told.

**Stability is not guaranteed.** `bibo_stable` constrains only the q³ coefficient; on a tidal model with the tide given, the fit put that coefficient at 0 and a positive q² term, and the simulation diverged at step 154 [S157](../sources/S157-lstm-swmm5-summary.md).

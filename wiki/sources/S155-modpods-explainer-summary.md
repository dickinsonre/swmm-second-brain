---
title: "S155: modpods, for a SWMM person, summary written from the page (deploy of 2026-08-21)"
type: source
raw: raw/apps/modmods-explained-v2026-08-21.md
kind: app-md
author: Robert Dickinson
published: 2026-08-21
ingested: 2026-11-16
tags: [apps, modpods, surrogates, rdii, machine-learning, netlify]
reviewed: no
---
**What it is.** A technical summary of the app "modpods, for a SWMM person", the page served at modmods-explained.netlify.app, deployed 21 August 2026. The app explains Dantzer's modpods method to a SWMM modeler as a fitted unit hydrograph, in seven tabs. Raw file: [raw/apps/modmods-explained-v2026-08-21.md](../../raw/apps/modmods-explained-v2026-08-21.md).

**How it was written. This one is different.** The page ships no summary and no version number. Claude (Anthropic) wrote the file on 16 November 2026, at Bob's request, from the live page, read tab by tab in a browser. Nothing was fitted or rerun, so none of the page's live results is in it. Bob has not read it (Q84). The page itself carries no AI-use note and names no author.

**Claims worth keeping** (all copied from the page)
- The page's one sentence: modpods "replaces the RTK triangle with a gamma PDF and fits its parameters instead of asking you to pick them."
- The kernel is `scipy.stats.gamma.pdf(t, a=α, scale=θ, loc=d)` sampled at integer timesteps. Read as a Nash cascade, α is the number of linear reservoirs and θ the storage constant of each. Read as an RTK triangle by moment match, T = (α - 1)θ + d and K = 3·mean/T - 2.
- The kernel is not normalised: its sampled sum drifts with the parameters, and the volume gain sits in the fitted coefficient. Reading an RTK R out of a fit means multiplying the coefficient by the kernel's sum.
- dq/dt is regressed on powers of q, the rain and the convolved rain, with no bias and no interaction terms. The repository's optimizers are `STLSQ(threshold=0)` and `ConstrainedSR3(reg_weight_lam=0, regularizer='l2')`: "Both mean ordinary least squares."
- Repository defaults read at commit `dda892dd` (2026-08-12): poly_order 3, max_transforms 4, early stopping 0.005, search bounds shape [1.0, 50.0], scale [0.1, 5.0], loc [0.0, 20.0]. The paper writes a rate β; the repository passes scale = 1/β.
- Where it breaks: the nonlinear reservoir and the weir fit; the pump (a hidden binary state) and tidal backwater (a downstream head the model never sees) fail. Adding the missing state or forcing makes them tractable again.
- The port was checked against scipy: gamma pdf to 1e-12, convolution to 1e-10, derivative to 1e-12; validated against scipy 1.17.1 and numpy 2.4.4 on 2026-08-15.
- From the replication package (tab 7): 1,258 folders (610 CAMELS, 547 SWMM, 101 USGS); modpods median evaluation NSE 0.136 on 365 CAMELS basins against LSTM 0.762; 0.74 on SWMM output, best junction 0.9935; two defects in the summary scripts; corrected SWMM median 0.6909 to 0.7406.

**Limits it states.** None for the method beyond tab 5. This summary adds: no live number recorded; no version, author, About tab, Doc tab or AI-use note on the page.

**Checked at ingest.** Two numbers on tab 7 differ from the [Evidence Atlas](../entities/arrm-evidence-atlas.md) built from the same package: the folder counts and the junction called worst (Q85, Q86).

**Feeds:** [modpods, for a SWMM person (app)](../entities/modpods-explainer-app.md), [modpods (Dantzer's method)](../entities/modpods.md), [Where a surrogate of SWMM breaks](../concepts/surrogates-hidden-state-missing-forcing.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md).

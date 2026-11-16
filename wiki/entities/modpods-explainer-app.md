---
title: modpods, for a SWMM person (app)
type: entity
updated: 2026-11-16
sources: [S155]
tags: [apps, modpods, surrogates, rdii, netlify]
reviewed: 11/16/2026
---
Bob's app that explains [modpods (Dantzer's method)](modpods.md) to a SWMM modeler as "RTK with the triangle replaced by a fitted gamma". It is on Netlify at modmods-explained.netlify.app (the site name spells it "modmods"), deployed 21 August 2026, with no version number on the page [S155](../sources/S155-modpods-explainer-summary.md).

**A caution about its source.** The page ships no technical summary. [S155](../sources/S155-modpods-explainer-summary.md) was written by Claude on 16 November 2026 from the live page, with nothing fitted or rerun, and Bob has not yet read it (Q84). The page names no author and carries no AI-use note, About tab or Doc tab.

**Seven tabs, one idea each** [S155](../sources/S155-modpods-explainer-summary.md)

| Tab | What it shows |
|---|---|
| The kernel | the gamma PDF as a unit hydrograph, read as a Nash cascade and as a moment-matched RTK triangle |
| Convolve | rainfall turned into two latent states, "two effective subcatchments" |
| Discover | dq/dt regressed on powers of the state and the inputs |
| Fit | the outer loop, a train and validation split, CSV import, a fitted [HYDROGRAPHS] export |
| Where it breaks | five signals a SWMM model can produce, fitted in turn |
| The repo | the repository's defaults, API and three differences from a blog post, at commit dda892dd |
| The evidence | results from the replication package |

**What it claims about SWMM5.** The kernel's T, K and volume gain map onto the RTK R, T and K of `rdii.c`, with one bookkeeping step: the sampled kernel does not sum to 1, so R has to be read from the coefficient times the kernel's sum [S155](../sources/S155-modpods-explainer-summary.md). See [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md). Its export writes T in hours once the user declares the timestep (5, 15, 60 or 360 minutes) [S155](../sources/S155-modpods-explainer-summary.md).

**Where it breaks.** The pump and tidal backwater fail; the nonlinear reservoir and the weir fit. The page's reading: "Where a fitted low-order model collapses is where the dynamic-wave machinery is actually earning its keep" [S155](../sources/S155-modpods-explainer-summary.md). The same split, measured, is on [Where a surrogate of SWMM breaks](../concepts/surrogates-hidden-state-missing-forcing.md).

**Checks it states.** The JavaScript port was checked against scipy: gamma pdf to 1e-12, convolution to 1e-10, derivative to 1e-12, against scipy 1.17.1 and numpy 2.4.4 on 15 August 2026 [S155](../sources/S155-modpods-explainer-summary.md). No human review is recorded.

**Where it disagrees with its sibling.** Its evidence tab and the [Evidence Atlas](arrm-evidence-atlas.md) read the same package and give different folder counts and a different worst junction (Q85, Q86).

---
title: RDII unit hydrographs (RTK)
type: concept
updated: 2026-11-18
sources: [S16, S55, S155, S157, S332]
tags: [hydrology, rdii, swmm5]
reviewed: 11/16/2026
changed_after_review: "2026-11-18 (S300 to S375 ingest): a paragraph added near the end, headed Added 18 November 2026 (S332)"
---
SWMM5 computes rainfall-dependent inflow and infiltration (RDII) from triangular unit hydrographs [S16](../sources/S16-li-rdii-in-swmm5.md).

**Structure**
- A unit hydrograph set has up to three hydrographs: short-term, intermediate-term and long-term response [S16](../sources/S16-li-rdii-in-swmm5.md).
- A group has up to 12 sets, one per month, and names the rain gage that feeds it [S16](../sources/S16-li-rdii-in-swmm5.md).
- A node receives RDII by naming a group and a sewershed area in its Inflows property. The sewershed area is typically a small part of the subcatchment area that sends surface runoff to the same node [S16](../sources/S16-li-rdii-in-swmm5.md).

**Parameters** [S16](../sources/S16-li-rdii-in-swmm5.md)

| Symbol | Meaning |
|---|---|
| R | Fraction of rainfall volume that enters the sewer |
| T | Time from the start of rainfall to the hydrograph peak, hours |
| K | Ratio of time to recession to time to peak |
| Dmax | Maximum depth of initial abstraction |
| Drec | Recovery rate of initial abstraction |
| Do | Initial abstraction already used at the start |

A blank parameter is taken as 0 [S16](../sources/S16-li-rdii-in-swmm5.md).

**Files.** An RDII interface file has the same text format as a routing interface file: the keyword `SWMM5`, a description, the time step in seconds, the variables (flow first), the node names, then one line per node per step. RDII files that SWMM writes itself are binary [S16](../sources/S16-li-rdii-in-swmm5.md).

**A use beyond RDII.** With calibrated unit hydrographs the RDII procedure can replace the subcatchment rainfall-runoff procedure, in which case "RDII" at a node is really overland runoff [S16](../sources/S16-li-rdii-in-swmm5.md).

**Who wrote it.** Bob coded the RTK/RDII implementation for SWMM 5 during the CRADA project with EPA [S55](../sources/S55-swmm-brain-readme.md). His later tools on it: an RTK Hydrograph Generator app, the RDII Analyst at Innovyze, and Ruby scripts for RTK parameter fitting in ICM [S55](../sources/S55-swmm-brain-readme.md).

**Not in the sources yet.** How InfoSWMM and ICM treat RDII (the article's title promises it, but those parts were images), and a description of the method from the code. Queued: "InfoSWMM, InfoSWMM SA RDII Analyst 3.0 with EPA SSOAP Tools" (2017, 4,019 words).

**Added 16 November 2026.** A fitted alternative to the triangle. [modpods (Dantzer's method)](../entities/modpods.md) convolves rainfall with gamma-PDF kernels whose shape, scale and delay it fits. Read by moment match, a kernel gives an RTK triangle with T = (α - 1)θ + d and K = 3·mean/T - 2. The sampled kernel does not sum to 1, so an RTK R has to be read from the fitted coefficient times the kernel's sum [S155](../sources/S155-modpods-explainer-summary.md). On a small SWMM5 model built from RTK unit hydrographs with IA = 0, modpods predicted held-out storms better than an LSTM: NSE 0.989 against 0.963 with every third storm held out, and 0.952 against 0.731 with the largest storm held out [S157](../sources/S157-lstm-swmm5-summary.md). Both sources are summaries Claude wrote from the app pages (Q84).

**Added 18 November 2026.** RDII Rosetta Stone maps InfoSWMM RDII to EPA SWMM5 and InfoWorks ICM; its storm-response arithmetic is a line-for-line port of EPA SWMM 5.2.4 rdii.c and matches the engine within float precision on 8 verification models [S332](../sources/S332-rdii-rosetta-stone-summary.md).

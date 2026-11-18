---
title: "S279: Finite difference vs ML for flood modeling, summary written from the page (v2026-10-09)"
type: source
raw: raw/apps/finite-difference-vs-ml-v2026-10-09.md
kind: app-md
author: Robert Dickinson
published: 2026-10-09
ingested: 2026-11-18
tags: [dashboards, surrogates, machine-learning, saint-venant, extrapolation]
drafted_by: Claude (Anthropic), from the published dashboard
reviewed: no
---
**What it is.** A technical summary of the dashboard Finite difference vs ML for flood modeling, version 2026-10-09: a dashboard of one synthetic experiment: a 1D Saint-Venant finite difference solver on an 8-mile reach and two scikit-learn surrogates (a neural network and a random forest) trained on 200 of its runs, scored against ten reasons, each with a test. Raw file: [raw/apps/finite-difference-vs-ml-v2026-10-09.md](../../raw/apps/finite-difference-vs-ml-v2026-10-09.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude dashboard https://claude.ai/artifact/MF4SmBcz852QKsLFwiQDUa, version 1791519555-865a: its page file (files/index.html, 52,851 bytes, SHA-256 fe3ece0053f490d3aa21c31c9ea7dc0fc4bc23e4b2317584fdd37c52e7680b7c) and its 15 data files (27,269 bytes of CSV), rendered in headless Chromium on 2026-11-18 through the Netlify conversion and read in full. Nothing was rerun to write this file." The page carries no AI-use note; each of its data files says "Synthetic experiment run by Claude on 2026-10-09". The Netlify copy is a conversion by Claude on 18 November 2026.

**Claims worth keeping** (all copied from the file)
- Inside the record (peaks 200 to 1,200 cfs, all in bank) the network matches the solver's peak depth at mile 4 to 0.007 ft RMSE and answers 4,200 times faster (1,700 ms against 0.40 ms per flood).
- At a 3,000 cfs design flood, ten trainings of the network give 5.90 to 9.75 ft against the solver's 8.40 ft; the forest gives 5.50 ft; the first network training loses 18% (251 ac-ft) of the 1,397 ac-ft inflow and the forest 56%.
- Solver continuity is at worst 4 x 10^-12 % over 265 runs; steady depth matches Manning normal depth within 2 x 10^-13 ft.
- A surrogate trained on a teacher solver with n off by 0.005 is 0.33 ft from the reference but 0.008 ft from its teacher.
- A grid test caught a centered convective term that ran clean on five grids and broke on the 66 ft grid (2,324 rising steps on the recession); the upwind term fixed it.

**Limits it states.** The reference is the solver itself; one synthetic reach, no rainfall, gauges or calibration; two small off-the-shelf surrogates with two inputs; rows 3, 4, 5 and 8 of the scorecard true by construction; a hydraulics test, not rainfall-runoff forecasting.

**Checked at ingest.** 3,000 / 1,200 = 2.5; 1,699.8 / 0.404 = 4,206 (given as 4,200); 251 / 1,397 = 18% (our arithmetic). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Finite difference vs ML for flood modeling (dashboard)](../entities/finite-difference-vs-ml.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md), [Where a surrogate of SWMM breaks: hidden state and missing forcing](../concepts/surrogates-hidden-state-missing-forcing.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md).

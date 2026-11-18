---
title: "Hard Meters, Soft Models (app)"
type: entity
updated: 2026-11-17
sources: [S205, S239]
tags: [apps, bme, flow-monitoring, calibration, sewers]
reviewed: no
---
Bob's app Hard Meters, Soft Models: a browser port of the network-domain Bayesian Maximum Entropy of Corinne Wiesner-Friedman's PyBME 0.5.0: flow meters are hard data, a hydraulic model run is soft data, and the graph Laplacian of the pipe network is the prior. Version 1.0, 2026-10-22 [S239](../sources/S239-hard-meters-soft-models-summary.md). Netlify address: https://hard-meters-soft-models.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S239](../sources/S239-hard-meters-soft-models-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S239](../sources/S239-hard-meters-soft-models-summary.md)
- The port matches PyBME in 116 parity checks: covariances to 1e-12, the README example to 1e-9, the 396-point space-time fields to 1e-11, with one tie-order exception explained.
- At the 328 unmetered node-hours of the example network, BME's RMSE is 0.0334 MGD, 16 % better than the model alone and 28 % better than PyBME's example as written; its 95 % band covers the truth at 99.4 % of points.
- With a model 25 % low on dry-weather flow while its soft PDFs still claim a sigma of about 0.07 MGD, BME gives 0.2111 against 0.2120 for the model alone, and its 95 % band covers the truth at only 61 % of points.
- Integration check: an independent dense-quadrature reference gives a mean of 1.3996; Gauss-Hermite gives 1.4018; Laplace returns the kriging Gaussian.
- Eleven findings in PyBME, each reproduced in Python against the unmodified repository.

**What it does not show.** The synthetic dataset is PyBME's; no real metered system was fused. BME is only as honest as the variances it is given. [S239](../sources/S239-hard-meters-soft-models-summary.md)

**Noted at ingest.** Issue drafts for PyBME sit in `raw/apps/PyBME-issue-drafts.md`, left queued because they are not an app summary (Q56); whether they are these eleven findings was not checked. PyBME is Corinne Wiesner-Friedman's, MIT.

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [Calibrating SWMM through a surrogate](../concepts/calibrating-through-a-surrogate.md).

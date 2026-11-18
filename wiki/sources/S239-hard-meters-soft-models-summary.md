---
title: "S239: Hard Meters, Soft Models, summary written from the page (v1.0)"
type: source
raw: raw/apps/hard-meters-soft-models-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-22
ingested: 2026-11-17
tags: [apps, bme, flow-monitoring, calibration, sewers]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Hard Meters, Soft Models, version 1.0: a browser port of the network-domain Bayesian Maximum Entropy of Corinne Wiesner-Friedman's PyBME 0.5.0: flow meters are hard data, a hydraulic model run is soft data, and the graph Laplacian of the pipe network is the prior. Raw file: [raw/apps/hard-meters-soft-models-v1.0.md](../../raw/apps/hard-meters-soft-models-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792638461-e46f, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in a session on 21 to 22 October 2026 under Bob's direction; Bob supplied the PyBME repository and asked for an app. Claude installed PyBME and ran its tests, wrote the Python reference scripts, ported the engine to JavaScript, and found and reproduced eleven findings in PyBME.

**Claims worth keeping** (all copied from the file)
- The port matches PyBME in 116 parity checks: covariances to 1e-12, the README example to 1e-9, the 396-point space-time fields to 1e-11, with one tie-order exception explained.
- At the 328 unmetered node-hours of the example network, BME's RMSE is 0.0334 MGD, 16 % better than the model alone and 28 % better than PyBME's example as written; its 95 % band covers the truth at 99.4 % of points.
- With a model 25 % low on dry-weather flow while its soft PDFs still claim a sigma of about 0.07 MGD, BME gives 0.2111 against 0.2120 for the model alone, and its 95 % band covers the truth at only 61 % of points.
- Integration check: an independent dense-quadrature reference gives a mean of 1.3996; Gauss-Hermite gives 1.4018; Laplace returns the kriging Gaussian.
- Eleven findings in PyBME, each reproduced in Python against the unmodified repository.

**Limits it states.** The synthetic dataset is PyBME's; no real metered system was fused. BME is only as honest as the variances it is given.

**Checked at ingest.** Issue drafts for PyBME sit in `raw/apps/PyBME-issue-drafts.md`, left queued because they are not an app summary (Q56); whether they are these eleven findings was not checked. PyBME is Corinne Wiesner-Friedman's, MIT. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://hard-meters-soft-models.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Hard Meters, Soft Models (app)](../entities/hard-meters-soft-models.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [Calibrating SWMM through a surrogate](../concepts/calibrating-through-a-surrogate.md).

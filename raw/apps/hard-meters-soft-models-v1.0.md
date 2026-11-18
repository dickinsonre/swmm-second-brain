---
name: Hard Meters, Soft Models
file: hard-meters-soft-models.html
version: "1.0"
date: 2026-10-22
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/QGqj5iaH8GCuzNEdorjhqY", repo: none named in the page}
engines:
  - {name: network BME, source: "JavaScript port of PyBME 0.5.0 (Corinne Wiesner-Friedman): network.py, soft_data.py, integration.py, predict.py, synthetic_network.py, swmm.py", license: MIT}
units: US customary (MGD, ft, ft/s, in/hr)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/QGqj5iaH8GCuzNEdorjhqY, version 1792638461-e46f (index.html, 421,406 bytes, SHA-256 f819042af6dd53f39e62d2c91588d484f63e13b3c1bc1546e97bc2883f894e8a), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Hard Meters, Soft Models: PyBME's network Bayesian Maximum Entropy in the browser, on sewer data

## In three points
- **What:** Ports the network-domain Bayesian Maximum Entropy of Corinne Wiesner-Friedman's PyBME to the browser: flow meters are hard data, a hydraulic model run is soft data, and the graph Laplacian of the pipe network is the prior.
- **So what:** The port matches PyBME in 116 parity checks, and on the example network BME cuts unmetered error to 0.0334 MGD, 16% better than the model alone, with its 95% band covering the truth at 99.4% of unmetered points.
- **Now what:** Use it to blend a few meters with a model across the unmetered nodes. BME is only as honest as the variances it is given: with a model 25% low, its 95% band covered the truth at only 61% of points.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-22"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

You have a sewer model that covers every node and is wrong by an unknown amount, and four meters that are right but say nothing about the other seven nodes. BME (Christakos 1990; BMElib by Serre, Bogaert and Christakos) blends them as a calculation rather than a calibration decision. Tabs: Fuse, Anatomy, Prior, Your .inp, Findings, Verify, Repo, About, Doc.

## Results the page reports

- At the 328 unmetered node-hours, BME's RMSE is 0.0334 MGD, 16% better than the model alone and 28% better than PyBME's example as written; 95% band coverage 99.4%. At TRUNK's unmetered hours the error goes from 0.068 to 0.041.
- With a model 25% low on dry-weather flow and soft PDFs still claiming sigma about 0.07 MGD, BME gives 0.2111 against 0.2120 for the model alone, and its 95% band covers truth at 61% of points.
- Integration check: one meter (1.0) two pipes away and one interval soft datum ("between 1 and 3") one pipe away; an independent dense-quadrature reference gives a mean of 1.3996; Gauss-Hermite gives 1.4018; Laplace returns the kriging Gaussian.
- Eleven findings in PyBME, each reproduced in Python against the unmodified repository.

## Checks (as stated on the page)

- 116 parity checks against PyBME's own output, rerun live on the Verify tab: covariances to 1e-12, the README example to 1e-9, the 396-point space-time fields to 1e-11, with one tie-order exception explained.
- Accuracy claims are measured against references that do not use PyBME's integrators (dense quadrature and Monte Carlo).

## What this does not show

- The synthetic dataset is PyBME's; no real metered system was fused.
- BME depends on the variances given to the soft data.

## How to reproduce

Open the page; Verify reruns the parity checks; Your .inp loads a SWMM model as soft data.

## Credits and licenses

PyBME 0.5.0, copyright Corinne Wiesner-Friedman, MIT; the engine's algorithms are ports of her code and the synthetic dataset is hers. BMElib 2.0 (MATLAB): Marc L. Serre, Patrick Bogaert and George Christakos, UNC Chapel Hill. Graph Matern priors: Borovitskiy et al. (2021); diffusion kernels: Kondor and Lafferty (2002).

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude session on 21 to 22 October 2026, under the direction of Robert (Bob) Dickinson, who supplied the PyBME repository and asked for an app. Claude installed PyBME and ran its tests and examples, wrote the Python scripts behind every reference number, ported the network-BME engine to JavaScript, built every tab, found and reproduced the eleven findings, chose the suggested fixes, and wrote the text. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-10-22): first version.

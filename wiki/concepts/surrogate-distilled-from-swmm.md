---
title: A surrogate distilled from SWMM
type: concept
updated: 2026-11-18
sources: [S56, S155, S156, S157, S261, S279]
tags: [surrogates, machine-learning, ideas]
reviewed: 11/16/2026
changed_after_review: "2026-11-17 (S256 to S267 ingest): a paragraph added near the end, headed Added 17 November 2026 (S261); 2026-11-18 (S268 to S299 ingest): a paragraph added near the end, headed Added 18 November 2026 (S279)"
---
An idea of Bob's, dated 29 June 2026, status seed: train a fast emulator on SWMM's own output, not on field gauges [S56](../sources/S56-swmm-brain-note-surrogate.md).

**The claim.** Field monitoring is sparse. A calibrated SWMM model can produce unlimited labeled pairs of rain against flow and rain against depth. So run a Monte Carlo library of thousands of synthetic storms through the model and distill the behavior into a surrogate. The framing becomes "CNN distilled from SWMM", not "CNN instead of SWMM" [S56](../sources/S56-swmm-brain-note-surrogate.md).

**What it would be for** [S56](../sources/S56-swmm-brain-note-surrogate.md)
- an emulator light enough to run in a browser
- rapid what-if testing
- faster calibration loops

**The plan in the note** [S56](../sources/S56-swmm-brain-note-surrogate.md)
1. Start with a small benchmark SWMM network.
2. Vary storm patterns, antecedent conditions and selected calibrated parameters.
3. Export response hydrographs as supervised training data.
4. Validate the surrogate on peak, timing, shape, surcharge behavior and depth envelopes.
5. Only then try larger networks.

**Status.** Seed. The note points to an `experiments/synthetic-storm-surrogate/` folder that is not in the repository, and reports no result [S56](../sources/S56-swmm-brain-note-surrogate.md).

**Not in the sources yet.** Any run of the idea, and any of Bob's later surrogate work.

Kept from [swmm-brain (the old brain repository)](../entities/swmm-brain-repo.md).

**Added 16 November 2026.** Bob's later surrogate work is now in the sources, in three apps whose summaries Claude wrote from the app pages (Q84). [modpods, for a SWMM person](../entities/modpods-explainer-app.md) and the [Evidence Atlas](../entities/arrm-evidence-atlas.md) study a published method whose fitted models reach a median evaluation NSE of 0.7406 on 181 junctions of a SWMM model and 0.1358 on 365 real catchments [S155](../sources/S155-modpods-explainer-summary.md) [S156](../sources/S156-arrm-evidence-atlas-summary.md). [LSTM + SWMM5](../entities/lstm-swmm5-app.md) trains an LSTM and that method on SWMM5's own output, then calibrates SWMM through the LSTM [S157](../sources/S157-lstm-swmm5-summary.md). What they found is on [Where a surrogate of SWMM breaks](surrogates-hidden-state-missing-forcing.md) and [Calibrating SWMM through a surrogate](calibrating-through-a-surrogate.md).

**Added 17 November 2026, fourth batch.** [SWMM6 Hands-On Watershed (app)](../entities/swmm6-hands-on-watershed.md) trains a two-layer network on 3,300 OpenSWMM 6 runs of one synthetic catchment with snow: held-out peak R2 0.952, median peak error 9.4 % above 5 cfs, and 3.4 % before snow was added [S261](../sources/S261-swmm6-hands-on-watershed-summary.md).

**Added 18 November 2026.** A synthetic experiment on an 8-mile reach puts numbers on the boundary of a surrogate's record: inside 200 in-bank floods a neural network matches the Saint-Venant solver's peak depth to 0.007 ft RMSE and answers 4,200 times faster; at a design flood 2.5 times the largest on record, ten trainings give 5.90 to 9.75 ft against the solver's 8.40 ft, and a surrogate scored against its own teacher looks fine even when the teacher is 0.33 ft wrong [S279](../sources/S279-finite-difference-vs-ml-summary.md).

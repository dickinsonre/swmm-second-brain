---
title: A surrogate distilled from SWMM
type: concept
updated: 2026-11-16
sources: [S56, S155, S156, S157]
tags: [surrogates, machine-learning, ideas]
reviewed: 2026-11-15
changed_after_review: "2026-11-16 (modpods ingest): one paragraph added at the end, headed Added 16 November 2026, on the three surrogate apps (S155, S156, S157)"
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

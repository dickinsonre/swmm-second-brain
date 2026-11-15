---
title: A surrogate distilled from SWMM
type: concept
updated: 2026-11-14
sources: [S56]
tags: [surrogates, machine-learning, ideas]
reviewed: 2026-11-15
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

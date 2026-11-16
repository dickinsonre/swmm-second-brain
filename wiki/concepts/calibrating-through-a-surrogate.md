---
title: Calibrating SWMM through a surrogate
type: concept
updated: 2026-11-16
sources: [S157]
tags: [calibration, surrogates, lstm, swmm5]
reviewed: 11/16/2026
---
Search the parameters through a fast learned model, then confirm the answer in SWMM. The [LSTM + SWMM5 (app)](../entities/lstm-swmm5-app.md) tried it on a small demo and recorded what went wrong. Its source is a summary Claude wrote from the page, not yet read by Bob (Q84).

**The pipeline** [S157](../sources/S157-lstm-swmm5-summary.md)
1. SWMM runs the base .inp.
2. SWMM runs a Latin-hypercube sample of parameter multipliers.
3. An LSTM learns rain plus multipliers to flow.
4. An optimizer searches the multipliers through the LSTM; SWMM confirms every answer before it is reported.
5. Optionally, the search finishes in SWMM ("polish"), or runs in SWMM from scratch for comparison ("direct").

**The demo.** Four subcatchments (70 ac, Horton), three conduits to one outfall, 42 days of rain. The "observation" is SWMM itself with hidden multipliers: width × 0.60, % impervious × 1.15, pervious n × 1.50, infiltration × 0.70, conduit n × 1.10 [S157](../sources/S157-lstm-swmm5-summary.md).

**Results of the stored build run** (NSE on the calibration window, verification in parentheses) [S157](../sources/S157-lstm-swmm5-summary.md)

| Route | NSE | SWMM runs |
|---|---|---|
| Base model | 0.965 (0.935) | |
| LSTM, confirmed in SWMM | 0.996 (0.976) | 62 |
| Response surface, confirmed in SWMM | 0.99913 (0.997) | |
| Polished in SWMM | 0.99999 (0.99990) | + 135 |
| Direct search in SWMM | 0.99999 (0.99995) | 477 |

**What the page found** [S157](../sources/S157-lstm-swmm5-summary.md)
- **A good fit is not the right parameters.** At the LSTM optimum, conduit n is × 0.70 against a true × 1.10.
- **A surrogate can send the search into the wrong basin.** Polishing in SWMM from the LSTM's answer stalls at NSE 0.99646 after 164 runs, in a second basin. Refining around the optimum with a few more SWMM runs escapes it: 0.99637 to 0.99974 in 18 runs.
- **A response surface beat the LSTM** at predicting SWMM on 12 unseen parameter sets: median NSE 0.996 for a quadratic surface and 0.986 for a linear one, against 0.981.
- **The LSTM's advantage is new rain.** On days 43 to 84 of the rain record, never seen in training, it matches SWMM at median NSE 0.969 (worst 0.938).
- **A second gauge helps a little.** Calibrating to two series cut the RMS error of the log multipliers to 0.033, against 0.072 with the outfall alone and 0.038 for the direct search.
- **Seeds matter.** Three repeats confirm at NSE 0.9932, 0.9952 and 0.9937.
- **Ranges found through a surrogate describe the surrogate.** The near-optimal ranges found through the LSTM exclude the truth.
- **Little time saved on a fast model.** 197 SWMM runs against 477, but 58 s against 58 s, because the demo runs in 0.11 s.

**What it does not show.** No observed flow: the truth is EPA SWMM 5.2.4 output, so the model's structure is right by construction. Uncertainty bounds come through the LSTM, not from a likelihood [S157](../sources/S157-lstm-swmm5-summary.md).

**Related.** [Calibration, validation and uncertainty](calibration-validation-uncertainty.md); [Where a surrogate of SWMM breaks](surrogates-hidden-state-missing-forcing.md).

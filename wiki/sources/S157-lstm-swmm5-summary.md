---
title: "S157: LSTM + SWMM5, summary written from the page (v2.0)"
type: source
raw: raw/apps/swmm5-lstm-calibration-v2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-18
ingested: 2026-11-16
tags: [apps, swmm5, lstm, modpods, surrogates, calibration, wasm, machine-learning, netlify]
reviewed: 11/16/2026
---
**What it is.** A technical summary of the app "LSTM + SWMM5", version 2.0 (18 October 2026), the page served at lstm-swmm5-amin-talei.netlify.app. EPA SWMM 5.2.4 runs in the page as WebAssembly. The app asks two things: can an LSTM read a SWMM model's rainfall and runoff, and can an LSTM calibrate one. Raw file: [raw/apps/swmm5-lstm-calibration-v2.0.md](../../raw/apps/swmm5-lstm-calibration-v2.0.md).

**How it was written. This one is different.** The page ships no summary file. Claude (Anthropic) wrote this one on 16 November 2026, at Bob's request, from the live page, read tab by tab in a browser. Every number is from the page's stored build run, its tables and its Evidence tab; nothing was trained or calibrated. Bob has not read it (Q84). The page's own Use of AI section says the app was built with Claude in Claude Code sessions from 14 to 18 October 2026 under Bob's direction, and that version 2.0 answers a review of version 1.2 written by another AI model.

**Claims worth keeping** (all copied from the page)
- Head to head on 120 days of SWMM5 output at 15-minute steps (31 storms, 19.7 in), held-out NSE, LSTM median of 5 seeds against modpods. Every 3rd storm: Horton P1 0.960 / 0.718; RTK P2 0.963 / 0.989; pond P3 0.967 / -430.014; pump flow P4 0.355 / 0.147; wet-well depth -0.050 / -4.457; tidal with rain only -0.049 / diverged; tidal with the tide stage given 0.997 / diverged.
- Holding out the largest storm flips P1: LSTM 0.301, modpods 0.670. On P2, 0.731 against 0.952.
- The P1c control (Horton dry time cut from 7 days to 6 hours): modpods still 0.595 against the LSTM's 0.938, so P1's gap is behavior inside each storm, not antecedent memory.
- A forget gate held at f is a linear reservoir with τ = -Δt / ln f; f = 0.953 gives τ = 5.2 h.
- Calibration build run: LSTM to SWMM NSE 0.996 (verification 0.976) from a base of 0.965; polished 0.99999; direct SWMM search 0.99999 in 477 runs. A quadratic response surface predicts SWMM better than the LSTM on unseen parameter sets (0.996 against 0.981).
- C-1: the LSTM gets a fit, not the parameters: conduit n × 0.70 against a true × 1.10. C-9: near-optimal ranges found through the LSTM exclude the truth.
- F-8: WebAssembly against native on the calibration demo: 56 of 4,032 periods differ, at most 0.102 cfs (0.41 % of peak), NSE 0.999996; the native build disagrees with itself by 4 periods when glibc's FMA paths are off. The six probe models are byte-identical.
- F-9: SWMM 5.2.4 applies a monthly rainfall adjustment one value late (`gage.c`). F-1: an .out holds, at each report time, the rain of the interval that starts there.
- F-3 to F-6: `bibo_stable` does not guarantee stability; a fitted cubic can rest at a false flow (P3: 22.40 cfs, volume error 7715 %); near that point RK4 and the implicit solver give opposite verdicts (NSE 0.469 against -34.509); the kernels are not normalised (sum 1.582 at the first seed).
- Checks: the .out reader against EPA's `swmm_output`, 2,603,294 values, 0 mismatches; LSTM gradients against finite differences, worst relative error 2.38e-7; modpods against scipy LSODA.

**Limits it states.** No observed flow; one synthetic rain record and six small models; one LSTM recipe; a modpods optimizer that replaces the repository's Gaussian-process step with a pattern search; "No person has yet reviewed every number on the page."

**Checked at ingest.** The page does not name Amin Talei, whose name the Netlify site carries. Its modpods port follows commit dda892d, the same commit as [S155](S155-modpods-explainer-summary.md); it says the repository head had moved 101 commits by 14 October 2026.

**Feeds:** [LSTM + SWMM5 (app)](../entities/lstm-swmm5-app.md), [Where a surrogate of SWMM breaks](../concepts/surrogates-hidden-state-missing-forcing.md), [Calibrating SWMM through a surrogate](../concepts/calibrating-through-a-surrogate.md), [modpods (Dantzer's method)](../entities/modpods.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md).

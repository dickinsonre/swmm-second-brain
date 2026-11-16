---
title: LSTM + SWMM5 (app)
type: entity
updated: 2026-11-16
sources: [S157]
tags: [apps, swmm5, lstm, modpods, surrogates, calibration, wasm, netlify]
reviewed: 11/16/2026
---
Bob's app that runs EPA SWMM 5.2.4 in the page as WebAssembly and asks two questions: can an LSTM read the rainfall and runoff of a SWMM model, and can it then calibrate one. Version 2.0, 18 October 2026, on Netlify at lstm-swmm5-amin-talei.netlify.app; the page saves itself as `swmm5-lstm-calibration.html` [S157](../sources/S157-lstm-swmm5-summary.md).

**A caution about its source.** The page ships no summary file. [S157](../sources/S157-lstm-swmm5-summary.md) was written by Claude on 16 November 2026 from the live page's stored results, with nothing trained or calibrated, and Bob has not yet read it (Q84). The page says it was built with Claude from 14 to 18 October 2026 under Bob's direction, and that "No person has yet reviewed every number on the page."

**Six tabs** [S157](../sources/S157-lstm-swmm5-summary.md): Calibrate, Verdict, Head-to-head, Inside the models, Your model, Evidence.

**The two surrogates.** An LSTM of one layer and 16 cells, trained by backpropagation through time in 192-hour windows, written with + - × ÷ only so a rerun matches to the last bit. A JavaScript port of [modpods](modpods.md) at commit dda892d, with the repository's Bayesian optimizer replaced by a pattern search [S157](../sources/S157-lstm-swmm5-summary.md).

**The verdict, in short** [S157](../sources/S157-lstm-swmm5-summary.md). On six small SWMM5 models over a 120-day seeded record:
- RTK unit hydrographs (linear): modpods wins every hold-out.
- Horton runoff and a pond: the LSTM wins interpolation (0.960 against 0.718; 0.967 against -430.014).
- The largest storm held out: the LSTM drops to 0.301 on Horton while modpods keeps 0.670.
- Tidal backwater with rain only: both fail; given the tide stage, the LSTM reaches 0.997 and modpods still diverges.

The full table and what it means are on [Where a surrogate of SWMM breaks](../concepts/surrogates-hidden-state-missing-forcing.md).

**The forget gate as a recession constant.** A cell whose forget gate holds at f decays like a linear reservoir with τ = -Δt / ln f; the default bias gives f = 0.953 and τ = 5.2 h at 15-minute steps [S157](../sources/S157-lstm-swmm5-summary.md).

**Calibration.** On a demo with five hidden parameter multipliers, the LSTM route reached SWMM-confirmed NSE 0.996 but with conduit n × 0.70 against a true × 1.10; a quadratic response surface did better. See [Calibrating SWMM through a surrogate](../concepts/calibrating-through-a-surrogate.md).

**Engine findings it records** [S157](../sources/S157-lstm-swmm5-summary.md)
- F-1: a SWMM5 .out holds, at each report time, the rain of the interval that starts there. See [Reading SWMM output](../concepts/reading-swmm-output.md).
- F-8: WebAssembly against native, 56 of 4,032 periods differ on the calibration demo. See [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
- F-9: SWMM 5.2.4 applies a monthly rainfall adjustment one value late (Q87).

**Checks it states.** The .out reader against EPA's `swmm_output`: 2,603,294 values, 0 mismatches. Six probe models byte-identical between WebAssembly and native. Version 2.0 fixed nine faults from an AI review of version 1.2, each reproduced first, and shows each faulty line as it was [S157](../sources/S157-lstm-swmm5-summary.md).

**Not on the page.** Amin Talei, whose name is in the Netlify site name, is not credited on the page; there is no About tab, Doc tab or technical summary file [S157](../sources/S157-lstm-swmm5-summary.md).

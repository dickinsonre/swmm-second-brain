---
title: "SRTC Radio for ICM (app)"
type: entity
updated: 2026-11-17
sources: [S205, S249]
tags: [apps, icm, ruby, calibration, sensitivity]
reviewed: no
---
Bob's app SRTC Radio for ICM: the slider layer for srtc_icm.rb, a Ruby script for InfoWorks ICM (hw_ and sw_ networks): load the response surface the script harvests from one base and two extreme runs per parameter layer, tune multipliers with sliders against an observed hydrograph without re-simulating, and export srtc_tuned.json for the script's apply phase. ICM runs outside the page. Version 1.0.0, 2026-09-30 [S249](../sources/S249-srtc-radio-icm-summary.md). Netlify address: https://srtc-radio-icm.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S249](../sources/S249-srtc-radio-icm-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S249](../sources/S249-srtc-radio-icm-summary.md)
- The tuned hydrograph is a linear superposition, Q(t) = Q_base(t) + the sum of s_i times each layer's change; the multipliers written by apply are m_i = 1 + s_i u_i.
- Objectives: NSE, RMSE, MAE, R2, peak error, volume error, or a composite.
- The Verify tab measures the gap between the linear prediction and the real tuned ICM run, which decides whether one pass was enough.
- Configure the Ruby fills in the gauge, the layers and the ICMExchange connection and downloads srtc_icm.rb with the prepare, harvest, apply and verify command lines; run_params keys follow the ICM Exchange new_run documentation.

**What it does not show.** The response surface is linear in the sliders: interactions between layers, thresholds (surcharge, overflow onset, pump switching) and parameters that change the response's shape are invisible until Verify. Field names are checked against the live network only when the script runs. [S249](../sources/S249-srtc-radio-icm-summary.md)

**Noted at ingest.** The summary reports no calibration run, in ICM or otherwise.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoWorks ICM](infoworks-icm.md).

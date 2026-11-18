---
title: "S249: SRTC Radio for ICM, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/srtc-radio-icm-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-09-30
ingested: 2026-11-17
tags: [apps, icm, ruby, calibration, sensitivity]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SRTC Radio for ICM, version 1.0.0: the slider layer for srtc_icm.rb, a Ruby script for InfoWorks ICM (hw_ and sw_ networks): load the response surface the script harvests from one base and two extreme runs per parameter layer, tune multipliers with sliders against an observed hydrograph without re-simulating, and export srtc_tuned.json for the script's apply phase. ICM runs outside the page. Raw file: [raw/apps/srtc-radio-icm-v1.0.0.md](../../raw/apps/srtc-radio-icm-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1790737695-5f81, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The published page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session. The summary says the Netlify copy adds a one-line AI-use note.

**Claims worth keeping** (all copied from the file)
- The tuned hydrograph is a linear superposition, Q(t) = Q_base(t) + the sum of s_i times each layer's change; the multipliers written by apply are m_i = 1 + s_i u_i.
- Objectives: NSE, RMSE, MAE, R2, peak error, volume error, or a composite.
- The Verify tab measures the gap between the linear prediction and the real tuned ICM run, which decides whether one pass was enough.
- Configure the Ruby fills in the gauge, the layers and the ICMExchange connection and downloads srtc_icm.rb with the prepare, harvest, apply and verify command lines; run_params keys follow the ICM Exchange new_run documentation.

**Limits it states.** The response surface is linear in the sliders: interactions between layers, thresholds (surcharge, overflow onset, pump switching) and parameters that change the response's shape are invisible until Verify. Field names are checked against the live network only when the script runs.

**Checked at ingest.** The summary reports no calibration run, in ICM or otherwise. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://srtc-radio-icm.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SRTC Radio for ICM (app)](../entities/srtc-radio-icm.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoWorks ICM](../entities/infoworks-icm.md).

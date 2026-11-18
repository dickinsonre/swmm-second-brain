---
name: SRTC Radio for ICM
file: srtc-radio-icm.html
version: "1.0.0"
date: 2026-09-30
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/VQ7xKvDcs2tw5ukofpgzqT", repo: none named in the page}
engines:
  - {name: InfoWorks ICM, note: "runs outside the page through srtc_icm.rb (UI or ICMExchange); the page tunes on the harvested response surface"}
units: the model's own
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/VQ7xKvDcs2tw5ukofpgzqT, version 1790737695-5f81 (index.html, 169,814 bytes, SHA-256 a722e916f0537e4f217a388567a2616824078242a814e88584d1c07ad6201b4d), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# SRTC Radio for ICM: sensitivity-based radio tuning calibration, the slider layer for srtc_icm.rb

## In three points
- **What:** The slider layer for srtc_icm.rb, a Ruby script for InfoWorks ICM (hw_ and sw_ networks): load the response surface the script harvests from one base and two extreme runs per parameter layer, tune multipliers with sliders against an observed hydrograph without re-simulating, and export srtc_tuned.json for the apply phase.
- **So what:** The tuned hydrograph is a linear superposition, Q(t) = Q_base(t) + sum of s_i times each layer's change, and the Verify tab measures the gap between that prediction and the real tuned ICM run, which decides whether one pass was enough.
- **Now what:** Use it for a fast first calibration, then rerun around the tuned scenario if Verify departs. Interactions, thresholds (surcharge, overflow onset, pump switching) and shape-changing parameters are invisible until Verify.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0.0 · 2026-09-30"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Radio, Sensitivity, Verify, Configure the Ruby, Method. Objectives: NSE, RMSE, MAE, R2, peak error, volume error, or a composite. Multipliers written by apply are m_i = 1 + s_i u_i. Configure the Ruby fills in the gauge, the layers and the ICMExchange connection and downloads srtc_icm.rb with that CONFIG and the command lines (prepare, harvest, apply, verify); run_params keys follow the ICM Exchange new_run documentation.

## What this does not show

- The response surface is linear in the sliders: interactions between layers, threshold behaviour and parameters that change the response's shape are invisible until Verify; treat the multipliers as a proposal.
- Field names are checked against the live network only when the script runs.

## How to reproduce

Load srtc_response.json (or the sample) on Radio, tune, export srtc_tuned.json, run apply and verify in ICM, and load srtc_verify.csv on Verify.

## Credits and licenses

InfoWorks ICM and its Exchange API (Autodesk). No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0.0 (2026-09-30): first version.

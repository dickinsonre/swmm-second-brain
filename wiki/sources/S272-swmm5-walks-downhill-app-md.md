---
title: "S272: SWMM5 Walks Downhill, app .md (v1.1.0)"
type: source
raw: raw/apps/swmm5-walks-downhill-v1.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-18
tags: [apps, calibration, gradient-descent, swmm5, wasm, extran]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app SWMM5 Walks Downhill, version 1.1.0: gradient descent on two SWMM5 knobs with EPA SWMM 5.2.4 in the loop, five engine runs per step, on a built-in six-subcatchment model and nine OWA EXTRAN models. Raw file: [raw/apps/swmm5-walks-downhill-v1.1.0.md](../../raw/apps/swmm5-walks-downhill-v1.1.0.md).

**How it was written.** The app ships this file. The file says the page was built with Claude (Claude Fable 5.2) on 15 November 2026 at Bob's request, from a Matheorems post on gradient descent, and that Bob had not reviewed the code, the knobs or the essay.

**Claims worth keeping** (all copied from the file)
- Cost J = (1 - NSE)/2 on 47 flow readings; slope from central differences in scaled knobs (h = 0.01); two walkers with step sizes 0.50 and 0.25, 40 steps, from 75%, 520 ft.
- Built-in model: both walks end near the knobs that made the data (red 45.24%, 220.5 ft; teal 45.14%, 223.5 ft; truth 45%, 220 ft).
- OWA EXTRAN models (inflow factor and roughness factor as knobs): the longer-step walker ends within 5% of the cost at the published values on 8 of 9, the shorter-step walker on 3 of 9; on extran10 both end pinned at the top of the roughness range with NSE 0.966.
- A step size 1.5 times the stability limit (0.958 against 0.639) fails to settle; a log scale for width rescues a start on the high-width shelf.
- 21 of 21 Node checks and 29 of 29 browser checks pass.

**Limits it states.** Synthetic observed flow; two knobs applied uniformly; one storm; one start, seed and pair of step sizes per OWA model; plain fixed-step descent; EPA SWMM 5.2.4 only; Chromium only; no person has reviewed it.

**Checked at ingest.** The checks table's numbers agree with its In three points block (45.24%, 220.5 ft; 8 of 9; 3 of 9; NSE 0.966). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM5 Walks Downhill (app)](../entities/swmm5-walks-downhill.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

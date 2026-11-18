---
name: SWMM6 Hands-On Watershed
file: swmm6-hands-on-watershed.html
version: 1.1.0
date: 2026-11-08
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/5sBAfgdZheSv2Puc3r4Ho3", repo: none named in the page}
engines:
  - {name: OpenSWMM Engine (HydroCouple), version: "6.0.0-alpha.4 (as its reports read)", branch: swmm6_rel, commit: 137e65e4e25e9425a489b99d5b7365c8355f8f6b, commit_date: 2026-09-10, build: "Emscripten 3.1.51, factory createOswmm6Module, from dickinsonre/BatchSWMMRunner at b793404", wasm_sha256: a857f2de88933edb7beb89704fa252e2bd13bf2fc8f35211ce29f161e3bbf463, license: Apache-2.0}
  - {name: EPA SWMM, version: 5.2.4, role: "comparison for snow only, not in the page", license: public domain}
units: US customary (in, ac, cfs, ft, degrees F)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/5sBAfgdZheSv2Puc3r4Ho3, version 1794321174-e662 (index.html, 4,482,308 bytes, SHA-256 d0b2e7ace7e8b6c017c7c6d4ef2a23c5340cece3e2b802d751b581d26e0fb0f2), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# SWMM6 Hands-On Watershed: drive the OpenSWMM 6 engine with your hands and read its water balance

## In three points
- **What:** One page that carries the OpenSWMM 6 engine compiled to WebAssembly, a 179.06 ac synthetic catchment with snow and groundwater, eight knobs you move by hand gestures, and a neural-network emulator that answers while you move.
- **So what:** Every term of P - ET - Q - Flood - DeepPerc = Delta S is read from the engine's own continuity tables, and the balance closed within 0.049 in on all 3,500 test runs; the emulator's held-out peak R2 is 0.952 with a median error of 9.4%.
- **Now what:** Download the page or open it on Netlify to use the camera (sandboxed previews block it). The catchment is synthetic, the September engine build has a dry-conduit evaporation defect fixed upstream, and live hand tracking was never tested.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.1.0 (8 November 2026)"). Every number below is copied from the page's About tab or its Doc essay. No model was run to write this file.

## What it does

The page carries the OpenSWMM 6 engine and a small synthetic catchment for it to run. You change eight things about the storm, the cold and the ground (temperature and snowpack among them) with hand gestures through the webcam, or with the mouse. A neural-network emulator answers while the hand moves; when the hand stops, the engine runs the scenario in about a tenth of a second. The catchment's layers (sky, snow and surface, soil, groundwater, channel) pull apart in 3D. The idea follows Alireza Razeghi Haghighi's LinkedIn post about Riverlight (November 2026); Riverlight's code was not published, so none of it is used. Tabs: Explore, Balance, Emulator, About, Doc.

## The model (as the page states it)

- 179.06 ac in six rectangular hillslope subcatchments at 3% slope, no overlaps, draining to junctions J1 to J3; three trapezoidal channels (8 ft bottom, 2:1 sides, 6 ft deep) to a free outfall.
- Green-Ampt infiltration (suction 4.0 in, Ksat 0.25 in/hr); one aquifer (porosity 0.45, field capacity 0.28, wilting point 0.12).
- Snowpack on every subcatchment: melt coefficients 0.0015 to 0.003 in/hr/F impervious, 0.0012 to 0.0025 pervious, base 32 F, snow below 34 F; air temperature the chosen mean plus or minus 8 F daily.
- Dynamic wave at a 20 s step, reported every 5 minutes for 72 hours from 10 March 2026; a triangular storm peaking at 40% of its duration, starting at hour 6.

## Results the page reports

- Default storm, 2.50 in in six hours: 1.442 in infiltrated, 1.018 in ran off; 1.018 in left at the outfall within 72 hours, 0.104 in returned to the air, 1.380 in stayed in soil and groundwater. Balance from the tables: 2.500 - 0.104 - 1.018 - 0.000 - 0.000 = 1.379 in against Delta S 1.380 in. Continuity errors -0.028%, 0.000% and -0.047%.
- Emulator: two hidden layers of 32 units, trained on 3,300 SWMM6 runs (Latin hypercubes), scored on 200 held-out runs. Peak R2 0.952; for peaks above 5 cfs, median error 9.4%, 90th percentile 37.4%; time to peak usually within 32 minutes, worst miss 19.8 hours; volume R2 0.992; about 10 microseconds per answer. Without snow (v1.0) the median peak error was 3.4%.

## Checks (as stated on the page)

- Engine identity: every report header read OpenSWMM 6.0.0-alpha.4, and the wasm matched the SHA-256 in its build manifest (checked again in the browser).
- Engine swap from v1.0's alpha.2 build: on 125 test models with peaks above 5 cfs, peaks match within a median 0.04% (largest 0.75%).
- Snow against EPA SWMM 5.2.4: six scenarios agree within 0.3% except near freezing; rain on a 2 in pack at 38 F gives a peak 4.5% off, and at 34 F outflow volume is 9.4% off.
- 3,500 scenarios: 0 ERROR lines; worst runoff continuity error 0.50%; basin balance closed within 0.049 in on every run.
- Binary reader: .out peaks in C1, C2, C3 of 17.46, 34.90, 52.35 cfs against the report's 17.46, 34.91, 52.35 cfs; groundwater storage from the .out agrees with the report to 0.003 in.
- Gestures: 30 of 30 synthetic poses classified correctly; a scripted sequence fired every controller action in order.
- All checks are mechanical.

## What this does not show

- No real place: terrain and catchment are synthetic and uncalibrated.
- Snow from a September build: OpenSWMM reworked snowmelt after 10 September 2026.
- Known defect in this build: a conduit that goes dry keeps its last evaporation rate (DynamicWave.cpp at 137e65e, recomputeConduitLossOne returns early for DRY conduits). On a storm that fell entirely as snow the report shows 0.022 ac-ft evaporated and a routing continuity error of -34,178%; EPA SWMM 5.2.4 reports zero. Fixed upstream on 12 September 2026 (commit b051d270).
- Percent continuity errors are large at the smallest storms because they divide by almost nothing.
- The emulator knows one catchment and fixed knob ranges.
- Live hand tracking was not tested (no camera where it was built); gestures were tested with synthetic hands.
- Two leftovers in the Doc's limits list are inconsistent with v1.1: it says the emulator has six knobs (the page has eight) and names alpha.2 as the engine version.

## How to reproduce

Open the page on an ordinary web host or as a downloaded file in Chrome or Edge, press Start camera (or Replay gestures), and use the Export menu for the time series, the balance, the emulator log or the scenario's .inp. three.js r128 loads from cdnjs.cloudflare.com and MediaPipe Tasks Vision 1.2.2 from cdn.jsdelivr.net when the camera starts, so the page needs the network for those.

## Credits and licenses

OpenSWMM Engine (HydroCouple), Apache-2.0, with the upstream NOTICE carried in the page's build manifest; Robert Dickinson's BatchSWMMRunner build. three.js r128 (MIT). MediaPipe Tasks Vision 1.2.2 (Apache-2.0) and Google's hand-landmarker model. The idea: Alireza Razeghi Haghighi's Riverlight post.

## AI use

The page says the app was built with Claude, Anthropic's AI model, in a Claude session on 8 November 2026, under Bob Dickinson's direction. He chose the problem, asked for the app, and asked for the swap to a swmm6_rel engine in v1.1. Claude looked for Riverlight's code and license, found and checked both engine builds, and wrote the page, the emulator, the gesture logic, the readers and the essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1.0 (2026-11-08): engine changed from LocalSWMM's 6.0.0-alpha.2 build, which never melts snow, to the swmm6_rel build at 137e65e. The Doc says the first version's emulator worked without snow.
- 1.0.0: first version.

---
name: Agent Relay
file: agent-relay.html
version: 1.0.0
date: 2026-11-17
author: Robert Dickinson
links: {netlify: none yet, artifact: https://claude.ai/artifact/P5QGs2t4BnJtA6FPKx87G9, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.2, source: npm @fileops/swmm-wasm-web 0.0.4 (prebuilt WebAssembly, wasm embedded in the JS), license: engine public domain; wrapper MIT (Issac Gardner)}
units: US customary (cfs, ft, in, acres)
ai_use: built with Claude (Anthropic); see AI use
---

# Agent Relay: a working miniature of an agent-per-stage water workflow

## In three points
- **What:** Runs the seven-box AI-enabled digital-delivery workflow from Ranjeet Bandiwadekar's LinkedIn diagram once on an invented town: five rule-based agents read and write one versioned GIS layer, EPA SWMM 5.2.2 runs in the browser, and a person approves every write.
- **So what:** The relay finds all four planted faults and moves the layer from v1 to v13; calibration recovers the planted multiplier (1.257 against 1.25, NSE 0.939 to 0.998), and 21 of 21 build checks pass.
- **Now what:** Use it to see where an agent-per-stage workflow needs a person and what each hand-off must carry. No language model runs, the town and its faults are synthetic, and EPA SWMM stands in for InfoWorks ICM.

**In one sentence.** Agent Relay runs the seven-box "AI-enabled digital delivery" workflow once on an invented town, using rule-based agents and a real EPA SWMM engine, and finds four planted faults in 33 engine runs with a person approving every change.

**In one paragraph.** A LinkedIn diagram by Ranjeet Bandiwadekar proposes GIS, hydraulic modelling, CAD and operations joined by AI agents around one shared GIS layer. Agent Relay builds that in miniature. Five agents, each a short list of fixed rules, read and write one versioned layer; EPA SWMM 5.2.2 runs in the browser wherever hydraulics are needed; nothing is written until a person approves it. On an invented town with four planted faults, the relay finds all four, moving the layer from v1 to v13. 21 build-time checks pass. The limit is plain: the data is synthetic and no language model is involved, so this shows that the plumbing can work, not that the products exist.

## What it does

It takes the seven-box "AI-Enabled Digital Delivery for Water Infrastructure" diagram posted on LinkedIn by Ranjeet Bandiwadekar (November 2026) and runs it once on an invented sewer network. Five rule-based agents (GIS, Modelling, Design, Integration, Operations) read and write one versioned feature layer. A person approves or rejects every proposed write. Each stage shows whether the capability shipped as a product on 2026-11-17. The output is a change log from layer v1 to v13, a SWMM input file, charts of calibration, design alternatives and sensor residuals, and CSV exports.

No language model runs in the app. EPA SWMM stands in for InfoWorks ICM.

## How it computes

**Network.** 10 circular pipes, 11 nodes (10 junctions, 1 free outfall), 6 subcatchments (12.10 ac), Manning n = 0.013, trunk slope 0.0030 ft/ft.

**Engine options written to the .inp.** FLOW_UNITS CFS, INFILTRATION HORTON (3.0 / 0.5 in/hr, decay 4 1/hr), FLOW_ROUTING DYNWAVE, ROUTING_STEP 2, SURCHARGE_METHOD SLOT, INERTIAL_DAMPING PARTIAL, VARIABLE_STEP 0.75, REPORT_STEP 00:02:00, WET_STEP 00:01:00, 6 h simulation, ALLOW_PONDING NO. A fresh WebAssembly module instance is created for every run (main thread, no worker).

**Storms.** 5-minute intensities starting at minute 30: calibration 1.10 in in 3 h, validation 0.70 in in 2 h, design 2.40 in in 2 h, operations 0.90 in in 2.5 h. All synthetic shapes.

**GIS agent (6 rules).** Unsnapped end (within 25 ft of a node: snap). Adverse slope (upstream invert below downstream: reverse). Missing diameter (propose the largest upstream diameter, marked inferred; if no upstream pipe, field request). Missing material (never inferred: field request). Diameter drop downstream (flag for a person, no fix). Pipe crossing a constraint polygon (tag).

**Modelling agent.** Refuses if any pipe is unconnected, has no diameter or runs uphill. Calibrates one multiplier k on subcatchment imperviousness: grid 0.70 to 1.60 step 0.10, four refinements at ±0.03 and ±0.06 round the best, then a parabola through the best three points. Objective: RMSE of flow in P6 at the 2-minute report times. NSE = 1 - sum((obs-sim)^2) / sum((obs-mean(obs))^2). Validates on the second storm. Then runs the design storm.

**Design agent.** A: while the engine reports flooding, increase the pipe with the highest Qpeak/Qfull by one nominal size (12, 15, 18, 21, 24, 27, 30, 36, 42, 48 in); then raise any changed pipe that is smaller than the pipe feeding it. B: FUNCTIONAL storage of constant plan area at the flooding node, +200 sq ft per run. C: reduce imperviousness in S1 to S4, +5% per run, ceiling 30%. Standards: full-flow velocity 2.0 to 10.0 ft/s, cover at least 3.0 ft (rim - invert - D at each manhole end), no diameter drop downstream, constraint tags.

**Manning, full circular pipe.** Qfull = (1.486/n) A R^(2/3) S^(1/2), A = pi D^2/4, R = D/4. Code: core.js R.qFull.

**Integration agent.** Edits to different attributes merge and are logged as auto-merged. Edits to the same attribute with different values stop; recommendation by source rank (field survey 3, record drawing 2, design assumption 1).

**Operations agent.** Residual = sensor depth - model depth at J3 and J5. Alarm when residual > 0.06 ft (3 x sensor noise sigma of 0.02 ft) for 3 consecutive 2-minute readings. Upstream alarm without downstream alarm places the restriction between the sensors. Sediment is modelled as FILLED_CIRCULAR.

**Flooding volumes** are taken from the engine's .rpt (Flow Routing Continuity, Flooding Loss, printed to 0.001 ac-ft, about 44 cu ft), not integrated from the 2-minute .out samples.

**Synthetic "sensor" records.** The same engine run with a planted truth (imperviousness x 1.25; 0.8 ft sediment in P3) plus seeded Gaussian noise (flow: 3% of value + 0.03 cfs; level: 0.02 ft).

## Inputs and outputs

Reads nothing from disk; the town is built in. Writes (through an export dialog with Download and Copy): pipes, nodes, subcatchments and change log as CSV; the SWMM .inp the agent last ran; the engine .rpt; the reality-check table and the build checks as CSV; a WebM video of the walkthrough. The .inp carries [TITLE], [OPTIONS], [EVAPORATION], [RAINGAGES], [SUBCATCHMENTS], [SUBAREAS], [INFILTRATION], [JUNCTIONS], [OUTFALLS], [STORAGE] when alternative B is chosen, [CONDUITS], [XSECTIONS], [TIMESERIES], [REPORT], [COORDINATES].

## Checks

Mechanical, run by tools/test.js against the same engine at build time: 21 of 21 pass.

| Check | Result |
|---|---|
| raw data blocks the model | pass: PB2 has no diameter; PC1 runs uphill; PC2 is not connected at both ends |
| GIS agent raises 6 findings | pass: 6 |
| no blockers after approvals | pass: 0 |
| all nodes drain to OUT | pass: 11 of 11 |
| step API and swmm_run give the same .out series | pass: 180 flow values at P6 identical |
| reader: .out series equal the .rpt tables to print precision | pass: 2880 values compared, largest difference 0.0005 |
| design storm continuity errors under 1% | pass: runoff -0.022%, routing -0.091% |
| calibration recovers the planted multiplier within 0.05 | pass: found 1.257, planted 1.25 |
| calibration improves the fit | pass: NSE 0.939 to 0.998 |
| validation event NSE above 0.9 | pass: 0.998 |
| design storm floods at J4 only | pass: 653 cu ft; nodes J4 |
| alternative A removes the flooding | pass: P4 18 to 21 in (was at 220% of full-flow capacity); P4 21 to 27 in (standards: no smaller than the 27 in pipe feeding it) |
| alternative B removes the flooding | pass: 2 sizing runs |
| alternative C removes the flooding | pass: 3 sizing runs, Disconnect 15% of impervious area |
| hydraulics alone would have stopped at a pipe that fails standards | pass: P4 18 to 21 in (was at 220% of full-flow capacity); P4 21 to 27 in (standards: no smaller than the 27 in pipe feeding it) |
| one conflict, on J4 rim | pass: 1 |
| survey rim breaks minimum cover on P4 | pass: P3: cover 2.55 ft is below 3.0 ft; P4: cover 2.55 ft is below 3.0 ft |
| as-designed network does not flood in the design storm | pass: 0.0 |
| ops agent alarms at LS-1 and not LS-2 | pass: J3 runs deeper than the model says. J5, downstream, does not. Something is holding water back between the two sensors: P3 or P4. |
| twin agrees with the sensors once the sediment is in the layer | pass: peak residual LS-1 0.059 ft, band 0.06 ft |
| repeat run gives identical peaks | pass: engine runs so far 35 |

Key numbers: calibration found k = 1.257 (planted 1.25); NSE 0.939 to 0.998, RMSE 0.38 to 0.07 cfs over 14 trial runs; validation NSE 0.998. Design storm: 653 cu ft flooding at J4 (0.015 ac-ft) with k = 1.257; 0 cu ft with k = 1. P4: Qpeak 12.67 cfs, Qfull 5.75 cfs. Alternatives: A $130,000 (P4 to 27 in), B $33,600 (400 sq ft), C $60,459 (15%). Operations: peak residual at LS-1 0.85 ft, alarm at minute 62; 0.06 ft after the field report. Design-storm continuity: runoff -0.022%, routing -0.091%. One full relay in the browser: 33 engine runs, 10 writes approved by a person, 2 auto-merged, layer v1 to v13.

Browser check: the built page was loaded in headless Chromium, the full relay was run in dark and light themes with no console errors, and the same counts and k were obtained in both.

Complexity: the SWMM App Complexity Meter analyzer was not run for this build; raw counts only (1,428 source lines in 12 files).

Human review: none yet.

## What this does not show

1. No language model runs; the agents are fixed rules. It says nothing about how an LLM agent would behave.
2. The faults were planted and the sensor records come from the same engine, so recovery is expected. It proves the plumbing, not performance on real data.
3. Nothing was run in InfoWorks ICM, ArcGIS, QGIS, AutoCAD or Civil 3D.
4. One calibration parameter, one meter, one event. Equifinality is not explored.
5. Unit costs, standards thresholds and the source ranking are illustrative.
6. Eleven nodes; no evidence on scale.
7. The reality table is one day's reading of vendor pages (2026-11-17) and no person has reviewed it.
8. The results reader is a new minimal one, not the shared parser the one-parser rule asks for. It was checked against the engine's printed tables for this network only (SWMM 5.2.2 .out, no pollutants).
9. Known engine behaviour: with SURCHARGE_METHOD EXTRAN the overtopping of J4 produced one-step pressure spikes and a sub-minute "flood" at J1 at every routing step tried (5, 2, 1 s). SLOT removed it. Not investigated further.
10. Runs on the main thread; a wasm trap would need a page reload.
11. The GIF button records WebM video (MediaRecorder), not an animated GIF, and shows only the map with captions.
12. Inside a claude.ai artifact, exports go through the platform downloads capability, which does not accept .inp or .rpt; those are saved as .inp.txt and .rpt.txt. The save path inside claude.ai was not exercised by the headless test, which loads the standalone file.

## How to reproduce

`node tools/test.js` (needs the npm package @fileops/swmm-wasm-web@0.0.4 unpacked beside the app) regenerates build/results.json and every number above. `node build.js` rebuilds agent-relay.html, this file and the essay. In the page, the header GIF button or "Play the walkthrough" runs the same relay with alternative A and the survey value chosen.

## Credits and licenses

Workflow and diagram: Ranjeet Bandiwadekar (LinkedIn, November 2026); this app is an independent illustration and is not endorsed by him. EPA SWMM 5.2.2: US Environmental Protection Agency, public domain. WebAssembly build: @fileops/swmm-wasm-web 0.0.4, Issac Gardner, MIT. InfoWorks ICM, AutoCAD and Civil 3D are Autodesk products; ArcGIS is an Esri product; QGIS is a QGIS.org project; none runs here. App: Robert Dickinson, SWMM Enablement, 2026.

Sources for the reality table:
- Model-aware AI in InfoWorks ICM 2027.2 (Autodesk Water, 14 Oct 2026): https://www.autodesk.com/blogs/water/2026/10/14/infoworks-icm-2027-2-model-aware-ai/
- InfoWorks ICM 2027.1 (Autodesk Water, 16 Jul 2026): https://www.autodesk.com/blogs/water/2026/07/16/infoworks-icm-2027-1-ai-powered-assistance-richer-esri-mapping-and-smarter-network-design/
- Autodesk Assistant product page: https://www.autodesk.com/solutions/autodesk-ai/autodesk-assistant
- AU 2026: the biggest Autodesk announcements: https://www.autodesk.com/autodesk-university/es/node/1446
- Autodesk extends reach of AI with standalone Assistant (AEC Magazine): https://aecmag.com/news/autodesk-extends-reach-of-ai-with-standalone-assistant/
- AI Assistants in ArcGIS (ArcNews, Winter 2026): https://www.esri.com/about/newsroom/arcnews/ai-assistants-in-arcgis-provide-practical-help-and-give-useful-results
- The next era of AI and ArcGIS (ArcNews): https://www.esri.com/about/newsroom/arcnews/the-next-era-of-ai-and-arcgis
- What's new in geospatial AI, November 2026 (Esri): https://www.esri.com/arcgis-blog/products/arcgis/geoai/whats-new-in-geospatial-ai-november-2026
- Synchronize feature layers (ArcGIS for AutoCAD help): https://doc.arcgis.com/en/arcgis-for-autocad/latest/manage/synchronize-feature-layers.htm

## AI use

Agent Relay was built with Claude, Anthropic's AI model (Claude Fable 5.2), in one session on 17 November 2026, under the direction of Robert (Bob) Dickinson. He chose the subject, asked for an app that shows how the workflow might work, and is responsible for publishing it. Claude researched what Autodesk and Esri ship today from the nine sources above, designed the example town and its four planted faults, wrote all of the code, the tests, the Doc essay, the Word file and this file, and chose the illustrative thresholds and unit costs. The checks are mechanical (21 at build time, plus a headless browser run in both themes). When this version was built, no person had reviewed the code, the essay or the reality table. No AI runs inside the app.

## Changes

`1.0.0 (2026-11-17)`: first version.

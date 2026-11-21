---
name: SWMM Model Comparison Tool
file: swmm-model-comparison-tool.html
version: 1.0.0
date: 2026-11-18
author: Robert Dickinson
links: {netlify: https://swmm-model-comparison-tool.netlify.app, artifact: https://claude.ai/artifact/LU6voRgvLvrobQCdCk1aY1, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4, license: public domain, role: computed demo results only}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: f297e9b0, license: Apache-2.0, role: computed demo results only}
units: US customary in the demo (CFS, ft, ac-ft); SI labels when FLOW_UNITS is CMS, LPS or MLD
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM Model Comparison Tool: find what differs between two SWMM5 or SWMM6 model sets

The SWMM Model Comparison Tool lists every difference between two SWMM5 or SWMM6 model sets, and on one unchanged input file it measured EPA SWMM 5.2.4 and OpenSWMM 6.0.0-alpha.4 within 1.68 percent of peak on every conduit.

The tool is a single web page patterned on the Model Comparison Tool that arrived in HEC-RAS 6.5. It reads the .inp, .rpt and .out files of two SWMM5 or SWMM6 runs, sorts their contents into flow data, plan, geometry and results, and reports what is unique, different and identical in each. Its readers were checked against engine output: 86 node depths and 87 link peaks from five runs on two engines, and 6 boundary volumes against the engines' own continuity tables. A repeat run came back byte for byte the same. It does not run a model, and it cannot tell you which of two models is right.

## What it does
Loads model sets (an .inp, plus optional .rpt and .out). Compares two of them and reports, for flow data, plan, geometry and results, what is unique to dataset 1, unique to dataset 2, different, and identical. Differences are dataset 2 minus dataset 1. Patterned on the HEC-RAS 6.5 Model Comparison Tool (Project, Flow, Plan, Geometry Summary and Detailed, Results; Differences and All views; File Aliases, Color Palettes, Plot Differences, Copy All). It runs no engine.

## How it computes
- Readers (src/core.js): `parseINP` (sections, feature layers, options), `parseRPT` (engine line, continuity blocks, Node Depth, Node Flooding and Link Flow summaries), `parseOUT` (classic binary layout; variable counts read from the file; closing record checked). One reader per format; the page never parses a file itself.
- Components: flow = RAINGAGES, TIMESERIES, INFLOWS, DWF, PATTERNS, RDII, HYDROGRAPHS. plan = OPTIONS. geometry = node, link, XSECTIONS, LOSSES, TRANSECTS, SUBCATCHMENTS, SUBAREAS, COORDINATES, VERTICES, POLYGONS, CURVES, STREETS, INLETS. Optional layers: infiltration, LID, groundwater, quality, controls, climate, SWMM6 sections (any section EPA SWMM5 does not define). Each component is fingerprinted with FNV-1a 32-bit over its rows with comments and spacing removed; equal fingerprints share an ID (f01, p01, g01). The fingerprint only draws the Project diagram.
- Geometry: features matched by name within a layer. Attributes compared numerically when both parse as numbers, else as case-insensitive text. XSECTIONS and LOSSES are attributes of the link; SUBAREAS, INFILTRATION and POLYGONS of the subcatchment; COORDINATES of the node. A name unique on each side under two layers of the same kind (JUNCTIONS and VIRTUAL_JUNCTIONS) is flagged as moved.
- Plan: one row per OPTIONS keyword. SWMM6-only keywords tagged: NODE_CONTINUITY, ANDERSON_ACCEL, VIRTUAL_JUNCTION_MOMENTUM, DPS_CELERITY, DPS_ALPHA, DPS_DECAY_TIME, and SURCHARGE_METHOD DYNAMIC_SLOT.
- Flow: per rain gage, the time series as intensity (VOLUME and CUMULATIVE converted), min, max, total depth. Per external FLOW inflow: Q(t) = Sfactor * TS(t) + Baseline * Pattern(t), TS interpolated linearly and zero outside its table, on a 1 minute grid over the simulation; min, max, trapezoid volume. Per DWF: Average * product of patterns (MONTHLY, DAILY, HOURLY, WEEKEND). Volumes in ac-ft (US) or 1000 m3 (SI).
- Result layers (one number per element per run, d = run2 - run1): node max depth, node max head, node flooding volume (sum of flooding rate * report step), link max |flow|, link max |velocity|, link max depth, subcatchment max runoff. Elements matched by ID, never by index.
- Hydrograph differences (on request): for each shared conduit (flow) and node (depth), over every reporting period: worst = max|a-b| / peak_a, avg = mean|a-b| / peak_a, peakChange = (peak_b - peak_a) / peak_a. Elements with peak_a below a floor are dropped (1 L/s in the file's flow units; 0.001 m of depth). Reported as a distribution: n, median, p90, max, share above 1, 10 and 25 percent. Refused when period count, report step, report start or flow units differ. Byte-identical files are reported as such and not compared.
- With no .out, node max depth and HGL and link max flow and velocity come from the two .rpt summary tables.

## Inputs and outputs
Reads .inp, .rpt (or .txt) and .out by file picker, folder picker or drop. Pairing: results attach to the .inp with the same base name, case-insensitive; a single result file of a kind pairs with a single .inp anyway; several .inp files load as several sets; a lone .rpt or .out attaches to the focused set. Writes nothing to disk except what the user exports: any table as tab-separated text (Copy All) or CSV, the whole comparison as CSV, a walkthrough GIF. Nothing is uploaded.

## Checks
Mechanical, run by the build (tests/core.test.js, tests/browser.test.js, tests/gif.test.js, tests/gifpage.test.js, tests/contrast.test.js): 69 of 69 pass.
- .out reader against the engine's report: max node depth over report periods equals "Reported Max Depth" within 0.005 ft, 86 of 86 values, 5 runs, 2 engines. Link peak in .out never exceeds the report's Maximum |Flow|: 87 of 87.
- Flow statistics against the continuity tables of both EPA runs: Base Dry weather inflow ac-ft 0.2317 vs 0.231; Base External inflow ac-ft 1.8802 vs 1.88; Base Rain depth in 1.43 vs 1.43; Relief Dry weather inflow ac-ft 0.2752 vs 0.275; Relief External inflow ac-ft 3.5434 vs 3.543; Relief Rain depth in 1.7875 vs 1.787.
- Planted changes, Base vs Relief: found exactly 2 conduits and 1 junction added, 1 subcatchment removed, 10 features altered, 4 plan keywords, 4 flow rows.
- Hydrograph measure equals corinne-testing/scripts/out-diff.js to 1e-12 on two pairs of files.
- Null controls: repeat run byte-identical (222923 bytes); same .inp on two engines gives 0 input differences; EPA 5.2.4 rejects the SWMM6-options file with 6 ERROR 205 lines.
- Pairing rules: 8 of 8 cases. Hostile element and file names render as text in every tab. Computed numbers identical in dark and light themes. No horizontal overflow at 375 px. GIF encoder output decoded by Pillow; Make a GIF pressed in a real page (8 frames). Contrast: 58 colour pairs in two themes at or above target.
- Complexity: the Meter index (HydroCouple = 100) was not computed; the analyzer could not be extracted into this build. Raw counts: 21 source files, 2452 non-blank lines, 815 functions, 1561 decision points.

Demo results (Maple Fork, 17 nodes, 17 links, 13 subcatchments, 6 h, 180 periods of 120 s):

| Comparison | Inputs differing (flow, plan, geometry) | Routing continuity % | Worst conduit flow | Worst node depth | Max peak change (conduits) |
|---|---|---|---|---|---|
| Base vs Relief, EPA 5.2.4 | 4, 4, 14 | -0.694 / -0.204 | 213.1% | 88.34% | 83.25% |
| Same .inp, EPA 5.2.4 vs OpenSWMM 6.0.0-alpha.4 | 0, 0, 0 | -0.694 / -0.636 | 1.68% (median 0.59%) | 3.85% (median 1.55%) | 0.96% |
| OpenSWMM 6.0.0-alpha.4: as written vs SWMM6 options | 0, 3, 4 | -0.636 / -0.199 | 116.97% | 62.92% | 35.17% |
| Base vs repeat run | 0, 0, 0 | -0.694 / -0.694 | 0 (byte-identical) | 0 | 0 |

Percentages are of the element's own peak in dataset 1.

## What this does not show
- Which model is right: there is no observed data.
- Generality: one invented network, one alpha commit of OpenSWMM (f297e9b0, 2026-11-18).
- CONTROLS, LID, groundwater, quality and climate sections are fingerprinted, not itemized. Files named in the .inp (rain, hot start) are not read. RDII is listed, not synthesized. Flow statistics were checked on the demo only.
- SWMM6 2D results (HDF5) are not read. Two datasets at a time.
- Not compared with the HEC-RAS tool running; built from its user's manual page.
- No person has reviewed the code or tried a real project model.
- Found during the build, not investigated: (1) in OpenSWMM 6.0.0-alpha.4 the keyword VIRTUAL_JUNCTION_MOMENTUM FULL is accepted with a warning that it is retired and treated as BASIC, so the demo omits it; (2) virtual junction J12, whose row has no maximum depth, reports 9.54 ft where the junction reported 6.00 ft (its MaxDepth); (3) the SWMM6-options .out lists nodes in a different order from the .inp (virtual junctions after the junctions).

## How to reproduce
tools/make-demo.js writes the three .inp files; tools/run-demo.sh runs EPA SWMM 5.2.4 (gcc -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0, tag v5.2.4) and OpenSWMM (cmake Release, GEOPACKAGE, HDF5, 2D and GPU off, swmm6_rel @ f297e9b0); tests/core.test.js and tests/browser.test.js check them; tools/facts.js computes every number above; tools/build.js assembles the page. In the page: Project tab, Demo comparisons, then Results, Compute Hydrograph Differences.

## Credits and licenses
HEC-RAS Model Comparison Tool (USACE HEC): the design followed. EPA SWMM 5.2.4: public domain. OpenSWMM Engine: Copyright 2026 HydroCouple Developers, Apache-2.0, https://github.com/HydroCouple/openswmm.engine; lead developer Caleb Buahin; developer and technical review Corinne Wiesner-Friedman. Only results are redistributed, no engine code. Difference measure after Corinne Wiesner-Friedman, "Exact and user-defined cross-section geometry for SWMM", HydroCouple, August 2026. html2canvas 1.4.1 (MIT) loaded from cdnjs for the GIF. App code: Copyright 2026 Robert Dickinson. Not affiliated with or endorsed by USACE, US EPA or HydroCouple.

## AI use
This app was built with Claude, Anthropic's AI model, in one working session in November 2026, at the direction of Robert (Bob) Dickinson. He chose the project, which was to duplicate the HEC-RAS Model Comparison Tool for SWMM5 and SWMM6, and he set the standing rules for how his apps are documented. Responsibility for publishing it is his.

What Claude did. It read the HEC-RAS user's manual page, decided the SWMM equivalent of each feature, wrote the demo network and its variants, compiled EPA SWMM 5.2.4 and OpenSWMM 6.0.0-alpha.4 from source and ran the five demo models, and wrote the readers, the comparison code, the page, the tests, the figures and this text.

How it was checked. The checks are mechanical, not the AI's judgment: 69 automated checks against engine output, a planted list of changes, an independent script and a real browser. No person has yet reviewed the code, opened the app on a real project model, or set it beside the HEC-RAS tool. At the time of writing Bob had not yet reviewed the results.

## Changes
`1.0.0 (2026-11-18)`: first version.


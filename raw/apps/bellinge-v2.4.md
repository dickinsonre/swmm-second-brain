---
name: Bellinge
file: bellinge.html
version: 2.4
date: 2026-11-19
author: Robert Dickinson
links: {netlify: none yet, artifact: https://claude.ai/artifact/3LdUbSXyMJ42AuCQHqHnyL, repo: none yet (the FAQ says swmm-engine-comparisons)}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: USEPA/Stormwater-Management-Model tag v5.2.4, commit: 7952ca83, license: public domain}
  - {name: OpenSWMM, version: 6.0.0-alpha.1, tag: v6.0.0-alpha.1, commit: 74ef6e27, license: Apache-2.0}
  - {name: OpenSWMM, version: 6.0.0-alpha.2, tag: v6.0.0-alpha.2, commit: 0df29948, license: Apache-2.0}
  - {name: OpenSWMM, version: 6.0.0-alpha.3, tag: v6.0.0-alpha.3, commit: 86c28a88, license: Apache-2.0}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: 3c30f1e6 (2026-10-17), license: Apache-2.0}
  - {name: SWMM 4.4H, version: 2004 CDM/OSU Fortran, source: SWMMEnablement/SWMM_MD_Documents WCH_2004_SWMM_Fortran_Code, build: SWMM 4.4H Workbench corrected build (f2c + Emscripten), license: public domain}
  - {name: EXTRAN III, version: April 1981 printed listing (Roesner, Shubinski, Aldrich, CDM), build: EXTRAN III Workbench transcription, two builds (as printed, bugs fixed), license: public domain}
dataset: {name: Bellinge open urban drainage dataset, source: Nedergaard Pedersen et al. 2021, ESSD 13 4779-4798, DTU Data collection 5029124, license: CC BY 4.0}
units: US customary shown by default (ft, cfs, in, ac) with an SI toggle; the engines run the file in its own units (Bellinge is CMS)
ai_use: built and documented with Claude (Anthropic), October and November 2026; see AI use
complexity: {index: 70.3, scale: HydroCouple = 100, meter: 1.7.0 against baseline HC-2026-11-10-h}
---

# Bellinge: one open sewer model, or your own, through seven SWMM engines (1981 to 2026) in the browser

**In one sentence.** Bellinge runs the open Odense sewer model, or your own, through seven SWMM engines from 1981 to 2026 in the browser; on the 29 June 2012 storm OpenSWMM's dynamic slot floods 18 manholes where EPA SWMM 5.2.4 floods 127.

**In one paragraph.** Bellinge is a single web page that carries the open Bellinge dataset from Odense, Denmark (1,020 nodes, 1,044 links, 713 subcatchments, and a two-gauge rain record of 749,401 wet minutes from 2009 to 2021) and seven SWMM engines compiled to WebAssembly: EXTRAN III (1981), SWMM 4.4H (2004), EPA SWMM 5.2.4 and four tags of OpenSWMM 6. A scenario is a window on the rain record plus an optional stated change to the model from a catalogue of thirty; 42 are offered, 33 pre-run. Each run gets its own worker and the results sit side by side. The runs were checked by continuity and against each other, never against observations: the thirteen level meters in the dataset are not in the page, and the Fortran engines run conversions of the file.

## What it does

Runs the published Bellinge SWMM model (Odense, Denmark: 1,020 nodes, 1,044 links, 713 subcatchments) or any EPA SWMM 5 .inp of your own through seven engines compiled to WebAssembly, inside one page, nothing uploaded. A scenario is a window on the 2009 to 2021 one-minute rain record (the 48 h base run, the 29 June 2012 storm, the six most intense bursts, or any custom window up to five days) plus an optional stated modification of the model from a catalogue of 30. Results of every scenario and engine sit side by side: summary rows, each run against a reference, flooding and outfall hydrographs, a map of freeboard and d/D or of the difference between two runs, HGL profiles, every engine's report and the conversion ledgers. The question it answers is not "what will flood" but "how far apart are the engines, and where".

## How it computes

1. **Scenario to inputs.** `SCN.apply` rewrites the published .inp text for the chosen modifications (section, lines, note recorded as a ledger); `BX.buildRunInp` sets START/END/REPORT dates, REPORT_STEP 00:05:00, ROUTING_STEP 0:00:04 (unless the modification sets one), no subcatchment series; `BX.rainFile(R, m0, m1)` cuts the rain record to the window plus one day before and one hour after, in the published line format, and `SCN.scaleRain` applies the climate factor. The file name satisfies the model's FILE gauge reference. (src/app_bellinge.js scenarioInputs; src/core.js; src/scenarios.js)
2. **Engine modes.** As written: no change. SWMM6 DW: FLOW_ROUTING forced to DYNWAVE plus SURCHARGE_METHOD DYNAMIC_SLOT, NODE_CONTINUITY SEMI_IMPLICIT, ANDERSON_ACCEL (alpha.1 skips DYNAMIC_SLOT: it initialises the dynamic-wave solver before setting the surcharge method, Routing.cpp lines 243 to 249 of the tag). FV: FLOW_ROUTING FV (alpha.3 and later). EPA SWMM 5.2.4 rejects all three keywords (ERROR 205), so it runs only as written. (src/app_run.js applyMode)
3. **Workers.** One Web Worker per run, a fresh engine instance and MEMFS per worker; swmm_open / swmm_start / swmm_step / swmm_end for SWMM 5, the handle-based swmm_engine_* API for OpenSWMM 6; .rpt and .out read back unedited (`BX.parseRpt`, `BX.parseOut`; SWMM 5 and OpenSWMM 6 share the .out layout, magic 516114522). (src/worker.js)
4. **Old engines.** SWMM 4.4H: a preparation step (rain FILE to [TIMESERIES], rating-curve outlets to capped conduits, weirs or orifices, control rules to pump start and stop depths; src/s4prep.js) then the SWMM5 to SWMM4 converter (src/s5to4.js) writes a $RUNOFF + $EXTRAN deck. EXTRAN III: the deck converter (src/x3_convert.js, src/x3core.js) writes a 1981 card deck and src/tape3.js writes SWMM 4.4H's RUNOFF.INT as a SWMM III interface tape in the layout of the 1981 manual's Figure 2-2. Limits of 1981: 187 junctions and links, 99,999 steps (NTCYC read with FORMAT I5). A run longer than 99,999 steps at the stable step is windowed: trailing one-hour mean of 4.4H's runoff, its largest peak, back to the last dry moment (2 per cent of the peak mean), one hour of lead, length floor(99999 x dt / reportStep) x reportStep (src/app_old.js x3Window). Any network larger than 187 is cut to one outfall's branch (src/submodel.js), and the branch is applied to every engine in the comparison.
5. **Comparison.** Peaks from the engines' own .rpt summaries where present (rs.peakSource = 'rpt'), else from the .out; node depth difference against the reference with a 5 cm tolerance; link peak flow difference at 10 per cent; period-by-period out-diff on a shared report grid (src/stats.js); NSE and trapezoid volumes.
6. **Design storm.** For each of eleven years (2010 to 2020) the largest depth in 5, 10, 20, 30, 60, 120, 180, 240 and 360 minutes from both gauges pooled; Gumbel by the method of moments; alternating-block storm for T = 2 to 20 years. The pooling overstates the sample (two gauges 7 km apart are not independent) and the app says so where the number is shown.

## Inputs and outputs

- Reads: EPA SWMM 5 .inp (every section parsed into tables; the engines receive the text with file references rewritten to basenames, nothing else), the data files an .inp names (rain, time series, hot start), the embedded Bellinge .inp (sha256 1ac98b81...) and rain record (rebuilds rg_bellinge_Jun2010_Aug2021.dat byte for byte, sha256 54fc24f9...).
- Writes (to save): each run's .rpt, .out and the exact .inp or card deck the engine received; the full rain .dat; a storm-events CSV; comparison CSVs; the Word file; this .md.
- Adds to an .inp: only the [OPTIONS] lines listed under How it computes, and the modification rewrites the scenario states. Strips nothing.
- Units: display in US customary or SI, converted once from the model's FLOW_UNITS; flood volumes follow the .rpt (10^6 gal or ML).

## Checks

Mechanical, on this build (2026-11-19):

- test/t_node.mjs, 16 checks: the embedded .inp has the published SHA-256 and size (1,227,640 bytes); 1,020 nodes, 1,044 links, 713 subcatchments; 995 junctions, 9 outfalls, 16 storages; 1,015 conduits, 6 pumps, 13 weirs, 3 orifices, 7 outlets; 749,401 wet minutes; the rebuilt rain .dat has the published SHA-256; the 29 June 2012 event carries 19.4 / 23.6 mm; the catalogue has 30 entries in 5 families and every entry applies; the storm window is written into [OPTIONS]; the windowed rain file holds 19.4 mm; the climate factor scales the rain by 1.3; EXTRAN III refuses the whole model and accepts the G60K220 branch (159 nodes, 167 links).
- test/ui.mjs, 19 checks in headless Chromium on both builds: the page boots into Bellinge with seven engines, fourteen runs and the two pre-recorded base runs; every view renders without a page error; the rail ends with About then Doc; the Doc tab carries what is unique, the three sizes of summary, four questions, 17 section cards each with a one-line summary, eight diagrams (one repeated), ten screenshots, seventeen listings and twelve tables, the measured complexity box, the Word file and the embedded technical summary; choosing the G60K220 branch clears the whole-model runs; the 29 June 2012 storm on the branch runs through EPA SWMM 5.2.4, OpenSWMM swmm6_rel (SWMM6 DW), SWMM 4.4H and EXTRAN III bugs fixed and reproduces the October numbers (127 / 18 / 111 / 130 flooding nodes, outfall peaks within 2 per cent, continuity errors as recorded); a builder scenario (rain × 1.3) runs and finds its unmodified baseline
- Complexity: index 70.3 against HydroCouple = 100 (Size 63.1, Structure 75.1, Test evidence 28.5, SWMM vocabulary 94.5; analyzer 1.7.0 against baseline HC-2026-11-10-h); the shipped page alone 66.5.

Engine results carried in the Doc tab (October 2026 runs, same engine files):

- EPA Example 1 outfall peak: 71.18 cfs (SWMM 5.2.4), 71.71 (SWMM 4.4H), 71.70 (EXTRAN III bugs fixed), 74.5 (OpenSWMM alpha.1), 69.2 (FV).
- 29 June 2012 storm, 03:00 to 12:00, G60K220 branch: flooding nodes 127 / 18 / 111 / 130 and outfall peak 42.6 / 42.6 / 36.5 / 40.0 cfs for SWMM 5.2.4 as written / swmm6_rel SWMM6 DW / SWMM 4.4H / EXTRAN III bugs fixed; routing continuity -0.61 / 0.14 / -9.2 / -3.3 per cent.
- 48 h base run, whole model: flooding nodes 466 (5.2.4), 643 (alpha.1 DW, runoff continuity -43.9 per cent), 62 (alpha.2 DW), 62 (alpha.3 DW), 61 (swmm6_rel DW), 520 (swmm6_rel FV); routing continuity 0.35 / -0.38 / 2.79 / 1.64 / 0.09 / -0.79 per cent; wall time 2.5 / 25.8 / 12.8 / 11.6 / 14.4 / 99 min.
- EXTRAN III window on the 48 h run: 03:46 to 17:36 on 29 June, 76 per cent of the runoff, continuity -4.6 per cent, 143 flooding manholes against 126.

Human review: none yet of the November revision; no person has compared any run with a desktop SWMM run of the same file node by node.

## What this does not show

1. No observations. The dataset's 13 level meters and flow meter (2010 to 2020) are not in the page; agreement between engines is not correctness.
2. The two Fortran engines run conversions of the file, not the file. Their ledgers (Reports view) list every mapped, approximated and dropped line. Their peaks come from printed tables, not a .out, so no period-by-period diff for them.
3. The pre-recorded 48 h base run keeps time series as 10-minute frames quantised to a byte; its peaks are from the .rpt summaries, its animation approximate.
4. OpenSWMM 6 is alpha software; numbers move between tags. Quote the tag, the options, the network and the reference engine with any number.
5. Known defects worked around, not fixed: (D1) OpenSWMM alpha.1 allocates the dynamic slot after initialising the solver, so DYNAMIC_SLOT is not written for it; (D2) alpha.1 loses 43.9 per cent of runoff on the Bellinge base run (a hydrology defect of that tag, absent in alpha.2); (D3) EXTRAN III as printed never lets a closed rectangle run full (HYDRAD label 180) and diverges on the branch; (D4) EXTRAN III as printed lets a free-surface junction head rise above ground (TRANSX lines 199 to 200); the bugs-fixed build caps it.
6. The October source tree and its three test suites (51 checks) were lost with the sandbox that held them; the source in this build was recovered from the published page and split back into modules, and the tests were rewritten (16 Node checks plus the Chromium suite). The pre-run scenario results and the recorded base run are the October files, unchanged (SHA-256 in the build record).
7. The comparison metric decides the answer: peak, continuity, flooded volume and hydrograph shape rank the engines differently on the same runs.

## How to reproduce

- Source tree: src/ (28 page modules, worker.js, template.html), essay/ (essay.json, figs.json, images.json, compose.mjs, bellinge.md), tools/ (build.mjs, make_docx.js, complexity.js, meter-core.js, meter-anchor.json, build-record-v2.3.json), test/ (t_node.mjs, ui.mjs), data/ (the engines and the base64 gzip data files as published).
- `node tools/complexity.js` then `node tools/build.mjs` writes dist/bellinge.html (single file) and dist/artifact/ (index.html + assets/), bellinge-essay.docx and bellinge.md. `node test/t_node.mjs`; `node test/ui.mjs single` and `node test/ui.mjs artifact` (Playwright Chromium).
- The October numbers: open Bellinge, scenario "29 Jun 2012 storm", network "G60K220", tick EPA SWMM 5.2.4 as written, swmm6_rel SWMM6 DW, SWMM 4.4H and EXTRAN III bugs fixed, Run. The 48 h rows were run outside the browser with the same engine files (tools/scen_batch.mjs of the October tree, not recovered).
- Engines: EPA SWMM 5.2.4 by one emcc command (MODULARIZE, EXPORT_NAME createSwmm5, SINGLE_FILE, ENVIRONMENT web,worker, the swmm_* entry points plus _malloc and _free exported); OpenSWMM 6 with -fexceptions, GEOPACKAGE / 2D / HDF5 / GPU off, four port patches on the three older tags; SWMM 4.4H and EXTRAN III through netlib f2c then emcc. The recipes are in the swmm-wasm-build skill and the two Workbench apps.

## Credits and licenses

- Bellinge dataset: Agnethe Nedergaard Pedersen, Jonas Wied Pedersen, Morten Borup, Anders Brink-Kjær, Lasse Engbo Christiansen and Peter Steen Mikkelsen (2021), Bellinge: an open urban drainage dataset, Earth System Science Data 13, 4779 to 4798, doi:10.5194/essd-13-4779-2021; DTU Data collection 5029124; CC BY 4.0.
- EPA SWMM 5.2.4: US Environmental Protection Agency, Lewis Rossman and colleagues; public domain.
- OpenSWMM 6: Caleb Buahin and the HydroCouple project, github.com/HydroCouple/openswmm.engine, Apache License 2.0. This product includes software developed by the HydroCouple project (OpenSWMM). The four OpenSWMM builds carry four small port patches on the three older tags (a static library target, no dlopen, the output thread run inline, one duplicate OpenMP fallback removed); the physics is untouched. The upstream NOTICE is reproduced in the About tab.
- SWMM 4.4H: Wayne Huber, Robert Dickinson and the SWMM 4 authors; the 2004 CDM/OSU release; the Workbench build and the S5to4 converter by Robert Dickinson with Claude.
- EXTRAN III: L. A. Roesner, R. P. Shubinski and J. A. Aldrich, Camp Dresser and McKee, April 1981; transcription, bug fixes and converter from the EXTRAN III Workbench by Robert Dickinson with Claude.
- f2c: Feldman, Gay, Maimone and Schryer, Bell Laboratories; Emscripten: Alon Zakai and contributors.
- The app, essay and this file: Robert Dickinson, 2026. Use freely with attribution; the engines keep their own licenses.

## AI use

The app was built with Claude, Anthropic's AI model, in Claude Code sessions on 17 and 18 October 2026, and revised on 19 November 2026, under the direction of Robert (Bob) Dickinson, who chose the project, the engines, the dataset and the scenario families, and who is responsible for the work. Claude compiled the seven engines to WebAssembly (transcribing and rebuilding EXTRAN III from its printed listing), wrote the converters' preparation steps, the scenario machinery, the views, the tests, the About text, the essay (in the manner of an Isaac Asimov science essay, from the app's own numbers), the diagrams, and in November the front matter the documentation rules ask for (what is unique, the three summaries, the questions and answers, the section summaries, the related-apps table, the complexity measurement), this file and the Word-file script. The checks are mechanical: SHA-256 of the data against the published files, the engines' own continuity and summary tables, the Node and headless-Chromium suites listed under Checks, and the Complexity Meter's analyzer. The October source tree was lost with its sandbox and recovered by Claude from the published page; no person has yet reviewed the November revision, and no person has compared any run with a desktop SWMM run of the same file.

## Changes

- `2.4 (2026-11-19)`: Doc tab and .docx restructured to the documentation rules: unique-ness section, three sizes of summary with one image, four opening questions with answers at the end, one-line summary per section, related apps on the author's Netlify sites, measured complexity box; Doc tab moved after About; bellinge.md written and embedded; byline is the author alone (AI use stated in its own section); source recovered from the published page, tests rewritten (16 Node + Chromium); file sizes in the text corrected to this build.
- `2.3 (2026-10-19)`: private FAQ added to the essay (Section 13).
- `2.2 (2026-10-19)`: seven diagrams, ten screenshots and seventeen code listings added to the essay and the .docx; sections 6 and 12 added.
- `2.1 (2026-10-18)`: the essay "Seven Engines and a Danish Sewer" as a Doc tab and a .docx.
- `2.0 (2026-10-18)`: Bellinge, merging Bellinge Explorer and Seven SWMM Engines: the open model with 42 scenarios (33 pre-run) or one model of your own, through seven engines; multi-file published page plus single file.

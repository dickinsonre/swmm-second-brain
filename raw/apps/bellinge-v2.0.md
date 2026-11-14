---
name: Bellinge
file: bellinge.html
version: 2.0
date: 2026-10-18
written: 2026-11-14
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/3LdUbSXyMJ42AuCQHqHnyL", netlify: "https://bellinge-swmm5-swmm6.netlify.app (not read for this summary; it may serve another build)", repo: none recorded in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model tag v5.2.4, commit 7952ca8379 (2023-10-10)", license: public domain}
  - {name: OpenSWMM, version: 6.0.0-alpha.1, source: "HydroCouple/openswmm.engine tag v6.0.0-alpha.1, commit 74ef6e27aa (2026-05-26)", license: Apache-2.0}
  - {name: OpenSWMM, version: 6.0.0-alpha.2, source: "tag v6.0.0-alpha.2, commit 0df29948a4 (2026-07-07)", license: Apache-2.0}
  - {name: OpenSWMM, version: 6.0.0-alpha.3, source: "tag v6.0.0-alpha.3, commit 86c28a886e (2026-08-11)", license: Apache-2.0}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, source: "branch swmm6_rel, commit 3c30f1e6c2 (2026-10-17)", license: Apache-2.0}
  - {name: SWMM, version: 4.4H, source: "the 2004 CDM/OSU Fortran in SWMMEnablement/SWMM_MD_Documents; the corrected build of the SWMM 4.4H Workbench (33 compile patches plus source-audit fixes)"}
  - {name: EXTRAN III, version: April 1981, source: "the EXTRAN III Workbench transcription of the printed listing (Roesner, Shubinski and Aldrich, Camp Dresser & McKee; 15 routines)"}
units: the engines run each file in its own units; the page converts displayed values to US or SI. Results below are quoted as the essay gives them, US first. Rain depths are published in mm; inches are given first and the conversion is this summary's.
ai_use: the app was built with Claude (Anthropic). This summary was written by Claude from the page's source. See AI use.
written_from: "the published artifact's page source, its embedded build record (script#d-build: version 2.0, date 2026-10-18) and its Doc essay (script#d-essay), read on 2026-11-14. The engine and data files that the published page fetches were not read. No engine was run and no test was rerun to write this file."
---

# Bellinge: one open Danish sewer model and its rain record through seven SWMM engines

This summary was written after the fact. The page carries no technical summary of its own. Every number below is copied from the page's build record, its About tab or its Doc essay, "Seven Engines and a Danish Sewer". Nothing here was measured again.

## What it does

It runs the open Bellinge model, the combined sewer of a district of Odense, Denmark, with its 2009 to 2021 one-minute rain record and a set of scenarios, through seven engines compiled to WebAssembly. One EPA SWMM 5 model of the user's own can be run in its place. A scenario is a window on the rain record with, optionally, a stated change to the published `.inp` from a catalogue: climate factor, one gauge for the whole town, a design storm from the record's own IDF, new inflows, RDII, DWF growth, imperviousness, roughness, upsized pipes, basin storage, pump capacity, offsets, random data errors and more. Each run is a Web Worker with its own in-memory file system. Nothing is uploaded.

Five engines run the scenario's `.inp` as written: EPA SWMM 5.2.4 and four generations of OpenSWMM 6. The OpenSWMM builds also run with their own solver options: SWMM6 DW (dynamic wave with the dynamic Preissmann slot, semi-implicit node continuity and Anderson acceleration) and, from alpha.3 on, FV (the explicit finite-volume solver). Two engines run decks converted from the file: SWMM 4.4H (Runoff feeding Extran through an interface file) and EXTRAN III, as printed or with its known bugs fixed, fed the runoff 4.4H computed.

The app joins two earlier apps, Bellinge Explorer and Seven SWMM Engines.

## The data

- Model: `BellingeSWMM_v021_nopervious.inp`, 1,227,640 bytes, sha256 `1ac98b81fbce2a42898423e2cf120ed46d36910637f73ad27c2a1004973c472c`. 1,020 nodes, 1,044 links and 713 subcatchments.
- Rain: gauges rg5425 and rg5427, stored delta-coded so that the published `.dat` rebuilds byte for byte (sha256 `54fc24f965b385203bd637acec4e12a769199db24bfead96c09041177ee178e9`). 749,401 wet minutes, June 2009 to August 2021.
- The 29 June 2012 storm: 0.76 in and 0.93 in (19.4 and 23.6 mm) at the two gauges, with a ten-minute peak intensity of 2.13 in/h (54 mm/h).
- The record's own IDF: annual maxima for 2010 to 2020 at both gauges, nine durations from 5 to 360 minutes, with Gumbel fits for 2, 5, 10 and 20 years.
- Scenarios: 42 offered (base, storm, six top storms, custom, and 33 pre-run model changes). The catalogue has 30 entries. The 48-hour base run is pre-recorded by EPA SWMM 5.2.4 and OpenSWMM swmm6_rel, made in Node with the same engine files on 2026-10-17. The 33 model-change scenarios were pre-run by both engines on the 29 June 2012 03:00 to 12:00 window.
- Each scenario gives the engines the published model with its window set, a 5-minute report step and subcatchment series off, plus the slice of the rain file inside the window (plus or minus 1 day).

## The engines in the page

Toolchain for the C and C++ engines: Emscripten 3.1.51 (system LLVM 18 + Binaryen 116), `-O2`, single-file, single-threaded. The two Fortran engines go through f2c and then Emscripten.

| Engine | Bytes | sha256 | Build notes from the record |
|---|---|---|---|
| EPA SWMM 5.2.4 | 678,177 | `4602e507bb5c372c5b80952e585eb13f61137251b87fdddf2ff56f2d2eb8a45f` | C, `-D_FORTIFY_SOURCE=0` |
| OpenSWMM alpha.1 | 1,523,690 | `ff5f687c78303a4ba065b41ab9d96d895df1cadd762c49c86b992efe586e7534` | No FV; four port patches |
| OpenSWMM alpha.2 | 1,823,837 | `6e78f5ca224c4f90c85fdbb1b52548e4a76ec98a637247d679b1d3a270a17c6c` | No FV; four port patches |
| OpenSWMM alpha.3 | 2,060,673 | `61421f751c86dfe8841d7c7a26052dd4adec386581ee5652e312614328898649` | FV arrives; four port patches |
| OpenSWMM swmm6_rel | 5,242,647 | `5ae19ddf4c12587206ebdef3ed3f623aabe887575ddec971fac7d2072fa2b8bf` | The engine's own Emscripten support; GeoPackage, 2D, HDF5 and GPU off |
| SWMM 4.4H | 2,085,703 | `7274315fd0404db9063c0d38618202bddffbee78b56352ba9034e6eaaf276e2c` | f2c to Emscripten 3.1.6; runs a deck made by the Workbench's S5to4 converter |
| EXTRAN III | 562,722 | `3fccd4b5cd4b451348adf9360262a3f195ea379e3ed9897574fb4ecb8e76d727` | Two builds: as printed, and with ten 1981 bug fixes, three tape-path fixes and one ground cap on free-surface junction heads |

- The four port patches on the three older OpenSWMM tags: a static library target, no dlopen, the output thread run inline, one duplicate OpenMP fallback removed. The About tab says the physics is untouched.
- The EXTRAN III builds reproduce the Workbench engines on all seven manual example decks line for line, by the build record.
- Limits of the 1981 program: 187 junctions and links, 20 storage junctions, 99,999 time steps. The whole Bellinge model is refused by EXTRAN III. The branch upstream of outfall G60K220 (159 nodes, 167 links) fits. A run longer than 99,999 steps is cut to the span around the largest runoff peak.
- The two Fortran engines report peaks from printed tables, not a `.out`.
- alpha.1 is run without DYNAMIC_SLOT. The essay gives the reason: that tag sets the surcharge method after it has initialised the dynamic-wave solver, so the slot's arrays are never allocated.

## Results as stored in the essay

**EPA Example 1, peak at the outfall.** 71.18 cfs in EPA SWMM 5.2.4, 71.71 cfs in SWMM 4.4H and 71.70 cfs in EXTRAN III with its bugs fixed. OpenSWMM alpha.1 gives 74.5 and the finite-volume solver 69.2.

**The 29 June 2012 storm (03:00 to 12:00) on the G60K220 branch** (the essay's Table 4):

| Engine | Routing continuity | Flooding nodes | Peak at the outfall |
|---|---|---|---|
| EPA SWMM 5.2.4, as written | -0.61 % | 127 | 42.6 cfs (1.206 m³/s) |
| OpenSWMM swmm6_rel, SWMM 6 dynamic wave | 0.14 % | 18 | 42.6 cfs (1.206 m³/s) |
| SWMM 4.4H | -9.2 % | 111 | 36.5 cfs (1.033 m³/s) |
| EXTRAN III, bugs fixed | -3.3 % | 130 | 40.0 cfs (1.132 m³/s) |

EXTRAN III as printed diverges on this branch. The essay traces it to the hydraulic-radius routine, which never lets a closed rectangle run full.

**The 48-hour base run on the whole model** (the essay's Table 5; run outside the browser with the same engine files):

| Engine and mode | Runoff continuity | Routing continuity | Flooding nodes | Flooded volume | To the outfalls | Wall time |
|---|---|---|---|---|---|---|
| EPA SWMM 5.2.4, as written | -0.14 % | 0.35 % | 466 | 0.25 Mgal (0.96 ML) | 6.96 Mgal (26.3 ML) | 2.5 min |
| OpenSWMM alpha.1, SWMM 6 DW | -43.9 % | -0.38 % | 643 | 1.47 Mgal (5.56 ML) | 0.43 Mgal (1.6 ML) | 25.8 min |
| OpenSWMM alpha.2, SWMM 6 DW | -0.14 % | 2.79 % | 62 | 0.17 Mgal (0.65 ML) | 6.86 Mgal (26.0 ML) | 12.8 min |
| OpenSWMM alpha.3, SWMM 6 DW | -0.14 % | 1.64 % | 62 | 0.20 Mgal (0.76 ML) | 6.92 Mgal (26.2 ML) | 11.6 min |
| OpenSWMM swmm6_rel, SWMM 6 DW | -0.14 % | 0.09 % | 61 | 0.21 Mgal (0.79 ML) | 7.03 Mgal (26.6 ML) | 14.4 min |
| OpenSWMM swmm6_rel, FV | -0.14 % | -0.79 % | 520 | 2.16 Mgal (8.19 ML) | 5.21 Mgal (19.7 ML) | 99 min |

What the essay draws from the table:

- alpha.1's runoff continuity error of -43.9 % is a hydrology defect on this model that the July tag does not have.
- From July to October the dynamic-wave routing continuity tightens from 2.79 % to 1.64 % to 0.09 %.
- The three later DW runs agree with each other at about sixty flooding nodes and differ from EPA SWMM 5.2.4 by a factor of seven.
- FV took 66,000 steps against the dynamic wave's 656,000.
- "The app does not tell you which to believe. It tells you how far apart they are."

## Checks

From the build record:

- Node, `test/t_bellinge.js`, 19 checks: `[OPTIONS]` editing per solver mode (as-written byte-identical; SWMM6 DW adds exactly DYNAMIC_SLOT, SEMI_IMPLICIT and ANDERSON_ACCEL after FLOW_ROUTING; FV replaces FLOW_ROUTING in place), referenced-file detection, unit conversion, and the five modern engines on Example1 through the worker's own call sequence.
- Node, `test/t_scenarios.js`, 12 checks: the embedded rain record rebuilds the published `.dat` byte for byte (SHA-256); 42 scenarios are offered; the storm's rain file holds the published 19.4 mm; all 30 catalogue entries apply with their defaults; the whole model is refused by EXTRAN III while the G60K220 branch fits; the 99,999-step window rule picks the span around the largest runoff peak.
- Headless Chromium, `test/ui.mjs`, 20 checks, on both the single-file and the multi-file build: the page boots into Bellinge with seven engines and the two pre-recorded base runs; every view renders; the 29 June 2012 storm on the branch runs through four engines; a model of the user's own (Example1) opens and runs four engines; no page errors.

Human review: none recorded. The About tab says no person has yet compared these runs with a desktop SWMM run of the same file node by node.

## What this does not show

From the page and its essay:

1. Agreement between engines is not correctness. No field observations are in the page. Thirteen level meters and a flow meter recorded Bellinge from 2010 to 2020; they are in the dataset and not in the page.
2. The two Fortran engines run a deck converted from the file, not the file. Their ledgers list every approximation and drop. The period-by-period diff is not available for them.
3. The comparison numbers state their metric (peak, continuity, worst instant, NSE) because each gives a different answer on the same pair of runs.
4. OpenSWMM 6 is alpha software and its results change between tags.
5. The pre-recorded base run keeps its time series as frames at ten-minute resolution, quantised to a byte, so its animations are approximate.

Added by this summary:

6. This file was written from the page, not from the build. No stored result was rerun. The engine and data files beside the published page were not read.
7. The build record gives one size and hash for EXTRAN III, though the page has two builds of it.
8. The build record is dated 2026-10-18. The essay's test table says "all passing on 19 October 2026".
9. The essay's section 9 cites "Table 3" for the 18 against 127 flooding nodes. Those numbers are in its Table 4.
10. A source comment in the page says the Bellinge mode was ported from Bellinge Explorer v1.5. The version of this app is 2.0 by its build record.

## How to reproduce

Open the artifact. The page boots into Bellinge with the two pre-recorded base runs. Pick a scenario and engines and run. Reports holds every engine's full report, the conversion ledgers for the two old engines and the exact input each engine received. The single-file build (`bellinge.html`, about 17 MB) embeds everything and works opened from disk. To check this summary, view the page source and read `script#d-build` and `script#d-essay`.

## Credits and licenses

- Bellinge: Nedergaard Pedersen, Pedersen, Borup, Brink-Kjær, Christiansen and Mikkelsen (2021), Bellinge: an open urban drainage dataset, Earth System Science Data 13, 4779-4798, doi:10.5194/essd-13-4779-2021. Data in DTU Data collection 5029124, CC BY 4.0.
- EPA SWMM 5.2.4: USEPA, public domain. Sample model: EPA's Example1.inp.
- OpenSWMM 6: HydroCouple/openswmm.engine, Apache-2.0.
- SWMM 4.4H: the 2004 CDM/OSU release. EXTRAN III: Roesner, Shubinski and Aldrich, Camp Dresser & McKee, April 1981.

## AI use

From the page's About tab: the app was built with Claude, Anthropic's AI model, in Claude Code sessions on 17 and 18 October 2026, under the direction of Robert (Bob) Dickinson. He asked for one app called Bellinge that uses all of the engines, offering Bellinge with all of its scenarios or one other SWMM5 model to run in every engine. Responsibility for the work is his. Claude checked out the three OpenSWMM tags, wrote the port patches, built the four OpenSWMM engines and EPA SWMM 5.2.4 to WebAssembly, wrote the loader, the `[OPTIONS]` editor, the worker driver, the views, the tests and the text, and reused its own Bellinge Explorer work for the two older engines. The essay was drafted by Claude in the manner of an Isaac Asimov science essay, at Bob's request, from the app's own numbers. The page says every number shown is read from the engines' own output files or from the recorded runs' files. No person has yet compared these runs with a desktop SWMM run of the same file node by node.

The essay's byline in the page reads "Robert Dickinson, with Claude".

This summary: written by Claude (model claude-fable-5-2) on 14 November 2026 at Bob's request, from the page source only. Bob has not yet read it.

## Changes

- `2.0 (2026-10-18)`: the build this summary describes. The page records no change history in the parts read.

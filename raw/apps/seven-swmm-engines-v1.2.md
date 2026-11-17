---
name: Seven SWMM Engines
file: seven-swmm-engines.html
version: "1.2"
date: 2026-10-28
written: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/JPA8SNkMHsngmP5LA93nv2", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model tag v5.2.4 (7952ca8379, 2023-10-10)", license: public domain}
  - {name: OpenSWMM 6, version: 6.0.0-alpha.1, source: "HydroCouple/openswmm.engine v6.0.0-alpha.1@74ef6e27aa (2026-05-26), four port patches", license: Apache-2.0}
  - {name: OpenSWMM 6, version: 6.0.0-alpha.2, source: "v6.0.0-alpha.2@0df29948a4 (2026-07-07), four port patches", license: Apache-2.0}
  - {name: OpenSWMM 6, version: 6.0.0-alpha.3, source: "v6.0.0-alpha.3@86c28a886e (2026-08-11), four port patches", license: Apache-2.0}
  - {name: OpenSWMM 6, version: 6.0.0-alpha.4, source: "swmm6_rel@3c30f1e6c2 (2026-10-17)", license: Apache-2.0}
  - {name: SWMM 4.4H, version: "4.4H, 2004 CDM/OSU release, corrected build of the SWMM 4.4H Workbench", source: "SWMMEnablement/SWMM_MD_Documents", license: not stated in the page}
  - {name: EXTRAN III, version: "April 1981 listing (Roesner, Shubinski and Aldrich, CDM), as printed and with the Workbench's fixes", source: "EXTRAN III Workbench transcription", license: not stated in the page}
units: "each engine runs the file in its own FLOW_UNITS; the display switch converts every value to US (ft, cfs, in, ac) or SI (m, m3/s, mm, ha); flood volumes follow the .rpt (10^6 gal or ML)"
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page's own AI-use note says the app was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/JPA8SNkMHsngmP5LA93nv2, version 1793197555-561e (index.html, 14,875,773 bytes, SHA-256 950b92cecf819fda78b871ecdc32e1f3d6743045c95dd4f68208b90847fb398d), its About and Doc tabs read in headless Chromium on 2026-11-16. No model was run to write this file."
---

# Seven SWMM Engines: one SWMM 5 input file through seven engines in the browser

## In three points
- **What:** Runs one SWMM 5 input file through seven engines in the browser (EPA SWMM 5.2.4, OpenSWMM 6 alpha.1 to alpha.4, SWMM 4.4H and EXTRAN III) and compares what they report.
- **So what:** On the sample model the outfall peak runs from 71.69 to 75.94 cfs across the runs, with EPA SWMM 5.2.4 at 73.9 cfs, while the TSS routing continuity error runs from -1.96 % (5.2.4) to -85.40 % (alpha.3 FV).
- **Now what:** Use it to see where engines part company on your own model. Agreement is not correctness: no field data is in the page, and the engines share most of their ancestry.

This summary was written after the fact. The page ships no technical summary of its own. Every number below is copied from the page's About tab or its Doc essay. No engine was run to write this file. The version is the page's own: its Doc compares "version 1.1 (old reader)" with "version 1.2 (the kit)", and its About tab says "Built 2026-10-28".

## What it does

It runs one EPA SWMM 5 input file through seven engines compiled to WebAssembly and embedded in the page, and compares what they report. Five engines run the file as written: EPA SWMM 5.2.4 and four generations of OpenSWMM 6 (alpha.1, alpha.2, alpha.3 and swmm6_rel, which reports 6.0.0-alpha.4). The OpenSWMM builds also run with their own solver options: SWMM6 DW (dynamic wave with the dynamic Preissmann slot, semi-implicit node continuity and Anderson acceleration) and, from alpha.3 on, FV (the explicit finite-volume Saint-Venant solver). Two engines run decks converted from the file: SWMM 4.4H (the 2004 Fortran, Runoff feeding Extran through an interface file) and EXTRAN III (the April 1981 listing, as printed or with its known bugs fixed, fed the runoff 4.4H computed). Nothing is uploaded; each run is a Web Worker with its own in-memory file system.

## How it computes

| Engine | Reports as | Size | Notes from the page |
|---|---|---|---|
| EPA SWMM 5.2.4 | 5.2.4 | 0.65 MB | C, src/solver + src/run; -D_FORTIFY_SOURCE=0 |
| OpenSWMM 6 alpha.1 | 6.0.0-alpha.1 | 1.45 MB | DYNAMIC_SLOT, SEMI_IMPLICIT, ANDERSON available; no FV |
| OpenSWMM 6 alpha.2 | 6.0.0-alpha.2 | 1.74 MB | [FILES] interfaces made real; no FV |
| OpenSWMM 6 alpha.3 | 6.0.0-alpha.3 | 1.97 MB | FLOW_ROUTING FV arrives |
| OpenSWMM 6 swmm6_rel | 6.0.0-alpha.4 | 5.00 MB | engine's own Emscripten support; GEOPACKAGE/2D/HDF5/GPU off |
| SWMM 4.4H | 4.4H | 1.99 MB | Runoff + Extran; explicit, fixed step; peaks from the printed tables, outfall flow from EXTRAN.INT |
| EXTRAN III | April 1981 | 0.54 MB | 187 junctions and links, 99,999 time steps; inflows from the 4.4H RUNOFF.INT as a SWMM III tape; peaks from the printed summaries, outfall flow from unit N22 |

- Builds: Emscripten 3.1.51 (system LLVM 18 + Binaryen 116), -O2, single-file, single-threaded; f2c + Emscripten for the two Fortran engines. SWMM 5 is driven through swmm_open/step/end, OpenSWMM 6 through its handle-based swmm_engine_* API. The .rpt and .out files are read back unedited.
- The three older OpenSWMM tags carry four port patches (a static library target, no dlopen, the output thread run inline, one duplicate OpenMP fallback removed); the page says "the physics is untouched".
- [OPTIONS] editing per mode: as written is byte-identical; SWMM6 DW adds exactly three keys after FLOW_ROUTING; FV replaces FLOW_ROUTING in place; kinematic-wave files are forced to DYNWAVE; alpha.1 skips DYNAMIC_SLOT and says why.
- SWMM 4.4H deck: the Workbench's SWMM5-to-SWMM4 converter (S5to4), with rain files moved to [TIMESERIES], rating-curve outlets fitted as capped conduits, weirs or orifices, and control rules reduced to pump start and stop depths.
- EXTRAN III: two builds, as printed, and with the Workbench's ten 1981 bug fixes plus three tape-path fixes and one ground cap on free-surface junction heads. 1981 limits: 187 junctions and links, 20 storage junctions, 99,999 steps, US units inside. A run longer than 99,999 steps at the stable step is cut to the span around SWMM 4.4H's largest runoff peak, and the ledger says so.
- Results: since 28 October 2026 every .rpt and .out is read by the SWMM Results Kit 1.0.0, the shared library for Bob's engine apps.

## Inputs and outputs

- Reads a SWMM 5 .inp with its referenced data files (rain gage FILE with a quoted Windows path, TIMESERIES FILE, [FILES] USE/SAVE, climate file), rewriting paths to basenames.
- Samples: EPA's Example1.inp, and the Bellinge open dataset (Nedergaard Pedersen et al. 2021, doi:10.5194/essd-13-4779-2021, CC BY 4.0) with its two FILE rain gauges inlined as [TIMESERIES] for 29-30 June 2012, only the report step (5 min) and report switches changed.
- Writes CSV and JSON exports of the run records; shows map, profile, model tables, results and reports.

## What the runs show (as stated in the Doc)

- On the sample model, total outfall flow peaks between 71.69 and 75.94 cfs; EPA SWMM 5.2.4 reports 73.9 cfs. Peaks by run: alpha.1 SWMM6 DW 75.94 cfs, alpha.4 SWMM6 DW 73.76 cfs, alpha.4 FV 71.69 cfs.
- Flow routing continuity is within 0.03 percent in every run. Alpha.1 writes 359 report periods where the others write 360.
- TSS routing continuity error: EPA SWMM 5.2.4 -1.96 %; alpha.1 SWMM6 DW -58.54 %; alpha.2 SWMM6 DW -53.43 %; alpha.3 SWMM6 DW -53.20 %; alpha.4 SWMM6 DW -1.65 %; alpha.3 FV -85.40 %; alpha.4 FV -3.70 %.
- Bellinge through EPA SWMM 5.2.4 has 1,044 links. Version 1.1's report reader read 1,037 of them; it dropped the 7 DUMMY rows and lost fields on WEIR, PUMP and ORIFICE rows. Version 1.2 reads all 1,044. Node depths and continuity were identical in both versions.

## Checks (as stated on the page)

- Node unit tests, test/t_five.js, 19 checks: [OPTIONS] editing per mode, referenced-file detection and basename rewriting, unit conversion for CFS, LPS and MGD files, and the five modern engines running Example1 through the worker's call sequence (alpha.3 and swmm6_rel FV with FLOW_ROUTING FV echoed and 0.000 % routing continuity).
- Headless Chromium, test/ui.mjs, 17 checks: the page boots on Example1, the default nine runs finish, results, map, profile, reports and model tables render, the Bellinge sample loads as SI with EXTRAN III refused on the whole model and nine branches offered; no page errors.
- Branch run, test/branch.mjs: Bellinge G60K220 through SWMM 5.2.4, SWMM 4.4H and both EXTRAN III builds. The bugs-fixed build finishes the 13.8-h window around the largest runoff peak at a 0.5 s step; the as-printed build diverges there.
- Results kit: its .out reader matched EPA SWMM 5.2.4's own swmm-output library on 96 corpus runs (11,738,268 values, 0 wrong) and on the 7 .out files the page's engines write. Its .rpt reader passed 16,533 cross-checks against the same runs' .out files on 103 reports (7,037 table rows).
- All checks are mechanical. The page names no person's review.

## What this does not show

- Agreement between engines is not correctness. No field observations are in the page, and seven engines that share most of their ancestry can agree while all being wrong.
- The two Fortran engines run a converted deck, not the file; their ledgers list every approximation and drop. They report peaks from printed tables, not a .out, so the period-by-period diff is not available for them.
- The kit is proved on SWMM 5.2.4 files and OpenSWMM 6 alphas 1 to 4. Its SWMM 5.0 and 5.1 report layouts are coded, not proved.
- OpenSWMM 6 is alpha software; its results change between tags.

## How to reproduce

Open the page, load Example1 or the Bellinge sample, tick the engine and mode cells, press Run all. The test files named above (test/t_five.js, test/ui.mjs, test/branch.mjs) are named in the page but not shipped with it.

## Credits and licenses

EPA SWMM 5.2.4: USEPA, public domain. OpenSWMM 6: HydroCouple/openswmm.engine, Apache-2.0, Copyright 2026 HydroCouple Developers. SWMM 4.4H: the 2004 CDM/OSU Fortran. EXTRAN III: Roesner, Shubinski and Aldrich, Camp Dresser & McKee, April 1981. Bellinge dataset: Nedergaard Pedersen et al. (2021), CC BY 4.0, via the self-contained copy in JoaquinAlvarado-py/LocalSWMM.

## AI use

The page says the app was built with Claude, Anthropic's AI model, in a Claude Code session on 18 October 2026 (build 2026-10-28), under the direction of Robert (Bob) Dickinson. He asked for one SWMM5 file to be run by several engines, chose the OpenSWMM 6 release ladder, asked for the SWMM6 solver options to be used, and asked for SWMM 4.4H and EXTRAN III to join. Claude built the engines, wrote the app, the tests and the text, and on 28 October 2026 moved the app onto the SWMM Results Kit at Bob's request. This summary was written by Claude on 16 November 2026 from the published page.

## Changes

- 1.2 (2026-10-28): results read by the SWMM Results Kit 1.0.0; the report reader now keeps DUMMY and OUTLET rows and the fields it used to drop on CHANNEL, weir, orifice and pump rows.
- 1.1: the page's earlier reader (the page gives no date for it).

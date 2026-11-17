---
title: "S199: Seven SWMM Engines, summary written from the page (v1.2)"
type: source
raw: raw/apps/seven-swmm-engines-v1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-10-28
ingested: 2026-11-17
tags: [apps, swmm5, swmm6, swmm4, extran, wasm, comparison, water-quality, results-reading]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Seven SWMM Engines, version 1.2 (built 28 October 2026): one SWMM 5 input file run through seven engines compiled to WebAssembly in the page, EPA SWMM 5.2.4, OpenSWMM 6 alpha.1 to alpha.4, SWMM 4.4H and EXTRAN III, with their reports compared. Raw file: [raw/apps/seven-swmm-engines-v1.2.md](../../raw/apps/seven-swmm-engines-v1.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary of its own. Claude (Anthropic) wrote this file on 16 November 2026, at Bob's request, from the published artifact (version 1793197555-561e) and its About and Doc tabs. No engine was run. Bob has not read it (Q99). The page says the app was built with Claude in a Claude Code session on 18 October 2026 (build 2026-10-28) under Bob's direction; Bob chose the OpenSWMM release ladder, the SWMM6 solver options, and asked for SWMM 4.4H and EXTRAN III to join.

**Claims worth keeping** (all copied from the page)
- Engines and sizes: EPA SWMM 5.2.4, tag v5.2.4 (7952ca8379, 2023-10-10), 0.65 MB; OpenSWMM 6 alpha.1 (74ef6e27aa, 2026-05-26), 1.45 MB; alpha.2 (0df29948a4, 2026-07-07), 1.74 MB; alpha.3 (86c28a886e, 2026-08-11), 1.97 MB, where FLOW_ROUTING FV arrives; swmm6_rel at 3c30f1e6c2 (2026-10-17), which reports 6.0.0-alpha.4, 5.00 MB; SWMM 4.4H, 1.99 MB; EXTRAN III, 0.54 MB.
- Builds: Emscripten 3.1.51, -O2, single-file, single-threaded; f2c + Emscripten for the two Fortran engines. The three older OpenSWMM tags carry four port patches (a static library target, no dlopen, the output thread run inline, one duplicate OpenMP fallback removed); the page says "the physics is untouched".
- Modes: as written (byte-identical options); SWMM6 DW adds exactly three keys after FLOW_ROUTING (the dynamic Preissmann slot, semi-implicit node continuity and Anderson acceleration); FV replaces FLOW_ROUTING. alpha.1 skips DYNAMIC_SLOT and says why.
- SWMM 4.4H runs a deck from the Workbench's converter (S5to4); EXTRAN III runs the April 1981 listing, as printed or with the Workbench's ten bug fixes plus three tape-path fixes and one ground cap, fed the runoff SWMM 4.4H computed. 1981 limits: 187 junctions and links, 20 storage junctions, 99,999 steps.
- Example 1: total outfall flow peaks between 71.69 and 75.94 cfs across the runs; EPA SWMM 5.2.4 reports 73.9 cfs; alpha.1 SWMM6 DW 75.94; alpha.4 SWMM6 DW 73.76; alpha.4 FV 71.69. Flow routing continuity within 0.03 percent in every run. alpha.1 writes 359 report periods where the others write 360.
- TSS routing continuity error on Example 1: EPA 5.2.4 -1.96 %; alpha.1 SWMM6 DW -58.54 %; alpha.2 -53.43 %; alpha.3 -53.20 %; alpha.4 SWMM6 DW -1.65 %; alpha.3 FV -85.40 %; alpha.4 FV -3.70 %.
- Bellinge through EPA 5.2.4 has 1,044 links. Version 1.1's report reader read 1,037: it dropped the 7 DUMMY rows and lost fields on WEIR, PUMP and ORIFICE rows. Version 1.2, on the SWMM Results Kit 1.0.0, reads all 1,044. Node depths and continuity were identical in both versions.
- Results Kit: its .out reader matched EPA's own swmm-output library on 96 corpus runs (11,738,268 values, 0 wrong) and on the 7 .out files the page's engines write; its .rpt reader passed 16,533 cross-checks against the same runs' .out files on 103 reports (7,037 table rows). Its SWMM 5.0 and 5.1 report layouts are coded, not proved.
- Tests named but not shipped: test/t_five.js (19 checks), test/ui.mjs (17 checks), test/branch.mjs (Bellinge G60K220 through 5.2.4, 4.4H and both EXTRAN III builds; the bugs-fixed build finishes the 13.8-h window at a 0.5 s step, the as-printed build diverges).

**Limits it states.** "Agreement between engines is not correctness." No field observations, and engines that share most of their ancestry can agree while all wrong. The two Fortran engines run a converted deck and report peaks from printed tables, so no period-by-period diff. OpenSWMM 6 is alpha software. All checks mechanical; no person's review named.

**Checked at ingest.** 1,044 - 1,037 = 7, the DUMMY rows. On Example 1, 73.9 cfs is also conduit C11's peak in the Link Flow Summary, where the .out at 5-minute reporting gives 71.18 cfs [S22](S22-li-ten-problems.md). The Bellinge app summary gives the outfall peak as 71.18 for 5.2.4, 74.5 for alpha.1 and 69.2 for finite volume [S81](S81-bellinge-summary.md). The two summaries do not say which measure each figure is, so they are not compared here (Q100).

**Feeds:** [Seven SWMM Engines (app)](../entities/seven-swmm-engines.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [SWMM Results Kit](../entities/swmm-results-kit.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Open questions](../open-questions.md).

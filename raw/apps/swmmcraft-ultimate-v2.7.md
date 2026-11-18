---
name: SWMMCRAFT Ultimate
file: swmmcraft-ultimate.html
version: 2.7
date: 2026-11-14
author: Robert Dickinson (SWMM Enablement)
links: {artifact: private claude.ai artifact, replit: paste the file into index.html, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: USEPA/Stormwater-Management-Model tag v5.2.4 commit 7952ca83, target: wasm32-wasip1 (wasi-sdk 24, clang 18, -O2), sha256: 5673fedec32405a9914102d3fb807355d2199d6d2350f3e92d270c3ae7acd28e, license: public domain}
units: US customary on screen (cfs, ft, in, ac); a metric model is shown in US units and written back in its own
ai_use: all code, tests, figures and text written by Claude (Anthropic) under Robert Dickinson's direction; see AI use
---

# SWMMCRAFT Ultimate: a block-world editor for SWMM 5 networks with EPA SWMM 5.2.4 inside the page

## In three points
- **What:** A block-world editor for SWMM 5 networks with EPA SWMM 5.2.4 compiled to WebAssembly inside the one page: draw or import a model, press RUN, and watch the engine's depths and flows.
- **So what:** 396 of 396 corpus models came back identical after import, export and rerun, and again after renaming 20,922 objects.
- **Now what:** Use it to teach and inspect small networks, not to design. The map edits six object types, and results are read at the report steps.

**In one sentence.** SWMMCRAFT is one web page in which you build or import a SWMM 5 sewer network out of blocks and EPA SWMM 5.2.4, carried inside the page, runs it; 396 published models pass through it and come back identical.

**In one paragraph.** You draw manholes, pipes, subcatchments and rain gauges on a block-world map, or import a .inp file, and press ▶ RUN. The page holds EPA's own engine compiled to WebAssembly, so what plays back is SWMM's arithmetic. An imported model keeps every section it came with: 396 models from a published corpus were imported, exported and run again, and all 396 gave identical results, unedited and again with every object renamed. Version 2.7 repairs what a fourth outside review found and adds three things for play: worlds grown from a seed, an X-ray of how full each pipe ran, and eight quests judged by the engine. The map edits only part of a model, and results are read at the report steps.

## What it does

A single HTML file. You draw or import a SWMM 5 network (junctions, outfalls, storage, conduits, subcatchments, rain gauges), press RUN, and EPA SWMM 5.2.4, compiled to WebAssembly and carried in the file, runs the model in the browser. The map then plays the engine's depths and flows. It imports and exports .inp files, keeping every section of an imported model, and reads .out files from desktop SWMM. It is a teaching and inspection tool for small networks, not a design package.

## How it computes

- **Engine.** EPA's C source, unchanged except `mkstemp()` (absent from wasi-libc; `engine/shim.c` returns a numbered name). 519 KB wasm, 184 KB gzip, base64 in the page. A JavaScript WASI shim serves `m.inp` from memory and collects `m.rpt` and `m.out`. Each run uses a fresh instance.
- **Engine start (2.7).** Tried in order: Web Worker from a Blob URL; Web Worker from a data: URL; the page's own thread (`WebAssembly.compile` + async instantiate). A worker run is stopped after 120 s; a page-thread run is not.
- **Results.** The page parses the binary .out (one record per report step). "Max reported" values and "sampled" hour counts come from those records. Columns headed "SWMM" come from the .rpt summary tables, which use every routing step. Flow statistics: max |Q|, max forward, max reverse.
- **Node states.** NEAR RIM: depth >= 95 % of max depth (SWMMCRAFT's own warning). SURCHARGED: SWMM's rule under dynamic wave, depth + invert >= crown of the highest connected link (`stats.c`), junctions only. FLOODING: SWMM overflow > 0.
- **SKETCH playback.** Before RUN, depths and flows come from a clock formula, not hydraulics. The panel says SKETCH.
- **Reference map (2.7).** One table of every place a name is read, built from the `project_findObject()` calls in SWMM 5.2.4's readers. It drives rename, delete warnings, editor choices and the export check. Conditional references included: `[LID_USAGE]` field 10 (drain to), outfall RouteTo, `[ADJUSTMENTS]` subcatchment, `[SNOWPACKS]` plowing target, `[HYDROGRAPHS]` rain gauge, `[LABELS]` anchor node.
- **Editors (2.7).** Each field remembers the text shown when the dialog opened. SAVE writes only fields whose text changed. A preview lists the changes. No change: nothing written, no undo step.
- **World seeds (2.7).** `seedWorld(text,size,level)`: FNV-style hash of `text|size|level` seeds a xorshift32 stream. Random tree on a grid (170-unit cells) rooted on the east edge; one subcatchment at most per cell, inset 10 to 34 units; inverts rise upstream at 0.4 to 1.5 % (0.4 to 1.0 % on the outfall pipe); storm = the example hyetograph x (0.6 to 1.6). Sizing: Q = i_peak * sum(A * C), C = imperv + (1 - imperv) * max(0, 1 - 0.5 / i_peak) (0.5 in/hr is the exporter's default Horton minimum rate); D = 12 * (Q * 0.013 / (0.463 * sqrt(S)))^(3/8) in, rounded up to a stock size (12 to 96 in). PEACEFUL: Q x 2. NORMAL: Q x 1. HARD: Q x 1, then one trunk pipe (tributary C*A >= half the total) set to the largest stock size <= 62 % of its design diameter.
- **X-ray (2.7).** Per conduit, max over report steps of SWMM's link Capacity result (depth / full depth): < 0.5 green, < 0.8 yellow, < 1 orange, >= 1 red, tagged with the percent. Paints nothing when the results do not match the current map.
- **Quest book (2.7).** Eight tasks judged from engine results only (run; select the conduit with the largest max |Q|; X-ray; a surcharged or flooding junction; a later run with none; surface runoff down >= 10 % under equal precipitation; COMPARE with A pinned to a different run; run a seeded world). Progress in `localStorage` key `swmmcraft_quests_v1`.

## Inputs and outputs

- Reads: SWMM 5 `.inp` (all sections; headers may carry `;` comments), SWMM binary `.out`, SWMMCRAFT project JSON.
- Writes: `.inp` (an imported file keeps its own section order, units, options and every section the map does not edit; `[REPORT]` is overridden to NODES ALL, LINKS ALL), project JSON, CSV tables, a 12 s WebM recording.
- For a model drawn in the page the exporter writes stated defaults: subareas 0.012 / 0.10 / 0.05 / 0.10 / 25 % / OUTLET, Horton 3 / 0.5 / 4 / 7 / 0, FREE outfalls, 1,000 ft2 storage, circular conduits, zero offsets.
- Names are compared without regard to case, as SWMM compares them.

## Checks

Mechanical, all on the 2.7 build unless stated. Corpus = Bob's 1729-SWMM5-Models-2030, files under 300 KB, duplicates removed: 459 models, of which 396 run in EPA SWMM 5.2.4 as they stand.

| Check | Result |
|---|---|
| Example in the in-page engine | C6 max reported 26.887 cfs; SWMM summary 26.96; continuity -0.139 % runoff, 0.008 % routing |
| In-page vs native engine, .out byte for byte | 13 of 13 models identical (2.4) |
| Unedited round trip (import, export, run, compare every depth and flow by name) | 396 of 396 identical |
| Rename every node, conduit, subcatchment and gauge, export, run | 396 of 396 identical; 20,922 objects renamed, 31,746 references moved, 20,441 series compared, 0 values differ |
| Same test before the gauge repair | 350 identical, 23 changed rain, 23 refused to export |
| Editor sweep in Chromium (SAVE unchanged = identical export; one number changed = one token on one line; UNDO = identical) | 436 exportable models, 12,128 checks, 0 failures |
| Names where 2.6 never looked | present in 27 of 396 models |
| Review-4 fixtures | LID drain and RouteTo renames run with 0 errors; divider conduit keeps D1 after a roughness edit; commented headers import 7 nodes, 7 links |
| Keyboard-only session | Tab stays in the dialog; Escape closes; focus returns to the opener (HELP, TABLE, EXPORT); Delete under a dialog deletes nothing |
| Engine start with the worker refused, Blob-only refused, worker failing | all play C6 at 26.887 cfs |
| Page node states vs SWMM's tables (2.5, 254 dynamic-wave models) | 3,140 of 3,310 surcharged junctions flagged, 0 false positives |
| Seeded worlds, seeds 1 to 100 x 3 sizes x 3 difficulties = 900 | all deterministic, valid, 0 overlap area, 0 crossing pipes, 0 adverse slopes, 0 SWMM errors; max continuity error 0.201 % |
| Seeded worlds by difficulty (SWMM summary tables) | PEACEFUL 296 clean, 4 surcharged, 0 flooded; NORMAL 136 clean, 163 surcharged, 1 flooded; HARD 0 clean, 300 surcharged, 296 flooded; node above the small pipe surcharged in 300 of 300 |
| Quests in Chromium | 8 of 8 completed on the example; wrong pipe and A = B earn nothing; progress survives reload |
| Complexity, SWMM App Complexity Meter (meter-core.js 1.7.0, baseline HC-2026-11-10-h, HydroCouple = 100) | index 68.5 from 71 hand-written source files (Size 66.5, Structure 75.5, Test evidence 3.4, SWMM vocabulary 92.0); shipped .html alone 62.3 |
| Earlier review checks (rotation and picking 112 of 112, projects, .out coverage, case, status, touch emulation, text census) | same results as 2.6 |

Human review: Robert Dickinson directed the work and passed on four outside reviews (2.2: 76/100, 2.3: 79, 2.4: 86, 2.6: 82). No person has yet checked the items listed below.

## What this does not show

1. SKETCH playback is synthetic until RUN.
2. Results from the .out are sampled at report steps; SWMM's summary values can be higher (26.96 vs 26.887 cfs for C6).
3. The map edits only junctions, outfalls, storage, conduits, subcatchments and gauges. Everything else is carried, renamed with what it names, and not editable. Names inside external rainfall or inflow files are not renamed.
4. A gauge reading rainfall from an external file has no rain in the page.
5. Seeded worlds are plausible layouts, not designs; difficulty names state odds over 900 worlds, not a promise for one world. A later generator will grow different worlds from the same seed.
6. RUN inside the Claude preview was tested by refusing the worker in Chromium, not in the preview itself.
7. Touch was tested in emulation (iPhone 13 profile), not on a phone. Dialogs were not tested with a screen reader.
8. Not checked by a person: essay wording, error and report messages, quest wording, exporter default parameters, behavior on a production model.
9. Map is schematic: subcatchment area is typed, not measured; a new conduit's length is its on-screen length read as feet.

## How to reproduce

From the project folder (Node 22, Playwright Chromium, swmm-toolkit 0.17.0 for the native engine):

```
node build.js                                   # builds the .html and .docx; fails if any number in the essay disagrees with its test output
node tools/corpus_roundtrip.js <html> <tag>     # unedited round trip
node tools/corpus_rename.js <html> <tag>        # rename everything
node tools/editor_sweep.js <html> <tag>         # editor sweep
node tools/review4_repro.js <html> <tag>        # fourth-review fixtures
node tools/keyboard_check.js <html>
node tools/run_fallback_check.js <html>
node tools/seed_check.js <html> 100             # 900 seeded worlds
node tools/quest_check.js <html>
```

Fixtures: `review4/fx_lid_drain.inp`, `fx_route_to.inp`, `fx_divider.inp`, `fx_header_comment.inp`. Example export: `runs/v2_export.inp`.

## Credits and licenses

- EPA SWMM 5.2.4: U.S. Environmental Protection Agency, public domain. Compiled unchanged apart from the `mkstemp()` stand-in.
- Fonts, embedded under the SIL Open Font License 1.1: Tiny5 (Copyright 2022-2024 The Tiny5 Project Authors), Press Start 2P (Copyright 2012 The Press Start 2P Project Authors, Reserved Font Name "Press Start 2P"), VT323 (Copyright 2011 The VT323 Project Authors).
- Every texture, icon and the inspector Manny are drawn by the page. No game assets, fonts, sounds or names from any commercial game.
- Test corpus: 1729-SWMM5-Models-2030, Robert Dickinson.
- Outside reviewer of 2.2, 2.3, 2.4 and 2.6: reviews passed on by Robert Dickinson as written.
- App code license: none stated yet by the author.

## AI use

SWMMCRAFT was built with Claude, Anthropic's AI model, in Claude sessions in October and November 2026, under the direction of Robert (Bob) Dickinson, who asked for the app and each revision and is responsible for the work. Claude wrote all of the code, the test scripts, the figures, the Doc essay, the .docx, the About page and this file. The world seeds, X-ray and quest book were proposed by Claude when Bob asked for imaginative improvements. The checks above are mechanical (engine runs, scripted comparisons); the items under "What this does not show" have not been reviewed by a person.

## Changes

- `2.7 (2026-11-14)`: fourth review: one reference map (LID drain, RouteTo, adjustments, snowpacks, hydrograph gauges, labels); editors write only changed fields, with a preview; renamed gauges keep their own row; commented section headers; three-way engine start and a run error that stays; dialog focus trap and return; sampled vs SWMM summary columns; reverse flow; FIT and per-view cameras; change log read by Manny. Added world seeds, X-ray, quest book, this file; the Doc opens with three sizes of summary and five questions and closes with their answers and a measured complexity box.
- `2.6 (2026-11-03)`: block-game skin, pixel icons, embedded fonts.
- `2.5`: carry-everything import and export, case-blind names, three node states, object table.
- `2.4`: EPA SWMM 5.2.4 in the page, projects, phone layout.
- `2.3`: reference-safe rename, unit-aware import, exact overlap test.
- `2.2`: view rotation. `2.1`: block-world redesign, Manny. `2.0`: export that runs in EPA SWMM.

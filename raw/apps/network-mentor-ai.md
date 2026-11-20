---
name: Network Mentor AI
file: network-mentor-ai.html
version: 1.1.0
date: 2026-11-19
author: Robert Dickinson
links: {netlify: "https://network-mentor-ai.netlify.app", artifact: "https://claude.ai/artifact/45htVKeNxZdQZW4mVZcnPk", repo: none}
origin: Lovable project network-mentor-ai (React, TanStack Start, Supabase), MIT License, (c) 2026 Robert Dickinson
engines:
  - {name: EPA SWMM, version: 5.2.4, use: "one run, offline; results embedded", via: "swmm-toolkit 0.17.0 (PyPI), engine version 52004", cross_check: "swmm-toolkit 0.16.2, identical report apart from timestamps", license: public domain}
runtime_engine: none
units: US customary (CFS, ft, in, acres)
complexity: {index: 59.3, shipped_file_alone: 56.7, scale: "HydroCouple org = 100", analyzer: "meter-core.js 1.7.0", baseline: HC-2026-11-10-h}
ai_use: built with Claude (Anthropic); see AI use
---

# Network Mentor AI: guided tours of six drainage programs on one real SWMM run

**In one sentence.** Network Mentor AI builds guided tours of six drainage programs on replicas that share one storm-sewer model, and every number they show comes from a real EPA SWMM 5.2.4 run, with routing continuity of -0.007 percent.

**In one paragraph.** Network Mentor AI is a single-file studio for writing guided tours of InfoWorks ICM, ICM SWMM networks, EPA SWMM 5, OpenSWMM 6 with HydroCouple, InfoDrainage and Civil 3D drainage. Each replica has screens, a model tree, a ribbon, a map, a run window and results, and each tour step lights one element. It began as a Lovable app whose run window printed "Continuity 99.6%" for every product; reading its source turned up eighteen defects. In this edition all six replicas load one 35.4-acre network run once through EPA SWMM 5.2.4, thirteen checks tie the page's numbers to that run, and all 47 template steps find their target, against 39 of 43 before. The main limit: one network and one storm.

## What it does

A single-file studio for writing guided tours ("onboarding tours") of drainage and hydraulic modeling software. It holds replicas of six programs: InfoWorks ICM, ICM SWMM networks, EPA SWMM 5, OpenSWMM 6 with HydroCouple, InfoDrainage and Civil 3D drainage. A tour is a list of steps; each step names a screen and one element and carries a Markdown lesson. Users play 9 templates, write tours in an editor, have Claude draft one (inside Claude) or get an offline draft, and share tours as codes, JSON, PDF or CSV. All replicas show one demo network whose numbers come from one EPA SWMM 5.2.4 run.

## How it computes

Tours

- Every element a tour can target carries a `data-sim` name (for example `run-start`, `rpt-flooding`, `map-node-j3`). A step is `{screenId, targetSim, title, body, action}` with action in `look | click | type`.
- Showing a step: render the step's screen, `querySelector("[data-sim=...]")`, open collapsed tree parents, measure `getBoundingClientRect`, draw a scrim with a hole (SVG even-odd path) and a ring, place the callout right, else left, below or above, clamped inside the stage. A missing target shows a warning in the callout.
- "Let me try": four blocking rectangles surround the hole, so only the target takes clicks; the click reaches the control, then the tour advances.
- Target list: each product screen is rendered off-screen at load and every `data-sim` collected (280 product:name pairs across 6 products). The editor offers only names present on the step's screen.
- Claude draft (published artifact only, `sample` capability): the prompt carries persona, goal, the screen list with names and labels, the demo-model facts and the JSON shape. The checker then replaces unknown screens with the product default, moves a step whose name lives on another screen, nulls names that exist nowhere, and forces action to `look` when unknown.
- Offline draft: template steps for the product scored by goal-word overlap (4+ letters, light stemming), +3 for run or result words; top 6 kept in screen order.

Demo model (EPA SWMM 5 input, `network-mentor-demo.inp`)

- Layout from the Lovable app's map, 1 map unit = 5 ft. Subcatchments S1, S2, S3 = 11.36, 11.62, 12.43 ac (35.4 ac), from the polygons; polygons do not overlap. Width = area / flow length (450, 500, 520 ft). Impervious 50, 65, 40 %. Horton 3.0 / 0.5 in/hr, decay 4.0 /hr.
- Junction inverts J1 110.0, J2 106.5, J3 103.0, J4 100.0 ft; outfall Out1 97.0 ft, FREE. Max depth J1 6.0 ft (J1 is meant to flood), others 9.0 to 10.0 ft.
- Conduits C1 to C4: circular 30, 54, 60, 60 in, n = 0.013, lengths 657.6, 632.5, 632.5, 670.8 ft.
- Storm: SCS Type II 24 h, 5.00 in, 15-minute INTENSITY blocks interpolated from the TR-55 cumulative table (illustrative depth, no location).
- Options: DYNWAVE, ROUTING_STEP 15 s, VARIABLE_STEP 0.75, INERTIAL_DAMPING PARTIAL, NORMAL_FLOW_LIMITED BOTH, REPORT_STEP 5 min, 24 h.

Equations used in the page

- Continuity: `E = 100 * (1 - total_outflow / total_inflow)`, outflow including flooding and final storage, inflow including initial storage (`src/solver/massbal.c`, lines 872 to 894, EPA SWMM 5.2.4).
- Full-flow capacity in the Properties grid: `Q = (1.486/n) * A * R^(2/3) * S^(1/2)`, circular, R = D/4, S from inverts and length.
- Storm depth from the series: the binary output starts at 0:05 and, at an interval boundary, reports the rate that starts there (the 24:00 sample is 0), so depth = sum(i * 5/60) + first sample * 5/60.

## Inputs and outputs

- Reads: share code (`LZString.compressToEncodedURIComponent` of tour JSON), share link with `#t=`, tour JSON (one tour or an array), including tours exported from the Lovable build.
- Writes: tour JSON; steps CSV (`step,screen,screen_label,target,action,title,body`); tour PDF (US Letter, jsPDF); template catalog CSV; demo .inp, .rpt and series CSV; walkthrough GIF (own LZW encoder, WebM fallback); this .md.
- Keeps: tours in `localStorage` key `network-mentor-ai:tours:v1`, QA ticks in `network-mentor-ai:qa:v1`, theme in `network-mentor-ai_theme`. Nothing leaves the browser except a Claude draft request inside Claude.

## Checks

Mechanical (this build):

- Template targets: 47 of 47 steps light their target with no warning, every template played in a headless browser in dark and light themes; Done closes every tour. Lovable build: 39 of 43, read from its source (not run).
- Engine numbers, 13 of 13 agree (QA tab, re-run on every visit):
  - template quotes: runoff continuity -0.026 %, routing -0.007 %, J1 flooding 0.12 h at 8.23 cfs, C1 Max/Full Flow 1.40, 0.05 % steps not converging;
  - peak flow / Manning capacity for C1 to C4 vs the report's Max/Full Flow (C1: 41.97 / 29.92 = 1.403 vs 1.40);
  - both continuity errors recomputed from the printed volumes (routing: -0.011 % vs -0.007 %, within the rounding band);
  - storm depth from the series = 5.000 in;
  - 5-minute series peaks never exceed the report peaks, 9 elements, gaps 0.02 to 2.55 cfs.
- Functional checks (Playwright, `func.js`): 31 of 31 pass, including editor reorder and pick, JSON/CSV/PDF export, share-code round trip, Lovable link import, "Let me try" reaching the Start button, offline draft targets, draft checker, GIF written, embedded .md, app tour. Contrast on the QA tab: dark "52 of 52 pass · lowest 5.49:1", light "52 of 52 pass · lowest 4.56:1".
- Phone width (375 px): 7 of 7 views without horizontal page scroll.
- Related-topics links: 9 Netlify sites opened and titles checked on 2026-11-19.
- Complexity (SWMM App Complexity Meter, meter-core.js 1.7.0, baseline HC-2026-11-10-h): 59.3 for the 18 hand-written source files; 56.7 for the shipped .html alone. Test evidence reads 0: the analyzer does not count the Playwright `ok()` checks.

Human review: none recorded for this build.

## What this does not show

1. The replicas copy layouts, not solvers. ICM, InfoDrainage and Civil 3D replicas show the EPA SWMM 5.2.4 numbers and say so.
2. ICM SWMM networks run Autodesk's build of the SWMM 5 engine; OpenSWMM 6 is a separate engine. Neither was run.
3. One network, one storm. Teaches reading a run, not design.
4. The Claude draft path was not exercised from the build session; the offline path and the checker were.
5. The ICM 2D mesh and the HydroCouple coupling graph are teaching drawings.
6. Share links work on an ordinary web host; inside Claude use the share code. Tours stay in one browser until exported.
7. Not checked by a person: the corrected ICM, InfoDrainage and Civil 3D template prose; the HydroCouple sketch.
8. The Lovable comparison (39 of 43) and the 18 findings come from reading its source; the Lovable build was not run.

## How to reproduce

```
python3 build/make_inp.py 5.0 > run/demo.inp
python3 -c "from swmm.toolkit import solver; solver.swmm_run('run/demo.inp','run/demo.rpt','run/demo.out')"   # swmm-toolkit 0.17.0
python3 -I build/extract.py && python3 -I build/pack_demo.py
node build/make.js        # complexity, build, tests, rebuild, Word file, this .md
```

Test scripts: `build/smoke.js` (every template, both themes), `build/func.js` (functional), `build/mobile.js` (375 px), `build/complexity.js` (Meter).

## Credits and licenses

- Original app and this edition: Robert Dickinson, MIT License.
- EPA SWMM 5.2.4: US EPA, public domain (17 USC 105). The EPA does not endorse this app.
- swmm-toolkit (PyPI) used to run the engine offline.
- HydroCouple and OpenSWMM 6 (github.com/HydroCouple) are described, not bundled.
- jsPDF 2.5.1 and html2canvas 1.4.1 (MIT, cdnjs); lz-string 1.5.0 (MIT, jsDelivr); fonts Barlow, Barlow Condensed, IBM Plex Mono, Source Serif 4 (SIL OFL, Google Fonts).
- InfoWorks ICM, InfoDrainage and Civil 3D are Autodesk products; their layouts are imitated for training only. No affiliation with Autodesk, the US EPA or the HydroCouple developers.
- SWMM App Complexity Meter analyzer, read from the Meter artifact for the complexity box.

## AI use

This app was rebuilt with Claude, Anthropic's AI model, in Claude sessions in October and November 2026, under the direction of Robert (Bob) Dickinson, who wrote the original Lovable app, chose the rebuild, set the house rules the November revision follows, and is responsible for it.

**What Claude did.** It read the Lovable source and wrote the findings register; designed the demo network's SWMM input (scale, elevations, pipe sizes, storm) and ran it through EPA SWMM 5.2.4; wrote all of this page's code, the corrected tour templates, the help articles, the Doc essay, the matching Word document and the technical summary (.md); and wrote this text. In November it added the opening summaries, the four questions and their answers, the related-topics list, and the complexity measurement made with the SWMM App Complexity Meter's own analyzer. Inside Claude, the Generate tour button asks Claude for a draft at the moment you click it; that draft is AI output, and the app checks its targets, not its prose.

**How it was checked.** Mechanically: the engine numbers on the QA tab are compared with the SWMM report each time it opens; every template target is looked up on its rendered screen; contrast is measured; a headless browser played every template in both themes and ran the functional checks listed in the .md; every related-topics link was opened and its title checked.

**Not yet checked by a person.** The corrected template prose about ICM, InfoDrainage and Civil 3D behavior, and the illustrative HydroCouple workflow.

## Changes

- `1.1.0 (2026-11-19)`: Doc tab and Word edition reworked to the current house rules: What is unique, one-sentence, one-paragraph and one-page summaries, four questions answered at the end, a one-sentence lead under every section, related topics from the Netlify catalog, and a measured complexity box (HydroCouple = 100). Added the technical summary network-mentor-ai.md, embedded in the page and linked from About. Credits corrected: lz-string loads from jsDelivr.
- `1.0.0 (2026-10-25)`: Rebuilt from the Lovable source as one HTML file: six replicas on one EPA SWMM 5.2.4 run, nine corrected templates, editor, player, share codes, JSON/PDF/CSV export, offline and Claude tour drafts, QA tab, findings register (18 defects), Doc tab and Word edition.

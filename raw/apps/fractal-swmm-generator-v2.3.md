---
name: Fractal SWMM5/SWMM6 Network Generator
file: fractal-swmm-generator-v2.3.html
version: 2.3
date: 2026-11-12
author: Robert Dickinson
links: {netlify: none recorded, artifact: https://claude.ai/artifact/RLo2udE9LTzQc9oJurFjLd (private), repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: USEPA/Stormwater-Management-Model tag v5.2.4, build: wasm32-wasi reactor (clang 18) reporting VERSION 52004, sha256: edf4f4eefc21dd862b89a183371d2934b998c324628cff38a8a7e35e4a811c7e, license: public domain}
targets_written_not_run:
  - {name: OpenSWMM legacy, version: 5.3.0-beta.3}
  - {name: OpenSWMM, version: 6.0.0-alpha.3+}
units: US customary (CFS, ft, in, ac); 1 map unit = 3 ft
ai_use: built with Claude (Anthropic); see AI use
---

# Fractal SWMM5/SWMM6 Network Generator: grows a drainage network from a fractal rule, shows every step, runs it, and audits it

## What it does
Generates tree-shaped drainage networks from 22 fractal patterns, gives every inlet its exact Voronoi cell of one fixed basin, and writes a runnable SWMM .inp. The Build tab replays how the file was made, one logged step at a time, with the rule and its numbers. The Generator tab runs the exported file in an embedded EPA SWMM 5.2.4, checks it (Evidence), charts it from the .out file (Results), and since v2.3 audits its hydraulics pipe by pipe. It is a teaching and test-model generator. It is not a design tool.

## How it computes
Network (core.js, generateNetwork). Depth-first recursion from the outfall upstream; d = recursion depth, o = stream order of a node (1 at the trunk, d at the tips).
- Length: L = 300 ft * r_L^(d-o) for the Horton family (r_L 0.5 to 0.9, default 0.7); other patterns use their own rule, printed at each Build step.
- Diameter: D = D0 * 1.3^(d-o), D0 from 4 to 60 in (default 12). Arterial side branches: one collector class, factor 0.7, applied once and inherited upstream.
- Invert: z = 100 + 2*o + lift (ft). lift = sum of 0.005 * L over every same-order pipe between the node and the outfall, rounded to 0.01 ft. Zero for 20 of 22 patterns; nonzero for Spine (trunk) and DLA (beyond depth d). Radial hub: 101 ft.
- Junction max depth 10 ft, no ponding. Outfall Out1: invert 100 ft, FREE. Manning n 0.013, circular pipes, no offsets.
- Inlets: every non-outfall node with no upstream pipe, tagged from the finished graph.
- Node budgets: Exact (depth-first build cut at the count) or Nearest full depth. Cap 5,000 nodes.

Subcatchments (generateCells). Basin fixed at 1,740 x 1,440 ft = 57.52 ac. Each inlet gets its exact Voronoi cell clipped to the basin (half-plane clipping). W = 2*sqrt(A). 50 % impervious, 2 % slope, n 0.015 / 0.25, depression storage 0.06 / 0.2 in, 25 % zero-storage, Horton 3.0 to 0.5 in/hr, decay 4 /hr. The jagged outline on the map is drawing only; [POLYGONS] gets the exact cell.

Storm and options (genINP). 01/01/2026 00:00 to 06:00, DYNWAVE, ROUTING_STEP 5 s, REPORT_STEP 5 min, WET_STEP 1 min. RG1 from TS1: 24 five-minute blocks tracing 0 to 1.0 in/hr at 0:30, 0.4 at 1:00, 0 at 2:00; total 0.80 in, peak block 0.95 in/hr. [REPORT] SUBCATCHMENTS, NODES, LINKS ALL (without it the .out holds no series). SWMM6-only lines (DYNAMIC_SLOT, SEMI_IMPLICIT, ANDERSON_ACCEL, [VIRTUAL_JUNCTIONS]) are written to the SWMM6 target only.

Step log. Every object carries the index k of the log entry that created it. Frame k = objects with index <= k, written by the same .inp writer as Export. The last frame must equal the exported text byte for byte (FNV-1a shown).

Hydraulic audit (core.js, geomAudit, hydAudit; v2.3).
- Full-flow capacity: Qfull = (1.486/n) * A * R^(2/3) * S^(1/2), A = pi*D^2/4, R = D/4, S from the two inverts.
- From the .out (5-min report steps): max |flow|, max depth, max velocity per pipe; ratio = Qmax/Qfull; "ran full" = depth >= D.
- Screening values, this generator's own: slope > 10 %, length < 10 ft, same-order minimum slope 0.5 %.
- Pipe volume = sum of (pi*D^2/4)*L, ft3.
- Smallest D0 (searchSmallestD0): bisection over whole inches 4 to 60 for the smallest D0 with no node in the .rpt Node Flooding Summary. Tests 60 and 4 first, then halves. Trial text comes from inpWithD0: the same writer, diameters recomputed with the generator's expression.

Results reader (readOut). Classic SWMM .out binary: magic 516114522, object IDs, variable counts, one record per report step. Node vars 0 depth, 4 total inflow, 5 flooding; link vars 0 flow, 1 depth, 2 velocity; subcatchment var 4 runoff; system vars 1 rainfall, 10 flooding. Adapted from out-diff.js in Bob's corinne-testing skill.

## Inputs and outputs
- Reads: project .json files saved by the app (values range-checked on open). No .inp import.
- Writes: .inp (SWMM5, legacy 5.3 or SWMM6 target), .rpt of the last run, step-log and network .csv, project .json (parameters, seed, exact .inp with FNV-1a, step log, engine SHA-256, report, evidence), .gif or .webm walkthrough, this .md.
- As a claude.ai artifact, .inp and .rpt are saved with .txt appended (host file-type list).

## Checks
Mechanical, on this build (v2.3):
- Regression suite: 182 generated models (22 patterns, depths 2, 3, 5, 7, both node-budget modes, SWMM6 targets), 137 engine runs, 0 failures. Replay text = export text on all 182; no uphill pipe; no pipe larger than the pipe below it; inlets = leaves; area closes to the basin within 1 part in a million.
- v2.3 audit: 66 engine runs (22 patterns x depth 3, 50 nodes, 120 nodes). Flat pipes: 0. WARNING lines: 0.
- v2.2 to v2.3: 154 models compared; 134 byte-identical; the 20 that differ are Spine (7), DLA (7), Arterial (6).
- Spine, 85 nodes: v2.2 11 flat pipes, 11 WARNING 04, Out1 peak 22.55 cfs at 0.67 h; v2.3 0 flat, 0 warnings, 26.68 cfs at 0.58 h.
- DLA, depth 3: v2.2 139 flat pipes, 111 flooded nodes, routing continuity -2.13 %; v2.3 0 flat, 16 flooded, -1.363 %.
- Arterial, 120 nodes: v2.2 smallest pipe 2.9 in, 78 of 119 under 6 in, 3 nodes flood; v2.3 smallest 8.4 in, 0 flood.
- At 50 nodes, 20 of 22 patterns peak at Out1 between 26.40 and 27.18 cfs at 0.58 h; longest-path travel 1.2 to 4.3 min. Outliers: Nested (24.71 cfs, one report step late), DLA (8.55 cfs, 22 nodes flood).
- Smallest D0, 50 nodes, 174 runs: Basin 8 in (2,003 ft3); Radial 9 in (2,738 ft3); Koch 11 in (3,127 ft3); H-Tree 7 in (3,964 ft3); Arterial 12 in (4,401 ft3); Grid 9 in (5,129 ft3); Tokunaga 8 in (5,233 ft3); Alluvial 11 in (5,564 ft3); Sierpinski 10 in (5,794 ft3); Spine 8 in (5,898 ft3); Cantor 11 in (6,062 ft3); Delta 11 in (6,422 ft3); Meander 9 in (6,554 ft3); Pythagoras 9 in (6,699 ft3); Herring 8 in (7,034 ft3); Random 10 in (7,574 ft3); Nested 11 in (7,816 ft3); Dragon 9 in (7,879 ft3); L-System 10 in (8,091 ft3); DLA 19 in (8,281 ft3); Horton 10 in (9,727 ft3); Trellis 11 in (10,524 ft3). Every trial at or above the answer was dry and every one below it flooded.
- inpWithD0: 308 pattern/depth/diameter combinations equal "move the slider and export", byte for byte.
- Default model (Horton, depth 3): 5,185 bytes, FNV-1a b33bbe9d. D0 12 in: Out1 peak 18.90 cfs, 0.532 MG, J3 and J7 flood 0.058 MG. D0 24 in: 25.95 cfs, 0.589 MG, no flooding. Smallest D0 with no flooding: 15 in (14 in floods 2 nodes).
- .out reader: 6 models run with a 5-s report step; 835 maxima (node depth, link flow, subcatchment runoff) within 0.005 of the .rpt tables.
- Run time, node harness: Koch depth 7, 5,000 nodes, shortest pipe 3.1 ft, average routing step 0.6 s, 236 s.
- Browser, 5,000 nodes (Koch depth 7): completed in 490 s, numerical checks passed; v2.2 stopped it at its fixed 60 s limit.
- Browser (headless Chromium): v2.1, v2.2 and v2.3 check scripts pass on this build with no console errors and no horizontal overflow at 375 px.

Human review: none yet of v2.3. See below.

## What this does not show
1. Not a design. Diameters follow D0 * 1.3^(d-o), not the flow. At depth 7 the Horton trunk is 57.9 in for about 27 cfs (median pipe at 9 % of capacity).
2. One basin (57.52 ac), one storm (0.80 in), uniform subcatchment hydrology. On it the outfall hydrograph does not distinguish most patterns.
3. Every network is a tree (cycle rank 0). No loops, pumps, weirs, storage or offsets.
4. DLA still floods at default settings: order is capped at d, so most pipes are D0 whatever they carry.
5. Deep trees have very short, steep tip pipes (Koch depth 7: 3.1 ft at 65 %). They run, slowly; the Pipe geometry row flags them.
6. Qfull is for the pipe's own slope; pressurized pipes exceed it. Maxima are at 5-min report steps; the .rpt tables (every routing step) can be higher.
7. The D0 search tests flooding only and assumes monotonic response. Pipe volume is not cost.
8. SWMM6 and legacy 5.3 targets are written, never run: the embedded engine is EPA 5.2.4 and runs a classic copy.
9. A project file holds the .inp and .rpt, not the .out series.
10. Not checked by a person: the two v2.3 generator changes and the 0.5 % value; the Build narration for all 22 patterns; the audit card and map coloring beyond screenshots; this file.

## How to reproduce
Sources: app/src/core.js (generator, writer, audit), ui.js, ui22.js, ui23.js; engine eng/swmm524.wasm.
- node test/suite21.js: the 182-model suite.
- node test/audit23.js: the 66-run audit table.
- node test/same-as-v22.js: v2.2 against v2.3 exports.
- node test/d0-check.js: the 308 inpWithD0 comparisons.
- node test/out-verify.js: the 835 .out against .rpt comparisons.
- node test/measure.js, measure22.js, measure23.js, measure23b.js (in that order): every number in the Doc figures and in this file (app/doc/data.json).
- node test/browser21.js, browser22.js, browser23.js: the browser checks.
In the app: Generator tab, Run the exported model, then read Evidence, Results and Hydraulic audit; Find the smallest D0 with no flooding.

## Credits and licenses
- EPA SWMM 5.2.4: U.S. Environmental Protection Agency, public domain. WebAssembly build and WASI shim (browser_wasi_shim) taken unchanged from Robert Dickinson's Lua x SWMM5 Playground.
- OpenSWMM option and virtual-junction rules: openswmm.engine, as recorded in earlier SWMM6-target work on this app. No OpenSWMM code is embedded.
- html2canvas 1.4.1 and gif.js 0.2.0 from cdnjs (walkthrough recording only).
- Outside review of v2.0 by ChatGPT (OpenAI), November 2026, supplied by Robert Dickinson.
- App: Robert (Bob) Dickinson, SWMM Enablement.

## AI use
This version was built with Claude, Anthropic's AI model, in Claude Code sessions in November 2026, under the direction of Robert (Bob) Dickinson. Bob proposed the Build tab after reading the MATLAB post, chose this generator for the first one, set the standing rules it follows (US customary units, a Doc tab, AI disclosure), and commissioned the outside review. Responsibility for the work is his.

What Claude did. It instrumented the generator with the step log; wrote the Build tab, its narration and the Evidence panel; rewrote the export in US customary units; found and fixed the six export defects in v2.0; reproduced and fixed the nine review findings in v2.1; in v2.2 added the inspector, map pan and zoom, the object table, the `.out` reader (adapted from the `.out` script in Bob's testing skill) and the Results card, project save and open, undo, typed values, visible seeds and sweep cancel, and found the missing `[REPORT]` section; in v2.3, asked by Bob for a deep dive, audited all 22 patterns on the engine, chose and made the two generator changes (the 0.5 % slope for same-order pipes and the two Arterial pipe classes), wrote the Hydraulic audit, the map coloring and the smallest-D₀ search, and made the smaller repairs listed above; wired Bob's existing EPA SWMM 5.2.4 WebAssembly engine (taken unchanged from his Lua × SWMM5 Playground) into a Web Worker; wrote the node test suite and the browser checks; drew the figures from measured runs; and wrote this essay and the matching Word document.

The outside review. v2.0 was reviewed by ChatGPT (OpenAI) at Bob's request in November 2026. It graded the app and listed the nine findings in the review section. The findings were checked against this build before being fixed. v2.2 builds the release the review proposed next. Of its version-3 suggestions, v2.3 ran the controlled comparison across patterns as a measurement and built the audit and the D₀ search; a bottleneck challenge and looped networks are not built.

How it was checked. By the mechanical tests above: byte comparison of replay and export on 182 models, the geometry and area checks, 137 engine runs, 835 comparisons of the `.out` reader against the engine's own report, the v2.3 audit and search runs, and headless-browser runs of the finished file. Not yet checked by a person: the two generator changes in v2.3 and the choice of 0.5 % (Claude's, reported to Bob with the lines that changed); the narration text for all 22 patterns (spot-checked by Claude on screenshots, not read line by line); the audit card and map coloring beyond the screenshots Claude looked at; the SWMM6-target files (only classic copies were run); and this essay.

## Changes
- 2.3 (2026-11-12): engine audit of all 22 patterns; same-order pipes fall 0.5 % (Spine, DLA; no more WARNING 04); Arterial two pipe classes; Hydraulic audit card; map coloring by slope, capacity use, depth ratio, velocity; smallest-D0 search; run time limit scales with size, elapsed time and Cancel on the Evidence run; Pipe geometry evidence row; Ctrl+Z after a slider; project files range-checked; D0 4 to 60 in by the inch; saving inside a claude.ai artifact; this .md.
- 2.2 (2026-11-02): inspector; results from the .out; [REPORT] ALL; baseline comparison; project save and open; undo; typed values; visible seed; pan and zoom; object table; sweep cancel.
- 2.1 (2026-11-02): Evidence panel; inlets from the finished graph; exact Voronoi cells on a fixed basin; exact node budgets; honest run status.
- 2.0 (2026-11-02): Build tab and step log; US customary units; six export defects fixed.

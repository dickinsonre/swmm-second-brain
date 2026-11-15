---
title: "S78: Fractal SWMM5/SWMM6 Network Generator, technical summary (app .md, v2.3)"
type: source
raw: raw/apps/fractal-swmm-generator-v2.3.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-15
tags: [apps, generators, swmm5, swmm6, test-models, verification, wasm]
reviewed: no
---
**What it is.** The technical summary carried inside the Fractal SWMM5/SWMM6 Network Generator, version 2.3. Raw file: [raw/apps/fractal-swmm-generator-v2.3.md](../../raw/apps/fractal-swmm-generator-v2.3.md). Extracted byte for byte from Bob's published artifact on 14 November 2026.

**How it was written.** By Claude (Anthropic) in Claude Code sessions in November 2026 under Bob's direction. Bob proposed the Build tab and commissioned an outside review of v2.0 by ChatGPT. Not checked by a person: the two generator changes of v2.3, the narration for the 22 patterns, the SWMM6-target files, and the file itself.

**Claims worth keeping**
- 22 fractal patterns grow tree-shaped networks from the outfall upstream. Length follows L = 300 ft × r_L^(d-o) for the Horton family; diameter D = D0 × 1.3^(d-o); invert z = 100 + 2 o + lift.
- One fixed basin, 1,740 by 1,440 ft = 57.52 ac. Each inlet gets its exact Voronoi cell; width W = 2 sqrt(A).
- One storm: 0.80 in over 2 hours, peak block 0.95 in/hr.
- The Build tab replays the file one logged step at a time; the last frame must equal the exported text byte for byte.
- Engine: EPA SWMM 5.2.4 as a wasm32-wasi reactor (clang 18), taken unchanged from Bob's Lua × SWMM5 Playground. The SWMM6 and legacy 5.3 targets are written and never run.
- Regression suite: 182 generated models, 137 engine runs, 0 failures.
- v2.3 audit of all 22 patterns found flat pipes. Spine at 85 nodes: 11 flat pipes and 11 WARNING 04 in v2.2, 0 in v2.3. DLA at depth 3: 139 flat pipes and 111 flooded nodes in v2.2; 0 flat and 16 flooded in v2.3.
- At 50 nodes, 20 of 22 patterns peak at the outfall between 26.40 and 27.18 cfs at 0.58 h.
- Smallest D0 with no flooding, 50 nodes, by bisection over whole inches: from 7 in (H-Tree) to 19 in (DLA); pipe volume from 2,003 ft³ (Basin) to 10,524 ft³ (Trellis).
- Without a `[REPORT]` section naming ALL, the `.out` holds no series; found in v2.2.
- `.out` reader: 835 maxima within 0.005 of the `.rpt` tables on 6 models run with a 5-second report step.
- Koch at depth 7, 5,000 nodes: shortest pipe 3.1 ft, average routing step 0.6 s, 236 s in Node and 490 s in the browser.

**Limits it states.** "It is not a design tool." Diameters follow the rule, not the flow. One basin and one storm; "the outfall hydrograph does not distinguish most patterns". Every network is a tree with no loops, pumps, weirs, storage or offsets. The D0 search tests flooding only and assumes a monotonic response.

**Checked at ingest.** 1,740 × 1,440 ft = 2,505,600 ft², which is 57.52 ac. The 22 smallest-D0 entries are all present.

**Feeds:** [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

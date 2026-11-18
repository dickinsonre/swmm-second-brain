---
title: Fractal SWMM5/SWMM6 Network Generator (app)
type: entity
updated: 2026-11-17
sources: [S78, S106, S123, S128, S226, S227, S224, S229]
tags: [apps, generators, swmm5, swmm6, test-models]
reviewed: 11/16/2026
changed_after_review: "2026-11-17 (S224 to S242 ingest): a paragraph added near the end, headed Added 17 November 2026 (S226, S227, S224, S229)"
---
Bob's app that grows a tree-shaped drainage network from a fractal rule, shows every step of the build, writes a runnable SWMM `.inp`, runs it in an embedded EPA SWMM 5.2.4 and audits its hydraulics pipe by pipe. Version 2.3, 12 November 2026. "It is a teaching and test-model generator. It is not a design tool" [S78](../sources/S78-fractal-swmm-generator-app-md.md).

**The rules** [S78](../sources/S78-fractal-swmm-generator-app-md.md)

| Item | Rule |
|---|---|
| Patterns | 22, among them Horton, Koch, H-Tree, Spine, DLA, Arterial, Tokunaga |
| Pipe length | L = 300 ft × r_L^(d-o) for the Horton family, d the depth and o the stream order |
| Diameter | D = D0 × 1.3^(d-o), D0 from 4 to 60 in |
| Basin | Fixed, 1,740 by 1,440 ft, 57.52 ac |
| Subcatchments | Each inlet's exact Voronoi cell; width W = 2 sqrt(A); 50 % impervious |
| Storm | 0.80 in in 2 hours, peak block 0.95 in/hr |
| Size limit | 5,000 nodes |

**The Build tab.** Every object carries the index of the log entry that made it, and the tab replays the file one step at a time with the rule and its numbers. The last frame must equal the exported text byte for byte [S78](../sources/S78-fractal-swmm-generator-app-md.md).

**What the engine audit found (v2.3)** [S78](../sources/S78-fractal-swmm-generator-app-md.md)
- Two patterns wrote flat pipes. Spine at 85 nodes had 11 flat pipes and 11 WARNING 04 lines; DLA at depth 3 had 139 flat pipes and 111 flooded nodes. Same-order pipes now fall 0.5 %, and both have 0 flat pipes.
- Arterial wrote pipes as small as 2.9 in, 78 of 119 under 6 in. It now has two pipe classes and a smallest pipe of 8.4 in.
- On the one basin and storm, the outfall hydrograph barely tells the patterns apart: at 50 nodes, 20 of 22 peak between 26.40 and 27.18 cfs.
- A bisection finds the smallest D0 with no flooding: 7 in for H-Tree up to 19 in for DLA at 50 nodes.

**A lesson about the output file.** Without `[REPORT]` lines naming ALL subcatchments, nodes and links, the `.out` holds no series. Version 2.2 found its own exports lacked the section [S78](../sources/S78-fractal-swmm-generator-app-md.md). See [Reading SWMM output](../concepts/reading-swmm-output.md).

**Checks.** 182 generated models and 137 engine runs with 0 failures; replay text equals export text on all 182. Its `.out` reader agrees with the `.rpt` tables on 835 maxima [S78](../sources/S78-fractal-swmm-generator-app-md.md).

**SWMM6.** It writes SWMM6-only lines (DYNAMIC_SLOT, SEMI_IMPLICIT, ANDERSON_ACCEL, `[VIRTUAL_JUNCTIONS]`) to a SWMM6 target file. Those files are written and never run [S78](../sources/S78-fractal-swmm-generator-app-md.md).

**Limits.** Diameters follow the rule, not the flow: at depth 7 the Horton trunk is 57.9 in for about 27 cfs. Every network is a tree, with no loops, pumps, weirs or storage. DLA still floods at default settings. No person has reviewed the two generator changes of v2.3 [S78](../sources/S78-fractal-swmm-generator-app-md.md).

**History.** 2.0 on 2 November 2026 added the Build tab and US customary units and fixed six export defects; 2.1 answered nine findings of an outside review by ChatGPT [S78](../sources/S78-fractal-swmm-generator-app-md.md).

**Added 15 November 2026: a second generator.** A separate Replit app, [SWMM5 Topology Sandbox (app)](swmm5-topology-sandbox.md), also offers 22 network patterns. It exports a SWMM5-format INP file but runs no engine, and its hydrographs are estimates [S106](../sources/S106-swmm5-topology-sandbox-replit-summary.md). Neither summary says how the two generators are related (Q73).

**Added 15 November 2026: a third generator.** [EPANET 2.3 Generator (app)](epanet-23-generator.md) builds synthetic water and drainage networks from a seed and runs them in EPANET and in SWMM 5.1.015 in the browser, with 24 starter models [S128](../sources/S128-epanet-23-generator-replit-summary.md). [SWMM5 Modeler (app)](swmm5-modeler.md) also generates and scales up networks, on EPA SWMM5 5.1.14 [S123](../sources/S123-swmm5-modeler-replit-summary.md). No summary says how any of these generators is related to this one (Q73).

**Added 17 November 2026, second batch.** Later generators of the same kind, each with a no-overlap check: [Hedron Walk (app)](hedron-walk.md) [S226](../sources/S226-hedron-walk-summary.md), [Kleinian SWMM (app)](kleinian-swmm.md) [S227](../sources/S227-kleinian-swmm-summary.md), [Conformal SWMM (app)](conformal-swmm.md) [S224](../sources/S224-conformal-swmm-app-md.md) and [Rule 110 in SWMM5 (app)](rule110-swmm5.md) [S229](../sources/S229-rule110-swmm5-summary.md).

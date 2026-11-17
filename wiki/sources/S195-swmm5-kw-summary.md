---
title: "S195: swmm5-kw, summary written from the page (v1.1)"
type: source
raw: raw/apps/swmm5-kw-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-10
ingested: 2026-11-17
tags: [apps, swmm5, engine, kinematic-wave, steady-flow, graph, byte-for-byte, corpus]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of swmm5-kw version 1.1: EPA SWMM 5.2.4 whose kinematic wave and steady flow routing split a junction among several outlets instead of stopping at ERROR 133, and run directed loops instead of stopping at ERROR 131. The page runs stock 5.2.4 and the extension side by side in WebAssembly. Raw file: [raw/apps/swmm5-kw-v1.1.md](../../raw/apps/swmm5-kw-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary of its own. Claude (Anthropic) wrote this file on 16 November 2026, at Bob's request, from the published artifact (version 1794347262-6e96) and its About and Doc tabs. No model was run. Bob has not read it (Q99). The page says the extension, page, tests and essay were made with Claude under Bob's direction: the engine on 28 and 29 September 2026, the repository, page and essay on 29 October, and version 1.1 on 31 October after an outside review.

**Claims worth keeping** (all copied from the page)
- Repository SWMMBobSWMM6/swmm5-kw: `kwmod.c` plus changes to `flowrout.c`, `toposort.c`, `node.c` and `swmm5.c`, over tag v5.2.4 (commit 7952ca8). No license stated. Dynamic wave is untouched; with both options off it is stock 5.2.4. With either on, its report carries a KW/SF extension block saying the results are not stock.
- HEAD, the default split rule, finds the one junction water level y at which the outlets together carry exactly the inflow: each outlet sees y less its offset, carries the Manning flow at that normal depth, capped at its full-flow capacity. y is found by bisection, 22 to 31 halvings on average. Water beyond the sum of capacities stays in the junction and ponds or floods. CAPACITY shares by full-flow capacity; AREA is named, its formula not given in the sections read. A loop is iterated within each routing step until the returning flow settles.
- split.inp (a 3 ft pipe carrying 20 cfs into a junction with a 3.0 ft and a 1.5 ft outlet, both 400 ft): HEAD sends 73.8 % down the big pipe, dynamic wave 71.3 %, CAPACITY 86.4 %. Dynamic wave drives 5.73 cfs through the 1.5 ft pipe, about 9 % beyond its 5.25 cfs gravity full flow.
- diamond.inp and braid.inp: every peak within 1.8 % of dynamic wave; split.inp within 4.3 %. Steady flow with HEAD: routing continuity 0.000 % on split.inp; kinematic wave 0.131 %, against 0.124 % for stock kinematic wave on a plain three-pipe chain.
- Corpus gate, 1729-SWMM5-Models-2030 at commit 9ee63bd, 3,759 models: 357 KINWAVE or STEADY models run four ways, 352 with a byte-identical .out in all four; 3,239 dynamic-wave models with the extension on, 3,226 identical; interface-file models 159 of 163. The page says not one model differed: 10 decks crash stock and swmm5-kw at the same point, 11 could not be compared because stock never finished. The one model the extension changes is NCIMM_ROUTING/water.inp, which stock refuses with ERROR 131.
- What-if pass, 3,218 dynamic-wave models switched to KINWAVE: stock refused 925 with ERROR 133 or 131, and swmm5-kw ran 234 of those to the end; the other 691 stopped on checks the extension leaves alone. Of the 1,412 stock could run, every one gave identical bytes from swmm5-kw; 874 stopped on an input check in both. Among the 234: median continuity error magnitude 0.17 %, 60 past 1 %.
- Version 1.1 fixes after review: CAPACITY and AREA kept their "outlet is full" flags in `char done[64]`, so an outlet past the 64th was never set aside and the junction flooded; now one flag per outlet. HEAD could hand out up to 1.5e-6 cfs more than arrived; fixed. Checked on junctions of up to 130 outlets.
- Built and gated on Linux (GCC 13, musl 1.2.4) and as WebAssembly (Clang 18, wasi-libc); the wasm engines were checked against native builds.

**Limits it states.** Kinematic wave cannot represent backwater, surcharge or reverse flow, in a split or anywhere. Where a pipe in a loop would run backwards, the answer is wrong in direction. Five small test networks were compared with dynamic wave. Only the 30 largest continuity errors of the what-if pass were traced. No Windows build. No line-by-line review of the C by a person.

**Checked at ingest.** 357 + 3,239 + 163 = 3,759. The 22 models not identical in the gate (5 + 13 + 4) equal 10 crashes + 11 unfinished + 1 changed. 234 + 691 = 925. 3,239 - 3,218 = 21, the 10 + 11 that stock could not finish. 925 + 1,412 + 874 = 3,211, leaving 7 of the 3,218 what-if models unaccounted for (Q101). 5.73 / 5.25 = 1.091.

**Feeds:** [swmm5-kw](../entities/swmm5-kw.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Cycles and trees](../concepts/graph-cycles-and-trees.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [Open questions](../open-questions.md).

---
title: swmm5-kw
type: entity
updated: 2026-11-17
sources: [S195, S227, S229]
tags: [swmm5, engine, kinematic-wave, steady-flow, graph]
reviewed: no
---
One of Bob's variants of [EPA SWMM 5](swmm-5.md): 5.2.4 whose kinematic wave and steady flow routing split a junction among several outlets instead of stopping at ERROR 133, and run directed loops instead of stopping at ERROR 131. Version 1.1, repository SWMMBobSWMM6/swmm5-kw, no license stated; a page runs it beside stock 5.2.4 in WebAssembly [S195](../sources/S195-swmm5-kw-summary.md).

**A caution about its source.** [S195](../sources/S195-swmm5-kw-summary.md) was written by Claude on 16 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q99).

**What it changes** [S195](../sources/S195-swmm5-kw-summary.md)
- `kwmod.c` plus changes to `flowrout.c`, `toposort.c`, `node.c` and `swmm5.c`. Dynamic wave is untouched. With both options off it is stock 5.2.4.
- A split junction shares its outflow by one of three rules. HEAD, the default, finds the one water level at which the outlets, each at Manning normal depth and capped at full flow, carry exactly the inflow. CAPACITY shares by full-flow capacity. AREA is the third. Water beyond the outlets' capacity ponds or floods.
- A loop is iterated within each routing step until the returning flow settles.

**On one split** (a 3 ft pipe carrying 20 cfs into a 3.0 ft and a 1.5 ft outlet) [S195](../sources/S195-swmm5-kw-summary.md)

| Method | Share down the big pipe |
|---|---|
| HEAD | 73.8 % |
| Dynamic wave | 71.3 % |
| CAPACITY | 86.4 % |

Dynamic wave drives 5.73 cfs through the 1.5 ft pipe, about 9 % beyond its full flow by gravity.

**The corpus gate.** 3,759 models of [the corpus](corpus-1729.md). The page says not one model differed from stock except the one the extension exists for, NCIMM_ROUTING/water.inp, which stock refuses with ERROR 131. Switched to KINWAVE, 925 dynamic-wave models stop stock at ERROR 133 or 131; swmm5-kw ran 234 of them to the end [S195](../sources/S195-swmm5-kw-summary.md). See [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).

**What it does not show.** Kinematic wave still has no backwater, surcharge or reverse flow. A loop pipe that would run backwards is wrong in direction. Five small networks were compared with dynamic wave. No person has reviewed the C line by line [S195](../sources/S195-swmm5-kw-summary.md).

**Added 17 November 2026, second batch.** Two apps run the swmm5-kw build: [Kleinian SWMM (app)](kleinian-swmm.md), where the networks are trees so the results are stock 5.2.4's [S227](../sources/S227-kleinian-swmm-summary.md), and [Rule 110 in SWMM5 (app)](rule110-swmm5.md), which runs stock 5.2.4 from the same repository [S229](../sources/S229-rule110-swmm5-summary.md).

**Related.** [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Cycles and trees](../concepts/graph-cycles-and-trees.md), [Wrap, translate or extend](../concepts/wrap-translate-or-extend.md).

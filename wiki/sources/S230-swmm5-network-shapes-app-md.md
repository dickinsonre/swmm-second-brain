---
title: "S230: The Shapes of SWMM5 Networks, app .md (v1.1.0)"
type: source
raw: raw/apps/swmm5-network-shapes-v1.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-17
tags: [apps, swmm5, corpus, graphs, network-shape]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app The Shapes of SWMM5 Networks, version 1.1.0: an app that reduces each SWMM5 .inp to its tree and longest path to the outfall and lays 1,311 network shapes from the 1729 corpus on one outfall, in five views, after Dominic Roye's The Shapes of Rivers. No engine runs. Raw file: [raw/apps/swmm5-network-shapes-v1.1.0.md](../../raw/apps/swmm5-network-shapes-v1.1.0.md).

**How it was written.** The app ships this file. The file says the app was built with Claude (Claude Fable 5.2) in one session on 16 November 2026 under Bob's direction: Bob brought the idea and chose the first two views, and when the first build looked like a river he said it should look like a network. Claude proposed the method and wrote the code and tests. Bob has not reviewed the method, the code or any shape against its model.

**Claims worth keeping** (all copied from the file)
- Built-in set from corpus commit 9ee63bd: 4,540 .inp files, 3,317 measured, 1,311 unique shapes; 865 occur once, the most copied 380 times.
- Median sinuosity 1.356; median links in tree 25; median stem length 5,487 ft; longest stem 65.9 mi; median stem slope 0.172 %; median concavity 0.481 (n = 841).
- An independent Python and SciPy version agrees on tree link count for 3,317 of 3,317 files and on sinuosity for 3,310 of 3,317; the 7 differences are copies of 3 models with nodes exactly equidistant from two outfalls.
- Drawing: 706 shapes to scale, 465 schematic, 140 cannot tell.
- Median sinuosity rises with size: 1.167 under 10 links, 1.336 for 10 to 99, 1.482 for 100 to 999, 1.568 for 1,000 or more.
- Corpus files not measured: 499 have no coordinates, 406 no links, 103 no links that reach an outfall.

**Limits it states.** No flow, capacity or correctness of any model. 465 shapes come from schematic drawings. The tree is nearest outfall by drawn distance, not a flow-directed drainage area. 725 of 1,311 shapes come from the XPSWMM folder, so the corpus is one collection, not a sample of sewer systems; the size trend rests on 98 shapes of 1,000 links or more. Not checked by a person.

**Checked at ingest.** 706 + 465 + 140 = 1,311. 452 + 419 + 331 + 109 = 1,311 shapes across the size table. The `links:` line gives Netlify as "none yet"; Netlify reported a finished deploy at https://swmm5-network-shapes.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [The Shapes of SWMM5 Networks (app)](../entities/swmm5-network-shapes.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [Cycles and trees](../concepts/graph-cycles-and-trees.md), [Walks, paths, connectivity and search](../concepts/graph-paths-and-search.md).

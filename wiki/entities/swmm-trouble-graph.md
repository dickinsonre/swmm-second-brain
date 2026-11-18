---
title: "SWMM Trouble Graph (app)"
type: entity
updated: 2026-11-17
sources: [S205, S215]
tags: [apps, swmm5, rpt, diagnosis, graphs, negative-result]
reviewed: no
---
Bob's app SWMM Trouble Graph: an app that reads a SWMM5 .inp with the .rpt from a run of it, pins each flagged report record to its element, joins records that sit close together and ranks the places where separate tables testify against the same few elements. It runs no engine and does not change the model. Version 1.3, 2026-11-04 [S215](../sources/S215-swmm-trouble-graph-summary.md). Netlify address: https://swmm-trouble-graph.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S215](../sources/S215-swmm-trouble-graph-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S215](../sources/S215-swmm-trouble-graph-summary.md)
- Reader against the corpus: 3,558 .inp and .rpt pairs from the 1729 corpus parsed with no failures; 2,883 reports held summary tables; their 661,218 node and link rows named no element missing from the .inp, and all 469 printed element counts matched.
- Reader against the binary: on 12 models the .out peaks matched names across 1,912 links and 1,951 nodes; median .out to .rpt peak ratio 0.992, because the .out samples at the report step.
- Shuffle calibration: 1,620 draws over 540 models; any neighborhood under 0.05 in 14 draws (0.9 %). On the real reports any neighborhood passed in 39 of 540 models (7.2 %).
- Planted errors: 39 models, one typing error in a quiet conduit more than 3 hops from any flag; 296 runs counted. A hit means the first pick lands within 2 hops; a random element hits 2.0 %.
- Length too short (70 runs): the time-step list's first entry hit 40 %, the graph (Numerics) 23 %. Diameter too small (78 runs): flooding table 26 %, graph (Capacity) 26 %, graph (Numerics) 0 %. Roughness x 10 (78 runs): surcharge table 15 %, graph (All) 8 %. Invert raised (70 runs): every method 0 % to 7 %.
- The page's own reading: the graph did not beat the right single list.
- Engine parity of the seeded runs' engine (swmm-toolkit 0.17.0) with the corpus reports on 64 models: 14,293 of 15,493 peak flows exact, 15,380 within 2 %.

**What it does not show.** A neighborhood is a place to look, not a diagnosis; the tables say where trouble surfaced, and the cause can sit outside it. Nothing has been compared with field data. [S215](../sources/S215-swmm-trouble-graph-summary.md)

**Noted at ingest.** 70 + 78 + 78 + 70 = 296 runs. 14 / 1,620 = 0.86 % and 39 / 540 = 7.2 %. A negative result in the sense of [Negative results](../concepts/negative-results.md): the method the app was built for lost to a list the report already prints.

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Negative results](../concepts/negative-results.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md).

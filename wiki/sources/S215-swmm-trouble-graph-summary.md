---
title: "S215: SWMM Trouble Graph, summary written from the page (v1.3)"
type: source
raw: raw/apps/swmm-trouble-graph-v1.3.md
kind: app-md
author: Robert Dickinson
published: 2026-11-04
ingested: 2026-11-17
tags: [apps, swmm5, rpt, diagnosis, graphs, negative-result]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Trouble Graph, version 1.3: an app that reads a SWMM5 .inp with the .rpt from a run of it, pins each flagged report record to its element, joins records that sit close together and ranks the places where separate tables testify against the same few elements. It runs no engine and does not change the model. Raw file: [raw/apps/swmm-trouble-graph-v1.3.md](../../raw/apps/swmm-trouble-graph-v1.3.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793798092-4bc5, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app and essay were built with Claude in November 2026 under Bob's direction: Bob chose the problem from Ken Phuc Le's post about a knowledge graph on Autodesk Forma data and owns the corpus it was tested on; Claude wrote the readers, the graph analysis, the shuffle test and the seeded-defect test. For 1.1 Bob supplied a review of 1.0 written by an OpenAI model, and two more reviews for 1.2 and 1.3.

**Claims worth keeping** (all copied from the file)
- Reader against the corpus: 3,558 .inp and .rpt pairs from the 1729 corpus parsed with no failures; 2,883 reports held summary tables; their 661,218 node and link rows named no element missing from the .inp, and all 469 printed element counts matched.
- Reader against the binary: on 12 models the .out peaks matched names across 1,912 links and 1,951 nodes; median .out to .rpt peak ratio 0.992, because the .out samples at the report step.
- Shuffle calibration: 1,620 draws over 540 models; any neighborhood under 0.05 in 14 draws (0.9 %). On the real reports any neighborhood passed in 39 of 540 models (7.2 %).
- Planted errors: 39 models, one typing error in a quiet conduit more than 3 hops from any flag; 296 runs counted. A hit means the first pick lands within 2 hops; a random element hits 2.0 %.
- Length too short (70 runs): the time-step list's first entry hit 40 %, the graph (Numerics) 23 %. Diameter too small (78 runs): flooding table 26 %, graph (Capacity) 26 %, graph (Numerics) 0 %. Roughness x 10 (78 runs): surcharge table 15 %, graph (All) 8 %. Invert raised (70 runs): every method 0 % to 7 %.
- The page's own reading: the graph did not beat the right single list.
- Engine parity of the seeded runs' engine (swmm-toolkit 0.17.0) with the corpus reports on 64 models: 14,293 of 15,493 peak flows exact, 15,380 within 2 %.

**Limits it states.** A neighborhood is a place to look, not a diagnosis; the tables say where trouble surfaced, and the cause can sit outside it. Nothing has been compared with field data.

**Checked at ingest.** 70 + 78 + 78 + 70 = 296 runs. 14 / 1,620 = 0.86 % and 39 / 540 = 7.2 %. A negative result in the sense of [Negative results](../concepts/negative-results.md): the method the app was built for lost to a list the report already prints. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm-trouble-graph.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM Trouble Graph (app)](../entities/swmm-trouble-graph.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Negative results](../concepts/negative-results.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [Graphs: nodes, edges, direction and weight](../concepts/graph-basics.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

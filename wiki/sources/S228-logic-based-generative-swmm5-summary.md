---
title: "S228: Logic-Based Generative SWMM5, summary written from the page (v2.0.0)"
type: source
raw: raw/apps/logic-based-generative-swmm5-v2.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-30
ingested: 2026-11-17
tags: [apps, swmm5, generators, design-rules, ai, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Logic-Based Generative SWMM5, version 2.0.0: a storm sewer for a synthetic site designed three ways (Pattern, a regression trained on 40 logic designs; Hybrid, the same samples repaired rule by rule; Logic, forward-chained through the rules), each checked against fifteen rules and run in EPA SWMM 5.2.4 in the page. Raw file: [raw/apps/logic-based-generative-swmm5-v2.0.0.md](../../raw/apps/logic-based-generative-swmm5-v2.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793379005-2cc9, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says this version was built with Claude (Claude Opus 5.5) in October 2026 under Bob's direction: Bob asked how logic-based generative AI, which layers explicit rules on a statistical model, would work for SWMM5, supplied the concept text and asked for the rebuild; Claude designed the app and wrote all the code.

**Claims worth keeping** (all copied from the file)
- On seed 7 the Pattern design breaks rules in 22 of 24 pipes; the Hybrid repairs them all but digs the most trench; the Logic design is the leanest legal one.
- Rules include a minimum pipe size, 2 ft/s full-flow velocity, 3 ft of cover, and never a smaller pipe below a larger one. The checker shares only physics functions with the generators.
- Fifteen planted faults, one per rule, were caught 15 of 15; the unmodified design has 0 findings.
- Over 300 random sites and 7,691 pipes the logic generator broke rules on 102 pipe-rule pairs (38 capacity, 60 depth, 4 scour) and flagged all as conflicts; the hybrid flagged 96 with 0 unflagged; overlapping subcatchments 0 on all 300 sites.
- On all three default designs the WebAssembly .out matched a native gcc build byte for byte (275,760 bytes each).
- Outfall peak 219.30 cfs at the one-minute report step against the .rpt's routing-step maximum of 219.66 cfs.

**Limits it states.** Synthetic sites and storms; no real catchment. The rule set is the page's own, and passing it is not a design review.

**Checked at ingest.** 38 + 60 + 4 = 102. The .out peak under the .rpt peak is the report-step sampling described on [Reading SWMM output](../concepts/reading-swmm-output.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://logic-based-generative-swmm5.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Logic-Based Generative SWMM5 (app)](../entities/logic-based-generative-swmm5.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

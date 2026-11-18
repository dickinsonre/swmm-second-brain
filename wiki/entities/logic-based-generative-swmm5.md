---
title: "Logic-Based Generative SWMM5 (app)"
type: entity
updated: 2026-11-17
sources: [S205, S228]
tags: [apps, swmm5, generators, design-rules, ai, wasm]
reviewed: no
---
Bob's app Logic-Based Generative SWMM5: a storm sewer for a synthetic site designed three ways (Pattern, a regression trained on 40 logic designs; Hybrid, the same samples repaired rule by rule; Logic, forward-chained through the rules), each checked against fifteen rules and run in EPA SWMM 5.2.4 in the page. Version 2.0.0, 2026-10-30 [S228](../sources/S228-logic-based-generative-swmm5-summary.md). Netlify address: https://logic-based-generative-swmm5.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S228](../sources/S228-logic-based-generative-swmm5-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S228](../sources/S228-logic-based-generative-swmm5-summary.md)
- On seed 7 the Pattern design breaks rules in 22 of 24 pipes; the Hybrid repairs them all but digs the most trench; the Logic design is the leanest legal one.
- Rules include a minimum pipe size, 2 ft/s full-flow velocity, 3 ft of cover, and never a smaller pipe below a larger one. The checker shares only physics functions with the generators.
- Fifteen planted faults, one per rule, were caught 15 of 15; the unmodified design has 0 findings.
- Over 300 random sites and 7,691 pipes the logic generator broke rules on 102 pipe-rule pairs (38 capacity, 60 depth, 4 scour) and flagged all as conflicts; the hybrid flagged 96 with 0 unflagged; overlapping subcatchments 0 on all 300 sites.
- On all three default designs the WebAssembly .out matched a native gcc build byte for byte (275,760 bytes each).
- Outfall peak 219.30 cfs at the one-minute report step against the .rpt's routing-step maximum of 219.66 cfs.

**What it does not show.** Synthetic sites and storms; no real catchment. The rule set is the page's own, and passing it is not a design review. [S228](../sources/S228-logic-based-generative-swmm5-summary.md)

**Noted at ingest.** 38 + 60 + 4 = 102. The .out peak under the .rpt peak is the report-step sampling described on [Reading SWMM output](../concepts/reading-swmm-output.md).

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

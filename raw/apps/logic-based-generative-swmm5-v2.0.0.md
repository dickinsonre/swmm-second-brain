---
name: Logic-Based Generative SWMM5
file: logic-based-generative-swmm5.html
version: 2.0.0
date: 2026-10-30
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/CqTAn88QGgFDJoYa9ZmhVm", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4, compiled to wasm32-wasi with zig 0.13.0 cc, 535,080 bytes, SHA-256 beginning ff21e656634998c2; two portability patches in swmm5.c (mkstemp, realpath)", license: public domain}
units: US customary (ft, cfs, in)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Claude Opus 5.5) under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/CqTAn88QGgFDJoYa9ZmhVm, version 1793379005-2cc9 (index.html, 3,334,756 bytes, SHA-256 8aaf0b4dc45b98ccb2056967b6bd385af1bcb54560a014563e275a100e993ea5), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# Logic-Based Generative SWMM5: rules decide, a pattern model proposes, EPA SWMM 5.2.4 checks the result

## In three points
- **What:** Designs a storm sewer for a synthetic site three ways (Pattern, a regression trained on 40 logic designs; Hybrid, the same samples repaired rule by rule; Logic, forward-chained through the rules), checks each against fifteen rules, and runs each in EPA SWMM 5.2.4 in the page.
- **So what:** On one seed the Pattern design breaks rules in 22 of 24 pipes, the Hybrid repairs them all but digs the most trench, and the Logic design is the leanest legal one; the checker caught 15 of 15 planted faults.
- **Now what:** Put explicit design rules over any generated network before you trust it. The site and storm are synthetic, and passing the rules is not a design review.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Version 2.0.0, 2026-10-30"). The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

The question: how would logic-based generative AI, which layers explicit rules on a statistical model, work for SWMM5? Version 1 answered with two diagrams; version 2 builds a synthetic site (a grid of blocks with land use, a rolling ground surface and an outfall; one subcatchment per block, polygons tiling the site exactly), designs the sewer three ways, checks every design with a checker that shares only physics functions with the generators, and writes and runs an .inp with an alternating-block storm from one IDF curve. Rules include minimum pipe size, 2 ft/s full-flow velocity, 3 ft of cover, and never a smaller pipe below a larger one. Tabs: Design, Rules, Trace, Spectrum, Engine, Export, About, Doc.

## Checks (as stated on the page)

- Pattern generator: a regression trained on 40 logic designs. On seed 7 the Pattern design breaks rules in 22 of 24 pipes; the Hybrid repairs them all but digs the most trench; the Logic design is the leanest legal one.
- Engine: on all three default designs the WebAssembly .out matched a native gcc build of the same source byte for byte (275,760 bytes each); the .rpt files matched line for line apart from the clock.
- .out reader: outfall peak 219.30 cfs at the one-minute report step, just under the .rpt's routing-step maximum of 219.66 cfs.
- Checker: fifteen planted faults, one per rule, caught 15 of 15; the unmodified design has 0 findings.
- Generators over 300 random sites and 7,691 pipes: the logic generator broke rules on 102 pipe-rule pairs (38 capacity, 60 depth, 4 scour) and flagged all as conflicts; the hybrid flagged 96, 0 unflagged; overlapping subcatchments 0 on all 300 sites.
- Every number in the essay comes from one scripted run (verify.js) of the code the app carries.

## What this does not show

- Synthetic sites and storms; no real catchment.
- The rule set is the page's; passing it is not a design review.

## How to reproduce

Open the page, set the site on Design, and compare the three designs; Engine runs them; Export writes the .inp.

## Credits and licenses

EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The page says this version was built with Claude (Anthropic's AI model, Claude Opus 5.5) in October 2026, under the direction of Robert (Bob) Dickinson, who posed the question, supplied the concept text, asked for the rebuild and set the standing requirements (Doc tab, .docx, US units, non-overlapping subcatchments, dark default). Claude designed the app and wrote all of the code. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2.0.0 (2026-10-30): three generators, an independent checker and a real engine.
- 1.x: two diagrams.

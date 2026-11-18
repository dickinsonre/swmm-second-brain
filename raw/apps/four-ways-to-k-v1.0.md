---
name: Four Ways to K
file: four-ways-to-k.html
version: "1.0"
date: 2026-10-29
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/N5P39vtARDDKp5z5Q4Djw2", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4, commit 7952ca8; Emscripten 3.1.51, -O2, single file, from Seven SWMM Engines 1.2 unchanged", script_sha256: 4602e507bb5c372c5b80952e585eb13f61137251b87fdddf2ff56f2d2eb8a45f, native_check: "swmm-toolkit 0.17.0", license: public domain}
units: US customary (ft, cfs, ft/s)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Claude Opus 5.5) at Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/N5P39vtARDDKp5z5Q4Djw2, version 1793323393-f15c (index.html, 1,708,032 bytes, SHA-256 9087533c8b3f616dab98c613c8931ceb17cbd1fc0074cb624ede5f153469afb3), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# Four Ways to K: minor losses in EPA SWMM 5.2.4, one engine, five versions of one manhole

## In three points
- **What:** Runs four ways of putting a manhole loss into SWMM5 ([LOSSES], an equivalent Manning n, a side orifice, and a HEC-22 calculation) plus a no-loss control on one two-pipe test line, with EPA SWMM 5.2.4 doing every calculation in the page.
- **So what:** With the pipes full, [LOSSES], equivalent n and the orifice each raise J1 by 0.944 ft, matching the hand value 1.5 x 0.629; but at 2 cfs equivalent n charges 1.94 times too much loss, and the orifice parks the whole loss at the manhole.
- **Now what:** Use [LOSSES] or an orifice when the loss must hold at all depths, and read surcharge at the manhole knowing the method moves it. One test line, no field data.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-29"). The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

Bob asked whether SWMM5's fixed link losses could be done any other way. Test line: J1 (invert 100.0 ft) to C1, 300 ft, to J2 (98.5 ft) to C2, 300 ft, to OF1 (97.0 ft); both 24 in circular, n 0.013, slope 0.005; dynamic wave at a 2 s step, EXTRAN surcharge, partial inertial damping, normal-flow limitation BOTH, 1 minute reports. The orifice method adds node J2b and a 24 in side orifice. Four flow cases: surcharged at 20 cfs, half full at 8 cfs, shallow at 2 cfs, and a 0 to 25 to 0 cfs storm. The HEC-22 sheet reads the outlet pipe's state from the no-loss run and writes the fifth model. Tabs: Compare, HEC-22 sheet, Findings, Verify, About, Doc.

## Results the page reports

- 20 cfs surcharged: [LOSSES], equivalent n and the orifice each raise J1 by 0.944 ft; hand value 1.5 x 0.629 = 0.944. At the storm peak 1.478, 1.450 and 1.468 ft.
- Where the head goes: under [LOSSES] and equivalent n the manhole rises 0.315 ft; under the orifice 0.944 ft. HEC-22's straight-through manhole costs 40 percent as much.
- Part full: equivalent n was tuned to the full-pipe hydraulic radius; at 2 cfs (water at 0.24 of the diameter) the formula predicts 2.15 times too much loss and the engine gave 1.94 times; it is right at half full and undercharges a nearly full pipe by about a fifth.

## Checks (as stated on the page)

- The WebAssembly engine is Bob's existing EPA 5.2.4 build from Seven SWMM Engines 1.2, checked against swmm-toolkit 0.17.0 natively; results read by the SWMM Results Kit 1.0.0.
- The Verify tab reruns the page's checks.

## What this does not show

- One test line and four flow cases; no field data.

## How to reproduce

Open the page; Compare runs the five models per case; Export writes them.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); HEC-22 for the manhole method; Bore Shell 1.0.0; SWMM Results Kit 1.0.0. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model (Claude Opus 5.5), in a Claude session on 29 October 2026, at the direction of Robert (Bob) Dickinson, who asked the question and asked for the comparison to be engine-verified in one of his WebAssembly 5.2.4 apps. Claude read the 5.2.4 loss code, designed the test line and cases, and wrote the model builder, the HEC-22 implementation, the run and check harnesses, the page, its figures and the essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-10-29): first version.

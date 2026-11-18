---
name: Non-Prismatic Channel Lab
file: non-prismatic-channel-lab.html
version: "1.0"
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/LTCAP2wuh4sbw6Ffed8ks3", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA tag v5.2.4, commit 7952ca8 (2023-10-10); Emscripten 3.1.51, -O2, single file, from Seven SWMM Engines 1.2", script_sha256: 4602e507bb5c372c5b80952e585eb13f61137251b87fdddf2ff56f2d2eb8a45f, license: public domain}
units: US customary (ft, cfs)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session at Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/LTCAP2wuh4sbw6Ffed8ks3, version 1793628863-2301 (index.html, 2,145,604 bytes, SHA-256 282c62e7a6ea44248b72f5c6ec555ef8f5b01588d2d4617183e4dfb497a24c22), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# Non-Prismatic Channel Lab: what it costs to cut a non-prismatic channel into prismatic SWMM links

## In three points
- **What:** A 2,000 ft channel whose width you shape, solved by EPA SWMM 5.2.4 in the browser on an .inp the page writes and by a standard-step energy solution of the same channel; the gap between the two water surfaces is the cost of prismatic links.
- **So what:** At an abrupt constriction with no losses SWMM shows 44% of the energy method's 0.640 ft rise; converted [LOSSES] bring it to 92%; and a tapered channel under NORMAL_FLOW_LIMITED BOTH oscillates between 359.53 and 570.70 cfs on two engine copies alike.
- **Now what:** Model contractions and expansions with entrance and exit losses rather than prismatic steps alone, and watch the normal-flow limiter in tapers and widenings. Five test channels, no field data.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0 · EPA SWMM 5.2.4"); the date is the artifact's. Every number below is copied from the page. No model was run to write this file.

## What it does

Bob asked for it after a discussion of modeling a rock ramp in SWMM and ICM. You shape the width of a 2,000 ft channel, the page writes the .inp, the engine runs it in a Web Worker (a fresh module per run, files in memory), and the SWMM Results Kit 1.0.0 reads the .out and .rpt. Tabs: Lab, Sweep, Engine, Families, About, Doc.

## Results the page reports (build-time runs, FROUDE)

| Case | SWMM rise ft | Energy rise ft | Share | Throat error ft | Continuity % |
|---|---|---|---|---|---|
| Abrupt, no losses | 0.279 | 0.640 | 44% | 0.307 | -0.156 |
| Abrupt, converted [LOSSES] | 0.586 | 0.640 | 92% | 0.551 | -0.156 |
| Tapers, 50 ft links | 0.418 | 0.543 | 77% | 0.282 | 0.046 |
| Tapers, 10 ft links | 0.422 | 0.543 | 78% | 0.284 | 0.046 |

Rise is the water surface at x = 0 minus the energy method's surface for the same channel with no constriction; share is SWMM rise over energy-method rise with HEC coefficients.

## Checks (as stated on the page)

- Five test channels run on this engine (in Node) and on swmm-toolkit 0.17.0 / PySWMM 2.2.0: largest head difference at any node 0.00001 ft.
- The tapered channel under NORMAL_FLOW_LIMITED BOTH oscillates on both copies, 359.53 to 570.70 cfs at 10 s reports, identical to the hundredth.
- The energy method matches an independent Python standard-step solution of all five channels to 0.0000 ft.
- The page's .inp reproduces the hand-built decks' heads to 0.00001 ft; its converted K equals the decks' 0.45 and 0.60.
- Null test: the prismatic control agrees with the energy method within 0.004 ft along the reach.
- The engine script's SHA-256 is checked in the browser.

## What this does not show

- Field data: these are five test channels.
- ICM is discussed in the Doc but not run.

## How to reproduce

Open the page, shape the channel on Lab, and run; Sweep varies one setting; Export writes the .inp.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); the build from Seven SWMM Engines 1.2; SWMM Results Kit 1.0.0; HEC contraction and expansion coefficients. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude Code session in November 2026, at the direction of Robert (Bob) Dickinson, who asked for it after a discussion of modeling a rock ramp in SWMM and ICM. Claude read the EPA SWMM 5.2.4 source, designed and ran the test channels, found the normal-flow-limiter oscillation in tapers and widenings, and wrote the page (energy solver, .inp writer, charts, sweep) and the essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.

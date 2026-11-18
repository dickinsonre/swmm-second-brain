---
name: Selective Fidelity
file: selective-fidelity.html
version: "1.0"
date: 2026-10-21
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/2Z3EBUX1Cz8HFF5UU66ngT", repo: none named in the page}
engines:
  - {name: EPA SWMM 5.2.4 + fidelity.c 1.0, source: "tag v5.2.4, commit 7952ca837988; fidelity.c (714 lines), fidelity.h, 17 changed lines in dynwave.c; clang 18.1.3 wasm32-wasi -O2 -ffp-contract=off", wasm_sha256: 3b894cbb21b623ab5281aedd0295b3ebdb21cdcf790d5b1b6f3bd7ae0d4f337f, license: "public domain base"}
units: US customary (ft)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Claude Opus 5.5) under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/2Z3EBUX1Cz8HFF5UU66ngT, version 1792592258-d322 (index.html, 1,486,201 bytes, SHA-256 8aa442adc7cad70c7cd764c8bbf6ea044a2c24ac817fd0748ca1f104c9f2bcba), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# Selective Fidelity: detail where the question is, in EPA SWMM 5.2.4 dynamic wave

## In three points
- **What:** A patch to EPA SWMM 5.2.4 dynamic wave (fidelity.c) that solves every step only the conduits the current question depends on, coarsens the rest, promotes any that start to matter, and logs every simplification; it runs in the browser.
- **So what:** On the Two Valleys demo, targeting node E5, the patched engine took 2,894 steps against stock's 12,018 (4.15 times fewer) and conduit solves fell 4.43 times, while the E5 peak depth stayed 1.537 ft and the worst report period differed by 0.012 ft.
- **Now what:** Try it on a model where one short steep conduit sets the step for everything. Results outside the zone are approximate by design, and only three small networks and DYNWAVE were tested.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0 · SWMM 5.2.4 + fidelity.c 1.0"); the date is the build's (2026-10-21). The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

The idea came from an October 2026 post on X about whole-cell biology simulations made faster by full detail only where the question needs it; the post names no scientist or paper and its 200 times speed claim is unverified. In the Two Valleys demo (24 conduits, eight hours, a two-hour storm), conduit W5-W5A, 18 ft long and steep, averages a 2.59 s step and was the critical element in 99.99% of 12,018 steps; the other 23 could have averaged 25.3 to 30 s. Promotion triggers: either end more than 0.8 full, either end's head moving 0.25 ft since its last solve, or flow reversing; demotion only after ten minutes with no trigger. Tabs: Bench, Census, Noise floor, Ensemble, SWMM6, Verify, About, Doc.

## Results the page reports

- Target E5, everything upstream counted, default rules: 12,018 steps stock, 2,894 selective (4.15 times fewer); conduit solves 576,963 to 130,252 (4.43 times fewer); native run time 127 to 128 ms stock against 37 to 41 ms on one Linux machine.
- E5 peak depth 1.537 ft both ways; worst report period 0.012 ft apart; flow-routing continuity from -0.135% to -0.163%.

## Checks (as stated on the page)

- Byte comparison of .out files against unpatched 5.2.4 on 72 runnable regression models.
- Byte comparison of the WebAssembly engine against native builds.
- The stock engine rerun under four conditions as a noise floor.
- The checks are mechanical.

## What this does not show

- No field data; three built-in networks, all small; one machine per timing; DYNWAVE only.
- Results outside the zone are approximate by design.

## How to reproduce

Open the page, pick a target on Bench and run both engines; Census shows which conduit sets the step.

## Credits and licenses

EPA SWMM 5.2.4 (public domain) with the fidelity patch; @bjorn3/browser_wasi_shim 0.4.2. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model (Claude Opus 5.5), in a Claude session on 21 October 2026, under the direction of Robert (Bob) Dickinson, who asked whether the selective-fidelity idea applied to SWMM5 and SWMM6 and asked for the app. Claude read the EPA SWMM 5.2.4 source, designed and wrote the fidelity patch, built the native and WebAssembly engines, generated the Two Valleys demo network, ran every measurement, and wrote the page, its tests, the essay and the .docx. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-10-21): first version.

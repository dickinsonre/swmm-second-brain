---
title: "Selective Fidelity (app)"
type: entity
updated: 2026-11-17
sources: [S205, S265]
tags: [apps, swmm5, dynamic-wave, time-step, speed, wasm]
reviewed: no
---
Bob's app Selective Fidelity: a patch to EPA SWMM 5.2.4 dynamic wave (fidelity.c, 714 lines, with 17 changed lines in dynwave.c) that solves every step only the conduits the current question depends on, coarsens the rest, promotes any that start to matter and logs every simplification; it runs in the browser. The idea came from an October 2026 post on X about whole-cell biology simulations, which names no scientist or paper and whose 200 times speed claim is unverified. Version 1.0, 2026-10-21 [S265](../sources/S265-selective-fidelity-summary.md). Netlify address: https://selective-fidelity.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S265](../sources/S265-selective-fidelity-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S265](../sources/S265-selective-fidelity-summary.md)
- In the Two Valleys demo (24 conduits, eight hours, a two-hour storm), conduit W5-W5A, 18 ft long and steep, averages a 2.59 s step and was the critical element in 99.99 % of 12,018 steps; the other 23 could have averaged 25.3 to 30 s.
- Targeting node E5: 12,018 steps stock against 2,894 selective (4.15 times fewer); conduit solves 576,963 to 130,252 (4.43 times fewer); native run time 127 to 128 ms stock against 37 to 41 ms on one Linux machine.
- E5 peak depth 1.537 ft both ways; the worst report period 0.012 ft apart; flow-routing continuity from -0.135 % to -0.163 %.
- Promotion triggers: either end more than 0.8 full, either end's head moving 0.25 ft since its last solve, or flow reversing; demotion only after ten minutes with no trigger.
- Checks: .out byte comparison against unpatched 5.2.4 on 72 runnable regression models; the WebAssembly engine against native builds; the stock engine rerun under four conditions as a noise floor.

**What it does not show.** No field data; three small built-in networks; one machine per timing; DYNWAVE only. Results outside the zone are approximate by design. [S265](../sources/S265-selective-fidelity-summary.md)

**Noted at ingest.** 12,018 / 2,894 = 4.15 and 576,963 / 130,252 = 4.43. The summary does not say what the byte comparison on 72 models found, only that it was made.

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Engine speed, 1988 to 2024](../concepts/engine-speed-1988-2024.md).

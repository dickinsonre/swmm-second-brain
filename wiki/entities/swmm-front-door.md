---
title: "SWMM Front Door (sketch)"
type: entity
updated: 2026-11-18
sources: [S307]
tags: [designs, swmm5, swmm6, icm, one-swmm]
reviewed: no
---
Bob's design sketch SWMM Front Door: one page that asks what you want to do with a SWMM model. Version 0.1, 2026-11-09 [S307](../sources/S307-swmm-front-door-summary.md). Its `links:` line names no live Netlify address [S307](../sources/S307-swmm-front-door-summary.md).

**A caution about its source.** The page ships no technical summary. [S307](../sources/S307-swmm-front-door-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S307](../sources/S307-swmm-front-door-summary.md)
- A clickable sketch, labelled "v0.1 sketch", of a front door for One SWMM: "Run, compare, check and explain SWMM5, SWMM6 and ICM results in one place." It asks "What do you want to do?" and offers four doors (Run my model, Compare engines, Is it stable?, Explain this number), each answered for EPA's Example1.inp, with a Simple or Expert switch that opens drawers naming the tool call behind each answer.
- The compare door shows what the full app should do when engines disagree. On Example 1, SWMM6 alpha.4 dynamic wave agrees with SWMM 5.2.4 (peak flow in C11 73.76 against 73.90 cfs, 0.19% apart), while SWMM6 alpha.4 finite volume does not (deepest water at J1 0.24 ft against 0.72 ft), so the sketch shows no green check. ICM results come in as an imported CSV, labelled "imported".

**How to use it, as the summary puts it.** Use it to judge the layout and the wording before the app is built. It is a design: the Open .inp and Import buttons do nothing, the theme, help, GIF and Export buttons are drawn but not wired, and every number is fixed text copied from Seven SWMM Engines runs of EPA Example 1 on 28 October 2026. [S307](../sources/S307-swmm-front-door-summary.md)

**What it does not show.** As the design states: engines agreeing is not the same as either being right; ICM is never run, only read. It is a sketch: no file is opened and no engine runs. [S307](../sources/S307-swmm-front-door-summary.md)

**Noted at ingest.** A Claude Design artifact, converted to a standalone page for Netlify with a small script standing in for the design tool's runtime; its numbers are fixed text.

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [One SWMM (app)](one-swmm.md), [Seven SWMM Engines (app)](seven-swmm-engines.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).

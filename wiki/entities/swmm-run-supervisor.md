---
title: "SWMM Run Supervisor (app)"
type: entity
updated: 2026-11-17
sources: [S205, S217]
tags: [apps, swmm5, hot-start, solvers, ai-agents, wasm]
reviewed: no
---
Bob's app SWMM Run Supervisor: EPA SWMM 5.2.4 in WebAssembly cut into 15-minute windows joined by hot-start files; after each window a supervisor (Claude, rules, a fixed preset or a replay) picks how hard the solver works in the next, and every run is scored against an all-careful dynamic-wave run. Version and date 2026-10-24 [S217](../sources/S217-swmm-run-supervisor-summary.md). Netlify address: https://swmm-run-supervisor.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S217](../sources/S217-swmm-run-supervisor-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S217](../sources/S217-swmm-run-supervisor-summary.md)
- Restart floor, all 96 windows at the careful preset against the unbroken careful run: node depth series differ by 0.045 ft rms; 158 of 164 node peaks within 0.1 ft, worst 0.51 ft at node 136; flooding +0.86 %.
- Two hot-start seams were found and fixed; one missing flag made the first runoff step after a restart a dry step, giving 1 % too much runoff.
- As shipped: continuity 0.829 %, 9,974 routing steps (11.5 % of a fixed 1 s step); 143 of 164 peak depths within 0.1 ft of the careful run; worst at JCT-138.
- The careful reference's own force-main peak moves 4.7 ft between a 1 s and a 0.9 s step.
- SWMM 5.2.4 options are global, so Claude's per-element watch list is recorded, not applied.
- Engine: an Emscripten 3.1.51 build from dickinsonre/BatchSWMMRunner, hash-checked in the page.

**What it does not show.** It does not show that Claude beats the rules: the rules were written with hindsight on this storm, no live Claude run is quoted, and a stand-in planner proves only that the path works. It does not show the careful run is right. Wall time includes 96 engine restarts, so the scoreboard counts routing steps. On Netlify or any ordinary host Claude mode is unavailable. [S217](../sources/S217-swmm-run-supervisor-summary.md)

**Noted at ingest.** 96 windows of 15 minutes is 24 hours; 9,974 steps against 86,400 at 1 s is 11.5 %. A 0.045 ft rms floor from restarts alone is a measured cost of the state a hot start keeps, the subject of [Hot start: what a restart loses](../concepts/hot-start-restart-state.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Hot start: what a restart loses](../concepts/hot-start-restart-state.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [BatchSWMM56 (app)](batchswmm56.md).

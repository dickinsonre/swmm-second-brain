---
title: "S217: SWMM Run Supervisor, summary written from the page (v2026-10-24)"
type: source
raw: raw/apps/swmm-run-supervisor-v2026-10-24.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-17
tags: [apps, swmm5, hot-start, solvers, ai-agents, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Run Supervisor, version 2026-10-24: EPA SWMM 5.2.4 in WebAssembly cut into 15-minute windows joined by hot-start files; after each window a supervisor (Claude, rules, a fixed preset or a replay) picks how hard the solver works in the next, and every run is scored against an all-careful dynamic-wave run. Raw file: [raw/apps/swmm-run-supervisor-v2026-10-24.md](../../raw/apps/swmm-run-supervisor-v2026-10-24.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792821210-3e6e, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says Claude wrote all of the app's code and text for Bob, found the two hot-start seams and measured every number quoted; Bob set the goal and the standards. Inside the app Claude is a live participant only in Claude mode, asked only when a person presses the button, and never sees the reference or edits the model.

**Claims worth keeping** (all copied from the file)
- Restart floor, all 96 windows at the careful preset against the unbroken careful run: node depth series differ by 0.045 ft rms; 158 of 164 node peaks within 0.1 ft, worst 0.51 ft at node 136; flooding +0.86 %.
- Two hot-start seams were found and fixed; one missing flag made the first runoff step after a restart a dry step, giving 1 % too much runoff.
- As shipped: continuity 0.829 %, 9,974 routing steps (11.5 % of a fixed 1 s step); 143 of 164 peak depths within 0.1 ft of the careful run; worst at JCT-138.
- The careful reference's own force-main peak moves 4.7 ft between a 1 s and a 0.9 s step.
- SWMM 5.2.4 options are global, so Claude's per-element watch list is recorded, not applied.
- Engine: an Emscripten 3.1.51 build from dickinsonre/BatchSWMMRunner, hash-checked in the page.

**Limits it states.** It does not show that Claude beats the rules: the rules were written with hindsight on this storm, no live Claude run is quoted, and a stand-in planner proves only that the path works. It does not show the careful run is right. Wall time includes 96 engine restarts, so the scoreboard counts routing steps. On Netlify or any ordinary host Claude mode is unavailable.

**Checked at ingest.** 96 windows of 15 minutes is 24 hours; 9,974 steps against 86,400 at 1 s is 11.5 %. A 0.045 ft rms floor from restarts alone is a measured cost of the state a hot start keeps, the subject of [Hot start: what a restart loses](../concepts/hot-start-restart-state.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm-run-supervisor.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM Run Supervisor (app)](../entities/swmm-run-supervisor.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Hot start: what a restart loses](../concepts/hot-start-restart-state.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [BatchSWMM56 (app)](../entities/batchswmm56.md).

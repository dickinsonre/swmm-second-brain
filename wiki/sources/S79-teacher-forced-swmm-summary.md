---
title: "S79: Teacher-Forced SWMM, summary written from the page (v1.0)"
type: source
raw: raw/apps/teacher-forced-swmm-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-15
tags: [apps, swmm5, hot-start, dynamic-wave, engine-comparison, verification, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-15
---
**What it is.** A technical summary of the app Teacher-Forced SWMM, version 1.0 (25 October 2026), which compares two versions of the EPA SWMM 5.2.4 engine by restarting one from the other's exact state. Raw file: [raw/apps/teacher-forced-swmm-v1.0.md](../../raw/apps/teacher-forced-swmm-v1.0.md).

**How it was written. This one is different.** The page carries no summary of its own. Claude (Anthropic, model claude-fable-5-2) wrote the file on 14 November 2026, at Bob's request, from the published page's source, its build record and its Doc essay. No engine was run and nothing was rerun. Bob has not read it (Q52). The app itself was built with Claude Opus 5.5 in one session on 25 October 2026 under Bob's direction; the page says no person has reviewed the slot variant code against EPA issue 231, rerun the experiments, or checked the interpretation of the eleven cases.

**Claims worth keeping** (all copied from the page)
- Three differences per element and window, each scaled by the element's peak: L, teacher-forced (B forced minus A restarted); R, the restart null control; G, free-run. Default window 5 minutes.
- The stock hot start fails the null control. On the slot versions of EXTRAN examples 1, 4 and 7: 0 of 94 restarts exact in each, with worst flow changes of 1.457588, 1.725739 and 5.0 cfs.
- Five pieces of solver state do not survive a stock restart: R-1 `hotstart.c:234-236` (routing state written as 32-bit floats); R-2 `flowrout.c:496` with `dwflow.c:287`; R-3 `dynwave.c:674` with `node.c:303`; R-4 `dynwave.c:140` with `dynwave.c:728`; R-5 `dynwave.c:209-212`.
- With a double-precision sidecar file the restart is bit-exact on 282 of 282 restarts across three models, against 0 of 282 for stock.
- D-1, called a defect: `project.c:165` floors the total duration to whole seconds. A run from midnight to 00:50 gets 2999 seconds and its hot start is written one second early.
- With every switch off the engine's `.out` is byte-identical to stock 5.2.4 on eight EXTRAN test models. wasm equals native on 15 of 15 runs.
- EXTRAN to SLOT on example 1, conduit 8060: forced difference 80 % of peak against 79 % free-run at 0.58 hours.
- Inertial damping FULL: exposure ratio 0.45 on example 1 and 0.58 on EPA Example 2, with 47 to 59 % of active element-windows compensated.
- Head tolerance tightened tenfold: the free-run difference is 2.5 times the teacher-forced total for flow and 3.3 times for depth.
- The slot variants 1, 2 and 4 were written from the descriptions in EPA issue 231, not from a patch file.

**Limits it states.** No observed data; the method says nothing about which engine is right. The teacher-forced number depends on the window. Subcatchments are not bit-exact: on user2 the precise restart is off by up to 0.007 percent of an element's peak, source not traced. Eleven model-and-change pairs on small test networks.

**Checked at ingest.** Every number in the file was searched for in the page source when it was written. The build record gives the engine's size (843,845 bytes) and hash but not its compiler.

**Feeds:** [Teacher-Forced SWMM (app)](../entities/teacher-forced-swmm.md), [Hot start: what a restart loses](../concepts/hot-start-restart-state.md), [Run duration floored to whole seconds](../concepts/run-duration-floor.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

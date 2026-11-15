---
title: Teacher-Forced SWMM (app)
type: entity
updated: 2026-11-15
sources: [S79]
tags: [apps, swmm5, hot-start, dynamic-wave, engine-comparison]
reviewed: 2026-11-15
---
Bob's app that asks where in a run two versions of an engine come to differ. Version 1.0, 25 October 2026 [S79](../sources/S79-teacher-forced-swmm-summary.md).

**A caution about its source.** The page ships no technical summary. [S79](../sources/S79-teacher-forced-swmm-summary.md) was written by Claude on 14 November 2026 from the page's source, with nothing rerun, and Bob has not yet read it (Q52).

**The idea.** The ordinary comparison lets engines A and B both run free from the start. The second way restarts B from A's exact state at each restart time and measures what B does in one short window. The page borrows the name from the training of language models, where it is called teacher forcing [S79](../sources/S79-teacher-forced-swmm-summary.md).

**Three differences per element and window**, each scaled by the element's peak in A's free run [S79](../sources/S79-teacher-forced-swmm-summary.md)

| Symbol | Name | Definition |
|---|---|---|
| L | teacher-forced | B forced minus A restarted |
| R | restart | A restarted minus A running free; the null control, which must be zero |
| G | free-run | B free minus A free |

The exposure ratio E is the sum of |G| over the sum of |L|. The default window is 5 minutes.

**It first had to repair the restart.** Stock SWMM 5.2.4's hot start failed the null control on every restart tried. See [Hot start: what a restart loses](../concepts/hot-start-restart-state.md). It also found [Run duration floored to whole seconds](../concepts/run-duration-floor.md).

**Changes offered for engine B** [S79](../sources/S79-teacher-forced-swmm-summary.md): three Preissmann slot momentum variants (1, 2 and 4) written from the descriptions in EPA issue 231; inertial damping FULL or NONE; roughness times 1.10; a head tolerance of 0.0005 ft; EXTRAN surcharge against SLOT; or options typed in.

**What the stored cases show** [S79](../sources/S79-teacher-forced-swmm-summary.md)

| Change | Finding |
|---|---|
| EXTRAN to SLOT, EXTRAN example 1 | The network carries the change: 80 % of peak forced against 79 % free-run at 0.58 hours |
| Inertial damping FULL | The network undoes part of it: exposure ratio 0.45 and 0.58 |
| Head tolerance tightened tenfold | The network amplifies it: free-run difference 2.5 times the forced total for flow, with 23 % landing in windows where the change did nothing |
| Every roughness raised 10 % | Free-run depth difference 2.8 to 4.4 times the forced one |

**Checks.** With every switch off the engine's `.out` is byte-identical to stock 5.2.4 on eight EXTRAN test models; the browser and command-line harnesses agree on 11,115 numbers [S79](../sources/S79-teacher-forced-swmm-summary.md).

**What it does not show.** No observed data: "the method says nothing about which engine is right". The forced number depends on the window. Eleven model-and-change pairs on small test networks. Comparing SWMM 5 with SWMM6 or ICM this way needs those engines to read and write the same state. No person has reviewed the slot variant code against EPA issue 231 [S79](../sources/S79-teacher-forced-swmm-summary.md).

**Related.** [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md).

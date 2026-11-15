---
title: "Hot start: what a restart loses"
type: concept
updated: 2026-11-15
sources: [S79]
tags: [swmm5, hot-start, dynamic-wave, findings, verification]
reviewed: no
---
A SWMM hot start file saves the state of a run so that a later run can begin from it. In EPA SWMM 5.2.4 a run restarted from its own hot start file does not reproduce the run that wrote it [S79](../sources/S79-teacher-forced-swmm-summary.md). The [Teacher-Forced SWMM (app)](../entities/teacher-forced-swmm.md) measured this while trying to use the hot start as a tool, and had to repair it first.

**The test.** A null control: run engine A to a restart time and save a hot start; restart A from that file and run one window; compare with A running free. The difference must be zero [S79](../sources/S79-teacher-forced-swmm-summary.md).

**The result, stock 5.2.4**, on the slot versions of three EXTRAN manual examples, over every 5-minute window [S79](../sources/S79-teacher-forced-swmm-summary.md)

| Model | Restarts | Exact | Worst flow change within five minutes |
|---|---|---|---|
| EXTRAN example 1 | 94 | 0 | 1.457588 cfs |
| EXTRAN example 4 | 94 | 0 | 1.725739 cfs |
| EXTRAN example 7 (pumps) | 94 | 0 | 5.0 cfs |

**Five pieces of solver state that do not survive**, as the app's essay lists them [S79](../sources/S79-teacher-forced-swmm-summary.md)

| ID | Where | What |
|---|---|---|
| R-1 | `hotstart.c:234-236`, links at 253-256 | Routing state is written as 32-bit floats |
| R-2 | `flowrout.c:496` with `dwflow.c:287` | Conduit area is rebuilt from link depth on restart |
| R-3 | `dynwave.c:674` with `node.c:303` | The trapezoidal volume update uses the last step's net inflow |
| R-4 | `dynwave.c:140` with `dynwave.c:728` | Surface area from the last non-surcharged step is reset to 0 |
| R-5 | `dynwave.c:209-212` | The variable time step restarts at the minimum |

The essay says none of the five is a bug in ordinary use [S79](../sources/S79-teacher-forced-swmm-summary.md).

**The repair.** The app's build writes a sidecar file beside the hot start, in double precision, carrying those five things, and restores them after routing opens. With it, 282 of 282 restarts across the three models are bit-exact, against 0 of 282 for the stock hot start. With the switch off, the build's output is byte-identical to stock 5.2.4 on eight EXTRAN test models [S79](../sources/S79-teacher-forced-swmm-summary.md).

**What still is not exact** [S79](../sources/S79-teacher-forced-swmm-summary.md)
- Subcatchments. On model user2 (17 subcatchments) the precise restart is off by up to 0.007 percent of an element's peak. The source has not been traced.
- Variable time steps. A run that stops at a restart time takes a shortened last step that the free run never takes.
- The end of the run itself: see [Run duration floored to whole seconds](run-duration-floor.md).

**The practice it suggests.** The app reruns the null control in every experiment and shows the result before any other number [S79](../sources/S79-teacher-forced-swmm-summary.md). Our reading of the table above: a comparison that restarts an engine from saved state without that check cannot tell a restart artifact from a real difference.

**Status.** These are the page's findings, under its own IDs R-1 to R-5, read and measured by Claude in one session on 25 October 2026. No person has reviewed them, and the summary they are cited from was written from the page, not from a rerun (Q52). They have no IDs in [The SWMM findings register](findings-register.md) (Q47).

See [Dynamic wave routing](dynamic-wave-routing.md), [Byte-for-byte gate](byte-for-byte-gate.md).

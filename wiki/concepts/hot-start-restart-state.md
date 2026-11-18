---
title: "Hot start: what a restart loses"
type: concept
updated: 2026-11-17
sources: [S79, S196, S202, S217]
tags: [swmm5, hot-start, dynamic-wave, findings, verification]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S192 to S202 ingest): one paragraph added at the end on saved states in two apps (S196, S202); 2026-11-17 (S205 to S223 ingest): a paragraph added near the end, headed Added 17 November 2026 (S217)"
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

**Added 17 November 2026.** Two more apps touch saved states.
- [One Model, Three Engines](../entities/one-model-three-engines.md): from a state saved at full load, a one-minute run changes no pipe's flow by more than 5.3e-7 cfs; from a state saved at 80 percent, the outlet still reports 1.62 of 2.0 cfs after a minute. The numbers are from the app's lumped teaching model [S202](../sources/S202-one-model-three-engines-summary.md).
- [SWMM5 RASPIPE](../entities/swmm5-raspipe.md): its hot-start files carry node and link states, not the states of its pipe cells [S196](../sources/S196-swmm5-raspipe-summary.md).

**Added 17 November 2026.** [SWMM Run Supervisor (app)](../entities/swmm-run-supervisor.md) cuts a 24-hour run into 96 windows of 15 minutes joined by hot-start files. With every window at the careful preset, the node depths differ from the unbroken run by 0.045 ft rms, 158 of 164 peaks within 0.1 ft and the worst 0.51 ft off. One missing flag made the first runoff step after a restart a dry step, 1 % too much runoff, since fixed [S217](../sources/S217-swmm-run-supervisor-summary.md).

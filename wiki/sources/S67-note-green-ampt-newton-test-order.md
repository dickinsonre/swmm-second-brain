---
title: "S67: Note, SWMM5's Green-Ampt solver tests the Newton correction before applying it (2026-11-14)"
type: source
raw: raw/notes/green-ampt-newton-test-order.md
kind: note
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-14
tags: [swmm5, infiltration, green-ampt, findings, verification]
reviewed: 2026-11-15
---
**What it is.** A one-idea note, on the repository's note template, about four lines of `grnampt_getF2` in EPA SWMM 5.2.4. Its own status line reads "working". Raw file: [raw/notes/green-ampt-newton-test-order.md](../../raw/notes/green-ampt-newton-test-order.md).

**How it was written.** Its AI-use line: "drafted by Claude (Anthropic) on 14 November 2026 from test runs Claude made in a chat with Bob Dickinson. The wording is Claude's until Bob rewrites it." It also says the runs "were made once and have not been rerun by Bob". Every claim below is therefore an AI-written passage. One part was checked at ingest and is marked.

**Claims worth keeping**
- In `src/solver/infil.c`, lines 847 to 856, the Newton loop computes a correction `df2`, tests `fabs(df2) < 0.00001` (ft), and returns before the line `f2 -= df2;` runs. The loop starts with `f2` equal to `f1`.
- So when the first correction is already under the limit, the function returns the minimum volume, and the step infiltrates at Ksat alone with the suction term dropped.
- When that happens: a wet step of 10 s or more, and Ks (in/hr) times wet step (s) times (1 + c1/F) below 0.432, where c1 is (suction head + ponded depth) times the moisture deficit and F is the cumulative infiltration.
- Test model: one 10 ac pervious subcatchment, suction 12.6 in, Ksat 0.01 in/hr, deficit 0.10, 24 hours of rain totalling 6.137 in. c1 = 1.26 in.
- Results: stock 5.2.4 infiltrates 1.096 to 1.097 in at wet steps of 5, 30, 60 and 300 s, with a peak runoff of 3.3109 cfs. At a 15 s wet step it infiltrates 0.868 in, with a peak of 3.4858 cfs. The note calls this a 21 % loss. The continuity error stayed at -0.001 %.
- At 15 s the early return starts once F passes 0.67 in. At 30 s it would need F above 2.86 in, which the run never reaches.
- Four independent solvers of the same equation gave 1.096 in and 3.3109 cfs at 15 s. The note does not say what the four are.
- The fix is one line moved: apply `f2 -= df2;` before the test. With it, the 15 s run gives 1.096 in and 3.3109 cfs.
- A smaller effect in every run: the value returned is the iterate before its last correction, so stock is high by up to 0.00001 ft per call. On a silt loam test, 1.287 in against 1.286 in.
- To rerun: `greenampt_clay_15s.inp` on stock 5.2.4 gives 0.868 in; with `swmm524_greenampt_alternates.patch` and `GA_ALT=6` it gives 1.096 in.

**Limits it states.** "Not shown: any real model, LID, snowmelt or storage seepage." Runs made once.

**Checked at ingest**
- The ten quoted lines were compared with `infil.c` at tag v5.2.4 in EPA's repository (USEPA/Stormwater-Management-Model) on 14 November 2026. They match, at lines 847 to 856. The same file sends wet steps under 10 s down a different branch, which fits "10 s or more".
- The 0.432 follows from the code as quoted: the first correction is Ks times ts times (1 + c1/F), and 0.00001 ft is 0.00012 in, times 3,600 s per hour (our algebra).
- With Ks = 0.01 in/hr and c1 = 1.26 in the condition gives F above 0.67 in at 15 s and above 2.86 in at 30 s, as stated. (1.096 - 0.868) / 1.096 is 20.8 %.
- Not checked: any of the run results. The `.inp`, the patch and the full write-up the note links to (`green-ampt-newton-stop-2026-11-14.md`) are not in the repository (Q44).

**Feeds:** [Green-Ampt Newton test order](../concepts/green-ampt-newton-test-order.md), [Infiltration methods](../concepts/infiltration-methods.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [The SWMM findings register](../concepts/findings-register.md), [EPA SWMM 5](../entities/swmm-5.md).

---
title: One Model, Three Engines (app)
type: entity
updated: 2026-11-17
sources: [S202]
tags: [apps, infosewer, icm, conversion, backwater]
reviewed: no
---
Bob's 2026 field guide to moving the InfoSewer training model into ICM InfoWorks and ICM SWMM. Version 1.1, 2 November 2026 [S202](../sources/S202-one-model-three-engines-summary.md).

**A caution about its source.** The page ships no technical summary. [S202](../sources/S202-one-model-three-engines-summary.md) was written by Claude on 16 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q99).

**The study and the app.** The study is Bob's: the training model imported to [InfoWorks ICM](infoworks-icm.md), converted to ICM SWMM, compared by Ruby, two load fixes, saved-state runs and a 315-location comparison. The page says the study's run dates and software builds are not recorded in it. The app adds the seven steps with checks after each, a Compare tab, and three labs computed in the browser by teaching solvers. Neither ICM engine runs in the page [S202](../sources/S202-one-model-three-engines-summary.md).

**The lesson it teaches: matching flow does not prove a conversion** [S202](../sources/S202-one-model-three-engines-summary.md)
- In a 15 in pipe carrying 1.2 cfs with 1.00 ft of water at the outlet, normal depth is 0.56 ft at 2.25 ft/s. The backwater profile puts 0.76 ft at mid-length, 35 percent deeper, at 1.54 ft/s, 32 percent slower. Both carry exactly 1.2 cfs.
- On twelve teaching pipes, depth misses by up to 0.47 ft and velocity by up to 1.22 ft/s while the flows match, "because both methods were handed the same discharge."
- Shrinking one pipe from 15 to 12 in leaves every flow unchanged and raises its depth from 0.48 to 0.54 ft.

**Saved states.** A dry chain of 15 pipes takes about 35 minutes to pass 99 percent of its load. Started from a state saved at full load, one minute changes no pipe's flow by more than 5.3e-7 cfs; from a state saved at 80 percent, the outlet still reports 1.62 of 2.0 cfs after a minute [S202](../sources/S202-one-model-three-engines-summary.md). See [Hot start: what a restart loses](../concepts/hot-start-restart-state.md).

**Checks.** 56 automated checks in Node. An outside review of version 1.0 reproduced the backwater and chain numbers independently; version 1.1 answers that review [S202](../sources/S202-one-model-three-engines-summary.md).

**What it does not show.** No ICM run. The chain is a lumped model whose fill times move by about 12 percent when every pipe is split. The Ruby snippets were not run in ICM. The essay's account of the study has not had Bob's review [S202](../sources/S202-one-model-three-engines-summary.md).

**Related.** [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md), [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md), [InfoSewer to InfoWorks ICM (app)](infosewer-to-infoworks-icm-guide.md).

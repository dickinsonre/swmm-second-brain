---
title: "S202: One Model, Three Engines, summary written from the page (v1.1)"
type: source
raw: raw/apps/one-model-three-engines-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-17
tags: [apps, infosewer, icm, swmm5, conversion, backwater, hot-start, ruby]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of One Model, Three Engines, version 1.1 (2 November 2026): a 2026 field guide to moving the InfoSewer training model into ICM InfoWorks and ICM SWMM, with the seven steps, a compare tool, and labs on backwater and spin-up. Raw file: [raw/apps/one-model-three-engines-v1.1.md](../../raw/apps/one-model-three-engines-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary of its own. Claude (Anthropic) wrote this file on 16 November 2026, at Bob's request, from the published artifact (version 1793654421-62b5) and its About and Doc tabs. No engine was run. Bob has not read it (Q99). The page says the app and essay were built with Claude (Opus 5.5) on 2 November 2026 under Bob's direction, and that the study behind it is his: the InfoSewer training model, its import to ICM InfoWorks, the conversion to ICM SWMM, the Ruby comparison, two load fixes, the saved-state runs and a 315-location comparison. The page says the study's run dates and software builds are not recorded in it, and that the essay's account of the study has not yet had Bob's review.

**Claims worth keeping** (all copied from the page; the numbers are from its teaching solvers, not from ICM)
- Teaching pipe: 15 in, slope 0.002, n 0.013, 300 ft, 1.2 cfs, 1.00 ft of water at the outlet. Normal depth 0.56 ft at 2.25 ft/s. The backwater profile puts 0.76 ft at mid-length, 35 percent deeper, at 1.54 ft/s, 32 percent slower. Both carry exactly 1.2 cfs.
- Twelve teaching pipes at mid-length: depth misses by up to 0.47 ft and velocity by up to 1.22 ft/s while flow lies on the one-to-one line, "because both methods were handed the same discharge."
- Spin-up chain: 15 pipes of 15 in, 300 ft each at 0.003, 2.0 cfs of load, about 1,844 ft3 stored at steady state. Started dry, the outlet sees 1.1 percent of the flow after one minute and 99 percent after about 35 minutes.
- One-minute equilibrium test from a saved state at full load: largest change in any pipe's flow 5.3e-7 cfs, stored volume change 2.0e-5 ft3. From a state saved at 80 percent of the load, the outlet still reports 1.62 cfs of the 2.0 cfs after one minute.
- Break It (six 15 in pipes, 300 ft at 0.002, 0.3 cfs at every manhole): shrinking pipe 3 to 12 in leaves every flow unchanged while its mid-length depth goes from 0.48 to 0.54 ft; an outfall held at 1.1 ft raises the last pipe's depth from 0.71 to 0.91 ft; moving load from manhole 2 to 5 leaves the outlet at 1.80 cfs while pipes 2, 3 and 4 each carry 0.3 cfs less.
- The Compare tab pairs two tables by ID, checks field definitions, and scores agreement with a reference by an a + r|A| rule, median and 90th percentile.
- 56 automated checks in Node before each build. An external review of version 1.0 (76/100, provisional) independently reproduced the default backwater numbers (normal depth 0.5616 ft, mid-length 0.7601 ft, 1.5362 ft/s) and the chain's (1,844.4 ft3, 35.02 minutes to 99 percent, 1.6201 cfs after a minute from 80 percent).
- Version 1.1 corrected the claim that matching flow proves a conversion, and fixed a solver bug that held free-outfall drawdown profiles flat at critical depth (0.43 ft over the full 300 ft); the drawdown now reaches 0.50 ft at 10.54 ft from the outlet.
- Esri's retirement of ArcGIS Desktop on March 1, 2026 is cited.

**Limits it states.** Neither ICM engine runs in the page. The spin-up chain is a lumped kinematic model whose fill times move by about 12 percent when every pipe is split in two. Steep, supercritical pipes and jumps are outside the method. The Ruby snippets use field names from Bob's scripts but were not run in ICM. Two ICM help passages are cited from the review; Claude could not open those pages.

**Checked at ingest.** 0.7601 / 0.5616 = 1.354 and 1.5362 / 2.25 = 0.683, so "35 percent deeper" and "32 percent slower" hold from the unrounded values.

**Feeds:** [One Model, Three Engines (app)](../entities/one-model-three-engines.md), [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md), [Hot start: what a restart loses](../concepts/hot-start-restart-state.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md), [InfoWorks ICM](../entities/infoworks-icm.md).

---
title: "S83: People as Pollutants, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/people-as-pollutants-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-29
ingested: 2026-11-15
tags: [apps, swmm5, water-quality, pumps, storage, findings, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-15
---
**What it is.** A technical summary of the app People as Pollutants, version 1.0.0 (29 October 2026): a three-level transit station written as an EPA SWMM 5.2.4 input file, with the water read as a crowd. Raw file: [raw/apps/people-as-pollutants-v1.0.0.md](../../raw/apps/people-as-pollutants-v1.0.0.md).

**How it was written. This one is different.** The page carries no summary of its own. Claude (Anthropic, model claude-fable-5-2) wrote the file on 14 November 2026, at Bob's request, from the page's source, its Verify and About tabs, its essay and its two embedded records. Nothing was rerun. Bob has not read it (Q52). The app was built with Claude in one session on 29 October 2026 at Bob's request; the page says no person has checked the station geometry, the device capacities or the Weidmann parameters as entered.

**Claims worth keeping** (all copied from the page)
- The mapping: one cubic foot of water is one person; a floor zone is a storage unit whose area is the floor area divided by 100; a walkway, stair, escalator, gate, lift or train door is a TYPE4 pump; traveler types are pollutants; a pollutant PATIENCE decays at 1 per 600 seconds.
- Twelve floor zones and twenty-two pumps. The engine is unmodified EPA SWMM 5.2.4 as a wasm32-wasi reactor (clang 18).
- Baseline: 23,241.8 people walk in, 4,200 and 7,000 get off trains, 0 lost to flooding; census error 2.86 people, 0.008 percent; flow routing continuity 0.004 percent.
- D-1: `qualrout.c` line 41, `ZeroDepth = 0.003281` (1 mm in ft). A node shallower than that with no inflow has its concentrations set to zero. With depth read as density 1:1, one tracer's quality continuity error is -30.395 percent. Mitigated by scaling depth by 100.
- D-2: `dynwave.c`, `setNodeDepth()`, `surfArea = MAX(surfArea, MinSurfArea)`. A storage unit smaller than MIN_SURFAREA (default 12.566 ft²) changes depth as if it had that area. With the default the census misses by 0.573 percent. Fixed with MIN_SURFAREA 0.01.
- D-3 is in the in-memory file system, not SWMM: a 6 MB report took 5.7 s to write.
- The page calls D-1 and D-2 "two SWMM defaults" that leak into a crowd model, not errors in SWMM for water.
- Prompted by Gavin Nicholls' LinkedIn post about Throng; the page says it is not affiliated and uses none of its code or data.

**Limits it states.** Water has no destination, so route choice is fixed by pump curve shares. Storage units are mixed tanks, not queues. No field data. The geometry is drawn, not surveyed.

**Checked at ingest.** Every number was searched for in the page source when the file was written. Level depths in feet are the summary's conversions from the page's 6.00 and 11.94 m. The IDs D-1 and D-2 here are unrelated to D-1 in [S79](S79-teacher-forced-swmm-summary.md) and to D1 and D2 in [S59](S59-topsoil-recovery-check-app-md.md) (Q47).

**Feeds:** [People as Pollutants (app)](../entities/people-as-pollutants.md), [The SWMM findings register](../concepts/findings-register.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

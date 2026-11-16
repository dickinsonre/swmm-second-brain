---
title: "S77: Under Load, technical summary (app .md, v1.4.0)"
type: source
raw: raw/apps/under-load.md
kind: app-md
author: Robert Dickinson
published: 2026-11-11
ingested: 2026-11-15
tags: [apps, swmm5, dynamic-wave, sensitivity, verification, wasm, ai-agents]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary that ships with Under Load, version 1.4.0: eight instruments around EPA SWMM 5.2.4 in the browser, the main one a sweep that finds how far a model's design storm is from its next regime change. Raw file: [raw/apps/under-load.md](../../raw/apps/under-load.md). Bob uploaded it on 14 November 2026.

**How it was written.** By Claude (Anthropic), October and November 2026, under Bob's direction. Bob supplied the eight office-hours topics and his answers. Versions 1.1.0 to 1.3.0 repair findings of three outside reviews (70, 83 and 84 of 100; the reviewer is not named). Version 1.4.0 repairs what Claude's own review found: 16 of 26 probes failed on 1.3.0.

**Claims worth keeping**
- Load knob: a multiplier on every rain gage series and every FLOW row of [INFLOWS]. Dry-weather flow is not scaled.
- Regime signature: the sets of conduits that ran full, nodes that flooded, weirs that spilled and conduits that reversed. Flooding is read from the `.rpt`, not from `.out` frames.
- Edge finder: sweep 0.25 to 2.50 by 0.05 plus 0.85 to 1.25 by 0.01, then bisection to 0.25 % of load, 48 runs per sweep step at most.
- One engine patch: `dynwave.c` line 239 `Omega = UL_Omega;` (was `Omega = OMEGA;`, 0.5).
- Null effect of the patch: byte-identical `.out` on 72 of 72 EPA regression models that run (73 in USEPA/swmm-nrtestsuite).
- wasm (zig 0.17.0 cc, wasm32-wasi, -O2) against native x86-64 gcc, same source: identical on 63 of 72. Largest difference: model user5, link 647, 16.19 of 168.73 cfs.
- Narrows preset at design: next edge +1.88 % (a conduit runs full), next flooding edge +6.62 %. 23 edges, 124 runs.
- `.rpt` against `.out` flooding over a fine scan of 75 steps: the `.rpt` total decreases 0 times with load, the `.out` frame sum decreases 9 times.
- Butterfly, Narrows at 1.30x, 1 % nudge: flooding 19,210 to 21,127 ft³, amplification 9.98 +/- 0.23.
- Omega sweep, Narrows at design: at 0.1, 87 ft³ flooding and continuity -0.969 %; at 0.5, 0 ft³ and -0.089 %; at 1.5, 40,424 ft³, 36 % of steps not converging and 5.401 %. Settings agree from 0.3 to 0.9.
- Correction in 1.1.0: the "ragged edge" and 617x amplification reported in 1.0.0 were `.out` sampling artifacts.

**Limits it states.** The three presets (Narrows, Crest, Loop) are invented and sized to sit near capacity. No chaos in the mathematical sense is claimed. A flooding episode narrower than the sample gap is invisible; one recorded case lies between 1.021x and 1.023x. The thresholds are the app's choices, not EPA's. Agreement across omega is numerical agreement, not physical accuracy.

**Checked at ingest.** (21,127 - 19,210) / 19,210 = 9.98 %, which over a 1 % nudge is the stated 9.98. Its human-review line lists the three outside reviews, without saying who made them (Q38).

**Feeds:** [Under Load (app)](../entities/under-load.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

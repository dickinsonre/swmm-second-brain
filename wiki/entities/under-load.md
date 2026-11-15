---
title: Under Load (app)
type: entity
updated: 2026-11-15
sources: [S77]
tags: [apps, swmm5, dynamic-wave, sensitivity, ai-agents, verification]
reviewed: no
---
Bob's app that wraps EPA SWMM 5.2.4, running in the browser, in eight instruments, one per topic of an office-hours conversation. Version 1.4.0, 11 November 2026 [S77](../sources/S77-under-load-app-md.md).

**The main question.** How far is this model's design storm from the next regime change: a pipe running full, a node flooding, a weir spilling, a flow reversing? [S77](../sources/S77-under-load-app-md.md)

**How it answers** [S77](../sources/S77-under-load-app-md.md)
- A load multiplier scales every rain gage series and every FLOW inflow. Dry-weather flow is not scaled.
- A run's regime signature is four sets of object IDs: conduits that ran full, nodes that flooded, weirs that spilled, conduits that reversed.
- The edge finder sweeps the load from 0.25 to 2.50, and wherever two neighboring samples differ in signature it bisects to 0.25 % of load.
- The verdict is NEAR EDGE if flooding starts within 10 % of design load, WATCH within 25 %, CLEAR beyond. The bands are the app's choices, not EPA's.

On its Narrows preset the next edge is +1.88 % (a conduit runs full) and the next flooding edge +6.62 % [S77](../sources/S77-under-load-app-md.md).

**The other instruments** [S77](../sources/S77-under-load-app-md.md)

| Instrument | What it does |
|---|---|
| Butterfly | Two runs 1 % apart in load; amplification is the ratio of relative changes. Narrows at 1.30x: 9.98 for flooding |
| Omega sweep | Reruns with the under-relaxation factor of the dynamic wave solver changed |
| Reel | Picks the most eventful windows of a `.out` by a physics score |
| Agent stamp | Compares a model before and after an edit, field by field, and blocks COMPLETE when a check has no number |
| Claims, agent card, timeline | Explained-versus-evidenced claims, a machine-readable card, a career timeline |

**Two things it measured about SWMM itself** [S77](../sources/S77-under-load-app-md.md)
- Omega. SWMM 5.2.4 fixes the factor at 0.5 in `dynwave.c`. On Narrows at design: 0 ft³ of flooding at 0.5, 87 ft³ at 0.1, and 40,424 ft³ at 1.5 with 36 % of steps not converging. Results agree from 0.3 to 0.9. See [Dynamic wave routing](../concepts/dynamic-wave-routing.md).
- Flooding from the `.rpt` and from the `.out` are not the same curve. Over a fine load scan the `.rpt` total never decreases with load; the sum of `.out` frames decreases 9 times. Version 1.0.0's "ragged edge" and 617x amplification were withdrawn as `.out` sampling artifacts. See [Reading SWMM output](../concepts/reading-swmm-output.md).

**Checks.** The omega patch has no effect at its default: byte-identical `.out` on 72 of 72 EPA regression models that run. The browser build against a native gcc build is on [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md). 43 headless-browser probes pass [S77](../sources/S77-under-load-app-md.md).

**History.** 1.0.0 on 29 October 2026, then three outside reviews graded 70, 83 and 84 of 100, each answered by a version, and a self-review for 1.4.0 in which 16 of 26 probes failed on 1.3.0 [S77](../sources/S77-under-load-app-md.md).

**What it does not show.** The three presets are invented and sit near capacity by design. A flooding episode narrower than the gap between samples is invisible. No person has reviewed the networks or the text line by line [S77](../sources/S77-under-load-app-md.md).

**Open.** The reviewers of 1.0.0 to 1.2.0 are not named (Q38). See [Open questions](../open-questions.md).

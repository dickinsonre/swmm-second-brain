---
title: "S231: SWMMCRAFT Ultimate, app .md (v2.7)"
type: source
raw: raw/apps/swmmcraft-ultimate-v2.7.md
kind: app-md
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-17
tags: [apps, swmm5, editor, teaching, wasm]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app SWMMCRAFT Ultimate, version 2.7: a block-world editor for SWMM 5 networks with EPA SWMM 5.2.4 compiled to WebAssembly inside the one page: draw or import a model, press RUN and watch the engine's depths and flows. A teaching and inspection tool for small networks, not a design package. Raw file: [raw/apps/swmmcraft-ultimate-v2.7.md](../../raw/apps/swmmcraft-ultimate-v2.7.md).

**How it was written.** The app ships this file. The file says SWMMCRAFT was built with Claude in sessions in October and November 2026 under Bob's direction; Claude wrote all of the code, tests, figures and text, and proposed the world seeds, X-ray and quest book when Bob asked for imaginative improvements. Bob passed on four outside reviews (2.2: 76/100, 2.3: 79, 2.4: 86, 2.6: 82).

**Claims worth keeping** (all copied from the file)
- Corpus: files under 300 KB, duplicates removed, 459 models, of which 396 run in EPA SWMM 5.2.4 as they stand.
- Unedited round trip (import, export, run, compare every depth and flow by name): 396 of 396 identical. Renaming every object: 396 of 396 identical, 20,922 objects renamed, 31,746 references moved, 0 values differ. Before the gauge repair: 350 identical, 23 changed rain, 23 refused to export.
- Example in the in-page engine: C6 max reported 26.887 cfs against SWMM's summary 26.96, because the .out is sampled at report steps.
- In-page against native engine, .out byte for byte: 13 of 13 models identical (version 2.4).
- Node states against SWMM's tables (version 2.5, 254 dynamic-wave models): 3,140 of 3,310 surcharged junctions flagged, 0 false positives.
- 900 seeded worlds: all valid, 0 overlap area, 0 crossing pipes, 0 SWMM errors, max continuity error 0.201 %; HARD gives 296 of 300 flooded.
- Complexity on the meter: 68.5 from 71 hand-written source files (HydroCouple = 100); the shipped .html alone 62.3.

**Limits it states.** The map edits only junctions, outfalls, storage, conduits, subcatchments and gauges; the rest is carried. Results from the .out are sampled at report steps. Touch tested in emulation only. Not checked by a person: essay wording, messages, exporter defaults, behaviour on a production model.

**Checked at ingest.** 350 + 23 + 23 = 396. The engine is the v5.2.4 tag, commit 7952ca83, unchanged except a stand-in for `mkstemp()`. Distinct from the earlier [SWMMCRAFT, infiltration simulator (app)](../entities/swmmcraft-infiltration-simulator.md). The `links:` line names no Netlify address; Netlify reported a finished deploy at https://swmmcraft-ultimate.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMMCRAFT Ultimate (app)](../entities/swmmcraft-ultimate.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [SWMMCRAFT, infiltration simulator (app)](../entities/swmmcraft-infiltration-simulator.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md), [Reading SWMM output](../concepts/reading-swmm-output.md).

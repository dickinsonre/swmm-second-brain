---
title: "S283: Cymatic Synapse Generator, summary written from the page (v1.15)"
type: source
raw: raw/apps/cymatic-synapse-swmm5-swmm6-v1.15.md
kind: app-md
author: Robert Dickinson
published: 2026-10-31
ingested: 2026-11-18
tags: [apps, generators, swmm5, swmm6, storage, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Cymatic Synapse Generator, version 1.15: a generator that turns a Grok Imagine render into an EPA SWMM 5.2.4 model (a twin-rail trunk, storage hubs with throttled outlets, contours and Voronoi subcatchments) and runs it in EPA 5.2.4 and OpenSWMM 6 DW and FV in the browser. Raw file: [raw/apps/cymatic-synapse-swmm5-swmm6-v1.15.md](../../raw/apps/cymatic-synapse-swmm5-swmm6-v1.15.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/MSrYvnKsoEQoDaAqRjeMty, version 1793462693-fa99 (index.html, 7,407,120 bytes, SHA-256 5ac1f1ea49b65c4eedcde3775f4f030d529049eaee933850069fa1114289894b), every tab read in headless Chromium on 2026-11-18. The date above is the artifact's last publish. Nothing was run to write this file." The page says it was built with Claude (Opus 5.5) in October 2026 at Bob's request, with his WebAssembly engines from Seven SWMM Engines reused byte for byte; outside reviews shaped the versions (85/100 for the first, 89/100 for the eleventh, answered in 1.15).

**Claims worth keeping** (all copied from the file)
- 28 native EPA 5.2.4 runs (swmm-toolkit 0.17.0) over 23 models finished with 0 errors and 0 warnings; runoff continuity -0.003 to -0.004%, routing within 0.118%.
- Seed 7 default: OF1 peak 717.1 cfs; basins removed, pipes kept 798.6 cfs; redesigned without storage 812.1 cfs; all about 31.08 to 31.09 MG.
- The default storm drops 130.29 ac-ft on 521.19 ac, which is 3.00 in.
- The browser and native builds of 5.2.4 agree byte for byte on six of ten presets and within 0.059 ft on the rest.

**Limits it states.** Before a run the picture shows design numbers; playback interpolates between report times; the glow is decoration; OpenSWMM 6 FV runs with four cells per conduit by default, which its own manual calls not converged.

**Checked at ingest.** 130.29 ac-ft / 521.19 ac = 0.25 ft = 3.00 in (our arithmetic). The `links:` line gives Netlify as https://cymatic-synapse-swmm5-swmm6.netlify.app.

**Feeds:** [Cymatic Synapse Generator (app)](../entities/cymatic-synapse-generator.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Seven SWMM Engines (app)](../entities/seven-swmm-engines.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).

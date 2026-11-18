---
title: "S316: EPANET Web, summary written from the page (v1.0)"
type: source
raw: raw/apps/epanet-web-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, epanet, wasm, owa, verification]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app EPANET Web, version 1.0: a browser workspace for EPANET models on OWA EPANET 2.3.5. Raw file: [raw/apps/epanet-web-v1.0.md](../../raw/apps/epanet-web-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/C1k9UteHrTY6QrirDQ1afW, version 1792949013-3682 (index.html, 1,839,635 bytes, SHA-256 71c4751d95b1b1a55b158a5c0a783277412a02e14c93baec0a4f90cfbcdca6fa), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, on 25 October 2026 under the direction of Robert (Bob) Dickinson, who wrote the Lovable project, supplied its source and asked for a single-file HTML app; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A browser workspace for EPANET water distribution models, from Bob's Lovable port of the Open Water Analytics EPANET-UI desktop program. The Lovable release was its Phase 1 (workspace shell, .inp parser and writer, project tree, inspector, outline sketch); this edition adds a canvas map, property editors, the OWA EPANET 2.3.5 engine in a Web Worker, and Results, Tables, Report and Verify tabs.
- On Net1, 2,751 of 2,781 hydraulic values are bit-identical to OWA's committed native reference output; the rest differ by at most 5.21e-6 relative. Water quality differs by up to 0.172606 mg/L, which the page traces to OWA's quality code changing after the reference file was committed in August 2018, and says is an inference. Seven writer defects (D1 to D7) in the Lovable round trip are fixed.
- Engine identity: EN_getversion returns 20305, matching CODEVERSION in types.h at tag v2.3.5. The build was not compiled in this session; the version constant and the fixture match are the evidence.
- Against OWA's tests/data/example1.out for Net1, 3,710 values: node head, pressure, link headloss, status and setting all bit-identical; link flow 312 of 325 (max 6.10e-5); node quality 50 of 275 (max 0.172606); reaction totals 0 of 4.
- Round trip: the writer keeps everything the engine reads; both files are run and compared.

**Limits it states.** As the page lists it: only Net1 has a native reference output; Net2, Net3 and your own models are checked for round-trip identity only, since compiling more native references was not possible in that session. Agreement with EPANET is not agreement with the pipes in the ground. Output files compare in 4-byte floats, so differences below about one part in ten million cannot be seen. The writer does not keep every blank line and column alignment. No basemaps, GIS or CAD import, EPANET-MSX, transient analysis, recents or translations.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [EPANET Web (app)](../entities/epanet-web.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [EPANET](../entities/epanet.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

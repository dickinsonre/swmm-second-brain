---
title: "EPANET Web (app)"
type: entity
updated: 2026-11-18
sources: [S316]
tags: [apps, epanet, wasm, owa, verification]
reviewed: no
---
Bob's app EPANET Web: a browser workspace for EPANET models on OWA EPANET 2.3.5. Version 1.0, 2026-10-25 [S316](../sources/S316-epanet-web-summary.md). Its `links:` line names no live Netlify address [S316](../sources/S316-epanet-web-summary.md).

**A caution about its source.** The page ships no technical summary. [S316](../sources/S316-epanet-web-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S316](../sources/S316-epanet-web-summary.md)
- A browser workspace for EPANET water distribution models, from Bob's Lovable port of the Open Water Analytics EPANET-UI desktop program. The Lovable release was its Phase 1 (workspace shell, .inp parser and writer, project tree, inspector, outline sketch); this edition adds a canvas map, property editors, the OWA EPANET 2.3.5 engine in a Web Worker, and Results, Tables, Report and Verify tabs.
- On Net1, 2,751 of 2,781 hydraulic values are bit-identical to OWA's committed native reference output; the rest differ by at most 5.21e-6 relative. Water quality differs by up to 0.172606 mg/L, which the page traces to OWA's quality code changing after the reference file was committed in August 2018, and says is an inference. Seven writer defects (D1 to D7) in the Lovable round trip are fixed.
- Engine identity: EN_getversion returns 20305, matching CODEVERSION in types.h at tag v2.3.5. The build was not compiled in this session; the version constant and the fixture match are the evidence.
- Against OWA's tests/data/example1.out for Net1, 3,710 values: node head, pressure, link headloss, status and setting all bit-identical; link flow 312 of 325 (max 6.10e-5); node quality 50 of 275 (max 0.172606); reaction totals 0 of 4.
- Round trip: the writer keeps everything the engine reads; both files are run and compared.

**How to use it, as the summary puts it.** Use it to open, edit, run and round-trip EPANET models in a browser with nothing sent to a server. Only Net1 has a native reference; there are no basemaps, no GIS or CAD import, no MSX and no transients, and new pipes cannot be drawn. [S316](../sources/S316-epanet-web-summary.md)

**What it does not show.** As the page lists it: only Net1 has a native reference output; Net2, Net3 and your own models are checked for round-trip identity only, since compiling more native references was not possible in that session. Agreement with EPANET is not agreement with the pipes in the ground. Output files compare in 4-byte floats, so differences below about one part in ten million cannot be seen. The writer does not keep every blank line and column alignment. No basemaps, GIS or CAD import, EPANET-MSX, transient analysis, recents or translations. [S316](../sources/S316-epanet-web-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [EPANET](epanet.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

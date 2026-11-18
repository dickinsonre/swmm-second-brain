---
name: EPANET Web
file: epanet-web.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/C1k9UteHrTY6QrirDQ1afW", original: "Lovable project epanet-web (MIT), a port of OWA EPANET-UI", repo: "https://github.com/dickinsonre/EPANET-UI (fork of the desktop program)"}
engines:
  - {name: OWA EPANET, version: "2.3.5 (CODEVERSION 20305)", source: "OWA EPANET tag v2.3.5", build: "WebAssembly build shipped in npm epanet-js 0.9.0 (MIT); EpanetEngine.wasm SHA-256 f3f0f4aad13dfb21d9f26fb6587474bc200cc52a28337a8ee4cc32d38cf08f29", license: "EPA contributions public domain; OWA contributions MIT"}
units: as the model's own FLOW units
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 25 October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/C1k9UteHrTY6QrirDQ1afW, version 1792949013-3682 (index.html, 1,839,635 bytes, SHA-256 71c4751d95b1b1a55b158a5c0a783277412a02e14c93baec0a4f90cfbcdca6fa), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# EPANET Web: a browser workspace for EPANET models on OWA EPANET 2.3.5

## In three points
- **What:** A browser workspace for EPANET water distribution models, from Bob's Lovable port of the Open Water Analytics EPANET-UI desktop program. The Lovable release was its Phase 1 (workspace shell, .inp parser and writer, project tree, inspector, outline sketch); this edition adds a canvas map, property editors, the OWA EPANET 2.3.5 engine in a Web Worker, and Results, Tables, Report and Verify tabs.
- **So what:** On Net1, 2,751 of 2,781 hydraulic values are bit-identical to OWA's committed native reference output; the rest differ by at most 5.21e-6 relative. Water quality differs by up to 0.172606 mg/L, which the page traces to OWA's quality code changing after the reference file was committed in August 2018, and says is an inference. Seven writer defects (D1 to D7) in the Lovable round trip are fixed.
- **Now what:** Use it to open, edit, run and round-trip EPANET models in a browser with nothing sent to a server. Only Net1 has a native reference; there are no basemaps, no GIS or CAD import, no MSX and no transients, and new pipes cannot be drawn.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 25 October 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Workspace, Results, Tables, Report, INP, Verify, About, Doc. The map pans, zooms and selects every element type, with vertices, labels, flow arrows and a colour legend. Junctions, reservoirs, tanks, pipes, pumps and valves can be edited, and every other section in a full-text editor. Each run gets a fresh engine instance and file system in a Web Worker: EN_open, EN_solveH, EN_solveQ, EN_getstatistic, EN_report, EN_close, then the page reads EPANET's binary output with its own reader. Examples: Net1, Net2, Net3 from the OWA repository (tag v2.3.5) and a ten-line Probe written to exercise the round-trip cases. CSV, .rpt and GIF export.

## Checks (as stated on the page)

The Verify tab runs live in the browser:
- Engine identity: EN_getversion returns 20305, matching CODEVERSION in types.h at tag v2.3.5. The build was not compiled in this session; the version constant and the fixture match are the evidence.
- Against OWA's tests/data/example1.out for Net1, 3,710 values: node head, pressure, link headloss, status and setting all bit-identical; link flow 312 of 325 (max 6.10e-5); node quality 50 of 275 (max 0.172606); reaction totals 0 of 4.
- Round trip: the writer keeps everything the engine reads; both files are run and compared.

## What this does not show

As the page lists it: only Net1 has a native reference output; Net2, Net3 and your own models are checked for round-trip identity only, since compiling more native references was not possible in that session. Agreement with EPANET is not agreement with the pipes in the ground. Output files compare in 4-byte floats, so differences below about one part in ten million cannot be seen. The writer does not keep every blank line and column alignment. No basemaps, GIS or CAD import, EPANET-MSX, transient analysis, recents or translations.

## Credits and licenses

OWA EPANET, tag v2.3.5 (US EPA contributions public domain; OWA contributions MIT); epanet-js 0.9.0 (MIT, Luke Butler; glue edited only to drop its ES-module export); OWA EPANET-UI (MIT); Lewis Rossman, EPANET's author at US EPA. The Lovable epanet-web is MIT, © 2026 Robert Dickinson.

## AI use

The page says: built with Claude, Anthropic's AI model, on 25 October 2026 under the direction of Robert (Bob) Dickinson, who wrote the Lovable project, supplied its source and asked for a single-file HTML app; responsibility is his. Claude read the Lovable source, found the Verify-tab defects by running the original parser and writer in Node, ported and fixed them, wrote the binary output reader, chose and embedded the epanet-js engine build, and wrote the map, inspector, charts, tables, checks, GIF encoder, text and Doc essay. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first HTML edition (the version read).

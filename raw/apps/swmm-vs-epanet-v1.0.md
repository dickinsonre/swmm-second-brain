---
name: SWMM vs EPANET
file: swmm-vs-epanet.html
version: "1.0"
date: 2026-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/LeDmUB8dvATfeqCn1PXHrN", original: "Lovable app swmm-epanet-comparison-tool", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, build: "USEPA tag v5.2.4, commit 7952ca8; zig 0.17.0, wasm32-wasi, -O2, unmodified solver; 524,846 bytes, SHA-256 52f33fa6...327b1", license: public domain}
  - {name: OWA EPANET, version: 2.3.5, build: "OpenWaterAnalytics tag v2.3.5, commit 444725f; zig 0.17.0, wasm32-wasi, -O2, plus a mkstemp() shim; 230,375 bytes, SHA-256 d5ed4ea0...d81d3", license: "EPA contributions public domain; OWA contributions MIT"}
units: US customary (ft, psi, gpm)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/LeDmUB8dvATfeqCn1PXHrN, version 1792899482-fae8 (index.html, 588,678 bytes, SHA-256 3cd6dd50edbd7ee0145f5c639c32075891d5fcae2de6d8ed70d7442e2427dd41), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM vs EPANET: one pressurized network, two engines, one browser tab

## In three points
- **What:** Builds one pressurized pipe network, writes it as an EPA SWMM 5.2 input and an EPANET 2.3 input, runs both real engines in the browser (compiled to WebAssembly, in a Web Worker), and compares heads, pressures and flows. A single-file edition of Bob's Lovable app, rebuilt in US customary units.
- **So what:** On the 6-node, 6-pipe sample, the worst head RMSE across four junctions and the tank is 0.29 ft (largest single difference 0.76 ft) and pressures agree within 0.13 psi RMSE. SWMM reports +0.708% flow routing continuity error: about 5 gpm more water runs through its pipes to the tank and disappears there. The Lovable build never parsed SWMM's results, ignored roughness in SWMM (n fixed at 0.013), flooded junctions at 10 m, and ran a 24-hour simulation for 48 hours.
- **Now what:** Use it to see how a gravity engine and a pressure engine treat the same pipes. No pumps, valves, controls or water quality are translated; demands are fixed; a full tank means different hardware in each engine; and every magnitude comes from one small network.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); it gives the build month (October 2026) but no day. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Network, Inputs, Run, Compare, About, Doc. Quick start: Run both engines (about a second), then Compare; click T1 on the map, then P6; change a pipe diameter and run again. Both engines run as command-line programs inside a Web Worker against an in-memory file system; the modules are stored gzip-compressed in the page. The Compare tab sets aside the demand-step instants by default: EPANET's report at seven o'clock already includes the new demand, SWMM's is the state a moment before (40 of 191 samples sit on a jump at a 15-minute report step).

## Checks (as stated on the page)

- The in-page WASI host against Node's built-in WASI on the same inputs: SWMM .out byte-identical (64,272 bytes); EPANET .out identical except the 10 header bytes that hold the input file name; both reports identical apart from their clock lines.
- The SWMM binary reader refuses the file unless its walk lands exactly on the results offset SWMM recorded; the EPANET reader's first J1 head (87.354 m) matches the report's 87.35.
- The sample network and five variants (flat demand, Darcy-Weisbach, no tank, Manning friction, SLOT surcharge) through both engines, 30-odd paired runs; at a one-second step the RMSE jumps to 2.87 ft because the report lands within a second of a demand jump.
- A headless-browser run. No person has compared the results with a desktop run of either engine.

## What this does not show

As the page lists it: pumps, valves, controls and water quality; SWMM hydrology; EPANET's pressure-driven demand; a full tank (EPANET closes the inlet, SWMM spills); a minimum tank level in SWMM; water hammer (neither engine models an elastic pipe; SWMM's inertia is a rigid column); generality beyond one 6-node, 6-pipe network.

## Credits and licenses

EPA SWMM source (public domain); OWA EPANET source; Rossman (2017), SWMM Reference Manual Volume II. The Lovable swmm-epanet-comparison-tool is Bob Dickinson's. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for this edition; responsibility is his. Claude found and confirmed the defects by running the original translation, compiled both engines to WebAssembly, and wrote the WASI host, writers, readers, statistics, interface, figures, Doc essay and Word document. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10): first single-file edition (the version read).

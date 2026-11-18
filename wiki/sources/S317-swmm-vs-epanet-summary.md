---
title: "S317: SWMM vs EPANET, summary written from the page (v1.0)"
type: source
raw: raw/apps/swmm-vs-epanet-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10
ingested: 2026-11-18
tags: [apps, swmm5, epanet, pressurized-networks]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app SWMM vs EPANET, version 1.0: one pressurized network, two engines, one browser tab. Raw file: [raw/apps/swmm-vs-epanet-v1.0.md](../../raw/apps/swmm-vs-epanet-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/LeDmUB8dvATfeqCn1PXHrN, version 1792899482-fae8 (index.html, 588,678 bytes, SHA-256 3cd6dd50edbd7ee0145f5c639c32075891d5fcae2de6d8ed70d7442e2427dd41), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for this edition; responsibility is his. Claude found and confirmed the defects by running the original translation, compiled both engines to WebAssembly, and wrote the WASI host, writers, readers, statistics, interface, figures, Doc essay and Word document. The checks are mechanical."

**Claims worth keeping** (all copied from the file)
- Builds one pressurized pipe network, writes it as an EPA SWMM 5.2 input and an EPANET 2.3 input, runs both real engines in the browser (compiled to WebAssembly, in a Web Worker), and compares heads, pressures and flows. A single-file edition of Bob's Lovable app, rebuilt in US customary units.
- On the 6-node, 6-pipe sample, the worst head RMSE across four junctions and the tank is 0.29 ft (largest single difference 0.76 ft) and pressures agree within 0.13 psi RMSE. SWMM reports +0.708% flow routing continuity error: about 5 gpm more water runs through its pipes to the tank and disappears there. The Lovable build never parsed SWMM's results, ignored roughness in SWMM (n fixed at 0.013), flooded junctions at 10 m, and ran a 24-hour simulation for 48 hours.
- The in-page WASI host against Node's built-in WASI on the same inputs: SWMM .out byte-identical (64,272 bytes); EPANET .out identical except the 10 header bytes that hold the input file name; both reports identical apart from their clock lines.
- The SWMM binary reader refuses the file unless its walk lands exactly on the results offset SWMM recorded; the EPANET reader's first J1 head (87.354 m) matches the report's 87.35.
- The sample network and five variants (flat demand, Darcy-Weisbach, no tank, Manning friction, SLOT surcharge) through both engines, 30-odd paired runs; at a one-second step the RMSE jumps to 2.87 ft because the report lands within a second of a demand jump.
- A headless-browser run. No person has compared the results with a desktop run of either engine.

**Limits it states.** As the page lists it: pumps, valves, controls and water quality; SWMM hydrology; EPANET's pressure-driven demand; a full tank (EPANET closes the inlet, SWMM spills); a minimum tank level in SWMM; water hammer (neither engine models an elastic pipe; SWMM's inertia is a rigid column); generality beyond one 6-node, 6-pipe network.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM vs EPANET (app)](../entities/swmm-vs-epanet.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [EPANET](../entities/epanet.md), [Two Engines, One Town (app)](../entities/two-engines-one-town.md), [Force main friction](../concepts/force-main-friction.md).

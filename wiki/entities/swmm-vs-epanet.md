---
title: "SWMM vs EPANET (app)"
type: entity
updated: 2026-11-18
sources: [S317]
tags: [apps, swmm5, epanet, pressurized-networks]
reviewed: no
---
Bob's app SWMM vs EPANET: one pressurized network, two engines, one browser tab. Version 1.0, 2026-10 [S317](../sources/S317-swmm-vs-epanet-summary.md). Its `links:` line names no live Netlify address [S317](../sources/S317-swmm-vs-epanet-summary.md).

**A caution about its source.** The page ships no technical summary. [S317](../sources/S317-swmm-vs-epanet-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S317](../sources/S317-swmm-vs-epanet-summary.md)
- Builds one pressurized pipe network, writes it as an EPA SWMM 5.2 input and an EPANET 2.3 input, runs both real engines in the browser (compiled to WebAssembly, in a Web Worker), and compares heads, pressures and flows. A single-file edition of Bob's Lovable app, rebuilt in US customary units.
- On the 6-node, 6-pipe sample, the worst head RMSE across four junctions and the tank is 0.29 ft (largest single difference 0.76 ft) and pressures agree within 0.13 psi RMSE. SWMM reports +0.708% flow routing continuity error: about 5 gpm more water runs through its pipes to the tank and disappears there. The Lovable build never parsed SWMM's results, ignored roughness in SWMM (n fixed at 0.013), flooded junctions at 10 m, and ran a 24-hour simulation for 48 hours.
- The in-page WASI host against Node's built-in WASI on the same inputs: SWMM .out byte-identical (64,272 bytes); EPANET .out identical except the 10 header bytes that hold the input file name; both reports identical apart from their clock lines.
- The SWMM binary reader refuses the file unless its walk lands exactly on the results offset SWMM recorded; the EPANET reader's first J1 head (87.354 m) matches the report's 87.35.
- The sample network and five variants (flat demand, Darcy-Weisbach, no tank, Manning friction, SLOT surcharge) through both engines, 30-odd paired runs; at a one-second step the RMSE jumps to 2.87 ft because the report lands within a second of a demand jump.
- A headless-browser run. No person has compared the results with a desktop run of either engine.

**How to use it, as the summary puts it.** Use it to see how a gravity engine and a pressure engine treat the same pipes. No pumps, valves, controls or water quality are translated; demands are fixed; a full tank means different hardware in each engine; and every magnitude comes from one small network. [S317](../sources/S317-swmm-vs-epanet-summary.md)

**What it does not show.** As the page lists it: pumps, valves, controls and water quality; SWMM hydrology; EPANET's pressure-driven demand; a full tank (EPANET closes the inlet, SWMM spills); a minimum tank level in SWMM; water hammer (neither engine models an elastic pipe; SWMM's inertia is a rigid column); generality beyond one 6-node, 6-pipe network. [S317](../sources/S317-swmm-vs-epanet-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [EPANET](epanet.md), [Two Engines, One Town (app)](two-engines-one-town.md), [Force main friction](../concepts/force-main-friction.md).

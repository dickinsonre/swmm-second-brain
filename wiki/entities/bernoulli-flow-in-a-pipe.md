---
title: "Bernoulli Flow in a Pipe (app)"
type: entity
updated: 2026-11-18
sources: [S319]
tags: [apps, pipes, friction, epanet, swmm5, verification]
reviewed: no
---
Bob's app Bernoulli Flow in a Pipe: two gauges, one pipe, three friction laws, checked against EPANET 2.2 and SWMM 5.2.4. Version 2.2, 2026-11-03 [S319](../sources/S319-bernoulli-flow-in-a-pipe-summary.md). Its `links:` line names no live Netlify address [S319](../sources/S319-bernoulli-flow-in-a-pipe-summary.md).

**A caution about its source.** The page ships no technical summary. [S319](../sources/S319-bernoulli-flow-in-a-pipe-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S319](../sources/S319-bernoulli-flow-in-a-pipe-summary.md)
- A one-pipe lab: given the pressure at both ends, how much flows? It solves Bernoulli's energy balance with Darcy-Weisbach (Colebrook or Swamee-Jain), Hazen-Williams or Manning, shows velocity, flow, Reynolds number and an energy ledger that must close, and writes the same pipe as SWMM 5 and EPANET .inp files.
- The Lovable version 1's main panel never converged: its 15-pass fixed-point loop amplified its own error (slope about f·L/D = 1.25 at its default), printed 30.3 ft/s (9.24 m/s) where the engines' root is 29.92 ft/s (9.120 m/s; feet are our conversion), and missed EPANET by as much as 149% across eight test pipes. The rewritten solver matches 51 engine results within 0.0003%.
- Nine test pipes, V1 to V9, in two engines: EPANET 2.2 (one solve at accuracy 10^-8, with Hazen-Williams, Darcy-Weisbach and Chezy-Manning) and EPA SWMM 5.2.4 (dynamic wave at a fixed 0.5 s step for two hours, as a CIRCULAR conduit and as a FORCE_MAIN under each equation). SWMM ran water only, having no viscosity input; the oil line ran in EPANET alone.
- 51 results, worst gap 0.0003%. The Verify tab recomputes every one of them in the browser against the stored engine flows.
- 27 exported .inp files round-tripped: written by the app, run by the engines, flows back within 0.00034% of the app's.
- Defects D1 to D10 in the Lovable source (solver, equation, zero-head case, transition rule, engine labels) and D11 to D19 from the outside review of v2.1 (EPANET fluid density, a lowest-pressure readout and liquid check, refused inputs, saved materials, keyboard and phone use, a redrawn figure, a complete verification suite), each listed on the Verify tab.

**How to use it, as the summary puts it.** Use it to teach the energy balance and how SWMM and EPANET treat the same pressure pipe. Agreement with the engines checks arithmetic, not the friction laws: no measured flow, one steady full pipe, and SWMM 6 was read, not run. [S319](../sources/S319-bernoulli-flow-in-a-pipe-summary.md)

**What it does not show.** As the page lists it: no measured flow, so agreement proves the arithmetic matches the engines and not that any law describes a real pipe; one pipe, steady and full, with no networks, surges or partly full pipes; SWMM 6's column is the SWMM 5 number, justified by its source at one commit; liquid stays liquid or the app says so (it warns at the vapor pressure of water, about 0.34 psi absolute at 68 F) but models no cavitation; the laminar-turbulent transition band is a guess in every engine. [S319](../sources/S319-bernoulli-flow-in-a-pipe-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Force main friction](../concepts/force-main-friction.md), [EPANET](epanet.md).

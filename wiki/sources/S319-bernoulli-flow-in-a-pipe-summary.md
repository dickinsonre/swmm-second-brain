---
title: "S319: Bernoulli Flow in a Pipe, summary written from the page (v2.2)"
type: source
raw: raw/apps/bernoulli-flow-in-a-pipe-v2.2.md
kind: app-md
author: Robert Dickinson
published: 2026-11-03
ingested: 2026-11-18
tags: [apps, pipes, friction, epanet, swmm5, verification]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Bernoulli Flow in a Pipe, version 2.2: two gauges, one pipe, three friction laws, checked against EPANET 2.2 and SWMM 5.2.4. Raw file: [raw/apps/bernoulli-flow-in-a-pipe-v2.2.md](../../raw/apps/bernoulli-flow-in-a-pipe-v2.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/HWaPmxhYD3trZmFoAhMAFa, version 1793712264-3f89 (index.html, 1,633,130 bytes, SHA-256 d4c317a830642ce52db470c96f3f474b5894de42bac1bb00f774e5b63f6ba1c8), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, on 24 October 2026 under the direction of Robert (Bob) Dickinson, who built version 1 in Lovable, supplied its source and asked for an HTML app; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A one-pipe lab: given the pressure at both ends, how much flows? It solves Bernoulli's energy balance with Darcy-Weisbach (Colebrook or Swamee-Jain), Hazen-Williams or Manning, shows velocity, flow, Reynolds number and an energy ledger that must close, and writes the same pipe as SWMM 5 and EPANET .inp files.
- The Lovable version 1's main panel never converged: its 15-pass fixed-point loop amplified its own error (slope about f·L/D = 1.25 at its default), printed 30.3 ft/s (9.24 m/s) where the engines' root is 29.92 ft/s (9.120 m/s; feet are our conversion), and missed EPANET by as much as 149% across eight test pipes. The rewritten solver matches 51 engine results within 0.0003%.
- Nine test pipes, V1 to V9, in two engines: EPANET 2.2 (one solve at accuracy 10^-8, with Hazen-Williams, Darcy-Weisbach and Chezy-Manning) and EPA SWMM 5.2.4 (dynamic wave at a fixed 0.5 s step for two hours, as a CIRCULAR conduit and as a FORCE_MAIN under each equation). SWMM ran water only, having no viscosity input; the oil line ran in EPANET alone.
- 51 results, worst gap 0.0003%. The Verify tab recomputes every one of them in the browser against the stored engine flows.
- 27 exported .inp files round-tripped: written by the app, run by the engines, flows back within 0.00034% of the app's.
- Defects D1 to D10 in the Lovable source (solver, equation, zero-head case, transition rule, engine labels) and D11 to D19 from the outside review of v2.1 (EPANET fluid density, a lowest-pressure readout and liquid check, refused inputs, saved materials, keyboard and phone use, a redrawn figure, a complete verification suite), each listed on the Verify tab.

**Limits it states.** As the page lists it: no measured flow, so agreement proves the arithmetic matches the engines and not that any law describes a real pipe; one pipe, steady and full, with no networks, surges or partly full pipes; SWMM 6's column is the SWMM 5 number, justified by its source at one commit; liquid stays liquid or the app says so (it warns at the vapor pressure of water, about 0.34 psi absolute at 68 F) but models no cavitation; the laminar-turbulent transition band is a guess in every engine.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Bernoulli Flow in a Pipe (app)](../entities/bernoulli-flow-in-a-pipe.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Force main friction](../concepts/force-main-friction.md), [EPANET](../entities/epanet.md).

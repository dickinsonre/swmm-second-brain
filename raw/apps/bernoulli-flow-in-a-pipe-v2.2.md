---
name: Bernoulli Flow in a Pipe
file: bernoulli-flow-in-a-pipe.html
version: "2.2"
date: 2026-11-03
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/HWaPmxhYD3trZmFoAhMAFa", original: "Lovable app bernoulli-flow-in-pipe (version 1)", repo: none named in the page}
engines:
  - {name: EPANET, version: "2.2 (libepanet shipped in wntr 1.5.0)", note: "run while building; results stored in the page and recomputed against on the Verify tab"}
  - {name: EPA SWMM, version: "5.2.4 (swmm-toolkit 0.17.0)", note: "run while building, dynamic wave at a fixed 0.5 s step"}
  - {name: OpenSWMM 6, version: "commit 8c77aa8", note: "ForceMain.cpp and DynamicWave.cpp read, not run; no OpenSWMM code in the page"}
units: US customary by default, SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 24 October and 3 November 2026 under Robert Dickinson's direction, and that version 2.2 answers an outside review written by ChatGPT (OpenAI). See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/HWaPmxhYD3trZmFoAhMAFa, version 1793712264-3f89 (index.html, 1,633,130 bytes, SHA-256 d4c317a830642ce52db470c96f3f474b5894de42bac1bb00f774e5b63f6ba1c8), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Bernoulli Flow in a Pipe: two gauges, one pipe, three friction laws, checked against EPANET 2.2 and SWMM 5.2.4

## In three points
- **What:** A one-pipe lab: given the pressure at both ends, how much flows? It solves Bernoulli's energy balance with Darcy-Weisbach (Colebrook or Swamee-Jain), Hazen-Williams or Manning, shows velocity, flow, Reynolds number and an energy ledger that must close, and writes the same pipe as SWMM 5 and EPANET .inp files.
- **So what:** The Lovable version 1's main panel never converged: its 15-pass fixed-point loop amplified its own error (slope about f·L/D = 1.25 at its default), printed 30.3 ft/s (9.24 m/s) where the engines' root is 29.92 ft/s (9.120 m/s; feet are our conversion), and missed EPANET by as much as 149% across eight test pipes. The rewritten solver matches 51 engine results within 0.0003%.
- **Now what:** Use it to teach the energy balance and how SWMM and EPANET treat the same pressure pipe. Agreement with the engines checks arithmetic, not the friction laws: no measured flow, one steady full pipe, and SWMM 6 was read, not run.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v2.2 · 2026-11-03"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Lab, Engines, Verify, Ex. 2.4, Scenarios, Theory, About, Doc. Presets include a 6-in steel force main, the Lovable bench, a 12-in cast-iron main climbing 10 ft, a 1-in trickle in the transition band, a 2-in oil line, air at the Lovable default, and Ex. 2.4, a galvanized hydrant line read off an infographic Bob supplied. Pipe roughness, Manning n and Hazen-Williams C come from the Lovable table as shipped; the page notes the three laws describe three different pipes unless you make them agree. Export gives the .inp files.

## Checks (as stated on the page)

- Nine test pipes, V1 to V9, in two engines: EPANET 2.2 (one solve at accuracy 10^-8, with Hazen-Williams, Darcy-Weisbach and Chezy-Manning) and EPA SWMM 5.2.4 (dynamic wave at a fixed 0.5 s step for two hours, as a CIRCULAR conduit and as a FORCE_MAIN under each equation). SWMM ran water only, having no viscosity input; the oil line ran in EPANET alone.
- 51 results, worst gap 0.0003%. The Verify tab recomputes every one of them in the browser against the stored engine flows.
- 27 exported .inp files round-tripped: written by the app, run by the engines, flows back within 0.00034% of the app's.
- Defects D1 to D10 in the Lovable source (solver, equation, zero-head case, transition rule, engine labels) and D11 to D19 from the outside review of v2.1 (EPANET fluid density, a lowest-pressure readout and liquid check, refused inputs, saved materials, keyboard and phone use, a redrawn figure, a complete verification suite), each listed on the Verify tab.

## What this does not show

As the page lists it: no measured flow, so agreement proves the arithmetic matches the engines and not that any law describes a real pipe; one pipe, steady and full, with no networks, surges or partly full pipes; SWMM 6's column is the SWMM 5 number, justified by its source at one commit; liquid stays liquid or the app says so (it warns at the vapor pressure of water, about 0.34 psi absolute at 68 F) but models no cavitation; the laminar-turbulent transition band is a guess in every engine.

## How to reproduce

Export the .inp files from any preset and run them in EPA SWMM 5.2.4 and EPANET 2.2; compare with the Verify tab.

## Credits and licenses

EPA SWMM 5.2.4 source, public domain (forcmain.c, dwflow.c, consts.h, link.c); EPANET 2.2 source (hydcoeffs.c, input1.c), MIT License, Copyright (c) 2019, with the Dunlop transition polynomial ported from it; OpenSWMM 6 (HydroCouple), Apache-2.0, read at commit 8c77aa8, no code included; wntr 1.5.0 and swmm-toolkit 0.17.0; Swamee and Jain (1976); Colebrook (1939); EPANET 2.2 User Manual Table 3.2 for galvanized iron. The page's own code: © 2026 Robert Dickinson. EPA and HydroCouple do not endorse it.

## AI use

The page says: built with Claude, Anthropic's AI model, on 24 October 2026 under the direction of Robert (Bob) Dickinson, who built version 1 in Lovable, supplied its source and asked for an HTML app; responsibility is his. Claude read the Lovable source and ran its solvers verbatim, found and measured D1 to D10, rewrote the solver, read the SWMM 5, EPANET and OpenSWMM friction code, wrote the .inp exporters, built and ran the nine verification pipes, and wrote the page, the Doc and the .docx. Version 2.2 answers an outside review of v2.1 written by ChatGPT (OpenAI), which Bob supplied; Claude reproduced each finding and made the fixes D11 to D19. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.2 (2026-11-03): fixes D11 to D19 from an outside review of v2.1 (the version read).
- 2.1 (2026-11-03): Ex. 2.4 galvanized-iron pipe as a preset and tab, with a hand Colebrook-White check beside SWMM 5.2.4 and EPANET 2.2.
- 2.0 (2026-10-24): single-file edition; defects D1 to D10 fixed; engine verification; .inp export; Doc tab.
- 1 (Lovable): the original React app bernoulli-flow-in-pipe.

---
title: "S198: Two Engines, One Town, summary written from the page (version of 2026-11-02)"
type: source
raw: raw/apps/two-engines-one-town-v2026-11-02.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-17
tags: [apps, swmm5, epanet, coupling, python, javascript, verification]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Two Engines, One Town: working code for driving EPA SWMM 5.2.4 and EPANET 2.3 from Python and JavaScript, and a Coupling Lab that runs EPANET's Net1 into a sewer modeled in SWMM. Raw file: [raw/apps/two-engines-one-town-v2026-11-02.md](../../raw/apps/two-engines-one-town-v2026-11-02.md).

**How it was written. A summary written from the page.** The page ships no technical summary and no version number; the version is the date of its build session. Claude (Anthropic) wrote this file on 16 November 2026, at Bob's request, from the published artifact (version 1793635671-66a8) and its About and Doc tabs. No snippet or model was run. Bob has not read it (Q99). The page says it was built with Claude in a Claude Code session on 2 November 2026 at Bob's request, to bring an earlier answer up to date; Claude built both engines from source, wrote and ran every snippet, designed the sewer and ran the sweep.

**Claims worth keeping** (all copied from the page)
- The page says every snippet in it was run and every number measured, and that it replaces an earlier answer none of whose code ran (kept on its Old answer tab).
- Versions run: owa-epanet 2.3.5 (engine 20305); pyswmm 2.2.0; swmm-toolkit 0.17.0 (swmm engine 52004); wntr 1.5.0; epyt 2.3.5.3; swmm-api 0.4.74; swmmio 0.8.2; epanet-js 0.9.0; @swmmrs/swmmrs 0.2.0; openswmm 6.0.0a3; Python 3.12.3; Node v22.23.4; Ubuntu 24.04.5, gcc 13.3.0.
- The town is EPANET's Net1: nine junctions, a source reservoir, one pump and an elevated tank, demands in GPM, a two-hour pattern peaking at 1.6 times average. The sewer under it is invented for the app: nine manholes, nine pipes of 12 to 24 in at 0.2 percent with 8 ft of cover, n = 0.013, draining to a plant at node OUT.
- The sewer at manhole j receives a fraction R of the water delivered at junction j (R from 0.50 to 1.00). Demand fixed, or pressure-dependent (PDA, from EPANET 2.2) with minimum 0 psi and required 40 psi; between them the share rises with the square root of pressure.
- Route A: EPANET first, its delivered water into SWMM [DWF] and hourly [PATTERNS], SWMM once. Route B: both engines in lock-step through pyswmm and owa-epanet, handing water over every 60 seconds. Largest gap between them over day 3: 0.018 GPM at M = 1 and 0.057 GPM at M = 3.
- Normal demand: Net1 asks 1,100 GPM on average and gets all of it, every junction above 105 psi. With R = 0.85 the plant peaks at 1,455.9 GPM at 8:00. Over day 3, R times delivered water averages 935.0 GPM and the plant receives 935.0 GPM, 0.0004 percent apart.
- M = 2: the tank drains to its 100 ft floor and junction 32 falls to 13.4 psi. Fixed demand at M = 4: lowest pressure -861 psi; plant peak 5,629 GPM; at R = 1, 0.483 million gallons lost to flooding on day 3. PDA at M = 3: 78 % of demand delivered; plant peak levels near 2,546 GPM; no pipe more than 88 % full. The sweep was 16 EPANET and 176 SWMM runs.
- Six routes to EPANET on 225 pressures (nine junctions, 24 hours), each against owa-epanet: epanet-js 1.5e-08 psi; EPyT 7.4e-06; WNTR with its bundled EPANET 2.2 3.1e-05 (runepanet the same); WNTR's own Python solver 9.6e-05. The page puts the differences down to float32 storage.
- The check caught the page's own first WNTR snippet, which converted with 1 psi = 0.70307 m; EPANET uses 0.4333 psi per foot of head (PSIperFT in types.h); the mismatch was up to 0.07 psi.
- "Three SWMM engines produce identical numbers."

**Limits it states.** One water network and one invented sewer. No lateral travel time, no infiltration or inflow, no rain, a constant return factor. The coupling runs one way. OpenSWMM 6 was tested only as a drop-in engine on this model. No MATLAB, R, C# or Windows runs. No field data. No person has reviewed the snippets, the sewer design or the text.

**Checked at ingest.** 0.85 x 1,100 = 935.0 GPM, the day-3 average quoted. 9 x 25 = 225 only if hour 24 is counted; the page says "every hour of Net1's 24-hour run", which gives 25 time points from 0 to 24 hours.

**Feeds:** [Two Engines, One Town (app)](../entities/two-engines-one-town.md), [EPANET](../entities/epanet.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).

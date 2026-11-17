---
name: Two Engines, One Town
file: two-engines-one-town.html
version: 2026-11-02
date: 2026-11-02
written: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/4qVQv1VRhT9vo8icmBuZn1", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: "5.2.4 (swmm engine 52004 in swmm-toolkit 0.17.0)", source: "USEPA/Stormwater-Management-Model tag v5.2.4", license: public domain}
  - {name: EPANET, version: "2.3.5 (epanet engine 20305 in owa-epanet)", source: "OpenWaterAnalytics/EPANET tag v2.3.5", license: not stated in the page}
  - {name: OpenSWMM, version: 6.0.0a3, note: "tested only as a drop-in engine on the one model"}
units: US customary (GPM, ft, psi, million gallons)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page's own AI-use note says it was built with Claude at Bob Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/4qVQv1VRhT9vo8icmBuZn1, version 1793635671-66a8 (index.html, 1,957,874 bytes, SHA-256 3f49d78c018aa3878499603a66d4a1a2f3e312e2e249494117dff4083d7d7db8), its About and Doc tabs read in headless Chromium on 2026-11-16. No snippet or model was run to write this file."
---

# Two Engines, One Town: driving EPA SWMM 5.2.4 and EPANET 2.3 from code, and coupling them

## In three points
- **What:** Working code for driving EPA SWMM 5.2.4 and EPANET 2.3 from Python and JavaScript, with a lab that couples EPANET's Net1 to a sewer laid under it.
- **So what:** Six routes to EPANET agree on 225 pressures to within 9.6e-05 psi, and the coupled run sends 935.0 GPM and receives 935.0 GPM over day 3, a difference of 0.0004 percent.
- **Now what:** Copy the snippet for the route the Overview chooser names. The sewer is invented for the app, the coupling runs one way, and there is no field data.

This summary was written after the fact. The page ships no technical summary and no version number of its own, so the version above is the date of its build session. Every number below is copied from the page's About tab or its Doc essay. No snippet or model was run to write this file.

## What it does

A working reference for driving EPA SWMM 5.2.4 and EPANET 2.3 from code in November 2026. The page says every snippet in it was run and every number measured, and that it replaces an earlier answer, none of whose code ran. Its Coupling Lab runs EPANET's Net1 into a sewer modeled in SWMM. Tabs: Overview (a chooser that names a route for what you want to do), Code (every verified snippet with its output, versions and run time), Coupling Lab, Verify, Old answer, About, Doc.

## Versions run (from the page)

owa-epanet 2.3.5; pyswmm 2.2.0; swmm-toolkit 0.17.0; wntr 1.5.0; epyt 2.3.5.3; swmm-api 0.4.74; swmmio 0.8.2; numpy 2.5.4; pandas 3.1.0; python 3.12.3; node v22.23.4; epanet-js 0.9.0; @swmmrs/swmmrs 0.2.0; swmm engine in swmm-toolkit 52004; epanet engine in owa-epanet 20305; openswmm 6.0.0a3; Ubuntu 24.04.5 LTS, gcc 13.3.0, x86-64 cloud container.

## How it computes

- The sewer at manhole j receives a fraction R (the return factor) of the water delivered at junction j; the Lab lets R run from 0.50 to 1.00.
- Demand is fixed or pressure-dependent (PDA, from EPANET 2.2): below a minimum pressure a junction gets nothing, above a required pressure it gets everything, in between a share that rises with the square root of the pressure. Here the minimum is 0 psi and the required pressure is 40 psi.
- The town is EPANET's Net1: nine junctions, a source reservoir, one pump and an elevated tank, demands in GPM, a two-hour pattern peaking at 1.6 times average. The sewer under it is invented for the app: nine manholes, nine pipes from 12 to 24 inches at 0.2 percent slope with 8 ft of cover, n = 0.013, draining to a plant at node OUT.
- Route A (the Lab's): EPANET runs first, its delivered water goes into SWMM [DWF] and hourly [PATTERNS], SWMM runs once. Route B: both engines in lock-step through pyswmm and owa-epanet, handing water over every 60 seconds.

## Results the page reports

- Normal demand: Net1 asks for 1,100 GPM on average, gets all of it, and keeps every junction above 105 psi. With R = 0.85 the plant peaks at 1,455.9 GPM at 8:00.
- Continuity over day 3: R times delivered water averages 935.0 GPM; the plant receives 935.0 GPM; they differ by 0.0004 percent.
- Demand multiplier M = 2: the tank drains to its 100-foot floor and junction 32 falls to 13.4 psi.
- Fixed demand at M = 4: lowest pressure -861 psi; the plant peak climbs to 5,629 GPM; at R = 1 SWMM reports 0.483 million gallons lost to flooding on day 3.
- PDA at M = 3: the town receives 78% of what it asked for; the plant peak levels off near 2,546 GPM; no pipe runs more than 88% full anywhere in the sweep.
- The coupling sweep was 16 EPANET and 176 SWMM runs.

## Checks (as stated on the page)

- Six routes to EPANET, 225 pressure values (nine junctions, every hour of Net1's 24-hour run), each compared with owa-epanet: epanet-js agrees to 1.5e-08 psi; EPyT to 7.4e-06 psi; WNTR with its bundled EPANET 2.2 to 3.1e-05 psi, and the runepanet console program read from its .out the same; WNTR's own Python solver to 9.6e-05 psi. The differences are float32 storage, not hydraulics.
- The check caught the page's own first draft of the WNTR snippet, which converted metres to psi with 1 psi = 0.70307 m; EPANET uses 0.4333 psi per foot of head (PSIperFT in types.h). The mismatch was up to 0.07 psi.
- Three SWMM engines produce identical numbers.
- Route A against route B over day 3: largest gap 0.018 GPM at M = 1 and 0.057 GPM at M = 3.
- A parity test of the page's .inp writer against the Python one. All checks are mechanical; the page says no person has yet reviewed the snippets, the sewer design or the text.

## What this does not show

- One water network and one invented sewer. Net1 is a teaching model; the sewer was laid for this app.
- No travel time in house laterals, no infiltration or inflow, no rain, and a return factor constant all day and all year.
- The coupling runs one way: nothing in the sewer can change the water system.
- OpenSWMM 6 was tested only as a drop-in engine on this model; none of its new features were exercised.
- No MATLAB, R, C# or Windows runs. No field data.

## How to reproduce

The page names its verification kit: lab.py (EPANET to SWMM coupling), runall.py (snippets, comparisons, sweep; it rewrites results.json, which the page embeds), rerun_snips.py (OpenSWMM in its own environment) and figs.py (figures). The kit is not shipped inside the page. The Coupling Lab's "Save sewer .inp" writes the sewer model for the settings on screen, ready for SWMM 5.2.4.

## Credits and licenses

EPA SWMM source (tag v5.2.4) and update notes (August 2023); OWA EPANET (tag v2.3.5) and release notes; pyswmm, swmm-toolkit, swmm-api, swmmio, OpenSWMM engine, swmmrs, owa-epanet, WNTR, EPyT, epanet-js; the PySWMM paper (Journal of Open Source Software).

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude Code session on 2 November 2026, at Bob Dickinson's request to bring an earlier answer up to date as an app with a Doc tab and a .docx. Claude installed the packages, built EPA SWMM 5.2.4 and EPANET 2.3.5 from source, wrote and ran every snippet, designed the invented sewer under Net1, ran the coupling sweep, and wrote the scripts, page, figures and essay. This summary was written by Claude on 16 November 2026 from the published page.

## Changes

- 2026-11-02: first version as an app; replaces an earlier answer (shown on the Old answer tab).

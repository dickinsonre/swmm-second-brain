---
title: "S320: Manning's n Explorer, summary written from the page (v3.1)"
type: source
raw: raw/apps/mannings-n-explorer-v3.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, mannings-n, solvers, routing, audits]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Manning's n Explorer, version 3.1: how Manning's n travels between solvers. Raw file: [raw/apps/mannings-n-explorer-v3.1.md](../../raw/apps/mannings-n-explorer-v3.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/21oNHReNNirWG8L5zo6XPo, version 1792897236-6626 (index.html, 2,420,594 bytes, SHA-256 8491b35d628c32a1289f88ff06395a8d4319ced64aabea0508fc050c8ed9b5d6), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: the write-up and the single-file edition were produced with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and set the requirements; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A workbench for one idea: a calibrated Manning's n is the number that made one program, grid and time step reproduce one set of high-water marks, so copying it into another solver can count some losses twice. It lines up thirty solvers by what they resolve (turbulence, sub-grid topography, numerical diffusion), gives a starting-point estimate for transferring n without calibration data, routes a flood wave, and walks through calibration. Single-file edition of Bob's Lovable app.
- Reading all 5,559 source lines turned up thirteen code defects, four of which changed what the app teaches. The Flood Wave tab routed through a single sub-reach, so all three curves peaked at 8.0 hours with 0.08%, 0.04% and 0.02% attenuation and there was nothing to watch; the Muskingum-Cunge routine used half the diffusion it printed; and both stage models ran backwards (raise n and the water surface went down).
- All 5,559 lines of the source read and every formula pulled into a Node test: thirteen code defects, listed on the Audit tab.
- Muskingum-Cunge diffusion checked against Ponce's form, D = q/(S0·c·Δx) = 2ν/(c·Δx).
- SWMM5 statements checked against the EPA SWMM 5.2.4 source files, and vendor statements against their documentation.

**Limits it states.** As the page lists it: no solver was run (not TUFLOW, ICM, HEC-RAS or SWMM5); the grades and purity percentages are judgements from the original app, five of them justified by scheme descriptions this edition had to correct; the routing has no floodplain storage, lateral spreading or backwater; kinematic routing has nothing to say above the depth where the pipe's discharge curve peaks; the transfer tools give starting points, not answers.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Manning's n Explorer (app)](../entities/mannings-n-explorer.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Force main friction](../concepts/force-main-friction.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).

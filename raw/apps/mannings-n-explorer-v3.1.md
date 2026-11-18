---
name: Manning's n Explorer
file: mannings-n-explorer.html
version: "3.1"
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/21oNHReNNirWG8L5zo6XPo", original: "Lovable project mannings-n-explorer (React/Vite)", repo: none named in the page}
engines: none (Muskingum-Cunge routing and transfer calculators written for the page; no solver among the thirty listed was run)
units: US customary (ft, cfs)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was produced with Claude in October 2026 under Robert Dickinson's direction, with a research subagent for part of the vendor checks. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/21oNHReNNirWG8L5zo6XPo, version 1792897236-6626 (index.html, 2,420,594 bytes, SHA-256 8491b35d628c32a1289f88ff06395a8d4319ced64aabea0508fc050c8ed9b5d6), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Manning's n Explorer: how Manning's n travels between solvers

## In three points
- **What:** A workbench for one idea: a calibrated Manning's n is the number that made one program, grid and time step reproduce one set of high-water marks, so copying it into another solver can count some losses twice. It lines up thirty solvers by what they resolve (turbulence, sub-grid topography, numerical diffusion), gives a starting-point estimate for transferring n without calibration data, routes a flood wave, and walks through calibration. Single-file edition of Bob's Lovable app.
- **So what:** Reading all 5,559 source lines turned up thirteen code defects, four of which changed what the app teaches. The Flood Wave tab routed through a single sub-reach, so all three curves peaked at 8.0 hours with 0.08%, 0.04% and 0.02% attenuation and there was nothing to watch; the Muskingum-Cunge routine used half the diffusion it printed; and both stage models ran backwards (raise n and the water surface went down).
- **Now what:** Use it to think before you copy an n between models. No solver was run; the grades and purity percentages are judgements carried over from the original app, and the routing is Muskingum-Cunge on a prismatic wide channel at fixed depth.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v3.1 single-file edition · 24 October 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: The Problem, Solvers, Report Card, n-Calculator, Flood Wave, n-Transfer, Partitioning, Calibration, What To Do, Audit, About and Doc. The Flood Wave tab now routes the whole reach as a cascade of sub-reaches. The Routing slider stops at a depth ratio of 0.9: in a circular conduit the kinematic celerity ratio is 1.33 at half depth, 1.03 at 80% depth and zero near 94%, where the discharge curve peaks, while the original's fitted formula reported 1.22 at 80% and 1.08 at 95%. Export menu for tables and the essay.

## Checks (as stated on the page)

- All 5,559 lines of the source read and every formula pulled into a Node test: thirteen code defects, listed on the Audit tab.
- Muskingum-Cunge diffusion checked against Ponce's form, D = q/(S0·c·Δx) = 2ν/(c·Δx).
- SWMM5 statements checked against the EPA SWMM 5.2.4 source files, and vendor statements against their documentation.

## What this does not show

As the page lists it: no solver was run (not TUFLOW, ICM, HEC-RAS or SWMM5); the grades and purity percentages are judgements from the original app, five of them justified by scheme descriptions this edition had to correct; the routing has no floodplain storage, lateral spreading or backwater; kinematic routing has nothing to say above the depth where the pipe's discharge curve peaks; the transfer tools give starting points, not answers.

## Credits and licenses

Robert Manning (1889); Strickler (1923); Ven Te Chow (1959); Ponce's Muskingum-Cunge form; EPA SWMM 5.2.4 source; the vendors' documentation for TUFLOW, ICM and HEC-RAS. MIT © 2026 Robert Dickinson, as stated in the footer (SWMM5.org).

## AI use

The page says: the write-up and the single-file edition were produced with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and set the requirements; responsibility is his. Claude read and ported the source, wrote the fixes, checked the SWMM5 statements against the EPA SWMM 5.2.4 source and the vendor statements against their documentation (partly through a research subagent), drew the figures and drafted the essay. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 3.1 (2026-10-24): single-file edition with thirteen defects fixed (the version read).
- Earlier versions: the Lovable app.

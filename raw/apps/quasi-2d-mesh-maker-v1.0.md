---
name: Quasi-2D Mesh Maker for SWMM5
file: quasi-2d-mesh-maker.html
version: "1.0"
date: 2026-10-04
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/ThYoHcuNTUPPDWC9qpKBnk", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "built from source and run outside the page on files this generator wrote (4 Oct 2026); no engine runs in the page", license: public domain}
units: US customary (ft, CFS, GPM, MGD) with an SI switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/ThYoHcuNTUPPDWC9qpKBnk, version 1791108486-b603 (index.html, 123,410 bytes, SHA-256 739045f9589fc00c1909c3cda83fb3cfdfa11429c848e780e997a115f2b091ba), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Quasi-2D Mesh Maker for SWMM5: boundary and ground surface in, a runnable overland-flow mesh (.inp) out

## In three points
- **What:** Draw the area that can flood and what water cannot cross, give it a ground surface (planes, a street valley, a sag, rolling ground, a DEM or survey points), and get a PCSWMM-style quasi-2D overland mesh as a SWMM5 .inp, with links to a 1D sewer.
- **So what:** Its storage-exact mesh (half-width links that hold exactly the cell area) measured stored area / plan area = 1.000 in EPA SWMM 5.2.4 and reached the steady sheet-flow depth on time, where the plain width rule reached the same depth late.
- **Now what:** Use the storage-exact rule for any quasi-2D mesh and read link velocities knowing they show twice the sheet-flow velocity. No comparison with a 2D shallow-water solver or PCSWMM's own width rule.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-04"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Steps: Domain, Mesh, Water in / out, Sewer link, Export, Verified. Obstructions remove the cells inside them, and a 2D conduit is dropped when the line between two cell centres crosses an edge, so thin walls block flow. Cells short of a link become storage nodes carrying the remainder. Whole cells cover 97% of the area inside the boundary (cells are not clipped). The .inp opens in EPA SWMM 5.2, PCSWMM or any SWMM5 reader.

## Checks (as stated on the page; EPA SWMM 5.2.4 built from source, 4 Oct 2026)

- Storage: stored area / plan area = 1.000 for the storage-exact mesh; halving n keeps the discharge.
- Sheet flow, 4 in/hr on a 1% plane, 200 x 400 ft, n = 0.03: both width rules reach the same steady depth; only the storage-exact mesh gets there on time (kinematic time of concentration 9.5 min); partial and full inertial damping gave identical rows.
- Continuity, rain as subcatchments or as direct inflow: hexagonal 286 cells -0.07% and 0.00%; rectangular 256 cells -0.08% and -0.02% (volumes read from the .rpt, plus or minus 22 ft3).
- Subcatchment polygons: 20,000 random points, none inside more than one polygon.

## What this does not show

- PCSWMM's own width rule, agreement with a 2D shallow-water solver, or diagonal-flow behaviour.

## How to reproduce

Open the page, build a mesh and export the .inp; the Verified tab lists the engine runs.

## Credits and licenses

EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-10-04): first version.

---
name: Walk the Mesh
file: walk-the-mesh.html
version: "1.0"
date: 2026-10-19
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/6ZJVfC6AgbMFTAzRuPy3Rh", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA commit 7952ca8, compiled to wasm32-wasi with wasi-sdk 24, module sha256 beginning cd3f7b8b8764f981", license: public domain}
units: US customary (ft, ac, cfs, ft/s)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built, tested and written with Claude under Bob Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/6ZJVfC6AgbMFTAzRuPy3Rh, version 1792425948-1977 (index.html, 6,329,421 bytes, SHA-256 22368ed27907bdc97103acc97c1ff8f42bc17e03fb3077dc005095bc7df43d5f), every tab read in headless Chromium on 2026-11-17 (the page has Notes and Essay tabs, no About or Doc). No model was run to write this file; the date is the artifact's publish date."
---

# Walk the Mesh: the Clairaut 4D-surface walk, adapted to SWMM5 quasi-2D modeling

## In three points
- **What:** You stand inside a SWMM 2D mesh (a grid of junctions, storage and conduits) and the view shows where a surge launched from you would be after each second; the page then runs EPA SWMM 5.2.4 in the browser on the same mesh for surge and flood runs.
- **So what:** A point surge reaches each cell at the wave-ray travel time (slope 0.99 to 1.02 over five still-water worlds) only on a mesh that stores the right water; the obvious quasi-2D mesh in SWMM 5.2.4 stores twice as much, so waves arrive a factor of 1.414 too late.
- **Now what:** Check a quasi-2D mesh's storage before trusting its timing; the Mesh check tab shows the code lines and a fix (Manning's n times 0.841). No buildings, pipes, infiltration or other mesh tools are covered.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0 · EPA SWMM 5.2.4"); the date is the artifact's. The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

Adapted from a Perplexity "Clairaut" app about walking on a 4D surface. Worlds: flat lake, round pond, island, ring reef, shoal lens, and two floods (valley floodplain, twin hollows). Meshes from 30 x 30 to 80 x 80 cells on a 600 x 600 ft domain (8.26 ac); at 60 x 60 cells of 10 ft, 3,600 junctions and storage and 7,080 conduits; wave speeds 1.3 to 15.0 ft/s. Walk with W A S D or ride a ray. Flood runs show depth, speed, hazard (combined H1 to H6 classes, AIDR Guideline 7-3, used by ARR 2019, converted from SI) and arrival time per cell. Tabs: Walk the mesh, Run SWMM5, Mesh check, Notes, Essay.

## Checks (as stated on the page)

- Surge arrival: a point surge reaches each cell at the wave-ray travel time, slope 0.99 to 1.02 across the five still-water worlds, on a mesh that stores the right water; the obvious mesh stores twice as much, so waves arrive a factor of the square root of 2 (1.414) too late. The fix multiplies Manning's n by 2^(-1/4) = 0.841.
- Lake at rest, 120 s on the pond, island, reef and shoal beds: max |Q| = 0.000 cfs on all four (engine).
- Every [COORDINATES] entry scrambled: .out byte-identical (9.18 MB).
- Steady sheet flow on a 1% plane against Manning normal depth: area-true mesh +2.9 to +4.1%, plain mesh +2.2 to +3.9%.
- WebAssembly against a native gcc build: byte-identical .out for fixed-step surges; variable-step flood max-depth envelope within 0.0007 ft with equal continuity.
- The code lines behind the storage finding are quoted verbatim from tag v5.2.4 with their line numbers.

## What this does not show

- Current-carried waves, infiltration, buildings, pipes, or any mesh tool other than this page's generator; the Notes tab has the full list.

## How to reproduce

Open the page, pick a world and mesh, walk, then use Run SWMM5 on the same mesh; Export writes the .inp.

## Credits and licenses

EPA SWMM 5.2.4 (public domain). The idea: the Clairaut app. No license is stated for the page.

## AI use

The page says it was built, tested and written with Claude (Anthropic) under Bob Dickinson's direction; its Notes tab says what Claude did, how it was checked and what has not been checked. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.

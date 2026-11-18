---
name: Hedron Walk
file: hedron-walk.html
version: 1.7.0
date: 2026-10-31
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/WCkkGP8dx93nK786rJ5JbM", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "compiled to WebAssembly, runs in the page", license: public domain}
units: US customary (ft, ac, cfs, ac-ft, in)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Claude Opus 5.5) under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/WCkkGP8dx93nK786rJ5JbM, version 1793467105-9cfa (index.html, 3,251,702 bytes, SHA-256 ee4dc7d33ba2f86306583349d39baaff97b0e6183e1c11e40752744b9bdeac4d), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file; the date is the artifact's publish date."
---

# Hedron Walk: a SWMM5 network generator built from two pictures

## In three points
- **What:** Turns a picture of a winding path tiled with triangles (and a second, the Mobius gimbal) into a SWMM5 model: a ribbon about 3,600 ft by 300 ft of 1,408 subcatchments, 21 trunk pipes, a vortex chamber, a ring pond, an orifice, a weir and two outfalls, run on EPA SWMM 5.2.4 in the page.
- **So what:** The picture's labels (count 4^k, length 1/2^k) hold exactly, the 1,408 subcatchments add to 24.69 ac with no overlap, and the default storm sends 2.526 of 4.115 ac-ft to runoff with the pond inflow peaking at 28.5 cfs.
- **Now what:** Use it to make valid, non-overlapping test networks with a known geometry. Pipes are sized by the rational method on a synthetic storm; the networks are not designs.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.7.0"); the date is the artifact's. The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

A hedron is a triangle from repeated midpoint splitting: at level k its edge is 1/2^k of the base and one base triangle holds 4^k of them; the centre child is the parent turned 180 degrees about its centroid and halved. Rule 30 decides which triangles are paved. The generator builds a ribbon about 3,600 ft long and 300 ft wide: 1,408 subcatchments, 21 trunk pipes, a vortex chamber, a ring pond, an orifice, a weir and two outfalls. The trunk has one junction per base triangle, sized by Q = CiA at the storm's peak intensity and Manning's full-pipe flow at n = 0.013, rounded up and never shrinking downstream. The storm is a triangular hyetograph, 2 in in 2 hours peaking at 2 in/hr at 45 minutes, in five-minute blocks; dynamic wave routing. Tabs: Walk, Network, 3D, Wave, Run, Hedrons, Rule 30, Verify, About, Doc.

## Results the page reports

- Default ribbon: 4.115 ac-ft of rain on 24.69 ac, 2.526 ac-ft of runoff (about 61 percent); inflow to the ring pond peaks at 28.5 cfs about 1 h 05 min in; the pond rises to 3.84 ft of its 8.00 at about 1 h 50 min; its orifice peaks at 7.5 cfs.
- Three Rule 30 carpets pave 49.9, 49.8 and 49.6 percent; runoff 2.526, 2.522 and 2.514 ac-ft; pond inflow peaks 28.5, 28.4 and 28.3 cfs. Over four seeds imperviousness stays between 49.9 and 50.2 percent.

## Checks (as stated on the page)

- Counts: 4^k hedrons per base triangle at each level, counted.
- Addresses: every residue names exactly one hedron, no gaps or collisions.
- Parity: the bit matches the way each hedron points, at every level.
- Half-turn: the centre child equals the parent under the half-turn map to 9 x 10^-13 ft.
- No overlap: every face and subcatchment keeps positive area, the outline never crosses itself, and the tightest bend, 284 ft, exceeds the 150 ft half-width.
- Area: subcatchments add to 24.69 ac, the same as the faces drawn, within 0.02 percent of the smooth outline.

## What this does not show

- A design: sizing is rational method on a synthetic storm.
- The picture's text about quantum computing plays no part.

## How to reproduce

Open the page, set the sliders on Walk, and run on Run; Export writes the .inp; Record WebM records a walkthrough.

## Credits and licenses

EPA SWMM 5.2.4 (public domain). The 3D view follows the conventions of Bob's SWMM5 Benchmark 3D Viewer. No license is stated for the page.

## AI use

The page says Hedron Walk was built with Claude (Claude Opus 5.5, Anthropic's AI model) in a claude.ai session on 27 October 2026, under the direction of Robert (Bob) Dickinson, who supplied the picture and its text and asked for a SWMM5 .inp generator that looks like it. Claude chose how to read the picture's numbers as geometry (discarding a first, self-similar spiral reading), and wrote the generator, the .inp writer, the checks, the page and its later views. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.7.0: current version, with the Mobius gimbal as a second picture.
- 1.1 to 1.3: network map, 3D view, Wave view.
- First version: 27 October 2026.

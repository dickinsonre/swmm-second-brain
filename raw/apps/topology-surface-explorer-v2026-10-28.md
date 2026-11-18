---
name: Topology Surface Explorer
file: topology-surface-explorer.html
version: 2026-10-28
date: 2026-10-28
written: 2026-11-18
author: "Robert Dickinson (supplied the file; the file itself carries no author line, license or version number)"
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/LbcjojQQ5EWzsAecUWvXnZ", repo: none}
engines: none (a surface classifier and 3D views; three.js 0.160.0 and its addons load from jsDelivr)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says this edition was made with Claude (Claude Opus 5.5) on 28 October 2026 at Robert Dickinson's request, by importing a file he supplied. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/LbcjojQQ5EWzsAecUWvXnZ, version 1793230423-cf1e (index.html, 286,517 bytes, SHA-256 c9d2186aaafce1c5f0c1839d6377ef1199c1c7b9540770ad78cc373d03bf6408), its markup read on 2026-11-18 (its 3D module did not load in headless Chromium without the network). Nothing was run to write this file."
---

# Topology Surface Explorer: surfaces built by gluing the edges of a polygon

## In three points
- **What:** An interactive explorer for surfaces built by gluing the edges of a polygon. Type a gluing word such as aba'b' and the app names the surface, computes its Euler characteristic, orientability and boundary count, reduces the word to normal form step by step, and shows the surface as a polygon, a 3D model, a hyperbolic tiling, a walk and a kart race. Not a water-modeling app.
- **So what:** An independent surface classifier written for the check agrees with the app on 21 of 21 words; all 25 invariant checks printed during six step-by-step reductions read "Surface unchanged"; straight-walk crossing counts match hand predictions on all five flat surfaces. One known issue: on a curved surface the Walk tab's "straight-line distance from start" loses accuracy after about 25 units of walking and is off by up to 0.28 at 36 units (the walking itself is unaffected).
- **Now what:** Use it to learn the classification of surfaces by playing with words. The essay, its history and figures, and the 3D models, hyperbolic drawings and kart physics have not been checked by a person.

This summary was written after the fact. The page ships no technical summary of its own. It gives no version number; the date above is the import date the page states. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Glue & classify, Walk a surface, 3D gallery, Kart race, About, Doc. Edges are read counter-clockwise; a label used twice is glued, used once it stays as boundary; a' (or a⁻¹, a^-1, A) is the inverse. The 3D gallery and surfaces load three.js 0.160.0 and its examples/jsm addons from jsDelivr, so those views need a network.

## Checks (as stated on the page)

- The supplied file run unmodified in a headless browser to collect every number in the Doc.
- An independent surface classifier against the app on 21 words: 21 agree.
- 25 invariant checks during six reductions; crossing counts on five flat surfaces against hand predictions; a control test of the hyperbolic drawing.
- The same data collection re-run on the edited file returned identical numbers.

## What this does not show

As the page lists it: the Walk distance readout error on curved surfaces (measurements, cause and the responsible line of code are in the Doc); no person has checked the essay text and its history, the figures, the 3D models, the hyperbolic drawings or the kart physics.

## Credits and licenses

Imported on 28 October 2026 from the single file "Topology surface explorer (single file).html" supplied by Robert Dickinson, SHA-256 b4293bd1100e9dcfaf444cf172a8bb9af6865d45314a8a965d3157aeb7f84fdc; the file carries no author line, license or version number. three.js 0.160.0 (MIT).

## AI use

The page says: this edition was made with Claude, Anthropic's AI model (Claude Opus 5.5), on 28 October 2026 at the request of Robert (Bob) Dickinson, who supplied the app file and asked for it to be imported; responsibility for publishing it is his. No line of the app's own code was changed: Claude removed the outer document tags, added a dark-theme line, the About and Doc tabs and a wrapping tab bar, retitled the page, ran the file to collect the Doc's numbers, and wrote an independent classifier to check it. This summary was written by Claude on 18 November 2026 from the published page; its tabs were read from the page's markup, because its 3D module failed to load in the reading machine without the network.

## Changes

- 2026-10-28: imported as an artifact with About and Doc tabs (the version read).

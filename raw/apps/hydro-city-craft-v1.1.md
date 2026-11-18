---
name: Hydro City Craft
file: hydro-city-craft.html
version: "1.1"
date: 2026-10-26
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/6rvKezyDXceKe8PK1EgHTe", original: "Lovable project hydro-city-craft (React, Three.js, Leaflet; MIT)", repo: "https://github.com/SWMMEnablement/hydro-city-craft"}
engines: none (an independent JavaScript rasterizer, core.js; the water is a bookkeeping depth from Schueler's Simple Method, not a hydraulic run)
units: US customary (ft, in); Minecraft blocks at 5 ft per block for the original's flood levels
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in one session on 24 to 26 October 2026 under Robert Dickinson's direction, and that version 1.1 answers an outside review of 1.0. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/6rvKezyDXceKe8PK1EgHTe, version 1793022744-50e0 (index.html, 2,508,705 bytes, SHA-256 26fd34ffe3337a15acf267e0909603de14c55591c420e429a011b3c1268f06a0), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Hydro City Craft: OpenStreetMap streets and water built in Minecraft blocks

## In three points
- **What:** Turns a box of the real world from OpenStreetMap into a Minecraft world: buildings extruded from their footprints, streets painted by class, rivers, canals and lakes filled in. View it in 3D, click a building to see where its height came from, raise the water, and take it into the game as a WorldEdit schematic (Sponge Schematic version 2, Java Edition 1.20.4) or a ready-to-install data pack.
- **So what:** Version 1.0 measured impervious cover in Minecraft blocks, so a coarser grid meant wider streets: Manhattan's ponding went from 12.60 in at grid 64 to 9.26 in at grid 256. Version 1.1 measures it on its own grid of 6.6-ft squares with roads at real widths, and gives 8.29 in at every grid size. Thirty defects are listed with the lines that caused them: twenty in the Lovable build and ten in version 1.0, found by an outside review.
- **Now what:** Use it to teach imperviousness and runoff on a city you can walk through in the game. The ground is flat, there are no pipes, and the water is uniform ponding under stated closed-basin assumptions, not a forecast and not a bound.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("What changed in 1.1 (26 October 2026)"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Build, Water, Census, Defects, About, Doc. Pick a box (search runs on Enter, at most one request a second, cached, as Nominatim's usage policy asks), generate it, view it in 3D or on the map, and export. Each Generate is a job that can be cancelled; data that returns for a box no longer selected is not built. Three.js, OrbitControls and Leaflet are inside the file; Manhattan and Venice carry embedded OpenStreetMap extracts, so the page works offline. The Water tab spreads one storm's runoff (Simple Method, every storm counted, Pj = 1) uniformly over open ground.

## Checks (as stated on the page)

- The Lovable TypeScript compiled unchanged (one import line altered for the bundler) and run beside the new engine on the same synthetic city and on the Manhattan and Venice snapshots: twenty checks pass, thirteen of them comparing the engines.
- Read-back of the exports by independent parsers; every command line expanded back into blocks.
- Each of the outside review's eight points reproduced before it was fixed; two multipolygon bugs fixed (a waterway that is also a lake's outer ring no longer fills the island; an unclosed ring is reported and skipped).

## What this does not show

As the page lists it: the ground is flat, with no elevation model, so the flood fills like a bathtub; no sewers, inlets, outfalls or infiltration after the rain (the street-drain gutters and ponds are decoration and say so); one storm spread evenly; impervious means mapped, at assumed road widths by class unless OSM has a width tag.

## Credits and licenses

OpenStreetMap contributors; Nominatim; Sponge Schematic Specification version 2 (SpongePowered); Three.js, OrbitControls, Leaflet; Schueler's Simple Method. Arnis (github.com/louis-e/arnis) is a separate Rust program; this app is an independent JavaScript rasterizer. The Lovable hydro-city-craft is MIT, © 2026 Robert Dickinson.

## AI use

The page says: built with Claude, Anthropic's AI model, in one Claude session on 24 to 26 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for a single-file HTML app, and on 26 October supplied an outside review of version 1.0, which version 1.1 answers; responsibility is his. Claude read the Lovable source and its handover notes, found the first twenty defects, reproduced each review point before fixing it, and wrote the page, the engine (core.js), the 3D and map views, the exports, the tests, the defect register, the Doc essay and its .docx. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.1 (2026-10-26): answers an outside review of 1.0 (grid-independent hydrology, multipolygon fixes, offline libraries, cancellable jobs, a data pack) (the version read).
- 1.0 (2026-10-24): single-file edition with the Lovable build's twenty defects fixed.

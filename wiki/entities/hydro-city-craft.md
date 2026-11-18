---
title: "Hydro City Craft (app)"
type: entity
updated: 2026-11-18
sources: [S363]
tags: [apps, openstreetmap, minecraft, impervious-cover]
reviewed: no
---
Bob's app Hydro City Craft: OpenStreetMap streets and water built in Minecraft blocks. Version 1.1, 2026-10-26 [S363](../sources/S363-hydro-city-craft-summary.md). Its `links:` line names no live Netlify address [S363](../sources/S363-hydro-city-craft-summary.md).

**A caution about its source.** The page ships no technical summary. [S363](../sources/S363-hydro-city-craft-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S363](../sources/S363-hydro-city-craft-summary.md)
- Turns a box of the real world from OpenStreetMap into a Minecraft world: buildings extruded from their footprints, streets painted by class, rivers, canals and lakes filled in. View it in 3D, click a building to see where its height came from, raise the water, and take it into the game as a WorldEdit schematic (Sponge Schematic version 2, Java Edition 1.20.4) or a ready-to-install data pack.
- Version 1.0 measured impervious cover in Minecraft blocks, so a coarser grid meant wider streets: Manhattan's ponding went from 12.60 in at grid 64 to 9.26 in at grid 256. Version 1.1 measures it on its own grid of 6.6-ft squares with roads at real widths, and gives 8.29 in at every grid size. Thirty defects are listed with the lines that caused them: twenty in the Lovable build and ten in version 1.0, found by an outside review.
- The Lovable TypeScript compiled unchanged (one import line altered for the bundler) and run beside the new engine on the same synthetic city and on the Manhattan and Venice snapshots: twenty checks pass, thirteen of them comparing the engines.
- Read-back of the exports by independent parsers; every command line expanded back into blocks.
- Each of the outside review's eight points reproduced before it was fixed; two multipolygon bugs fixed (a waterway that is also a lake's outer ring no longer fills the island; an unclosed ring is reported and skipped).

**How to use it, as the summary puts it.** Use it to teach imperviousness and runoff on a city you can walk through in the game. The ground is flat, there are no pipes, and the water is uniform ponding under stated closed-basin assumptions, not a forecast and not a bound. [S363](../sources/S363-hydro-city-craft-summary.md)

**What it does not show.** As the page lists it: the ground is flat, with no elevation model, so the flood fills like a bathtub; no sewers, inlets, outfalls or infiltration after the rain (the street-drain gutters and ponds are decoration and say so); one storm spread evenly; impervious means mapped, at assumed road widths by class unless OSM has a width tag. [S363](../sources/S363-hydro-city-craft-summary.md)

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [SWMMCRAFT Ultimate (app)](swmmcraft-ultimate.md).

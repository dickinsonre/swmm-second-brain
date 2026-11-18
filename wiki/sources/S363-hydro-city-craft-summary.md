---
title: "S363: Hydro City Craft, summary written from the page (v1.1)"
type: source
raw: raw/apps/hydro-city-craft-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-26
ingested: 2026-11-18
tags: [apps, openstreetmap, minecraft, impervious-cover]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Hydro City Craft, version 1.1: OpenStreetMap streets and water built in Minecraft blocks. Raw file: [raw/apps/hydro-city-craft-v1.1.md](../../raw/apps/hydro-city-craft-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/6rvKezyDXceKe8PK1EgHTe, version 1793022744-50e0 (index.html, 2,508,705 bytes, SHA-256 26fd34ffe3337a15acf267e0909603de14c55591c420e429a011b3c1268f06a0), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in one Claude session on 24 to 26 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for a single-file HTML app, and on 26 October supplied an outside review of version 1.0, which version 1.1 answers; responsibility is his."

**Claims worth keeping** (all copied from the file)
- Turns a box of the real world from OpenStreetMap into a Minecraft world: buildings extruded from their footprints, streets painted by class, rivers, canals and lakes filled in. View it in 3D, click a building to see where its height came from, raise the water, and take it into the game as a WorldEdit schematic (Sponge Schematic version 2, Java Edition 1.20.4) or a ready-to-install data pack.
- Version 1.0 measured impervious cover in Minecraft blocks, so a coarser grid meant wider streets: Manhattan's ponding went from 12.60 in at grid 64 to 9.26 in at grid 256. Version 1.1 measures it on its own grid of 6.6-ft squares with roads at real widths, and gives 8.29 in at every grid size. Thirty defects are listed with the lines that caused them: twenty in the Lovable build and ten in version 1.0, found by an outside review.
- The Lovable TypeScript compiled unchanged (one import line altered for the bundler) and run beside the new engine on the same synthetic city and on the Manhattan and Venice snapshots: twenty checks pass, thirteen of them comparing the engines.
- Read-back of the exports by independent parsers; every command line expanded back into blocks.
- Each of the outside review's eight points reproduced before it was fixed; two multipolygon bugs fixed (a waterway that is also a lake's outer ring no longer fills the island; an unclosed ring is reported and skipped).

**Limits it states.** As the page lists it: the ground is flat, with no elevation model, so the flood fills like a bathtub; no sewers, inlets, outfalls or infiltration after the rain (the street-drain gutters and ponds are decoration and say so); one storm spread evenly; impervious means mapped, at assumed road widths by class unless OSM has a width tag.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Hydro City Craft (app)](../entities/hydro-city-craft.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [SWMMCRAFT Ultimate (app)](../entities/swmmcraft-ultimate.md).

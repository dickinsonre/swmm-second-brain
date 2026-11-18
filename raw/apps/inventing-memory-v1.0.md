---
name: Inventing Memory
file: inventing-memory.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/KMEHD5HkZLbCEMa1n7GMpq", original: "Lovable project inventing-memory (inventing-memory-source_v2.zip: 84 files; TanStack Start, React 19; MIT)", repo: none named in the page}
engines:
  - {name: "EPA SWMM 5.2.4 cross-section code", version: "tag v5.2.4", note: "xsect.c and shape.c ported to JavaScript with the tables from xsect.dat; no SWMM run"}
  - {name: "a Hopfield network", note: "the Lovable project's simulation, ported and replayed tick for tick"}
units: US customary by default in the Scale-it panel, SI behind a switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 25 October 2026 under Robert Dickinson's direction. Inside Claude it can add an optional live note from Claude. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/KMEHD5HkZLbCEMa1n7GMpq, version 1792946814-c724 (index.html, 1,204,332 bytes, SHA-256 db7471840cb48929ee7b0bdf8446417b1850ca9890ec592e4ad6b85fa53649b7), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Inventing Memory: a Hopfield forgetting machine that remembers SWMM5 cross-section shapes

## In three points
- **What:** A single-file edition of Bob's Lovable experiment: a Hopfield network on 144 cells taught 14 glyphs of SWMM5 cross-section shapes, made to forget (every weight shrinks and picks up noise each tick), kicked with damaged glyphs, and judged on whether it recalls a taught shape or invents a new one. A second page explores the properties of all 19 shapes against EPA SWMM 5.2.4 reference curves ported from xsect.c.
- **So what:** Fourteen patterns on 144 cells is 0.097, under the classic 0.138 capacity, yet Hebb's rule never shows more than 7 of the 14 taught shapes; the added projection rule shows all 14 until it forgets them, faster, and 46% of its cell-ticks are inventions even with no forgetting (σ = 0). Neither rule gives invention by forgetting.
- **Now what:** Use it as a playful lesson in memory, capacity and the geometry of SWMM shapes. The 12 x 12 alphabet is not SWMM's geometry, the exported CUSTOM-shape .inp was not run through the EPA engine, and the projection rule is one alternative among several untried.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Machine, Engine, Audit, About, Doc. Every 240 ms the machine forgets (weights shrink by σ/2 with Gaussian noise of size σ/2), kicks one cell in five with a random or damaged glyph, recalls once at temperature 1.5, and judges: a cell more than 10 of 144 bits from every taught glyph and its inverse is a hallucination and gets an invented name; with self-rewriting on, 5% of hallucinations are imprinted back. Added in this edition: the projection learning rule (Hebbian stays the default), honesty meters, an inspector with the SWMM5 CUSTOM-shape reading, .inp and CSV export, EPA SWMM 5.2.4 reference curves for all 19 shapes, and a Scale-it panel. Fixed: relearn restores the pattern count; decay σ can go to 0 for a null control. The Lovable AI annotation, which needed a Lovable server and key, is replaced by notes computed from measurements.

## Checks (as stated on the page)

- Port: a seeded replay of the shipped loop matches the original TypeScript tick for tick (mean energy and all 16 labels identical for 600 ticks in four configurations, including self-rewriting, σ = 0 and σ = 0.04); the kernel port matches xsect.ts on 19 shapes x 4 tables x 51 points with zero difference.
- Reference: xsect.dat and xsect.c from the EPA repository at tag v5.2.4; at full depth every EPA curve returns A/Afull = 1 and R/Rfull = 1; the peak of each section-factor table agrees with sMax in xsect_setParams within 0.0021, except the semi-elliptical, where EPA's own table peaks at 1.050.
- CUSTOM shapes: the shape.c port reproduces the circle (0.783, 0.249, 1.078 at 0.94) and a closed square (area 1, radius 0.25).
- Measurements: five seeds x 800 ticks per configuration, 64,000 cell-ticks each; every number in the Audit and Doc is read from that run.

## What this does not show

As the page lists it: no SWMM5 run of the exported .inp; the 12 x 12 alphabet is the Lovable glyph set, not SWMM's geometry (a circle on 144 cells is a blob); mirror agreement, piece count and holes stand in for "looks like a conduit"; the projection rule is one alternative; ellipse and arch sizes use size code 1 for their full-section constants, and the modified basket handle is compared only with W = H and a semicircular top.

## Credits and licenses

Amit, Gutfreund and Sompolinsky (1985) for the 0.138 capacity; EPA SWMM 5.2.4 source (public domain), xsect.dat, xsect.c, shape.c, link.c, table.c; the Lovable project, MIT © 2026 Robert Dickinson.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for an HTML app; responsibility is his. Claude read the Lovable source, ported the simulation and geometry kernel, ported the needed parts of xsect.c and shape.c, added the projection rule, meters, inspector and exports, ran every measurement quoted in the Audit and Doc tabs, and wrote the page, the Doc essay and figures, and the .docx. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first single-file edition (the version read).

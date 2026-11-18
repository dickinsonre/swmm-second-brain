---
title: "S366: Inventing Memory, summary written from the page (v1.0)"
type: source
raw: raw/apps/inventing-memory-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, neural-networks, hopfield, cross-sections]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Inventing Memory, version 1.0: a Hopfield forgetting machine that remembers SWMM5 cross-section shapes. Raw file: [raw/apps/inventing-memory-v1.0.md](../../raw/apps/inventing-memory-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/KMEHD5HkZLbCEMa1n7GMpq, version 1792946814-c724 (index.html, 1,204,332 bytes, SHA-256 db7471840cb48929ee7b0bdf8446417b1850ca9890ec592e4ad6b85fa53649b7), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for an HTML app; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A single-file edition of Bob's Lovable experiment: a Hopfield network on 144 cells taught 14 glyphs of SWMM5 cross-section shapes, made to forget (every weight shrinks and picks up noise each tick), kicked with damaged glyphs, and judged on whether it recalls a taught shape or invents a new one. A second page explores the properties of all 19 shapes against EPA SWMM 5.2.4 reference curves ported from xsect.c.
- Fourteen patterns on 144 cells is 0.097, under the classic 0.138 capacity, yet Hebb's rule never shows more than 7 of the 14 taught shapes; the added projection rule shows all 14 until it forgets them, faster, and 46% of its cell-ticks are inventions even with no forgetting (σ = 0). Neither rule gives invention by forgetting.
- Port: a seeded replay of the shipped loop matches the original TypeScript tick for tick (mean energy and all 16 labels identical for 600 ticks in four configurations, including self-rewriting, σ = 0 and σ = 0.04); the kernel port matches xsect.ts on 19 shapes x 4 tables x 51 points with zero difference.
- Reference: xsect.dat and xsect.c from the EPA repository at tag v5.2.4; at full depth every EPA curve returns A/Afull = 1 and R/Rfull = 1; the peak of each section-factor table agrees with sMax in xsect_setParams within 0.0021, except the semi-elliptical, where EPA's own table peaks at 1.050.
- CUSTOM shapes: the shape.c port reproduces the circle (0.783, 0.249, 1.078 at 0.94) and a closed square (area 1, radius 0.25).
- Measurements: five seeds x 800 ticks per configuration, 64,000 cell-ticks each; every number in the Audit and Doc is read from that run.

**Limits it states.** As the page lists it: no SWMM5 run of the exported .inp; the 12 x 12 alphabet is the Lovable glyph set, not SWMM's geometry (a circle on 144 cells is a blob); mirror agreement, piece count and holes stand in for "looks like a conduit"; the projection rule is one alternative; ellipse and arch sizes use size code 1 for their full-section constants, and the modified basket handle is compared only with W = H and a semicircular top.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Inventing Memory (app)](../entities/inventing-memory.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Conduit cross-sections: the built-in shapes](../concepts/conduit-cross-sections.md).

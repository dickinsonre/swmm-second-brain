---
name: RDII Rosetta Stone
file: rdii-rosetta-stone.html
version: "1.0"
date: 2026-10-21
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/3jemmFKg8cjQyjwd22RpVe", original: "Lovable project (TanStack Start, React 19), itself ported from an earlier single-file React version", repo: none named in the page}
engines:
  - {name: "EPA SWMM 5.2.4 rdii.c", version: "tag v5.2.4", note: "ported line for line to JavaScript for the storm-response view; EPA SWMM 5.2.4 compiled from the USEPA tag and run while building on eight verification models"}
units: US customary (cfs, in, ac)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/3jemmFKg8cjQyjwd22RpVe, version 1792638304-d93a (index.html, 783,636 bytes, SHA-256 620a55af1c52d7ac0994d98c4cc84d2d50cc5c5d0a62fc6ded97b950b0a32fc6), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# RDII Rosetta Stone: InfoSWMM RDII mapped to EPA SWMM5 and InfoWorks ICM, with live RTK math

## In three points
- **What:** For InfoSWMM users moving RDII to EPA SWMM5 or InfoWorks ICM: every concept, field name and workflow mapped across the three, with live RTK unit-hydrograph math, a storm-response view in cfs, a runnable SWMM5 .inp export, CSV exports and a Verify tab. A single-file rebuild of Bob's Lovable project; RTK in SWMM5's rdii.c was coded by Bob during the EPA SWMM5 CRADA.
- **So what:** The storm-response arithmetic is a line-for-line port of EPA SWMM 5.2.4 rdii.c and matches the engine within float precision on 8 verification models. Two defects in the source were fixed: the ICM Ruby snippet now writes inside a transaction (D-1), and all three exports carry the same initial abstraction values (D-2).
- **Now what:** Use it to move RDII parameters between products with the arithmetic checked. ICM and InfoSWMM were not run (InfoSWMM's swmm5.dll may be older than 5.2.4), the Ruby snippet has not run in ICM, and matching the engine says nothing about whether three triangles describe a given sewer.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-21"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: RTK Explorer, Field Mapping, Architecture, Migration, RDII Analyst, Verify, About, Doc. All five original sections and their text are kept. The storm-response view adds initial abstraction, a sewershed area and four storm shapes, in cfs.

## Checks (as stated on the page)

- EPA SWMM 5.2.4 compiled from the USEPA v5.2.4 tag; eight verification models written; engine runs compared with the port step by step, report totals compared, and repeat runs compared byte for byte.
- The app screenshotted in both themes at desktop and phone widths; colours run through a contrast check.

## What this does not show

As the page lists it: ICM was not run (field names come from the source app and Bob's ICM data-model notes; ICM's own RTK computation was not compared with rdii.c; the Ruby snippet has not run in ICM); InfoSWMM was not run; no observed flow was used; one UH group, one month set (ALL) and one node per model (monthly sets and sharing are described but not computed); rain gages with INTENSITY time series only.

## Credits and licenses

RTK unit hydrograph in EPA SWMM5's rdii.c, coded by Robert Dickinson during the EPA SWMM5 CRADA; reference engine USEPA/Stormwater-Management-Model tag v5.2.4 (public domain); swmm5.org. Bore Shell 1.0 layout; fonts Space Grotesk, DM Sans, JetBrains Mono. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the source project and asked for a single-file HTML app; responsibility is his. Claude read the source, a Lovable project (Lovable is an AI app builder) ported from an earlier single-file React version, compiled EPA SWMM 5.2.4, ported rdii.c to JavaScript, wrote the eight verification models and the comparison scripts, and rebuilt the app and its essay. The checks are mechanical; the essay's prose has not been checked by a person. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-21): first single-file edition (the version read).

---
name: SWMM Similarity Index
file: swmm-similarity-index.html
version: "1.0"
date: 2026-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Gb8CqJedmkQ9DwvYxPsz7w", original: "https://model-harmony-index.lovable.app (Lovable project swmm-similarity-index; MIT)", repo: none named in the page}
engines: none (a scoring engine over model input files and finished reports; the test reports came from EPA SWMM 5.2.4 runs)
units: as the models' own units (a unit round trip is one of its checks)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the Lovable project was generated with Lovable's AI tooling and that this edition was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Gb8CqJedmkQ9DwvYxPsz7w, version 1792896068-ee18 (index.html, 1,607,591 bytes, SHA-256 e98c068ad619757a3b8ca6a5ba927ac105b7f50b41d615b98f3874587b8235ee), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM Similarity Index: Bill James scoring for SWMM5, EPANET and ICM models

## In three points
- **What:** Scores how alike two hydraulic models are on a 0 to 1,000 scale, after Bill James's similarity scores for baseball players: start at 1,000 and subtract for each difference in junctions, outfalls, conduits and results. A single-file edition of Bob's Lovable project, with Compare, Outputs, Batch, Methodology and Verify tabs; 19 defects fixed, so scores differ from the Lovable app on some pairs.
- **So what:** The Lovable report parser misread EPA SWMM 5.2.4: version 5.2.4 prints two more columns than it expected, so for subcatchment 1 of EPA Example 1 it read a peak of 1.48 and a runoff coefficient of 0.4 where the report says 4.66 cfs and 0.559. A unit round trip (the Baseline sample converted to CFS by exact factors) now scores 1,000; the Lovable engine gave 881. 32 of 32 checks pass.
- **Now what:** Use it to see how far two versions of a model have drifted. A score of 1,000 means no difference was found among the attributes it scores, inside your tolerances; it does not mean the models are hydraulically equivalent, and much of a SWMM model is invisible to the score. No real ICM export has been tested.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0 · HTML edition"); it gives the build month (October 2026) but no day. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Compare, Outputs, Batch, Methodology, Verify, About, Doc. Junctions and outfalls are matched by ID and distance, conduits by ID only (length, slope, n, shape, geom1); the Doc draws what is scored, what is only counted, and what the score never reads. PDF export (jsPDF) draws the radar chart from the chart itself. Dropped: the Lovable per-folder score cache.

## Checks (as stated on the page)

A script runs the original Lovable engine and this edition on the same files; the Verify tab reads its results. 32 of 32 pass:
- Identity: each of 13 input files scores exactly 1,000 against itself with an empty ledger.
- Symmetry: all 78 pairs of input files and all 45 pairs of finished reports score the same both ways round.
- Null effect on real files: exam1.inp and extran1.inp in Bob's corpus are EXTRAN Example 1 written out twice with different option blocks; they score 1,000, and their byte-identical EPA SWMM 5.2.4 reports score 1,000.
- Unit round trip: 1,000 (Lovable 881).
- The report parser checked against reports EPA SWMM 5.2.4 actually wrote: EPA Example 1 and the EXTRAN examples in Viewer-Demo-Results.

## What this does not show

As the page lists it: a score of 1,000 is not hydraulic equivalence; the Doc's figure shows how much of a SWMM model the index never reads. No person has reviewed the new Hydrology weights or the coverage term, and no real ICM export was tested.

## Credits and licenses

Bill James's similarity scores (The Politics of Glory) via Baseball-Reference; models from SWMMBobSWMM6/1729-SWMM5-Models-2030 (Viewer-Demo-Results: exam1, extran1, extran8a, extran8b; OpenSWMM_Engine_Test_Decks: Example1.inp); jsPDF 2.5.1, jsPDF-AutoTable 3.8.2, html2canvas 1.4.1, gif.js 0.2.0. MIT License, © 2026 Robert Dickinson. SWMM5 is EPA's public-domain model; the page is not affiliated with EPA, Autodesk or Bill James.

## AI use

The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable project and asked for this single-file app; responsibility is his. Claude read the Lovable source, ported the TypeScript engine, found and fixed the 19 numbered defects, and wrote the interface, the charts, the derived control files, the verification script, the Doc essay and its .docx. The Lovable project itself was generated with Lovable's AI tooling. The EPA Example 1 report was run in EPA SWMM 5.2.4 by Bob's local SWMM5 MCP server. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10): first HTML edition (the version read).

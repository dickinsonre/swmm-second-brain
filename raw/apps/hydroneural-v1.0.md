---
name: HydroNeural
file: hydroneural.html
version: "1.0"
date: 2026-10-22
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/QKCJF1fy1xv35NBFqZLbgr", original: "Lovable project HydroNeural (export HydroNeural-source_1.zip: 84 files, 9,140 lines, TanStack Start + React 19 + Tailwind 4)", repo: none named in the page}
engines: none (every number on the dashboard is seeded mock data, as the page says)
units: US customary by default (ft, in/hr, cfs, ac), SI behind a toggle; the literature text keeps its authors' units
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session on 22 October 2026 under Robert Dickinson's direction, and that the Lovable project, including its literature review, was generated earlier by Lovable's AI. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/QKCJF1fy1xv35NBFqZLbgr, version 1792679529-6cc5 (index.html, 1,978,568 bytes, SHA-256 85e8b920ed6cc2d4b76f5342c3ea084d1a90e64f8a6a271ad90ca98a9059923c), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# HydroNeural: a SWMM5 surrogate console, with its mock data and its literature review audited

## In three points
- **What:** A single-file edition of HydroNeural, a Lovable-built console for a machine-learning surrogate of EPA SWMM5. It carries the original's forecast dashboard and literature review, adds an Anatomy of the source and an Audit of what the code computes, and explains it in a Doc tab. The header says it plainly: all numbers are seeded mock.
- **So what:** No surrogate exists here: no model was trained and no SWMM5 model was run; the map depths are a bias toward the lower-right corner plus noise, and the hydrograph is smoothed rain. Of the review's 22 references with a complete DOI, checked against Crossref, 8 match exactly, 11 are the right paper with a detail wrong (three credit the wrong first author), one DOI resolves to an unrelated paper on aerosol water-vapour uptake, and two returned errors.
- **Now what:** Use it as a worked example of auditing an AI-generated app and its citations before trusting either. It does not show whether the review's claims about each paper are right, only whether the cited records exist and match.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("HydroNeural HTML edition 1.0"); the date is the build session the page names. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Dashboard (six panels rebuilt as plain SVG and HTML: network map, hydrograph, storm library, experiment registry and metrics), Literature (the review as shipped, "Working paper v0.1"), Anatomy (the source: shadcn primitives, the TanStack router, Tailwind, error hooks, described rather than re-implemented), Audit, About, Doc. The literature review text, storm library, experiment registry and mock generators are reproduced as they are, with the audit's findings marked.

## Checks (as stated on the page)

- The generators in src/lib/swmm-mock.ts ported to plain JavaScript with the types removed and nothing else changed, then run in Node; the node, conduit, subcatchment and flooding counts come from that run. Hydrograph metrics from the component's own formulas on the generated series, with KGE added in the standard Gupta et al. form.
- Citations: 22 complete DOIs fetched from Crossref and compared on title, first author, year and journal. 8 exact; 11 right paper with a detail wrong, mostly Elsevier volume numbers, three with the wrong first author ([12] is Sun et al., not Buhl; [15] is Tanim et al., not Wang; [20] is Bentivoglio et al., not Morales-Hernández); [25] resolves to a paper on aerosol water-vapour uptake in Atmospheric Research; [14] and [23] errored at both Crossref and doi.org. Six more entries carry no complete DOI, three with a literal "..." in its place.

## What this does not show

As the page lists it: it does not show a surrogate (no training, no SWMM5 run; the experiment registry's four rows are typed numbers in the order the review ranks the methods); it does not reproduce the Lovable app pixel for pixel; it does not show whether the review's claims about each paper are right.

## Credits and licenses

The papers and tools the review cites, among them Garzón et al. (2024, SWMM_GNN), Zhang et al. (2024, GNN-UDS), pyswmm 2.1, and Rossman (2015) for SWMM5. The zip carries no LICENSE file; the project is Bob's.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session on 22 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the HydroNeural source export from Lovable, asked for an HTML app that shows all of it, and is responsible for the result. The Lovable project itself, including its literature review, was generated earlier by Lovable's AI. Claude read the 84 files, ported the four data generators, rebuilt the six panels, rendered the review, wrote the Anatomy and Audit tabs, assigned the method tags on the references, drew the nine figures and wrote the essay, its Word copy and the AI-use text. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-22): first HTML edition (the version read).

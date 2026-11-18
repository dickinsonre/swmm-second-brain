---
name: St. Venant Water Flow for Grandkids
file: st-venant-water-flow.html
version: "2.1"
date: 2026-10-22
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/5JyRoJJUpCrE23t7XYN5EH", original: "Lovable React web site (handover notes dated 8 March 2026)", repo: none named in the page}
engines: none (teaching simulators for slope and roughness; SWMM4 and SWMM6 described from their manuals and source, not run)
units: US customary (every displayed unit converted from the original)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says this edition was built with Claude on 21 October 2026 (version 2.1 on 22 October) under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/5JyRoJJUpCrE23t7XYN5EH, version 1792669679-8cde (index.html, 3,265,331 bytes, SHA-256 adc81674057616ee0198a26dc499171728828155a7ec136a743eba8598488f9b), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# St. Venant Water Flow for Grandkids: how water moves, for children under ten, with a grown-up mode

## In three points
- **What:** A teaching app that explains how water moves (the Saint-Venant equations, Manning's roughness, the water cycle, SWMM5, and how Singapore and Dubai keep their streets dry) to children under ten, with a grown-up mode that shows the real equations. Simulators, a water race, a gallery of real channels, a question-answering "Dr. St. Venant", an 18-question quiz and a glossary. Built by Bob in Lovable, here as one HTML file.
- **So what:** The original said SWMM5 uses the Preissmann four-point implicit scheme; the edition corrects it (SWMM5 iterates between conduit flows and node heads each step; the Preissmann box belongs to InfoWorks ICM and HEC-RAS 1D, and SWMM5's Preissmann slot is a surcharge option). Version 2.1 adds the SWMM family (SWMM4 1988, SWMM5 2004 to 2005, SWMM6 2026 alpha) with a "how many lifeguards does a pipe get?" explorer built on SWMM6's own finite-volume cell rule. The physics formulas themselves were not changed.
- **Now what:** Use it with a child at a window during a downpour. It is a teaching toy: the simulators are simple, and SWMM4 and SWMM6 are described from their manuals and source code, not run.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Version 2.1 · 2026-10-22"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: St. Venant, The Equations, Water Cycle, Singapore, Quiz, Glossary, Build Drain, About, Doc. Version 2.1 adds the SWMM family on the home page with a timeline and a grown-up comparison table, three quiz questions in a new SWMM Family category (18 questions, six topics), two new Dr. St. Venant answers, and four glossary words (SWMM4, SWMM6, EXTRAN, Finite Volume). The answer matcher scores a whole-word hit above a prefix hit, so "SWMM6" finds the SWMM6 answer. The About tab lists each change from the Lovable source as a card (source text, replacement, reason) with a CSV.

## Checks (as stated on the page)

- Facts looked up and corrected against primary sources, each change listed with the source text as it was.
- SWMM4 described from the 1988 EPA User's Manual (Huber and Dickinson, EPA/600/3-88/001a) and the 4.4/4.5 block documentation; SWMM6 from openswmm.engine, branch swmm6_rel, commit 306f847 (22 October 2026, engine 6.0.0-alpha.4), with the cell rule and the authors' measurement quoted verbatim.

## What this does not show

The page is for children, with simplified simulators; the physics formulas from the Lovable source were not changed, and no engine runs. Singapore's rain (about 94 in a year) and the other figures in the stories are illustrative of the lesson.

## Credits and licenses

Adhémar Barré de Saint-Venant (1871); Robert Manning; EPA SWMM 4 (Huber and Dickinson, 1988); EPA SWMM 5; HydroCouple's openswmm.engine. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session on 21 October 2026 under the direction of Robert (Bob) Dickinson, who wrote and published the original app, supplied its source, set the standing requirements (dark by default, US units, Doc and About pages, an AI disclosure) and is responsible for it. Claude changed the build so the app compiles to one HTML file, added the theme switch, tour, GIF recorder and CSV exports, converted every displayed unit to US customary, looked up and corrected the facts listed, rewrote the answer matcher, and wrote the Doc. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.1 (2026-10-22): the SWMM family, three quiz questions, two answers, four glossary words, Doc section 10 (the version read).
- 2.0 (2026-10-21): single-file edition with corrections.
- 1 (Lovable): the original web site.

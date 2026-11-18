---
title: "S362: St. Venant Water Flow for Grandkids, summary written from the page (v2.1)"
type: source
raw: raw/apps/st-venant-water-flow-v2.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-22
ingested: 2026-11-18
tags: [apps, teaching, children, saint-venant]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app St. Venant Water Flow for Grandkids, version 2.1: how water moves, for children under ten, with a grown-up mode. Raw file: [raw/apps/st-venant-water-flow-v2.1.md](../../raw/apps/st-venant-water-flow-v2.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/5JyRoJJUpCrE23t7XYN5EH, version 1792669679-8cde (index.html, 3,265,331 bytes, SHA-256 adc81674057616ee0198a26dc499171728828155a7ec136a743eba8598488f9b), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 21 October 2026 under the direction of Robert (Bob) Dickinson, who wrote and published the original app, supplied its source, set the standing requirements (dark by default, US units, Doc and About pages, an AI disclosure) and is responsible for it."

**Claims worth keeping** (all copied from the file)
- A teaching app that explains how water moves (the Saint-Venant equations, Manning's roughness, the water cycle, SWMM5, and how Singapore and Dubai keep their streets dry) to children under ten, with a grown-up mode that shows the real equations. Simulators, a water race, a gallery of real channels, a question-answering "Dr. St. Venant", an 18-question quiz and a glossary. Built by Bob in Lovable, here as one HTML file.
- The original said SWMM5 uses the Preissmann four-point implicit scheme; the edition corrects it (SWMM5 iterates between conduit flows and node heads each step; the Preissmann box belongs to InfoWorks ICM and HEC-RAS 1D, and SWMM5's Preissmann slot is a surcharge option). Version 2.1 adds the SWMM family (SWMM4 1988, SWMM5 2004 to 2005, SWMM6 2026 alpha) with a "how many lifeguards does a pipe get?" explorer built on SWMM6's own finite-volume cell rule. The physics formulas themselves were not changed.
- Facts looked up and corrected against primary sources, each change listed with the source text as it was.
- SWMM4 described from the 1988 EPA User's Manual (Huber and Dickinson, EPA/600/3-88/001a) and the 4.4/4.5 block documentation; SWMM6 from openswmm.engine, branch swmm6_rel, commit 306f847 (22 October 2026, engine 6.0.0-alpha.4), with the cell rule and the authors' measurement quoted verbatim.

**Limits it states.** The page is for children, with simplified simulators; the physics formulas from the Lovable source were not changed, and no engine runs. Singapore's rain (about 94 in a year) and the other figures in the stories are illustrative of the lesson.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [St. Venant Water Flow for Grandkids (app)](../entities/st-venant-water-flow.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md).

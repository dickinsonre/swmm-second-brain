---
title: SWMM5 Manual Search (app)
type: entity
updated: 2026-11-15
sources: [S101, S102]
tags: [apps, replit, swmm5, manuals, search, ai-agents]
reviewed: no
---
Bob's Replit app SWMM5 Manual Search: an app that searches the SWMM manual, shows matching sections, diagrams and calculators, checks and runs `.inp` files, and answers questions with an AI assistant. Version 5.2, at `swmm-manual-search-robertdickinson.replit.app` [S101](../sources/S101-swmm5-manual-search-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S101](../sources/S101-swmm5-manual-search-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S101](../sources/S101-swmm5-manual-search-replit-summary.md)
- A crawler writes the manual to `data/docs.jsonl`; a Whoosh index with stemming, SWMM synonyms and fuzzy terms serves the search.
- Its `/stats` run returned 53 chapters, 621 indexed sections and 248,407 words, with an index date of May 22, 2026.
- The calculator registry holds 30 entries; the README says nine. The homepage has 43 interactive diagram controls and 19 chat-language controls. `data/swmm_version_history.json` holds 41 version records.
- It validates and runs a submitted `.inp` through PySWMM and swmm-toolkit; the engine reports EPA SWMM 5.2.4.
- The chatbot and the result summarizer use Anthropic's `claude-sonnet-4-5` model, sending up to eight manual results as context.
- Tests: 25 passed, 0 failed.
- The version `5.2` is the SWMM version the app reports, not a release number of the app.
- Credits: Robert Dickinson as creator; Scott Jeffers for domain expertise and stewardship of the manual collection; the U.S. EPA as the source of the manual and the engine.
- Repository: https://github.com/dickinsonre/SJ-SWMM5-ManualSearch. The app's own code has no stated open-source license.

**What it does not show.** No fresh crawl was run and the stored index was not compared with the live manual. User-supplied simulations and live Anthropic responses were not tested. The production homepage was not loaded. [S101](../sources/S101-swmm5-manual-search-replit-summary.md)

**Noted at ingest.** The three `/stats` figures are the ones printed on the landing page of [S102](../sources/S102-swmm-manual-search-landing-page-replit-summary.md).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [SWMM Manual Search landing page (app)](swmm-manual-search-landing-page.md), [EPA SWMM 5](swmm-5.md), [Master SWMM PDF (app)](master-swmm-pdf.md).

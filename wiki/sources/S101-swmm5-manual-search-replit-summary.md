---
title: "S101: SWMM5 Manual Search, summary written by Replit Agent (v5.2)"
type: source
raw: raw/apps/swmm-manual-search-robertdickinson-v5.2.md
kind: app-md
author: Robert Dickinson
published: 2026-07-20
ingested: 2026-11-15
tags: [apps, replit, swmm5, manuals, search, ai-agents]
reviewed: no
---
**What it is.** A technical summary of SWMM5 Manual Search, version 5.2: an app that searches the SWMM manual, shows matching sections, diagrams and calculators, checks and runs `.inp` files, and answers questions with an AI assistant. It is one of Bob's Replit apps, at `swmm-manual-search-robertdickinson.replit.app`. Raw file: [raw/apps/swmm-manual-search-robertdickinson-v5.2.md](../../raw/apps/swmm-manual-search-robertdickinson-v5.2.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says the checked source and Git history do not identify Replit Agent or another AI as a developer. The copy here was read out of the editor of the Replit project named SJ_SWMM5_Manual_Search on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- A crawler writes the manual to `data/docs.jsonl`; a Whoosh index with stemming, SWMM synonyms and fuzzy terms serves the search.
- Its `/stats` run returned 53 chapters, 621 indexed sections and 248,407 words, with an index date of May 22, 2026.
- The calculator registry holds 30 entries; the README says nine. The homepage has 43 interactive diagram controls and 19 chat-language controls. `data/swmm_version_history.json` holds 41 version records.
- It validates and runs a submitted `.inp` through PySWMM and swmm-toolkit; the engine reports EPA SWMM 5.2.4.
- The chatbot and the result summarizer use Anthropic's `claude-sonnet-4-5` model, sending up to eight manual results as context.
- Tests: 25 passed, 0 failed.
- The version `5.2` is the SWMM version the app reports, not a release number of the app.
- Credits: Robert Dickinson as creator; Scott Jeffers for domain expertise and stewardship of the manual collection; the U.S. EPA as the source of the manual and the engine.
- Repository: https://github.com/dickinsonre/SJ-SWMM5-ManualSearch. The app's own code has no stated open-source license.

**Limits it states.** No fresh crawl was run and the stored index was not compared with the live manual. User-supplied simulations and live Anthropic responses were not tested. The production homepage was not loaded.

**Checked at ingest.** The three `/stats` figures are the ones printed on the landing page of [S102](S102-swmm-manual-search-landing-page-replit-summary.md).

**Feeds:** [SWMM5 Manual Search (app)](../entities/swmm5-manual-search.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [SWMM Manual Search landing page (app)](../entities/swmm-manual-search-landing-page.md), [EPA SWMM 5](../entities/swmm-5.md), [Master SWMM PDF (app)](../entities/master-swmm-pdf.md).

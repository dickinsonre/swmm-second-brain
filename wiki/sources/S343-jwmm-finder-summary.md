---
title: "S343: JWMM Finder, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/jwmm-finder-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-06
ingested: 2026-11-18
tags: [apps, papers, jwmm, search, calibration]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app JWMM Finder, version 1.0.0: all 750 papers of the Journal of Water Management Modeling, searchable in the browser. Raw file: [raw/apps/jwmm-finder-v1.0.0.md](../../raw/apps/jwmm-finder-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/Mw2zmVmpeVpG6GrC7vg8Jf, version 1794011522-1b09 (index.html, 3,871,382 bytes, SHA-256 595399d9e2c3c7c8316e7853741cb4835ef35e0a040cb7c4bff2b0c8b999e882), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: Claude, Anthropic's AI model, built this app in a Claude session in November 2026 at the direction of Robert (Bob) Dickinson, who chose the project, supplied the review document and its CSV table, and is responsible for the app. Claude wrote the data-build script (merging, name normalizing, model families, keyword flags), the search engine, the interface, the charts, the Doc essay and its .docx."

**Claims worth keeping** (all copied from the file)
- One HTML file that holds structured summaries of all 750 papers listed by the Journal of Water Management Modeling (JWMM), 1993 to November 2026, with a search engine, filters that count before you click, charts of the whole collection, a starred list and exports (CSV, BibTeX, citations). Each summary has the objective, study area, methods, findings, limitations, engineering implications, models and topics.
- You can find a paper by what it measured, where and with which model, not only by its title: 300 papers name SWMM in some version, 126 EPA SWMM5, 89 PCSWMM, 17 InfoWorks ICM or CS. Six keyword flags sort papers by how they report calibration: 211 say not calibrated, 472 report calibration, 57 report NSE, and 7 carry Robert E. Dickinson in the author list.
- 62 automated engine tests: known-item queries must return the right paper first; filter counts must equal the review's own section headings; boolean results must obey set arithmetic; unit conversions are checked against hand-worked values.
- The page was loaded in headless Chromium in both themes and at phone width and checked for console errors.

**Limits it states.** As the page lists it: the papers themselves. Summaries condense them, and themes, families and flags come from keyword rules. No person has yet checked the 750 summaries against the papers, the 28 family rules or the six keyword flags paper by paper. Check the original figures and tables before relying on a number.

**Checked at ingest.** 509 + 217 + 12 + 10 + 2 = 750 and 734 + 16 = 750, with 493 + 241 = 734 (our arithmetic). The page carries condensed summaries of 750 papers that are copyright their authors and CHI, written by a separate AI process. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [JWMM Finder (app)](../entities/jwmm-finder.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Robert (Bob) Dickinson](../entities/robert-dickinson.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md).

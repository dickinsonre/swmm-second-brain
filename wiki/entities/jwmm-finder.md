---
title: "JWMM Finder (app)"
type: entity
updated: 2026-11-18
sources: [S343]
tags: [apps, papers, jwmm, search, calibration]
reviewed: no
---
Bob's app JWMM Finder: all 750 papers of the Journal of Water Management Modeling, searchable in the browser. Version 1.0.0, 2026-11-06 [S343](../sources/S343-jwmm-finder-summary.md). Its `links:` line names no live Netlify address [S343](../sources/S343-jwmm-finder-summary.md).

**A caution about its source.** The page ships no technical summary. [S343](../sources/S343-jwmm-finder-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S343](../sources/S343-jwmm-finder-summary.md)
- One HTML file that holds structured summaries of all 750 papers listed by the Journal of Water Management Modeling (JWMM), 1993 to November 2026, with a search engine, filters that count before you click, charts of the whole collection, a starred list and exports (CSV, BibTeX, citations). Each summary has the objective, study area, methods, findings, limitations, engineering implications, models and topics.
- You can find a paper by what it measured, where and with which model, not only by its title: 300 papers name SWMM in some version, 126 EPA SWMM5, 89 PCSWMM, 17 InfoWorks ICM or CS. Six keyword flags sort papers by how they report calibration: 211 say not calibrated, 472 report calibration, 57 report NSE, and 7 carry Robert E. Dickinson in the author list.
- 62 automated engine tests: known-item queries must return the right paper first; filter counts must equal the review's own section headings; boolean results must obey set arithmetic; unit conversions are checked against hand-worked values.
- The page was loaded in headless Chromium in both themes and at phone width and checked for console errors.

**How to use it, as the summary puts it.** Use it to find the paper, then read the paper. The summaries were extracted automatically (734 from full text, 16 from the abstract only), and the themes, model families and flags come from keyword rules; no person has checked them against the papers. [S343](../sources/S343-jwmm-finder-summary.md)

**What it does not show.** As the page lists it: the papers themselves. Summaries condense them, and themes, families and flags come from keyword rules. No person has yet checked the 750 summaries against the papers, the 28 family rules or the six keyword flags paper by paper. Check the original figures and tables before relying on a number. [S343](../sources/S343-jwmm-finder-summary.md)

**Noted at ingest.** 509 + 217 + 12 + 10 + 2 = 750 and 734 + 16 = 750, with 493 + 241 = 734 (our arithmetic). The page carries condensed summaries of 750 papers that are copyright their authors and CHI, written by a separate AI process.

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Robert (Bob) Dickinson](robert-dickinson.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md).

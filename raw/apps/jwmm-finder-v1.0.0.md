---
name: JWMM Finder
file: jwmm-finder.html
version: 1.0.0
date: 2026-11-06
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Mw2zmVmpeVpG6GrC7vg8Jf", subject: "https://www.chijournal.org", repo: none}
engines: none (a search engine written for the page: query parser, Porter stemmer, field-weighted BM25, synonyms; no model runs)
units: the papers' own units, mostly metric; a US switch adds US customary equivalents beside them
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude built the app in November 2026 under Robert Dickinson's direction, and that a separate AI process wrote the 750 paper summaries. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Mw2zmVmpeVpG6GrC7vg8Jf, version 1794011522-1b09 (index.html, 3,871,382 bytes, SHA-256 595399d9e2c3c7c8316e7853741cb4835ef35e0a040cb7c4bff2b0c8b999e882), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# JWMM Finder: all 750 papers of the Journal of Water Management Modeling, searchable in the browser

## In three points
- **What:** One HTML file that holds structured summaries of all 750 papers listed by the Journal of Water Management Modeling (JWMM), 1993 to November 2026, with a search engine, filters that count before you click, charts of the whole collection, a starred list and exports (CSV, BibTeX, citations). Each summary has the objective, study area, methods, findings, limitations, engineering implications, models and topics.
- **So what:** You can find a paper by what it measured, where and with which model, not only by its title: 300 papers name SWMM in some version, 126 EPA SWMM5, 89 PCSWMM, 17 InfoWorks ICM or CS. Six keyword flags sort papers by how they report calibration: 211 say not calibrated, 472 report calibration, 57 report NSE, and 7 carry Robert E. Dickinson in the author list.
- **Now what:** Use it to find the paper, then read the paper. The summaries were extracted automatically (734 from full text, 16 from the abstract only), and the themes, model families and flags come from keyword rules; no person has checked them against the papers.

This summary was written after the fact. The app ships no technical summary of its own. Its version and date are the page's own ("v1.0.0, November 6, 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Search, Synthesis, Explore, Starred, About, Doc. Search runs in the page and no query leaves it. The Synthesis tab carries the review's cross-paper synthesis unchanged. With US units on, a US customary equivalent appears in brackets after each metric quantity the app recognizes, marked with ≈; the original numbers stay. The Doc tab holds the essay "Finding the Needle: How JWMM Finder Searches 750 Papers", also offered as a .docx.

## What is in it (as the page counts it)

- 750 papers: 509 R-series (the older book-chapter series), 217 C, 12 S, 10 H and 2 A. The S, H and A series begin in 2024.
- 1,424 distinct author names; eleven variants merged by hand ("W.T. Dickinson" stays a different person from Robert E. Dickinson).
- 13 themes from the review's keyword rules, up to three per paper; 28 model and tool families assigned by the app.
- Summaries: 734 from the full text (493 from a PDF, 241 from the journal web page) and 16 from the abstract only, because those chapters were scanned or only partly available.
- Keyword flags: says not calibrated 211; calibration reported 472; says not validated 55; validation reported 459; reports NSE 57; your papers 7. The page notes that a GIS or data paper with no model to calibrate can still get "says not calibrated", which is why its 211 is higher than the review's estimate of about 170.

## Checks (as stated on the page)

- 62 automated engine tests: known-item queries must return the right paper first; filter counts must equal the review's own section headings; boolean results must obey set arithmetic; unit conversions are checked against hand-worked values.
- The page was loaded in headless Chromium in both themes and at phone width and checked for console errors.

## What this does not show

As the page lists it: the papers themselves. Summaries condense them, and themes, families and flags come from keyword rules. No person has yet checked the 750 summaries against the papers, the 28 family rules or the six keyword flags paper by paper. Check the original figures and tables before relying on a number.

## Credits and licenses

Journal of Water Management Modeling, All Papers listing at chijournal.org; papers © their authors and CHI, DOIs under the 10.14796 prefix. "Journal of Water Management Modeling: A Paper-by-Paper Review of All 750 Papers", prepared for Robert Dickinson, November 6, 2026, with its summary table (CSV). M. F. Porter (1980), the stemmer; S. E. Robertson, H. Zaragoza and M. Taylor (2004), the BM25F ranking. No license is stated for the page.

## AI use

The page says: Claude, Anthropic's AI model, built this app in a Claude session in November 2026 at the direction of Robert (Bob) Dickinson, who chose the project, supplied the review document and its CSV table, and is responsible for the app. Claude wrote the data-build script (merging, name normalizing, model families, keyword flags), the search engine, the interface, the charts, the Doc essay and its .docx. Earlier, a separate AI process wrote the paper summaries, the themes and the synthesis; Claude did not write or change them. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.0 (2026-11-06): first release (the version read).

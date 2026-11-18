---
name: ICWMM Insights
file: icwmm-insights.html
version: "1.0"
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/TTLJ9ydfNXvxNvSXi3ixcf", original: "Lovable project bobswmm-icwmm-insights (source export dated 21 October 2026)", repo: none named in the page}
engines: none (one tested scoring module, scoring.js; no SWMM5 or ICM run stands behind any hydraulic number)
units: US customary by default, SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the original was generated in Lovable, an AI app builder, from Bob Dickinson's prompts, and that this edition was made with Claude in October 2026 at his request, with a research sub-agent doing part of the archive search. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/TTLJ9ydfNXvxNvSXi3ixcf, version 1792895927-cf7c (index.html, 1,472,775 bytes, SHA-256 8f8f57c68552e35f7bf778aa60300d048bea965751f0eaf71fcf31960ef17746), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# ICWMM Insights: Robert Dickinson's ICWMM papers and the Bill James similarity score

## In three points
- **What:** A small site about Bob's papers at the International Conference on Water Management Modeling, built around an idea from baseball: score two model runs by starting at 1,000 and subtracting for every difference. It has a calculator for that score, Bill James's baseball original for comparison, a quiz, sample charts and an archive of his ICWMM and journal papers.
- **So what:** The Lovable build mixed real facts with generated ones, so this edition labels every number and entry by where it came from (verified, unconfirmed, Lovable placeholder, illustrative, computed live). Of 59 archive entries on file, 9 are verified against icwmm.org and chijournal.org; 49 Lovable placeholders are hidden by default. The full defect register has 36 items, among them hard-coded results (872, 985, 94.2%, 98.5%) now computed live and six AI-generated "model output" images replaced by drawings from the sample data.
- **Now what:** Use it to read Bob's ICWMM record and try the similarity score on six numbers you supply. No SWMM5 or ICM run stands behind any hydraulic number, the calculator does not read model files, and it does not reproduce the 2025 paper's node-by-node method.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Single-file edition 1.0, 2026-10-24"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Home, Archive, Similarity Index, Charts, About, Doc. The calculator keeps the Lovable schedule as the default, with its 700 floor shown, and adds the Dickinson 2020 rule, a swap check, fixed JSON and CSV import, and US/SI units. The baseball tab adds James's published schedule as a switch with real season lines and corrects a misattributed quote. The 51st ICWMM page is rewritten from the real 2018 paper with Anthony Kuch (ICM against SWMM5 against XPSWMM). Placeholder downloads and videos are replaced by the real ICWMM, CHI journal and Baseball-Reference pages.

## Checks (as stated on the page)

- Computed: every score, percentage and summary statistic comes from scoring.js; a Node test file pins 32 results (four sample scores under both rules, symmetry, unit invariance, the 700 floor, string inputs from JSON, zero guards, both baseball schedules on real season lines).
- Checked against a primary page: archive entries against icwmm.org and chijournal.org; the baseball schedule and season lines against Baseball-Reference; the 2025 venue and dates (Toronto, March 5 to 7) against a conference listing.
- Illustrative: every hydraulic number in the samples, charts and gallery was typed by the Lovable build and carries an illustrative-data label.
- Every page loaded in a headless browser in both themes.

## What this does not show

As the page lists it: no SWMM5 or InfoWorks ICM run behind any hydraulic number; the calculator scores six numbers you supply and reads no .inp, .out or ICM results; it does not reproduce the 2025 paper's node-by-node method or results; the archive lists 9 confirmed papers out of 59 entries, and ICWMM years before 2020 are not confirmed.

## Credits and licenses

Bill James's similarity scores (baseball); Baseball-Reference; icwmm.org; chijournal.org; Anthony Kuch, co-author of the 2018 paper. No license is stated for the page. The defect register quotes the Lovable build's old contact link, an address the page says is no longer Bob's.

## AI use

The page says: the original app was generated in Lovable, an AI app builder, from Bob Dickinson's prompts (source export dated 21 October 2026); Lovable wrote its code, text, sample data and archive entries, and the six gallery images it used were AI-generated. This edition was made with Claude, Anthropic's AI model, in October 2026 at Bob's request; responsibility is his. Claude read the Lovable source, moved every score into one tested module, checked the archive and the baseball claims against icwmm.org, chijournal.org and Baseball-Reference (a research sub-agent did part of the archive search), and rewrote the pages. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-24): first single-file edition (the version read).

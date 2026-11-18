---
title: "S345: ICWMM Insights, summary written from the page (v1.0)"
type: source
raw: raw/apps/icwmm-insights-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, papers, icwmm, similarity]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app ICWMM Insights, version 1.0: Robert Dickinson's ICWMM papers and the Bill James similarity score. Raw file: [raw/apps/icwmm-insights-v1.0.md](../../raw/apps/icwmm-insights-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/TTLJ9ydfNXvxNvSXi3ixcf, version 1792895927-cf7c (index.html, 1,472,775 bytes, SHA-256 8f8f57c68552e35f7bf778aa60300d048bea965751f0eaf71fcf31960ef17746), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: the original app was generated in Lovable, an AI app builder, from Bob Dickinson's prompts (source export dated 21 October 2026); Lovable wrote its code, text, sample data and archive entries, and the six gallery images it used were AI-generated. This edition was made with Claude, Anthropic's AI model, in October 2026 at Bob's request; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A small site about Bob's papers at the International Conference on Water Management Modeling, built around an idea from baseball: score two model runs by starting at 1,000 and subtracting for every difference. It has a calculator for that score, Bill James's baseball original for comparison, a quiz, sample charts and an archive of his ICWMM and journal papers.
- The Lovable build mixed real facts with generated ones, so this edition labels every number and entry by where it came from (verified, unconfirmed, Lovable placeholder, illustrative, computed live). Of 59 archive entries on file, 9 are verified against icwmm.org and chijournal.org; 49 Lovable placeholders are hidden by default. The full defect register has 36 items, among them hard-coded results (872, 985, 94.2%, 98.5%) now computed live and six AI-generated "model output" images replaced by drawings from the sample data.
- Computed: every score, percentage and summary statistic comes from scoring.js; a Node test file pins 32 results (four sample scores under both rules, symmetry, unit invariance, the 700 floor, string inputs from JSON, zero guards, both baseball schedules on real season lines).
- Checked against a primary page: archive entries against icwmm.org and chijournal.org; the baseball schedule and season lines against Baseball-Reference; the 2025 venue and dates (Toronto, March 5 to 7) against a conference listing.
- Illustrative: every hydraulic number in the samples, charts and gallery was typed by the Lovable build and carries an illustrative-data label.
- Every page loaded in a headless browser in both themes.

**Limits it states.** As the page lists it: no SWMM5 or InfoWorks ICM run behind any hydraulic number; the calculator scores six numbers you supply and reads no .inp, .out or ICM results; it does not reproduce the 2025 paper's node-by-node method or results; the archive lists 9 confirmed papers out of 59 entries, and ICWMM years before 2020 are not confirmed.

**Checked at ingest.** The Bill James of the similarity score is the baseball writer, not [William (Bill) James](../entities/william-james.md). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [ICWMM Insights (app)](../entities/icwmm-insights.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Robert (Bob) Dickinson](../entities/robert-dickinson.md), [SWMM Similarity Index (app)](../entities/swmm-similarity-index.md).

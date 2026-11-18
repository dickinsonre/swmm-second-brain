---
title: "ICWMM Insights (app)"
type: entity
updated: 2026-11-18
sources: [S345]
tags: [apps, papers, icwmm, similarity]
reviewed: no
---
Bob's app ICWMM Insights: Robert Dickinson's ICWMM papers and the Bill James similarity score. Version 1.0, 2026-10-24 [S345](../sources/S345-icwmm-insights-summary.md). Its `links:` line names no live Netlify address [S345](../sources/S345-icwmm-insights-summary.md).

**A caution about its source.** The page ships no technical summary. [S345](../sources/S345-icwmm-insights-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S345](../sources/S345-icwmm-insights-summary.md)
- A small site about Bob's papers at the International Conference on Water Management Modeling, built around an idea from baseball: score two model runs by starting at 1,000 and subtracting for every difference. It has a calculator for that score, Bill James's baseball original for comparison, a quiz, sample charts and an archive of his ICWMM and journal papers.
- The Lovable build mixed real facts with generated ones, so this edition labels every number and entry by where it came from (verified, unconfirmed, Lovable placeholder, illustrative, computed live). Of 59 archive entries on file, 9 are verified against icwmm.org and chijournal.org; 49 Lovable placeholders are hidden by default. The full defect register has 36 items, among them hard-coded results (872, 985, 94.2%, 98.5%) now computed live and six AI-generated "model output" images replaced by drawings from the sample data.
- Computed: every score, percentage and summary statistic comes from scoring.js; a Node test file pins 32 results (four sample scores under both rules, symmetry, unit invariance, the 700 floor, string inputs from JSON, zero guards, both baseball schedules on real season lines).
- Checked against a primary page: archive entries against icwmm.org and chijournal.org; the baseball schedule and season lines against Baseball-Reference; the 2025 venue and dates (Toronto, March 5 to 7) against a conference listing.
- Illustrative: every hydraulic number in the samples, charts and gallery was typed by the Lovable build and carries an illustrative-data label.
- Every page loaded in a headless browser in both themes.

**How to use it, as the summary puts it.** Use it to read Bob's ICWMM record and try the similarity score on six numbers you supply. No SWMM5 or ICM run stands behind any hydraulic number, the calculator does not read model files, and it does not reproduce the 2025 paper's node-by-node method. [S345](../sources/S345-icwmm-insights-summary.md)

**What it does not show.** As the page lists it: no SWMM5 or InfoWorks ICM run behind any hydraulic number; the calculator scores six numbers you supply and reads no .inp, .out or ICM results; it does not reproduce the 2025 paper's node-by-node method or results; the archive lists 9 confirmed papers out of 59 entries, and ICWMM years before 2020 are not confirmed. [S345](../sources/S345-icwmm-insights-summary.md)

**Noted at ingest.** The Bill James of the similarity score is the baseball writer, not [William (Bill) James](william-james.md).

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Robert (Bob) Dickinson](robert-dickinson.md), [SWMM Similarity Index (app)](swmm-similarity-index.md).

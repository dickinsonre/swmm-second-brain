---
title: ICM InfoWorks release history (app)
type: entity
updated: 2026-11-15
sources: [S107, S127]
tags: [apps, replit, icm, release-history, ai]
reviewed: 11/16/2026
---
Bob's Replit app ICM InfoWorks: an app for browsing the release history of Autodesk InfoWorks ICM: a timeline, search, filters, version comparison, learning paths, diagrams and AI answers that cite features. Version 1.0.0, at `icm-new-view-robertdickinson.replit.app` [S127](../sources/S127-icm-infoworks-release-history-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S127](../sources/S127-icm-infoworks-release-history-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S127](../sources/S127-icm-infoworks-release-history-replit-summary.md)
- The data set holds 50 release records and 822 feature records. The latest release is 2027.2 and the earliest 1.5.
- The release source is a file in the project, `server/data/versions.ts`, not a live documentation feed. The latest record labels its date as user-supplied.
- No Autodesk ICM simulation engine is called. `engines: none`.
- Feature "evolution chains" cluster similar titles at a similarity threshold of 0.5; the file calls them heuristic links, not verified feature ancestry.
- The capability radar counts keyword matches: documented mentions, not engineering capability.
- Diagram calculators use SI: SCS runoff with `S = 25400 / CN - 254` and `Ia = 0.2 * S` in millimeters, a design rainfall depth expression, and a pump operating point. The file says they were read, not numerically validated.
- 5 main tabs, 9 diagram entries and 9 learning paths.
- `npm run check` failed with 13 diagnostics. No test script exists. A data check passed 4 assertions.
- The whole release data set is put into the AI system prompt. Routes exist for Claude, Gemini, OpenAI and DeepSeek through OpenRouter; the page offers Claude and Gemini.
- Project license MIT. Reuse rights for the Autodesk documentation content were not verified.

**What it does not show.** Release dates, feature wording and links were not checked against Autodesk's own sources. AI answers and citations were not checked. Exports, filters and comparisons were not exercised end to end. [S127](../sources/S127-icm-infoworks-release-history-replit-summary.md)

**Noted at ingest.** The app's name in the file is "ICM InfoWorks", the same as the product; this wiki titles its page by what it does (Q77). The SCS storage is in millimeters; the form in inches, `S = 1000 / CN - 10`, is in [S107](../sources/S107-green-ampt-calculator-replit-summary.md).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [InfoWorks ICM](infoworks-icm.md).

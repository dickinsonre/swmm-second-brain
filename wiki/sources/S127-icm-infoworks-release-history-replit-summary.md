---
title: "S127: ICM InfoWorks, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/icm-new-view-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2025-11-13
ingested: 2026-11-15
tags: [apps, replit, icm, release-history, ai]
reviewed: no
---
**What it is.** A technical summary of ICM InfoWorks, version 1.0.0: an app for browsing the release history of Autodesk InfoWorks ICM: a timeline, search, filters, version comparison, learning paths, diagrams and AI answers that cite features. It is one of Bob's Replit apps, at `icm-new-view-robertdickinson.replit.app`. Raw file: [raw/apps/icm-new-view-robertdickinson-v1.0.0.md](../../raw/apps/icm-new-view-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says recent Git commits identify Replit Agent as author of release-note, chat-sidebar and learning-path changes. The copy here was read out of the editor of the Replit project named ICMNewView on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** Release dates, feature wording and links were not checked against Autodesk's own sources. AI answers and citations were not checked. Exports, filters and comparisons were not exercised end to end.

**Checked at ingest.** The app's name in the file is "ICM InfoWorks", the same as the product; this wiki titles its page by what it does (Q77). The SCS storage is in millimeters; the form in inches, `S = 1000 / CN - 10`, is in [S107](S107-green-ampt-calculator-replit-summary.md).

**Feeds:** [ICM InfoWorks release history (app)](../entities/icm-release-history-app.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [InfoWorks ICM](../entities/infoworks-icm.md).

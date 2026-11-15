---
title: "S140: SWMM5Wiki, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/gator-swmm-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2025-08-28
ingested: 2026-11-15
tags: [apps, replit, swmm5, education, quiz]
reviewed: no
---
**What it is.** A technical summary of SWMM5Wiki, version 1.0.0: an educational guide to SWMM (hydrology, hydraulics, history, the conceptual model and LID controls) with a glossary and a separate game page of modeling challenges; it does not run a simulation. It is one of Bob's Replit apps, at `gatorbeaverswmm.com`. Raw file: [raw/apps/gator-swmm-robertdickinson-v1.0.0.md](../../raw/apps/gator-swmm-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the project source and documentation do not identify AI tools used to build it. The copy here was read out of the editor of the Replit project named GatorSWMM on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It does not run a stormwater simulation. No SWMM or other engine is bundled or called. `engines: none`.
- 5 educational sections, 8 glossary terms and 16 game scenarios, each confirmed by a development API response. Two client pages, `/` and `/game`.
- Multiple-choice answers are graded by the selected option's `correct` flag.
- Written responses are graded by case-insensitive substring matches against stored keywords; a response is marked correct when it matches at least two. Its score is the matched-keyword count divided by the stored keyword count, capped at 100.
- Design answers are compared with `solution.minDiameter` using a 10% tolerance, with a fallback minimum diameter of 18 when that field is absent.
- A storage-node scenario stores `orificeDiameter` instead, so that scenario is not graded against its stored solution.
- New content and progress are held in server memory and are lost when the process restarts. PostgreSQL table definitions exist, but the server imports `MemStorage`.
- The game page displays SWMM5 and ICM, and a stored scenario still compares ICM and SWMM routing.
- `npm run build` passed. `npm run check` failed with 1 TypeScript diagnostic. No `test` script. Both pages loaded in the development preview with no console errors.
- `package.json` declares MIT. `units: US customary`.

**Limits it states.** Individual quiz submissions, all challenge types, API write validation and progress after a server restart were not tested. The published pages and mobile layouts were not checked.

**Checked at ingest.** Its `file:` is gator-swmm, its address gatorbeaverswmm.com and its name SWMM5Wiki; none of the three says it holds a game of challenges (Q77). The `date:` is the newest date in the Git log, 28 August 2025, and every change listed is from that day (Q75). The fallback minimum diameter of 18 has no unit in the file. A second quiz app, [SWMM5 Quizzer (app)](../entities/swmm5-quizzer.md) [S138](S138-swmm5-quizzer-replit-summary.md), was ingested with it.

**Feeds:** [SWMM5Wiki (app)](../entities/swmm5wiki.md), [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [SWMM5 Quizzer (app)](../entities/swmm5-quizzer.md), [InfoDrainage Explorer (app)](../entities/infodrainage-explorer.md).

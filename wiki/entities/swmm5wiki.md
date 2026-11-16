---
title: "SWMM5Wiki (app)"
type: entity
updated: 2026-11-15
sources: [S138, S140]
tags: [apps, replit, swmm5, education, quiz]
reviewed: 11/16/2026
---
Bob's Replit app SWMM5Wiki: an educational guide to SWMM (hydrology, hydraulics, history, the conceptual model and LID controls) with a glossary and a separate game page of modeling challenges; it does not run a simulation. Version 1.0.0, at `gatorbeaverswmm.com` [S140](../sources/S140-swmm5wiki-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S140](../sources/S140-swmm5wiki-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S140](../sources/S140-swmm5wiki-replit-summary.md)
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

**What it does not show.** Individual quiz submissions, all challenge types, API write validation and progress after a server restart were not tested. The published pages and mobile layouts were not checked. [S140](../sources/S140-swmm5wiki-replit-summary.md)

**Noted at ingest.** Its `file:` is gator-swmm, its address gatorbeaverswmm.com and its name SWMM5Wiki; none of the three says it holds a game of challenges (Q77). The `date:` is the newest date in the Git log, 28 August 2025, and every change listed is from that day (Q75). The fallback minimum diameter of 18 has no unit in the file. A second quiz app, [SWMM5 Quizzer (app)](swmm5-quizzer.md) [S138](../sources/S138-swmm5-quizzer-replit-summary.md), was ingested with it.

See [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [SWMM5 Quizzer (app)](swmm5-quizzer.md), [InfoDrainage Explorer (app)](infodrainage-explorer.md).

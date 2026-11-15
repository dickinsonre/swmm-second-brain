---
title: "SWMM5 Quizzer (app)"
type: entity
updated: 2026-11-15
sources: [S138, S140]
tags: [apps, replit, swmm5, education, quiz]
reviewed: no
---
Bob's Replit app SWMM5 Quizzer: a quiz app of multiple-choice questions about EPA SWMM, with practice and timed modes, explanations, topic diagrams and a Simulation Quiz on stored network scenarios; it does not run the EPA SWMM engine. Version 1.0.0, at `swmm5quiz.com` and `quiz-master-robertdickinson.replit.app` [S138](../sources/S138-swmm5-quizzer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S138](../sources/S138-swmm5-quizzer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S138](../sources/S138-swmm5-quizzer-replit-summary.md)
- It does not run the EPA SWMM engine. `engines: none`. Hydraulic results, scenario questions, answers and explanations are data in `client/src/data/`.
- A quiz shuffles the question array with `Math.random()` and takes the first 25 questions.
- Counted from its data: 250 quiz question objects, 3 simulation scenario objects, 4 home-page category cards, 5 base diagram entries and 4 enhanced diagram entries. The app has 5 frontend route patterns.
- Category quiz routes show a category label but select from the full question array without filtering.
- The selector describes a timed mode with a per-question limit, but the quiz only tracks elapsed time and does not enforce a deadline.
- The Simulation Quiz introduction says a SWMM simulation runs, but the implementation selects prewritten scenario data and changes display phases.
- A code comment says 220 questions and the documentation page says 125, while the current question array contains 250.
- The server defines `POST /api/quiz/submit` and `GET /api/quiz/attempts`, held in process memory. The checked frontend does not call them.
- `npm run check` passed. No test script is defined. `/`, `/quiz`, `/simulation-quiz` and `/docs` loaded with no app console errors.
- The root `package.json` declares MIT. `units: US customary`.

**What it does not show.** Quiz interactions, API writes, the production pages, responsive layouts and `npm run build` were not checked. No independent human review of technical accuracy or of the stored simulation results is recorded. [S138](../sources/S138-swmm5-quizzer-replit-summary.md)

**Noted at ingest.** The app goes by three names: SWMM5 Quizzer in the file, quiz-master in its `file:` and SWMM5QuizMaster as a Replit project (Q77). The `date:` is the day of the summary; the change list runs from 16 August 2025 to 22 February 2026 (Q75). Its `repo:` is on an internal Replit host, not GitHub (Q79). The four faults above are Replit Agent's reading and were not rerun (Q76). A second quiz app, [SWMM5Wiki (app)](swmm5wiki.md) [S140](../sources/S140-swmm5wiki-replit-summary.md), was ingested with it.

See [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [SWMM5Wiki (app)](swmm5wiki.md), [InfoDrainage Explorer (app)](infodrainage-explorer.md).

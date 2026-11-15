---
title: "S138: SWMM5 Quizzer, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/quiz-master-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, education, quiz]
reviewed: no
---
**What it is.** A technical summary of SWMM5 Quizzer, version 1.0.0: a quiz app of multiple-choice questions about EPA SWMM, with practice and timed modes, explanations, topic diagrams and a Simulation Quiz on stored network scenarios; it does not run the EPA SWMM engine. It is one of Bob's Replit apps, at `swmm5quiz.com` and `quiz-master-robertdickinson.replit.app`. Raw file: [raw/apps/quiz-master-robertdickinson-v1.0.0.md](../../raw/apps/quiz-master-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the checked project files and Git history do not record AI tools used to build it. The copy here was read out of the editor of the Replit project named SWMM5QuizMaster on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** Quiz interactions, API writes, the production pages, responsive layouts and `npm run build` were not checked. No independent human review of technical accuracy or of the stored simulation results is recorded.

**Checked at ingest.** The app goes by three names: SWMM5 Quizzer in the file, quiz-master in its `file:` and SWMM5QuizMaster as a Replit project (Q77). The `date:` is the day of the summary; the change list runs from 16 August 2025 to 22 February 2026 (Q75). Its `repo:` is on an internal Replit host, not GitHub (Q79). The four faults above are Replit Agent's reading and were not rerun (Q76). A second quiz app, [SWMM5Wiki (app)](../entities/swmm5wiki.md) [S140](S140-swmm5wiki-replit-summary.md), was ingested with it.

**Feeds:** [SWMM5 Quizzer (app)](../entities/swmm5-quizzer.md), [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [SWMM5Wiki (app)](../entities/swmm5wiki.md), [InfoDrainage Explorer (app)](../entities/infodrainage-explorer.md).

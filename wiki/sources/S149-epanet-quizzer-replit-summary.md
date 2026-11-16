---
title: "S149: EPANET Quizzer, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/epanet-quizzer-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, epanet, education, quiz]
reviewed: no
---
**What it is.** A technical summary of EPANET Quizzer, version 1.0.0: a quiz app of multiple-choice questions on hydraulic modeling and water distribution in four categories, with timed and practice modes, worked explanations and a topic breakdown; it does not run EPANET. It is one of Bob's Replit apps, at `epanetquizzer.com`. Raw file: [raw/apps/epanet-quizzer-robertdickinson-v1.0.0.md](../../raw/apps/epanet-quizzer-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the checked source, documentation and Git log do not identify AI tools used to build it. The copy here was read out of the editor of the Replit project named EpanetQuizzer on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It teaches EPANET concepts and does not run EPANET simulations or calculate hydraulic results. `engines: none`.
- 250 questions in four categories: Hydraulic Fundamentals 70, Network Components 70, Water Quality Modeling 60 and Advanced Analysis 50. Some question records are generated from templates.
- The score is `round(correct answers / total questions * 100)`; each topic percentage is `round(correct answers in topic / questions in topic * 100)`.
- Timed mode counts down from each question's configured time limit; practice mode does not.
- Missed questions get a first review after 1 day. When a missed question is marked correct, the interval is multiplied by 2.5 and capped at 30 days.
- Questions, users, sessions and progress are held in server memory; a restart clears user and quiz data. Anonymous users are identified by an `httpOnly` cookie with a one-year maximum age.
- `npm run check` failed with 2 TypeScript errors. No `test` script. The home, quiz and results pages rendered without browser errors.
- It links the U.S. EPA EPANET page, EPANET documentation on Read the Docs and OpenWaterAnalytics/EPANET on GitHub. Project license MIT. `units: both`.

**Limits it states.** The hydraulic facts and worked solutions have not been checked by a subject-matter reviewer. A full quiz was not completed in the browser, and `npm run build` was not run.

**Checked at ingest.** It holds 250 questions, as does the [SWMM5 Quizzer (app)](../entities/swmm5-quizzer.md) [S138](S138-swmm5-quizzer-replit-summary.md); they are separate apps on different subjects. The `date:` is the day of the summary; the change list is from 11 and 12 February 2026 (Q75).

**Feeds:** [EPANET Quizzer (app)](../entities/epanet-quizzer.md), [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [SWMM5 Quizzer (app)](../entities/swmm5-quizzer.md), [EPANET for SWMM5 Experts (app)](../entities/epanet-for-swmm5-experts.md).

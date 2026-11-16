---
title: "EPANET Quizzer (app)"
type: entity
updated: 2026-11-15
sources: [S138, S149]
tags: [apps, replit, epanet, education, quiz]
reviewed: no
---
Bob's Replit app EPANET Quizzer: a quiz app of multiple-choice questions on hydraulic modeling and water distribution in four categories, with timed and practice modes, worked explanations and a topic breakdown; it does not run EPANET. Version 1.0.0, at `epanetquizzer.com` [S149](../sources/S149-epanet-quizzer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S149](../sources/S149-epanet-quizzer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S149](../sources/S149-epanet-quizzer-replit-summary.md)
- It teaches EPANET concepts and does not run EPANET simulations or calculate hydraulic results. `engines: none`.
- 250 questions in four categories: Hydraulic Fundamentals 70, Network Components 70, Water Quality Modeling 60 and Advanced Analysis 50. Some question records are generated from templates.
- The score is `round(correct answers / total questions * 100)`; each topic percentage is `round(correct answers in topic / questions in topic * 100)`.
- Timed mode counts down from each question's configured time limit; practice mode does not.
- Missed questions get a first review after 1 day. When a missed question is marked correct, the interval is multiplied by 2.5 and capped at 30 days.
- Questions, users, sessions and progress are held in server memory; a restart clears user and quiz data. Anonymous users are identified by an `httpOnly` cookie with a one-year maximum age.
- `npm run check` failed with 2 TypeScript errors. No `test` script. The home, quiz and results pages rendered without browser errors.
- It links the U.S. EPA EPANET page, EPANET documentation on Read the Docs and OpenWaterAnalytics/EPANET on GitHub. Project license MIT. `units: both`.

**What it does not show.** The hydraulic facts and worked solutions have not been checked by a subject-matter reviewer. A full quiz was not completed in the browser, and `npm run build` was not run. [S149](../sources/S149-epanet-quizzer-replit-summary.md)

**Noted at ingest.** It holds 250 questions, as does the [SWMM5 Quizzer (app)](swmm5-quizzer.md) [S138](../sources/S138-swmm5-quizzer-replit-summary.md); they are separate apps on different subjects. The `date:` is the day of the summary; the change list is from 11 and 12 February 2026 (Q75).

See [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [SWMM5 Quizzer (app)](swmm5-quizzer.md), [EPANET for SWMM5 Experts (app)](epanet-for-swmm5-experts.md).

---
title: "Replit apps: six more summaries"
type: concept
updated: 2026-11-15
sources: [S137, S138, S139, S140, S141, S142]
tags: [apps, replit, verification, ai-agents]
reviewed: 11/16/2026
---
Six more of Bob's Replit apps got a technical summary from Replit Agent on 15 November 2026, after the twenty-one on [Replit apps: the second seventeen summaries](replit-app-summaries-second-batch.md). They were ingested the same evening as [S137](../sources/S137-swmm-documents-explorer-replit-summary.md) to [S142](../sources/S142-icm-prn-file-reader-replit-summary.md). Each ends by saying that Replit Agent wrote it and that Bob has not yet reviewed it (Q74).

**The apps**

| App | Site name | Replit project | Source |
|---|---|---|---|
| [SWMM Documents Explorer (app)](../entities/swmm-documents-explorer.md) | `swmm-documents-explorer` | SWMM-Documents-Explorer | [S137](../sources/S137-swmm-documents-explorer-replit-summary.md) |
| [SWMM5 Quizzer (app)](../entities/swmm5-quizzer.md) | `swmm5quiz.com` | SWMM5QuizMaster | [S138](../sources/S138-swmm5-quizzer-replit-summary.md) |
| [SWMMCRAFT, infiltration simulator (app)](../entities/swmmcraft-infiltration-simulator.md) | `swmm-infiltration--robertdickinson` | SWMM-Infiltration | [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md) |
| [SWMM5Wiki (app)](../entities/swmm5wiki.md) | `gatorbeaverswmm.com` | GatorSWMM | [S140](../sources/S140-swmm5wiki-replit-summary.md) |
| [BobSWMM Writer (app)](../entities/bobswmm-writer.md) | `snagit-video-article--robertdickinson` | BobSWMMWriter | [S141](../sources/S141-bobswmm-writer-replit-summary.md) |
| [ICM PRN File Reader (app)](../entities/icm-prn-file-reader.md) | `icm-reader-robertdickinson` | ICMReader | [S142](../sources/S142-icm-prn-file-reader-replit-summary.md) |

Site names are `.replit.app` names except the two given in full. Six that came after these are on [Replit apps: a fourth set of six summaries](replit-app-summaries-fourth-batch.md).

**In common.** All six give `engines: none` and run no simulation [S137](../sources/S137-swmm-documents-explorer-replit-summary.md) [S138](../sources/S138-swmm5-quizzer-replit-summary.md) [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md) [S140](../sources/S140-swmm5wiki-replit-summary.md) [S141](../sources/S141-bobswmm-writer-replit-summary.md) [S142](../sources/S142-icm-prn-file-reader-replit-summary.md). None records a human review. Each was checked on the development copy, not the published site.

**Where they differ**
- Tests. One has a suite, and all 24 of its tests pass [S142](../sources/S142-icm-prn-file-reader-replit-summary.md). The other five have no test script.
- TypeScript checks pass in three [S137](../sources/S137-swmm-documents-explorer-replit-summary.md) [S138](../sources/S138-swmm5-quizzer-replit-summary.md) [S142](../sources/S142-icm-prn-file-reader-replit-summary.md) and fail in three: 2 errors [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md), 1 [S140](../sources/S140-swmm5wiki-replit-summary.md) and 1 [S141](../sources/S141-bobswmm-writer-replit-summary.md).
- One calls AI models when it runs: Claude for text and Gemini for transcription [S141](../sources/S141-bobswmm-writer-replit-summary.md).
- What they are. One reads model output, InfoWorks ICM PRN files [S142](../sources/S142-icm-prn-file-reader-replit-summary.md). One computes infiltration in its own code [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md). Two are quizzes [S138](../sources/S138-swmm5-quizzer-replit-summary.md) [S140](../sources/S140-swmm5wiki-replit-summary.md), one is a guide to a document archive [S137](../sources/S137-swmm-documents-explorer-replit-summary.md) and one is a writing tool [S141](../sources/S141-bobswmm-writer-replit-summary.md).
- Where they keep data: in server memory [S138](../sources/S138-swmm5-quizzer-replit-summary.md) [S140](../sources/S140-swmm5wiki-replit-summary.md) [S142](../sources/S142-icm-prn-file-reader-replit-summary.md), in PostgreSQL [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md) [S141](../sources/S141-bobswmm-writer-replit-summary.md), or in constants in the page [S137](../sources/S137-swmm-documents-explorer-replit-summary.md).

**What Replit Agent reported as doubtful.** None was rerun (Q76). A rainfall loop that puts 1.5 inches into a 1-hour storm at 1 inch/hour [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md). A Simulation Quiz that says a SWMM simulation runs and shows stored results [S138](../sources/S138-swmm5-quizzer-replit-summary.md). A model menu that offers Gemini and sends the request to Claude [S141](../sources/S141-bobswmm-writer-replit-summary.md). Uploaded PRN files returned without authentication [S142](../sources/S142-icm-prn-file-reader-replit-summary.md). One reported difference may not be one: the two Curve Number denominators are equal when `Ia = 0.2 * S` (our algebra, Q82) [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md).

**Names.** Four names do not say what the app is: SWMMCRAFT for an infiltration calculator, SWMM5Wiki at gatorbeaverswmm.com, BobSWMM Writer at snagit-video-article, and SWMM5 Quizzer at quiz-master (Q77).

See [Replit apps and the summaries Replit Agent wrote](replit-app-summaries.md), [Replit apps: the second seventeen summaries](replit-app-summaries-second-batch.md).

---
title: "S290: SWMM Evidence Board, app .md (v1.0.0)"
type: source
raw: raw/apps/swmm-evidence-board-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-17
ingested: 2026-11-18
tags: [apps, tacit-knowledge, diagnosis, teaching, swmm5, corpus]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app SWMM Evidence Board, version 1.0.0: eight SWMM models, seven with one planted fault and one clean control, cut into report tiles; the page logs which tiles an experienced modeler opens and in five cases locks the tile that points at the fault until a first diagnosis. Raw file: [raw/apps/swmm-evidence-board-v1.0.0.md](../../raw/apps/swmm-evidence-board-v1.0.0.md).

**How it was written.** The app ships this file. The file says it was built with Claude (Anthropic) at Bob's direction.

**Claims worth keeping** (all copied from the file)
- All 16 faulty and corrected runs finished in EPA SWMM 5.2.4 without error; one line changed in Cases 1, 2, 3, 5, 7 and 8, two in Case 4, none in Case 6 (the control).
- 101 of 104 numbers in the answer tables were found as text in the engine's .rpt and .inp; the other three were read from the .out (1,135.05 and 1,904.701 cfs) or computed (0.345 = 0.707 in / 2.05 in).
- Two planned faults were rejected by the engine and not used.
- Cases come from the public 1729 corpus, plus one generated lift station.

**Limits it states.** One interviewee and eight cases are anecdotes with a control, not statistics; self-scoring after seeing the answer; the log records tiles opened, not what was read; answers are in the page source. It keeps shared answers in the claude.ai database, which a Netlify copy does not have.

**Checked at ingest.** 0.707 / 2.05 = 0.345 (our arithmetic). The `links:` line names no Netlify address.

**Feeds:** [SWMM Evidence Board (app)](../entities/swmm-evidence-board.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [The top 25 problems in 31 years of forum threads](../concepts/forum-problems-top-25.md), [Reading SWMM output](../concepts/reading-swmm-output.md).

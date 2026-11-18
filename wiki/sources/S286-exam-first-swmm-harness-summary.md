---
title: "S286: Exam-First SWMM Harness, summary written from the page (v2026-10-19)"
type: source
raw: raw/apps/swmm5-swmm6-loop-harness-v2026-10-19.md
kind: app-md
author: Robert Dickinson
published: 2026-10-19
ingested: 2026-11-18
tags: [apps, calibration, testing, swmm5, swmm6, held-out, defects]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Exam-First SWMM Harness, version 2026-10-19: a calibration and testing harness built on "write the exam before the code": a frozen exam, a loop that rewrites the settings block of harness.py keeping an edit only when held-out scores improve, and a sealed set opened once, around EPA SWMM 5.2.4 and OpenSWMM 6.0.0-alpha.4 pinned by SHA-256. Raw file: [raw/apps/swmm5-swmm6-loop-harness-v2026-10-19.md](../../raw/apps/swmm5-swmm6-loop-harness-v2026-10-19.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/KECKQ6HYSkBn6dq5sKs5zk, version 1792451500-0250 (index.html, 663,394 bytes, SHA-256 893ff4c1a4102ee27c7ef2ef9df75d0b29718f7505677ab09d8ac100a50448e6), its Brief, About and Doc tabs read in headless Chromium on 2026-11-18. The page gives no version number; the version above is its build date. Nothing was run to write this file." The page says the harness, exam, loop, tests, engine builds and page were made with Claude in one session on 2026-10-19 under Bob's direction; the proposer that wrote the edits is a rule table Claude wrote, not a language model, and "v00 is the human's guess" is a stand-in Claude wrote.

**Claims worth keeping** (all copied from the file)
- 41 rounds of 8 edits (2,148 question gradings, 8 rewrites kept): held-out score 0.496 to 0.807, sealed score 0.637 to 0.715; detector 9 of 12 to 12 of 12 on sealed pairs; sealed calibration fell 0.524 to 0.430 while its held-out score rose 0.408 to 0.613.
- DR-1: OpenSWMM 6 (swmm6_rel 3c30f1e6) writes its internal node type straight into the .out, where 2 means storage and 3 divider, but its internal enum has DIVIDER = 2 and STORAGE = 3; the engine already has internal_to_c_node_type() for the conversion. A one-line fix was built and checked.
- DR-2: on network P17 (five junctions SWMM 5.2.4 never surcharges), FLOW_ROUTING FV reports 79.2 ft at J2 and 103.4 ft at J3, which are 11.50 and 12.75 ft deep, with routing continuity 0.0%; the spike disappears only at a 0.5 s step; cause undiagnosed.
- Every score is an engine run graded by the frozen grader; the engines give byte-identical .out files run to run.

**Limits it states.** No field data (a twin experiment); small generated networks, not the corpus; six whole-model parameters; one proposer, one loop seed, one machine; no person has reviewed the exam, key or defect register.

**Checked at ingest.** DR-1 agrees with what [S69](S69-swmm6-code-house-app-md.md) found reading the same output plugin (DIVIDER stored as 2 and STORAGE as 3) and [S72](S72-li-swmm6-code-house-article.md) saw in a real file. The `links:` line gives Netlify as https://swmm5-swmm6-loop-harness.netlify.app.

**Feeds:** [Exam-First SWMM Harness (app)](../entities/exam-first-swmm-harness.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [The SWMM findings register](../concepts/findings-register.md).

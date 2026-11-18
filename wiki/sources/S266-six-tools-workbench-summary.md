---
title: "S266: Six Tools Workbench, summary written from the page (v1.1)"
type: source
raw: raw/apps/six-tools-workbench-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-11
ingested: 2026-11-17
tags: [apps, code-quality, swmm5, swmm6, icm, ai-agents]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Six Tools Workbench, version 1.1: Robert C. Martin's six public agent-built tools (bookwriter, scriptwriter, crapper, mutator, dryer, uml-viewer) shown at toy size in the browser, with results from rebuilt versions of the four code tools run on EPA SWMM 5.2.4, OpenSWMM 6 and Autodesk's public ICM Ruby scripts. The real-code results are a fixed snapshot. Raw file: [raw/apps/six-tools-workbench-v1.1.md](../../raw/apps/six-tools-workbench-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1791651656-f2f7, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The published page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session. The summary says the Netlify copy adds a one-line AI-use note.

**Claims worth keeping** (all copied from the file)
- His repositories were read on 10 October 2026 at commits bookwriter 236ff41, scriptwriter fa26c24, crapper 9f1bead, mutator c57f038, dryer 66ff6d2 and uml-viewer f65dafe; the scoring rules follow their READMEs and source.
- CRAP scores (complexity squared, discounted by coverage cubed), mutation testing with models as the tests, duplicate finding and a component map were measured on the real engine code by a toolkit, swmm-quality-tools, that came out of the session.
- Real-code sources: EPA SWMM tag v5.2.4 (7952ca8); openswmm.engine swmm6_rel at a070e98; Open-Source-Support at 58d610e; models from the 1729 corpus at 70b8f6e; coverage from a subset of 3,099 models. For a simulation engine the tests are models, not unit tests.
- The Writers tab's sample book is about one 24 in pipe: at 0.5 percent slope and n = 0.013 it carries 17.2 cfs at 22.5 in deep and 16.0 cfs full.

**Limits it states.** The toy tabs are miniatures read through a different parser, so Dryer's scores can differ a little from the real tool's. The real-code results are a snapshot of 10 and 11 October 2026.

**Checked at ingest.** Manning for a full 24 in pipe at S 0.005, n 0.013: (1.486 / 0.013) x 3.142 x 0.5^(2/3) x 0.005^0.5 = 16.0 cfs (our arithmetic). The summary gives none of the CRAP or mutation scores themselves. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://six-tools-workbench.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Six Tools Workbench (app)](../entities/six-tools-workbench.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md).

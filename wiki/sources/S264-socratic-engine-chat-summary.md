---
title: "S264: Socratic Engine Chat, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/socratic-engine-chat-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-19
ingested: 2026-11-17
tags: [apps, ai-agents, teaching, engine-chat]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Socratic Engine Chat, version 1.0.0: a working demonstration of the socratic-engine-chat pattern Bob proposed: a plain-English chat over a deliberately small engine (Manning's formula for five pipes flowing full) that keeps three promises: every number comes from the engine, nothing changes without the user's click, and in Learn mode the user predicts before the engine answers. Raw file: [raw/apps/socratic-engine-chat-v1.0.0.md](../../raw/apps/socratic-engine-chat-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792424805-980c, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in October 2026 at Bob's direction; Bob proposed the pattern and asked for this demonstration and the essay. Claude wrote the engine-chat kernel, the Manning engine and its tools, the phrase list, the tests and the essay; the essay opens in Bob's voice with his own history, and its historical remarks have not been checked by a person.

**Claims worth keeping** (all copied from the file)
- Numbers not traced to an engine call, the user's words or a declared constant are highlighted as unsourced.
- Change requests come back as dry runs with Apply and an exact Undo. The opening exercise asks the user to fix the overloaded pipe P3 ("set slope of P3 to 0.002", "set diameter of P3 to 18").
- Three carriers share one tool list: Claude inside the claude.ai viewer (spending the viewer's own usage and asking permission first), a phrase list that works anywhere with no AI, and a third the page describes.
- Tests: the kernel 43 checks, the engine and router 125, and 55 checks of the finished page in headless Chromium with a stand-in for Claude; faults were planted on purpose for the tests to catch.

**Limits it states.** No test talked to the real Claude, and no person has used the app from end to end. On an ordinary web host the Claude carrier is unavailable and the phrase list answers. The engine is deliberately small.

**Checked at ingest.** Nothing in the summary can be checked by arithmetic, and it reports no use of the pattern inside an engine app. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://socratic-engine-chat.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Socratic Engine Chat (app)](../entities/socratic-engine-chat.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [SWMM Run Supervisor (app)](../entities/swmm-run-supervisor.md), [App build contract (four working principles)](../concepts/app-build-contract.md).

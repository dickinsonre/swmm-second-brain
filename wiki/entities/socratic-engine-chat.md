---
title: "Socratic Engine Chat (app)"
type: entity
updated: 2026-11-17
sources: [S205, S264]
tags: [apps, ai-agents, teaching, engine-chat]
reviewed: no
---
Bob's app Socratic Engine Chat: a working demonstration of the socratic-engine-chat pattern Bob proposed: a plain-English chat over a deliberately small engine (Manning's formula for five pipes flowing full) that keeps three promises: every number comes from the engine, nothing changes without the user's click, and in Learn mode the user predicts before the engine answers. Version 1.0.0, 2026-10-19 [S264](../sources/S264-socratic-engine-chat-summary.md). Netlify address: https://socratic-engine-chat.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S264](../sources/S264-socratic-engine-chat-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S264](../sources/S264-socratic-engine-chat-summary.md)
- Numbers not traced to an engine call, the user's words or a declared constant are highlighted as unsourced.
- Change requests come back as dry runs with Apply and an exact Undo. The opening exercise asks the user to fix the overloaded pipe P3 ("set slope of P3 to 0.002", "set diameter of P3 to 18").
- Three carriers share one tool list: Claude inside the claude.ai viewer (spending the viewer's own usage and asking permission first), a phrase list that works anywhere with no AI, and a third the page describes.
- Tests: the kernel 43 checks, the engine and router 125, and 55 checks of the finished page in headless Chromium with a stand-in for Claude; faults were planted on purpose for the tests to catch.

**What it does not show.** No test talked to the real Claude, and no person has used the app from end to end. On an ordinary web host the Claude carrier is unavailable and the phrase list answers. The engine is deliberately small. [S264](../sources/S264-socratic-engine-chat-summary.md)

**Noted at ingest.** Nothing in the summary can be checked by arithmetic, and it reports no use of the pattern inside an engine app.

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [SWMM Run Supervisor (app)](swmm-run-supervisor.md), [App build contract (four working principles)](../concepts/app-build-contract.md).

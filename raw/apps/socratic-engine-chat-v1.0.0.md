---
name: Socratic Engine Chat
file: socratic-engine-chat.html
version: 1.0.0
date: 2026-10-19
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/BfqnFvNcZ3R7GXEZbn38zG", repo: none named in the page}
engines:
  - {name: Manning engine, note: "Manning's formula for five pipes flowing full, with tools for the chat"}
units: US customary
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude at Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/BfqnFvNcZ3R7GXEZbn38zG, version 1792424805-980c (index.html, 179,459 bytes, SHA-256 78e4cc22e19713186c8696060bacbd544f1f6549efd2b4a65352f253da64bdff), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file; the date is the artifact's publish date."
---

# Socratic Engine Chat: ask the engine in plain English, and guess first

## In three points
- **What:** A working demonstration of the socratic-engine-chat pattern: a plain-English chat over a small engine (Manning's formula for five pipes flowing full) that keeps three promises: every number comes from the engine, nothing changes without your click, and in Learn mode you predict before the engine answers.
- **So what:** Numbers not traced to an engine call, your words or a declared constant are highlighted as unsourced, and change requests come back as dry runs with Apply and an exact Undo; the kernel passes 43 tests and the engine and router 125.
- **Now what:** Use it to see the pattern before adding it to a real engine app. On an ordinary web host the Claude carrier is unavailable and the phrase list answers; no test has talked to the real Claude.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0.0"); the date is the artifact's. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Ask, Model, Ledger (every engine call), Doc, About. Three carriers share one tool list: Claude inside the claude.ai viewer (it may call the same tools in Work mode, or turn a sentence into one tool call in Learn mode, spending the viewer's own usage and asking permission first); the phrase list, which works anywhere with no AI; and a third carrier described in the page. The opening exercise asks you to fix the overloaded pipe P3 ("set slope of P3 to 0.002", "set diameter of P3 to 18") and read each dry run before applying it.

## Checks (as stated on the page)

- Node tests of the kernel (43 checks) and of the engine and router (125).
- 55 checks of the finished page in headless Chromium with a stand-in for Claude.
- Faults planted on purpose that the tests had to catch; a contrast check of both themes.
- Every engineering number in the essay computed by running code.

## What this does not show

- No test talked to the real Claude.
- No person has used the app from end to end.
- The essay's historical remarks have not been checked by a person.
- The engine is deliberately small.

## How to reproduce

Open the page; answer the opening question on Ask, then try the P3 fixes.

## Credits and licenses

No license is stated in the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, in October 2026, at the direction of Robert (Bob) Dickinson, who proposed the socratic-engine-chat pattern and asked for this demonstration and the essay. Claude wrote the engine-chat kernel, the Manning engine and its tools, the phrase list, the page and its tests, the essay and its Word file. The essay opens in Bob's voice with his own history (University of Florida from 1973, SWMM 2.5 from 1978). This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0.0: first version.

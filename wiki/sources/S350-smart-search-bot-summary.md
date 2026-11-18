---
title: "S350: Smart Search Bot, summary written from the page (v1.0)"
type: source
raw: raw/apps/smart-search-bot-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, ai, search, swmm5, fact-checking]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Smart Search Bot, version 1.0: answer a SWMM5 question, then check every sentence. Raw file: [raw/apps/smart-search-bot-v1.0.md](../../raw/apps/smart-search-bot-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/EnZCDe4PjCUJqqe3XTiMYC, version 1792949339-c783 (index.html, 1,805,231 bytes, SHA-256 2ed98c34269982ba82f69ca0b8e66847efa39e71713180aefe0812749d387a0a), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says it was built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable app and asked for the rebuild; Claude ran the original code to measure its defects, built the library and the engine with its tests, wrote the Netlify function and its tests, and wrote the page and the Doc."

**Claims worth keeping** (all copied from the file)
- A one-file rebuild of Bob's Lovable app BobSWMM Auto-Research. It answers a SWMM5 question in four stages (plan, retrieve, synthesize, validate) and marks every sentence of the result by what backs it. Its library is 1,621 passages cut from the EPA SWMM 5.2.4 engine source (at tag v5.2.4, 7952ca8) and PySWMM (commit 97cb36f), each keeping its file and lines.
- The Lovable app needed a server with a Lovable AI key and a Perplexity key. Here, inside claude.ai Claude plans, writes and checks on the viewer's own account; elsewhere the user's own Anthropic key works from the browser; library search needs nothing. The Lovable code, run in Node on a test report, showed the defects on the Fixes tab (12), among them formatted sentences losing their colour and a citation after a full stop moving to the next sentence.
- The Lovable code bundled with stubs for its UI kit and run in Node on a test report; every defect number on the Fixes tab comes from that harness.
- The engine (search, retrieval, sentence cutting, audit) has 23 assertions in a Node test file, run against the real library: citations after a full stop, abbreviations, code spans, bullets, tables, the Sources section, hedges, use counts, and retrieval that gives every query a share.
- All 104 library files re-fetched from GitHub at the pinned refs: 104 answered 200 and 104 were byte-identical to the clone.
- The recorded run's retrieval recomputed on every load and compared with its recorded source list.

**Limits it states.** As the page lays out: what each deployment can and cannot do (above); the sentence audit says what backs a sentence, not that the sentence is right.

**Checked at ingest.** Its Lovable original is named BobSWMM Auto-Research, the name of the Replit app on [bobSWMM Auto Research (app)](../entities/bobswmm-auto-research.md); whether the two share code is not stated (Q119). Its Netlify package lacks the function file netlify/functions/smart-search.mjs that the page calls. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Smart Search Bot (app)](../entities/smart-search-bot.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [bobSWMM Auto Research (app)](../entities/bobswmm-auto-research.md).

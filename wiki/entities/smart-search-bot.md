---
title: "Smart Search Bot (app)"
type: entity
updated: 2026-11-18
sources: [S350]
tags: [apps, ai, search, swmm5, fact-checking]
reviewed: no
---
Bob's app Smart Search Bot: answer a SWMM5 question, then check every sentence. Version 1.0, 2026-10-25 [S350](../sources/S350-smart-search-bot-summary.md). Its `links:` line names no live Netlify address [S350](../sources/S350-smart-search-bot-summary.md).

**A caution about its source.** The page ships no technical summary. [S350](../sources/S350-smart-search-bot-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S350](../sources/S350-smart-search-bot-summary.md)
- A one-file rebuild of Bob's Lovable app BobSWMM Auto-Research. It answers a SWMM5 question in four stages (plan, retrieve, synthesize, validate) and marks every sentence of the result by what backs it. Its library is 1,621 passages cut from the EPA SWMM 5.2.4 engine source (at tag v5.2.4, 7952ca8) and PySWMM (commit 97cb36f), each keeping its file and lines.
- The Lovable app needed a server with a Lovable AI key and a Perplexity key. Here, inside claude.ai Claude plans, writes and checks on the viewer's own account; elsewhere the user's own Anthropic key works from the browser; library search needs nothing. The Lovable code, run in Node on a test report, showed the defects on the Fixes tab (12), among them formatted sentences losing their colour and a citation after a full stop moving to the next sentence.
- The Lovable code bundled with stubs for its UI kit and run in Node on a test report; every defect number on the Fixes tab comes from that harness.
- The engine (search, retrieval, sentence cutting, audit) has 23 assertions in a Node test file, run against the real library: citations after a full stop, abbreviations, code spans, bullets, tables, the Sources section, hedges, use counts, and retrieval that gives every query a share.
- All 104 library files re-fetched from GitHub at the pinned refs: 104 answered 200 and 104 were byte-identical to the clone.
- The recorded run's retrieval recomputed on every load and compared with its recorded source list.

**How to use it, as the summary puts it.** Use it to research SWMM5 questions with each sentence traced to the engine or PySWMM source. On a plain Netlify deploy there is no Perplexity web search and no HTTP status check of web links, which need the page's Netlify function; the page names that function, smart-search.mjs, but it is not inside the published page. [S350](../sources/S350-smart-search-bot-summary.md)

**What it does not show.** As the page lays out: what each deployment can and cannot do (above); the sentence audit says what backs a sentence, not that the sentence is right. [S350](../sources/S350-smart-search-bot-summary.md)

**Noted at ingest.** Its Lovable original is named BobSWMM Auto-Research, the name of the Replit app on [bobSWMM Auto Research (app)](bobswmm-auto-research.md); whether the two share code is not stated (Q119). Its Netlify package lacks the function file netlify/functions/smart-search.mjs that the page calls.

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [bobSWMM Auto Research (app)](bobswmm-auto-research.md).

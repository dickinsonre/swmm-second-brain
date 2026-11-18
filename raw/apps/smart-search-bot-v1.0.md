---
name: Smart Search Bot
file: smart-search-bot.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/EnZCDe4PjCUJqqe3XTiMYC", original: "Lovable app BobSWMM Auto-Research (its README calls it Smart Search Bot; MIT)", repo: none named in the page}
engines: none (a retrieval and sentence-audit engine over a 1,621-passage library of EPA SWMM 5.2.4 and PySWMM source; the language model is Claude, on the viewer's account inside claude.ai or the user's own Anthropic key elsewhere)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 25 October 2026 under Robert Dickinson's direction, and that in use it calls Claude to plan, write and check. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/EnZCDe4PjCUJqqe3XTiMYC, version 1792949339-c783 (index.html, 1,805,231 bytes, SHA-256 2ed98c34269982ba82f69ca0b8e66847efa39e71713180aefe0812749d387a0a), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Smart Search Bot: answer a SWMM5 question, then check every sentence

## In three points
- **What:** A one-file rebuild of Bob's Lovable app BobSWMM Auto-Research. It answers a SWMM5 question in four stages (plan, retrieve, synthesize, validate) and marks every sentence of the result by what backs it. Its library is 1,621 passages cut from the EPA SWMM 5.2.4 engine source (at tag v5.2.4, 7952ca8) and PySWMM (commit 97cb36f), each keeping its file and lines.
- **So what:** The Lovable app needed a server with a Lovable AI key and a Perplexity key. Here, inside claude.ai Claude plans, writes and checks on the viewer's own account; elsewhere the user's own Anthropic key works from the browser; library search needs nothing. The Lovable code, run in Node on a test report, showed the defects on the Fixes tab (12), among them formatted sentences losing their colour and a citation after a full stop moving to the next sentence.
- **Now what:** Use it to research SWMM5 questions with each sentence traced to the engine or PySWMM source. On a plain Netlify deploy there is no Perplexity web search and no HTTP status check of web links, which need the page's Netlify function; the page names that function, smart-search.mjs, but it is not inside the published page.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Research, Map, Library (1,621 passages), Fixes, About, Doc. My sources (PDF included) stay in the tab and only retrieved passages go to Claude; Search-only mode sends nothing anywhere. Where it runs: inside claude.ai, Claude on the viewer's account, library search and my sources; on Netlify with the function, your own Anthropic key, Perplexity web search (with PERPLEXITY_API_KEY set) and real HTTP status of web links; as a plain file, your own key, library search and my sources. The key is held in the tab's memory, never stored.

## Checks (as stated on the page)

- The Lovable code bundled with stubs for its UI kit and run in Node on a test report; every defect number on the Fixes tab comes from that harness.
- The engine (search, retrieval, sentence cutting, audit) has 23 assertions in a Node test file, run against the real library: citations after a full stop, abbreviations, code spans, bullets, tables, the Sources section, hedges, use counts, and retrieval that gives every query a share.
- All 104 library files re-fetched from GitHub at the pinned refs: 104 answered 200 and 104 were byte-identical to the clone.
- The recorded run's retrieval recomputed on every load and compared with its recorded source list.
- The Netlify function tested in Node against a mocked Perplexity and mocked web servers (ping, missing key, refused key reported as 401, both endpoints, HEAD-refusing servers, a 404, a timeout).
- The page driven in headless Chromium: 73 checks in both themes and at phone width.

## What this does not show

As the page lays out: what each deployment can and cannot do (above); the sentence audit says what backs a sentence, not that the sentence is right.

## Credits and licenses

Original app by Robert Dickinson, MIT License, 2026. EPA SWMM 5.2.4 by the US EPA Office of Research and Development (L. Rossman, author of the files quoted), public domain. PySWMM by Bryant E. McDonnell and contributors, BSD 2-Clause. IBM Plex; html2canvas, gif.js and pdf.js from cdnjs.

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable app and asked for the rebuild; Claude ran the original code to measure its defects, built the library and the engine with its tests, wrote the Netlify function and its tests, and wrote the page and the Doc. In use, the page sends the topic, plan, retrieved passages and the briefing's sentences to Claude (claude.ai mode, which asks permission on the first run) or to api.anthropic.com (your-key mode). This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first single-file rebuild (the version read).

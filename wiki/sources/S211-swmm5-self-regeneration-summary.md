---
title: "S211: SWMM5 Self-Regeneration, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/swmm5-self-regeneration-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-26
ingested: 2026-11-17
tags: [apps, swmm5, output, inference, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM5 Self-Regeneration, version 1.0.0: an app that reads only a SWMM5 binary .out, writes a new .inp in four rungs, runs each in EPA SWMM 5.2.4 in the page and diffs every regenerated .out against the original, element by element; the original .inp, when present, is used only to score. Raw file: [raw/apps/swmm5-self-regeneration-v1.0.0.md](../../raw/apps/swmm5-self-regeneration-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793053288-ffa0, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in a session on 26 October 2026 under Bob's direction: Bob posed the question, from an infographic called Can an Object Model Itself?, chose the .out-to-.inp test and set the verification standards; Claude compiled the engine, wrote the inference, the .inp writer and the diff, and ran a 277-model sweep.

**Claims worth keeping** (all copied from the file)
- R1 joins the network with default circles and n = 0.013: 9 % of conduits stay within 10 % of their own peak, median worst-instant error 32 %.
- R2 adds shapes, sizes and Manning's n: every conduit within 10 %, median 5.2 %. R2b lets the engine refine n: median 1.8 %.
- R3 explains the inflows from rain instead of replaying them and still lands within two percent.
- The page's engine run twice on the same .inp writes byte-identical .out files. Against a native gcc build of the same source, 46 of 60 corpus models give byte-identical .out files; the other 14 differ from the last bit onward.
- A 277-model corpus sweep was run, each regenerated .inp scored against its original.
- The engine: tag v5.2.4, built with zig cc 0.17 for wasm32-wasi at -O2, one shim (mkstemp), 524 KB.

**Limits it states.** No field data; one engine. Same .out is not the same .inp. Nothing faster than about two report steps can be recovered.

**Checked at ingest.** The rung results are for the built-in site-drainage demo; the summary gives no rung results for the 277-model sweep. The 14 of 60 that differ browser to native fit the pattern on [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm5-self-regeneration.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM5 Self-Regeneration (app)](../entities/swmm5-self-regeneration.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

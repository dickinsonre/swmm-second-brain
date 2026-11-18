---
title: "SWMM5 Self-Regeneration (app)"
type: entity
updated: 2026-11-17
sources: [S205, S211]
tags: [apps, swmm5, output, inference, wasm]
reviewed: no
---
Bob's app SWMM5 Self-Regeneration: an app that reads only a SWMM5 binary .out, writes a new .inp in four rungs, runs each in EPA SWMM 5.2.4 in the page and diffs every regenerated .out against the original, element by element; the original .inp, when present, is used only to score. Version 1.0.0, 2026-10-26 [S211](../sources/S211-swmm5-self-regeneration-summary.md). Netlify address: https://swmm5-self-regeneration.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S211](../sources/S211-swmm5-self-regeneration-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S211](../sources/S211-swmm5-self-regeneration-summary.md)
- R1 joins the network with default circles and n = 0.013: 9 % of conduits stay within 10 % of their own peak, median worst-instant error 32 %.
- R2 adds shapes, sizes and Manning's n: every conduit within 10 %, median 5.2 %. R2b lets the engine refine n: median 1.8 %.
- R3 explains the inflows from rain instead of replaying them and still lands within two percent.
- The page's engine run twice on the same .inp writes byte-identical .out files. Against a native gcc build of the same source, 46 of 60 corpus models give byte-identical .out files; the other 14 differ from the last bit onward.
- A 277-model corpus sweep was run, each regenerated .inp scored against its original.
- The engine: tag v5.2.4, built with zig cc 0.17 for wasm32-wasi at -O2, one shim (mkstemp), 524 KB.

**What it does not show.** No field data; one engine. Same .out is not the same .inp. Nothing faster than about two report steps can be recovered. [S211](../sources/S211-swmm5-self-regeneration-summary.md)

**Noted at ingest.** The rung results are for the built-in site-drainage demo; the summary gives no rung results for the 277-model sweep. The 14 of 60 that differ browser to native fit the pattern on [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md).

---
title: "SWMM Engine Map (app)"
type: entity
updated: 2026-11-17
sources: [S205, S263]
tags: [apps, swmm5, engines, translation, byte-for-byte]
reviewed: no
---
Bob's app SWMM Engine Map: a hydrocouple.org-style site that maps the SWMM engines Bob's SWMM Enablement work has built or measured (C++, Rust and the translated ports), with EPA SWMM 5.2.4 as the fixed point, and runs four engines in the browser against EPA byte for byte. Version and date 2026-10-29 [S263](../sources/S263-swmm-engine-map-summary.md). Netlify address: https://swmm-engine-map.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S263](../sources/S263-swmm-engine-map-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S263](../sources/S263-swmm-engine-map-summary.md)
- EPA 5.2.4 keeps its state in 415 file- and program-scope variables, so it holds one model per process: opening a second model over the first returns 0 from swmm_open, empties the first report, and leaks 361,322 bytes in 134 allocations under AddressSanitizer.
- The gate: the .out matches EPA's byte for byte, and the .rpt after removing the three wall-clock lines; no tolerance, because a last-bit difference in dynamic wave can change the iteration count at the next step.
- 781 large corpus models are not yet gated by the C++ and Rust engines; the five translated ports are gated on 480 models.
- TypeScript and Java match EPA on FMA/AVX2 processors. Timing is from one two-core machine; SWMM6 is measured on one alpha commit.
- It follows hydrocouple.org's section order and palette with no HydroCouple logo, image or text reused.

**What it does not show.** Not a new or more accurate engine. [S263](../sources/S263-swmm-engine-map-summary.md)

**Noted at ingest.** The gate is the one on [Byte-for-byte gate](../concepts/byte-for-byte-gate.md); the processor condition for TypeScript and Java is the subject of [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md).

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM5 language translations (swmm5-*)](swmm5-language-ports.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [HydroCouple Interactive (app)](hydrocouple-interactive.md).

---
title: "S263: SWMM Engine Map, summary written from the page (v2026-10-29)"
type: source
raw: raw/apps/swmm-engine-map-v2026-10-29.md
kind: app-md
author: Robert Dickinson
published: 2026-10-29
ingested: 2026-11-17
tags: [apps, swmm5, engines, translation, byte-for-byte]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Engine Map, version 2026-10-29: a hydrocouple.org-style site that maps the SWMM engines Bob's SWMM Enablement work has built or measured (C++, Rust and the translated ports), with EPA SWMM 5.2.4 as the fixed point, and runs four engines in the browser against EPA byte for byte. Raw file: [raw/apps/swmm-engine-map-v2026-10-29.md](../../raw/apps/swmm-engine-map-v2026-10-29.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793318466-1416, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the site, its essay and the .docx were made with Claude (Claude Opus 5.5) on 29 October 2026 under Bob's direction: Bob asked for a HydroCouple-style map that answers a review of hydrocouple.org and supplied the corpus and the engines; Claude extracted three WebAssembly engines from the swmm5-rust app, checked their SHA-256 against that repository's manifest, and bundled the TypeScript port.

**Claims worth keeping** (all copied from the file)
- EPA 5.2.4 keeps its state in 415 file- and program-scope variables, so it holds one model per process: opening a second model over the first returns 0 from swmm_open, empties the first report, and leaks 361,322 bytes in 134 allocations under AddressSanitizer.
- The gate: the .out matches EPA's byte for byte, and the .rpt after removing the three wall-clock lines; no tolerance, because a last-bit difference in dynamic wave can change the iteration count at the next step.
- 781 large corpus models are not yet gated by the C++ and Rust engines; the five translated ports are gated on 480 models.
- TypeScript and Java match EPA on FMA/AVX2 processors. Timing is from one two-core machine; SWMM6 is measured on one alpha commit.
- It follows hydrocouple.org's section order and palette with no HydroCouple logo, image or text reused.

**Limits it states.** Not a new or more accurate engine.

**Checked at ingest.** The gate is the one on [Byte-for-byte gate](../concepts/byte-for-byte-gate.md); the processor condition for TypeScript and Java is the subject of [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm-engine-map.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM Engine Map (app)](../entities/swmm-engine-map.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM5 language translations (swmm5-*)](../entities/swmm5-language-ports.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [HydroCouple Interactive (app)](../entities/hydrocouple-interactive.md).

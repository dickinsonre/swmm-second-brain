---
title: "S274: Tri-Pyramid, summary written from the page (v3.0)"
type: source
raw: raw/apps/tri-pyrimid-swmm5-swmm6-v3.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-18
tags: [apps, results, visualization, swmm5, wasm, report-step]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Tri-Pyramid, version 3.0: a demographic-profile chart for a sewer: every node and link binned by fullness, flooding and conduit Froude number, mirrored nodes against links and animated through the run, with EPA SWMM 5.2.4 in the browser. Raw file: [raw/apps/tri-pyrimid-swmm5-swmm6-v3.0.md](../../raw/apps/tri-pyrimid-swmm5-swmm6-v3.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/MbTWrupxYSmMAH7NY1QKWY, version 1792448305-0a48 (index.html, 2,141,577 bytes, SHA-256 b916238adb4108a6b0b158aca111fc759350e3a2409c670cbf12dfc2da225393), its tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says Bob directed the work and chose the borrowing; Claude (Opus 5) built the page and in October 2026 wrote its Doc and drew its figures.

**Claims worth keeping** (all copied from the file)
- The embedded wasm engine, checked by SHA-256, writes a 319,329-byte .out byte-for-byte identical to the one from a native gcc build of 5.2.4.
- 29 of 29 node maximum depths from the .out agree with the .rpt within 0.006 ft (largest 0.0045 ft).
- Share of time each of 27 conduits spent supercritical, from the page's rebuilt geometry against SWMM's Flow Classification Summary: 0.03 percentage points on average, 0.50 at worst.
- Report-step sampling: with a 120 s report step and 5 s routing, the samples caught 31% of link CB1's routing-step peak; 2 of 28 links fall under the app's 80% threshold and 13 more under 99%.

**Limits it states.** No topology by design (a screening view); geometry compared with the engine on one 27-conduit network, not read against xsect.c; parsers not run on the full 3,813-model corpus; large models and other browsers unmeasured.

**Checked at ingest.** The summary says the parsers have not been run on "the full 3,813-model corpus the page can reach"; the corpus README counts 4,540 .inp files as file counts, not distinct networks ([S87](S87-corpus-1729-readme.md) via [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md)). The `links:` line gives Netlify as https://tri-pyrimid-swmm5-swmm6.netlify.app.

**Feeds:** [Tri-Pyramid (app)](../entities/tri-pyramid.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

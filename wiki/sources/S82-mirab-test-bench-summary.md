---
title: "S82: Mirab Test Bench, summary written from the page (v1.0)"
type: source
raw: raw/apps/mirab-test-bench-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-15
tags: [apps, swmm5, swmm5plus, mirab, engine-comparison, findings, wasm, verification]
reviewed: 2026-11-15
---
**What it is.** A technical summary of the app Mirab Test Bench, version 1.0 (24 October 2026): a bench that reads the `.anr` results Ehsan Madadi's Mirab writes, reruns the model in EPA SWMM 5.2.4 in the page, and measures the gap. Raw file: [raw/apps/mirab-test-bench-v1.0.md](../../raw/apps/mirab-test-bench-v1.0.md).

**How it was written. This one is different.** The page carries no summary of its own. Claude (Anthropic, model claude-fable-5-2) wrote the file on 14 November 2026, at Bob's request, from the page's source, its findings register and its embedded evidence record. Nothing was rerun. Bob has not read it (Q52). The app was built with Claude in one session in October 2026 under Bob's direction; the page says no person has reviewed its findings register against the SWMM5+, swmm5plus-capi and Mirab sources.

**Claims worth keeping** (all copied from the page)
- Versions: Mirab 0.2.4 at c9029ef; swmm5plus-capi 0.2.1; SWMM5+ 1.0.3 (CIMM-ORG/SWMM5plus at afd44de) with EPA SWMM 5.1.13 for input and hydrology; EPA SWMM 5.2.4 at 7952ca8.
- Parity of the EPA engine across a native build, Mirab's library and the page's wasm: bit-equal on 7,200, 42,048 and 18,432 `.anr` values in three samples.
- Census of 449 `.inp` files, native glibc against the page's engine: 380 byte-identical, 59 differ, 10 rejected by both. All 59 match a native build linked against musl. Cause given: the math library, not WebAssembly.
- Among the 59: median worst relative difference 6.44e-08; 15 above 1 % and 11 above 10 %.
- SWMM5+ against EPA 5.2.4 on Long Beach sewer: every conduit's peak 25 to 29 % low; median peak change 27.81 %. With a dummy pattern placed first: 0.34 %.
- S-1 (defect, high, confirmed by experiment): SWMM5+ dry-weather inflow ignores the first pattern in `[PATTERNS]`; `interface/api.c:399` tests `if (jj > 0)`.
- S-2 (found by reading, not run): the weekend pattern multiplies the hourly one.
- S-4 and S-5 are open and unexamined by anyone who works on SWMM5+.
- P-1: `realpath()` writes into a 260-byte buffer in EPA 5.2.4 `swmm5.c`.
- The page does not run SWMM5+.

**Limits it states.** Three small circular-pipe dynamic-wave models. No observed flows, so nothing says which engine is more accurate. No speed claims.

**Checked at ingest.** 380 + 59 + 10 = 449. P-1 names the same buffer as the `swmm5.c:1593` defect in [S71](S71-swmm-engines-byte-for-byte-summary.md), found separately by translating the engine. The percentages in the comparison table were computed from stored fractions by the summary. Depths in feet are the summary's conversions from meters.

**Feeds:** [Mirab Test Bench (app)](../entities/mirab-test-bench.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md), [The SWMM findings register](../concepts/findings-register.md).

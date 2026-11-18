---
title: "S222: SWMM5+ Bench, summary written from the page (v1.0)"
type: source
raw: raw/apps/swmm5plus-bench-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-17
tags: [apps, swmm5plus, swmm5, finite-volume, comparison]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM5+ Bench, version 1.0: one SWMM model run through two dynamic-wave engines side by side: CIMM's finite-volume SWMM5+ 1.0.3 through Ehsan Madadi's swmm5plus-capi C interface (recorded runs, or a Live bridge to a local library), and EPA SWMM 5.2.4 compiled into the page; 34 models recorded. Raw file: [raw/apps/swmm5plus-bench-v1.0.md](../../raw/apps/swmm5plus-bench-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792869902-f990, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in a session on 24 October 2026 at Bob's request: Bob chose the subject and pointed at Ehsan Madadi's repositories; Claude checksum-checked the release libraries, wrote the Python driver and the bridge, compiled EPA 5.2.4 natively and to WebAssembly, ran every model in both engines and traced the findings to source.

**Claims worth keeping** (all copied from the file)
- SWMM5+ is about 88,000 lines of modern Fortran built around coarrays and HDF5, usually run in a container; swmm5plus-capi v0.2.1 builds it as an ordinary shared library (interface version 2, EPA SWMM 5.1.13 parser). SWMM5+ is CIMM-ORG/SWMM5plus at afd44de (2024-11-25).
- EXTRAN4 as shipped: EPA floods 178 ac-ft (21.9 ha-m), 15.0 % of the inflow, at two nodes (an upstream end and a node with two links); in SWMM5+ both are faces and cannot flood.
- Changing one weir's Surcharge flag from NO to YES gives both engines the same equivalent-orifice formula above the crown, and the weir peaks come back within 1.9 %.
- Example 1 at five-minute reporting: the SWMM5+ record shows 279,414 ft3 of lateral inflow and 294,105 ft3 of outflow (5.3 % more out than in); subtracting the 14,421 ft3 that subcatchment 8 sends straight to outfall 18 closes the budget to 0.1 %.
- SWMM5+ is explicit: on EXTRAN4 a mean step of 0.119 s and 241,021 steps for eight hours.
- The four Linux files of the v0.2.1 release match the SHA-256 values in its SHA256SUMS. The page's EPA engine wrote a .out byte-identical to native on 32 of 33 models.
- 34 models recorded on Linux x86-64 (2 cores) on 24 October 2026 through s5p_run.py, the driver the bridge uses.

**Limits it states.** No field data, so it cannot say which engine is right on a real system. SWMM5+ does not run in the browser.

**Checked at ingest.** 294,105 - 14,421 = 279,684 ft3 against 279,414 in, a 0.1 % difference (our arithmetic). 241,021 x 0.119 s = 28,681 s, about eight hours. The weir surcharge flag is the same one that moves EXTRAN4 node 82309 from 12.03 ft to 20.28 ft on [SWMM QA Report Bench (app)](../entities/swmm-qa-report-bench.md) [S192](S192-swmm-qa-report-bench-app-md.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm5plus-bench.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM5+ Bench (app)](../entities/swmm5plus-bench.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [SWMM5+ (CIMM finite-volume engine)](../entities/swmm5plus.md), [Mirab Test Bench (app)](../entities/mirab-test-bench.md), [Weirs and outlets](../concepts/weirs-and-outlets.md), [SWMM QA Report Bench (app)](../entities/swmm-qa-report-bench.md).

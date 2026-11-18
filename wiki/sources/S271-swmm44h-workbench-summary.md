---
title: "S271: SWMM 4.4H Workbench, summary written from the page (v2026-10-17)"
type: source
raw: raw/apps/swmm44h-engine-swmm5-import-v2026-10-17.md
kind: app-md
author: Robert Dickinson
published: 2026-10-17
ingested: 2026-11-18
tags: [apps, swmm4, fortran, wasm, conversion, swmm5, history]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM 4.4H Workbench, version 2026-10-17: the 2004 SWMM 4.4H Fortran engine (the CDM/OSU release by Moore, Dickinson and Huber) translated by f2c and compiled to WebAssembly, carried as distributed and with 121 marked corrections, beside EPA SWMM 5.2.4 and a SWMM5-to-SWMM4 deck converter. Raw file: [raw/apps/swmm44h-engine-swmm5-import-v2026-10-17.md](../../raw/apps/swmm44h-engine-swmm5-import-v2026-10-17.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/FnWcKvgsHhJX3ikBL1Qz9i, version 1792424858-74c2 (index.html, 14,110,965 bytes, SHA-256 355b89a17d44d59e3bafc1eb3b9479ac87330381a8543ed94b99da13f06a49f4), its start view and Doc essay read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says it was built with Claude in Claude Code sessions in October 2026 under Bob's direction: Claude wrote the patches, the audit, the corrected source, the converter, the page and its text. Its Doc is an essay in the manner of Isaac Asimov with Claude as narrator; a few historical remarks in it come from Claude's general knowledge and were not checked.

**Claims worth keeping** (all copied from the file)
- The source audit has 95 entries; the corrected source carries 121 changes, each marked; 26 faults were left alone and listed.
- Browser against native gfortran on the Extran example: 8,394 report lines, 7,297 identical; of 1,643 numbers that differ, 1,250 differ in the last digit only, and no printed depth or flow of 1 or more differs by more than 1%.
- After the fixes, 395 of 435 test decks reproduced their stored reports exactly; on 300 converted census models, 218 of 286 that finished in both engines gave the same report apart from two removed print lines.
- Census of 300 SWMM5 models from the 1729 corpus translated to SWMM 4.4H: 252 finished in both generations, 211 had pipes to compare; the middle model's median difference in conduit peak flow is 8.3%; 114 agree within 10% and 53 differ by more than half.
- The converter keeps hydrology and hydraulics only: quality, LID, RDII, groundwater, snow, control rules and outlets are dropped and listed.

**Limits it states.** Which engine is right is not shown (no measurements); differences mix the engines with the translation; Extran is explicit with a fixed step; four register items remain open; Chromium only; the 121 changes and the translator are checked by machine, not read by a person.

**Checked at ingest.** 114 + 24 + 20 + 53 = 211 and 218 + 68 + 5 + 9 = 300, as the census bars and the two-engine table give them (our arithmetic). The `links:` line gives Netlify as https://swmm44h-engine-swmm5-import.netlify.app.

**Feeds:** [SWMM 4.4H Workbench (app)](../entities/swmm44h-workbench.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [SWMM 4 against SWMM 5: the 2006 quality assurance tests](../concepts/swmm4-versus-swmm5-qa-2006.md), [SWMM 4 Twin Engines (app)](../entities/swmm4-twin-engines.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [EXTRAN](../entities/extran.md).

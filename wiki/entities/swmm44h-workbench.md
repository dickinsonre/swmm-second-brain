---
title: "SWMM 4.4H Workbench (app)"
type: entity
updated: 2026-11-19
sources: [S271, S391]
tags: [apps, swmm4, fortran, wasm, conversion, swmm5, history]
reviewed: no
---
Bob's app SWMM 4.4H Workbench: the 2004 SWMM 4.4H Fortran engine (the CDM/OSU release by Moore, Dickinson and Huber) translated by f2c and compiled to WebAssembly, carried as distributed and with 121 marked corrections, beside EPA SWMM 5.2.4 and a SWMM5-to-SWMM4 deck converter. Version and date 2026-10-17 [S271](../sources/S271-swmm44h-workbench-summary.md). Netlify address, from its `links:` line: https://swmm44h-engine-swmm5-import.netlify.app [S271](../sources/S271-swmm44h-workbench-summary.md).

**A caution about its source.** The page ships no technical summary. [S271](../sources/S271-swmm44h-workbench-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S271](../sources/S271-swmm44h-workbench-summary.md)
- The source audit has 95 entries; the corrected source carries 121 changes, each marked; 26 faults were left alone and listed.
- Browser against native gfortran on the Extran example: 8,394 report lines, 7,297 identical; of 1,643 numbers that differ, 1,250 differ in the last digit only, and no printed depth or flow of 1 or more differs by more than 1%.
- After the fixes, 395 of 435 test decks reproduced their stored reports exactly; on 300 converted census models, 218 of 286 that finished in both engines gave the same report apart from two removed print lines.
- Census of 300 SWMM5 models from the 1729 corpus translated to SWMM 4.4H: 252 finished in both generations, 211 had pipes to compare; the middle model's median difference in conduit peak flow is 8.3%; 114 agree within 10% and 53 differ by more than half.
- The converter keeps hydrology and hydraulics only: quality, LID, RDII, groundwater, snow, control rules and outlets are dropped and listed.

**What it does not show.** Which engine is right is not shown (no measurements); differences mix the engines with the translation; Extran is explicit with a fixed step; four register items remain open; Chromium only; the 121 changes and the translator are checked by machine, not read by a person. [S271](../sources/S271-swmm44h-workbench-summary.md)

**Noted at ingest.** 114 + 24 + 20 + 53 = 211 and 218 + 68 + 5 + 9 = 300, as the census bars and the two-engine table give them (our arithmetic).

**Its address.** The SWMM 1 Engine lists it among its related apps as "SWMM 4.4H Engine" at https://swmm44h-engine-swmm5-import.netlify.app/, the name its own summary file carries [S391](../sources/S391-swmm1-engine-app-md-v3-15.md).

See [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [SWMM 4 against SWMM 5: the 2006 quality assurance tests](../concepts/swmm4-versus-swmm5-qa-2006.md), [SWMM 4 Twin Engines (app)](swmm4-twin-engines.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [EXTRAN](extran.md).

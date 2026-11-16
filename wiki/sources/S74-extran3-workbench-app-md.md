---
title: "S74: EXTRAN III Workbench, technical summary (app .md, v1.6.0)"
type: source
raw: raw/apps/extran3-workbench.md
kind: app-md
author: Robert Dickinson
published: 2026-11-11
ingested: 2026-11-15
tags: [swmm-history, extran, verification, apps, wasm, hydraulics]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary that ships with the EXTRAN III Workbench, version 1.6.0: the 1981 EXTRAN run from its printed listing, beside EPA SWMM 5.2.4. Raw file: [raw/apps/extran3-workbench.md](../../raw/apps/extran3-workbench.md). Bob uploaded it on 14 November 2026.

**How it was written.** By Claude (Anthropic) in Claude Code sessions in October and November 2026, under Bob's direction. Its human-review line reads "Robert Dickinson reviewed results and directed the tests".

**Claims worth keeping**
- Source: the CDM listing dated 20-MAY-81, manual pages 167 to 228, surviving only as OCR text, cut into 15 program units.
- Four EXTRAN III engines: as printed and with ten 1981 bugs fixed, each at the 1981 array sizes and with enlarged arrays. Built by f2c (libf2c 20140711), then clang to wasm32-wasi at -O2. Also EPA SWMM 5.2.4 (529,581 bytes).
- The page holds the seven manual example decks with their printed 1981 results, 164 SWMM 4 EXTRAN decks from January 2003, and ten SWMM 5 sample models.
- Against CDM's printed 1981 output: 2,424 values in seven examples; 2,253 exact with the browser engine (92.9 %); 98.4 % counting last-digit and OCR-confusion differences. A native gfortran build gets 2,260 exact.
- The method (TRANSX): explicit link-node solution, modified Euler, a half step then a full step. A junction above 0.96 of the depth to its highest crown is treated as surcharged.
- Run length: TRANSX runs whole passes of MP = (NTCYC+99)/100 steps, so 1,080 steps on the card runs 1,089 and 2,880 runs 2,900.
- The ten fixes, by card: DEPTHX 95, DEPTHX 96-97, DEPTHX 56, HEAD 86, HYDRAD 45 (a closed rectangle never ran full), TRANSX 340, TRANSX 459, BOUND 229, BOUND 234, OUTPUT 62.
- 1981 array sizes: 187 junctions, 187 links, 20 storage junctions, 60 orifices, 60 weirs, 20 pumps, 25 free and 25 gated outfalls, 65 inflow hydrographs. Enlarged: 5,000 junctions and links. Only sizes change, on 92 of 2,998 lines.
- Enlarged against 1981-size engines on 171 decks: reports byte-identical.
- SWMM 5 corpus (SWMMEnablement/1729-SWMM5-Models), 257 models at 1981 sizes: 207 through both engines, 34 too big, 10 SWMM 5.2.4 cannot run, 6 cannot be converted. Of the 34, the enlarged builds run 16.
- Of those 16, EXTRAN III continuity is within 5 % in 2 and prints asterisks in 5.
- Decks written as SWMM 5 models: 171 written and run; median peak-depth difference 0.16 ft as printed, 0.12 ft bugs fixed.

**Limits it states.** A SWMM comparison tests routing, not hydrology. "SWMM 5 is a different program, not the truth." Agreement with 1981 covers only the code paths of the seven examples. Larger arrays do not make the explicit method stable on large models. Storage-junction drift in SWMM 4 decks EXAM57 and EXAM59 is not explained. Not checked by any person: 139 doubtful listing lines (136 repairs marked likely or guess, 3 kept as read) against page images. The 257-model statistics were not rerun after the run-length finding.

**Checked at ingest.** 207 + 34 + 10 + 6 = 257. 2,253 / 2,424 = 92.9 %. 16 + 9 + 5 + 4 = 34. [S05](S05-swmm5org-article-facts.md) says the converter ran on 259 models (Q51).

**Feeds:** [EXTRAN III Workbench (app)](../entities/extran-iii-workbench.md), [EXTRAN](../entities/extran.md), [Verification against printed runs](../concepts/verification-against-printed-runs.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).

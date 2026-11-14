---
title: Verification against printed runs
type: concept
updated: 2026-11-14
sources: [S01, S05, S07]
tags: [verification, method, swmm-history]
reviewed: no
---
How Bob's rebuilt historical engines are checked: type the printed program listing back in, compile it, feed it the decks printed in the old manuals, and score the output number by number against the old printouts [S01](../sources/S01-swmm1-engine-app-md.md). SWMM 1 and EXTRAN III were rebuilt this way from printed listings; SWMM 4.4H came from its Fortran source [S07](../sources/S07-swmm5org-topic-swmm-history.md).

**The steps, as done for SWMM 1** [S01](../sources/S01-swmm1-engine-app-md.md)
1. Transcribe every card, with the identification field in columns 73 to 80.
2. Compare each typed card with its page image (done by the AI, not by a person), and run an ink-per-column check of the typed text against the scan.
3. Compile with two unrelated compilers (GNU Fortran, and f2c then C).
4. Build three ways (WebAssembly, native f2c, GNU Fortran) and compare the printouts.
5. Punch the decks from the manual's tables and score against the printed output.
6. Keep the listing as printed. Repairs go in a separate, optional engine.

**What agreement looked like** [S01](../sources/S01-swmm1-engine-app-md.md)

| 1971 run | Agreement |
|---|---|
| Estuary example | 52 stage values, largest difference 0.0041 ft |
| Sewer example | Capacity table to the last digit; 6 of 10 hydrographs to 0.001 cfs |
| Baker Street, San Francisco | 88 of 95 flow and cost numbers to the digit |
| Wingohocking, Philadelphia | 51 of 51 subarea dry-weather flows |
| Bloody Run, Cincinnati | Outfall dry-weather flow 13.940 against 13.94 cfs |
| Kingman Lake, Washington, D.C. | 53 of 55 storage design numbers |

**What disagreement taught.** Each mismatch was traced to a card: `INIT 55` for the sewer example, `TRAN346` for the Baker Street loads, `HYDR137` for Cincinnati's continuity error [S01](../sources/S01-swmm1-engine-app-md.md).

**Limits that always apply** [S01](../sources/S01-swmm1-engine-app-md.md)
- Modern arithmetic is IEEE single precision; the IBM System/360 was base 16 and truncated. Expect three to four digits of agreement.
- Decks written in 2026 have no 1971 printout. Their numbers are checked against a second compiler and nothing else.
- For SWMM 1, no person has compared 10,889 of the cards with the page images.

**EXTRAN III.** Bob's notes say each run of the workbench is scored value by value against the printed 1981 output, the SWMM5-to-EXTRAN converter was run against SWMM 5.2.4 on 259 models, and 139 doubtful listing lines are not yet confirmed against page images [S05](../sources/S05-swmm5org-article-facts.md). These figures were copied from his notes and not re-verified.

See [SWMM 1 (1971)](../entities/swmm-1.md), [SWMM 1 Engine (app)](../entities/swmm-1-engine-app.md), [EXTRAN](../entities/extran.md), [Continuity is not validation](continuity-is-not-validation.md).

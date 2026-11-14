---
title: OpenSWMM 6 and HydroCouple
type: entity
updated: 2026-11-14
sources: [S02, S03, S04, S05, S21, S22]
tags: [swmm6, engine, hydrocouple]
reviewed: no
---
OpenSWMM 6 is the SWMM line developed at HydroCouple [S22](../sources/S22-li-ten-problems.md). Caleb Buahin is the lead developer of the HydroCouple platform [S21](../sources/S21-li-edition-56-swmm-history.md).

**What the ingested sources say, which is not much yet**
- It is one of four lines moving forward from SWMM 5, with SWMM5+ at CIMM, EPA's 5.2 line and the vendor engines; the four share no common test models [S22](../sources/S22-li-ten-problems.md).
- Bob: "SWMM6 has really good testing procedures - aided by AI tools", and SWMM6 on the HydroCouple GitHub has at least 2,000 models [S22](../sources/S22-li-ten-problems.md).
- The HydroCouple GitHub organization is the fixed 100 of the [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md): 6,607,205 code tokens across 43 repositories at baseline HC-2026-11-10-h. Its default branches had 1,019 commits by 13 people in the 12 months to 1 November 2026 [S02](../sources/S02-complexity-meter-app-md.md).
- openswmm.engine scores 90.1 and openswmm.gui 89.1 on the same scale [S02](../sources/S02-complexity-meter-app-md.md).

**Findings on record**
- SWMM6 `[OPTIONS]` keywords are fatal (ERROR 205) in EPA 5.2.4 and silently ignored by legacy 5.3 (F-0005) [S04](../sources/S04-findings-register-seed.md).
- A metric-units fault in the 6.0.0-alpha.2 timeseries inflow path, found with the Self-Play Lab [S05](../sources/S05-swmm5org-article-facts.md); listed as a register candidate, status confirmed [S03](../sources/S03-findings-register-format.md).
- A virtual-junction crash in alpha.2, and a CHANGELOG that lists 17 `FV_` keys where `OptionsHandler.cpp` parses 21: register candidates [S03](../sources/S03-findings-register-format.md).
- Anderson acceleration gave no speedup on one test case (F-0013) [S04](../sources/S04-findings-register-seed.md).

**Not in the sources yet.** Almost everything: the solvers, 2D, the GUI, the input format, the license. Queued: "SWMM6 Code House" (2026-11-04, 4,427 words), "Forking without Drowning on GitHub for #SWMM6" (2026-08-14), the swmm5.org topic pages "Inside SWMM6" and "ICM InfoWorks and SWMM6".

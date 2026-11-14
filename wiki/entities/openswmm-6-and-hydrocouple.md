---
title: OpenSWMM 6 and HydroCouple
type: entity
updated: 2026-11-14
sources: [S02, S03, S04, S05, S21, S22, S23, S29, S59, S69, S72]
tags: [swmm6, engine, hydrocouple]
reviewed: no
---
OpenSWMM 6 is the SWMM line developed at HydroCouple [S22](../sources/S22-li-ten-problems.md). Caleb Buahin is the lead developer of the HydroCouple platform [S21](../sources/S21-li-edition-56-swmm-history.md).

**What the ingested sources say, which is not much yet**
- It is one of four lines moving forward from SWMM 5, with SWMM5+ at CIMM, EPA's 5.2 line and the vendor engines; the four share no common test models [S22](../sources/S22-li-ten-problems.md).
- Bob: "SWMM6 has really good testing procedures - aided by AI tools", and SWMM6 on the HydroCouple GitHub has at least 2,000 models [S22](../sources/S22-li-ten-problems.md).
- The HydroCouple GitHub organization is the fixed 100 of the [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md): 6,607,205 code tokens across 43 repositories at baseline HC-2026-11-10-h. Its default branches had 1,019 commits by 13 people in the 12 months to 1 November 2026 [S02](../sources/S02-complexity-meter-app-md.md).
- openswmm.engine scores 90.1 and openswmm.gui 89.1 on the same scale [S02](../sources/S02-complexity-meter-app-md.md).

**The code the translations start from**
- Repository HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, which [swmm6-rust](swmm6-rust.md)'s README calls 6.0.0-alpha.4. Licensed Apache 2.0, Copyright 2026 HydroCouple Developers. Lead developer Caleb Buahin; developer and documentation Corinne Wiesner-Friedman [S29](../sources/S29-swmm6-rust-readme.md) [S23](../sources/S23-swmm6-csharp-readme.md).
- Portions derive from public-domain EPA SWMM; the USEPA does not endorse the translations, and neither does HydroCouple [S23](../sources/S23-swmm6-csharp-readme.md).
- What the engine holds, as listed by the Rust translation: the 1D engine with legacy dynamic wave (EXTRAN and SLOT surcharge, virtual junctions), a finite-volume router (HLL/HLLC with MUSCL-Hancock reconstruction), new quality engines (EULERIAN_ARD, LAGRANGIAN), heat, water-age and reaction-species modules, UEB snow, Richards-equation LID columns, and a 2D surface module with 1D-2D coupling [S29](../sources/S29-swmm6-rust-readme.md).
- Thirteen translations of the 1D engine are on record, all byte-identical to it on the decks they finished: see [SWMM6 language translations](swmm6-language-ports.md).

**Findings on record**
- SWMM6 `[OPTIONS]` keywords are fatal (ERROR 205) in EPA 5.2.4 and silently ignored by legacy 5.3 (F-0005) [S04](../sources/S04-findings-register-seed.md).
- A metric-units fault in the 6.0.0-alpha.2 timeseries inflow path, found with the Self-Play Lab [S05](../sources/S05-swmm5org-article-facts.md); listed as a register candidate, status confirmed [S03](../sources/S03-findings-register-format.md).
- A virtual-junction crash in alpha.2, and a CHANGELOG that lists 17 `FV_` keys where `OptionsHandler.cpp` parses 21: register candidates [S03](../sources/S03-findings-register-format.md).
- Anderson acceleration gave no speedup on one test case (F-0013) [S04](../sources/S04-findings-register-seed.md).
- 6.0.0-alpha.4 ignores an unknown LID layer keyword (SOIL2) instead of reporting it; an issue was drafted with a tested patch [S59](../sources/S59-topsoil-recovery-check-app-md.md).
- Defect D2, a drain on a bio-retention cell with no storage layer, gives the same -1,100.9 % continuity error in OpenSWMM 5.3.0-beta.3 and 6.0.0-alpha.4 as in EPA 5.2.4; and OpenSWMM 6 keeps 5.2.4's rule that LID soil evaporation stops while water infiltrates (`LID.cpp` line 907). See [LID bio-retention layers](../concepts/lid-bioretention-layers.md) [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**Size and shape, from reading it.** 351,187 lines in 675 files at 6.0.0-alpha.4, commit 9648837 [S69](../sources/S69-swmm6-code-house-app-md.md). A run's state lives in one `SimulationContext`, one per concurrent simulation, and a node is an index into arrays; output is written by a separate IO thread; a fourth routing model, FV, is an explicit finite volume method [S72](../sources/S72-li-swmm6-code-house-article.md). The [SWMM6 Code House (app)](swmm6-code-house.md) holds 20 reading notes on this code, all hypotheses.

**Builds on record.** Branch swmm6_rel, commit 13746831, licensed Apache-2.0: OpenSWMM 6.0.0-alpha.4 and the legacy engine 5.3.0-beta.3, both built to WebAssembly for the [Topsoil Recovery Check (app)](topsoil-recovery-check.md) and rebuilt byte-identical from the pinned sources with Zig 0.17.0 [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**Not in the sources yet.** How the solvers work (the sources name them but do not explain them), 2D beyond what the Rust translation covers, the GUI, the input format. Queued: "SWMM6 Code House" (2026-11-04, 4,427 words), "Forking without Drowning on GitHub for #SWMM6" (2026-08-14), the swmm5.org topic pages "Inside SWMM6" and "ICM InfoWorks and SWMM6".

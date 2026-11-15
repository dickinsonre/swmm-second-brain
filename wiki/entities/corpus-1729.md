---
title: 1729-SWMM5-Models-2030 (the corpus)
type: entity
updated: 2026-11-14
sources: [S23, S29, S30, S35, S41, S42, S43, S45, S52, S54]
tags: [corpus, verification, swmm5, swmm6]
reviewed: 2026-11-15
---
Bob's public repository of SWMM5 models, https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030 [S23](../sources/S23-swmm6-csharp-readme.md).

**Size and the gate set.** The corpus holds 4,540 .inp files. The SWMM5 gate set is 480 of the 518 distinct models (distinct by content) in six folders: EPA, Hydraulics, Hydrology, LID, OWA_EXTRAN and OWA_ROUTING. The other 38 were left out by an early timing survey with a 12-second limit, "whose records were not kept. The cut is rough" [S41](../sources/S41-swmm5-go-readme.md). 49 of the 480 stop on an input error [S41](../sources/S41-swmm5-go-readme.md). EPA 5.2.4 runs all 480 in 256 s [S43](../sources/S43-swmm5-pascal-readme.md).

**As a gate set.** 480 of its models are the gate set every SWMM6 translation is checked on, the same set "the SWMM5 ports were checked on" [S23](../sources/S23-swmm6-csharp-readme.md). The READMEs list what the 480 and the 452 extra decks span between them: EPA's examples, the OWA EXTRAN set, hydrology, hydraulics, water quality, LID, RDII, controls, hot start, input errors, the FV solver and SWMM6's own tests [S23](../sources/S23-swmm6-csharp-readme.md).

**Decks that depend on each other.** Three decks SAVE and USE one shared file, `cho.txt`. The later checks always include all three [S30](../sources/S30-swmm6-kotlin-readme.md).

**The slow ones.** `Hydrology/SCANLON.inp` and `EPA/72_H&H_Elements(2).inp` did not finish within 1,800 s in the Hy and Ruby ports [S35](../sources/S35-swmm6-ruby-readme.md). When Ruby's run of SCANLON was stopped it had written 42,334,342 of its 78,975,850 `.out` bytes (53.6 %) [S35](../sources/S35-swmm6-ruby-readme.md).

**Other uses.** swmm6-rust's `census/` compares OpenSWMM 6 with EPA SWMM 5.2.4 on a corpus of SWMM5 models [S29](../sources/S29-swmm6-rust-readme.md). Whether that corpus is this one, the source does not say.

**Heavy decks.** `Hydrology/sewer_rdii_problem.inp` allocates 3.38 GB of RDII rainfall history in EPA [S42](../sources/S42-swmm5-kotlin-readme.md): 613 unit hydrographs, a 9,900-hour base, a 60-second rain interval, 375 million values EPA almost never touches [S54](../sources/S54-swmm5-r-readme.md). EPA takes 34.8 s on `SCANLON.inp` and 38.6 s on `72_H&H_Elements(2).inp`, its two longest [S45](../sources/S45-swmm5-ruby-readme.md); the second routes a dry year at a 10 s step before its 36-hour storm [S52](../sources/S52-swmm5-hy-readme.md).

**Not in the sources.** What "1729" and "2030" stand for.

See [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM6 language translations](swmm6-language-ports.md).

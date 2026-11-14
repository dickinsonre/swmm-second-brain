---
title: 1729-SWMM5-Models-2030 (the corpus)
type: entity
updated: 2026-11-14
sources: [S23, S29, S30, S35]
tags: [corpus, verification, swmm5, swmm6]
reviewed: no
---
Bob's public repository of SWMM5 models, https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030 [S23](../sources/S23-swmm6-csharp-readme.md).

**As a gate set.** 480 of its models are the gate set every SWMM6 translation is checked on, the same set "the SWMM5 ports were checked on" [S23](../sources/S23-swmm6-csharp-readme.md). The READMEs list what the 480 and the 452 extra decks span between them: EPA's examples, the OWA EXTRAN set, hydrology, hydraulics, water quality, LID, RDII, controls, hot start, input errors, the FV solver and SWMM6's own tests [S23](../sources/S23-swmm6-csharp-readme.md).

**Decks that depend on each other.** Three decks SAVE and USE one shared file, `cho.txt`. The later checks always include all three [S30](../sources/S30-swmm6-kotlin-readme.md).

**The slow ones.** `Hydrology/SCANLON.inp` and `EPA/72_H&H_Elements(2).inp` did not finish within 1,800 s in the Hy and Ruby ports [S35](../sources/S35-swmm6-ruby-readme.md). When Ruby's run of SCANLON was stopped it had written 42,334,342 of its 78,975,850 `.out` bytes (53.6 %) [S35](../sources/S35-swmm6-ruby-readme.md).

**Other uses.** swmm6-rust's `census/` compares OpenSWMM 6 with EPA SWMM 5.2.4 on a corpus of SWMM5 models [S29](../sources/S29-swmm6-rust-readme.md). Whether that corpus is this one, the source does not say.

**Not in the sources.** How many models the repository holds in all, what "1729" and "2030" stand for, and how the 480 were chosen.

See [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM6 language translations](swmm6-language-ports.md).

---
title: 1729-SWMM5-Models-2030 (the corpus)
type: entity
updated: 2026-11-17
sources: [S23, S29, S30, S35, S41, S42, S43, S45, S52, S54, S74, S87, S89, S75, S79, S193, S195, S196, S197, S208, S211, S212, S215, S216]
tags: [corpus, verification, swmm5, swmm6]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S192 to S202 ingest): one paragraph added at the end on four more uses (S193, S195 to S197); 2026-11-17 (S205 to S223 ingest): a paragraph added near the end, headed Added 17 November 2026 (S208, S211, S212, S215, S216)"
---
Bob's public repository of SWMM5 models, https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030 [S23](../sources/S23-swmm6-csharp-readme.md).

**Size and the gate set.** The corpus holds 4,540 .inp files. The SWMM5 gate set is 480 of the 518 distinct models (distinct by content) in six folders: EPA, Hydraulics, Hydrology, LID, OWA_EXTRAN and OWA_ROUTING. The other 38 were left out by an early timing survey with a 12-second limit, "whose records were not kept. The cut is rough" [S41](../sources/S41-swmm5-go-readme.md). 49 of the 480 stop on an input error [S41](../sources/S41-swmm5-go-readme.md). EPA 5.2.4 runs all 480 in 256 s [S43](../sources/S43-swmm5-pascal-readme.md).

**As a gate set.** 480 of its models are the gate set every SWMM6 translation is checked on, the same set "the SWMM5 ports were checked on" [S23](../sources/S23-swmm6-csharp-readme.md). The READMEs list what the 480 and the 452 extra decks span between them: EPA's examples, the OWA EXTRAN set, hydrology, hydraulics, water quality, LID, RDII, controls, hot start, input errors, the FV solver and SWMM6's own tests [S23](../sources/S23-swmm6-csharp-readme.md).

**Decks that depend on each other.** Three decks SAVE and USE one shared file, `cho.txt`. The later checks always include all three [S30](../sources/S30-swmm6-kotlin-readme.md).

**The slow ones.** `Hydrology/SCANLON.inp` and `EPA/72_H&H_Elements(2).inp` did not finish within 1,800 s in the Hy and Ruby ports [S35](../sources/S35-swmm6-ruby-readme.md). When Ruby's run of SCANLON was stopped it had written 42,334,342 of its 78,975,850 `.out` bytes (53.6 %) [S35](../sources/S35-swmm6-ruby-readme.md).

**Other uses.** swmm6-rust's `census/` compares OpenSWMM 6 with EPA SWMM 5.2.4 on a corpus of SWMM5 models [S29](../sources/S29-swmm6-rust-readme.md). Whether that corpus is this one, the source does not say.

**Heavy decks.** `Hydrology/sewer_rdii_problem.inp` allocates 3.38 GB of RDII rainfall history in EPA [S42](../sources/S42-swmm5-kotlin-readme.md): 613 unit hydrographs, a 9,900-hour base, a 60-second rain interval, 375 million values EPA almost never touches [S54](../sources/S54-swmm5-r-readme.md). EPA takes 34.8 s on `SCANLON.inp` and 38.6 s on `72_H&H_Elements(2).inp`, its two longest [S45](../sources/S45-swmm5-ruby-readme.md); the second routes a dry year at a 10 s step before its 36-hour storm [S52](../sources/S52-swmm5-hy-readme.md).

**The name.** The 2030 is for Bob's plans for SWMM in the year 2030, when he will be 75. The 1729 is for Ramanujan the mathematician [S89](../sources/S89-note-corpus-name.md). Bob gave this on 15 November 2026 in answer to this page, which had listed it as not in the sources.

**Inventory, from its README** [S87](../sources/S87-corpus-1729-readme.md). A local inventory of 23 October 2026 counts 22,208 files and 15,977 MB in 44 top-level folders: 4,540 `.inp`, 4,099 `.rpt`, 3,461 `.out` and 4,029 `.md` files. The largest folder by count is XPSWMM, 1,859 models converted from XPSWMM with the XPSWMM Card Reader. The README warns that `.inp` totals "are file counts, not counts of distinct networks or passing tests".

**Added 23 October 2026** [S87](../sources/S87-corpus-1729-readme.md). Three folders: 40 EPA, PySWMM and swmm-python test models found missing by comparing file content; the 351 reproducer decks of the HydroCouple swmm-code-review, of which 11 crash or hang EPA SWMM 5.2.4; and 335 input files from the OpenSWMM engine repository, of which 250 need OpenSWMM 6. Before them, 53 of the review's input-reachable findings had no model in the corpus. See [What the gate cannot see](../concepts/gate-blind-spots.md).

**License.** The repository-level dedication is The Unlicense, but the README says named or contributed folders "require provenance checks before redistribution" and that the two OpenSWMM folders are Apache-2.0 material [S87](../sources/S87-corpus-1729-readme.md).

**Other users of it.** The [EXTRAN III Workbench (app)](extran-iii-workbench.md) ran 257 models of a corpus it names SWMMEnablement/1729-SWMM5-Models [S74](../sources/S74-extran3-workbench-app-md.md); whether that repository and this one hold the same files is Q51. The Workbench's 164 SWMM 4 decks and the [St. Venant Solver Rosetta Stone (app)](st-venant-solver-rosetta-stone.md)'s Example 1 deck come from this repository's `january5_2003_examples` folder [S74](../sources/S74-extran3-workbench-app-md.md), [S75](../sources/S75-st-venant-rosetta-stone-app-md.md); [Teacher-Forced SWMM (app)](teacher-forced-swmm.md) takes its sample models from it [S79](../sources/S79-teacher-forced-swmm-summary.md).

See [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM6 language translations](swmm6-language-ports.md).

**Added 17 November 2026: four more uses.**
- [swmm5-kw](swmm5-kw.md)'s gate ran 3,759 models at commit 9ee63bd [S195](../sources/S195-swmm5-kw-summary.md).
- [SWMM5 Engine Race](swmm5-engine-race.md) swept 1,156 distinct .inp files from 23 folders [S197](../sources/S197-swmm5-engine-race-app-md.md).
- [SWMM5 RASPIPE](swmm5-raspipe.md) drew 1,600 models at random, stratified by file size [S196](../sources/S196-swmm5-raspipe-summary.md).
- [SWMM 3 Runoff & Transport](swmm3-runoff-transport-app.md) runs the January 5, 2003 set of SWMM 4 example decks kept in the corpus [S193](../sources/S193-swmm3-runoff-transport-summary.md).

**Added 17 November 2026.** Five more apps were tested on the corpus: canonical export of 160 short models [S208](../sources/S208-swmm-canon-summary.md), a 277-model regeneration sweep [S211](../sources/S211-swmm5-self-regeneration-summary.md), a census of 307 files for short links [S212](../sources/S212-swmm5-residual-walk-summary.md), 3,558 .inp and .rpt pairs read [S215](../sources/S215-swmm-trouble-graph-summary.md) and 138 runs searched for rhythms [S216](../sources/S216-swmm-rhythm-detector-summary.md). All are summaries Claude wrote from the pages (Q108).

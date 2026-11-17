---
title: Topsoil Recovery Check (app)
type: entity
updated: 2026-11-17
sources: [S08, S59, S203]
tags: [apps, lid, infiltration, swmm5, swmm6, verification]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S203 ingest): one paragraph added at the end on version 2026-11-17"
---
Bob's page on how SWMM credits decompacted topsoil over compacted clay, deployed as `index.html` in a Netlify folder `topsoil-recovery-site/`. Version 2026-11-12 [S59](../sources/S59-topsoil-recovery-check-app-md.md). swmm5.org lists it as comparing Horton with the LID two-layer soil in EPA SWMM 5.2.4 [S08](../sources/S08-swmm5org-topic-inside-swmm5.md). The subject is on [Topsoil over compacted clay](../concepts/topsoil-over-compacted-clay.md).

**Five engines run in the page as WebAssembly** [S59](../sources/S59-topsoil-recovery-check-app-md.md)

| Engine | Source | License |
|---|---|---|
| EPA SWMM 5.2.4 | tag v5.2.4, commit 7952ca83 | public domain |
| EPA SWMM 5.2.4 + MaxInfil fix | same + `modhorton-maxinfil-fix.patch` (OpenSWMM 5.3.0's fix) | public domain |
| [swmm524-perched](swmm524-perched.md) | branch van-genuchten, commit 548e5fbf | none stated in the repo |
| OpenSWMM legacy 5.3.0-beta.3 | swmm6_rel, commit 13746831 | Apache-2.0 |
| OpenSWMM 6.0.0-alpha.4 | swmm6_rel, commit 13746831 | Apache-2.0 |

**Checks** [S59](../sources/S59-topsoil-recovery-check-app-md.md)
- verify.py, 12 Nov 2026: 1,181 of 1,181 cases in 94 s on two cores, in seven groups with expected counts: season 46, ablation 18, VG column checks 4, 8 in storm 7, Experiment H 54, parity 930, OpenSWMM 122. It exits 1 on a missing engine, failed run, missing file, count mismatch or moved number.
- Parity: the perched engine against EPA 5.2.4 with no SOIL2, VG or STRUCT line, 930 of 930 `.out` and LID reports byte-identical.
- All five `.wasm` files rebuilt from the pinned sources with Zig 0.17.0, byte-identical.
- Worst runoff continuity in the study runs 0.017 %; `.out` runoff matches `.rpt` totals within 0.033 in.
- An outside AI-assisted review (3 Nov 2026) graded the 30 Oct release 82/100; its findings are answered on the page's Limits tab.

**Defects it records.** D1, Modified Horton with MaxInfil in EPA 5.2.4 (see [Infiltration methods](../concepts/infiltration-methods.md)), and D2, a drain on a bio-retention cell with no storage layer (see [LID bio-retention layers](../concepts/lid-bioretention-layers.md)) [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**Dated changes** [S59](../sources/S59-topsoil-recovery-check-app-md.md)

| Date | Change |
|---|---|
| 2026-10-29 | First release: recovery test, seasons, soil structure tab, perched engine, Run it yourself |
| 2026-10-30 | 8 in storm test, MaxInfil fix engine, OpenSWMM legacy 5.3.0 and 6.0.0-alpha.3, Engines tab |
| 2026-10-31 | Both OpenSWMM engines moved to the swmm6_rel branch (6.0.0-alpha.4) |
| 2026-11-02 | van Genuchten option in swmm524-perched; binned Rv with stand-in inputs |
| 2026-11-03 | Outside-review fixes, verify.py, BUILD.md, VG OPTION lines and ablation |
| 2026-11-12 | Experiment H (ideas from the SWMM-USERS list), defect D2, Doc tab summaries and questions, the .md |

**Who did what.** Claude (Anthropic) did most of the work at Bob's request; Bob set the question and reviews the conclusions. The people who raised the question are not named in the source [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**Added 2026-11-17.** Version 2026-11-17 of the summary is [S203](../sources/S203-topsoil-recovery-check-v2026-11-17.md); S59 above is the 2026-11-12 version. It adds Windows x64 builds of EPA 5.2.4 and swmm524-perched with a compare script, links to the engine repository and to Bob's GitHub accounts (https://github.com/dickinsonre, https://github.com/SWMMBobSWMM6), and two corrections: EPA 5.2.4 reads a SOIL2 line as a second SOIL line, and the perched engine ignores DRAIN lines only when the model has a SOIL2 line [S203](../sources/S203-topsoil-recovery-check-v2026-11-17.md).

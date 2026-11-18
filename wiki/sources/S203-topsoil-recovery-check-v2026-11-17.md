---
title: "S203: Topsoil Recovery Check, technical summary (app .md, 2026-11-17)"
type: source
raw: raw/apps/topsoil-recovery-check-v2026-11-17.md
kind: app-md
author: Robert Dickinson
published: 2026-11-17
ingested: 2026-11-17
tags: [swmm5, lid, infiltration, swmm6, verification, apps]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: no
---
**What it is.** Version 2026-11-17 of the technical summary that ships with the Topsoil Recovery Check page. It follows version 2026-11-12, [S59](S59-topsoil-recovery-check-app-md.md), and differs from it in six lines. Raw file: [raw/apps/topsoil-recovery-check-v2026-11-17.md](../../raw/apps/topsoil-recovery-check-v2026-11-17.md).

**How it was written.** By Claude (Anthropic) at Bob's request, like S59. The new lines come from building the two engines for Windows and running them on four example models on 17 November 2026.

**Claims worth keeping (new in this version)**
- Correction to S59. With a SOIL2 line the perched engine ignores DRAIN lines (`StorageDrain = 0.0` in its perched flux routine). Without one it runs 5.2.4's bio-retention routine and shares defect D2: 232.848 in of drain flow from 20.550 in of rain, the same as 5.2.4, checked 17 Nov 2026. S59 said only that the perched engine ignores DRAIN lines.
- A new defect entry. EPA 5.2.4 reads a SOIL2 line as a second SOIL line, with no error or warning: `findmatch(toks[1], LidLayerWords)` (`lid.c` line 397) uses `match()` (`input.c`), which accepts any word that starts with a keyword. The clay replaces the topsoil: winter season surface runoff 13.521 in, against 3.400 in with the SOIL2 line removed. A VG line is ERROR 205.
- Windows x64 command-line builds of EPA 5.2.4 and swmm524-perched (Zig 0.17.0, x86_64-windows-gnu, repo folder `windows/`): under Wine 9.0 their `.out` files are byte-identical to Linux builds made the same way on 8 example runs; those Linux builds pass 1,059 of 1,059 verify.py cases (all groups but OpenSWMM). Not yet run on a Windows machine.
- Links: the `van-genuchten` branch of the engine repository, its Windows folder, and Bob's GitHub accounts https://github.com/dickinsonre and https://github.com/SWMMBobSWMM6.

Everything else, including every number S59 carries, is unchanged.

**Checked 18 November 2026.** The file links the branch, which can move. On 18 November 2026 the head of `van-genuchten` was commit 816f2799058cf6282bb5f7abca82a516e69206cd, committed 17 November 2026 at 15:34 Eastern ("Windows x64 engines and compare.py; SOIL2 and DRAIN corrections in README"), with no later commit; its `windows/` folder holds `runswmm-524.exe`, `runswmm-perched.exe`, `compare.py`, `SHA256SUMS`, `README.md` and `examples`. The wiki links that commit: https://github.com/SWMMBobSWMM6/swmm524-perched/tree/816f2799058cf6282bb5f7abca82a516e69206cd and https://github.com/SWMMBobSWMM6/swmm524-perched/tree/816f2799058cf6282bb5f7abca82a516e69206cd/windows.

**Feeds:** [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md), [swmm524-perched](../entities/swmm524-perched.md), [LID bio-retention layers](../concepts/lid-bioretention-layers.md), [Two-layer soil infiltration (SOIL2)](../concepts/two-layer-infiltration.md), [EPA SWMM 5](../entities/swmm-5.md), [The SWMM findings register](../concepts/findings-register.md).

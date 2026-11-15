---
title: SWMM Engine What If (app)
type: entity
updated: 2026-11-14
sources: [S70]
tags: [apps, swmm5, swmm6, translation, benchmarks, verification]
reviewed: 2026-11-15
---
Bob's decision aid for anyone putting SWMM into another language or changing what it computes: what you gain, what you pay, and what evidence exists. Version 1.4, 12 November 2026 [S70](../sources/S70-swmm-engine-what-if-app-md.md). The argument is on [Wrap, translate or extend](../concepts/wrap-translate-or-extend.md).

**How it works.** The user picks one of 7 goals, one of three roads, and a language (21) or an extended engine (4). The app returns a fit judgment with its reason, the measured cost and gate result copied from that engine's repository, the trap that engine had to beat, and a next step. It runs no SWMM engine [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**What makes version 1.4 a source of its own.** For it, Claude cloned all 20 SWMM 5 translations at their listed commits, rebuilt them on one machine on 12 November 2026, and ran them [S70](../sources/S70-swmm-engine-what-if-app-md.md):
- **Gate.** 14 ports matched EPA on 480 of 480. Six interpreters ran reduced sets and matched on every model they ran.
- **Speed.** One interleaved benchmark for all 20 on the same 12 models. This is the common measurement Q27 asked for, for every port but R. The table is on [SWMM5 translations: the re-run of 12 November 2026](../concepts/swmm5-ports-rerun-2026-11.md).
- **Generic math.** Which ports follow EPA when glibc drops its FMA routines, and which keep the FMA answers. See [Matching glibc math in a translation](../concepts/glibc-math-in-translation.md).
- **Probes.** 24 language traps rerun in a few lines each; 24 reproduced.

**What it reports and did not rerun** [S70](../sources/S70-swmm-engine-what-if-app-md.md)
- The 12 OpenSWMM 6 translations (see [SWMM6 language translations](swmm6-language-ports.md)).
- Four engines that extend EPA's C: swmm5-kw, [swmm524-perched](swmm524-perched.md), swmm5-raspipe and swmm5-infosewer. Their numbers are on the concept page.

**The app's own arithmetic is checked** [S70](../sources/S70-swmm-engine-what-if-app-md.md)
- Exact fused multiply-add against glibc: 200,000 of 200,000 triples.
- The bundled glibc `pow` against the build machine's: 300,000 of 300,000 arguments.
- In node 22, `Math.pow` differs from glibc on 9.52 %, 10.13 % and 9.85 % of 50,000 arguments in three classes and 0.07 % in the fourth, each by one unit in the last place.

**Review.** One outside review of v1.1 gave 82/100, with five findings fixed in v1.2. No person has reviewed v1.3 or v1.4 or repeated the re-run. The 294 + 7 fit judgments are Claude's [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**Versions** [S70](../sources/S70-swmm-engine-what-if-app-md.md)

| Version | Date | What |
|---|---|---|
| 1.0 | 2026-10-30 | First build, 9 engines, two roads |
| 1.1 | 2026-10-30 | Renamed SWMM Engine What If |
| 1.2 | 2026-10-31 | Outside-review fixes |
| 1.3 | 2026-11-11 | 12 newer ports, the SWMM6 family, the third road |
| 1.4 | 2026-11-12 | All 20 ports rebuilt and re-run; one benchmark for all 20 |

**Open.** Its summary says "netlify: none yet", while swmm5-engine-what-if.netlify.app serves v1.1 (Q45). Its list of empty repositories is older than two READMEs already in this wiki (Q48). See [Open questions](../open-questions.md).

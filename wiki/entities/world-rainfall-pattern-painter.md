---
title: World Rainfall Pattern Painter (app)
type: entity
updated: 2026-11-14
sources: [S65, S66]
tags: [apps, rainfall, design-storms, lovable, verification]
reviewed: no
---
Bob's design-storm generator, built with Lovable and served at https://rain-canvas-studio.lovable.app, with a public API [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md). Version 3.2.0 of 2 November 2026; summary rewritten 14 November 2026; MIT license [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md). Its site name and `file:` identifier are `rain-canvas-studio` [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md). The method is on [Design storms and temporal patterns](../concepts/design-storm-patterns.md).

**What it does.** Takes a total depth, a duration, a time step and a temporal pattern, and returns a hyetograph. It exports to CSV, EPA SWMM, [InfoWorks ICM](infoworks-icm.md), XP-SWMM and HEC-HMS formats, reads rainfall files back in, compares patterns and holds engineering calculators [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md).

**Two dated descriptions**

| | February 2026 [S66](../sources/S66-li-design-storm-app-66-patterns.md) | Version 3.2.0, November 2026 [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md) |
|---|---|---|
| Patterns | 66 | 339, and a Custom editor; 234 old IDs kept as aliases |
| Confidence stated | none | 3 High, 57 Medium, 279 Low |
| Public API | not mentioned | yes, same calculator as the app |
| Tests reported | none | 1,502 of 1,502 |

**How it grew** [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md)

| Version | Date | What |
|---|---|---|
| 1.0.0 | 2025-11-09 | First release, as Rainfall Pattern Painter |
| 2.0.0 | 2026-02-24 | Renamed World Rainfall Pattern Painter |
| 2.1.0 | 2026-02-27 | Public API, storm assistant |
| 2.3.0 | 2026-03-27 | About 180 added design storms |
| 2.4.0 | 2026-05-30 | 38 added patterns |
| 3.0.1 | 2026-10-22 | One shared calculator for app and API; duplicates merged; 339 patterns |
| 3.1.0 | 2026-11-01 | Source notes and confidence on every pattern; ICM event CSV |
| 3.2.0 | 2026-11-02 | Shared active storm across tabs; Changes tab |

**Checks** [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md)
- 14 November 2026: 1,496 Vitest tests in 18 files and 6 live API tests in 1 file, all passed.
- Every one of the 339 patterns returns its depth: largest difference 1.776e-15 in in the calculator and 0.0002 in (0.005 %) through the API's 4-decimal rounding.
- Published ordinate comparisons, as the summary lists them: NRCS WinTR-55 whole-hour values for SCS Types IA and II, and DWD KOSTRA examples for the Euler Type II arrangement. The uniform block is checked against its definition.
- A method fidelity review on 2 November 2026 graded it B-; reviewer and tool not recorded (Q38).

**What the summary will not claim** [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md)
- That any person has checked the 339 source notes against the original documents.
- That an exported file imports into EPA SWMM, ICM, XP-SWMM or HEC-HMS: the tests exercise the app's own parsers and the exact ICM text, not those programs.
- That a pattern suits a site or a regulator because its volume closes.
- Any human review. An earlier claim of one was removed because the project holds no record of it.

**Open.** The raw file's name carries another app's version (Q35). The article lists HEC-HMS export as coming three months after the change list says it shipped (Q42). Two entries in the climate table need a look (Q43). See [Open questions](../open-questions.md).

---
title: SWMM Engines, Byte for Byte (app)
type: entity
updated: 2026-11-15
sources: [S41, S70, S71, S82]
tags: [apps, swmm5, swmm6, translation, verification]
reviewed: 2026-11-15
---
Bob's results viewer for the engine translations: every stored verdict of the [Byte-for-byte gate](../concepts/byte-for-byte-gate.md) in one page. It lives in the swmm5-go repository as `app/swmm-engines.html`, with its essay as the Doc tab [S41](../sources/S41-swmm5-go-readme.md). It runs no engine and contains no engine code [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md).

**A caution about its source.** The page ships no technical summary. [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md) was written by Claude on 14 November 2026 from the page's embedded data, with nothing rerun. Treat it as a faithful copy of what the page stores, dated by the page's build stamp, 6 November 2026.

**What the page stores** [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md)

| | |
|---|---|
| Gate models | 480 |
| Engines | EPA 5.2.4 as reference, and C++, Rust, Fortran, C#, Python, TypeScript, Java, Go |
| Identical to EPA on all 480 | C++, Rust, Fortran, C#, TypeScript, Java, Go |
| Python | 465 identical, 15 not run |
| Compared per engine | 152,690 report lines, 1,244,999,775 `.out` bytes |
| SWMM6 tab | six translations; five pass 480 and 452 extra decks, Python 412 of 413 run |

**It covers fewer engines than exist.** The page has 8 SWMM 5 translations and 6 of SWMM6. [SWMM Engine What If (app)](swmm-engine-what-if.md), built six days later, lists 20 and 12 [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**Its benchmark, and the later one.** Median CPU ratio to EPA on 12 models:

| Engine | 29 Oct 2026, 3 reps [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md) | 12 Nov 2026, 5 reps (Python 2) [S70](../sources/S70-swmm-engine-what-if-app-md.md) |
|---|---|---|
| C++ | 0.943 | 0.94 |
| Rust | 1.106 | 1.163 |
| Fortran | 1.260 | 1.281 |
| Go | 1.723 | 1.542 |
| C# | 5.194 | 5.353 |
| Java | 9.175 | 9.847 |
| TypeScript | 19.236 | 19.323 |
| Python | 81.628 | 87.397 |

The later run says the eight reproduced "within 11 percent" [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**Five defects in EPA SWMM 5.2.4, found by translating it** [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md)

| Where | What |
|---|---|
| `inlet.c:146` | A keyword list with no NULL sentinel, so a lookup reads past its end |
| `gage.c:251` | An int overflow when a time series has one point |
| `swmm5.c:1593` | A full path written into a 260-byte buffer |
| `output.c:523` | An 8-byte value written with a 4-byte size |
| `project.c:421` | A memset that counts doubles where bytes are needed |

They have the app's own numbers 1 to 5 and no IDs in [The SWMM findings register](../concepts/findings-register.md) (Q47).

**What it says it does not show.** "Identical to EPA means EPA's answers, right or wrong." One platform. 49 of the 480 models stop on an input error. No gate model that ran exercises streets and inlets, a climate file, or the USE interface files. No person has read the generated code line by line [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md).

**Open.** The public address nine-swmm5-engines-not-c.netlify.app serves an earlier build titled Nine SWMM5 Engines (Q45). See [Open questions](../open-questions.md).

**One of the five, seen twice.** The `swmm5.c:1593` buffer was also found by the [Mirab Test Bench (app)](mirab-test-bench.md), as its finding P-1: `realpath()` writes into a 260-byte buffer [S82](../sources/S82-mirab-test-bench-summary.md).

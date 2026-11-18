---
title: "swmm5-rs Side by Side (app)"
type: entity
updated: 2026-11-17
sources: [S205, S220]
tags: [apps, swmm5, rust, translation, byte-for-byte, findings]
reviewed: no
---
Bob's app swmm5-rs Side by Side: a comparison of EPA SWMM 5.2.4's C with swmm5-rs, the same 54 source files translated statement by statement to Rust by c2rust, model by model and byte by byte on 113 models. Version 1.2, 2026-10-19 [S220](../sources/S220-swmm5-rs-side-by-side-summary.md). Netlify address: https://swmm5-rs-side-by-side.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S220](../sources/S220-swmm5-rs-side-by-side-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S220](../sources/S220-swmm5-rs-side-by-side-summary.md)
- 91 of 91 binary .out files are byte-identical: every model that runs.
- 88 of 113 .rpt reports are identical apart from the wall-clock lines.
- 25 reports differ, each by one extra line, "WARNING 09: time series interval greater than recording interval for Rain Gage ...". In every one a rain gage reads a one-point time series, such as TS1 0 0 in EPA's swc1.inp.
- 22 models both engines refuse, with the same error report (22 of 22).
- Cause: at gage.c:251 EPA converts 8.64 x 10^14 seconds to a C int, a conversion C leaves undefined; gcc on x86-64 gets -2,147,483,648 and skips the warning, while Rust must clamp, gets +2,147,483,647 and writes it. The page treats it as an EPA C quirk on one-point rain series and shows a fix.

**What it does not show.** One CPU family; other CPUs and compilers were not the subject. c2rust output is a mechanical translation, not the later hand-written safe Rust of swmm5-rust. [S220](../sources/S220-swmm5-rs-side-by-side-summary.md)

**Noted at ingest.** 91 + 22 = 113 models, and 88 + 25 = 113 reports. 8.64 x 10^14 s is 10^10 days, beyond the 2,147,483,647 a 32-bit int holds. The case is one more of [Where languages part from C](../concepts/where-languages-part-from-c.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM5 language translations (swmm5-*)](swmm5-language-ports.md), [The SWMM findings register](../concepts/findings-register.md).

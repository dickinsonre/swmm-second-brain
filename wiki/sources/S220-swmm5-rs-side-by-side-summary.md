---
title: "S220: swmm5-rs Side by Side, summary written from the page (v1.2)"
type: source
raw: raw/apps/swmm5-rs-side-by-side-v1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-10-19
ingested: 2026-11-17
tags: [apps, swmm5, rust, translation, byte-for-byte, findings]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app swmm5-rs Side by Side, version 1.2: a comparison of EPA SWMM 5.2.4's C with swmm5-rs, the same 54 source files translated statement by statement to Rust by c2rust, model by model and byte by byte on 113 models. Raw file: [raw/apps/swmm5-rs-side-by-side-v1.2.md](../../raw/apps/swmm5-rs-side-by-side-v1.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792425948-fbdb, reading its Verdict and Essay tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in a session on 17 October 2026 at Bob's request; the translation and the first 113-model run came from an earlier Claude session on 16 to 17 October. Claude rebuilt swmm5-rs with c2rust, built five C engine variants and wrote the page and essay.

**Claims worth keeping** (all copied from the file)
- 91 of 91 binary .out files are byte-identical: every model that runs.
- 88 of 113 .rpt reports are identical apart from the wall-clock lines.
- 25 reports differ, each by one extra line, "WARNING 09: time series interval greater than recording interval for Rain Gage ...". In every one a rain gage reads a one-point time series, such as TS1 0 0 in EPA's swc1.inp.
- 22 models both engines refuse, with the same error report (22 of 22).
- Cause: at gage.c:251 EPA converts 8.64 x 10^14 seconds to a C int, a conversion C leaves undefined; gcc on x86-64 gets -2,147,483,648 and skips the warning, while Rust must clamp, gets +2,147,483,647 and writes it. The page treats it as an EPA C quirk on one-point rain series and shows a fix.

**Limits it states.** One CPU family; other CPUs and compilers were not the subject. c2rust output is a mechanical translation, not the later hand-written safe Rust of swmm5-rust.

**Checked at ingest.** 91 + 22 = 113 models, and 88 + 25 = 113 reports. 8.64 x 10^14 s is 10^10 days, beyond the 2,147,483,647 a 32-bit int holds. The case is one more of [Where languages part from C](../concepts/where-languages-part-from-c.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm5-rs-side-by-side.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [swmm5-rs Side by Side (app)](../entities/swmm5-rs-side-by-side.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Where languages part from C](../concepts/where-languages-part-from-c.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [SWMM5 language translations (swmm5-*)](../entities/swmm5-language-ports.md), [The SWMM findings register](../concepts/findings-register.md).

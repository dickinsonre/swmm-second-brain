---
name: swmm5-rs Side by Side
file: swmm5-rs-side-by-side.html
version: "1.2"
date: 2026-10-19
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/9UkQ3jFbKvDW77nAgcHz7f", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "EPA's C, five build variants", license: public domain}
  - {name: swmm5-rs, source: "all 54 EPA C files translated statement by statement to Rust by c2rust"}
units: as the models carry them
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction, and that the translation came from an earlier Claude session. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/9UkQ3jFbKvDW77nAgcHz7f, version 1792425948-fbdb (index.html, 5,024,027 bytes, SHA-256 ce11e6daf4d3b1d70675a55596ad9615c9d351150d3ef5551d5885f630f108e3), its Verdict and Essay tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# swmm5-rs Side by Side: EPA SWMM 5.2.4 in C and in Rust, on the same 113 models

## In three points
- **What:** Compares EPA SWMM 5.2.4's C with swmm5-rs, the same 54 source files translated statement by statement to Rust by c2rust, model by model and byte by byte on 113 models.
- **So what:** 91 of 91 binary .out files are byte-identical on every model that runs; 25 reports differ by one extra WARNING 09 line, traced to one line of EPA's C (gage.c:251) that converts 8.64 x 10^14 seconds to a C int with undefined result.
- **Now what:** Treat the warning as an EPA C quirk on one-point rain series, not a Rust error; the page shows the fix. The comparison is on one CPU family, and c2rust output is not hand-written safe Rust.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.2 · 19 Oct 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Verdict, Side by side, The one line, CPU not language, The fix, Method, Essay. Each model runs through both engines and the files they write are compared byte for byte.

## Results the page reports

- 91 of 91 binary .out files byte-identical: every model that runs.
- 88 of 113 .rpt reports identical apart from the wall-clock lines.
- 25 reports differ, each by one extra line: "WARNING 09: time series interval greater than recording interval for Rain Gage ...". In every one a rain gage reads a one-point time series (such as TS1 0 0 in EPA's swc1.inp).
- 22 models both engines refuse, with the same error report (22 of 22).
- Cause: at gage.c:251 EPA converts 8.64 x 10^14 seconds to a C int; C leaves the result undefined; gcc on x86-64 gets -2,147,483,648 and skips the warning, while Rust must clamp, gets +2,147,483,647, and writes it.

## Checks (as stated on the page)

- The Method tab gives the builds (swmm5-rs rebuilt with c2rust, five C engine variants) and the comparison procedure.

## What this does not show

- The page's "CPU, not language" tab says the difference comes from the processor's handling of an undefined C conversion; other CPUs and compilers were not the subject.
- c2rust output is a mechanical translation, not the later hand-written safe Rust of swmm5-rust.

## How to reproduce

Open the page; Side by side lists every model with both engines' results.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); c2rust. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude session on 17 October 2026, at the request and under the direction of Robert (Bob) Dickinson, who set the comparison. The translation itself and the first 113-model run came from an earlier Claude session on 16 to 17 October. Claude rebuilt swmm5-rs with c2rust, built the five C engine variants, and wrote the page and the essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.2 (2026-10-19): the version read.

---
title: "Ruby Glory Map (app)"
type: entity
updated: 2026-11-18
sources: [S334]
tags: [apps, icm, ruby, infoswmm, importer]
reviewed: no
---
Bob's app Ruby Glory Map: a map of the InfoSWMM multi-scenario importer for InfoWorks ICM. Version 1.0, 2026-10-25 [S334](../sources/S334-ruby-glory-map-summary.md). Its `links:` line names no live Netlify address [S334](../sources/S334-ruby-glory-map-summary.md).

**A caution about its source.** The page ships no technical summary. [S334](../sources/S334-ruby-glory-map-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S334](../sources/S334-ruby-glory-map-summary.md)
- A map of the two Ruby scripts in SWMMBobSWMM6/Hackathon_KM, the InfoSWMM multi-scenario importer for InfoWorks ICM (an upstream copy is in Innovyze/Open-Source-Support): where every line sits, what the scripts hand each other, which ICM API they lean on, and 21 findings with the code they point at. Bob's Lovable project of this name never built anything, because its fetch of the repository got a 404 every time.
- Every non-blank line of both scripts falls in exactly one of 32 sections (0 unmapped, 0 overlapping), and the 440 lines quoted in the findings are pulled from the cloned files at build time. One finding, the inactive-element scan (RG-07), is timed: Array#include? against Set#include? is 55 times slower at 1,000 elements and 268 times at 5,000. The repository's README names two files (VERSION 3 CHANGELOG.md, OBJECT DEDUPLICATION.md) that it does not hold.
- Checked by machine: section coverage (32 sections, 0 unmapped, 0 overlapping); source quotes pulled from the files at build time; the four UI regexes (UI L446 to 449) run against the strings printed at EX L1229 to 1245, all four matching; the Ruby rules behind RG-02 and RG-04 (an assigned-but-skipped local is nil; "no" == "No" is false) run on Ruby 3.3.6; the RG-07 timing.
- Resting on Claude's reading and on the ICM help: the 21 findings and their fixes.

**How to use it, as the summary puts it.** Use it to read and fix the importer before running it. Neither script was run, in ICM or on the mock; the 21 findings rest on Claude's reading and the ICM help, and no person has checked any against a run in ICM. [S334](../sources/S334-ruby-glory-map-summary.md)

**What it does not show.** As the page lists it: neither script was run, in ICM or on the mock; no real InfoSWMM .mxd or SCENARIO.DBF was available, so the DBF reader was checked by arithmetic, not with a file; timings come from Ruby 3.3.6 in a Linux sandbox, while ICM 2027 embeds Ruby 3.4.6 and earlier versions Ruby 2.4.0; the table and field names used in Phase 2 were not checked against a live model. [S334](../sources/S334-ruby-glory-map-summary.md)

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md).

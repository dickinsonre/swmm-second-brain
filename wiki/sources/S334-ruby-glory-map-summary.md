---
title: "S334: Ruby Glory Map, summary written from the page (v1.0)"
type: source
raw: raw/apps/ruby-glory-map-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, icm, ruby, infoswmm, importer]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Ruby Glory Map, version 1.0: a map of the InfoSWMM multi-scenario importer for InfoWorks ICM. Raw file: [raw/apps/ruby-glory-map-v1.0.md](../../raw/apps/ruby-glory-map-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/SxuRkh6KVc2JJMvZHpDRMH, version 1792938245-cc1d (index.html, 266,665 bytes, SHA-256 bf833fe58accca622a0b8b6bfcd693b3a7a4f76a7e3fc708d85f7464b180845b), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: made with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 at the request of Robert (Bob) Dickinson, who supplied the Lovable project and asked for the app; responsibility for what is published stays with him."

**Claims worth keeping** (all copied from the file)
- A map of the two Ruby scripts in SWMMBobSWMM6/Hackathon_KM, the InfoSWMM multi-scenario importer for InfoWorks ICM (an upstream copy is in Innovyze/Open-Source-Support): where every line sits, what the scripts hand each other, which ICM API they lean on, and 21 findings with the code they point at. Bob's Lovable project of this name never built anything, because its fetch of the repository got a 404 every time.
- Every non-blank line of both scripts falls in exactly one of 32 sections (0 unmapped, 0 overlapping), and the 440 lines quoted in the findings are pulled from the cloned files at build time. One finding, the inactive-element scan (RG-07), is timed: Array#include? against Set#include? is 55 times slower at 1,000 elements and 268 times at 5,000. The repository's README names two files (VERSION 3 CHANGELOG.md, OBJECT DEDUPLICATION.md) that it does not hold.
- Checked by machine: section coverage (32 sections, 0 unmapped, 0 overlapping); source quotes pulled from the files at build time; the four UI regexes (UI L446 to 449) run against the strings printed at EX L1229 to 1245, all four matching; the Ruby rules behind RG-02 and RG-04 (an assigned-but-skipped local is nil; "no" == "No" is false) run on Ruby 3.3.6; the RG-07 timing.
- Resting on Claude's reading and on the ICM help: the 21 findings and their fixes.

**Limits it states.** As the page lists it: neither script was run, in ICM or on the mock; no real InfoSWMM .mxd or SCENARIO.DBF was available, so the DBF reader was checked by arithmetic, not with a file; timings come from Ruby 3.3.6 in a Linux sandbox, while ICM 2027 embeds Ruby 3.4.6 and earlier versions Ruby 2.4.0; the table and field names used in Phase 2 were not checked against a live model.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Ruby Glory Map (app)](../entities/ruby-glory-map.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md).

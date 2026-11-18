---
name: Ruby Glory Map
file: ruby-glory-map.html
version: "1.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/SxuRkh6KVc2JJMvZHpDRMH", original: "Lovable project Ruby Glory Map (first prompt 30 May 2026; it never built anything, because its fetch got a 404 every time)", repo: "https://github.com/SWMMBobSWMM6/Hackathon_KM (commit cc6d63a, 2025-10-22)"}
engines: none (the two Ruby scripts were not run in ICM or on the mock harness)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was made with Claude on 25 October 2026 at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/SxuRkh6KVc2JJMvZHpDRMH, version 1792938245-cc1d (index.html, 266,665 bytes, SHA-256 bf833fe58accca622a0b8b6bfcd693b3a7a4f76a7e3fc708d85f7464b180845b), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Ruby Glory Map: a map of the InfoSWMM multi-scenario importer for InfoWorks ICM

## In three points
- **What:** A map of the two Ruby scripts in SWMMBobSWMM6/Hackathon_KM, the InfoSWMM multi-scenario importer for InfoWorks ICM (an upstream copy is in Innovyze/Open-Source-Support): where every line sits, what the scripts hand each other, which ICM API they lean on, and 21 findings with the code they point at. Bob's Lovable project of this name never built anything, because its fetch of the repository got a 404 every time.
- **So what:** Every non-blank line of both scripts falls in exactly one of 32 sections (0 unmapped, 0 overlapping), and the 440 lines quoted in the findings are pulled from the cloned files at build time. One finding, the inactive-element scan (RG-07), is timed: Array#include? against Set#include? is 55 times slower at 1,000 elements and 268 times at 5,000. The repository's README names two files (VERSION 3 CHANGELOG.md, OBJECT DEDUPLICATION.md) that it does not hold.
- **Now what:** Use it to read and fix the importer before running it. Neither script was run, in ICM or on the mock; the 21 findings rest on Claude's reading and the ICM help, and no person has checked any against a run in ICM.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Version 1.0, built 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Map, Flow, Source, Contract (what the scripts pass each other), API (the ICM calls used), Findings, Verify, About, Doc. The Verify tab carries a mock ICM harness for running both scripts yourself.

## Checks (as stated on the page)

- Checked by machine: section coverage (32 sections, 0 unmapped, 0 overlapping); source quotes pulled from the files at build time; the four UI regexes (UI L446 to 449) run against the strings printed at EX L1229 to 1245, all four matching; the Ruby rules behind RG-02 and RG-04 (an assigned-but-skipped local is nil; "no" == "No" is false) run on Ruby 3.3.6; the RG-07 timing.
- Resting on Claude's reading and on the ICM help: the 21 findings and their fixes.

## What this does not show

As the page lists it: neither script was run, in ICM or on the mock; no real InfoSWMM .mxd or SCENARIO.DBF was available, so the DBF reader was checked by arithmetic, not with a file; timings come from Ruby 3.3.6 in a Linux sandbox, while ICM 2027 embeds Ruby 3.4.6 and earlier versions Ruby 2.4.0; the table and field names used in Phase 2 were not checked against a live model.

## Credits and licenses

SWMMBobSWMM6/Hackathon_KM at cc6d63a; Innovyze/Open-Source-Support, "0000 - InfoSWMM Multi-Scenario Import" at c580601; ICM Ruby help (ruby_icm_help.md) and ICM Ruby Lessons Learned. No license is stated for the page.

## AI use

The page says: made with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 at the request of Robert (Bob) Dickinson, who supplied the Lovable project and asked for the app; responsibility for what is published stays with him. Claude traced the source repository from the Lovable project's chat history, cloned it and the Innovyze library, wrote the extractor that maps the code, read both scripts, wrote every finding, fix and paragraph, ran the Ruby checks and the timing, built the mock ICM harness, and built the page and the Word document. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-25): first version (the version read).

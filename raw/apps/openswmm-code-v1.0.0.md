---
name: OpenSWMM Code
file: openswmm-code.html
version: 1.0.0
date: 2026-11-05
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/3P8yW8u7XjoVqFwQQv8qZJ", repo: none named in the page}
engines: none (a source-code atlas; nothing is compiled or run)
data: {releases: "34 EPA SWMM5 releases, 5.0.003 (2004) to 5.2.4 (2023), plus CHI's OpenSWMM 5.1.912 fork", file_slots: 2519, distinct_texts: 941, sources: "EPA GitHub tags, the Internet Archive, OpenSWMM.org"}
units: none (files, releases, dates)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the atlas was first generated with Perplexity's AI tools and this edition was built with Claude, both at Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/3P8yW8u7XjoVqFwQQv8qZJ, version 1793884249-47ed (index.html, 2,627,552 bytes, SHA-256 091156a928791a501e9268b4ae67058ef8a3f416485670d39bf20efb61545fa3), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# OpenSWMM Code: the SWMM5 engine source of 34 releases, 5.0.003 to 5.2.4, in one page

## In three points
- **What:** A browsable atlas of the complete computational-engine source of 34 EPA SWMM5 releases from 2004 to 2023 plus CHI's OpenSWMM 5.1.912 fork, with Compare, Evolution, Search and Release notes views.
- **So what:** All 1,628 files from the 21 releases on EPA's GitHub match their tagged commits, every one of the 941 stored texts passes a SHA-1 check in the browser, and 11 of EPA's 45 listed builds have no surviving source anywhere public.
- **Now what:** Use Compare to see what actually changed between the build a model was calibrated on and today's. Five release dates differ from EPA's history, and the 13 releases not on GitHub can be checked only for self-consistency.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0.0"); the date is the build session's. The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

A model calibrated in 2009 under SWMM 5.0.016 does not give quite the same outfall peak under 5.2.4; the release notes say what EPA meant to change, and only the code says what did. EPA's GitHub starts at 5.0.022 (a commit dated April 2014); older builds survived as zips in the Internet Archive or on OpenSWMM.org. The page holds 2,519 file slots and stores each of 941 distinct texts once, named by its SHA-1. Tabs: Browse, Compare, Evolution, Search, Release notes, About, Doc.

## Checks (as stated on the page)

- Two descriptions agree: for the 21 releases from EPA's GitHub, all 1,628 files are identical to the tagged commit (line ends aside), and all 21 commit hashes match their tags.
- Round trip: all 941 texts rebuilt from the packed block byte for byte at build time; the same check reruns in the browser from the About tab (941 of 941 by SHA-1, 2,519 of 2,519 file slots point at a stored text).
- Self-consistency: for all 34 releases, the highest build number named in their own files equals the release label.
- Dates: 29 of 34 match EPA's update history.

## Defect register (first entries, as the page lists them)

- D1: five dates differ from EPA's history: 5.1.004 (atlas 2014-04-18, EPA 2014-04-14); 5.1.013 (2018-07-31 against 2018-05-10); 5.1.014 (2020-03-16 against 2020-03-01); 5.1.015 (2020-07-20 against 2020-05-01); 5.2.4 (2023-08-07 against 2023-07-15). The atlas dates follow the OpenSWMM catalogue; kept, with EPA's date shown beside each.
- D2: the original Sources text said each archived zip carries a Readme naming its build; only 5.0.008 and 5.0.009 do. The Sources text was corrected.

## What this does not show

- 11 EPA builds have no surviving engine source: 5.0.001, 5.0.002, 5.0.004, 5.0.005, 5.0.005a, 5.0.005b, 5.0.006, 5.0.006a, 5.0.010, 5.0.019, 5.0.020. Their release notes are in the app; their code is not.
- OpenSWMM fork builds 5.1.907, 5.1.909, 5.1.910 and 5.1.911 can be read on openswmm.org but are not in the app.
- The 13 releases from the Internet Archive and OpenSWMM cannot be compared with a primary source.
- Engine source only; nothing is compiled or run, so the atlas shows what the code says, not what a model does.

## How to reproduce

Open the page; the About tab's "Run the check again" rehashes all 941 texts. Compare any two releases file by file. Export to CSV.

## Credits and licenses

EPA SWMM5 source, US EPA (public domain). CHI's OpenSWMM 5.1.912 fork, from OpenSWMM.org. The page states no license for the fork's code or for the page itself.

## AI use

The page says the atlas Bob supplied was generated with Perplexity's AI tools, which gathered the 34 releases and the fork and wrote the original Browse, Compare, Evolution, Search, Release notes and Sources views. This edition was built with Claude, Anthropic's AI model, in a Claude session on 5 November 2026, under the direction of Robert (Bob) Dickinson, who supplied the atlas and asked for it as an OpenSWMM Code app. Claude audited the data against EPA's GitHub tags, packed the 941 texts into one file, ported the views into the app shell, added the in-browser integrity check, corrected the Sources text, and wrote the essay, its seven figures and the .docx. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0.0 (2026-11-05): first edition as an app, from the Perplexity-built SWMM5 Source Atlas.

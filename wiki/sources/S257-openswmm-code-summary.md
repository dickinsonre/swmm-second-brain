---
title: "S257: OpenSWMM Code, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/openswmm-code-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-05
ingested: 2026-11-17
tags: [apps, swmm5, source-code, history, versions]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app OpenSWMM Code, version 1.0.0: a browsable atlas of the engine source of 34 EPA SWMM5 releases, 5.0.003 (2004) to 5.2.4 (2023), plus CHI's OpenSWMM 5.1.912 fork, with Compare, Evolution, Search and Release notes views. Nothing is compiled or run. Raw file: [raw/apps/openswmm-code-v1.0.0.md](../../raw/apps/openswmm-code-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793884249-47ed, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the atlas Bob supplied was generated with Perplexity's AI tools, which gathered the releases and wrote the original views. This edition was built with Claude in a session on 5 November 2026 under Bob's direction: Claude audited the data against EPA's GitHub tags, packed the texts into one file, added the in-browser integrity check and corrected the Sources text.

**Claims worth keeping** (all copied from the file)
- EPA's GitHub starts at 5.0.022 (a commit dated April 2014); older builds survived as zips in the Internet Archive or on OpenSWMM.org.
- For the 21 releases from EPA's GitHub, all 1,628 files are identical to the tagged commit (line ends aside), and all 21 commit hashes match their tags.
- The page holds 2,519 file slots and stores each of 941 distinct texts once, named by its SHA-1; all 941 pass the check in the browser.
- 11 of EPA's listed builds have no surviving engine source anywhere public: 5.0.001, 5.0.002, 5.0.004, 5.0.005, 5.0.005a, 5.0.005b, 5.0.006, 5.0.006a, 5.0.010, 5.0.019 and 5.0.020.
- For all 34 releases, the highest build number named in their own files equals the release label.
- Five release dates differ from EPA's update history: 5.1.004 (atlas 2014-04-18, EPA 2014-04-14), 5.1.013 (2018-07-31 against 2018-05-10), 5.1.014 (2020-03-16 against 2020-03-01), 5.1.015 (2020-07-20 against 2020-05-01) and 5.2.4 (2023-08-07 against 2023-07-15). The atlas follows the OpenSWMM catalogue and shows EPA's date beside each.

**Limits it states.** The 13 releases from the Internet Archive and OpenSWMM cannot be compared with a primary source. OpenSWMM fork builds 5.1.907 to 5.1.911 are not in the app. Engine source only: the atlas shows what the code says, not what a model does.

**Checked at ingest.** 34 - 21 = 13 releases from outside GitHub. Five dates in two sources disagree; the page keeps both, and so does this wiki (Q110). EPA's update history is the primary record for EPA's dates; the atlas follows a catalogue. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://openswmm-code.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [OpenSWMM Code (app)](../entities/openswmm-code.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md), [OpenSWMM.org (the forum)](../entities/openswmm-forum.md), [EPA SWMM 5](../entities/swmm-5.md), [OpenSWMM 3D Code Model (app)](../entities/openswmm-3d-code-model.md).

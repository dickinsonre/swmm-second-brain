---
title: "S314: ITM_SWMM Repository Map, summary written from the page (v1.0)"
type: source
raw: raw/apps/itm-swmm-repository-map-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10
ingested: 2026-11-18
tags: [apps, swmm5-gui, itm, transients, pascal]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app ITM_SWMM Repository Map, version 1.0: a map of the fork that fits the Illinois Transient Model into the EPA SWMM 5 GUI. Raw file: [raw/apps/itm-swmm-repository-map-v1.0.md](../../raw/apps/itm-swmm-repository-map-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/1wKHbrMebTmQx7XNpeH2D8, version 1792899660-5383 (index.html, 3,031,523 bytes, SHA-256 6c604371c76b88345ddf31c3258856fe3ec7dee5ffd38b3ae1b0c425b9e3fdc9), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source, chose the repository and decided what the app should be; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A single-file rebuild of Bob's Lovable repository viewer, aimed at one repository: SWMMBobSWMM6/ITM_SWMM, a fork of Arturo S. Leon's ITM_SWMM, which fits the Illinois Transient Model (a finite-volume code for pipes that go from dry to full to pressurized in seconds) into the EPA SWMM 5 Delphi GUI as an optional routing engine. The page carries the repository inside itself (257 files) so it works in the Claude viewer, where the GitHub API cannot be reached.
- The Lovable original could not read this repository: its list of readable extensions had no .pas or .dfm, so it opened 16 of 257 files and none of the 117 Pascal units. The rebuild highlights Pascal and forms, decodes the pictures out of the forms, draws the unit graph and the seam where ITM joins SWMM, parses the three test models, and reads facts from the binaries (itm_swmm.exe, itm2.dll version 2.0, swmm5.dll build 5.2.4).
- File list: 257 files and 33,377,661 bytes from git ls-tree at 572609c; the fork against a fresh clone of upstream with diff -rq.
- Text payload: the SHA-256 of the packed text (2.95 MB) is recomputed in the browser and shown on the About tab.
- Engine messages: all 16 quoted ITM messages checked at build time to appear verbatim in bin/itm2.dll; the build fails if one does not.
- Binaries: machine type, link dates, exports and imports read from the PE headers with pefile; version strings found as literal text in the files.

**Limits it states.** As the page lists it: no diff against EPA's SWMM 5.2 Delphi GUI source; no run of the .exe or DLLs; three binary .dfm forms and the .chm unpacking are not covered; more than 60 GitHub requests an hour are not possible from a saved copy; the CDN libraries need a network.

**Checked at ingest.** The page carries the 257 files of Arturo S. Leon's ITM_SWMM repository; neither the page nor the summary names a license for them. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [ITM_SWMM Repository Map (app)](../entities/itm-swmm-repository-map.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [EPA SWMM 5](../entities/swmm-5.md).

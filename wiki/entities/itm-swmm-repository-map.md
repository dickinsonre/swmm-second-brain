---
title: "ITM_SWMM Repository Map (app)"
type: entity
updated: 2026-11-18
sources: [S314]
tags: [apps, swmm5-gui, itm, transients, pascal]
reviewed: no
---
Bob's app ITM_SWMM Repository Map: a map of the fork that fits the Illinois Transient Model into the EPA SWMM 5 GUI. Version 1.0, 2026-10 [S314](../sources/S314-itm-swmm-repository-map-summary.md). Its `links:` line names no live Netlify address [S314](../sources/S314-itm-swmm-repository-map-summary.md).

**A caution about its source.** The page ships no technical summary. [S314](../sources/S314-itm-swmm-repository-map-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S314](../sources/S314-itm-swmm-repository-map-summary.md)
- A single-file rebuild of Bob's Lovable repository viewer, aimed at one repository: SWMMBobSWMM6/ITM_SWMM, a fork of Arturo S. Leon's ITM_SWMM, which fits the Illinois Transient Model (a finite-volume code for pipes that go from dry to full to pressurized in seconds) into the EPA SWMM 5 Delphi GUI as an optional routing engine. The page carries the repository inside itself (257 files) so it works in the Claude viewer, where the GitHub API cannot be reached.
- The Lovable original could not read this repository: its list of readable extensions had no .pas or .dfm, so it opened 16 of 257 files and none of the 117 Pascal units. The rebuild highlights Pascal and forms, decodes the pictures out of the forms, draws the unit graph and the seam where ITM joins SWMM, parses the three test models, and reads facts from the binaries (itm_swmm.exe, itm2.dll version 2.0, swmm5.dll build 5.2.4).
- File list: 257 files and 33,377,661 bytes from git ls-tree at 572609c; the fork against a fresh clone of upstream with diff -rq.
- Text payload: the SHA-256 of the packed text (2.95 MB) is recomputed in the browser and shown on the About tab.
- Engine messages: all 16 quoted ITM messages checked at build time to appear verbatim in bin/itm2.dll; the build fails if one does not.
- Binaries: machine type, link dates, exports and imports read from the PE headers with pefile; version strings found as literal text in the files.

**How to use it, as the summary puts it.** Use it to find your way around ITM_SWMM before opening Delphi. It runs neither the .exe nor the DLLs, has no diff against EPA's own GUI source (not in the repository), and cannot open three binary .dfm forms or the .chm help. [S314](../sources/S314-itm-swmm-repository-map-summary.md)

**What it does not show.** As the page lists it: no diff against EPA's SWMM 5.2 Delphi GUI source; no run of the .exe or DLLs; three binary .dfm forms and the .chm unpacking are not covered; more than 60 GitHub requests an hour are not possible from a saved copy; the CDN libraries need a network. [S314](../sources/S314-itm-swmm-repository-map-summary.md)

**Noted at ingest.** The page carries the 257 files of Arturo S. Leon's ITM_SWMM repository; neither the page nor the summary names a license for them.

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [EPA SWMM 5](swmm-5.md).

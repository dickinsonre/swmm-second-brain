---
name: ITM_SWMM Repository Map
file: itm-swmm-repository-map.html
version: "1.0"
date: 2026-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/1wKHbrMebTmQx7XNpeH2D8", original: "Lovable app itm-swm-repository-map", repo: "https://github.com/SWMMBobSWMM6/ITM_SWMM (snapshot 572609c, 23 July 2026), a fork of artuleon/ITM_SWMM by Arturo S. Leon"}
engines: none (a snapshot of the repository carried inside the page; nothing is run)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/1wKHbrMebTmQx7XNpeH2D8, version 1792899660-5383 (index.html, 3,031,523 bytes, SHA-256 6c604371c76b88345ddf31c3258856fe3ec7dee5ffd38b3ae1b0c425b9e3fdc9), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# ITM_SWMM Repository Map: a map of the fork that fits the Illinois Transient Model into the EPA SWMM 5 GUI

## In three points
- **What:** A single-file rebuild of Bob's Lovable repository viewer, aimed at one repository: SWMMBobSWMM6/ITM_SWMM, a fork of Arturo S. Leon's ITM_SWMM, which fits the Illinois Transient Model (a finite-volume code for pipes that go from dry to full to pressurized in seconds) into the EPA SWMM 5 Delphi GUI as an optional routing engine. The page carries the repository inside itself (257 files) so it works in the Claude viewer, where the GitHub API cannot be reached.
- **So what:** The Lovable original could not read this repository: its list of readable extensions had no .pas or .dfm, so it opened 16 of 257 files and none of the 117 Pascal units. The rebuild highlights Pascal and forms, decodes the pictures out of the forms, draws the unit graph and the seam where ITM joins SWMM, parses the three test models, and reads facts from the binaries (itm_swmm.exe, itm2.dll version 2.0, swmm5.dll build 5.2.4).
- **Now what:** Use it to find your way around ITM_SWMM before opening Delphi. It runs neither the .exe nor the DLLs, has no diff against EPA's own GUI source (not in the repository), and cannot open three binary .dfm forms or the .chm help.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); it gives the build month (October 2026) but no day. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Map (stats strip, filterable tree, breadcrumb detail panel, treemap), ITM Seam (sixteen quoted ITM messages and seven code observations), Units (the unit graph), Test Models, About, Doc. Repository at snapshot 572609c: branch main, 257 files, 5 folders, 31.83 MB, 4 commits; by size 53.1% Windows binary, 25.8% Delphi form, 7.7% help, 6.9% Pascal unit. The fork differs from upstream only in README.md. A saved copy opened in a browser can run a live check against the GitHub API and encode GIFs; inside the viewer the GIF worker falls back to WebM.

## Checks (as stated on the page)

- File list: 257 files and 33,377,661 bytes from git ls-tree at 572609c; the fork against a fresh clone of upstream with diff -rq.
- Text payload: the SHA-256 of the packed text (2.95 MB) is recomputed in the browser and shown on the About tab.
- Engine messages: all 16 quoted ITM messages checked at build time to appear verbatim in bin/itm2.dll; the build fails if one does not.
- Binaries: machine type, link dates, exports and imports read from the PE headers with pefile; version strings found as literal text in the files.
- Test models: the in-page .inp parser run in Node on all three test files and compared with a separate line scan.
- The original's limit (16 readable files) comes from running its own extension rules over the tree.

## What this does not show

As the page lists it: no diff against EPA's SWMM 5.2 Delphi GUI source; no run of the .exe or DLLs; three binary .dfm forms and the .chm unpacking are not covered; more than 60 GitHub requests an hour are not possible from a saved copy; the CDN libraries need a network.

## Credits and licenses

ITM_SWMM by Arturo S. Leon (upstream artuleon/ITM_SWMM, initial commit 18 October 2025); the fork's commits by dickinsonre; EPA SWMM 5.2 (swmm5.dll); pefile. The page carries the text of the repository's files and names no license for them.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source, chose the repository and decided what the app should be; responsibility is his. Claude read the Lovable source and the ITM_SWMM code, found four problems in the original, and wrote the snapshot build script, the in-page parsers and highlighters, the charts and diagrams, the page, the Doc essay and its .docx, and the seven code observations on the ITM Seam tab. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10): first single-file rebuild (the version read).

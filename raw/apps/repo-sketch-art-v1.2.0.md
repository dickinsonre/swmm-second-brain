---
name: Repo Sketch Art
file: repo-sketch-art.html
version: 1.2.0
date: 2026-10-31
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/NwcCpEWPiHDRXMSgWSEJPF", original: "Lovable export repo-sketch-art (79 files and no app: only the blank starter's placeholder page)", repo: none named in the page}
engines: none (a repository analyzer and hand-drawn renderer written for the page)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session in October 2026 under Robert Dickinson's direction, and that versions 1.1.0 and 1.2.0 answer two outside reviews he supplied. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/NwcCpEWPiHDRXMSgWSEJPF, version 1793471312-1d57 (index.html, 2,751,508 bytes, SHA-256 2f55d25f31a4714082bebafc8fb381058b1838e15bec2e5da89c81187bdb2ec2), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Repo Sketch Art: open the box before you port it

## In three points
- **What:** Opens a repository in the browser (a zip, a folder, or straight from GitHub by owner/repo, branch, folder, file, commit or release link), sorts every file into one of eleven kinds, weighs each against a known Lovable starter, draws the result by hand as a tree or a treemap, and gives a verdict on how much source was written beyond the starter.
- **So what:** It exists because the Lovable export Bob sent under this name held 79 files and no app: the only page was Lovable's placeholder (src/routes/index.tsx, line 23, "REMOVE_THIS"). Two outside reviews graded versions 1.0.0 (B-, six faults) and 1.1.0 (86, a B, five faults); every fault was reproduced in a failing test and fixed, for example 350 blank lines appended to the placeholder counted as 350 lines of code, and a failed manifest still said "the archive is intact".
- **Now what:** Use it before porting any Lovable or other export, to see whether there is an app inside. The verdict counts measured source lines only; unread files and incomplete inventories make it provisional, not firm.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.2.0"); the date is the second outside review's (31 October 2026), which v1.2.0 answers. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Sketch, Files, About, Doc. Hollow circle, faded name: a file identical to the starter; ring with a dot: a starter file that was edited, with the lines added; filled circle: a new file. The verdict counts new source lines (neither blank nor only a comment) beyond the starter; type is decided before folder, so a README in server/ is a doc and a JSON file in tests/fixtures/ is data; docs, data, config, assets, lockfiles and the UI kit never count. Files not read (over 8 MB, a failed download, past the GitHub budget) get a line estimate that never decides a verdict. FILE_MANIFEST.json is checked entry by entry and reported as verified, differs, partial or not checked. In the published Claude artifact GitHub cannot be reached, so the app offers the repository's zip link; the standalone copy (Netlify or a local file) reads GitHub directly.

## Checks (as stated on the page)

- The eleven faults found by the two outside reviews each reproduced in a test that fails on the earlier version, then fixed and kept as regression tests.
- The empty starter kept as the first sample.

## What this does not show

The page's verdicts measure lines of source beyond a starter, not whether the code works. Estimates for unread files never decide a verdict, and an incomplete GitHub file list or an unexamined submodule leaves the verdict provisional.

## Credits and licenses

The Lovable starter template it compares against. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable export, chose this design from three options, and is responsible for the work. Claude inspected the zip and found it held only the empty starter, then wrote the analyzer, the hand-drawn renderer, the tree and treemap layouts, the GitHub loader, the GIF encoder, the page and the Doc essay. Bob supplied the two outside reviews (31 October 2026). This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.2.0 (2026-10-31 or later): five faults from the review of 1.1.0 fixed (the version read).
- 1.1.0: six faults from the review of 1.0.0 fixed.
- 1.0.0 (2026-10): first version.

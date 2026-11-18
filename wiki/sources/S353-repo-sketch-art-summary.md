---
title: "S353: Repo Sketch Art, summary written from the page (v1.2.0)"
type: source
raw: raw/apps/repo-sketch-art-v1.2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-31
ingested: 2026-11-18
tags: [apps, repositories, porting]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Repo Sketch Art, version 1.2.0: open the box before you port it. Raw file: [raw/apps/repo-sketch-art-v1.2.0.md](../../raw/apps/repo-sketch-art-v1.2.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/NwcCpEWPiHDRXMSgWSEJPF, version 1793471312-1d57 (index.html, 2,751,508 bytes, SHA-256 2f55d25f31a4714082bebafc8fb381058b1838e15bec2e5da89c81187bdb2ec2), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable export, chose this design from three options, and is responsible for the work. Claude inspected the zip and found it held only the empty starter, then wrote the analyzer, the hand-drawn renderer, the tree and treemap layouts, the GitHub loader, the GIF encoder, the page and the Doc essay."

**Claims worth keeping** (all copied from the file)
- Opens a repository in the browser (a zip, a folder, or straight from GitHub by owner/repo, branch, folder, file, commit or release link), sorts every file into one of eleven kinds, weighs each against a known Lovable starter, draws the result by hand as a tree or a treemap, and gives a verdict on how much source was written beyond the starter.
- It exists because the Lovable export Bob sent under this name held 79 files and no app: the only page was Lovable's placeholder (src/routes/index.tsx, line 23, "REMOVE_THIS"). Two outside reviews graded versions 1.0.0 (B-, six faults) and 1.1.0 (86, a B, five faults); every fault was reproduced in a failing test and fixed, for example 350 blank lines appended to the placeholder counted as 350 lines of code, and a failed manifest still said "the archive is intact".
- The eleven faults found by the two outside reviews each reproduced in a test that fails on the earlier version, then fixed and kept as regression tests.
- The empty starter kept as the first sample.

**Limits it states.** The page's verdicts measure lines of source beyond a starter, not whether the code works. Estimates for unread files never decide a verdict, and an incomplete GitHub file list or an unexamined submodule leaves the verdict provisional.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Repo Sketch Art (app)](../entities/repo-sketch-art.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Bob's GitHub repositories (where the rest of the material lives)](../entities/bobs-github-repositories.md).

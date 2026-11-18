---
title: "Repo Sketch Art (app)"
type: entity
updated: 2026-11-18
sources: [S353]
tags: [apps, repositories, porting]
reviewed: no
---
Bob's app Repo Sketch Art: open the box before you port it. Version 1.2.0, 2026-10-31 [S353](../sources/S353-repo-sketch-art-summary.md). Its `links:` line names no live Netlify address [S353](../sources/S353-repo-sketch-art-summary.md).

**A caution about its source.** The page ships no technical summary. [S353](../sources/S353-repo-sketch-art-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S353](../sources/S353-repo-sketch-art-summary.md)
- Opens a repository in the browser (a zip, a folder, or straight from GitHub by owner/repo, branch, folder, file, commit or release link), sorts every file into one of eleven kinds, weighs each against a known Lovable starter, draws the result by hand as a tree or a treemap, and gives a verdict on how much source was written beyond the starter.
- It exists because the Lovable export Bob sent under this name held 79 files and no app: the only page was Lovable's placeholder (src/routes/index.tsx, line 23, "REMOVE_THIS"). Two outside reviews graded versions 1.0.0 (B-, six faults) and 1.1.0 (86, a B, five faults); every fault was reproduced in a failing test and fixed, for example 350 blank lines appended to the placeholder counted as 350 lines of code, and a failed manifest still said "the archive is intact".
- The eleven faults found by the two outside reviews each reproduced in a test that fails on the earlier version, then fixed and kept as regression tests.
- The empty starter kept as the first sample.

**How to use it, as the summary puts it.** Use it before porting any Lovable or other export, to see whether there is an app inside. The verdict counts measured source lines only; unread files and incomplete inventories make it provisional, not firm. [S353](../sources/S353-repo-sketch-art-summary.md)

**What it does not show.** The page's verdicts measure lines of source beyond a starter, not whether the code works. Estimates for unread files never decide a verdict, and an incomplete GitHub file list or an unexamined submodule leaves the verdict provisional. [S353](../sources/S353-repo-sketch-art-summary.md)

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Bob's GitHub repositories (where the rest of the material lives)](bobs-github-repositories.md).

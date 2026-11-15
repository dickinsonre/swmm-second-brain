---
title: "S57: setup.sh of the old swmm-brain repository (the list of knowledge repositories)"
type: source
raw: raw/swmm-brain/setup.sh
kind: script
author: Robert Dickinson
published: 2026-08-22
ingested: 2026-11-14
tags: [repositories, method]
reviewed: 2026-11-15
---
**What it is.** A shell script that clones or updates a list of GitHub repositories as sibling folders, then says "Start the brain: claude". Its value here is the list, with Bob's one-line description of each repository. Raw file: [raw/swmm-brain/setup.sh](../../raw/swmm-brain/setup.sh). Dated by the repository's last commit.

**How it was written.** Not stated.

**Claims worth keeping**
- Six repositories are active by default, described as the "knowledge substrate": `rdickinson-rdickinson` (life's work, SWMM and ICM), `AWI_RED_Combined` (consolidated Ruby and source toolkit), `InfoWorks-ICM-Ruby-Scripting-`, `ICM_Tools` (ICM SQL and Ruby helpers), `Innovyze-ICM-Libraries`, `SwmmHistory`. All under the owner `Dickinsonre`.
- Twelve more are listed, commented out, among them `ReSWMM`, `InfoSewer-to-ICM`, `EPANET-SWMM5-Generate`, `Open-Source-Support`, and four under `SWMMEnablement`: `bobswmmapps` (an index of Bob's browser apps), `rulesforresponsiblemodeling`, `epa-swmm5-essentials`, `.github`.
- The repositories are cloned side by side and keep their own histories. The old repository's ignore file leaves every top-level folder but `notes/` out of version control, so the clones never entered it.
- The script prefers full history over shallow clones: "History is the point for legacy work".

**Feeds:** [Bob's GitHub repositories (where the rest of the material lives)](../entities/bobs-github-repositories.md), [swmm-brain (the old brain repository)](../entities/swmm-brain-repo.md).

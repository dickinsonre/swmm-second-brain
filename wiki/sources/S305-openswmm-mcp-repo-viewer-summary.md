---
title: "S305: OpenSWMM MCP Repo Viewer, summary written from the page (v1.1)"
type: source
raw: raw/apps/openswmm-mcp-repo-viewer-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, swmm6, openswmm, mcp, repositories]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app OpenSWMM MCP Repo Viewer, version 1.1: HydroCouple's MCP server for OpenSWMM 6, with the engine, GUI and gymnasium. Raw file: [raw/apps/openswmm-mcp-repo-viewer-v1.1.md](../../raw/apps/openswmm-mcp-repo-viewer-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/WBjjAc1zXQDszVjaNzR1KJ, version 1792903632-89cc (index.html, 5,310,214 bytes, SHA-256 a0a3e41f2bb08cb736c70215384accae6cce8ddd649c920925726a8093ea5a6a), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says it was built with Claude, Anthropic's AI model, under the direction of Robert (Bob) Dickinson, who supplied the Lovable source; version 1.0 on 24 October 2026 and version 1.1 on 25 October. Claude cloned the repositories and built the snapshot and source packs, measured the Lovable defects, parsed the tool catalog, and wrote the page and the Doc. This summary was written by Claude on 18 November 2026 from the published page."

**Claims worth keeping** (all copied from the file)
- A single-file browser for HydroCouple/openswmm.mcp, the Model Context Protocol server for the OpenSWMM 6 engine: its README, every file on both branches, the MCP tools the server registers, its commits, its three open pull requests, and an Ask panel that can read all of it. Version 1.1 adds source packs of the three SWMM6 repositories the server sits on (openswmm.engine swmm6_rel, openswmm.gui swmm6_gui, openswmm.gymnasium dev). A rebuild of Bob's Lovable app.
- The snapshot counts 105 files on dev and 2 on main, 59 commits on dev, and a FastMCP server with 20 tools (14 core), 8 prompts, 6 resources, 3 skills and 10 settings, parsed with Python's ast module. Of the three PRs, #1 merges clean, #2 has 11 conflicting files and #3 has 3. PyPI's openswmm.mcp is 0.0.0. The Lovable defects were measured: a fetch loop (119 requests against 1), a preview filter that refused 9 files, and a 12,000-character cut that truncated 13 files.
- Files and contents read with git ls-tree and cat-file; history from git log --numstat (59 commits on dev, 1 on main, 9 on PR #2, 12 on PR #3).
- Merge status with git merge-tree against each base.
- Tool catalog parsed with Python's ast; the 14 core names match the CORE set in tests/unit/test_server_budget.py.
- PyPI: openswmm.mcp 0.0.0 downloaded and its wheel listed (not installed or run); FastMCP 3.4.11 installed in a scratch environment, where pip reported the missing auth extra.

**Limits it states.** As the page lists it: anything after the snapshot; CI runs and test results; review comments and discussions; running the server or the engine; engine and GUI images and data files.

**Checked at ingest.** The page carries OpenSWMM source text (Apache-2.0); its Netlify folder adds OPENSWMM-LICENSE and OPENSWMM-NOTICE. The page shows email addresses of HydroCouple developers inside the packs it displays. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [OpenSWMM MCP Repo Viewer (app)](../entities/openswmm-mcp-repo-viewer.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [OpenSWMM Code (app)](../entities/openswmm-code.md).

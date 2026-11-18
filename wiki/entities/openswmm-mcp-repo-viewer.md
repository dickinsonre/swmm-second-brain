---
title: "OpenSWMM MCP Repo Viewer (app)"
type: entity
updated: 2026-11-18
sources: [S305]
tags: [apps, swmm6, openswmm, mcp, repositories]
reviewed: no
---
Bob's app OpenSWMM MCP Repo Viewer: HydroCouple's MCP server for OpenSWMM 6, with the engine, GUI and gymnasium. Version 1.1, 2026-10-25 [S305](../sources/S305-openswmm-mcp-repo-viewer-summary.md). Its `links:` line names no live Netlify address [S305](../sources/S305-openswmm-mcp-repo-viewer-summary.md).

**A caution about its source.** The page ships no technical summary. [S305](../sources/S305-openswmm-mcp-repo-viewer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S305](../sources/S305-openswmm-mcp-repo-viewer-summary.md)
- A single-file browser for HydroCouple/openswmm.mcp, the Model Context Protocol server for the OpenSWMM 6 engine: its README, every file on both branches, the MCP tools the server registers, its commits, its three open pull requests, and an Ask panel that can read all of it. Version 1.1 adds source packs of the three SWMM6 repositories the server sits on (openswmm.engine swmm6_rel, openswmm.gui swmm6_gui, openswmm.gymnasium dev). A rebuild of Bob's Lovable app.
- The snapshot counts 105 files on dev and 2 on main, 59 commits on dev, and a FastMCP server with 20 tools (14 core), 8 prompts, 6 resources, 3 skills and 10 settings, parsed with Python's ast module. Of the three PRs, #1 merges clean, #2 has 11 conflicting files and #3 has 3. PyPI's openswmm.mcp is 0.0.0. The Lovable defects were measured: a fetch loop (119 requests against 1), a preview filter that refused 9 files, and a 12,000-character cut that truncated 13 files.
- Files and contents read with git ls-tree and cat-file; history from git log --numstat (59 commits on dev, 1 on main, 9 on PR #2, 12 on PR #3).
- Merge status with git merge-tree against each base.
- Tool catalog parsed with Python's ast; the 14 core names match the CORE set in tests/unit/test_server_budget.py.
- PyPI: openswmm.mcp 0.0.0 downloaded and its wheel listed (not installed or run); FastMCP 3.4.11 installed in a scratch environment, where pip reported the missing auth extra.

**How to use it, as the summary puts it.** Use it to read the MCP server and its SWMM6 dependencies offline. It is a snapshot (late 24 October 2026): no CI runs, review comments or discussions, and neither the server nor the engine is run. [S305](../sources/S305-openswmm-mcp-repo-viewer-summary.md)

**What it does not show.** As the page lists it: anything after the snapshot; CI runs and test results; review comments and discussions; running the server or the engine; engine and GUI images and data files. [S305](../sources/S305-openswmm-mcp-repo-viewer-summary.md)

**Noted at ingest.** The page carries OpenSWMM source text (Apache-2.0); its Netlify folder adds OPENSWMM-LICENSE and OPENSWMM-NOTICE. The page shows email addresses of HydroCouple developers inside the packs it displays.

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [OpenSWMM Code (app)](openswmm-code.md).

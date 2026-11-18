---
name: OpenSWMM MCP Repo Viewer
file: openswmm-mcp-repo-viewer.html
version: "1.1"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/WBjjAc1zXQDszVjaNzR1KJ", original: "Lovable app openswmm-mcp-repo-viewer", repo: "https://github.com/HydroCouple/openswmm.mcp (the repository the page views)"}
engines: none (a snapshot of four repositories carried in the page; nothing is run)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 24 and 25 October 2026 under Robert Dickinson's direction. Its Ask panel uses Claude inside a Claude artifact. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/WBjjAc1zXQDszVjaNzR1KJ, version 1792903632-89cc (index.html, 5,310,214 bytes, SHA-256 a0a3e41f2bb08cb736c70215384accae6cce8ddd649c920925726a8093ea5a6a), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# OpenSWMM MCP Repo Viewer: HydroCouple's MCP server for OpenSWMM 6, with the engine, GUI and gymnasium

## In three points
- **What:** A single-file browser for HydroCouple/openswmm.mcp, the Model Context Protocol server for the OpenSWMM 6 engine: its README, every file on both branches, the MCP tools the server registers, its commits, its three open pull requests, and an Ask panel that can read all of it. Version 1.1 adds source packs of the three SWMM6 repositories the server sits on (openswmm.engine swmm6_rel, openswmm.gui swmm6_gui, openswmm.gymnasium dev). A rebuild of Bob's Lovable app.
- **So what:** The snapshot counts 105 files on dev and 2 on main, 59 commits on dev, and a FastMCP server with 20 tools (14 core), 8 prompts, 6 resources, 3 skills and 10 settings, parsed with Python's ast module. Of the three PRs, #1 merges clean, #2 has 11 conflicting files and #3 has 3. PyPI's openswmm.mcp is 0.0.0. The Lovable defects were measured: a fetch loop (119 requests against 1), a preview filter that refused 9 files, and a 12,000-character cut that truncated 13 files.
- **Now what:** Use it to read the MCP server and its SWMM6 dependencies offline. It is a snapshot (late 24 October 2026): no CI runs, review comments or discussions, and neither the server nor the engine is run.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.1 · 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Ask, Overview, Files, Tools, Commits, Pull requests, Fixes, About, Doc. Snapshot heads: dev 60995e0 (24 October 2026), main eeb8200 (11 April 2026); PR #1 dev, PR #2 fix/fastmcp-deps-and-control-rule-tests, PR #3 feature/ledger. SWMM6 packs: openswmm.engine swmm6_rel @ 8c77aa8 (3,000 files, 2,529 packed, 9.8 MB), openswmm.gui swmm6_gui @ 25a2fab (3,068 files, 2,475 packed, 8.9 MB), openswmm.gymnasium dev @ f18af22 (225 files, 223 packed, 0.3 MB). Text files up to 600 KB are packed; images, binaries and data files are listed, not packed. Libraries: marked 12.0.2, DOMPurify 3.1.6, highlight.js 11.9.0, html2canvas 1.4.1, gif.js 0.2.0 from cdnjs.

## Checks (as stated on the page)

- Files and contents read with git ls-tree and cat-file; history from git log --numstat (59 commits on dev, 1 on main, 9 on PR #2, 12 on PR #3).
- Merge status with git merge-tree against each base.
- Tool catalog parsed with Python's ast; the 14 core names match the CORE set in tests/unit/test_server_budget.py.
- PyPI: openswmm.mcp 0.0.0 downloaded and its wheel listed (not installed or run); FastMCP 3.4.11 installed in a scratch environment, where pip reported the missing auth extra.
- The Lovable defects reproduced in a React harness and against the dev file list.

## What this does not show

As the page lists it: anything after the snapshot; CI runs and test results; review comments and discussions; running the server or the engine; engine and GUI images and data files.

## Credits and licenses

HydroCouple's openswmm.mcp, openswmm.engine, openswmm.gui and openswmm.gymnasium (Caleb Buahin and contributors); FastMCP. The page carries packed source text of openswmm.engine at swmm6_rel, which is Apache-2.0; its About tab does not reproduce the upstream LICENSE and NOTICE.

## AI use

The page says it was built with Claude, Anthropic's AI model, under the direction of Robert (Bob) Dickinson, who supplied the Lovable source; version 1.0 on 24 October 2026 and version 1.1 on 25 October. Claude cloned the repositories and built the snapshot and source packs, measured the Lovable defects, parsed the tool catalog, and wrote the page and the Doc. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.1 (2026-10-25): adds the engine, GUI and gymnasium repositories (the version read).
- 1.0 (2026-10-24): single-file rebuild of the Lovable viewer.

---
name: Understand Anything for SWMM and ICM
file: understand-anything-swmm-icm.html
version: "2.0"
date: 2026-11-05
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/VetHDrnAKHM2SMStTy1Wfr", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4, commit 7952ca8, compiled with gcc for measurement only (54 objects)", license: public domain}
  - {name: OpenSWMM Engine, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: 79bb4e1, note: "278 of 284 .cpp compiled with g++ -std=c++20, nothing executed", license: Apache-2.0}
tools: [gcc -fcallgraph-info, nm, graphify 0.9.102, networkx (comparison only)]
units: counts of files, functions, links and scripts
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/VetHDrnAKHM2SMStTy1Wfr, version 1793890442-8573 (index.html, 403,201 bytes, SHA-256 00b9bcfea32d5473d01b36af3a7b95053e9c61b93bda063dd11b7dce521c8a46), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Understand Anything for SWMM and ICM: code graphs of EPA SWMM 5.2.4, OpenSWMM 6 and the ICM Ruby scripts, checked against the compiler

## In three points
- **What:** Measures the file links and call graph of EPA SWMM 5.2.4 with the compiler and linker, compares OpenSWMM 6, censuses 532 ICM Ruby scripts, and scores code-graph tools (a June hand-drawn map, graphify) against that referee.
- **So what:** The June map found 60 of the 365 real file links and drew 28 wrong; graphify found 322 and invented none; and 46 of the 54 SWMM 5.2.4 files form one knot, so no learning order can run one way.
- **Now what:** Trust a code map only after checking it against the compiler; drop your own graph on the Your graph tab to score it. Understand Anything itself was read, not run.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v2.0 · Nov 2026"); the date is the build session's, 5 November 2026. The file name is the one the page says it updates. Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

It updates understand-anything-swmm-icm.html of 21 June 2026, which explained the Understand Anything code-graph plugin with a SWMM5 map drawn from memory. This version measures the map, tests the tools and gives a tracer for 967 functions, a census of the ICM Ruby scripts, and a place to drop your own graph. Tabs: Results, Engine graph, Your graph, ICM Ruby, Playbooks, Commands, About, Doc.

## Results the page reports

- The June map drew routing.c to dynwave.c; routing.c never calls dynwave.c (routeFlow calls flowrout_execute, and line 167 of flowrout.c calls dynwave_execute).
- EPA SWMM 5.2.4: 365 file links, 324 with calls, 79 with data; 967 functions, 1,916 call edges.
- June map: 60 of 365 real links, 24 that do not exist, 4 backward; 8 real files left out (among them error.c, rain.c, odesolve.c); 68% right among lines drawn, 16% of what is there.
- graphify free pass: 322 links in 2.3 seconds, none invented; 1,877 of the 1,916 call edges; from swmm_step all 443 functions the compiler reaches. Its 6 extra edges: five touch Windows-only xfilter, one an OpenMP call.
- The knot: 46 of 54 files form one strongly connected set; 60 pairs use each other directly; 8 leaf files (datetime.c, error.c, findroot.c, hash.c, keywords.c, mathexpr.c, mempool.c, odesolve.c); the best order still leaves 70 of 365 uses pointing backward.
- OpenSWMM 6: 278 of 284 .cpp compiled (6 need HDF5); 1 public writable symbol against 332 in SWMM 5.2.4; SimulationContext's header reaches 175 of 278 files; a knot of 31 of 278 files.
- ICM Ruby: 288 of 532 scripts contain no def; graphify gives 27 of 531 files a cross-file edge; a regular expression finds 63 tables touched, _links in 56 scripts, _nodes in 47, hw_subcatchment in 40.

## Checks (as stated on the page)

- All 54 EPA objects compiled at tag v5.2.4, commit 7952ca8, and read with nm; uses.py reproduced 365, 324 and 79 exactly; tables.py reproduced the Ruby census.
- The page's cut-vertex and betweenness code against networkx: same cut vertex on the 54-file sample (betweenness within 3.5e-18); same 26 cut vertices on graphify's 1,110-node graph (within 1.4e-17).
- Every graphify command marked "ran here" was run; headless browser test of all tabs, both themes, phone width, file drop, CSV and GIF, no console errors.

## What this does not show

- Understand Anything's real output: a safety check in the build session refused to build its downloaded code, and nobody worked around it.
- The D:\Swmm5.2.3-ApiGuide graph: that computer was not reachable.
- Windows builds: the reference is Linux gcc.
- Whether a path runs in a given model; a link says only that one file can reach another.
- Private coupling (statics, header-only C++, virtual dispatch, templates).
- The ICM solver (closed source; only the Ruby layer is measured); PySWMM, swmm_api and EPANET are listed but not measured.

## How to reproduce

The page names its scripts (uses.py, tables.py) and commands (gcc -c, nm, gcc -fcallgraph-info, graphify update); they are not shipped in the page. Your graph accepts a dropped graph file, for example Understand Anything's .ua/knowledge-graph.json.

## Credits and licenses

EPA SWMM 5.2.4 source (public domain). OpenSWMM Engine (HydroCouple; Caleb Buahin and the OpenSWMM team), Apache-2.0. graphify 0.9.102. Understand Anything, read from its source. No license is stated for the page itself.

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude session on 5 November 2026, under the direction of Robert (Bob) Dickinson, who chose the idea to update, supplied the session transcript and set the standing rules for testing and disclosure. Claude recovered the June app from the chat, compiled both engines, wrote the analysis and census scripts, ran graphify, scored the results, and wrote the page, the essay and the defect register. The June map that this version scores was also drawn by Claude, from memory. No person has reviewed the role descriptions, the defect wording or the essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2.0 (2026-11-05): measures the code graphs against the compiler; replaces the June 2026 hand-drawn map.
- June 2026: first version, an explainer for Understand Anything.

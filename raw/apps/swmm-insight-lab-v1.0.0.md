---
name: SWMM Insight Lab
file: swmm-insight-lab.html
version: 1.0.0
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/T1ThLQ4gdZq9ekKSJgaNbF", original: "Lovable project swmm-insight-lab (explorer v0.3.0, module data extracted 2026-05-31)", repo: "https://github.com/CIMM-ORG/SWMM5plus (commit afd44de, the code the page maps)"}
engines: none (a static map of the SWMM5+ Fortran source; a C-port scaffold the page generates compiles with gcc and clang)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/T1ThLQ4gdZq9ekKSJgaNbF, version 1792956479-51b6 (index.html, 1,327,923 bytes, SHA-256 9207a2ca7df7e2cb36f9c23e42dcfaac9cae45b2d08b9acf71dc17e37df65d6d), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM Insight Lab: a map of the SWMM5+ engine and its relation to EPA SWMM 5.1.13

## In three points
- **What:** Maps CIMM's SWMM5+ hydraulics engine at commit afd44de: its folder tree, its Fortran module graph, the papers behind it, its relation to the EPA SWMM 5.1.13 C code it links, a C-port scaffold, and the seven query tools of the original Lovable build (subtitle: SWMM5+ Repo Explorer). The Lovable README described a different app, a Mars settlement model; the code was this explorer.
- **So what:** Re-running the module extraction matched the Lovable data on 71 of 71 module declarations and 534 of 534 edges, and found 4 repeated use statements it had dropped. But 27 of the curated dependency edges do not exist in the source. The audit register holds 24 entries (broken, wrong, missing, unverified, improvement).
- **Now what:** Use it to find your way around SWMM5+ and its EPA counterparts. It shows what static reading can measure: there is no call graph, no speed on N processors, and no accuracy against EPA SWMM; the module summaries and relation labels are a person's reading, unchecked.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0.0 · 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Overview, Code tree, Architecture, Papers, vs EPA C, C scaffold, Tools, Audit, About, Doc. Measured from source and repeatable with the scripts: a census of 668 files, a use graph of 541 statements, the existence of the C files and EPA symbols, paper metadata from Crossref, and a scaffold that compiles. A zip writer exports the scaffold.

## Checks (as stated on the page)

- Cloned CIMM-ORG/SWMM5plus at afd44de and confirmed CIMM-ORG/SWMM5plus-1 points at the same commit.
- Module extraction re-run with the same regular expressions: 71 of 71 declarations and 534 of 534 edges match; 4 dropped use statements found.
- All 23 EPA counterpart files exist in both v5.1.13 and master; every named EPA function grepped in the 5.1.13 tree.
- Curated dependency edges checked against the source: 27 do not exist.
- 9 paper DOIs looked up on Crossref; the EPA grant's publication list read for the 2 conference talks; the SWMM5+ introduction paper's full text read on NSF PAR for its CFL, processor-count and research-status statements.
- The C scaffold zip built from the page's own code, unzipped and compiled with gcc and clang.

## What this does not show

As the page lays out: judgment, not checked (relation labels, unflagged module summaries, paper-to-module links, the subsystem of each folder, which EPA file is "nearest"); and outside what static reading can do (the call graph, speed on N processors, accuracy against EPA SWMM).

## Credits and licenses

SWMM5+ source, CIMM-ORG/SWMM5plus @ afd44de (public domain, per its LICENSE); EPA SWMM 5.1.13 (public domain); Hodges et al. (2024), Introducing SWMM5+, J. Environ. Eng. 150(10), doi:10.1061/JOEEDU.EEENG-7680; SWMM5+ Alpha technical report, doi:10.18738/T8/WQZ5EX; EPA Cooperative Agreement 83595001 publications.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for a single-file HTML app; responsibility is his. Claude read the Lovable source, cloned SWMM5+ and the EPA SWMM v5.1.13 and master trees, re-ran the module extraction, checked every C file, EPA function name, curated edge and paper, wrote the 24-entry audit register, and wrote the page's code (graph layout, zip writer, GIF encoder, scaffold generator) and the Doc. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.0 (2026-10-25): first single-file edition (the version read).

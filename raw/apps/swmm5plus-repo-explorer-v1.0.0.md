---
name: SWMM5+ Repo Explorer
file: swmm5plus-repo-explorer.html
version: 1.0.0
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/FZYrywFPdvNLuN7sFYCCEr", original: "Lovable project swmm-insight-lab (TanStack Start, React, a Lovable-hosted MCP server)", repo: "https://github.com/CIMM-ORG/SWMM5plus (commit afd44de, the code the page carries)"}
engines: none (the SWMM5+ Fortran source, 85 files, embedded and searchable; nothing is run)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude on 25 October 2026 under Robert Dickinson's direction, with a Claude sub-agent checking the paper citations. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/FZYrywFPdvNLuN7sFYCCEr, version 1792951511-0345 (index.html, 2,415,065 bytes, SHA-256 02cd72622aa6d8b43659da702e817dbbba89af02286e4bdc46ee495bf075f7ef), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# SWMM5+ Repo Explorer: the SWMM5+ source at afd44de, with its links to EPA SWMM 5.1.13 checked

## In three points
- **What:** The explorer from Bob's Lovable project swmm-insight-lab, rebuilt as one HTML file that runs offline, with every count re-extracted from the SWMM5+ source at commit afd44de. It adds the main program as a source unit, use, intrinsic statements, the Fortran source itself (all 85 files in the eight source folders, embedded and searchable), procedure counts, links pinned to a commit, corrected C paths and function names, a checked paper list and a findings register. (SWMM Insight Lab is a second single-file edition of the same Lovable project.)
- **So what:** None of the Lovable build's runtime links to the EPA C code resolved. SWMM5+ downloads EPA SWMM v5.1.13 (CMakeLists.txt lines 82 to 85), whose engine sits in src/; EPA moved it to src/solver/ after 5.1.13, and the Lovable table wrote every C path in the new layout while pinning the link to the old tag. Also, 27 of 130 curated edges have no use statement behind them; the edition keeps them, drawn dashed.
- **Now what:** Use it to browse SWMM5+ and its EPA counterparts offline. The graph is the use graph (which module may see which), not a call graph; nothing runs SWMM5+ or EPA SWMM; the C scaffold's stubs compile because they are empty.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0.0"); the date is the build session the page names. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Overview, Code tree, Architecture, Papers, vs EPA C, C scaffold, Tools, Findings, About, Doc. Provenance: CIMM-ORG/SWMM5plus at afd44de (2024-11-25), with SWMM5plus-1 an identical copy; EPA runtime v5.1.13; EPA reference master @ 7952ca8 (2023-10-10). Extraction by regular expressions over each .f90 line after stripping comments (module or program units; use statements with intrinsic and only lists; subroutine and function declarations outside interface blocks). The Lovable build's curated catalog, summaries and relation labels (extracted 2026-05-31) are kept, with corrections marked.

## Checks (as stated on the page)

- Module and use extraction re-run with a corrected pattern; procedures counted.
- Every cited C path listed in both EPA trees and every cited function grepped in v5.1.13.
- Paper citations checked against publisher pages by a Claude sub-agent.
- Lovable build against this edition on four measures: Fortran source units, use statements recorded, C links resolving at v5.1.13, curated edges backed by a use.

## What this does not show

As the page lists it: the use graph is not a call graph, and shows no coarray traffic between images or calls into the C engine; nothing runs SWMM5+ or EPA SWMM, so no claim about accuracy, speed or stability is tested; the C scaffold translates nothing; module summaries and C relation labels come from the Lovable build, and only the Findings items were checked line by line; the source is one commit.

## Credits and licenses

SWMM5+ (CIMM-ORG/SWMM5plus, public domain); EPA SWMM v5.1.13 and master (public domain). The embedded source keeps its upstream file headers.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who made the original Lovable app, supplied its source and asked for a single-file HTML version; responsibility is his. Claude read the Lovable source, cloned SWMM5+ at afd44de and EPA SWMM at v5.1.13 and master, re-ran the extraction, counted procedures, checked every cited C file and function, and wrote the page, its findings register, the Doc essay and the .docx; a Claude sub-agent checked the paper citations against publisher pages. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.0 (2026-10-25): first single-file edition (the version read).

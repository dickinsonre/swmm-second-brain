---
title: "S310: SWMM5+ Repo Explorer, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/swmm5plus-repo-explorer-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, swmm5plus, fortran, repositories]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app SWMM5+ Repo Explorer, version 1.0.0: the SWMM5+ source at afd44de, with its links to EPA SWMM 5.1.13 checked. Raw file: [raw/apps/swmm5plus-repo-explorer-v1.0.0.md](../../raw/apps/swmm5plus-repo-explorer-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/FZYrywFPdvNLuN7sFYCCEr, version 1792951511-0345 (index.html, 2,415,065 bytes, SHA-256 02cd72622aa6d8b43659da702e817dbbba89af02286e4bdc46ee495bf075f7ef), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who made the original Lovable app, supplied its source and asked for a single-file HTML version; responsibility is his."

**Claims worth keeping** (all copied from the file)
- The explorer from Bob's Lovable project swmm-insight-lab, rebuilt as one HTML file that runs offline, with every count re-extracted from the SWMM5+ source at commit afd44de. It adds the main program as a source unit, use, intrinsic statements, the Fortran source itself (all 85 files in the eight source folders, embedded and searchable), procedure counts, links pinned to a commit, corrected C paths and function names, a checked paper list and a findings register. (SWMM Insight Lab is a second single-file edition of the same Lovable project.)
- None of the Lovable build's runtime links to the EPA C code resolved. SWMM5+ downloads EPA SWMM v5.1.13 (CMakeLists.txt lines 82 to 85), whose engine sits in src/; EPA moved it to src/solver/ after 5.1.13, and the Lovable table wrote every C path in the new layout while pinning the link to the old tag. Also, 27 of 130 curated edges have no use statement behind them; the edition keeps them, drawn dashed.
- Module and use extraction re-run with a corrected pattern; procedures counted.
- Every cited C path listed in both EPA trees and every cited function grepped in v5.1.13.
- Paper citations checked against publisher pages by a Claude sub-agent.
- Lovable build against this edition on four measures: Fortran source units, use statements recorded, C links resolving at v5.1.13, curated edges backed by a use.

**Limits it states.** As the page lists it: the use graph is not a call graph, and shows no coarray traffic between images or calls into the C engine; nothing runs SWMM5+ or EPA SWMM, so no claim about accuracy, speed or stability is tested; the C scaffold translates nothing; module summaries and C relation labels come from the Lovable build, and only the Findings items were checked line by line; the source is one commit.

**Checked at ingest.** It is a second single-file edition of the Lovable project swmm-insight-lab, the same project as [SWMM Insight Lab (app)](../entities/swmm-insight-lab.md); the two editions are kept as two pages because they hold different apps. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM5+ Repo Explorer (app)](../entities/swmm5plus-repo-explorer.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [SWMM5+ (CIMM finite-volume engine)](../entities/swmm5plus.md), [SWMM5+ Explorer (app)](../entities/swmm5plus-explorer.md).

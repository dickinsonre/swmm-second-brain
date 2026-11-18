---
title: "S311: SWMM Insight Lab, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/swmm-insight-lab-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, swmm5plus, fortran, dependency-graph, audits]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Insight Lab, version 1.0.0: a map of the SWMM5+ engine and its relation to EPA SWMM 5.1.13. Raw file: [raw/apps/swmm-insight-lab-v1.0.0.md](../../raw/apps/swmm-insight-lab-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/T1ThLQ4gdZq9ekKSJgaNbF, version 1792956479-51b6 (index.html, 1,327,923 bytes, SHA-256 9207a2ca7df7e2cb36f9c23e42dcfaac9cae45b2d08b9acf71dc17e37df65d6d), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for a single-file HTML app; responsibility is his."

**Claims worth keeping** (all copied from the file)
- Maps CIMM's SWMM5+ hydraulics engine at commit afd44de: its folder tree, its Fortran module graph, the papers behind it, its relation to the EPA SWMM 5.1.13 C code it links, a C-port scaffold, and the seven query tools of the original Lovable build (subtitle: SWMM5+ Repo Explorer). The Lovable README described a different app, a Mars settlement model; the code was this explorer.
- Re-running the module extraction matched the Lovable data on 71 of 71 module declarations and 534 of 534 edges, and found 4 repeated use statements it had dropped. But 27 of the curated dependency edges do not exist in the source. The audit register holds 24 entries (broken, wrong, missing, unverified, improvement).
- Cloned CIMM-ORG/SWMM5plus at afd44de and confirmed CIMM-ORG/SWMM5plus-1 points at the same commit.
- Module extraction re-run with the same regular expressions: 71 of 71 declarations and 534 of 534 edges match; 4 dropped use statements found.
- All 23 EPA counterpart files exist in both v5.1.13 and master; every named EPA function grepped in the 5.1.13 tree.
- Curated dependency edges checked against the source: 27 do not exist.

**Limits it states.** As the page lays out: judgment, not checked (relation labels, unflagged module summaries, paper-to-module links, the subsystem of each folder, which EPA file is "nearest"); and outside what static reading can do (the call graph, speed on N processors, accuracy against EPA SWMM).

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM Insight Lab (app)](../entities/swmm-insight-lab.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [SWMM5+ (CIMM finite-volume engine)](../entities/swmm5plus.md), [SWMM5+ Repo Explorer (app)](../entities/swmm5plus-repo-explorer.md).

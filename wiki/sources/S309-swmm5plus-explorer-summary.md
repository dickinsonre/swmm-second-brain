---
title: "S309: SWMM5+ Explorer, summary written from the page (v1.0.1)"
type: source
raw: raw/apps/swmm5plus-explorer-v1.0.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, swmm5plus, fortran, c-port, audits]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app SWMM5+ Explorer, version 1.0.1: the Fortran source, the Lovable sketch, and a proposed C port, checked against upstream. Raw file: [raw/apps/swmm5plus-explorer-v1.0.1.md](../../raw/apps/swmm5plus-explorer-v1.0.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/LA4iK6BCAEUX7BZo52R53v, version 1792893142-e99a (index.html, 246,771 bytes, SHA-256 03a52c5c5b9e93fdd2768f18611d90d5b270054a2d62cb94b08eb83d04db75ab), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model (a Claude Code session configured for Claude Fable 5.1), in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable export, asked for it as a single HTML file, and set the standing rules the build follows."

**Claims worth keeping** (all copied from the file)
- A single-file rebuild of a Lovable microsite about SWMM5+, the parallel Fortran hydraulics engine from the University of Texas at Austin published through CIMM.org: home, architecture, an engine tour, a hydraulics primer and a chat (HydroBot), with verbatim excerpts cut from the upstream source at commit afd44de. What the rebuild adds is verification: every claim the Lovable copy made is checked against the code.
- Of twelve Lovable claims in the defect register, 4 hold, 6 are wrong and 2 are partly right. It said "about 40k lines of modern Fortran" where upstream has 88,020 lines in 72 files; it said the step calls MPI_Bcast and MPI_Allreduce where no .f90 file makes an MPI call (SWMM5+ uses coarrays, with 111 sync all); it described a Roe-style upwind face flux where update.f90 uses timescale interpolation weights.
- Upstream cloned at afd44de (mirror CIMM-ORG/SWMM5plus-1); an extraction script cuts and anchors the verbatim excerpts and counts lines, files, coarray syncs and BIND(C) interfaces.
- Each Lovable claim given a verdict against the source (holds, partly, wrong).

**Limits it states.** As the page lists it: no SWMM5+ simulation was run, so every number is about the source, not a result; the proposed C engine was never compiled; the excerpts are one commit of a Beta repository.

**Checked at ingest.** The page shows Ben Hodges's email address as it appears in the SWMM5+ sources. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM5+ Explorer (app)](../entities/swmm5plus-explorer.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [SWMM5+ (CIMM finite-volume engine)](../entities/swmm5plus.md), [SWMM5+ Branch Atlas (app)](../entities/swmm5plus-branch-atlas.md).

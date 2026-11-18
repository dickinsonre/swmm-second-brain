---
name: SWMM5+ Explorer
file: swmm5plus-explorer.html
version: 1.0.1
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/LA4iK6BCAEUX7BZo52R53v", original: "Lovable export swmm5plus-explorer-source.zip (TanStack Start, React 19, Tailwind v4; 95 files)", repo: "https://github.com/CIMM-ORG/SWMM5plus (commit afd44de, 2024-11-25, the code the page quotes)"}
engines: none (verbatim excerpts of the SWMM5+ Fortran source; no SWMM5+ run; the proposed C port has never compiled)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (a Claude Code session configured for Claude Fable 5.1) in October 2026 under Robert Dickinson's direction. Its HydroBot chat uses Claude inside a Claude artifact. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/LA4iK6BCAEUX7BZo52R53v, version 1792893142-e99a (index.html, 246,771 bytes, SHA-256 03a52c5c5b9e93fdd2768f18611d90d5b270054a2d62cb94b08eb83d04db75ab), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM5+ Explorer: the Fortran source, the Lovable sketch, and a proposed C port, checked against upstream

## In three points
- **What:** A single-file rebuild of a Lovable microsite about SWMM5+, the parallel Fortran hydraulics engine from the University of Texas at Austin published through CIMM.org: home, architecture, an engine tour, a hydraulics primer and a chat (HydroBot), with verbatim excerpts cut from the upstream source at commit afd44de. What the rebuild adds is verification: every claim the Lovable copy made is checked against the code.
- **So what:** Of twelve Lovable claims in the defect register, 4 hold, 6 are wrong and 2 are partly right. It said "about 40k lines of modern Fortran" where upstream has 88,020 lines in 72 files; it said the step calls MPI_Bcast and MPI_Allreduce where no .f90 file makes an MPI call (SWMM5+ uses coarrays, with 111 sync all); it described a Roe-style upwind face flux where update.f90 uses timescale interpolation weights.
- **Now what:** Use it to learn how SWMM5+ is built before reading the source. No SWMM5+ simulation was run, the proposed C engine has never compiled (its panes reference functions that are not defined), and the excerpts are one commit of a Beta repository.

This summary was written after the fact. The page ships no technical summary of its own. Its version and dates are the page's own ("v1.0.1 · rebuilt 2026-10-22 ... light-mode contrast patch 2026-10-24"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Home, Architecture, Engine, Hydraulics, HydroBot, About, Doc. Numbers on the Home tab are read from the extraction script's output, not typed. Lovable's hero image and server-side chat gateway were dropped; the HydroBot system prompt was corrected and reused. The register also confirms: two-stage RK2 (crk2 = [0.5d0, 1.0d0]); hydrology through 51 BIND(C) interfaces to libswmm5 loaded with dlopen; BIPquick partitioning (BIPquick.f90, 2,305 lines, one of four partition methods); and corrects file names (runge_kutta2.f90, rk2_lowlevel.f90, partitioning.f90; HDF5 calls in main/output.f90), junction structure (JM main and JB branch elements) and surcharge (a Preissmann slot, Static, Dynamic or SplitDynamic).

## Checks (as stated on the page)

- Upstream cloned at afd44de (mirror CIMM-ORG/SWMM5plus-1); an extraction script cuts and anchors the verbatim excerpts and counts lines, files, coarray syncs and BIND(C) interfaces.
- Each Lovable claim given a verdict against the source (holds, partly, wrong).

## What this does not show

As the page lists it: no SWMM5+ simulation was run, so every number is about the source, not a result; the proposed C engine was never compiled; the excerpts are one commit of a Beta repository.

## Credits and licenses

SWMM5+ by the University of Texas at Austin through CIMM (CIMM-ORG/SWMM5plus, public domain). The excerpts carry the upstream authors' file headers.

## AI use

The page says: built with Claude, Anthropic's AI model (a Claude Code session configured for Claude Fable 5.1), in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable export, asked for it as a single HTML file, and set the standing rules the build follows. Claude read the Lovable source and rewrote every page as vanilla HTML, CSS and JavaScript, ported the Fortran/C tokenizer and section data, cloned upstream, wrote the extraction script, and checked each claim. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.1 (2026-10-24): light-mode contrast patch (the version read).
- 1.0.0 (2026-10-22): single-file rebuild from the Lovable export.

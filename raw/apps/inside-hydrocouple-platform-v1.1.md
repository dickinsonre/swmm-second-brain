---
name: Inside hydrocouple.platform
file: inside-hydrocouple-platform.html
version: "1.1"
date: 2026-10-24
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Qp5VQ635oKEvWpYw63sUuD", repo: "reads the hydrocouple.platform repository at commit 3d7d3a1"}
engines: none (read from source; the platform was not run)
units: none
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Claude Opus 5.5) at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Qp5VQ635oKEvWpYw63sUuD, version 1792870243-3a22 (index.html, 809,256 bytes, SHA-256 735864526e335dcd14f633fb8deab07957a2e24937a59a28cfb027e4a94a0339), its Findings and Doc tabs read in headless Chromium on 2026-11-17 (the page has no About tab). Nothing was run to write this file; the date is the artifact's publish date."
---

# Inside hydrocouple.platform: the HydroCouple run platform read from source, with a register of ten findings

## In three points
- **What:** An explainer of the hydrocouple.platform repository (commit 3d7d3a1) read from source: its architecture, how a run moves through it, its rules, SWMM packaging and AI agents, with a numbered register of ten findings, each with its source lines.
- **So what:** Its JavaScript ports of the platform's rules pass 64 of 64 checks against the platform's own tests, and the first finding is a gap: the packaging scanner does not see the detailed report file a [LID_USAGE] line can name, so that path is left as the author wrote it.
- **Now what:** Use it to understand the platform before running SWMM jobs on it, and pass the findings to its developers. The platform itself was not run (0 of 78 platform tests), so every finding is read from source.

This summary was written after the fact. The page ships no technical summary of its own. Its version and commit are the page's own ("v1.1 · 3d7d3a1"); the date is the artifact's. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Brief, Architecture, Follow a run, Rules, SWMM packaging, AI agents, Findings, Doc. The page reports that the platform keeps customer keys with the customer and serves private and on-premises sites with outbound traffic only, through one code path.

## The findings register (as the page lists it)

Severity is consequence for a SWMM user: 2 Gap, 2 Design note, 3 Info, 3 Limit.
- F1: the packaging scanner does not see the [LID_USAGE] detailed report file (suggested fix: treat field 9 as an output reference and rewrite it to its bare file name).
- F2: the GUI scanner the platform copies has the same omission.
- F3: original file paths reach the control plane under every egress policy.
- F4: HydroCouple's run-1.0 schema cannot catalogue SWMM's .out and .rpt.
- F5: the engine's licence now differs by branch.
- F6: the full plan the README cites is not public.
- F7: any spend cap sends every AI run to a person.
- F8: one adapter, one workflow, one job class.
- F9: no multi-component compositions, no checkpoint resume.
- F10: this app did not run the platform.

## Checks (as stated on the page)

- 64 of 64 checks of the page's JavaScript ports against the platform's tests.
- 0 of 78 platform tests run.
- Related EPA SWMM 5.2.4 and OpenSWMM engine and GUI sources were read to confirm the [LID_USAGE] behaviour (EPA 5.2.4 opens the file and stops with ERROR 305 if it cannot).

## What this does not show

- The platform running: every finding is read from source, none run.
- Anything after commit 3d7d3a1; the page offers a check against the latest commit.

## How to reproduce

Open the page; "Show me" on each finding opens the live demo that reproduces it in the page's ports.

## Credits and licenses

hydrocouple.platform (HydroCouple); EPA SWMM 5.2.4 (public domain); the OpenSWMM engine and GUI sources. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model (Claude Opus 5.5), in October 2026, at the request of Robert (Bob) Dickinson, who chose the subject and supplied the outside review that shaped v1.1. Claude read the repository and the related EPA SWMM 5.2.4, OpenSWMM engine and GUI sources, and wrote the JavaScript ports of the platform's rules, the failure lab, the page and the essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1: shaped by an outside review.
- 1.0: first version.

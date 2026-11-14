---
title: "S26: CLAUDE.md of the old swmm-brain repository (four working principles for apps)"
type: source
raw: raw/swmm-brain/CLAUDE-swmm-brain.md
kind: note
author: Robert Dickinson
published: 2026-08-22
ingested: 2026-11-14
tags: [apps, method]
reviewed: no
---
**What it is.** The instruction file of the old repository: four working principles for building single-file browser apps for SWMM5 and EPANET hydraulics. Raw file: [raw/swmm-brain/CLAUDE-swmm-brain.md](../../raw/swmm-brain/CLAUDE-swmm-brain.md). It was named `CLAUDE.md` in the old repository and is stored here under another name so that an agent working in this repository does not load it as instructions. It is a source, not a rule of this wiki.

**How it was written.** Not stated. It defers to Bob's swmm-vibe-coding-apps skill for the full build contract.

**Claims worth keeping**
- Audience: water engineers and students "who learn a concept faster from a slider than from 50 pages of docs".
- Principle 1: state the modeling assumptions (units, equation form, boundary conditions, defaults) before writing code; ask when a request has more than one reasonable reading.
- Principle 2: write the minimum above a fixed floor. The floor ships on every app: a "How to Use" welcome modal, a step-by-step tour or per-tab intro banners, a "Make a GIF" button, CSV export for tables, and `.inp` export where a model is generated.
- Principle 3: on iteration, patch the named section only; never regenerate the whole file.
- Principle 4: done means the displayed equation matches the computation exactly, presets give expected values in a quick Node test before the interface is wired (it calls this the FableMeter pattern), no console errors, responsive at 375 px, and chart axes labeled with units.

**Feeds:** [App build contract (four working principles)](../concepts/app-build-contract.md), [swmm-brain (the old brain repository)](../entities/swmm-brain-repo.md).

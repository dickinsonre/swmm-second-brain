---
title: "S268: Inside the Network, app .md (v1.1.1)"
type: source
raw: raw/apps/inside-the-network-cfd-v1.1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-18
tags: [apps, cfd, hydraulics, swmm5, extran, wasm, verification]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app Inside the Network, version 1.1.1: a particle CFD solver that knows only walls, gravity and a friction rule, run beside EPA SWMM 5.2.4 along whole paths of four EXTRAN example networks compressed 50 to 1. This version changes the documentation only. Raw file: [raw/apps/inside-the-network-cfd-v1.1.1.md](../../raw/apps/inside-the-network-cfd-v1.1.1.md).

**How it was written.** The app ships this file. Its AI-use line reads "built with Claude (Anthropic)"; the 1.1.0 file it follows is ingested as [S76](S76-inside-the-network-cfd-app-md.md).

**Claims worth keeping** (all copied from the file)
- At steady flow the CFD solver and EPA SWMM 5.2.4 put the water within a foot of each other at every node on six of the seven paths and flood the same manhole; they differ mainly in how fast the sewer fills.
- 1.1.1 (2026-11-12) is documentation only: the Doc tab and the .docx gain one-sentence, one-paragraph and one-page summaries and five questions with answers at the end. No change to the solver, the engine or any number.
- The engine is EPA SWMM 5.2.4 from tag v5.2.4 plus the Dickinson KW/SF patch with the extension off (modes 0/0), a wasm32-wasi reactor of 853,130 bytes.

**Limits it states.** The same as 1.1.0, which the file repeats unchanged; see [S76](S76-inside-the-network-cfd-app-md.md).

**Checked at ingest.** A line-by-line diff against the 1.1.0 file finds only the version line, the In three points block, the one-sentence summary and the 1.1.1 change note added. The `links:` line gives Netlify as "not deployed yet".

**Feeds:** [Inside the Network (app)](../entities/inside-the-network-cfd.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Inside the Network (app)](../entities/inside-the-network-cfd.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

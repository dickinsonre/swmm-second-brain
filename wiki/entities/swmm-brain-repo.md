---
title: swmm-brain (the old brain repository)
type: entity
updated: 2026-11-14
sources: [S08, S55, S56, S57, S58]
tags: [repositories, method]
reviewed: 2026-11-15
---
`dickinsonre/swmm-brain`, Bob's earlier attempt at a knowledge repository, last committed on 22 August 2026 (commit 70348bb) [S55](../sources/S55-swmm-brain-readme.md). Its contents were copied into `raw/swmm-brain/` on 14 November 2026, when this repository replaced it (see the [log](../../log.md)).

**What it held: six files**

| File | What it is | Source page |
|---|---|---|
| `README.md` | Enhancements, apps, scripts and a career timeline | [S55](../sources/S55-swmm-brain-readme.md) |
| `CLAUDE.md` | Four working principles for building apps | [S58](../sources/S58-swmm-brain-working-principles.md) |
| `setup.sh` | Clones a list of knowledge repositories side by side | [S57](../sources/S57-swmm-brain-setup-script.md) |
| `notes/synthetic-storm-surrogate.md` | The one note | [S56](../sources/S56-swmm-brain-note-surrogate.md) |
| `notes/_TEMPLATE.md` | The note template; now at `raw/notes/_TEMPLATE.md` | |
| `.gitignore` | Kept every top-level folder but `notes/` out of the repository; stored here as `_gitignore.txt` | [S57](../sources/S57-swmm-brain-setup-script.md) |

**How it was meant to work.** `setup.sh` clones six or more repositories next to each other. Run `setup.sh`, then start Claude from that folder ("Start the brain: claude") [S57](../sources/S57-swmm-brain-setup-script.md). Bob's own thinking went into `notes/`, one idea per file, each marked seed, working or solid ([the template](../../raw/notes/_TEMPLATE.md)).

**What the README promised and the repository did not hold.** A tree of `enhancements/`, `apps/`, `scripts/` and `docs/` under the name `swmm5-dickinson/` [S55](../sources/S55-swmm-brain-readme.md). The swmm5.org topic page describes the repository the same way, as "engine changes, a WebAssembly build, and Ruby and PySWMM scripts" [S08](../sources/S08-swmm5org-topic-inside-swmm5.md). None of that is among the six files.

**How this repository differs.** The old design put whole repositories beside an agent. This one compiles each source once into linked pages with citations, and keeps a list of what disagrees.

**What carried over**
- The note template, for Bob's own ideas: `raw/notes/_TEMPLATE.md`.
- The list of repositories, as the map of where more sources are: [Bob's GitHub repositories (where the rest of the material lives)](bobs-github-repositories.md).
- The four principles: [App build contract (four working principles)](../concepts/app-build-contract.md).
- The ideas: [Two-layer soil infiltration (SOIL2)](../concepts/two-layer-infiltration.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md).

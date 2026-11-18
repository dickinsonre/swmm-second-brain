---
title: "S340: Vacuum Sewer Toolkit, summary written from the page (v1.0)"
type: source
raw: raw/apps/vacuum-sewer-toolkit-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, vacuum-sewers, epa-1991, icm, ruby]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Vacuum Sewer Toolkit, version 1.0: EPA 1991 vacuum sewer design and InfoWorks ICM Ruby, corrected. Raw file: [raw/apps/vacuum-sewer-toolkit-v1.0.md](../../raw/apps/vacuum-sewer-toolkit-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/JHc3kwDu7L4ny8PtxrPutt, version 1792957476-aa88 (index.html, 1,607,607 bytes, SHA-256 377b103539090e0c575eed7be4e94ae24206bfc979db8b9716d4868288f8f866), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who wrote the original app, supplied its source and is responsible for the work."

**Claims worth keeping** (all copied from the file)
- A single-file rebuild of Bob's Lovable app vcruby (126 files, 27 feature screens, 19,586 lines of TypeScript and 508 of Ruby by its own count): vacuum sewer design after the EPA 1991 manual and published state criteria, calculators, diagrams, components, comparisons with gravity, costs, and InfoWorks ICM Ruby scripts. The three ICM scripts are replaced by four corrected ones.
- The corrections register lists 35 entries (code 9, method 2, contradiction 4, number 6, practice 1, table 1, removed 5, physics 3, label 3, unsupported 1). The worst (C1): for a 320 m to 330 m guide the original sawtooth generator made inverts of 320, 319, 332, 329 and 330, one 13 m lift and 14 m of rise from a single pipe, three times the whole 13 ft (3.96 m) static budget. The engine passes 86 of 86 checks, the corrected Ruby 15 of 15 in a stand-in ICM, and both exported .inp files run clean in SWMM 5.2.
- Engine vac.js: 86 of 86 checks pass.
- Corrected ICM Ruby: 15 of 15 in a stand-in ICM harness; the original scripts were also run in that harness.
- SWMM 5.2 (pyswmm 2.2.0, toolkit 0.17.0) ran both exported .inp files with no errors or warnings; continuity error 1.60% (demo) and 0.15% (sawtooth).
- Published criteria looked up: WEF (via PDHengineer), Florida DEP, Texas 217.98, EPA 1991; the Innovyze examples.

**Limits it states.** As the page lists it: friction is single-phase; the two-phase correction uses a correlation built for steady separated flow in straight pipe, while a vacuum main runs in slugs and the multiplier depends heavily on the air assumed; no script has run inside ICM; costs are 1990 unit costs times an inflation factor. The demo network is synthetic.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Vacuum Sewer Toolkit (app)](../entities/vacuum-sewer-toolkit.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [Sewer Science (app)](../entities/sewer-science.md), [InfoWorks ICM](../entities/infoworks-icm.md).

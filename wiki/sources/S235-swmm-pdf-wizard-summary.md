---
title: "S235: SWMM PDF Wizard, summary written from the page (v1.1.0)"
type: source
raw: raw/apps/swmm-pdf-wizard-v1.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-19
ingested: 2026-11-17
tags: [apps, swmm5, swmm6, reports, pdf, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM PDF Wizard, version 1.1.0: a wizard that turns a SWMM model set (.inp, .rpt, .out from EPA SWMM 5 or OpenSWMM 6, plus figures and PDFs handed over by other apps) into a sendable PDF report, laid out in the page and finished by pdfcraft-cli 0.8.0 (ArtCraft's Rust PDF workbench) compiled to WebAssembly. It does not run SWMM. Raw file: [raw/apps/swmm-pdf-wizard-v1.1.0.md](../../raw/apps/swmm-pdf-wizard-v1.1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792368828-7e33, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in Claude Code sessions in October 2026 under Bob's direction; Bob asked for it and chose pdfcraft as the PDF engine. Claude compiled the Rust standard library and wasi-libc from source so pdfcraft-cli could be built to WebAssembly unchanged, and wrote the readers, the report builder, the bridge and the page.

**Claims worth keeping** (all copied from the file)
- The report carries a cover, linked contents, model and run summaries with continuity and warnings, hydrographs from the binary output, every engine table set in type, the full .rpt as an appendix and a Use of AI page.
- The binary .out carries its version number, 52004 for SWMM 5.2.4 and 60000 for this OpenSWMM 6; when the .rpt and .out disagree the wizard says so.
- The readers were checked against the engines on the Node Depth Summary's Maximum Depth and Reported Max Depth columns; run wrongly on purpose (water-surface elevation for depth), the check failed by 4,973 ft, the invert's elevation above datum.
- Other apps open it through swmm-pdf-bridge.js, which flattens charts to JPEG and posts one message to the wizard in a new tab; the bridge expects the address swmm-pdf-wizard.netlify.app.
- pdfcraft-cli is commit 9e5b70d of 16 October 2026, MIT OR Apache-2.0; the WebAssembly file is 7,015,516 bytes.

**Limits it states.** It reports on engine files and does not run SWMM. Plotted series are report-step values.

**Checked at ingest.** The bridge's expected address is the one Netlify reported deployed on 17 November 2026 [S205](S205-note-netlify-addresses.md). The `links:` line gives Netlify as "not yet deployed; its bridge script expects https://swmm-pdf-wizard.netlify.app/"; Netlify reported a finished deploy at https://swmm-pdf-wizard.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM PDF Wizard (app)](../entities/swmm-pdf-wizard.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [SWMM Results Kit](../entities/swmm-results-kit.md).

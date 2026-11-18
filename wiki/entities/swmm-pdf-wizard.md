---
title: "SWMM PDF Wizard (app)"
type: entity
updated: 2026-11-17
sources: [S205, S235]
tags: [apps, swmm5, swmm6, reports, pdf, wasm]
reviewed: no
---
Bob's app SWMM PDF Wizard: a wizard that turns a SWMM model set (.inp, .rpt, .out from EPA SWMM 5 or OpenSWMM 6, plus figures and PDFs handed over by other apps) into a sendable PDF report, laid out in the page and finished by pdfcraft-cli 0.8.0 (ArtCraft's Rust PDF workbench) compiled to WebAssembly. It does not run SWMM. Version 1.1.0, 2026-10-19 [S235](../sources/S235-swmm-pdf-wizard-summary.md). Netlify address: https://swmm-pdf-wizard.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S235](../sources/S235-swmm-pdf-wizard-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S235](../sources/S235-swmm-pdf-wizard-summary.md)
- The report carries a cover, linked contents, model and run summaries with continuity and warnings, hydrographs from the binary output, every engine table set in type, the full .rpt as an appendix and a Use of AI page.
- The binary .out carries its version number, 52004 for SWMM 5.2.4 and 60000 for this OpenSWMM 6; when the .rpt and .out disagree the wizard says so.
- The readers were checked against the engines on the Node Depth Summary's Maximum Depth and Reported Max Depth columns; run wrongly on purpose (water-surface elevation for depth), the check failed by 4,973 ft, the invert's elevation above datum.
- Other apps open it through swmm-pdf-bridge.js, which flattens charts to JPEG and posts one message to the wizard in a new tab; the bridge expects the address swmm-pdf-wizard.netlify.app.
- pdfcraft-cli is commit 9e5b70d of 16 October 2026, MIT OR Apache-2.0; the WebAssembly file is 7,015,516 bytes.

**What it does not show.** It reports on engine files and does not run SWMM. Plotted series are report-step values. [S235](../sources/S235-swmm-pdf-wizard-summary.md)

**Noted at ingest.** The bridge's expected address is the one Netlify reported deployed on 17 November 2026 [S205](../sources/S205-note-netlify-addresses.md).

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [SWMM Results Kit](swmm-results-kit.md).

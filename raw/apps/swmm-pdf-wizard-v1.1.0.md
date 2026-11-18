---
name: SWMM PDF Wizard
file: swmm-pdf-wizard.html
version: 1.1.0
date: 2026-10-19
written: 2026-11-17
author: Robert Dickinson
links: {netlify: "not yet deployed; its bridge script expects https://swmm-pdf-wizard.netlify.app/", artifact: "https://claude.ai/artifact/8uSbj3zArACYRCVyDfCc4b", repo: none named in the page}
engines:
  - {name: pdfcraft-cli, version: 0.8.0, source: "ArtCraft's Rust PDF workbench, commit 9e5b70d (2026-10-16), built unchanged for wasm32-wasip1", license: "MIT OR Apache-2.0"}
files: ["index.html", "pdfcraft-cli-gz.wasm (7,015,516 bytes)", "swmm-io.js", "swmm-pdf-bridge.js", "samples/swmm5.json", "samples/swmm6.json"]
units: as the model files carry them
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/8uSbj3zArACYRCVyDfCc4b, version 1792368828-7e33 (index.html, 276,081 bytes, SHA-256 441625dcd2b00ab0afb346ba77ac795a01f7c883c8d3ef96d029ba9d199e7619, plus five supporting files), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file; the date is the artifact's publish date."
---

# SWMM PDF Wizard: SWMM5 and SWMM6 model sets to finished PDF reports, finished by pdfcraft in the browser

## In three points
- **What:** Turns a SWMM model set (.inp, .rpt, .out from EPA SWMM 5 or OpenSWMM 6, plus figures and PDFs handed over by other apps) into a sendable PDF report, laid out in the page and finished by pdfcraft-cli compiled to WebAssembly.
- **So what:** The report carries a cover, linked contents, model and run summaries with continuity and warnings, hydrographs from the binary output, every engine table set in type, the full .rpt as an appendix and a Use of AI page; it warns when the .rpt and .out carry different version numbers (52004 or 60000).
- **Now what:** Deploy it with its five supporting files (the bridge script expects swmm-pdf-wizard.netlify.app) and let other apps send it their model sets. It reports on engine files and does not run SWMM; plotted series are report-step values.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.1.0"); the date is the artifact's. Every number below is copied from the page or its files. Nothing was run to write this file.

## What it does

Steps: 1 Model set, 2 Contents, 3 Finish (pdfcraft), 4 Build & download, About, Doc. The wizard writes a script of pdfcraft tool calls (combine, bookmark_add, page_number, doc_header_footer, doc_watermark, doc_set_info, doc_initial_view, doc_protect, doc_save and others) and runs it once in a Web Worker. Other apps open it with swmm-pdf-bridge.js (SwmmPdfBridge.open or a ready-made button), which flattens charts to JPEG and posts one message to the wizard in a new tab.

## Checks (as stated on the page)

- The binary .out carries its version number (52004 for SWMM 5.2.4, 60000 for this OpenSWMM 6); if the report and the binary disagree, the wizard says so.
- The readers were checked against the engines using the Node Depth Summary's "Maximum Depth" and "Reported Max Depth" columns; run wrongly on purpose (water-surface elevation for depth), the check failed by 4,973 ft, the invert's elevation above datum.
- pdfcraft reopens what it has written to confirm it.

## What this does not show

- It reports on engine files; it does not run SWMM.
- Plotted series are reporting-step values.

## How to reproduce

Deploy the folder with all six files. Open the page, load a model set or a sample (samples/swmm5.json, samples/swmm6.json), choose contents and finish, then build and download.

## Credits and licenses

pdfcraft (ArtCraft), MIT OR Apache-2.0, commit 9e5b70d. EPA SWMM 5 (public domain); OpenSWMM 6 (HydroCouple), Apache-2.0. No license is stated for the page itself.

## AI use

The page says it was built with Claude, Anthropic's AI model, in Claude Code sessions in October 2026, under the direction of Robert (Bob) Dickinson, who asked for it and chose pdfcraft as the PDF engine. Claude compiled the Rust standard library and wasi-libc from source so pdfcraft-cli could be built to WebAssembly, built pdfcraft-cli 0.8.0 unchanged, wrote the in-browser runner and a fix-up for the WASI shim, and wrote the readers, the report builder, the bridge, the page and the essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1.0: the version read.

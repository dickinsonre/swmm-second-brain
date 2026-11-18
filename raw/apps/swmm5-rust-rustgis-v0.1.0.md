---
name: swmm5-rust in RustGIS
file: swmm5-rust-rustgis.html
version: 0.1.0
date: 2026-11-01
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/S1kZpDWkw6aMDmFBpqM5DW", repo: "https://github.com/SWMMBobSWMM6/swmm5-rust"}
engines:
  - {name: swmm5-rust, version: "plugin 0.1.0, ABI 1", source: "EPA SWMM 5.2.4 translated into safe Rust (63 files, about 56,000 lines), packaged as swmm5-rust-0.1.0.rgplugin with a memfs feature", license: MIT}
  - {name: EPA SWMM, version: 5.2.4, role: "reference WebAssembly build for identity and for the page's time series", license: public domain}
units: US customary as the models carry them
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Claude Opus 5.5) for Robert Dickinson. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/S1kZpDWkw6aMDmFBpqM5DW, version 1793581554-353e (index.html, 5,567,324 bytes, SHA-256 a781b8cbc76c10b7e43442ee06dd0a8dabae9e905d84010155c485ab10f719d1), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# swmm5-rust in RustGIS: EPA SWMM 5.2.4 in safe Rust, running as a sandboxed RustGIS plugin

## In three points
- **What:** Runs swmm5-rust, EPA SWMM 5.2.4 translated into safe Rust, as the RustGIS plugin it was built to be: the page plays RustGIS's side of plugin ABI 1 around the WebAssembly module from swmm5-rust-0.1.0.rgplugin.
- **So what:** RustGIS plugins get no files at all, so a 322-line memfs module turns the engine's file calls into a name-to-bytes table; of 177 gate models the plugin ran, 177 match EPA's WebAssembly build byte for byte.
- **Now what:** Use it to see SWMM run inside a GIS that grants nothing, and as the path to a RustGIS SWMM tool. Identity is against EPA's WebAssembly build, and the plugin returns summary results only.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the plugin's ("plugin 0.1.0 · ABI 1"); the date is the end of the build session (31 October to 1 November 2026). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

RustGIS is the open-source GIS by Qiusheng Wu and opengeos; a plugin is a WebAssembly module run in the wasmi interpreter with no files. EPA's C SWMM calls fopen first and dies in that box. swmm5-rust holds a simulation as one Project value and has its own small C library (cio) with its own FILE; the memfs feature makes cio::CFile a cursor into a byte vector keyed by file name. The memfs module is 322 lines including its tests and is off in the default build. Tabs: Map, Plugin, Verify, About, Doc.

## Checks (as stated on the page)

- swmm5-rust's own gate: on 221 smoke and coverage models, 215 give files identical to EPA; the other six are decks where EPA itself reads memory it does not own.
- The default build without memfs was checked unchanged: unpatched and patched runswmm-rs binaries on the same 221 models (220 of 221 matched in the text read).
- Census through the plugin: of 177 models the plugin ran, 177 match EPA's WebAssembly build byte for byte (.out, and .rpt without its clock lines); 37 more are input-error decks where both engines stop with the same error.
- Planted errors caught 30 of 30; a "maximum depth replaced by average depth" error caught on 5 of 5 models.
- A second Claude agent reviewed the code and claims; its 17 findings were fixed.

## What this does not show

- Identity is against EPA's WebAssembly build.
- RustGIS meters runs with fuel.
- The plugin returns summary results; the page's time series are read from EPA's run of the same inputs.

## How to reproduce

Open the page and run a model through the Plugin tab; Verify shows the checks. Source: github.com/SWMMBobSWMM6/swmm5-rust.

## Credits and licenses

EPA SWMM 5.2.4: US EPA, public domain; Lewis Rossman's engine design. swmm5-rust: MIT. RustGIS 0.5.0 and its plugin SDK (opengeos/rustgis-plugins): Apache-2.0 and MIT; packaging script from opengeos/rustgis-plugin-template (MIT). wasi-libc: MIT and Apache-2.0 terms of its components.

## AI use

The page says it was built with Claude (Anthropic, Claude Opus 5.5) in one session on 31 October and 1 November 2026 for Robert (Bob) Dickinson, SWMM Enablement. Claude wrote the memfs engine feature, the plugin crate, the packaging, the census and RustGIS test harnesses, the fuel meter, the page and the Doc essay, and ran every check; a second Claude agent reviewed the code and claims, and an outside AI review Bob passed along was also answered. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 0.1.0: first plugin version.

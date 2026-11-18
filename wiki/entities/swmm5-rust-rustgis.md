---
title: "swmm5-rust in RustGIS (app)"
type: entity
updated: 2026-11-17
sources: [S41, S205, S221]
tags: [apps, swmm5, rust, gis, plugins, wasm]
reviewed: no
---
Bob's app swmm5-rust in RustGIS: swmm5-rust, EPA SWMM 5.2.4 translated into safe Rust (63 files, about 56,000 lines), run as the RustGIS plugin it was built to be: the page plays RustGIS's side of plugin ABI 1 around the WebAssembly module from swmm5-rust-0.1.0.rgplugin. RustGIS is the open-source GIS by Qiusheng Wu and opengeos. Version 0.1.0, 2026-11-01 [S221](../sources/S221-swmm5-rust-rustgis-summary.md). Netlify address: https://swmm5-rust-rustgis.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S221](../sources/S221-swmm5-rust-rustgis-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S221](../sources/S221-swmm5-rust-rustgis-summary.md)
- RustGIS plugins run in the wasmi interpreter with no files. EPA's C SWMM calls fopen first and dies there; a 322-line memfs module, off in the default build, turns swmm5-rust's file calls into a name-to-bytes table.
- Census through the plugin: of 177 models the plugin ran, 177 match EPA's WebAssembly build byte for byte (.out, and .rpt without its clock lines); 37 more are input-error decks where both engines stop with the same error.
- swmm5-rust's own gate: on 221 smoke and coverage models, 215 give files identical to EPA; the other six are decks where EPA itself reads memory it does not own.
- Planted errors were caught 30 of 30; a "maximum depth replaced by average depth" error was caught on 5 of 5 models.
- A second Claude agent reviewed the code and claims; its 17 findings were fixed.
- The plugin returns summary results only; the page's time series are read from EPA's run of the same inputs. RustGIS meters runs with fuel.

**What it does not show.** Identity is against EPA's WebAssembly build. The plugin returns summary results only. [S221](../sources/S221-swmm5-rust-rustgis-summary.md)

**Noted at ingest.** The summary reports the default build checked unchanged on the same 221 models with "220 of 221 matched in the text read", which leaves one model unexplained. Other sources give swmm5-rust 480 of 480 on the port gate [S41](../sources/S41-swmm5-go-readme.md); that is a different model set from the 221 here. Repository: SWMMBobSWMM6/swmm5-rust, MIT.

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [SWMM5 language translations (swmm5-*)](swmm5-language-ports.md), [Wrap, translate or extend](../concepts/wrap-translate-or-extend.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

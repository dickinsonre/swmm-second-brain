---
title: "Conformal SWMM (app)"
type: entity
updated: 2026-11-17
sources: [S205, S224]
tags: [apps, swmm5, swmm6, generators, wasm, openswmm]
reviewed: no
---
Bob's app Conformal SWMM: a generator that bends one square street grid through five complex functions (z, z squared, e to the z, a rational function with two poles, z cubed), writes each as a SWMM5 model and runs it on the OpenSWMM legacy engine 5.3.0-beta.3 compiled to WebAssembly in the page. Version 1.0.0, 2026-11-14 [S224](../sources/S224-conformal-swmm-app-md.md). Netlify address: https://conformal-swmm.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**Its source.** [S224](../sources/S224-conformal-swmm-app-md.md) is the technical summary the app ships with. Bob has not read this page.

**What the summary says** [S224](../sources/S224-conformal-swmm-app-md.md)
- Engine: HydroCouple/openswmm.engine, branch swmm6_rel, commit 283da75e21a8258af7b82b5222267b5f60057a81, src/legacy/engine, reporting "5.3.0 (Build 5.3.0)", API 53000; Apache-2.0 over public-domain EPA SWMM. EPA SWMM 5.2.4 is used for comparison only.
- Engine identity, WebAssembly against a native gcc 13.3 build of the same source: 16 of 16 .out files byte-identical (15 of 2,520,974 bytes, one of 9,428,456 bytes).
- Shared square, 82 nodes, 145 conduits, 64 subcatchments, 22.96 ac, pipes sized per network: peaks 21.75 (z), 21.88 (z squared), 21.73 (e to the z), 21.20 (rational) and 21.84 cfs (z cubed).
- EPA SWMM 5.2.4 on the same 16 .inp files: 0 errors, 0 warnings, peak in the same minute in 16 of 16, largest peak difference 0.013 cfs.
- A model is exported only if six audits pass, including a sibling test on 41 x 41 points and a winding test by the argument principle. A square centred on 0 under z squared folds 100 % with 0 boundary crossings: crossing and area-closure checks alone do not detect an exact double cover.
- No junction flooded in any of the 16 runs; runoff continuity -0.007 to -0.010 %; rain 2.00 in, runoff 1.10 to 1.15 in.

**What it does not show.** Formula networks, not real catchments, and not for design. One shared square, one storm, N = 8. The engine is a pre-release 5.3.0-beta.3, checked against EPA 5.2.4 on 16 files only. The .out reader is a local copy, not the shared results library. Not tested in Firefox, Safari or on phones. No person has reviewed the code, the numbers or the text. [S224](../sources/S224-conformal-swmm-app-md.md)

**Noted at ingest.** The five per-network peaks lie between 21.20 and 21.88 cfs, a spread of 3.2 % of the larger. The engine is the same OpenSWMM legacy 5.3 line listed with two claims on [SWMM Claim Frontier (app)](swmm-claim-frontier.md); credits and NOTICE follow the Apache-2.0 terms the file names.

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Planar graphs and Euler's formula](../concepts/planar-graphs.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).

---
title: "FV Link Lab (app)"
type: entity
updated: 2026-11-19
sources: [S377]
tags: [apps, swmm5, finite-volume, dynamic-wave, verification]
reviewed: no
---
Bob's app FV Link Lab runs stock EPA SWMM 5.2.4 and [swmm524-fvlink](swmm524-fvlink.md) side by side in the browser, both compiled to WebAssembly. The user picks a sample or loads an .inp, clicks conduits to make them finite volume (FV), runs both engines and compares hydrographs, peaks, step counts and wall time, or runs a byte-for-byte null check. Version 1.1.0, 2026-11-18 [S377](../sources/S377-fv-link-lab-app-md.md). Tabs: Run, Evidence, Defects, Mars, About and Doc; the Doc essay is *One Pipe, Its Own Clock*, 11 sections and 21 figures, also shipped as a .docx [S377](../sources/S377-fv-link-lab-app-md.md). Artifact https://claude.ai/artifact/VoY6Vve25S2JznvXz7YQk2; Netlify: none yet [S377](../sources/S377-fv-link-lab-app-md.md).

**What it checks** [S377](../sources/S377-fv-link-lab-app-md.md)
- In the page, 9 samples run through its own engines and native give 18 `.out` files byte-identical.
- WebAssembly against native over 73 EPA models: 65 identical, 1 `.rpt` with round-off only, 6 `.out` that differ (largest 0.83 %, user5, following the math library) and 1 with the same error. The null effect holds exactly inside WebAssembly on all 73.

**The Mars tab** (1.1.0). It runs the Thoth canal of [Thaw on the Thoth](thaw-on-the-thoth.md) on Earth-gravity engines by Froude scaling, with k = sqrt(32.2 / 12.2) = 1.624606, in three models (nospill, plan and lock), stock and FV, and offers an InfoWorks ICM kit as a download [S377](../sources/S377-fv-link-lab-app-md.md). Nothing has been run in ICM, and the kit's ICM field names, shape codes and link types are unverified [S377](../sources/S377-fv-link-lab-app-md.md).

**What it does not show** [S377](../sources/S377-fv-link-lab-app-md.md): no field data; no comparison with OpenSWMM's FV engine; no person has reviewed `fvlink.c` line by line or run the branch on a project model. Open defect FVL-15 is shown in the Defects tab.

See [swmm524-fvlink](swmm524-fvlink.md), [The byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [EPA SWMM 5](swmm-5.md).

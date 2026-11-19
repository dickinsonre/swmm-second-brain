---
title: "S81: Bellinge, summary written from the page (v2.0)"
type: source
raw: raw/apps/bellinge-v2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-18
ingested: 2026-11-15
superseded_by: S389
tags: [apps, swmm5, swmm6, swmm4, extran, engine-comparison, bellinge, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-15
---
**What it is.** A technical summary of the app Bellinge, version 2.0 (18 October 2026): the open Bellinge combined sewer model of Odense, Denmark, run through seven SWMM engines in the browser. Raw file: [raw/apps/bellinge-v2.0.md](../../raw/apps/bellinge-v2.0.md).

**How it was written. This one is different.** The page carries no summary of its own. Claude (Anthropic, model claude-fable-5-2) wrote the file on 14 November 2026, at Bob's request, from the page's source, its build record and its Doc essay, "Seven Engines and a Danish Sewer". Nothing was rerun. Bob has not read it (Q52). The app was built with Claude in Claude Code sessions on 17 and 18 October 2026 under Bob's direction.

**Claims worth keeping** (all copied from the page)
- The model: `BellingeSWMM_v021_nopervious.inp`, 1,020 nodes, 1,044 links, 713 subcatchments. Rain: gauges rg5425 and rg5427, 749,401 wet minutes, June 2009 to August 2021. From Nedergaard Pedersen and others (2021), Earth System Science Data 13, 4779-4798, CC BY 4.0.
- Seven engines: EPA SWMM 5.2.4; OpenSWMM 6 at tags alpha.1, alpha.2, alpha.3 and at swmm6_rel commit 3c30f1e6c2 (17 October 2026); SWMM 4.4H; EXTRAN III (April 1981), as printed and with its bugs fixed.
- EXTRAN III refuses the whole model (limits: 187 junctions and links). The branch above outfall G60K220, 159 nodes and 167 links, fits.
- The 29 June 2012 storm on that branch: EPA SWMM 5.2.4 floods 127 nodes with routing continuity -0.61 %; OpenSWMM swmm6_rel, SWMM 6 dynamic wave, floods 18 with 0.14 %; both peak at 42.6 cfs. SWMM 4.4H: 111 nodes, -9.2 %, 36.5 cfs. EXTRAN III bugs fixed: 130 nodes, -3.3 %, 40.0 cfs.
- EXTRAN III as printed diverges on the branch; the essay traces it to the hydraulic-radius routine that never lets a closed rectangle run full.
- The 48-hour base run on the whole model: EPA 5.2.4 floods 466 nodes in 2.5 min of wall time; the three later OpenSWMM dynamic wave runs flood 62, 62 and 61; the finite-volume solver floods 520 and takes 99 min.
- OpenSWMM alpha.1 shows a runoff continuity error of -43.9 % on this model; the July tag (alpha.2) does not.
- From alpha.2 to swmm6_rel the dynamic wave routing continuity goes 2.79 %, 1.64 %, 0.09 %.
- EPA Example 1, peak at the outfall: 71.18 cfs in EPA 5.2.4, 71.71 in SWMM 4.4H, 71.70 in EXTRAN III bugs fixed, 74.5 in OpenSWMM alpha.1, 69.2 in the finite-volume solver.
- Tests in the build record: 19 + 12 + 20 checks.

**Limits it states.** "Agreement between engines is not correctness." No field observations are in the page, though the dataset holds thirteen level meters and a flow meter. The two Fortran engines run a converted deck. OpenSWMM 6 is alpha. No person has compared the runs with a desktop SWMM run node by node.

**Checked at ingest.** The essay's byline reads "Robert Dickinson, with Claude"; its section 9 cites Table 3 for numbers in its Table 4; its test table is dated 19 October against a build record of 18 October (Q53). The essay's "factor of seven" between EPA's 466 flooding nodes and the dynamic wave's "about sixty" is 7.5 to 7.6 by division (ours).

**Feeds:** [Bellinge (app)](../entities/bellinge-app.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [EXTRAN](../entities/extran.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).

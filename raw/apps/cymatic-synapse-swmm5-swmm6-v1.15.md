---
name: Cymatic Synapse Generator
file: cymatic-synapse-swmm5-swmm6.html
version: "1.15"
date: 2026-10-31
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://cymatic-synapse-swmm5-swmm6.netlify.app", artifact: "https://claude.ai/artifact/MSrYvnKsoEQoDaAqRjeMty", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "WebAssembly build from Bob's Seven SWMM Engines app, reused byte for byte; swmm-toolkit 0.17.0 (native 5.2.4) used while building"}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: "3c30f1e6 (2026-10-17)", license: Apache-2.0, note: "the engine's own Emscripten build from the same app, 5,242,647 bytes; DW and FV"}
units: US customary (cfs, ft, ac, in, MG)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Opus 5.5) in October 2026 at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/MSrYvnKsoEQoDaAqRjeMty, version 1793462693-fa99 (index.html, 7,407,120 bytes, SHA-256 5ac1f1ea49b65c4eedcde3775f4f030d529049eaee933850069fa1114289894b), every tab read in headless Chromium on 2026-11-18. The date above is the artifact's last publish. Nothing was run to write this file."
---

# Cymatic Synapse Generator: a SWMM5 model generated from a picture, run in EPA SWMM 5.2.4 and OpenSWMM 6

## In three points
- **What:** A generator that turns a Grok Imagine render ("cymatic hyperslice ... nodal junctions as attenuated quantum field synapses") into an EPA SWMM 5.2.4 input file: the braided band becomes a twin-rail trunk, the ringed nodes become storage hubs with throttled outlets, the rings become 2 ft ground contours and the faint polygons become Voronoi subcatchments. The network then runs in the browser in EPA 5.2.4 and OpenSWMM 6 DW and FV.
- **So what:** Every one of 28 native 5.2.4 runs over 23 models finished with 0 errors and 0 warnings; on the default network the storage hubs cut the outfall peak from 812.1 cfs (redesigned without storage) to 717.1 cfs, and the 3 in storm on 521.19 ac closes at 130.29 ac-ft. The picture is drawn from engine output (d/D, surcharge, freeboard, flooding) once a run is in.
- **Now what:** Use it as a generator of varied test networks and to show what storage does, with Freeze geometry on to keep the pipes fixed while the storm or the basins change. The default design carries the 3 in storm; it is not a design guarantee.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.15"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Generator, Model, Checks, About, Doc. Ten presets (seeds 7, 11, 42, 3, 5, 9, 21, with throttle, storage and storm variants). The trunk is laid out from the outfall upstream (the "inverse surveyor path"); laterals keep their curves through [VERTICES]; Voronoi cells clipped to the field boundary mean every square foot drains to one node and no polygons overlap. After a run the page reads the binary .out: pipe brightness follows d/D, amber marks a full pipe or a surcharged node, a red outline marks less than 1 ft of freeboard, a red dot flooding.

## Results the page reports (native EPA 5.2.4, swmm-toolkit 0.17.0)

| Preset | Nodes | Conduits | OF1 peak, cfs | OF1 volume, MG | Flooding, ac-ft | Routing cont., % |
|---|---|---|---|---|---|---|
| Seed 7, default | 110 | 131 | 717.1 | 31.08 | 0.000 | -0.037 |
| Seed 7, 30% throttle | 110 | 131 | 641.5 | 31.08 | 0.035 | -0.080 |
| Seed 7, basins removed, pipes kept | 110 | 131 | 798.6 | 31.09 | 0.025 | -0.016 |
| Seed 7, redesigned without storage | 110 | 131 | 812.1 | 31.09 | 0.000 | 0.001 |
| Seed 5, 14 synapses, 6,000 ft trunk | 182 | 211 | 1045.4 | 45.00 | 0.000 | -0.047 |
| Seed 9, 5 in storm, 3 in basins | 108 | 129 | 1069.4 | 52.93 | 15.031 | -0.102 |
| Seed 21, small field | 41 | 50 | 230.3 | 10.44 | 0.000 | -0.051 |

Runoff continuity was -0.003% to -0.004% in every run; flow-routing continuity stayed within 0.118%.

## Checks

- The page states the 28 native runs above and that the browser and native builds of 5.2.4 agree byte for byte on six of ten presets and within 0.059 ft on the rest.
- Arithmetic we checked (ours): 130.29 ac-ft over 521.19 ac = 0.25 ft = 3.00 in, as stated.
- Outside reviews Bob supplied shaped the versions: the page scores the first, answered in 1.1, at 85/100 and the eleventh, answered in 1.15, at 89/100.

## What this does not show

As the page lists it: before a run, or when a run is out of date, the picture shows rational-method and Manning design numbers; playback interpolates between report times, so a spike shorter than the report step may not animate; the glow, stars and cell bodies are drawing choices; OpenSWMM 6 FV runs with four cells per conduit by default, which its own manual calls not converged; the default design carries the 3 in storm and is drawn so nobody mistakes it for a guarantee.

## How to reproduce

Pick a preset, Run, and export the .inp; Checks shows the geometry fingerprint that proves Freeze geometry held.

## Credits and licenses

The reference image is a Grok Imagine render supplied by Bob. EPA SWMM 5.2.4 (public domain); OpenSWMM 6 (HydroCouple, Apache-2.0). No license is stated for the page.

## AI use

The page says: built with Claude (Anthropic's AI model, Claude Opus 5.5) in October 2026 at the request of Robert (Bob) Dickinson, who supplied the reference image, the ask and the instruction to embed his WebAssembly engine. Claude decided how each element of the image maps to SWMM objects and wrote the generator, the .inp writer, the renderer, the .out reader, the engine comparison, every chart, the Doc essay and the .docx; the two engines are reused byte for byte and Claude wrote neither. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.15: answers an eleventh outside review (89/100); the version read.
- 1.10 to 1.13: all three engines together; classic dynamic wave options for EPA 5.2.4; a Peaks card; picked nodes and pipes, statistics and a 3D view.
- 1.1: follows an outside review (85/100).

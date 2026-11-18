---
title: "S241: Quasi-2D Mesh Maker for SWMM5, summary written from the page (v1.0)"
type: source
raw: raw/apps/quasi-2d-mesh-maker-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-04
ingested: 2026-11-17
tags: [apps, swmm5, quasi-2d, overland-flow, mesh]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Quasi-2D Mesh Maker for SWMM5, version 1.0: a generator that takes a flood boundary, obstructions and a ground surface (planes, a street valley, a sag, rolling ground, a DEM or survey points) and writes a PCSWMM-style quasi-2D overland mesh as a SWMM5 .inp, with links to a 1D sewer. No engine runs in the page. Raw file: [raw/apps/quasi-2d-mesh-maker-v1.0.md](../../raw/apps/quasi-2d-mesh-maker-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1791108486-b603, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The published page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session. The summary says the Netlify copy adds a one-line AI-use note.

**Claims worth keeping** (all copied from the file)
- Its storage-exact mesh, with half-width links that hold exactly the cell area, measured stored area / plan area = 1.000 in EPA SWMM 5.2.4 built from source on 4 October 2026.
- Sheet flow, 4 in/hr on a 1 % plane of 200 x 400 ft at n = 0.03: both width rules reach the same steady depth; only the storage-exact mesh gets there on time (kinematic time of concentration 9.5 min). Its link velocities show twice the sheet-flow velocity.
- Continuity, rain as subcatchments or as direct inflow: hexagonal 286 cells -0.07 % and 0.00 %; rectangular 256 cells -0.08 % and -0.02 %.
- Whole cells cover 97 % of the area inside the boundary; cells are not clipped. A 2D conduit is dropped when the line between two cell centres crosses an obstruction edge.
- 20,000 random points: none inside more than one subcatchment polygon.

**Limits it states.** No comparison with PCSWMM's own width rule or a 2D shallow-water solver, and no test of diagonal flow.

**Checked at ingest.** [Walk the Mesh (app)](../entities/walk-the-mesh.md) reports the same storage doubling on the plain mesh and a different fix, Manning's n times 0.841 [S242](S242-walk-the-mesh-summary.md); this page's fix is the half-width link. Both are pages Claude summarized; neither cites the other. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://quasi-2d-mesh-maker.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Quasi-2D Mesh Maker for SWMM5 (app)](../entities/quasi-2d-mesh-maker.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Walk the Mesh (app)](../entities/walk-the-mesh.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md), [Subcatchment width](../concepts/subcatchment-width.md).

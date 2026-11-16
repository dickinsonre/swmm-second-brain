---
title: "S76: Inside the Network, technical summary (app .md, v1.1.0)"
type: source
raw: raw/apps/inside-the-network-cfd.md
kind: app-md
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-15
tags: [apps, cfd, hydraulics, swmm5, extran, wasm, verification]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary that ships with Inside the Network, version 1.1.0: a 2D vertical-slice free-surface CFD solver run along one path of a SWMM 5 network, beside EPA SWMM 5.2.4 on the whole file. Raw file: [raw/apps/inside-the-network-cfd.md](../../raw/apps/inside-the-network-cfd.md). Bob uploaded it on 14 November 2026.

**How it was written.** By Claude (Anthropic) in November 2026 at Bob's direction. Bob asked for a CFD water simulation of a SWMM 5 network, supplied seven EXTRAN example files and chose the compressed whole-path approach. Claude chose the numerical method and wrote the solver (netcfd 1.1). "No person has yet reviewed the solver code or the essay, rerun the gates independently, or compared any of it with measured data."

**Claims worth keeping**
- The CFD is PIC/FLIP on a staggered grid with cut-cell walls and a ghost-fluid free surface, written for the app. At true scale it uses a rough-wall log law whose roughness is set so it carries Manning's velocity at full flow.
- Four EXTRAN manual examples (1, 2, 7, 80) run with lengths compressed 100, 50 or 25 to 1: length and time divided by the factor, bed slope and friction slope multiplied by it. Heights, depths, velocities and flows are unscaled.
- Everything that joins or leaves the path is taken from the SWMM 5 results, so the CFD cannot disagree with SWMM 5 about side branches or the Example 7 pump.
- Gates at true scale: Ritter dam-break depth 0.889 ft, CFD 0.900 ft at 0.1 ft cells; Manning normal depth within -1.1 to +3.2 % in five uniform-flow cases; Belanger sequent depth 2.267 ft, CFD 2.181 ft.
- Example 1, north branch, plateau means at 50 to 1: node depths differ from SWMM 5 by -0.27 to +0.61 ft; conduit flows by at most 1.2 cfs. Water over the rim for the event: CFD 102,622 ft³, SWMM 5 114,210 ft³.
- Example 80 (constricting pipes): the CFD is lower than SWMM 5 at every node, by 0.24 to 1.51 ft.
- A short true-scale section, 150 ft: at MH1 the CFD level is 2.35 ft and SWMM 5 with no losses 1.06 ft; with Kentry 0.5 and Kexit 1.0 SWMM 5 gives 1.92 ft. SWMM 5 is not steady over that window.
- Engine: EPA SWMM 5.2.4 plus Bob's KW/SF patch with the extension off, wasm32-wasi, 853,130 bytes. Byte-identical `.out` against a native EPA engine on three twin models and on EXAM80a.
- On three example files the wasm run writes 479 records and the native reference 480. The file traces it to `project.c`: `TotalDuration = floor((EndDateTime - StartDateTime) * SECperDAY)` gives 28799 s for a run ending at 08:00 on 01/01/1988; the native reference is the OWA fork inside swmm-toolkit, which gets 28800.
- Three supplied files were not used; two have routing continuity errors of -99.965 % and -17.407 %.

**Limits it states (L-1 to L-18).** Two dimensions; conduits are boxes. No air pressure. Thin water drifts below about three cells. No measured data anywhere. Chambers are not compressed: a riser stores what a shaft of 310 to 940 ft² would, against 12.57 ft² for a SWMM 5 junction. Compressed slopes reach about 124 %. Its `.out` reader is a minimal one, not the shared parser.

**Checked at ingest.** The comparisons carry no pass mark, by the file's own statement. The duration-floor note agrees with defect D-1 of [S79](S79-teacher-forced-swmm-summary.md), found independently.

**Feeds:** [Inside the Network (app)](../entities/inside-the-network-cfd.md), [Run duration floored to whole seconds](../concepts/run-duration-floor.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [EXTRAN](../entities/extran.md).

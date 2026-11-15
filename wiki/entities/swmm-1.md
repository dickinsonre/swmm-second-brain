---
title: SWMM 1 (1971)
type: entity
updated: 2026-11-15
sources: [S01, S07, S21, S22, S60, S73]
tags: [swmm-history, swmm1, engine]
reviewed: 2026-11-15
---
The first Storm Water Management Model, written from 1969 to 1971 by Metcalf & Eddy (Palo Alto), the University of Florida (Gainesville) and Water Resources Engineers (Walnut Creek) for the EPA Water Quality Office [S01](../sources/S01-swmm1-engine-app-md.md). Published as four volumes, EPA 11024 DOC 07/71 to 10/71: Final Report, Verification and Testing, User's Manual, Program Listing [S01](../sources/S01-swmm1-engine-app-md.md).

**Size.** 65 program units and 12,200 cards in five blocks [S01](../sources/S01-swmm1-engine-app-md.md). See [Block architecture and interface files](../concepts/block-architecture.md).

**Methods, as coded in 1971** [S01](../sources/S01-swmm1-engine-app-md.md)
- Runoff: a nonlinear reservoir on three planes per subarea with Horton infiltration (WSHED), gutter and pipe routing (GUTTER), surface quality (SFQUAL).
- Transport: elements sequenced upstream to downstream; kinematic wave by Newton iteration on normalized flow-area tables for 12 conduit shapes; dry-weather flow (FILTH); infiltration (INFIL); quality routing.
- Storage: basin routing, a string of treatment units, and cost.
- Receiving Water: link-node explicit hydrodynamics (SWFLOW) and quality.

**Faults found in the listing as printed.** Fourteen, found by running it in 2026 [S01](../sources/S01-swmm1-engine-app-md.md). The ones with consequences:

| Card | Fault | Effect |
|---|---|---|
| `STRA 16`, `SROU 17`, `PLUG 21` | DT converted from minutes to seconds twice | Storage with an orifice or weir outlet stops in `INTERP`; pumped outlets work |
| `TRCH104`, `TRCH106` | TRCHEK tests DT with no COMMON card for it | Every deck with high-rate filters is refused |
| `TRAN346` | `PLUTO(ND,NJ)=PLUTO(ND,NJ)/60.` | Candidate cause of printed 1971 pollutant loads far above the listing's; fits peak hours only |
| `HYDR137` | `WAREA(J)` left out of the continuity check | Printed continuity error wrong; flows unaffected |
| `TRAN497T`-`498`, `STOR103`-`104` | Pollutant loop order differs between writer and reader | With two or more outfalls, Storage reads coliforms as suspended solids |
| `HYDR 26`, `HYDR 51`-`55` | 200 elements cleared in arrays dimensioned 160 | Traced through blank COMMON: nothing corrupted in the f2c build |
| `INDA314T` | Stability limit `0.75*L/SQRT(32.2*(R+2))` differs from the manual's printout | The manual example's 300 s step exceeds the listing's limit in 9 channels |

All from [S01](../sources/S01-swmm1-engine-app-md.md), and listed again unchanged at version 3.13 [S73](../sources/S73-swmm1-engine-app-md-v3-13.md), which adds that WSHED reads the rain histogram once per step at its middle (`WSHE 24`) and calls that "a method, not a fault". None has a register ID yet; see [The SWMM findings register](../concepts/findings-register.md).

**Its mark on later versions.** The single subcatchment width goes back to SWMM 1's street models, in Bob's words [S22](../sources/S22-li-ten-problems.md). See [Subcatchment width](../concepts/subcatchment-width.md).

**Running it today.** [SWMM 1 Engine (app)](swmm-1-engine-app.md). How it was checked: [Verification against printed runs](../concepts/verification-against-printed-runs.md).

**Disagreements**
- Q02, settled by the EPA reference manual: its development-history table credits SWMM I to Metcalf & Eddy, Water Resources Engineers and the University of Florida [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md), matching [S01](../sources/S01-swmm1-engine-app-md.md) and [S07](../sources/S07-swmm5org-topic-swmm-history.md). Camp Dresser & McKee first appears in that table at SWMM 3 (1981), so [S21](../sources/S21-li-edition-56-swmm-history.md) is the one in error.
- [S21](../sources/S21-li-edition-56-swmm-history.md) gives SWMM 1 four blocks; the listing has five counting the Executive [S01](../sources/S01-swmm1-engine-app-md.md).

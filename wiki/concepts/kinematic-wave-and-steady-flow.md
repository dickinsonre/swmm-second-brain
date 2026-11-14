---
title: Kinematic wave and steady flow routing
type: concept
updated: 2026-11-14
sources: [S01, S08, S10, S17]
tags: [hydraulics, swmm5, routing]
reviewed: no
---
SWMM5 has two routing methods simpler than [dynamic wave](dynamic-wave-routing.md) [S17](../sources/S17-li-routing-options.md).

**Steady flow.** No routing at all: the inflow hydrograph at the upstream end of a conduit appears at the downstream end with no delay and no change of shape. Normal flow relates flow to area. It is insensitive to the time step and suits only preliminary analysis of long continuous simulations [S17](../sources/S17-li-routing-options.md).

**Kinematic wave.** Continuity plus a momentum equation reduced to "water surface slope equals conduit slope". The most a conduit carries is full normal flow; the excess is lost or ponds at the inlet node. Flow and area vary along the conduit, so hydrographs are delayed and attenuated. Stable at time steps of 1 to 5 minutes [S17](../sources/S17-li-routing-options.md).

**What neither can do.** Backwater, entrance and exit losses, flow reversal, pressurized flow. Both are limited to dendritic networks: one outflow link per node, or two at a divider [S17](../sources/S17-li-routing-options.md).

**Who has them.** Only SWMM5 and InfoSWMM have kinematic wave. SWMM5, InfoSWMM and InfoSewer have steady state; Bob rates InfoSewer's best for its flow loading and flow splitting. ICM SWMM and ICM InfoWorks have neither as a solver, only a quasi-steady state made by restarting from a saved state [S17](../sources/S17-li-routing-options.md).

**Lifting the dendritic limit.** Bob's repository SWMMBobSWMM6/swmm5-kw routes kinematic wave and steady flow through junctions that split flow and through loops [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

**Where it started.** The Transport Block of [SWMM 1 (1971)](../entities/swmm-1.md) (1971) routed by kinematic wave, with Newton iteration on normalized flow-area tables for 12 conduit shapes [S01](../sources/S01-swmm1-engine-app-md.md).

**How often it is asked.** "Kinematic or dynamic wave" tags 131 of Bob's 2,879 OpenSWMM thread titles [S10](../sources/S10-openswmm-top25-problems.md).

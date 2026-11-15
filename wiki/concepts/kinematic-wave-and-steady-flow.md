---
title: Kinematic wave and steady flow routing
type: concept
updated: 2026-11-15
sources: [S01, S08, S10, S17, S60]
tags: [hydraulics, swmm5, routing]
reviewed: 2026-11-15
---
SWMM5 has two routing methods simpler than [dynamic wave](dynamic-wave-routing.md) [S17](../sources/S17-li-routing-options.md).

**Steady flow.** No routing at all: the inflow hydrograph at the upstream end of a conduit appears at the downstream end with no delay and no change of shape. Normal flow relates flow to area. It is insensitive to the time step and suits only preliminary analysis of long continuous simulations [S17](../sources/S17-li-routing-options.md).

**Kinematic wave.** Continuity plus a momentum equation reduced to "water surface slope equals conduit slope". The most a conduit carries is full normal flow; the excess is lost or ponds at the inlet node. Flow and area vary along the conduit, so hydrographs are delayed and attenuated. Stable at time steps of 1 to 5 minutes [S17](../sources/S17-li-routing-options.md).

**What neither can do.** Backwater, entrance and exit losses, flow reversal, pressurized flow. Both are limited to dendritic networks: one outflow link per node, or two at a divider [S17](../sources/S17-li-routing-options.md).

**Who has them.** Only SWMM5 and InfoSWMM have kinematic wave. SWMM5, InfoSWMM and InfoSewer have steady state; Bob rates InfoSewer's best for its flow loading and flow splitting. ICM SWMM and ICM InfoWorks have neither as a solver, only a quasi-steady state made by restarting from a saved state [S17](../sources/S17-li-routing-options.md).

**Lifting the dendritic limit.** Bob's repository SWMMBobSWMM6/swmm5-kw routes kinematic wave and steady flow through junctions that split flow and through loops [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

**Where it started.** The Transport Block of [SWMM 1 (1971)](../entities/swmm-1.md) (1971) routed by kinematic wave, with Newton iteration on normalized flow-area tables for 12 conduit shapes [S01](../sources/S01-swmm1-engine-app-md.md).

**How often it is asked.** "Kinematic or dynamic wave" tags 131 of Bob's 2,879 OpenSWMM thread titles [S10](../sources/S10-openswmm-top25-problems.md).

**Added 15 November 2026: what the EPA hydraulics manual says.** From Chapters 2 and 4 of the primary document [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md):
- The limits, in the manual's words: directed acyclic networks only; a junction has at most one outlet link, which must be a conduit; a divider has two outlet conduits; a storage node may have any number of outlet links of any type; upstream conduit offsets are ignored except at storage nodes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Pumps, weirs and orifices work only from storage nodes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md); see [Pumps and pump curves](pumps-and-pump-curves.md), [Orifices](orifices.md) and [Weirs and outlets](weirs-and-outlets.md).
- Conduits are routed in topologically sorted order, found once by Kahn's algorithm. A loop stops the program with an error [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Flow dividers are active only under kinematic wave; under dynamic wave a divider is an ordinary junction [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- The head reported at a non-storage node is set to the highest water elevation in the connected links, for reporting only [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- It is unconditionally stable, so it does not use the variable time step [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). On the manual's 2,000 ft example it is stable at 120 s where dynamic wave needed 25 s [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Attenuation: the paragraph above, from Bob's article, says hydrographs are delayed and attenuated [S17](../sources/S17-li-routing-options.md). The manual's section 2.2 says kinematic wave solutions "show no attenuation, no dispersion, and some distortion", and its Table 2-1 answers "no" for hydrograph attenuation; its section 4.4 then reports "a very modest attenuation" on the example and names numerical diffusion as the cause [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Q61 in [Open questions](../open-questions.md).
- History: kinematic wave was in the 1971 release, with an enhancement to approximate backwater in subcritical flow. SWMM 5 dropped the enhancement for the classical formulation [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- The network objects themselves are on [SWMM 5 network objects, boundary and initial conditions](swmm5-network-objects.md).

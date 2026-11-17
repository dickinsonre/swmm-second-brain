---
title: Kinematic wave and steady flow routing
type: concept
updated: 2026-11-17
sources: [S01, S08, S10, S17, S60, S117, S125, S195]
tags: [hydraulics, swmm5, routing]
reviewed: 11/16/2026
changed_after_review: "2026-11-16 (S60 Chapter 5 ingest): one paragraph added at the end, headed Added 16 November 2026, later, on the area at maximum flow (S60); 2026-11-17 (S192 to S202 ingest): one paragraph added at the end on swmm5-kw (S195)"
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

**Added 15 November 2026: two apps past the dendritic limit.** [Kinematic Wave Router (app)](../entities/kinematic-wave-router.md), Bob's Ruby kinematic wave, divides flow equally at a split and iterates on loops; its loop fixture did not fully converge after 20 iterations [S125](../sources/S125-kinematic-wave-router-replit-summary.md). [BatchSWMM56 (app)](../entities/batchswmm56.md) carries the 5.2.4 KW/SF extension as its "SWMM5 Extended" engine [S117](../sources/S117-batchswmm56-replit-summary.md). Replit Agent wrote both summaries; Bob has read neither (Q74).

**Added 16 November 2026, later.** The kinematic wave solution for a closed conduit needs the area at which the section factor, and so the Manning flow, is greatest. Chapter 5 of the manual tabulates it as a fraction of the full area for every closed shape, from 0.92 for the arch to 0.9756 for the circle [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md); the table is on [Conduit cross-sections: the built-in shapes](conduit-cross-sections.md).

**Added 17 November 2026: swmm5-kw, measured.** The page for [swmm5-kw](../entities/swmm5-kw.md) 1.1 says how it lifts the dendritic limit [S195](../sources/S195-swmm5-kw-summary.md).
- A junction with several outlets shares its outflow by one of three rules. HEAD, the default, finds the one water level at which the outlets, each at Manning normal depth and capped at full flow, carry exactly the inflow; CAPACITY shares by full-flow capacity; AREA is the third. A loop is iterated within each routing step until the returning flow settles.
- On one split of 20 cfs into a 3.0 ft and a 1.5 ft outlet, HEAD sends 73.8 % down the big pipe, dynamic wave 71.3 % and CAPACITY 86.4 %. On two other small networks every peak is within 1.8 % of dynamic wave.
- Switched to KINWAVE, 925 of 3,218 dynamic-wave corpus models stop stock 5.2.4 at ERROR 133 or 131; swmm5-kw ran 234 of them to the end, with a median continuity error of 0.17 % and 60 past 1 %.
- It still cannot represent backwater, surcharge or reverse flow, and a loop pipe that would run backwards is wrong in direction [S195](../sources/S195-swmm5-kw-summary.md).

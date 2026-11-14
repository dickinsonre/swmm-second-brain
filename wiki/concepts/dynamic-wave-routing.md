---
title: Dynamic wave routing
type: concept
updated: 2026-11-14
sources: [S08, S10, S17, S18, S20, S22, S55, S60, S62]
tags: [hydraulics, swmm5, routing]
reviewed: no
---
Dynamic wave routing solves the full one-dimensional St. Venant equations: continuity and momentum in the conduits and a volume balance at the nodes [S17](../sources/S17-li-routing-options.md). It is the only SWMM5 routing method that handles backwater, entrance and exit losses, flow reversal, pressurized flow, loops and multiple downstream diversions [S17](../sources/S17-li-routing-options.md).

**How SWMM 5 does it**
- Each conduit is one computational element. Head is computed at the nodes and flow in the link; a 400 ft conduit has two points where anything is computed [S20](../sources/S20-li-edition-54-two-solvers.md).
- The lineage is EXTRAN: a node-link formulation [S20](../sources/S20-li-edition-54-two-solvers.md). See [EXTRAN](../entities/extran.md).
- Every time step is iterated. Bob's oldest posts on the subject (2013) are on successive under-relaxation inside each dynamic wave step [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).
- It needs time steps of about thirty seconds or less, and SWMM can cut the user's maximum step to stay stable [S17](../sources/S17-li-routing-options.md).

**The solution procedure, from the engine's author** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)
1. Start from the flows and heads of the last time step.
2. Solve the link equation for a new flow in every conduit.
3. Blend new and old flow with a relaxation factor of 0.5.
4. Compute a new head at every node from the new flows.
5. Blend new and old head with the same factor.
6. Stop when every head has moved less than the tolerance (default 0.005 ft) or after the maximum number of trials (default 8); otherwise repeat from step 2.

The method is implicit in time (backward Euler, solved by Picard iteration); earlier SWMM versions used an explicit Modified Euler method [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Flows and heads are updated one conduit and one node at a time, with no spatial coupling, so the Courant condition still applies, though less strictly [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). A 2,000 ft conduit split into 10 sections of 200 ft has a stable step near 25 s; run at a fixed 120 s it goes completely unstable, and with 120 s as the cap of a variable step it is stable [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Devices that keep it stable** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)
- Minimum nodal surface area, default 12.56 sq ft (a 4 ft manhole). It adds no volume. One app's tutorial input writes `MIN_SURFAREA 12.557`, with `MAX_TRIALS 8` and `HEAD_TOLERANCE 0.005`, the manual's defaults for the other two [S62](../sources/S62-rules-for-responsible-modeling-app-md.md).
- Inertial damping by Froude number: full inertia up to 0.5, none at 1 or above.
- A normal-flow limit when the water surface slope is less than the conduit slope, or the Froude number exceeds 1.
- Upstream weighting of area and hydraulic radius as flow nears supercritical.

**The equation has four terms.** Bob's 2007 poster with Khalid Khan and Jim Smullen plotted flow against them as dq1 to dq4 and compared SWMM 4 with SWMM 5; per the AI reading of the poster, SWMM 5 checks negative as well as positive flows, where SWMM 4 checked only positive ones [S18](../sources/S18-li-invalid-hydraulic-solutions-poster.md).

**The stability options carry history.** Conduit lengthening, minimum surface area, inertial damping and the surcharge iteration each fixed an instability; the manual listed them as options and said little about when to use them. "Add a dummy node, cut the time step" spread as folklore. Bob's comment: "True, very true." [S22](../sources/S22-li-ten-problems.md) See [Conduit lengthening](conduit-lengthening.md) and [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md).

**How often it hurts.** Dynamic-wave stability, continuity and surcharge is the largest problem group in Bob's OpenSWMM threads: 224 of 2,879 thread titles [S10](../sources/S10-openswmm-top25-problems.md).

**Fixes Bob has planned** (status in the source: planned; each "informed by how InfoWorks ICM handles the same problem") [S55](../sources/S55-swmm-brain-readme.md)

| Problem | SWMM 5 now, per the source | Proposed |
|---|---|---|
| Preissmann slot | Fixed width, about 1 % of pipe diameter | Narrow it as pressure stabilizes |
| Crown transition | Oscillation at the boundary between surcharge and free surface | Damped transition with a hysteresis band |
| Supercritical flow | Abrupt cutoff by the Froude limiter | Smooth blending across flow regimes |
| Junction losses | Continuity only, no head loss at junctions | Optional momentum-based head loss |
| Pond and pipe coupling | Instability when storage surface area is small | A relaxation factor for stiff coupling |

**Compared with ICM.** See [SWMM 5 versus ICM InfoWorks](swmm5-versus-icm-infoworks.md).

**Settled**
- Q12, implicit or explicit: both words have a basis. The time integration is implicit backward Euler, as [S20](../sources/S20-li-edition-54-two-solvers.md) says, but it is solved element by element without spatial coupling, so it keeps the time-step limit of an explicit scheme [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). The predecessors of SWMM 5 were explicit [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

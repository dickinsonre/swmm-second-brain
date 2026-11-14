---
title: Dynamic wave routing
type: concept
updated: 2026-11-14
sources: [S08, S10, S17, S18, S20, S22, S55]
tags: [hydraulics, swmm5, routing]
reviewed: no
---
Dynamic wave routing solves the full one-dimensional St. Venant equations: continuity and momentum in the conduits and a volume balance at the nodes [S17](../sources/S17-li-routing-options.md). It is the only SWMM5 routing method that handles backwater, entrance and exit losses, flow reversal, pressurized flow, loops and multiple downstream diversions [S17](../sources/S17-li-routing-options.md).

**How SWMM 5 does it**
- Each conduit is one computational element. Head is computed at the nodes and flow in the link; a 400 ft conduit has two points where anything is computed [S20](../sources/S20-li-edition-54-two-solvers.md).
- The lineage is EXTRAN: a node-link formulation [S20](../sources/S20-li-edition-54-two-solvers.md). See [EXTRAN](../entities/extran.md).
- Every time step is iterated. Bob's oldest posts on the subject (2013) are on successive under-relaxation inside each dynamic wave step [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).
- It needs time steps of about thirty seconds or less, and SWMM can cut the user's maximum step to stay stable [S17](../sources/S17-li-routing-options.md).

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

**Disagreements**
- [S20](../sources/S20-li-edition-54-two-solvers.md) calls the EXTRAN-lineage time integration "implicit backward Euler"; [S08](../sources/S08-swmm5org-topic-inside-swmm5.md) lists an app on "why SWMM5's explicit dynamic wave solution stays robust". Open question Q12 in [Open questions](../open-questions.md).

---
title: "S60: EPA SWMM Reference Manual, Volume II, Hydraulics (Rossman, May 2017)"
type: source
raw: raw/manuals/EPA_SWMM_VOLUME_II_HYDRAULICS.md
kind: epa-manual
author: Lewis A. Rossman
published: 2017-05-01
ingested: 2026-11-14
coverage: partial
read: [1.1 Introduction and Table 1-1, "Chapter 2 SWMM's Hydraulic Model (2.1 to 2.3)", "Chapter 3 Dynamic Wave Analysis (3.1 to 3.4)", "Chapter 4 Kinematic Wave Analysis (4.1 in part, 4.3, 4.4; pages 64 to 66 are not in the raw file)", "Chapter 6 Pumps and Regulators (6.1 to 6.4; page 122 is not in the raw file)"]
tags: [swmm5, hydraulics, primary-document, epa]
reviewed: 2026-11-15
changed_after_review: "2026-11-15: read list and coverage line extended; claims from Chapters 2, 4 and 6 added under Added 15 November 2026; Feeds extended"
---
**What it is.** EPA/600/R-17/111, the hydraulics volume of the SWMM 5 reference manual, by Lewis A. Rossman, U.S. EPA Office of Research and Development. A primary document: the engine's author describing what the engine computes. Raw file: [raw/manuals/EPA_SWMM_VOLUME_II_HYDRAULICS.md](../../raw/manuals/EPA_SWMM_VOLUME_II_HYDRAULICS.md), about 50,000 words.

**How it was written.** A U.S. government report, in the public domain. The markdown is a conversion of the PDF kept in Bob's `SWMMEnablement/SWMM_MD_Documents` repository. The conversion lost most equations (symbols are garbled or missing) and the 47 figures are not in `raw/`. The prose and the numbered procedures survive. Check any equation against the EPA PDF before quoting it.

**Coverage: partial.** Read in full so far: section 1.1 with Table 1-1; Chapter 2, SWMM's Hydraulic Model; Chapter 3, Dynamic Wave Analysis; Chapter 4, Kinematic Wave Analysis, as far as the raw file holds it; and Chapter 6, Pumps and Regulators, likewise. Not yet read: sections 1.2 to 1.5, Chapters 5 and 7, and the appendices. Claims in the wiki come only from the parts read.

**Claims worth keeping**
- SWMM was first developed in 1969 to 1971.
- Table 1-1, development history: SWMM I, 1971, Metcalf & Eddy, Water Resources Engineers and the University of Florida; SWMM II, 1975, University of Florida, the first widely distributed version; SWMM 3, 1981, University of Florida and Camp Dresser & McKee, adding the full dynamic wave routine, Green-Ampt infiltration, snow melt and continuous simulation; SWMM 3.3, 1983, US EPA, the first PC version; SWMM 4, 1988, Oregon State University and Camp Dresser & McKee, adding groundwater, RDII and irregular channel cross-sections over the 1990s; SWMM 5, 2005, US EPA and CDM-Smith, a complete rewrite in C.
- Dynamic wave modeling entered SWMM in version 3, in 1981, as a separate module called EXTRAN. Its node-link method came from the Sacramento-San Joaquin Delta Model (1965) and the WRE Transport Model (1975).
- Earlier versions solved the link equation with an explicit method (forward Euler; more exactly the two-step Modified Euler). SWMM 5 uses an implicit backward Euler method "to provide improved stability".
- The implicit equations are solved by functional iteration (successive approximations, or Picard's method): new flow for each link, relaxation, new head for each node, relaxation, repeat until the heads stop changing.
- The relaxation factor is 0.5. The default convergence tolerance is 0.005 ft and the default maximum number of trials is 8.
- Flows and heads are updated one conduit and one node at a time, not simultaneously, so there is no spatial coupling between elements and the Courant condition "would still apply but perhaps not as strictly".
- Minimum nodal surface area defaults to 12.56 sq ft, the area of a 4 ft manhole. It is a computational device and adds no volume.
- Inertial damping: the factor is 1 for Froude numbers up to 0.5, 0 at 1 or higher, linear between. A second option ignores the inertial term altogether.
- A node is surcharged when all conduits connected to it are full or its water level is above the crown of the highest connected conduit. Head is then updated by a perturbation equation, and under-relaxation is not applied to it.
- A node whose head would exceed its maximum is flooded and the excess is lost from the system, unless the node has a ponded area, in which case the water is stored above it and returns.
- A system continuity error above 5 to 10 percent may be a sign of numerical instability. The Flow Instability Index of a link ranges from 0 to 150 and does not measure the size of the fluctuations.
- Example: a 2 ft by 2 ft conduit, 2,000 ft long, in 10 sections of 200 ft has a stable time step of about 25 s; as one 2,000 ft section, about 250 s. A fixed step of 120 s on the 10-section conduit is completely unstable; a variable step capped at 120 s is stable.

**Added 15 November 2026: Chapters 2, 4 and 6**

*What the raw file lacks.* The page numbers in the converted text run 63, 67 in Chapter 4 and 121, 123 in Chapter 6. The end of section 4.1, all of section 4.2 (Solution Method, with Figures 4-1 and 4-2), section 6.3.6 and steps 3 to 6 of the weir summary are not in the raw file (Q60). Nothing below comes from them.

*Chapter 2, the hydraulic model*
- Four node types: junction, outfall, flow divider, storage unit. Storage units are the only nodes with volume and surface area, and they are not allowed to pressurize.
- An outfall's boundary is one of four: critical or normal depth in the connecting conduit, a fixed stage, a tide table by hour of the day, or a time series of stage. It may have a flap gate.
- A flow divider can have no more than two conduits on its discharge side. Its four kinds are cutoff, overflow, tabular and weir.
- Conduit slope is computed, not entered. A slope of 0 is not allowed: the drop between the ends has a minimum of 0.001 ft, and the user can set a larger minimum slope. Offsets are kept internally as elevations.
- Dynamic wave analysis accounts for channel storage, backwater, entrance and exit losses, culvert flow, flow reversal and pressurized flow, on any layout, at the price of small time steps.
- Kinematic wave analysis is most applicable to conduits steeper than about 0.1 percent with shallow, fast flow. Its five limits: directed acyclic networks only; a junction has at most one outlet link, which must be a conduit; a divider has two outlet conduits; a storage node may have any number of outlet links of any type; upstream conduit offsets are ignored except at storage nodes.
- Steady flow analysis translates the inflow hydrograph to the downstream end with no delay or change of shape, under the same limits, and suits "rough preliminary analysis of long-term continuous simulations".
- Table 2-1, kinematic wave column: branched networks only; flow splits with divider nodes; pumps, weirs and orifices only from storage nodes; no adverse slopes, minor losses, culverts, hydrograph attenuation, backwater, surcharge, reverse flow or tidal effects; offsets ignored.
- Section 2.2 says kinematic wave solutions "show no attenuation, no dispersion, and some distortion of the hydrograph shape" (see Q61).
- Outfall heads are needed only for dynamic wave analysis. A user-defined inflow is a baseline value times a pattern factor plus a scale factor times a time series value.
- By default all heads and flows start at 0. An initial conduit flow is taken as uniform steady flow at normal depth. Under dynamic wave, a non-storage, non-outfall node with no initial head starts at the average elevation of the initial flow depths in its inflowing conduits.

*Chapter 4, kinematic wave*
- Kinematic wave routing was in the original release of SWMM in 1971, before there was a dynamic wave option. The original had an enhancement to approximate backwater in subcritical flow. SWMM 5 dropped it for the classical formulation.
- Conduits are processed in topologically sorted order, found once before time 0 by Kahn's algorithm after every link is oriented in the direction of positive slope. If a loop is found the program stops with an error.
- Flow dividers are active only under kinematic wave analysis. Under dynamic wave a divider is treated as an ordinary junction.
- A storage node is updated by successive approximation, with a weight of 0.55 on the new estimate and a tolerance of 0.005 ft.
- The head reported at a non-storage node is set "arbitrarily" to the highest water elevation in the connected links, for reporting only. Surcharge depth at a node is ignored.
- Inflow beyond what the outflow links can take is lost from the system, or ponds if the node's ponded area is not zero. The ponded area "does not enter into any computations"; it only switches ponding on.
- Stability: unconditionally stable for weights above 0.5 (Metcalf and Eddy, 1971) and at 0.5 (Smith, 1978), so the variable time step is not used. It is still subject to numerical dispersion and to numerical diffusion, which attenuates the hydrograph.
- Example: the 2,000 ft conduit of Chapter 3 (2 ft by 2 ft, slope 0.05 percent, n of 0.015, ten sections of 200 ft) is stable under kinematic wave at 120 s, where dynamic wave needed 25 s. The kinematic result shows "a very modest attenuation" of the peak and some distortion; the manual calls the dynamic wave result the more accurate.

*Chapter 6, pumps and regulators*
- Five pump kinds: Type1 (flow by inlet volume), Type2 (flow by inlet depth), Type3 (flow by head difference), Type4 (flow by inlet depth, continuous), and Ideal (flow equals inflow; must be the only outflow link of its node).
- Type1 and Type2 curves are searched for the first point whose volume or depth exceeds the inlet node's. A pump's flow "is not allowed to be outside the minimum and maximum values defined by its pump curve".
- The pump flow is checked so the inlet does not go below 0 depth in the step. At a storage node it is capped by inflow plus stored volume over the step. At any other node under dynamic wave, if the estimated end-of-step head is below the invert, "the pumping rate is set equal to the node's current inflow" (see Q62).
- Pumps add no surface area under dynamic wave and their flows are not under-relaxed.
- Pump energy per step, in the converted Equation 6-2, is 0.7457 times the head difference in ft times the flow in cfs times the step in hours, divided by 8.814, without wire-to-water efficiency. Our check: 550 ft-lb/s per horsepower over 62.4 lb/ft³ is 8.814, and 0.7457 is kilowatts per horsepower, so the constants are consistent. The equation should still be checked against the PDF.
- Orifice discharge coefficient: 0.6 most commonly cited, 0.4 for ragged edges, 0.59 to 0.67 in experiments.
- An orifice whose inlet is not submerged is computed as a weir; a bottom orifice uses a weir coefficient of 3.33 ft^0.5/s and its perimeter as crest length.
- SWMM 5 gives an orifice a surface area under dynamic wave because older versions represented it as an equivalent pipe. A weir gets none.
- Weir coefficients in ft^0.5/s: 3.33 sharp-crested rectangular; 2.5 triangular (2.5 to 2.8 measured); 2.34 to 3.32 in Table 6-3 for broad crests; 3.32 in the original Engels side weir equation.
- The side weir equation has crest length to the power 0.83 and head to the power 1.67; "previous versions of SWMM used an incorrect form" with the length exponent equal to 1.0.
- Submerged weirs use Villemonte's factor. A weir surcharged inside a closed structure is computed as an orifice.
- An outlet is a regulator with a user's rating curve, a power function or a table, on upstream depth or on head difference. Outside the table's range the first or last flow is used.

*Wording slips seen in the converted text, to check against the PDF (Q63).* The storage-node side bar cites Equation 4-16 for a constant that Equation 4-15 defines. Section 6.2.6 says "side weirs" and "bottom weirs" in the orifice summary and sends step 4 back to "step 2". Section 6.3.2 calls the trapezoidal weir equation 6-18; it is numbered 6-20.

**Feeds:** [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md), [EXTRAN](../entities/extran.md), [SWMM 1 (1971)](../entities/swmm-1.md), [Lewis A. (Lew) Rossman](../entities/lew-rossman.md), [Open questions](../open-questions.md). Added 15 November 2026: [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [Orifices](../concepts/orifices.md), [Weirs and outlets](../concepts/weirs-and-outlets.md).

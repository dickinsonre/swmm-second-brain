---
title: "S185: SWMM Quality Assurance Report, Dynamic Wave Flow Routing (Rossman, EPA, 2006)"
type: source
raw: raw/manuals/SWMM5_QA.md
kind: epa-report
author: Lewis A. Rossman
published: 2006-09-01
ingested: 2026-11-16
coverage: partial
read: [Chapter 1 Introduction, Chapter 2 Routing Models, Chapter 3 Testing Procedure, "Chapter 4 Extran Manual Test Cases (nine of its pages are not in the raw file)", Chapter 7 Summary and Conclusions, Chapter 8 References]
tags: [swmm4, swmm5, dynamic-wave, verification, extran, test-models, primary-document, epa]
reviewed: no
---
**What it is.** EPA/600/R-06/097, the quality assurance report that compared the dynamic wave routing of SWMM 4.4h with SWMM 5.0.006 on twenty test examples, by Lewis A. Rossman of EPA's National Risk Management Research Laboratory, Cincinnati. A primary document: the engine's author reporting runs of both programs. Raw file: [raw/manuals/SWMM5_QA.md](../../raw/manuals/SWMM5_QA.md), about 12,000 words.

**How it was written.** A U.S. government report, in the public domain. The markdown is a conversion of the PDF; the equations are garbled and the result plots are not in `raw/`. Chapter 4 of the raw file runs 15 to 20, 24, 25, 27 to 34, 36 to 42, 45, 46 and 48 to 51: pages 21 to 23, 26, 35, 43, 44, 47 and 52 are missing, among them the descriptions of Examples EXTRAN3 and EXTRAN4 (Q92).

**Coverage: partial.** Read in full: Chapters 1 to 4, 7 and 8. Not yet read: Chapter 5 (Challenge Test Cases), Chapter 6 (User-Supplied Test Cases) and Appendices A and B.

**Claims worth keeping**
- SWMM was first developed in 1971. Its last major update before SWMM 5 was Version 4.4 (Huber and Dickinson, 1992), distributed from an Oregon State University web site.
- In 2002 EPA's Water Supply and Water Resources Division partnered with CDM to rewrite SWMM. SWMM 5 has a computational engine in C and a Windows interface in Delphi. A QA program (Schade, 2002) was set up to make its results compatible with SWMM 4.4. "The new SWMM 5 software was released to the public in October of 2004."
- Extran was "the most numerically challenging sub-model" to carry over. SWMM 5 did not copy it line for line; it restructured the code and "employed a slightly modified computational scheme with the intent of producing more numerically stable solutions in less time".
- SWMM 4 solves each step explicitly, a half step then a full step. SWMM 5 uses successive approximations with under-relaxation: relaxation factor 0.5, convergence tolerance 0.005 ft on nodal heads, and "limits the number of trials to four".
- Both programs average the end depths to get a conduit's area and hydraulic radius, and both cap the average velocity at 50 ft/sec so the friction term stays bounded.
- At a free-fall end, the depth in the conduit is the smaller of the critical and normal depths for the current flow.
- SWMM 4 iterates surcharged nodes at both the half step and the full step, with a user tolerance on the fractional flow difference. SWMM 5 folds the surcharge equation into its ordinary iterations and does not under-relax the head of a surcharged node.
- Both limit flow to normal flow at the upstream depth when either the water surface slope is less than the conduit slope or the Froude number exceeds 1.0; the user picks the criterion.
- Pumps, in both programs: a curve of flow against inlet node volume, inlet node depth or head difference, and the flow is limited to the inlet node's inflow when the curve flow would drain the node in the step.
- Orifices: SWMM 4 represents an orifice as an equivalent pipe whose length depends on the time step and the opening height and whose roughness depends on the discharge coefficient. SWMM 5 uses the orifice equation when the orifice is fully submerged and a modified weir equation when it is partly submerged. Both give the orifice a surface area at its end nodes based on the equivalent pipe length.
- Weirs are computed the same way in both, switching to the orifice equation when completely submerged, and add no surface area.
- Procedure: identical problems in both programs with equivalent options (Table 3.1), comparing runoff and routing flow balances, scatter plots of peak conduit flows, and time series at outfalls, devices and places where the peaks differed.
- Twenty examples in three groups: the ten Extran examples of the last SWMM 4.4 Users Manual (Roesner and others, 1992); five Challenge Test Cases "compiled by Robert E. Dickinson of CDM", circular conduits in series with flat slopes, pipe constrictions, steep drops, adverse slopes and inlet offsets; and five real systems from users, 59 to 273 conduits, each with a runoff component.
- Versions compared: SWMM 4.4h (July 4, 2005) and SWMM 5.0.006 (September 2005).
- EXTRAN1: seven circular conduits in two branches joining a pair of trapezoidal channels to a free outfall; inflows at three places; conduits 8040, 8060 and 1602 surcharge and node 80608 floods; 20-second step, 8 hours. "SWMM 4 and 5 produced essentially identical results."
- EXTRAN2: EXTRAN1 with node 10208 made a fixed-elevation outfall with a tide gate. Agreement "very good".
- EXTRAN5: node 82309 becomes a storage unit 40.5 ft high with a constant 800 sq ft of surface area, drained through a side outlet orifice to a new node 82308. Orifice flows agree "with the exception of a few points in time", though each program models the orifice differently; flow in conduit 1602 just downstream agrees almost perfectly.
- EXTRAN6: an off-line wet well 82310, fed from 82309 by conduit 8061 (300 ft of 4-ft pipe), pumped to 15009 by Type 1 pump 90011 whose curve tops out at 20 cfs at 1,200 cubic feet, which sets the well's capacity. Pump flows match. SWMM 4 restricts the inflow so the well never floods; SWMM 5 lets it flood, and the drop in SWMM 5's outflow volume "exactly equals the volume of flooding experienced at the pump's wet well".
- EXTRAN7: an in-line Type 2 pump from 82309 to 15009, rate against depth. SWMM 4 shows some flow instability when the inlet depth falls to zero; SWMM 5 is smoother. Continuity error: SWMM 4 -6.87 percent, SWMM 5 0.24 percent. SWMM 4 also holds a higher depth at 15009 after the hydrograph passes and an anomalously high depth at the start. Outfall flows, peaks and maximum elevations are "essentially identical".
- EXTRAN8: several cross-section shapes, including two irregular channels, 10081 and 10082. Triangular inflows of 1 hour base, peaks 15, 18 and 9 cfs at nodes 30001, 30004 and 30007, a constant 20 cfs at 30081, fixed outfall stage at 30083. A 1-hour hot start at 20 cfs, then 2 hours. "Perfect agreement."
- EXTRAN9: a variable-area storage unit with a side outlet orifice to a free outfall, triangular inflow of 5 hours base and peak 42.4 cfs (1.2 m3/s; conversion ours). "Essentially the same."
- EXTRAN10: five Type 3 pumps on one curve lifting water up a 50-foot hill between two storage units, each switched on and off at its own depths (2 and 6, 3 and 7, 4 and 8, 5 and 9, 6 and 10 ft for pumps 90002 to 90006), written as control rules for SWMM 5. Inflow ramps from 0 to 100 cfs in an hour and holds; 1-minute step, 5 hours. At 40 minutes the three running pumps give 25.7 cfs each in SWMM 5 and 23.0, 22.5 and 21.0 cfs in SWMM 4, "suggesting that something is not quite right" with SWMM 4.
- Chapter 7: the exceptions came from different assumptions for bottom orifices and Type 1 pump wet wells, and, in user cases, from SWMM 4 instabilities "even with as low a time step as 0.5 seconds", worst with odd-shaped storage and oscillating inertial flow. SWMM 5 ran stably at a much larger step in 50 percent of the Challenge and user examples. Conclusion: SWMM 5.0 "performs dynamic wave flow routing as good as or better than SWMM 4.4".
- Table 7.1, run times in seconds, SWMM 4 then SWMM 5: USER1 4 and 2; USER2 17 and 10; USER3 52 and 34; USER4 30 and 22; USER5 56 and 75.
- References: Huber and Dickinson, SWMM Version 4 User's Manual, EPA/600/3-88/001a, October 1992; Roesner, Aldrich and Dickinson, Extran Addendum, EPA/600/3-88/001b, October 1992.

**Checked at ingest.** Table 7.1 totals 159 s for SWMM 4 and 143 s for SWMM 5, so "slightly faster" holds in sum; SWMM 5 was slower on USER5. The Example 7 continuity error of SWMM 4, -6.87 percent, is the figure XROUTE prints on the same example twenty years later [S186](S186-st-venant-rosetta-stone-app-md-v2-6-2.md).

**Feeds:** [SWMM 4 against SWMM 5: the 2006 quality assurance tests](../concepts/swmm4-versus-swmm5-qa-2006.md), [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [Orifices](../concepts/orifices.md), [EXTRAN](../entities/extran.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md), [Lewis A. (Lew) Rossman](../entities/lew-rossman.md), [Open questions](../open-questions.md).

---
title: Pumps and pump curves
type: concept
updated: 2026-11-16
sources: [S60, S83, S131, S182, S183, S185, S186]
tags: [hydraulics, swmm5, pumps, primary-document]
reviewed: 11/16/2026
changed_after_review: "2026-11-16 (S180 to S187 ingest): one paragraph added at the end on the EXTRAN pump examples, the 2006 report and Registers 31 and 33 (S182, S183, S185, S186)"
---
SWMM 5 treats a pump as a link whose flow comes from a user-supplied pump curve [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Everything on this page is from sections 2.1.6 and 6.1 of the EPA hydraulics manual unless another source is cited.

**The five kinds**

| Kind | What sets the flow |
|---|---|
| Type1 | A series of constant flows over volume intervals at the inlet node [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Type2 | The same, over depth intervals at the inlet node [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Type3 | A centrifugal pump's characteristic curve, piecewise linear: flow from the head difference between the outlet and inlet nodes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Type4 | A variable speed in-line pump: flow varies continuously with inlet node depth [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Ideal | No curve. Flow equals the inflow to its inlet node. It must be the only outflow link from that node, and is meant for preliminary design [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |

**Reading the curve.** A Type1 or Type2 curve is searched step-wise for the first point whose volume or depth exceeds that at the inlet node, and the pump's flow is the flow of that point [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). A Type3 flow is interpolated between the two points that bracket the head difference; Type4 does the same with the inlet water level [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). The manual states that a pump's flow "is not allowed to be outside the minimum and maximum values defined by its pump curve and is not allowed to be negative" [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Pumps do not pass reverse flow [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Setting, startup and shutoff.** The curve flow is multiplied by the pump's speed setting, which control rules can change [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). A pump also has an initial on or off status and startup and shutoff depths at its inlet node [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Keeping the inlet node from going dry.** The adjusted flow is checked so that it does not take the inlet node's water level below 0 within the time step [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Inlet is a storage node: the pump cannot take more than the node's latest total inflow plus the volume it held at the start of the step, spread over the step (Equation 6-1) [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Inlet is not a storage node, dynamic wave: the node head at the end of the step is estimated with the current pumping rate (Equation 3-15a). "If this head is below the node's invert elevation then the pumping rate is set equal to the node's current inflow" [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

The manual does not say which rule holds when that inflow is larger than the highest flow on the curve. That is Q62 in [Open questions](../open-questions.md).

**Other computational details**
- A Type1 pump on a node that is not a storage unit gets a virtual wet well, whose volume varies linearly with depth up to the highest volume on the curve at full node depth [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Under [dynamic wave routing](dynamic-wave-routing.md) a pump adds no surface area to its end nodes, and no under-relaxation is applied to its flow [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- For a surcharged node, the flow derivative of a Type3 or Type4 pump is the negative of the slope of the curve segment in use. It is zero for the other kinds [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Power use is computed each step from head difference, flow and step length, without wire-to-water efficiency. The Pumping Summary reports it, with the percent of time each pump is on line and at the low or high end of its curve [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Where a pump may sit.** A pump's inlet is typically a storage node standing for the wet well. The exception the manual gives is an in-line booster pump in a force main under dynamic wave analysis [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Under [kinematic wave](kinematic-wave-and-steady-flow.md) analysis, pumping is possible only from storage nodes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**In Bob's apps.** People as Pollutants models every walkway, stair, escalator, gate, lift and train door of a transit station as a TYPE4 pump [S83](../sources/S83-people-as-pollutants-summary.md); see [People as Pollutants (app)](../entities/people-as-pollutants.md).

**Not in the sources yet.** The pump code itself (`link.c`, `dynwave.c`), and any run that tests the dry-node rule. The other structures are on [Orifices](orifices.md) and [Weirs and outlets](weirs-and-outlets.md).

**Added 15 November 2026: an editor for control rules.** [SWMM5 Control Rule Editor (app)](../entities/swmm5-control-rule-editor.md) reads and writes the `[CONTROLS]` section and checks rules for repeated priorities and missing conditions or actions, without running an engine [S131](../sources/S131-swmm5-control-rule-editor-replit-summary.md). Replit Agent wrote that summary; Bob has not read it (Q74).

**Added 16 November 2026, from the EXTRAN and QA ingest.** Bob's words for the two pumps of the EXTRAN test models: a Type 1 is "an off-line pump with a wet well where flow increases incrementally with available wet well volume" [S182](../sources/S182-li-extran-example-6-type-1-pump.md); a Type 2 is "an in-line pump where flow increases incrementally with inlet node depth" [S183](../sources/S183-li-extran-example-7-type-2-pump.md). EPA's 2006 report says SWMM 4 and SWMM 5 both limit a pump to its inlet's inflow when the curve flow would drain the node in a step, and that the two differ on Type 1 wet wells: SWMM 4 holds back the inflow so the well never floods, SWMM 5 lets it flood [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md). Twenty years later the Rosetta Stone measures XROUTE, SWMM 4.4H's solver, pumping 5 cfs from a dry junction on Example 7 (Register 31, Q95), and OpenSWMM 6 pumping above the top of its curve (Register 33). It quotes SWMM 5.2.4's dry-node rule as `if ( y <= 0.0 ) return Node[j].inflow;` in dynwave.c, which returns the inflow without the curve's limits; on its two decks 5.2.4 pumped at the curve [S186](../sources/S186-st-venant-rosetta-stone-app-md-v2-6-2.md). This bears on Q62. Test models: [The EXTRAN manual test models](extran-manual-test-models.md).

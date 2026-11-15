---
title: SWMM 5 network objects, boundary and initial conditions
type: concept
updated: 2026-11-15
sources: [S60]
tags: [hydraulics, swmm5, primary-document]
reviewed: 2026-11-15
---
SWMM 5 models the conveyance system as links joined at nodes. External flows enter at nodes, travel along links, fill and empty storage nodes, and leave at terminal nodes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). This page is Chapter 2 of the EPA hydraulics manual, a primary document, in digest [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Nodes**

| Node | What the manual says of it |
|---|---|
| Junction | Where links join: a manhole, a fitting, a confluence. Inputs are invert elevation, height to the ground, extra pressure head accepted before flooding, and ponded area when flooded [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Outfall | A terminal node that sets the downstream boundary: critical or normal depth in the connecting conduit, a fixed stage, a tide table by hour of day, or a time series of stage. It may have a flap gate [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Flow divider | Sends part of its inflow to a named link. No more than two conduits on its discharge side. Four kinds: cutoff, overflow, tabular, weir [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |
| Storage unit | The only node with storage volume and surface area, from a catch basin to a lake, described by surface area against height. It can lose water to evaporation and seepage. It is not allowed to pressurize [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) |

**Links**
- Conduit: inlet and outlet nodes, offsets, length, Manning's n, shape and size [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Offsets may be given as a height above the node invert or as an elevation; inside the program they are kept as elevations [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Slope is not an input. It is computed from the end elevations and the length [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). A slope of 0 is not allowed: the drop between the ends has a floor of 0.001 ft, and the user can set a larger minimum slope [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Optional on a conduit: a flap gate, entrance and exit loss coefficients, a seepage rate, and a culvert inlet code [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Pumps and flow regulators have their own pages: [Pumps and pump curves](pumps-and-pump-curves.md), [Orifices](orifices.md), [Weirs and outlets](weirs-and-outlets.md).

**Control rules.** Each pump and regulator has a setting: a pump's status or speed, the open fraction of an orifice, the crest height of a weir, the flow through an outlet. Rules change it during a run from conditions such as a node's water elevation, a link's flow, or the time [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Analysis methods.** [Dynamic wave](dynamic-wave-routing.md) solves the complete St. Venant equations and can be applied to any layout, at the price of small time steps [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). [Kinematic wave and steady flow](kinematic-wave-and-steady-flow.md) are the simpler choices, with limits on the network [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Boundary conditions.** Two kinds: the head at each outfall, needed only for dynamic wave analysis, and the external inflow at nodes [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Inflows come from subcatchment runoff, groundwater, RDII (see [RDII unit hydrographs (RTK)](rdii-unit-hydrographs.md)) and user-defined values [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). A user-defined inflow is a baseline value times a pattern factor, plus a scale factor times a time series value; the pattern combines hourly, daily and monthly multipliers [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Initial conditions.** By default every node head and link flow starts at 0, and the user may set initial heads at chosen nodes and initial flows in chosen conduits [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). An initial flow is taken as uniform steady flow, so the conduit starts at normal depth [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Under dynamic wave, a node that is neither storage nor outfall and has no initial head starts at the average elevation of the initial flow depths in the conduits that deliver flow into it [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Not in the sources yet.** Sections 1.2 to 1.5 of the same manual (the object model, Table 1-2, interpolation and units) are not yet read.

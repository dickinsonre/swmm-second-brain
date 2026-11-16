---
title: "How SWMM 5 is organized: objects, state and the time loop"
type: concept
updated: 2026-11-16
sources: [S60, S157]
tags: [swmm5, architecture, output, units, primary-document]
reviewed: no
---
Sections 1.2 to 1.5 of the EPA hydraulics manual, a primary document, in digest [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). Its figures are not in `raw/` and its two equations did not survive the conversion, so both are described in words.

**Four compartments.** Atmosphere (precipitation, pollutant deposition), Land Surface (evaporation, infiltration, runoff and pollutant loads), Sub-Surface (infiltration in, groundwater interflow out) and Conveyance (channels, pipes, pumps, regulators, storage and treatment). A model need not have all four: it can be the Conveyance compartment alone, fed by predefined hydrographs and pollutographs [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**Objects (Table 1-2)** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)

| Category | Objects |
|---|---|
| Hydrology | Rain Gage, Subcatchment, Aquifer, Snow Pack, Unit Hydrograph (the RDII response per unit of instantaneous rainfall) |
| Hydraulics | Junction, Outfall, Divider, Storage Unit, Conduit, Pump, Regulator (weir, orifice or outlet) |
| Water quality | Pollutant, Land Use |
| Treatment | LID Control, Treatment Function |
| Data | Curve, Time Series, Time Pattern, Control Rules |

The hydraulic objects are on [SWMM 5 network objects, boundary and initial conditions](swmm5-network-objects.md); the unit hydrograph on [RDII unit hydrographs (RTK)](rdii-unit-hydrographs.md).

**A discrete time model.** SWMM is "a distributed discrete time simulation model". At each step it computes the new state from the previous state, that step's inputs and the constant parameters (Equation 1-1), and the reported outputs from the new state and the parameters (Equation 1-2) [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**The state is small.** Table 1-3 lists the state variables; the manual calls the number "surprisingly small" and says all other quantities can be computed from them, the inputs and the parameters [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). By our count there are 21: runoff depth on a subcatchment; six infiltration variables (only some used, by method); two groundwater (unsaturated moisture, saturated depth); four snow pack; three for flow routing (node head H, link flow Q, link area A inferred from Q); five water quality. Inputs include weather, external inflows, dry weather flows, outfall stages and control settings. SWMM has over 150 user-supplied constants; a subcatchment's groundwater alone takes 14 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).

**The time loop (Figure 1-5)** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)
1. Read the input file and initialize the state, the simulation time T, the runoff time and the reporting time.
2. Set T1, the end of the current routing step.
3. While the runoff time is before T1, compute runoff (precipitation, evaporation, snowmelt, infiltration, groundwater, overland flow, buildup and washoff) and advance the runoff time.
4. Route the inflows through the conveyance system from T to T1.
5. If a reporting time falls between T and T1, interpolate the results at that time from those at T and T1, save them, and advance the reporting time.
6. Set T to T1 and repeat until the end of the run.

**Interpolation, with one exception.** Values between recorded or computed times are interpolated linearly; a reported flow comes from the computed flows on either side of the report time. Precipitation and infiltration rates are not: they hold constant through a runoff step, and a reported rainfall intensity is the value at the start of the runoff step [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md). That agrees with what the LSTM + SWMM5 app measured: a .out holds, at each report time, the rain of the interval that starts there [S157](../sources/S157-lstm-swmm5-summary.md). See [Reading SWMM output](reading-swmm-output.md).

**Units (Table 1-4), US customary** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md): subcatchment area in acres; storage surface area in sq ft; depth, elevation, head, length and width in ft; depression storage and rainfall volume in inches; rainfall intensity, infiltration rate and hydraulic conductivity in in/hr; evaporation in in/day; flow in cfs, gpm or mgd; storage volume in cu ft; velocity in ft/s; temperature in °F; wind in mph. Manning's n is in seconds per meter^(1/3) in both unit systems.

**Related.** [Where a surrogate of SWMM breaks](surrogates-hidden-state-missing-forcing.md): the hidden states that defeat a rain-driven surrogate.

# Three small ICM 2D cases isolate rain, exchange, and barrier alignment

**Status:** seed
**Date:** 2026-11-16

## The idea

Use three rerunnable cases in the ICM Lab Canon. Each has a short question and a check that can be read from numeric outputs. Record the ICM build, network commit, terrain, mesh, event, controls, and outputs for each run.

## Proof / from scratch

### 1. Closed rainfall box

Use a flat, initially dry 100 ft by 100 ft 2D zone with Vertical Wall boundaries. Apply 1.00 in of direct rainfall over one hour at 100 percent, with no other inputs, infiltration, or evaporation. Leave `Ignore rain falling on dry elements` unchecked. Verify the meshed area and the applied rain depth.

The analytical expectation for exactly 10,000 ft² is 833.33 ft³ of stored water, rounded to two decimal places. The mean stored depth is 1.00 in. Record the final storage and the volume residual against the actual meshed area. Save the rainfall input and final volume result.

### 2. Reversing manhole

Connect one 1D node to a small surface depression. Raise the sewer head above the opening and then lower it while water remains on the surface. Read the signed exchange hydrograph and plot levels on both sides. Verify the exchange starts and reverses under the head differences and opening relation set for the case.

### 3. Embankment with a gap

Place a single opening in a raised feature and apply a short pulse on one side. Compare the mesh configurations in the subgrid note. Read a transect through the gap and a separate transect across an intact part of the crest. Record arrival on the far side, volume along each route, and the conditions at which overtopping begins.

These are test designs. Set the acceptance criteria before running and add the measured outputs to each run record.

## Links

- [Autodesk 2D zone rainfall settings](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-111E1710-4BA5-4F49-8596-E5B00C4F6CE6.htm)
- [Autodesk 2D Parameters dialog](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-251BAAB1-AC3C-4F9D-8EE4-585FFBF51CF3.htm)
- [1D–2D node exchange](./icm-1d-2d-node-exchange.md)
- [2D volume balance](./icm-2d-volume-balance.md)
- [Subgrid sampling and barrier alignment](./icm-2d-subgrid-sampling.md)

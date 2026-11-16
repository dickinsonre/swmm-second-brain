# Test ICM 2D time stepping with a fixed mesh and event

**Status:** seed
**Date:** 2026-11-16

## The idea

Record the run timestep, 1D–2D coupling options, 2D stability control, and results reporting interval separately. In the InfoWorks 2D Parameters dialog, Timestep Stability Control sets the CFL bound used by the 2D engine for internal stepping. The same dialog documents the option to link 1D and 2D calculations at minor timesteps and the thresholds for depth and momentum.

## Proof / from scratch

1. Choose one case with a wetting front, bank spill, or reversing manhole flow. Save the mesh, run settings, warnings, and results locations as a baseline.
2. With the mesh and event fixed, repeat with a smaller run timestep and the same reporting interval. If the issue is a bank oscillation, test the minor-timestep coupling option in a separate run.
3. At fixed locations, compare arrival time, peak stage and flow, flow reversal, volume balance, and elapsed run time. Look at the whole hydrograph around the reported instability.
4. Test a mesh change in a separate comparison. Compare like-for-like event and reporting settings again. Record whether the numerical result and the warning changed together.

Include the depth threshold, momentum threshold, and any velocity limiting settings in the run record. Keep them visible when investigating a shallow-flow map or an apparent dry interruption.

## Links

- [Autodesk 2D Parameters dialog](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-251BAAB1-AC3C-4F9D-8EE4-585FFBF51CF3.htm)
- [Autodesk subgrid timestep method and depth tolerances](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-4DA1AD27-C00F-4232-AF35-F7A9579FCC15.htm)
- [1D–2D node exchange](./icm-1d-2d-node-exchange.md)
- [2D volume balance](./icm-2d-volume-balance.md)

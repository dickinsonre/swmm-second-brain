# A two-pipe benchmark can separate engine differences from conversion differences

**Status:** seed
**Date:** 2026-11-16

## The idea

Use one model small enough to inspect in every environment. Establish the EPA SWMM 5.2.4 and `swmm5-ruby` baseline with the same input. Then run the ICM SWMM and ICM InfoWorks versions with their conversion records. The Ruby port's published gate documents the EPA build and its byte-comparison criteria.

## Proof / from scratch

The proposed fixture has two junctions and a free outfall with invert elevations of 100, 99, and 98 ft. Set each junction rim 5 ft above its invert. Use two 200 ft circular conduits, each 12 in in diameter, with Manning's `n` of 0.013 and zero offsets. Start dry and simulate for one hour. Apply an inflow at the first junction and save results on a 1 min reporting grid.

| Minutes from start | Inflow (ft³/s) |
|---:|---:|
| 0 | 0.0 |
| 10 | 0.5 |
| 20 | 1.0 |
| 30 | 0.0 |
| 60 | 0.0 |

1. Run the same `.inp` in the pinned EPA and Ruby engines. Compare `.out` and `.rpt` using the gate's criteria and preserve both builds in the record.
2. Import and run in ICM SWMM. Keep ICM's simulation log and the actual engine input when available. Check mapped offsets, inflow interpolation, and output intervals.
3. Map the model to ICM InfoWorks. Check the conduit geometry, boundary condition, initial state, and inflow independently. Record hydraulic step settings for each engine.
4. Compare outfall peak flow, peak time, volume, and continuity error. Plot outfall flow and upstream level on the common time grid and agree on acceptable differences before running.

Add the input, build identifiers, mapping record, and outputs to the test evidence when the runs are available. This fixture is a test design awaiting runs.

## Links

- [EPA SWMM 5.2.4 software and manuals](https://www.epa.gov/water-research/storm-water-management-model-swmm)
- [Ruby SWMM5 port and comparison gate](https://github.com/SWMMBobSWMM6/swmm5-ruby)
- [Autodesk note on ICM SWMM engine input and output files](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Location-of-the-Engine-INP-and-Output-files-in-ICM-SWMM.html)
- [Second brain comparison questions, including Q16](https://github.com/dickinsonre/swmm-second-brain/blob/main/wiki/open-questions.md)
- [SWMM conversion checks](./swmm-inp-conversion-qa.md)

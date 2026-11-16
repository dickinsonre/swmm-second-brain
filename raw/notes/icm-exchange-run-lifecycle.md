# An Exchange run ends when the intended results can be opened

**Status:** seed
**Date:** 2026-11-16

## The idea

Record the ICM run definition, submitted job, simulation status, and exported results in one place. Autodesk documents Exchange methods to connect to the agent, launch simulations, and wait on job IDs. The simulation also carries a status and, on success, a substatus. These values help explain why a launch produced an incomplete or missing CSV.

## Proof / from scratch

Use one existing run with one scenario and one known output node.

1. Record the ICM build, network commit, scenario, event, run and simulation IDs, and reporting interval.
2. Connect to the local agent with `WSApplication.connect_local_agent` and check that the connection succeeds. Submit the intended simulation via `WSApplication.launch_sims`. Record the returned job ID and result storage settings.
3. Wait for that ID with `WSApplication.wait_for_jobs`. Its timeout is in milliseconds. Log a timeout and retain the job ID so the existing job can be checked before any resubmission.
4. Read the simulation's `status` and, when available, `success_substatus`. Capture the run log or warning if trouble occurs.
5. Open the simulation results. Confirm that the expected node, variable, and reporting window exist. Export to CSV with object IDs, timestamps, units, and the run metadata.

Check the CSV values and timestep count against the same simulation in GeoPlan. Record the statuses and observed Job Control behavior on the build tested. This procedure awaits an ICM run.

## Links

- [Autodesk WSApplication reference](https://help.autodesk.com/view/IWICMS/2027/ENU/?guid=Innovyze_Exchange_Classes_ICM_wsapplication_html)
- [Autodesk WSSimObject reference](https://help.autodesk.com/view/IWICMS/2027/ENU/?guid=Innovyze_Exchange_Classes_ICM_wssimobject_html)
- [ICM results field crosswalk](./icm-results-field-crosswalk.md)

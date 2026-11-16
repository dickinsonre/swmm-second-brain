---
title: "ICM Ruby: UI scripts and Exchange scripts"
type: concept
updated: 2026-11-16
sources: [S159, S160, S161, S152, S166, S179]
tags: [icm, ruby, exchange]
reviewed: no
---
InfoWorks ICM runs Ruby in two places: inside the desktop interface, against the network open in GeoPlan, and in ICM Exchange, the command-line runner. Three notes Bob supplied on 16 November 2026 set out how a script differs between them and how to test one. ChatGPT drafted them from Autodesk Help [S179](../sources/S179-note-icm-notes-drafted-by-chatgpt.md), so they are AI-written; their Autodesk facts are reported from Autodesk's help and not checked here, and nothing in them has been run (Q90).

**Two ways in** [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md)

| | Desktop interface | ICM Exchange |
|---|---|---|
| Network | `WSApplication.current_network`, the focused GeoPlan | opened by the script from a database path and a network scripting path |
| Opening | already open | `WSApplication.open(database_path, false)`, then `database.model_object(network_path).open`; `false` skips the database upgrade |
| Started from | the ICM interface | `ICMExchange.exe <script> [-login] <arguments>` in PowerShell, in the ICM install folder |
| License | | Autodesk documents Exchange for Ultimate licenses |

`WSApplication.ui?` tells a script which side it is on. The proposed check: count the nodes of one saved base network both ways and get the same number, using `hw_node` for an InfoWorks network and `sw_node` for an ICM SWMM one [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md). Table names are on [ICM network tables and result fields](icm-tables-and-result-fields.md).

**The Ruby inside ICM changed.** Autodesk documents Ruby 3.4.6 for UI and Exchange scripting from ICM 2027.0, replacing Ruby 2.4.0. A script that requires a library that changed or is gone fails with `LoadError` [S160](../sources/S160-note-icm-ruby-version-compatibility.md). The note's smoke test prints the ICM build, `RUBY_VERSION` and `WSApplication.ui?`, then loads each of the script's own `require` lines before touching the model, and keeps the ICM build and Ruby version beside every test result [S160](../sources/S160-note-icm-ruby-version-compatibility.md).

**Running a simulation from Exchange** [S161](../sources/S161-note-icm-exchange-run-lifecycle.md)
1. Record the ICM build, network commit, scenario, event, run and simulation IDs, and reporting interval.
2. Connect with `WSApplication.connect_local_agent`.
3. Submit with `WSApplication.launch_sims` and keep the job ID it returns.
4. Wait with `WSApplication.wait_for_jobs`; its timeout is in milliseconds. On a timeout, log it and keep the job ID, so the job can be checked before anything is resubmitted.
5. Read the simulation's `status` and, on success, `success_substatus`.
6. Open the results, confirm the expected node, variable and reporting window, and export a CSV with IDs, timestamps, units and run metadata. Check it against the same run in GeoPlan.

The note's point: a run is finished when the intended results open, not when the launch returns [S161](../sources/S161-note-icm-exchange-run-lifecycle.md).

**Why Exchange.** Bob deleted his web app that ran visitors' Ruby, and said ICM Exchange is the better way anyway [S152](../sources/S152-note-ruby-script-runner-deleted.md). See [InfoWorks ICM Ruby Script Runner (app)](../entities/icm-ruby-script-runner.md).

**Related.** [InfoWorks ICM](../entities/infoworks-icm.md). Bob's queued articles on Ruby and SQL for ICM (queue item 6 in the index) are the next source for this page.

**Relations**

| Subject | Relation | Object | Note | Source |
|---|---|---|---|---|
| `ruby:3.4.6`, `ruby:2.4.0` | `is_a` | `sb:RubyRuntime` |  | [S160](../sources/S160-note-icm-ruby-version-compatibility.md) |
| `ruby:3.4.6` | `available_in` | `icm:2027.0` | `verification: documented` for UI and Exchange scripting | [S160](../sources/S160-note-icm-ruby-version-compatibility.md) |
| `ruby:3.4.6` | `replaces` | `ruby:2.4.0` | `as_of: ICM 2027.0` `verification: documented` a script that requires a library that changed or is gone fails with LoadError | [S160](../sources/S160-note-icm-ruby-version-compatibility.md) |
| `icm:2027.0` | `is_a` | `sb:Release` |  | [S160](../sources/S160-note-icm-ruby-version-compatibility.md) |
| `icm:2027.0` | `part_of` | `icm:ICM` |  | [S160](../sources/S160-note-icm-ruby-version-compatibility.md) |
| `icm:ICMExchange` | `is_a` | `sb:Program` | the command-line runner | [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md) |
| `icm:ICMExchange` | `part_of` | `icm:ICM` |  | [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md) |
| `icm:ICMExchange` | `requires` | `icm:UltimateLicense` | `verification: documented` | [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md) |
| `icm:UltimateLicense` | `is_a` | `sb:License` |  | [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md) |
| `icm:WSApplication.current_network`, `icm:WSApplication.open` | `is_a` | `sb:ApiMethod` |  | [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md) |
| `icm:WSApplication.current_network` | `part_of` | `icm:UIScripting` | returns the network open in the focused GeoPlan | [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md) |
| `icm:WSApplication.open` | `part_of` | `icm:ICMExchange` | a second argument of false skips the database upgrade | [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md) |
| `icm:WSApplication.connect_local_agent`, `icm:WSApplication.launch_sims`, `icm:WSApplication.wait_for_jobs` | `is_a` | `sb:ApiMethod` |  | [S161](../sources/S161-note-icm-exchange-run-lifecycle.md) |
| `icm:WSApplication.connect_local_agent`, `icm:WSApplication.launch_sims`, `icm:WSApplication.wait_for_jobs` | `part_of` | `icm:ICMExchange` |  | [S161](../sources/S161-note-icm-exchange-run-lifecycle.md) |
| `icm:WSApplication.wait_for_jobs` | `has_parameter` | `icm:JobTimeout` | `verification: documented` in milliseconds | [S161](../sources/S161-note-icm-exchange-run-lifecycle.md) |
| `icm:JobTimeout` | `is_a` | `sb:Parameter` |  | [S161](../sources/S161-note-icm-exchange-run-lifecycle.md) |

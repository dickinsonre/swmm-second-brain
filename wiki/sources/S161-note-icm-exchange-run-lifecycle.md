---
title: "S161: note, an Exchange run ends when the intended results can be opened"
type: source
raw: raw/notes/icm-exchange-run-lifecycle.md
kind: note
author: Robert Dickinson
published: 2026-11-16
ingested: 2026-11-16
tags: [icm, ruby, exchange, simulation, note]
reviewed: no
---
**What it is.** A note on launching an ICM simulation from Exchange and knowing when it has finished. Raw file: [raw/notes/icm-exchange-run-lifecycle.md](../../raw/notes/icm-exchange-run-lifecycle.md).

**How it was written.** One of seven notes Bob supplied on 16 November 2026 in `ICM-Ruby-SWMM-Markdown.zip`, copied into `raw/notes/` unchanged. It is on the note template, dated 2026-11-16, status seed. The note does not name its author; Bob says the ICM notes come from the GPT plugin for Autodesk [S166](S166-note-icm-notes-from-gpt-plugin.md), so it is AI-written text (that his statement covers this set of seven is Claude's reading, Q89). Its facts about ICM come from Autodesk's online help, linked in the note, and were not checked here against ICM or the help pages. Its procedure says it awaits a run in ICM: nothing in it has been run.

**Claims worth keeping** (as the note states them; AI-written, not checked against ICM)
- Autodesk documents Exchange methods to connect to the agent (`WSApplication.connect_local_agent`), launch simulations (`WSApplication.launch_sims`, which returns a job ID) and wait on job IDs (`WSApplication.wait_for_jobs`, whose timeout is in milliseconds).
- A simulation carries a `status` and, on success, a `success_substatus`; these help explain an incomplete or missing CSV.
- On a timeout, log it and keep the job ID, so the existing job can be checked before any resubmission.
- Record the ICM build, network commit, scenario, event, run and simulation IDs and reporting interval; then open the results, confirm the expected node, variable and reporting window exist, and export to CSV with object IDs, timestamps, units and run metadata.
- Check the CSV values and timestep count against the same simulation in GeoPlan.

**Feeds:** [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md).

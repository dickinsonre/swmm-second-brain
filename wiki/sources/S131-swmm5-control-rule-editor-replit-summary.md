---
title: "S131: SWMM5 Control Rule Editor, summary written by Replit Agent (v0.1.0)"
type: source
raw: raw/apps/hydro-control-v0.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, control-rules, inp-files]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 Control Rule Editor, version 0.1.0: a browser editor for SWMM5 control rules that imports JSON, SWMM control text or the `[CONTROLS]` section of an INP file and writes the rules back out as JSON and SWMM5 text. It is one of Bob's Replit apps, at `hydro-control.replit.app`. Raw file: [raw/apps/hydro-control-v0.1.0.md](../../raw/apps/hydro-control-v0.1.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the source and documentation name no AI tool as having built it. The copy here was read out of the editor of the Replit project named SWMM5ControlRules on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It prepares rule data and does not run a SWMM simulation. There is no hydraulic solver. `engines: none`.
- It shows each rule's conditions, actions and priority. The exporter optionally sorts rules by priority and formats them as `[CONTROLS]` text.
- The parser reads supported control statements with regular expressions; `parseFromINP` extracts the `[CONTROLS]` section first.
- Its validation checks for repeated priorities, rules without conditions or THEN actions, and identical THEN/ELSE values for a matching object and attribute. It displays warnings and does not validate rules against a SWMM engine.
- Contents: three bundled example rules, six rule templates, thirteen attribute tooltip descriptions and eight object types in the attribute map.
- Inputs are pasted text and uploaded `.inp`, `.json` and `.txt` files. Outputs are `swmm5_controls.txt` and `swmm5_rules.json`.
- Rule data is held in browser JavaScript memory; reloading the page restores the bundled examples. The app accepts rule values as entered and does not convert units.
- The stack is Python 3.11 with Flask and Gunicorn, and one route, `GET /`.
- `python -m unittest discover -v`: zero tests discovered. `python -m py_compile app.py main.py` passed. `GET /` returned HTTP 200.
- The project has no license file. Git history records commits under `robertdickinson`.

**Limits it states.** The app was not tested with EPA SWMM or another engine, and exported rules were not validated by a simulation. Importing real INP files, copying and downloading were not individually tested. Mobile behavior and accessibility were not reviewed.

**Checked at ingest.** The site is hydro-control and the Replit project SWMM5ControlRules (Q77). Version 0.1.0 comes from `pyproject.toml`; the `date:` is the day of the summary, and the change list runs from 20 August 2025 to 22 February 2026 (Q75). It was brought over after the seventeen on the concept page and is added there as an eighteenth.

**Feeds:** [SWMM5 Control Rule Editor (app)](../entities/swmm5-control-rule-editor.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [SWMM5 .inp File Viewer (app)](../entities/swmm5-inp-file-viewer.md).

---
title: SWMM5 Control Rule Editor (app)
type: entity
updated: 2026-11-15
sources: [S131]
tags: [apps, replit, swmm5, control-rules, inp-files]
reviewed: no
---
Bob's Replit app SWMM5 Control Rule Editor: a browser editor for SWMM5 control rules that imports JSON, SWMM control text or the `[CONTROLS]` section of an INP file and writes the rules back out as JSON and SWMM5 text. Version 0.1.0, at `hydro-control.replit.app` [S131](../sources/S131-swmm5-control-rule-editor-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S131](../sources/S131-swmm5-control-rule-editor-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S131](../sources/S131-swmm5-control-rule-editor-replit-summary.md)
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

**What it does not show.** The app was not tested with EPA SWMM or another engine, and exported rules were not validated by a simulation. Importing real INP files, copying and downloading were not individually tested. Mobile behavior and accessibility were not reviewed. [S131](../sources/S131-swmm5-control-rule-editor-replit-summary.md)

**Noted at ingest.** The site is hydro-control and the Replit project SWMM5ControlRules (Q77). Version 0.1.0 comes from `pyproject.toml`; the `date:` is the day of the summary, and the change list runs from 20 August 2025 to 22 February 2026 (Q75). It was brought over after the seventeen on the concept page and is added there as an eighteenth.

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [SWMM5 .inp File Viewer (app)](swmm5-inp-file-viewer.md).

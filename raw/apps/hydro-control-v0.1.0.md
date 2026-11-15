---
name: SWMM5 Control Rule Editor
file: hydro-control
version: 0.1.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://hydro-control.replit.app, repo: none}
engines: none
stack: Python 3.11, Flask, Jinja2, HTML, CSS, JavaScript, Tailwind CSS CDN, Google Fonts Inter, Gunicorn; no database used
units: both
ai_use: Project source does not identify AI tools used to build the app; this summary was written by Replit Agent.
---

# SWMM5 Control Rule Editor: Create and exchange SWMM5 control rules

## What it does

The app lets stormwater model users create and edit SWMM5 control rules in a browser. It shows each rule's conditions, actions, and priority. It imports JSON, SWMM control text, or an INP file's `[CONTROLS]` section. It produces editable JSON and SWMM5 control text that users can copy or download. The app prepares rule data; it does not run a SWMM simulation.

## How it computes

There is no hydraulic solver or simulation engine.

1. `templates/index.html`, `rulesData` (lines 596–602), holds the initial rule objects in browser memory. UI event handlers edit those objects and re-render the rule list (`renderAllRules`, lines 802–904).
2. `validateRules` (lines 652–686) checks for repeated priorities, rules without conditions or THEN actions, and identical THEN/ELSE values for a matching object and attribute. It displays warnings; it does not validate rules against a SWMM engine.
3. `SWMM5Exporter.exportToSWMM5` (lines 246–310) optionally sorts rules by priority, then formats rules, conditions, actions, and priorities as `[CONTROLS]` text. `formatCondition` and `formatAction` (lines 312–329) format each clause. It does not calculate hydraulic values.
4. `SWMM5Parser.parse` (lines 393–499) reads supported control statements using regular expressions and builds rule objects. `parseValue` and `parseActionValue` (lines 501–519) convert numeric and status values. `parseFromINP` (lines 521–526) extracts the `[CONTROLS]` section before parsing.
5. `SWMM5Templates` (lines 556–591) holds reusable example rules. The editor uses browser JavaScript for edits, parsing, validation, and formatting; no engine is called.

## Inputs and outputs

- Inputs: pasted SWMM5 control text and JSON; uploaded `.inp`, `.json`, and `.txt` files (`templates/index.html`, lines 167–215).
- Outputs: formatted `[CONTROLS]` text and JSON in the page; copy-to-clipboard controls; downloadable `swmm5_controls.txt` and `swmm5_rules.json` files (`templates/index.html`, lines 362–385 and 688–702).
- Routes: `GET /` renders the editor (`app.py`, lines 8–11). No other application routes are defined in `app.py`.
- Storage: rule data is held in browser JavaScript memory (`templates/index.html`, lines 596–602). No database calls or server-side rule storage were found in the app code. Reloading the page restores the bundled examples.
- Units: tooltips mention both US customary and SI examples (`templates/index.html`, lines 532–546). The app accepts rule values as entered and does not convert units.

## Contents

- One editor page, served at `/` (`app.py`, lines 8–11; `templates/index.html`).
- Three bundled example rules (`templates/index.html`, lines 596–602).
- Six rule templates (`templates/index.html`, lines 556–564).
- Thirteen attribute tooltip descriptions (`templates/index.html`, lines 532–547).
- Eight object types in the attribute map (`templates/index.html`, lines 607–616).

## Checks

- `python -m unittest discover -v`: zero tests discovered; zero passed and zero failed. The repository contains no test files.
- `python -m py_compile app.py main.py`: passed.
- Flask test client request to `/`: HTTP 200; HTML title, editor heading, and SWMM5 output tab were present.
- Page load: `GET /` returned HTTP 200. The browser preview rendered the editor. The console reported the Tailwind CDN production-use warning and a missing `/favicon.ico` response (HTTP 404).
- Human review: none recorded.

## What this does not show

1. No automated test suite was found; import, export, validation, and editing behavior were not covered by automated tests.
2. The app was not tested with EPA SWMM or another simulation engine. Exported rules were not validated by a simulation.
3. Browser interaction paths, including importing real INP files, copying, and downloading, were not individually tested.
4. The missing `/favicon.ico` response was observed and not investigated further.
5. The source does not identify which AI tools, if any, contributed to building the app, or describe Robert Dickinson's individual implementation work. Git history records commits under `robertdickinson`.
6. The project has no license file. License terms for dependencies and external font/style services were not checked.
7. Mobile behavior and accessibility were not separately reviewed.

## How to reproduce

- Project metadata sets the app version to `0.1.0` and requires Python `>=3.11` (`pyproject.toml`, lines 3–5).
- Install the dependencies declared in `pyproject.toml`.
- Run the app with `gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app` (`.replit`, line 29).
- Run the discovered-test check with `python -m unittest discover -v`. No tests are currently present.
- Run the Python syntax check with `python -m py_compile app.py main.py`.

## Credits and licenses

- Author: Robert Dickinson, as specified for this summary. Git history records commits under `robertdickinson`.
- Framework and packages declared in `pyproject.toml`: Flask, Flask-SQLAlchemy, Gunicorn, psycopg2-binary, and email-validator. Flask-SQLAlchemy, psycopg2-binary, and email-validator were not found in application code usage.
- Frontend services named in the source: Tailwind CSS CDN and Google Fonts (Inter).
- SWMM5 is the target control-rule format. No simulation engine is included.
- Project license: no license stated. Third-party license terms were not checked.

## AI use

The project source and documentation do not name an AI tool as having built the app or specify which implementation work Robert Dickinson performed. Git history attributes recorded commits to `robertdickinson`. Replit Agent wrote this technical summary.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-02-22: Published the app.
- 2026-02-22: Added a project handover document.
- 2026-02-05: Saved progress.
- 2026-02-05: Improved editor styling and descriptions.
- 2026-02-05: Published the app.
- 2026-02-05: Saved progress.
- 2026-02-05: Added import functionality and SWMM5 export.
- 2026-02-05: Published the app.
- 2025-08-20: Created the interactive editor with real-time JSON output.
- 2025-08-20: Created the initial project.

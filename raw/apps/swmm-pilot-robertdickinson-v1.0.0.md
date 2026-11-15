---
name: Camel_SWMM
file: swmm-pilot-robertdickinson
version: 1.0.0
date: 2025-08-18
author: Robert Dickinson
links: {replit: https://swmm-pilot-robertdickinson.replit.app, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: swmm-toolkit 0.17.0, commit: not recorded, license: not stated for the engine}
stack: Python 3.11, Flask, Flask-CORS, Tkinter, swmm-toolkit, PySWMM, Matplotlib, NumPy, pandas, Plotly, ReportLab, OpenAI API
units: US customary
ai_use: OpenAI API with gpt-5 for optional report review, model drafting, what-if answers, and anomaly analysis.
---

# Camel_SWMM: Run and inspect EPA SWMM stormwater models

## What it does

The web status and health responses identify the application as version `1.0.0` (`web_app.py:398-410,442-450`). Camel_SWMM lets users manage SWMM input files, validate models, run the EPA SWMM engine, and inspect generated results. It presents simulation summaries, charts, comparisons, and reports through a Flask web interface; `main.py` also provides a Tkinter desktop startup path. Optional AI features review reports, draft model files, answer what-if questions, and analyze model or report content (`ai_features.py:179-329`).

## How it computes

1. The file routes resolve model paths and can validate `.inp` contents with `utils.inp_validator.validate_inp_content` (`web_app.py:1932-1958`).
2. `web_app.py::run_simulation` calls `core.swmm_integration.SWMMIntegration.run_simulation`. This calls `swmm.toolkit.solver.swmm_run(input, report, output)` and checks the resulting `.rpt` and `.out` files (`web_app.py:681-805`; `core/swmm_integration.py:130-196`).
3. `SWMMIntegration.run_simulation` parses the report's errors, warnings, summary, and continuity values. It reports the largest absolute parsed continuity error (`core/swmm_integration.py:189-216`).
4. `core.data_processor.SWMMDataProcessor` reads reports and binary output, extracts time series, and calculates statistics and flow-duration curves (`core/data_processor.py:20,56-206`).
5. `visualization.charts` creates plots. `reports.generator.ReportGenerator.generate_simulation_report` produces simulation reports. AI feature functions call the OpenAI API and return generated analysis; they do not replace the SWMM simulation (`visualization/charts.py`; `reports/generator.py`; `ai_features.py:179-329`).

## Inputs and outputs

- Model input: SWMM `.inp` files. Other upload and parsing code handles `.rpt`, `.out`, and text content (`web_app.py::UPLOAD_SIZE_LIMITS`; `web_app.py:1932-1958`; `ai_features.py:179-329`).
- Web pages: `/` and `/docs` (`web_app.py:358-386`).
- API endpoints: `/api/status`, `/api/engine/status`, `/api/health`, `/api/files`, `/api/files/upload`, `/api/upload`, `/api/simulation/run`, `/api/config`, `/api/themes`, `/api/themes/<theme_name>`, `/api/languages`, `/api/translations/<lang_code>`, `/api/settings`, `/api/demo/results`, `/api/files/parse-network`, `/api/files/content`, `/api/files/save`, `/api/ai/consent`, `/api/runs/save`, `/api/runs/list`, `/api/runs/compare`, `/api/runs/history`, `/api/runs/history/add`, `/api/runs/history/note`, `/api/visualization/generate`, `/api/reports/generate`, `/api/reports/download`, `/api/files/download`, `/api/files/validate`, `/api/files/analyze`, `/api/files/duplicate`, `/api/files/delete`, `/api/ai/review`, `/api/ai/build-model`, `/api/ai/what-if`, and `/api/ai/anomaly` (`web_app.py:358-2320`).
- Simulation results use `.rpt` and `.out` files. Report downloads are PDF when ReportLab is available and text otherwise. Result downloads can be ZIP files (`core/swmm_integration.py:161-217`; `web_app.py:1824-1929`).
- Models are stored in the configured projects directory, defaulting to `~/SWMM_Projects` (`utils/config.py:18-28,194-199`). Settings use `~/.camel_swmm_config.json` (`utils/config.py:13-20`). Saved runs, run history, and latest results are JSON files in `~/.camel_swmm/runs/`; in-memory stores are also used (`web_app.py:59-107`).
- No database dependency or database connection is declared in `pyproject.toml` or the inspected application source.

## Contents

- Web pages: 2 HTML routes, `/` and `/docs` (`web_app.py:358-386`; both loaded in the current preview).
- Example models: 5 `.inp` files in `SWMM_Projects/`, counted with `Path('SWMM_Projects').glob('*.inp')`.
- Translation files: 10 JSON files in `translations/`, counted with `Path('translations').glob('*.json')`.
- There is no bundled question bank. `/api/ai/what-if` accepts a user-provided question (`web_app.py:2257-2277`).

## Checks

- Tests: 29 passed, 0 failed. Command: `PYTHONDONTWRITEBYTECODE=1 python -m pytest -p no:cacheprovider -q`.
- Main pages: preview `GET /` returned HTTP 200. Preview `GET /docs` returned HTTP 200. The home-page browser log reported a missing resource; a follow-up request identified it as `GET /favicon.ico`, HTTP 404.
- Engine startup: the running application reported EPA SWMM version `5.2.4` in its startup log.
- Human review: none recorded.

## What this does not show

1. The published production pages and production API were not loaded. The URL comes from current deployment metadata; the page checks used the local preview.
2. Calls to the OpenAI API were not tested. Generated AI content was not checked for technical correctness.
3. The Tkinter desktop interface was not started or checked.
4. The five bundled example models use `FLOW_UNITS CFS`. Non-CFS input behavior was not checked (`SWMM_Projects/*.inp`; `ai_features.py:221-227`).
5. The preview's `/favicon.ico` request returns HTTP 404. This is an observed missing resource, not a passing check.
6. No independent engineering or other human review is recorded. The project's own license is not stated in the inspected project files.

## How to reproduce

- Replit run command: `python main.py` (`.replit:1-2,24-31`). For local web mode, run `RUN_WEB=true python main.py` (`main.py:55-72`).
- Tests: `PYTHONDONTWRITEBYTECODE=1 python -m pytest -p no:cacheprovider -q`.
- Git history used for the changes below: `git log --date=short --pretty=format:'%ad %s'`.

## Credits and licenses

- Robert Dickinson is the requested author attribution. Git history records recent changes by Replit Agent; no project license file was found.
- EPA SWMM is the simulation engine. The running engine reported version `5.2.4`; its license and source commit are not recorded in the inspected project files.
- `swmm-toolkit`: package metadata reports `CC0-1.0 AND (MIT OR Apache-2.0)`. This is package metadata, not a determination of the engine's license.
- `PySWMM`: BSD 2-Clause. Flask: BSD 3-Clause. Flask-CORS: no license classifier or expression in the installed metadata.
- Matplotlib: Python Software Foundation License. NumPy and pandas: BSD License. Plotly: MIT License. psutil: BSD License.
- OpenAI Python client: Apache Software License. ReportLab: BSD License. pytest: MIT. Werkzeug: BSD License.
- The project's own license: no license stated.

## AI use

Git history records Replit Agent commits for the engine integration, security and privacy work, visualizations and reports, and validation, translations, and accessibility. The project also calls the OpenAI API with `gpt-5` for report reviews, generated SWMM model drafts, what-if analysis, and anomaly analysis (`ai_features.py:9-14,179-329`). Git history and source do not record specific contributions by Robert Dickinson or identify AI tools used for earlier development.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-07-20: Validation, translation fallback, accessibility, and tests.
- 2026-07-20: Visualization, reports, and run comparison.
- 2026-07-20: Security and privacy hardening.
- 2026-07-20: Real SWMM engine integration and simulation results.
- 2025-08-18: Web-server support and application dependencies; the app version first appears in this dated Git history.

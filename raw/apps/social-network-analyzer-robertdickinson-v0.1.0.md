---
name: SWMM5 .inp File Interactive Viewer
file: social-network-analyzer-robertdickinson
version: 0.1.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://swmm5filestats.com, repo: none}
engines: none
stack: Python 3.11, Streamlit, Pandas, NumPy, SciPy, Plotly, Streamlit-AgGrid, NetworkX (declared dependency), Replit hosting; no database
units: not applicable
ai_use: Project source does not identify AI authorship; see AI use
---

# SWMM5 .inp File Interactive Viewer: Inspects SWMM5 input files

## What it does

The app accepts EPA SWMM5 input text and displays the file's sections as data grids. It helps people inspect the data rows and review basic descriptive statistics. It also provides interactive charts for supported data types. It displays input data; it does not run a SWMM simulation (`app.py:2108-2341`; no simulation engine is configured in `pyproject.toml` or `.replit`).

## How it computes

1. `validate_uploaded_file` checks the extension, size, and whether the file contains a recognized SWMM section marker (`app.py:2959-3068`).
2. `parse_inp_file_with_debug` splits the text into lines, starts a section at each bracketed section header, skips comments, and splits data rows on whitespace. It uses comment headers when available, otherwise uses one of the 17 built-in section column schemas or generic column names. It pads shorter rows and returns Pandas DataFrames (`app.py:2108-2340`).
3. `generate_statistics` converts each column to numeric values where possible and reports the mean, standard deviation, minimum, quartiles, median, and maximum. It also reports value frequencies. Frequency percentage is `count / row_count * 100` (`app.py:2346-2421`).
4. Chart functions create Plotly histograms, violin plots, frequency plots, box plots, scatter matrices, correlation heatmaps, bar charts, density plots, and parallel-coordinate plots (`app.py:2423-2957`). The correlation heatmap uses Pandas `DataFrame.corr()` (`app.py:2796-2831`).

No hydraulic or hydrologic equations are run. The app does not call a SWMM engine, and it does not convert units.

## Inputs and outputs

- **Input:** `.inp` and `.txt` uploads. The uploader accepts those extensions; the validator rejects files larger than `200 * 1024 * 1024` bytes (`app.py:3118-3124`, `app.py:2998-3029`).
- **Also included:** A built-in example SWMM input string (`app.py:2034-2106`).
- **Displayed output:** Section data grids, row and column counts, descriptive statistics, frequency tables, and charts (`app.py:3400-3465`, `app.py:4059-4089`).
- **Download:** The app has a source-code download button that exports `app.py` as `swmm_dashboard.py` (`app.py:3882-3899`).
- **Routes and APIs:** The configuration starts one Streamlit app on port `5000`; no separate API routes are defined (`.replit:7-9`, `app.py:4293-4294`).
- **Storage:** The manifest declares no database (`pyproject.toml:1-14`). The inspected app code has no file or database persistence for uploaded model data. Streamlit session state holds interface selections (`app.py:3070-3105`).

## Contents

- One Streamlit entry page, titled “SWMM5 .inp File Viewer” (`app.py:11-16`; `.replit:7-9`).
- 17 built-in SWMM section column schemas (`app.py:2121-2139`).
- 9 selectable theme definitions (`app.py:19-119`).
- The built-in example contains 10 sections and 43 data rows, counted by parsing `EXAMPLE_INP` with `parse_inp_file_with_debug` during this check (`app.py:2034-2106`; smoke run on 2026-11-15).

## Checks

- Python syntax check passed: `python -m compileall -q app.py`.
- Parser smoke check passed: parsed the built-in example into 10 DataFrames with 43 rows total. The check loaded `EXAMPLE_INP` and `parse_inp_file_with_debug` from `app.py` and asserted both counts (2026-11-15).
- Main page check passed: the local root page returned HTTP `200` and rendered in the preview (2026-11-15). The captured page showed the default upload and example-data view.
- Project test command attempted: `python -m pytest -q`. It could not start because `pytest` is not installed. No test files were found in the project.
- Human review: none recorded.

## What this does not show

1. **Automated tests:** No project test files were found, and `pytest` is unavailable in this environment. The project test suite was not checked.
2. **Interactive paths:** The preview check did not upload a user file or exercise chart generation, grid export, or the source download.
3. **Simulation results:** The app does not run a SWMM engine or calculate physical model results. It does not report or convert model units.
4. **Production page:** Deployment metadata reports the app as published, but this check loaded the local development page, not the production URL.
5. **Repository and review:** The configured Git remote uses an internal Replit host; a public GitHub URL was not verified. No human review is recorded.

## How to reproduce

- Run the app: `streamlit run app.py --server.port 5000 --server.address 0.0.0.0 --server.headless true` (`.replit:35-42`).
- Tests: no project test command or test files were found. `python -m pytest -q` requires `pytest`, which is not installed in the checked environment.
- Syntax check: `python -m compileall -q app.py`.

## Credits and licenses

- Robert Dickinson is listed as the author for this summary, as requested. The recent Git log records `robertdickinson` for upload UI changes and handover/design notes, and `dickinsonre_Autodesk_Water` for assistant-checkpoint entries (`git log -10`).
- Streamlit: Apache License 2.0.
- Pandas: BSD 3-Clause.
- NumPy: BSD.
- Plotly: MIT.
- NetworkX: BSD. It is declared as a dependency but is not imported by `app.py`.
- SciPy: BSD.
- Streamlit-AgGrid: MIT.
- Package licenses are from the installed distribution metadata checked on 2026-11-15. Dependency declarations are in `pyproject.toml:6-14`; versions are pinned in `uv.lock`.
- Project license: no license stated. No project license file was found.

## AI use

The project source does not name an AI tool that built the app. Git history records `robertdickinson` for upload UI changes and handover/design notes, and has assistant-checkpoint entries under `dickinsonre_Autodesk_Water`. The commit labels do not establish which work was AI-assisted.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: the 10 newest entries in `git log --date=short`.

- 2026-03-10: Added Project Explorer design details to the handover document.
- 2026-03-10: Added a Project Explorer design specification.
- 2026-03-01: Added a handover document with migration ideas.
- 2026-02-11: Published the app.
- 2025-08-26: Improved success-message visibility in the sidebar.
- 2025-08-26: Updated the Browse Files text in an assistant checkpoint.
- 2025-08-26: Added specific file upload guidance and limits.
- 2025-08-26: Aligned the file upload box with the sidebar width.
- 2025-08-26: Added playful file upload error messages.
- 2025-08-26: Restored an earlier project checkpoint.

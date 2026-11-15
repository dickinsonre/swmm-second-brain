---
name: "SWMM5 .inp File Viewer (ala InfoSWMM)"
file: swmm-5-inp-reader-robertdickinson
version: 0.1.0
date: 2025-08-26
author: Robert Dickinson
links: {replit: https://swmm-5-inp-reader-robertdickinson.replit.app, repo: none}
engines: none
stack: Python 3.11, Streamlit 1.48.1, Pandas 2.3.2, NumPy 2.3.2, Plotly 6.3.0, streamlit-aggrid 1.1.8; no database; Replit hosting
units: not applicable
ai_use: Git history lists Replit Agent and robertdickinson as commit authors; it does not identify the app's original builder.
---

# SWMM5 .inp File Viewer (ala InfoSWMM): Inspect SWMM5 input files without running a simulation

## What it does

The app reads uploaded SWMM5 `.inp` or `.txt` files and displays their sections as tables. It is for people who need to inspect model input without running a SWMM simulation. It shows section and row counts, a data grid, and column statistics. It also contains a built-in example file and a theme chooser, which are present in the checked source (`app.py:39-88`, `app.py:422-459`, `app.py:697-709`).

## How it computes

1. `main` validates the upload's extension and size, reads its bytes as UTF-8, and passes the text to `optimized_parse_inp` (`app.py:677-742`).
2. `optimized_parse_inp` splits the text at bracketed section headers and sends each section body to `process_section_block` (`app.py:475-505`).
3. `process_section_block` uses Pandas `read_csv` with whitespace separation, semicolon comments, and blank-line skipping. Seven known sections receive named columns; other sections receive generic column names (`app.py:463-471`, `app.py:507-534`).
4. `display_data_with_aggrid` shows an interactive grid when AgGrid is available and falls back to a Streamlit dataframe otherwise (`app.py:627-674`).
5. `calculate_stats_for_column` converts selected values to numbers where possible. It calculates mean, median, standard deviation, minimum, maximum, or a summary. Numeric summaries include a histogram; text summaries include value counts (`app.py:550-624`).

The app does not execute a hydraulic or hydrologic simulation engine. It parses and summarizes input text.

## Inputs and outputs

- Reads uploaded `.inp` and `.txt` files. The validator rejects files larger than 25 MB (`app.py:538-546`). The uploader accepts those two extensions (`app.py:713-718`).
- Reads file content as UTF-8 (`app.py:732-737`).
- Displays parsed section tables, row counts, and statistics in the Streamlit page. The configured app runs on port 5000 (`.replit:7-9`, `.replit:35-37`).
- The app defines no custom API routes. No database or file-output operation is present in the checked application code. Parsed data is held in Streamlit session state (`app.py:683-685`, `app.py:725-737`).

## Contents

- The declared project version is 0.1.0 (`pyproject.toml:3`). Git records the project setup on 2025-08-26 (`git log -- pyproject.toml`).
- The embedded example contains seven section headings, counted from `EXAMPLE_INP` (`app.py:422-459`).
- The parser defines column schemas for seven SWMM sections (`app.py:463-471`).
- The theme dictionary contains six themes (`app.py:39-88`).
- No other bundled records, pages, or models are defined in the checked application source.

## Checks

- `python -m unittest discover -v`: zero tests ran and zero failures were reported. The project contains no test files.
- Streamlit `AppTest` loaded the root page without exceptions. Clicking the example-data button parsed seven sections with no app exceptions.
- A local HTTP GET to `/` returned status 200. The captured app-preview screenshot was blank.
- Human review: none recorded.

## What this does not show

1. No user-uploaded model file was tested. Invalid, oversized, and malformed upload cases were not checked.
2. Browser rendering was not confirmed: the screenshot of the root page was blank even though the local request returned 200 and `AppTest` reported no exceptions.
3. No simulation results are produced or validated because the app does not run a simulation engine.
4. No person has recorded a review of this summary or of the current application.
5. The current source still contains the example-data button and theme chooser (`app.py:697-723`). Git history has entries saying example data and theme-selection functionality were removed, so the current source and those change descriptions do not fully agree.

## How to reproduce

Run the app with:

```sh
streamlit run app.py --server.port 5000
```

Run the available test discovery command with:

```sh
python -m unittest discover -v
```

The test command currently discovers no tests.

## Credits and licenses

- Robert Dickinson is the named author for this summary.
- Streamlit 1.48.1: Apache License 2.0.
- Pandas 2.3.2: BSD 3-Clause License.
- NumPy 2.3.2: BSD License.
- Plotly 6.3.0: MIT License.
- streamlit-aggrid 1.1.8: MIT License.
- Python 3.11 is configured in `.replit` (`.replit:1`). Package versions come from `uv.lock`; license names were checked in installed package metadata.
- SWMM5 is an input format described by the app. No SWMM simulation engine is included in the checked source.
- Project license: no license stated.

## AI use

Git history attributes project setup and interface changes to `robertdickinson`. It attributes the 2026-05-27 visual update and theme-selection change to Replit Agent. The history does not identify who originally wrote the app. The `.replit` workflow metadata lists `agent` as its author (`.replit:14-25`).

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

From `git log`, newest first:

- 2026-07-19: Published your App.
- 2026-05-27: Updated application visuals and removed unused theme-selection feature.
- 2026-05-27: Published your App.
- 2026-05-13: Added a last-updated date to the interface.
- 2026-05-13: Updated the application theme and removed unused functionality.
- 2025-08-27: Improved visual clarity and theme consistency.
- 2025-08-27: Improved file-upload feedback and section display.
- 2025-08-27: Organized sections into clickable boxes.
- 2025-08-27: Improved initial display and user guidance.
- 2025-08-27: Removed example data and related interface elements.

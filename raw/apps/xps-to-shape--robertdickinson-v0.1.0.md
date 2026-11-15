---
name: XPX to Shapefile Converter
file: xps-to-shape--robertdickinson
version: 0.1.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://xps-to-shape--robertdickinson.replit.app, repo: none}
engines: none
stack: Python 3.11, Flask, GeoPandas, Fiona, Shapely, pyproj, pandas, Werkzeug, Gunicorn, Replit hosting
units: not applicable
ai_use: Project files do not identify an AI tool that built the app; details under AI use.
---

# XPX to Shapefile Converter: Converts XPSWMM network data to GIS files

## What it does

The app accepts XPX or TXT files and extracts drainage network nodes, links, and polygons (`app.py:21-24`; `src/xpx_parser.py:44-61`). It creates point, line, and polygon ESRI Shapefiles for the records it can parse, then returns the files in a ZIP download (`app.py:225-263`; `src/shapefile_converter.py:27-136`). It is intended to help move XPSWMM data into GIS tools such as InfoDrainage, as described in `README.md`. It does not run a hydraulic simulation.

## How it computes

1. `XPXParser.parse` reads the input as text and dispatches lines beginning with `NODE`, `LINK`, `CONDUIT`, `PIPE`, `POLYGON`, or `SUBCATCHMENT` to record parsers (`src/xpx_parser.py:44-61`).
2. `_parse_node`, `_parse_link`, and `_parse_polygon` extract numeric attributes and coordinates using string checks and regular expressions (`src/xpx_parser.py:63-187`, `197-215`). Link geometry is made from the coordinates of its endpoint nodes when those nodes exist (`src/xpx_parser.py:141-145`).
3. `/validate` calculates record counts, coordinate bounds, diameter minimum and maximum, and sums of pipe lengths and catchment areas (`app.py:109-187`).
4. `detect_coordinate_system` checks coordinate ranges and may suggest an EPSG code. The suggestion is heuristic and can be absent (`app.py:26-54`).
5. `ShapefileConverter` builds Point, LineString, and Polygon geometries and writes them with GeoPandas using the selected CRS (`src/shapefile_converter.py:27-136`). It assigns a CRS; it does not reproject coordinates or convert physical units.
6. `/convert` gathers generated shapefile components into a ZIP file (`app.py:189-268`).

## Inputs and outputs

- Inputs: `.xpx` and `.txt` uploads. Flask limits request bodies to `50 * 1024 * 1024` bytes (`app.py:18-24`).
- `GET /`: serves the web page (`app.py:105-107`).
- `POST /validate`: accepts a multipart upload named `file`; returns JSON with preview, counts, statistics, coordinate-system suggestion, warnings, and errors (`app.py:109-187`).
- `POST /convert`: accepts a multipart upload named `file` and an optional `crs` form value; returns `xpx_shapefiles.zip` (`app.py:189-263`).
- `GET /health`: returns JSON status (`app.py:280-282`).
- Outputs: `nodes.shp`, `pipes.shp`, and `catchments.shp` when corresponding parsed records are available. Existing `.shp`, `.shx`, `.dbf`, `.prj`, and `.cpg` components are included in the ZIP (`app.py:225-248`, `270-278`).
- Uploads and generated files use server temporary directories. Validation removes its temporary directory after parsing; conversion removes its temporary directory after sending the response or after an error (`app.py:122-125`, `181-187`, `205-207`, `250-268`). No database is configured or used in the app source.

## Contents

- One HTML document (`templates/index.html`).
- Three interface tabs: Convert, XPX Guide, and Migration Workflow (`templates/index.html:388-394`).
- Four Flask routes (`app.py:105-107`, `109-187`, `189-268`, `280-282`).
- Three parsed record classes: `XPXNode`, `XPXLink`, and `XPXPolygon` (`src/xpx_parser.py:6-34`).
- The included sample file `sample_data/test.xpx` parsed as 3 nodes, 2 links, and 2 polygons in the run recorded under Checks.
- No database records are stored by the app source.

## Checks

- Test command: `python -m unittest discover -v`. It exited successfully and discovered 0 tests.
- Flask test client: `GET /` returned 200 and served the page. The browser preview showed the default Convert tab. The browser logged a 404; a separate check confirmed `/favicon.ico` returns 404.
- Flask test client: `GET /health` returned 200 with `{"status":"healthy"}`.
- Sample validation: `POST /validate` returned 200 with `valid: true`, 3 nodes, 2 links, 2 polygons, and no warnings or errors.
- Sample conversion: `POST /convert` returned 200 with a ZIP containing 15 shapefile component files for nodes, pipes, and catchments.
- Public app page: an HTTP request to the deployed root returned 200 and the title `XPX to Shapefile Converter - XPSWMM Migration Tool`.
- Human review: none recorded.

## What this does not show

1. The date the project assigned version `0.1.0` is not recorded. The front matter date is the date this summary was written, not a verified release date (`pyproject.toml:1-4`; no Git tags were present).
2. No automated tests were discovered. The sample file does not establish behavior for other XPX variants, malformed uploads, or the upload-size limit; these cases were not checked.
3. The browser preview checked the default tab only. Interactions in the other tabs were not checked.
4. Coordinate-system suggestions and the geographic accuracy of output files were not independently verified. The app assigns a CRS but does not reproject coordinates.
5. The deployed check requested only the public root page. Deployed validation and conversion were not checked.
6. `/favicon.ico` returns 404 in the current app run.
7. No person has reviewed this summary or recorded a human review of the app.
8. The repository states no license for the app itself. Dependency license compatibility was not reviewed.

## How to reproduce

- Development server: `python app.py` (`.replit:20-24`).
- Deployment command: `gunicorn --bind 0.0.0.0:5000 --workers 2 --timeout 120 app:app` (`.replit:26-28`).
- Test discovery command: `python -m unittest discover -v`. It currently discovers no tests.

## Credits and licenses

- Author: Robert Dickinson. The Git history attributes the listed commits to `robertdickinson`; it does not describe individual contributions.
- App license: no license stated. No project license file or `pyproject.toml` license field was found.
- Runtime libraries declared in `pyproject.toml`: Flask (BSD-3-Clause), GeoPandas (BSD), Fiona (BSD), Shapely (BSD), pyproj (MIT), pandas (BSD), Werkzeug (BSD), and Gunicorn (MIT). These license names come from the installed package metadata; some metadata identifies only “BSD License,” without a BSD version.
- Simulation engines: none.

## AI use

The project source and documentation do not name an AI tool used to build the app or describe AI contributions. Git history attributes commits to Robert Dickinson but does not specify his role in the work. `.replit` labels workflow entries with author `agent`, but does not identify a tool.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2025-12-06: Published your App
- 2025-12-06: Saved progress at the end of the loop
- 2025-12-06: Improve coordinate system detection and file validation
- 2025-11-26: Published your App
- 2025-11-26: Fix application deployment by correctly configuring the port
- 2025-11-26: Saved progress at the end of the loop
- 2025-11-26: Convert desktop application to web service for deployment
- 2025-11-26: Fix polygon coordinate parsing for accurate shapefile generation
- 2025-11-26: Build desktop application to convert XPSWMM files to InfoDrainage shapefiles
- 2025-11-26: Set up initial project structure and dependencies for file conversion

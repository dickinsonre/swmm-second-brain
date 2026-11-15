---
name: ForceMain SWMM5 EPANET Comparison
file: force-main-robertdickinson
version: "1.0"
date: 2026-11-15
author: Robert Dickinson
links: {replit: "https://forcemainswmm5epanetcomparison.com", repo: none}
engines:
  - {name: SWMM5, version: "PySWMM 2.1.0; native engine version not reported", source: "PySWMM Simulation", commit: "not recorded", license: "PySWMM BSD License; native engine license not recorded"}
  - {name: EPANET, version: "WNTR 1.5.0; native engine version not reported", source: "WNTR EpanetSimulator", commit: "not recorded", license: "WNTR Revised BSD; native engine license not recorded"}
stack: "Python 3.11, Streamlit 1.49.1, NumPy 2.3.2, pandas 2.3.2, SciPy 1.16.1, Matplotlib 3.10.6, Plotly 6.3.0, PySWMM 2.1.0, WNTR 1.5.0, OpenAI SDK 2.1.0"
units: SI
ai_use: "OpenAI GPT-5 powers the optional question-answering assistant."
---

# ForceMain SWMM5 EPANET Comparison: Model and compare force main systems

## What it does

The app provides engineers with tools to design and analyze force mains, calculate friction losses, and inspect hydraulic networks. It generates SWMM5 and EPANET input files and can run both simulation engines on paired generated models. It displays calculated results and visualizations, and includes troubleshooting guidance and an optional AI question-answering assistant. The app title is defined in `app.py:16`; its sidebar displays version 1.0 in `app.py:397`.

## How it computes

1. The force main calculator uses SI inputs. Hazen-Williams headloss is `hf = 10.67 * Q^1.852 * L / (C^1.852 * D^4.87)`. Darcy-Weisbach computes velocity from `V = Q / A`, calculates Reynolds number, selects a friction factor, then calculates `hf = f * L * V^2 / (D * 2 * g)`. The factor uses `64/Re` for laminar flow and Swamee-Jain for turbulent flow, with a linear transition between them. See `modules/calculator.py:48-105`.
2. NPSH available is `H_atm + H_static - H_friction - H_vapor - H_velocity`. Vapor pressure head can be derived from water temperature. See `modules/calculator.py:293-320`.
3. The network analyzer calculates link resistance and flow from head difference, interpolates pump curves, and solves junction continuity residuals using a Newton-Raphson iteration. It limits head updates to improve robustness. See `modules/network.py:148-192`, `modules/network.py:194-229`, and `modules/network.py:238-375`.
4. The SWMM5 and EPANET writers generate engine input text and validate it before download. See `modules/swmm_writer.py` and `modules/epanet_writer.py`.
5. The engine runners write generated text to temporary files. PySWMM runs SWMM5 simulations; WNTR runs `EpanetSimulator`. The runners summarize pumping-period flow and other available measures. See `modules/engine_runner.py:43-127` and `modules/engine_runner.py:130-227`.
6. `compare_engine_results` compares median pumping flow, velocity, force main headloss, and pump head. Percent difference is relative to the mean of the two values. The default review and exceedance thresholds are 5% and 10%. See `modules/engine_runner.py:230-276`.

## Inputs and outputs

- Users provide model settings through Streamlit controls. The app reads `data/pipe_materials.csv` and `data/pump_curves.csv` for reference data (`app.py:466` and `app.py:1017`).
- The combined generator provides downloadable SWMM5 `.inp` and EPANET `.net` files. The separate EPANET generator also offers `.net` downloads (`app.py:1181-1213` and `app.py:1425-1427`).
- Generated paired models and AI conversation state are held in Streamlit session state (`app.py:1218-1221` and `modules/qa_assistant_ui.py:11-26`). No database or separate application API routes were found.
- The AI assistant sends questions to the OpenAI API using GPT-5. It requires the `OPENAI_API_KEY` environment variable (`modules/qa_assistant.py:7-15`).

## Contents

- 10 navigation tools, including the AI assistant and source code view (`app.py:326-337`).
- 10 pipe-material records, excluding the CSV header (`data/pipe_materials.csv:1-11`).
- 50 pump curve points across 8 curve IDs (`data/pump_curves.csv:1-51`; counted from the CSV during this run).
- One paired SWMM5 and EPANET configuration fixture in the automated engine comparison test (`tests/test_engine_comparison.py:22-49`).
- 3 built-in suggested questions. The assistant also accepts user-entered questions (`modules/qa_assistant_ui.py:28-42` and `modules/qa_assistant_ui.py:78-123`).

## Checks

- `python -m pytest -q`: 5 passed, 0 failed. The tests cover flow unit normalization, generated input checks, a real-engine comparison, NPSH velocity head, and flow conversion (`tests/test_engine_comparison.py:51-109`).
- Streamlit `AppTest` executed all 10 sidebar views; 0 exceptions were reported. The views are defined in `app.py:326-337` and dispatched in `app.py:402-421`.
- The development app endpoint returned HTTP 200 in a `curl` check. The configured Streamlit workflow reported running.
- Human review: none recorded.

## What this does not show

1. The app footer displays version 1.0, while `pyproject.toml:3` declares package version 0.1.0. The source does not say which is the release version.
2. Native SWMM5 and EPANET engine build versions, commits, and licenses are not reported by the app. The versions and licenses above identify the installed Python wrapper packages only.
3. The OpenAI request was not made during verification. The assistant page loaded, but a live API response was not checked.
4. The screenshot check captured a loading placeholder rather than a settled browser view. Streamlit `AppTest` execution does not confirm visual layout.
5. The comparison view emitted a Streamlit deprecation warning for `use_container_width` at `app.py:1743-1744`. It did not stop the view from executing.
6. No design-engineer review, production simulation study, or independent validation against a field system was checked.

## How to reproduce

- Run the app with `streamlit run app.py --server.port 5000` (`.replit:7-10`).
- Run the tests with `python -m pytest -q`. The engine comparison test also documents `python -m pytest tests/test_engine_comparison.py -q` (`tests/test_engine_comparison.py:1-5`).

## Credits and licenses

- Author: Robert Dickinson, as specified for this summary.
- The project has no license stated in its project metadata or a root license file (`pyproject.toml:1-17`; license-file search performed during this run).
- Runtime package license metadata checked during this run: PySWMM, BSD; WNTR, Revised BSD; Streamlit, Apache 2.0; NumPy, pandas, and SciPy, BSD; Plotly, MIT; OpenAI SDK, Apache 2.0; Matplotlib, Python Software Foundation license; pytest, MIT.
- Installed runtime package versions and licenses were read from package metadata during this run. Declared dependency minimums are in `pyproject.toml:6-16`; Python 3.11 is configured in `.replit:1`.
- The repository does not record which AI tools helped build the app or what Robert Dickinson did.

## AI use

The source configures OpenAI GPT-5 for the optional assistant (`modules/qa_assistant.py:7-18`). It does not identify AI tools used to build the app.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-07-21: Force main audit, real solvers, and SWMM5/EPANET engine comparison.
- 2026-07-20: Force main audit commits; baseline review checkpoint, build transition, and publish entries.
- 2025-12-07: Standardized node naming across the application.
- 2025-12-07: Published the app.

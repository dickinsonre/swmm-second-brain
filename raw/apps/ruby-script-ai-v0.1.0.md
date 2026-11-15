---
name: InfoWorks ICM Ruby Script Runner
file: ruby-script-ai
version: 0.1.0
date: 2025-11-07
author: Robert Dickinson
links: {replit: "https://ruby-script-ai.replit.app", repo: none}
engines: none
stack: Python, Flask, Ruby, OpenAI Python client via Replit AI Integrations, Gunicorn, Requests, CodeMirror, GitHub REST API; no database configured
units: SI
ai_use: OpenAI Python client via Replit AI Integrations; source calls model gpt-5
---

# InfoWorks ICM Ruby Script Runner: An editor and helper for ICM Ruby scripts

## What it does

The app provides a web editor for writing and running Ruby scripts related to InfoWorks ICM. It returns script output and errors, and can request explanations, answers, and Markdown documentation from an AI service. It also provides example scripts, code templates, an API reference page, file upload and download, and GitHub browsing.

## How it computes

1. `app/main.py`, `run_script`, checks submitted Ruby text for emptiness, length, and a list of blocked strings. It writes the script to a temporary `.rb` file and invokes the `ruby` executable with captured output and a timeout. The source sets a 50,000-character limit and a 30-second timeout (`app/main.py:33-79`).
2. `app/ai_service.py`, `explain_script`, `answer_question`, and `generate_markdown`, build prompts with ICM scripting context and send them through the OpenAI Python client. The model name is `gpt-5` (`app/ai_service.py:98-192`).
3. `app/main.py`, `generate_template`, returns one of six predefined Ruby templates by key (`app/main.py:111-196`).
4. `app/github_service.py` calls GitHub's REST API to list repositories, navigate repository contents, retrieve file text, and search files (`app/github_service.py:19-143`).
5. The app does not include an InfoWorks ICM simulation engine. Its Ruby runner executes Ruby code; the ICM-specific examples require the InfoWorks ICM environment for those APIs (`README.md:71-73`, `replit.md:84`).
6. One example script computes a circle area with `radius = diameter / 2.0` and `area = Math::PI * radius ** 2` (`examples/08_arrays_loops.rb:21-30`). The web app itself does not calculate hydraulic or network results.

## Inputs and outputs

- The editor sends Ruby source and AI prompts as JSON to the app's API (`app/static/js/app.js:99-195`).
- Users can upload `.rb` files. The server saves them under `uploaded_scripts/` and returns their text (`app/main.py:198-227`). The configured request-size limit is 5 MB (`app/main.py:9-11`).
- Script execution uses a temporary Ruby file. Script and Markdown downloads are prepared in the system temporary directory (`app/main.py:54-77`, `app/main.py:229-313`).
- Uploaded scripts remain in the server's `uploaded_scripts/` directory. The app has no configured database. The editor and responses are held in the page; the frontend has no `localStorage` or `sessionStorage` calls (`app/main.py:10-16`, `app/static/js/app.js`).
- The app exposes these HTML routes and API endpoints (`app/main.py:18-408`):
  - `GET /` and `GET /docs`
  - `POST /api/run-script`, `/api/explain-script`, `/api/ask-ai`, `/api/generate-template`
  - `POST /api/upload-script`, `/api/download-script`, `/api/generate-markdown`, `/api/download-markdown`
  - `GET /api/list-uploaded-scripts` and `/api/load-uploaded-script/<filename>`
  - `GET /api/github/repositories`, `/api/github/contents`, `/api/github/file`, `/api/github/search`

## Contents

- The app has 2 HTML pages, served at `/` and `/docs` (`app/main.py:18-24`).
- The repository contains 8 Ruby example files (`examples/`; counted with `find examples -maxdepth 1 -type f -name '*.rb'`).
- The template generator contains 6 templates (`app/main.py:117-189`).
- The Flask app declares 16 routes: 2 page routes and 14 API routes (`app/main.py:18-408`; counted from `@app.route` declarations).
- Version `0.1.0` is declared in `pyproject.toml:3`. The version file first appears in the Git history on 2025-11-07 (`git log --follow -- pyproject.toml`).
- The project requires Python `>=3.11` and configures Python 3.11 and Ruby 3.2 runtimes (`pyproject.toml:5`, `.replit:1`). The run in this environment reported Python 3.11.14 and Ruby 3.2.2.
- CodeMirror `5.65.2` is loaded from a CDN (`app/templates/index.html:8-9`, `142-143`).

## Checks

- `python -m unittest discover -v`: 0 tests discovered, 0 passed, 0 failed. The command exited successfully, but the project contains no test suite.
- `ruby examples/01_hello_world.rb`: passed; printed the two expected greeting lines.
- Production `GET /` and `GET /docs`: both returned HTTP 200. The expected page titles were present, and neither response contained a traceback or internal server error. Checked with `curl` on 2026-11-15.
- Human review: none recorded.

## What this does not show

1. The test suite contains no tests, so behavior beyond the smoke checks above is not checked.
2. AI requests and generated AI responses were not checked against the external service.
3. GitHub repository access, file retrieval, and search were not checked against GitHub.
4. ICM-specific scripts were not run inside InfoWorks ICM with a real network.
5. Browser interactions, JavaScript errors, and external CDN asset loading were not checked.
6. The Ruby script filter is not a security sandbox. The README warns against exposing the app publicly without authentication and additional sandboxing (`README.md:67-69`). The code executes user-submitted Ruby on the server (`app/main.py:26-79`).
7. The project source does not state a public GitHub repository URL; `repo` is therefore `none`.
8. No human review is recorded in the project source or Git history.
9. The CodeMirror and Ruby runtime license terms were not checked.

## How to reproduce

- Start the configured Flask workflow with `python -m app.main` (`.replit:30`).
- Run the project's test discovery command with `python -m unittest discover -v`. No tests are currently defined.
- Run the Ruby example smoke check with `ruby examples/01_hello_world.rb`.

## Credits and licenses

- Robert Dickinson is named as the author in this file. Git history includes commits attributed to `robertdickinson`; it does not detail his individual contributions.
- Git metadata labels agent-authored changes as `Agent`. The project's Python dependencies provide Flask under a BSD-style license, Gunicorn under MIT, and the OpenAI and Requests packages under Apache-2.0. These licenses were identified from the installed package metadata and license files.
- The project has no license file or license statement: no license stated.

## AI use

The app uses the OpenAI Python client through Replit AI Integrations for script explanations, answers, and Markdown generation (`app/ai_service.py:98-192`, `replit.md:8`). The source calls model `gpt-5` (`app/ai_service.py:118-125`, `143-149`, `183-189`). Git metadata records both `robertdickinson` and agent-authored commits; it does not specify which individual changes Robert Dickinson made. No other app-building AI tool is named in the project files.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-07-21: Published the app.
- 2025-11-07: Added GitHub repository browsing and file import.
- 2025-11-07: Improved file handling and GitHub integration.
- 2025-11-07: Added script upload, download, and AI-generated Markdown.
- 2025-11-07: Fixed production imports.
- 2025-11-07: Added the ICM Ruby API reference page.
- 2025-11-07: Configured Gunicorn for production.
- 2025-11-07: Added script-execution safety checks and security warnings.
- 2025-11-07: Added ICM Ruby documentation and example scripts.
- 2025-11-07: Added AI assistance for ICM Ruby scripts.

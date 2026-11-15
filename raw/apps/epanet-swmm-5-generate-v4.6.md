---
name: EPANET 2.3 Generator
file: epanet-swmm-5-generate
version: "4.6"
date: "2026-07-20"
author: Robert Dickinson
links: {replit: "https://epanet-swmm-5-generate.replit.app", repo: "https://github.com/dickinsonre/EPANET-SWMM5-Generate"}
engines:
  - {name: EPANET, version: "2.3 (app label)", source: "epanet-js with @model-create/epanet-engine; README.md:34", commit: "not checked", license: "MIT per installed package metadata"}
  - {name: SWMM, version: "5.1.015 (bundled runner)", source: "ikegdivs/swmm-js; README.md:35", commit: "not checked", license: "EPA core public domain per HANDOUT.md:640; wrapper license not checked"}
stack: "JavaScript, TypeScript, HTML, CSS, Vite, WebAssembly, Node.js, Express, JSZip, Anthropic Claude; PostgreSQL/Drizzle workspace scaffold"
units: both
ai_use: "Optional Claude network explanations; development-tool attribution is incomplete in inspected project records."
---

# EPANET 2.3 Generator: generate and inspect synthetic water and drainage models

Source review and checks performed on 2026-11-15, from the current workspace.
The front-matter version date is the app's build date, not this review date.
Version and build date source: `artifacts/epanet-swmm-generator/index.html:3248`.
Deployment URL source: deployment metadata queried during this review.
Repository URL source: `README.md:120`. Repository accessibility was not checked.

Source shorthand below:
- `APP` means `artifacts/epanet-swmm-generator/index.html`.
- `SAMPLES` means `artifacts/epanet-swmm-generator/src/starter-samples.ts`.
- `HANDOUT` means `artifacts/epanet-swmm-generator/HANDOUT.md`.
- `API` means `artifacts/api-server/src/routes/anthropic/index.ts`.

## What it does

The app constructs synthetic pressurized-water and stormwater networks from settings and a seed.
It supports teaching, calibration exercises and solver-input development, rather than surveyed engineering designs (`APP:3078`).
It displays maps, model text and simulation results, and exports model and supporting files (`APP:1740-1753`; `HANDOUT`, Exports & File Formats).
It also offers committed starter inputs and optional AI explanations (`SAMPLES:1-40`; `API:38-79`).

## How it computes

- `mulberry32` initializes repeatable pseudo-random generation (`APP:3813`). Reproduction requires settings as well as the seed.
- `generateEPANETNetwork` builds the water-network geometry and attributes; `buildINP` serializes the input (`APP:5470`, `APP:6167`).
- `generateElevation` selects a terrain formula (`APP:4019-4050`). For rolling terrain, its initial surface is `elevation = maximum - ((normalized_x + normalized_y) / 2) * range * 0.6`; localized hills and a valley modify it (`APP:4024-4026`).
- `sizePipeByFlow` estimates pipe size in US customary quantities. `area_ft2 = pi * (diameter_in / 24)^2`; `velocity_ft_s = (flow_gpm / 449) / area_ft2` (`APP:5330-5331`). These are the code's constants, not independent conversion validation.
- The sizing screen rejects velocity above 5 ft/s and headloss per length above 0.01 ft/ft. It penalizes velocity below 2 ft/s and scores distance from 3.5 ft/s (`APP:5326-5338`). `hwHeadlossEst` supplies the headloss estimate.
- `pipeRoughnessForFormula` maps stored pipe quality to the selected formula's roughness convention (`APP:5356`). This is generator preprocessing, not the engine's complete hydraulic algorithm.
- `generateSWMMNetwork` constructs drainage geometry (`APP:7156`). Its node construction uses `invert = ground - cover - random_offset`; `maximum_depth = ground - invert` (`APP:7273-7279`). Outfall candidates are perimeter nodes sorted by ground elevation (`APP:7301-7308`).
- `generateDesignStorm` creates rainfall inputs; `buildSWMMINP` writes drainage, hydrology and optional process sections (`APP:7118`, `APP:7712`).
- EPANET is loaded through `Workspace.loadModule`; the runtime wrapper calls `Project.solveH` (`APP:8708-8728`, `APP:8916`; `src/solver-init.ts:1-7` under the app directory).
- SWMM is invoked through `cwrap('swmm_run', ...)` with input, report and output files in the engine filesystem (`APP:9425-9426`).
- `applyPressureQA` screens pressures in psi first, with meters of head for SI. It uses low and high thresholds of 20 psi and 100 psi equivalent (`APP:7027-7050`). This screen is not design certification.

## Inputs and outputs

- Generator settings, seed and configuration JSON are inputs. `applyConfigObject` restores settings; `persistConfig` uses browser local storage (`APP:11018-11082`).
- Starter INP files are downloaded as assets. The inspected starter module describes JSON Load Config separately from INP and provides download links (`SAMPLES:23-40`, `SAMPLES` function `render`).
- Exports include INP, RPT, HTML results, configuration JSON, GeoJSON, DEM, calibration CAL/DAT, PNG and ZIP packages (`HANDOUT`, Exports & File Formats; `APP` functions `generateResultsHTML`, `_buildCalFile`).
- Batch, sweep and ensemble exports package model collections and metadata (`HANDOUT`, Monte Carlo Ensembles and Node-count sweep).
- `POST /api/anthropic/summarize` accepts a network context and optional question. It returns a summary and model name (`API:55-96`; `artifacts/api-server/src/app.ts:32`).
- The server mounts health and Anthropic routers (`artifacts/api-server/src/routes/index.ts:1-8`).
- Core model state and solver files are browser-side. The AI endpoint keeps in-memory rate-limit counters and calls Anthropic; the inspected route does not persist conversation records (`API:13-35`, `API:68-96`).
- Database use beyond the workspace scaffold was not checked. No model database persistence is established by the inspected AI route.

## Contents

| Content | Count and source |
|---|---|
| Main modeling document | 1 inspected browser route, `/`, served by `APP`; loaded during this review |
| Inspection tabs | 10 button declarations counted at `APP:1742-1751`: Map, Stats, INP, Docs, HGL, 3D, Log, RPT, Results, AI |
| Starter models | 24 records counted now from `samples/validation.json`: 4 EPANET and 20 SWMM |
| EPANET starter families | 2: baseline and high demand, each in US and SI (`samples/README.md:8-18`) |
| SWMM starter families | 10 case rows, each in US and SI (`samples/README.md:20-35`) |
| LID control types in samples | 7: BC, PP, IT, RB, VS, GR and RG (`samples/README.md:27-33`) |

The sample manifest records earlier checks. Its contents are not a fresh rerun of every committed sample.

## Checks

Mechanical checks run on 2026-11-15:
- `pnpm --filter @workspace/epanet-swmm-generator test`: 9 passed, 0 failed, 0 skipped, from the command's test summary.
- The suite covers label/control preservation, QA display gating, diagnostic navigation, LID formatting, dimensional conversions, selection errors and configuration restoration.
- Its SWMM execution test runs 18 cases: each individual LID type, a BC/PP pair and the full set, in US and SI. It asserts a zero return code and a report containing `5.1.015` (`tests/swmm-lid.test.mjs:115-138` under the app directory; executed now).
- `pnpm --filter @workspace/epanet-swmm-generator typecheck`: passed with exit status zero.
- Main preview `/` loaded through the screenshot browser and displayed the map. Console output included an unidentified HTTP 404 resource failure and EPANET Warning 5: "Valves cannot deliver enough flow." The displayed Solver and QA indicators showed warnings.
- `curl` against the published root returned HTTP 200. This checks reachability, not published JavaScript behavior or parity with the workspace.

Human review: none recorded as a verified human review in the inspected evidence. Archived review material is indexed in `docs/reviews/README.md`.

## What this does not show

1. Engine source commits and the SWMM wrapper's license were not checked. The core-license statement does not establish the wrapper's terms.
2. Execution with native EPA SWMM 5.2.4 was not checked. The bundled report version above must not be confused with the app's export target (`APP:960`).
3. Full US/SI runoff equivalence, severe storms, drain-down and engineering suitability were not checked. Dimensional assertions and successful execution do not establish these.
4. Every committed starter file was not rerun. The sample-building script was not run because it rewrites sample files (`samples/README.md:54-62`).
5. Individual tab interactions, downloads, AI responses, mobile behavior and alternate browsers were not checked. Only the main page's initial visible state was loaded.
6. Published client behavior, workspace-to-production parity, the preview's missing resource and the cause of its valve warning were not checked.
7. Large-network timing, memory use, cancellation and rendering frame rates were not checked.
8. General INP import, round-trip preservation and later task implementations were not checked. Task notifications are not treated as code evidence.
9. Database deployment contents, comprehensive authentication/security behavior and external repository accessibility were not checked.
10. A complete dependency-license inventory, binary provenance and detailed allocation of development work between Robert Dickinson and AI tools were not checked.
11. No person has yet reviewed this summary. Authorship and acceptance of archived reviews were not checked; those reviews do not certify current hydraulic validity.

## How to reproduce

Run from the repository root with dependencies already installed:

```sh
pnpm --filter @workspace/epanet-swmm-generator run dev
pnpm --filter @workspace/api-server run dev
pnpm --filter @workspace/epanet-swmm-generator test
pnpm --filter @workspace/epanet-swmm-generator typecheck
```

The managed app workflow supplies the required port and base-path configuration. The Vite config requires both (`artifacts/epanet-swmm-generator/vite.config.ts:5-24`).
No environment-variable values or credentials are included here.
Open the main preview, generate a small network, inspect the input and run the selected solver.
Record executing engine version, units, configuration, seed and warnings when comparing models.

## Credits and licenses

- Robert Dickinson is credited as generator author (`HANDOUT:635`; `README.md:157`).
- The app and handout state MIT for the generator (`APP:3078`; `HANDOUT:635-648`). The root README gives less specific library-license guidance (`README.md:161-163`).
- Open Water Analytics EPANET and US EPA SWMM are credited in the project. The handout identifies the EPANET engine as MIT and EPA SWMM as public domain (`HANDOUT:639-640`).
- Installed `epanet-js` is MIT; source: its installed `package.json:4`.
- Installed `@model-create/epanet-engine` is MIT; source: its installed `package.json:20`.
- JSZip declares `MIT OR GPL-3.0-or-later`; source: its installed `package.json:66`.
- Vite and Express declare MIT in their installed package metadata, inspected during this review.
- The project references Rossman's EPANET manual, EPA SWMM reference material, SCS storm distributions and AWWA material (`APP:3078`). Reference attribution does not establish permission to redistribute those publications.

## AI use

The runtime assistant uses Anthropic Claude with model identifier `claude-opus-4-7` (`API:7`).
`buildAIContext` constructs a network snapshot; the server sends that context and an optional question to Anthropic (`APP:4930`; `API:68-79`).
This is an explanatory service, not the hydraulic solver.
The app calls itself a "vibe coding" educational tool (`APP:3078`), but the inspected records do not establish a complete development-tool history.
Replit Agent's current work was source inspection, running the listed checks and writing this summary.
Robert Dickinson is credited as developer in `README.md:157`; a finer attribution of implementation work is not established.
This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: `git log -10 --format='%ad %s' --date=short`, run during this review. Dates are commit dates, not inferred release dates.

- 2026-11-15: Add documentation for EPANET-SWMM v4.6 generation.
- 2026-10-30: Update epanet-swmm-generator features and build scripts.
- 2026-10-30: Published your App.
- 2026-10-30: Configure build environment and add documentation generator script.
- 2026-10-30: Add filtered starter INP downloads and ZIP exports with validation context.
- 2026-10-30: Git commit prior to merge.
- 2026-10-28: Add sample input files and build scripts for EPANET and SWMM generators.
- 2026-10-28: Update documentation and add UX feature roadmap.
- 2026-10-28: Update epanet-swmm-generator documentation and index file.
- 2026-10-28: Published your App.

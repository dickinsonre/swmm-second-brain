---
name: Kinematic Wave Router
file: ruby-swmm-router
version: 2026.11.15
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://ruby-swmm-router.replit.app, repo: none}
engines:
  - {name: Ruby kinematic-wave router, version: not stated, source: lib/kinematic_wave_router.rb (references EPA SWMM5 kinwave.c), commit: engine-specific commit not stated, license: public domain per README.md}
stack: Ruby 3.2/3.3 (.replit:1), Sinatra 4.2.1, Rack 3.2.4, Rackup 2.2.1, Puma 7.1.0 (Gemfile.lock:9-22), Replit hosting (.replit:29-30), optional ICM InfoWorks Ruby Exchange API (lib/icm_infoworks_integration.rb:4-18); no database configured (Gemfile; web_app.rb:1-26)
units: US customary
ai_use: Project records do not identify AI tools used to build the app; details under AI use.
---

# Kinematic Wave Router: Routes flow through SWMM5 drainage networks

## What it does

The web app reads a SWMM5 INP drainage network and routes a constant inflow from a selected inlet. It analyzes network topology and selects dendritic routing or an iterative loop solver. It displays peak and final outflow, time to peak, conduit properties, and a time series that can be downloaded as CSV. A separate Ruby integration module provides ICM InfoWorks import and export through the host application's Ruby API. (Sources: `web_app.rb:96-192`; `lib/network_topology.rb:92-133,200-319`; `views/results.erb:7-24,27-64`; `lib/icm_infoworks_integration.rb:23-112`.)

The app's title is “Kinematic Wave Router.” The app interface does not show a release version, and no `package.json` exists. The README has a separate version note, but it is not displayed by the app; this file therefore uses the requested date fallback. (Sources: `views/layout.erb:1-7`; `README.md:292-294`; workspace check for `package.json`.)

## How it computes

1. `KinematicWave::SWMM5Importer#import_from_file` reads INP text and parses junctions, outfalls, dividers, conduits, and cross sections. `process_conduit` estimates slope from the difference in invert elevations divided by length, with a minimum fallback when the elevation drop is not positive. (Source: `lib/swmm5_import.rb:23-49,86-110,113-225`.)
2. `Conduit#calculate_full_flow` computes full-flow area and capacity with Manning's equation: `Qfull = (1.486 / n) * A * R^(2/3) * sqrt(|S|)`. The area and wetted perimeter depend on cross-section geometry. The implementation estimates `beta = 1.67 * Qfull / Afull`; its section factor is `S = A * R^(2/3)`, where `R = A / wetted_perimeter`. (Source: `lib/kinematic_wave_router.rb:45-85,87-169`.)
3. `Network#validate_and_analyze` identifies strongly connected components to detect loops, checks for at least one outfall, and sets the routing mode. For dendritic networks, `determine_routing_order` sorts conduits from upstream to downstream. Dendritic flow splits are divided equally among outgoing conduits. (Source: `lib/network_topology.rb:73-133,149-198,210-247`.)
4. `Router#route_conduit` normalizes the previous flow and area values, calculates the weighted continuity coefficients, and solves `f(a) = beta1 * section_factor(a) + c1 * a + c2 = 0`. `newton_raphson` iterates within bounds until its convergence test is met or the configured iteration limit is reached. For looped networks, `Network#route_time_step_with_loops` routes conduits repeatedly with under-relaxation and checks the maximum outflow change. (Sources: `lib/kinematic_wave_router.rb:189-269,296-381`; `lib/network_topology.rb:249-319`.)
5. The web handler repeats routing for the requested number of time steps. It calculates peak outflow, final outflow, and time to peak, then writes a CSV with time in minutes and conduit outflows in CFS. (Source: `web_app.rb:124-185`.)

The web interface reports flow in CFS and conduit length in feet. The engine's Manning equation uses the US customary coefficient. (Sources: `views/configure.erb:95-107`; `views/results.erb:10-24,66-75`; `lib/kinematic_wave_router.rb:66-70`.)

## Inputs and outputs

- The browser accepts a `.inp` file at `POST /upload`. The server copies it into `uploads/` and stores its path and original filename in the Sinatra session. (Sources: `views/index.erb:48-53`; `web_app.rb:38-58`.)
- `GET /load_sample` selects `tests/simple_loop.inp`; `GET /example` downloads an example INP file. (Source: `web_app.rb:60-65,221-256`.)
- `GET /configure` displays the imported network. `POST /simulate` accepts inlet node, inflow, timestep, and step-count fields. (Sources: `web_app.rb:67-94,96-145`; `views/configure.erb:85-108`.)
- `POST /simulate` writes a CSV under `results/`; `GET /download` sends that file. The session stores the generated CSV path. (Source: `web_app.rb:172-188,210-219`.)
- Other routes: `GET /`, `GET /workflow_diagram`, `GET /reset`, `GET /documentation` and its named document paths, `GET /code`, and `GET /download_code`. (Source: `web_app.rb:28-36,258-341`.)
- The app uses server-side files for uploads and results. No database is configured in the inspected app or Gemfile. The exact storage medium for Sinatra session values was not verified. (Sources: `web_app.rb:26,38-58,172-188`; `Gemfile`.)
- The library also contains methods to export SWMM5 INP, report-style output, and time-series CSV files for direct Ruby callers. These exports are not exposed as web routes. (Sources: `lib/swmm5_export.rb:21-62`; routes in `web_app.rb:28-341`.)

## Contents

- Six ERB view templates, counted from `views/`. (Counted in this run with `find views -maxdepth 1 -type f -name '*.erb'`.)
- Five Ruby library files, counted from `lib/`. (Counted in this run with `find lib -maxdepth 1 -type f -name '*.rb'`.)
- Four Ruby example files, counted from `examples/`. (Counted in this run with `find examples -maxdepth 1 -type f -name '*.rb'`.)
- The loop test fixture contains four nodes and four conduits, as reported by `ruby tests/test_loop_solver.rb` for `tests/simple_loop.inp`.

## Checks

- `ruby tests/test_runner.rb`: zero passed and eight failed. Each failure reports `no block given (yield)`. The helper calls `yield`, but the test cases call it without blocks, so the intended assertions do not run. (Sources: this test run; `tests/test_runner.rb:21-29,32-47`.)
- `ruby tests/test_loop_solver.rb`: exited successfully and routed the loop fixture, but logged that the loop solver did not fully converge after 20 iterations; the reported maximum change was 0.0203 CFS. The script prints completion but contains no result assertions. (Sources: this test run; `tests/test_loop_solver.rb:9-64`; loop limits in `lib/network_topology.rb:249-319`.)
- The development app returned HTTP 200 for `/`, `/documentation`, `/documentation/theory`, `/documentation/guide`, `/documentation/router`, `/documentation/topology`, `/documentation/import`, `/documentation/export`, `/documentation/icm`, and `/code`. The sample-network configure and simulation-result pages also returned HTTP 200. The sample CSV download returned HTTP 200 with the expected time-series header. These requests were made against the running development app during this run.
- Human review: none recorded.

## What this does not show

1. The summary version uses the current date because the interface has no displayed release version and no `package.json` exists. The README separately states `1.0 (2025)`, but that version is not shown by the app. (Sources: `views/layout.erb:1-7`; `README.md:292-294`; workspace check for `package.json`.)
2. The automated test suite is currently unusable as a pass/fail check because its test helper is called without blocks. The loop test run also did not converge fully on its sample fixture. (Sources: checks above; `tests/test_runner.rb:21-47`; `lib/network_topology.rb:249-319`.)
3. An upload using a user-supplied INP file, malformed or unsupported INP sections, and behavior on networks beyond the included sample were not checked in this run.
4. The ICM InfoWorks integration was not run because it requires the ICM Ruby API host environment. (Source: `lib/icm_infoworks_integration.rb:23-47`.)
5. Production runtime behavior was not checked; the route checks used the development app.
6. The storage medium for session values was not checked. The inspected app shows session keys but does not configure a session store. (Source: `web_app.rb:26,50-51,187`.)
7. License terms for the Replit hosting service and ICM InfoWorks API were not checked. Gem licenses below were read from installed gem metadata during this run.
8. No human review is recorded.

## How to reproduce

Install the dependencies and start the app:

```sh
bundle install
ruby web_app.rb
```

Run the checked scripts:

```sh
ruby tests/test_runner.rb
ruby tests/test_loop_solver.rb
```

The app run command is also configured as `ruby web_app.rb`. (Sources: `.replit:21-24,29-30`; `Gemfile`.)

## Credits and licenses

- Robert Dickinson is the author named for this summary, as instructed.
- EPA SWMM5 is identified by the README as public domain; the README says the Ruby implementation maintains that status. It credits L. Rossman and M. Tryby for the original SWMM5 C-code port. (Source: `README.md:282-290`.)
- Sinatra 4.2.1: MIT. Rack 3.2.4: MIT. Rackup 2.2.1: MIT. Puma 7.1.0: BSD-3-Clause. Versions are from `Gemfile.lock`; licenses were checked with `gem specification <name> license --yaml` during this run.
- Replit provides the configured hosting. The optional ICM InfoWorks integration uses its Ruby Exchange API. (Sources: `.replit:29-30`; `lib/icm_infoworks_integration.rb:4-18`.)
- No separate project license file was found; the README states the project's public-domain status. (Source: `README.md:282-286`; workspace license-file search.)

## AI use

The inspected project code and documentation do not identify AI tools used to build the app or describe what Robert Dickinson did. The Replit configuration labels workflow authors as `agent`, but it does not specify an AI tool's contributions. (Source: `.replit:8-19`; project AI-reference search.)

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

The following are the ten newest `git log` entries, newest first.

2026-07-24: Added validation warnings and support for looped networks.
2025-11-14: Published your App.
2025-11-07: Deployed your application.
2025-11-07: Added footer links to EPA SWMM5 and the Replit project.
2025-11-07: Deployed your application.
2025-11-07: Deployed your application.
2025-11-07: Updated the workflow diagram to show four input options.
2025-11-07: Added an option to load sample data for network routing.
2025-11-07: Deployed your application.
2025-11-07: Deployed your application.

---
name: FV Link Lab
file: fv-link-lab.html
deployed_as: index.html (fvlink/app/netlify on the branch)
version: 1.1.0
date: 2026-11-18
author: Robert Dickinson
links: {netlify: none yet (drag fvlink/app/netlify onto Netlify), artifact: "https://claude.ai/artifact/VoY6Vve25S2JznvXz7YQk2", repo: "https://github.com/SWMMBobSWMM6/Stormwater-Management-Model/tree/swmm524-fvlink/fvlink"}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4, commit: 7952ca8, license: public domain}
  - {name: swmm524-fvlink, version: 5.2.4 + swmm524-fvlink.patch, branch: swmm524-fvlink, base commit: 7952ca8, license: public domain (EPA base), patch by Robert Dickinson}
build: Emscripten 3.1.51, LLVM 18, Binaryen 116; -O2 -sSINGLE_FILE=1 -sMODULARIZE=1 -sENVIRONMENT=web,worker -sALLOW_MEMORY_GROWTH=1 -sSTACK_SIZE=2MB; built 2026-10-21; not rebuilt for 1.1.0
units: US customary (cfs, ft) in every sample; otherwise the model's own FLOW_UNITS
ai_use: built with Claude (Anthropic); see AI use
---

# FV Link Lab: finite volume on chosen SWMM conduits, dynamic wave on the rest, in the browser

## What it does

Runs two SWMM engines side by side in the browser: stock EPA SWMM 5.2.4 and
swmm524-fvlink, the same source with a new `[FV_LINKS]` input section. Conduits
listed there are solved by an explicit finite-volume (FV) scheme on their own
cells; every other link and node stays stock dynamic wave. The user picks a
sample or loads an `.inp`, clicks conduits to make them FV, runs both engines,
and compares hydrographs, peaks, step counts and wall time, or runs a
byte-for-byte null check on the model with no FV links. Version 1.1.0 adds a
Mars tab: the Thoth canal from the story *Thaw on the Thoth*, run on these
Earth-gravity engines by Froude scaling, plus a downloadable InfoWorks ICM kit.

Tabs: Run, Evidence, Defects, Mars, About, Doc (essay *One Pipe, Its Own
Clock*, 11 sections, 21 figures, also shipped as
`swmm524-fvlink-one-pipe-its-own-clock.docx`).

## How it computes

### The FV link (`src/solver/fvlink.c`, 1,403 lines)

State per cell: flow area A and flow Q per barrel. Equations solved:

```
dA/dt + dQ/dx = 0
dQ/dt + d(Q^2/A + g*I1)/dx = g*A*(S0 - Sf),   Sf = n^2 Q|Q| / (1.486^2 A^2 R^(4/3))
```

- Flux: HLL, `F = (sR*FL - sL*FR + sL*sR*(UR - UL)) / (sR - sL)`, Davis wave
  speeds `sL = min(uL - cL, uR - cR)`, `sR = max(uL + cL, uR + cR)`,
  `c = sqrt(g*A/T)`, dry-bed estimates.
- Bed slope and offsets: hydrostatic reconstruction (Audusse et al. 2004).
- Closed shapes above the crown: static Preissmann slot, celerity 100 ft/s
  (`FV_SLOT_C`, line 45), width capped at 5 % of max. width (`FV_SLOT_WFRAC`, line 46).
- Friction: semi-implicit Manning on the real section area; slot area excluded.
- Positivity: each face limited by the cell or node it drains from.
- Geometry: SWMM's own `xsect_getAofY` at 256 depths (`FV_NTAB`, line 43),
  joined by straight lines, so width = dA/dy exactly and depth from area is an
  exact inverse. Where SWMM's area table falls with depth (some irregular
  transects, S5-DW4), the running maximum is kept.
- Mesh: default cell about 25 ft (`FV_DX_TARGET`, line 47), at least 4 cells
  (`FV_MIN_CELLS`, line 48).
- Substep: `dt <= 0.5 * dx / max(|u| + c)` (`FV_CFL`, line 44), floor 0.001 s
  (`FV_MIN_DT`, line 49).

### Coupling to dynamic wave

- FV links are subcycled inside every Picard iteration of the dynamic wave
  step, from the saved start-of-step state.
- Each end face sees a ghost state: the node head as water surface and the
  adjacent cell's velocity (the FVL-1 fix). See FVL-15 below for the inflow end.
- Junctions, storage units and dividers at an FV end keep their own continuity
  during the subcycle: backward-Euler head estimate using the end faces'
  conductance `K = sqrt(g*A*T)` as dQ/dH, up to 4 estimates per substep
  (`FV_MAX_PASS`, line 50), substep limited to `A_node / K` (`FV_NODE_FACTOR`, line 51).
- Outfalls, and nodes surcharged under EXTRAN, follow dynamic wave's head.
- Volume crossing each end face is booked into node continuity exactly
  (except a node surcharged under EXTRAN).
- Reported link flow is the time-averaged delivered flow, so quality routing's
  "one flow plus storage change" identity holds exactly.
- FV links take no part in dynamic wave's Courant step.

### The Mars tab: Froude scaling

Gravity is compiled in: `consts.h:37 #define GRAVITY 32.2`. The Mars model
(g = 12.2 ft/s2) is converted to an equivalent Earth model with
`k = sqrt(32.2 / 12.2) = 1.624606`:

| Quantity | Mars model | Earth model |
|---|---|---|
| lengths, levels, areas, volumes | as is | as is |
| flows (inflow, pump curve) | Q | Q x k |
| times (series, controls, steps, run end) | t | t / k |
| Manning's n | 0.0244 | n / k = 0.0150 |
| SWMM weir Cw (dimensional) | 2.050 | Cw x k = 3.330 |
| orifice Cd | 0.61 | 0.61 |
| thaw crest | 4,200 cfs, hour 42 | 6,823 cfs, hour 25.85 |
| run length | 96 h | 59.09 h |
| report step / routing step | 300 s / 30 s | 185 s / 18.466 s |

Results read back as: depth as is, flow / k, time x k. The Mars n and Cw come
from holding `g*n^2` and `Cw/sqrt(g)` fixed: n 0.015 x k = 0.0244, Cw 3.33 / k = 2.050.
Scaler: `examples/thoth-mars/icm/froude_scale.py`.

Mars tab models (Earth files embedded, Mars sources in `examples/thoth-mars/runs/`):

| Key | Earth file | Mars source | FV links in the FV run |
|---|---|---|---|
| nospill | `thoth_earth_nospill.inp` | `F_nospill_stock.inp` | CULVERT, 1 cell |
| plan | `thoth_earth_plan_38_52.inp` (Old Canal gate open Mars hours 38 to 52) | `F_full38c52_stock.inp` | CULVERT, 1 cell |
| lock | `thoth_earth_company_lock.inp` (Company geometry, Lock, 10-ft throat) | `CO_mars.inp` | THROAT (default cells) and CULVERT 1 cell |

## Inputs and outputs

- Reads `.inp` (SWMM 5.2.4 format plus `[FV_LINKS]`). Writes the FV `.inp`
  (adds or replaces `[FV_LINKS]`), and offers each engine's `.rpt` and `.out`
  for download. The stock run gets the model without `[FV_LINKS]`; stock 5.2.4
  stops on that header with ERROR 205.
- `[FV_LINKS]` line: `link [cells | *]`. ERROR 209 unknown link; ERROR 211 bad
  cell count; ERROR 116 for a link that cannot be FV (force main, culvert code,
  flap gate, losses, seepage, max. flow, street inlet, or a pump or dummy
  conduit drawing from an end node).
- New report table: *Finite-Volume Link Summary* (cells, cell length, substeps
  per routing step, smallest substep, link volume balance error, substeps at the floor).
- Mars tab: "Open it in the Run tab" loads the scaled model; "Download the ICM
  kit (.zip)" bundles the scaled `.inp` files and stock reports, the CSV
  tables, `build_thoth_iw.rb`, `mars_results.rb`, `froude_scale.py`,
  `compare.py`, `froude_check.json` and the kit README (JSZip 3.10.1 from cdnjs).
- Inside the claude.ai artifact viewer every download goes through the viewer's
  `downloads` capability (it asks first); types it will not save as they are
  (.inp, .rpt, .out, .rb, .py) come inside a .zip of the same name. Elsewhere
  downloads are plain browser downloads.
- Stores only theme and welcome-seen flags in localStorage. Files never leave the browser.

## Checks

Mechanical, from `fvlink/results/` unless noted.

| Check | Result |
|---|---|
| Null effect, no `[FV_LINKS]`, 73 EPA regression models (native) | 72 `.out` byte-identical to stock; 1 stops with the same error in both |
| Patch on a fresh v5.2.4 clone, rebuilt | binary byte-identical; OpenMP THREADS 2 same `.out` on 13 FV models |
| FV link volume balance | at most 2.7e-12 % over 37 EPA models and 14 synthetic cases |
| Lake at rest, every conduit FV | max abs(Q) 1.2e-11 cfs |
| 10-ft rectangular channel, 60 cfs, n 0.015, S 0.001 | FV 1.6592 ft vs Manning normal depth 1.6559 ft (+0.20 %) |
| 400-pipe tree, 10-ft trunk pipe FV | 0.19x stock wall time (n = 7 interleaved); every conduit peak within 0.53 %, every node peak within 0.80 % |
| WebAssembly vs native, EPA suite (`wasm_check.txt`) | stock and FV each: 65 identical, 1 `.rpt` round-off only, 6 `.out` differ (largest 16.2 cfs in 1,962 cfs, 0.83 %, user5; follows the math library, musl vs glibc), 1 same error; null effect exact inside WebAssembly on all 73 |
| App, headless Chromium (`app_browser_test.txt`) | 9 samples through the page's own engines vs native: 18 `.out` byte-identical |
| Froude scaling, native stock 5.2.4 at g 12.2 (Mars input) vs g 32.2 (scaled input), `examples/thoth-mars/icm/froude_check.json` | gate shut: largest depth difference U1 0.0008 ft, U4 0.0007, L6 0.0026, BASIN 0.035; 134.830 vs 134.827 Mgal over the levee; continuity -0.039 % both |
| same, plan | BASIN crest 13.991 vs 13.986 ft; Old Canal 1,442 vs 1,437 ac-ft; continuity -0.133 vs -0.135 % |
| same, Company geometry | levee at Mars hour 40.92 vs 40.74; 135.87 vs 136.11 Mgal; continuity -0.159 vs -0.167 %; LT7 flow differs up to 656 cfs at single instants (throat chatter) |
| Mars tab in headless Chromium, page engines (`app_mars_test.txt`) | nospill stock: levee at Mars hour 40.49, continuity -0.039 % (native scaled 40.49); plan stock: crest 13.986 ft, gate 1,436.5 ac-ft, continuity -0.135 % (native 13.986, 1,437, -0.135 %); lock stock: levee 40.74 (native 40.74) |
| Mars tab, FV runs in the page | nospill: levee 40.41, average dynamic wave step 10.0 s vs 0.36 s stock (Earth-model seconds); plan: crest 13.985 ft, gate 1,437.0 ac-ft; lock: reproduces FVL-15 (at Mars hour 24 LOCK 0.634 ft, BASIN 8.81 ft, THROAT 300 cfs into the basin) |
| Phone width 375 px | no horizontal overflow |

Human review: none recorded. An independent Claude agent reviewed `fvlink.c`
without the build history (found FVL-6 to FVL-10); two more checked the
technical description against code and results (FVL-13, FVL-14).

## What this does not show

- No field data. Stock dynamic wave is the reference, not the truth.
- **Open defect FVL-15** (found 2026-10-30). At the inflow end, the ghost pairs
  the node's level with the link's velocity. Fed from a still pool, the link
  is handed u^2/2g of head the pool never had (5.8 ft at 11.9 ft/s on Mars)
  and can run water uphill: in the Company lock model the throat carries
  300 cfs from the lock into the basin, whose water surface is 7.7 ft higher
  (in the page's lock run at Mars hour 24: LOCK 0.634 ft deep, BASIN 8.81 ft). Five prototype fixes
  (`fvlink/prototypes/`, fvl-15 to fvl-15e), none adopted. Do not put an FV
  link at the outlet of a pool. The code as it is (`fvlink.c` lines 1074 to 1103):

```c
    // --- left state
    if ( m == 0 )
    {
        zL = f->z1;
        etaL = hd1;
        hL = MAX(0.0, etaL - zL);
        uL = velOf(f, f->a[0], f->q[0]);
    }
    ...
    // --- right state
    if ( m == nc )
    {
        zR = f->z2;
        etaR = hd2;
        hR = MAX(0.0, etaR - zR);
        uR = velOf(f, f->a[nc-1], f->q[nc-1]);
    }
```

- Extra head at FV link ends: node upstream sits +0.19 ft (12 cells) and
  +0.13 ft (48 cells) above stock in the 30 cfs chain, +0.47 ft at the storage
  node in the mixed case. Numerical; shrinks with refinement.
- Not in FV links: evaporation, seepage, conduit lengthening, hot-start cell
  state. Quality tested with one conservative pollutant only. Not tested:
  reactive quality, ponding, control rules acting on an FV link.
- Cost: very short cells are slow (user4 1.88-ft link: 15.5 s vs 3.0 s stock);
  a full pipe subcycles at the slot celerity.
- Platforms: native Linux gcc 13.3 and this WebAssembly build. No MSVC.
  WebAssembly `.out` differs from native on 6 of 73 EPA models (math library).
- Not compared against OpenSWMM's FV engine.
- Mars and ICM: nothing has been run in InfoWorks ICM. `build_thoth_iw.rb` and
  `mars_results.rb` were run only against a stand-in for ICM's
  `WSApplication`; ICM field names, shape codes (OT1:2, OREC) and link types
  (WEIR, VSGATE, FIXPMP) are unverified. The n and Cw scaling is a dimensional
  argument with no Mars measurement behind it.
- In the story's Mars runs the culvert, Chute, intake channel and Old Canal
  kept Earth handbook n. Scaling them too (`runs/*_alln.inp`): plan crest
  unchanged at 13.991 ft; gate-shut levee hour 40.33 to 40.50; water over the
  levee 134.8 to 134.2 Mgal; Chute top peak 2.6 to 3.5 ft.
- No person has reviewed `fvlink.c` line by line, run the branch on a project
  model, approved the design choices in `fvlink/README.md`, or checked the
  app's parsers beyond the automated tests.

## How to reproduce

```
git clone --branch swmm524-fvlink https://github.com/SWMMBobSWMM6/Stormwater-Management-Model.git
cd Stormwater-Management-Model
gcc -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -Isrc/solver -Isrc/solver/include \
    src/solver/*.c src/run/*.c -lm -o runswmm_fv
# EPA checks: fvlink/VERIFICATION.md, Reproduction (null_gate.sh, suite.py, sweep.py)
# Mars engine: same build with GRAVITY 12.2 (examples/thoth-mars/mars_gravity.patch)
python3 examples/thoth-mars/icm/froude_scale.py MARS.inp EARTH.inp
python3 examples/thoth-mars/icm/compare.py        # writes froude_check.json
# App: fvlink/app/source/ (WebAssembly build notes, test scripts);
# Mars tab: fvlink/app/source/mars/ (make_mars_data.py, doc_mars.py, inject_mars.py)
node fvlink/app/source/test/test_mars.js           # headless Chromium, Playwright
```

## Credits and licenses

- EPA SWMM 5.2.4: U.S. EPA, Lewis Rossman and contributors; public domain.
- swmm-nrtestsuite v2.5.0-dev (EPA regression models, user2 sample): U.S. EPA.
- OpenSWMM engine (HydroCouple), commit 8dd7387: source read for comparison
  (ghost velocity, bed step at nodes).
- Method references: Godunov; Harten, Lax and van Leer (HLL); Davis (wave
  speeds); Audusse et al. 2004 (hydrostatic reconstruction); Preissmann (slot).
- Emscripten 3.1.51; html2canvas 1.4.1, gif.js 0.2.0, JSZip 3.10.1 (cdnjs).
- Story, models and patch direction: Robert Dickinson.

## AI use

This app, the swmm524-fvlink branch it runs, its tests and its documents were
made with Claude, Anthropic's AI model, in Claude Code sessions from October
13 to 21, 2026, and on November 18, 2026, under the direction of Robert (Bob)
Dickinson, who is responsible for the work. Claude read the EPA SWMM 5.2.4 and
OpenSWMM source, designed the method and chose its parameters, wrote
`fvlink.c` and the hooks, the test networks and scripts, ran every test, fixed
the defects in the register, compiled both engines to WebAssembly, wrote the
page, drew the figures from results files and wrote all the text. In November
it built the Thoth canal and the story around it, found FVL-15 and tried five
fixes (none adopted), derived the Froude scaling, built the ICM kit, checked
the scaling with two builds of stock 5.2.4, added the Mars tab and Doc section
10, and wrote this file. The checks are mechanical. Not checked by a person:
`fvlink.c` line by line, a project model, anything in InfoWorks ICM, and the
n and weir scaling.

## Changes

- `1.1.0 (2026-11-18)`: Mars tab (Thoth canal, Froude-scaled, three models,
  stock and FV runs, ICM kit download); FVL-15 in the Defects tab; Doc section
  10 and Figure 21; this technical summary embedded and linked; downloads
  routed through the claude.ai viewer when the page runs there.
- `1.0.0 (2026-10-21)`: first release: Run, Evidence, Defects, About, Doc;
  both engines in WebAssembly; 9 samples.

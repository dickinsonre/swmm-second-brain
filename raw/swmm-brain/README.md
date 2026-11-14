# SWMM-Brain-Dickinson

**50 years of stormwater modeling in one repository.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![SWMM](https://img.shields.io/badge/EPA_SWMM-5.2%2B-green.svg)](https://github.com/USEPA/Stormwater-Management-Model)
[![Blog](https://img.shields.io/badge/Blog-swmm5.org-blue.svg)](https://swmm5.org)
[![Newsletter](https://img.shields.io/badge/Newsletter-The_Dickinson_Canon-0A66C2.svg)](https://www.linkedin.com/in/robertdickinson/)
[![CIMM](https://img.shields.io/badge/SWMM5%2B_TAC-CIMM.org-green.svg)](https://cimm.org)

---

In 1974, I ran my first SWMM model on punch cards. Today I'm compiling the same engine to WebAssembly so it runs in a browser. This repository collects everything in between — engine enhancements, educational apps, automation scripts, and tools built across every version of SWMM from 3 to 5+.

## What's Here

```
swmm5-dickinson/
│
├── enhancements/                        ← Patches to the EPA SWMM5 engine
│   ├── twolayer-infiltration/           ← Two-layer soil model via LID reuse
│   │   ├── src/                             lid_twolayer.h, lid_twolayer.c
│   │   ├── examples/                        Example .inp files
│   │   └── docs/                            Theory guide, OpenSWMM submission
│   ├── improved-hydraulics/             ← Surcharge, Preissmann slot, transitions
│   └── wasm-engine/                     ← SWMM5 → WebAssembly via Emscripten
│
├── apps/                                ← Interactive educational tools
│   ├── vibe-coding/                         Replit & Lovable app source
│   └── code-browser/                        SWMM5 C source explorer
│
├── scripts/                             ← Automation & conversion
│   ├── ruby-icm/                            InfoWorks ICM Ruby scripts
│   └── python-swmm/                         PySWMM & swmm_api utilities
│
└── docs/                                ← Cross-cutting documentation
```

---

## Enhancements

### Two-Layer Infiltration · [`enhancements/twolayer-infiltration/`](enhancements/twolayer-infiltration/)

SWMM5's three built-in infiltration methods (Horton, Green-Ampt, Curve Number) all treat the soil as a single uniform layer. Real soil profiles have distinct horizons — sandy loam over clay, topsoil over hardpan — and the interface between layers controls how fast water moves downward.

This enhancement adds two-layer soil infiltration to standard subcatchments by reusing the existing LID control's soil layer machinery and the proven percolation equation already in `lid_proc.c`. The approach is surgical: one new keyword (`SOIL2`), one new flag (`UseAsInfil`), roughly 39 lines touched in existing code. Every existing INP file runs identically.

```ini
;; Define a two-layer soil profile as a LID control
SandyLoamClay    SOIL   12.0  0.453  0.190  0.085  0.43  4.33  0.30    ;; Upper layer
SandyLoamClay    SOIL2  24.0  0.464  0.310  0.187  0.04  8.22  0.15    ;; Lower layer

;; Assign to any subcatchment with a single flag
[LID_USAGE]
S1  SandyLoamClay  0  0  0  0  0  0  *  *  0  1    ;; UseAsInfil = 1
```

The core percolation equation, borrowed directly from `lid_proc.c :: soilFluxRates()`:

```
perc = Ksat × exp(-15.0 × (1.0 − θ/porosity))
```

Upper layer percolation becomes the lower layer's input. If the lower layer saturates, it throttles the upper layer. Simple, physically based, and already validated by every LID simulation ever run in SWMM5.

→ [Source code](enhancements/twolayer-infiltration/src/) · [Example INP](enhancements/twolayer-infiltration/examples/) · [Integration guide](enhancements/twolayer-infiltration/src/INTEGRATION.md) · [Documentation](enhancements/twolayer-infiltration/docs/)

---

### Improved Hydraulics · [`enhancements/improved-hydraulics/`](enhancements/improved-hydraulics/) · *planned*

Targeted fixes for known dynamic wave solver issues. The goal is better stability without sacrificing speed:

| Problem | Current SWMM5 Behavior | Proposed Fix |
|---|---|---|
| Preissmann slot | Fixed width (~1% of pipe diameter) | Adaptive narrowing as pressure stabilizes |
| Crown transition | Oscillation at surcharge/free-surface boundary | Damped transition with hysteresis band |
| Supercritical flow | Abrupt Froude limiter cutoff | Smooth blending across flow regime transitions |
| Junction losses | Continuity-only (no head loss at junctions) | Optional momentum-based head loss |
| Pond/pipe coupling | Instability when storage surface area is small | Relaxation factor for stiff coupling |

These are the issues I've watched modelers struggle with since SWMM3. Each fix is informed by how InfoWorks ICM handles the same problem — taking what works and adapting it for SWMM5's architecture.

→ [Design notes](enhancements/improved-hydraulics/docs/)

---

### WASM Engine · [`enhancements/wasm-engine/`](enhancements/wasm-engine/) · *in progress*

EPA SWMM5 compiled to WebAssembly via Emscripten. This is what makes the vibe coding apps possible — a full SWMM5 simulation engine running client-side in any browser, no install required.

```bash
emcc src/*.c -o swmm5.js \
  -s MODULARIZE=1 \
  -s EXPORTED_FUNCTIONS='["_swmm_run","_swmm_open","_swmm_start","_swmm_step","_swmm_end"]' \
  -s EXPORTED_RUNTIME_METHODS='["ccall","cwrap","FS"]'
```

```javascript
const swmm = await SWMM5();
swmm.FS.writeFile('model.inp', inpContent);
swmm.ccall('swmm_run', 'number', ['string','string','string'],
           ['model.inp', 'report.rpt', 'output.out']);
const report = swmm.FS.readFile('report.rpt', { encoding: 'utf8' });
```

→ [Build scripts](enhancements/wasm-engine/scripts/)

---

## Apps

### Vibe Coding Apps · [`apps/vibe-coding/`](apps/vibe-coding/)

I started calling them "vibe coding apps" because the workflow is: describe what you want the hydraulics to look like, let AI generate the interface, then correct the engineering. The result is interactive educational tools that would have taken weeks to build traditionally.

Each app runs in the browser with no backend. Most are deployed on Replit or Lovable:

- **Infiltration Explorer** — Horton, Green-Ampt, Curve Number, and Two-Layer compared side by side with real-time parameter sliders
- **RTK Hydrograph Generator** — Interactive RDII unit hydrograph tool with R, T, K parameter exploration
- **Manning's Calculator** — Visual open channel flow with depth, velocity, and flow area
- **Design Storm Generator** — SCS Type I/IA/II/III distributions with custom IDF curves
- **Rain Garden Engine** — Full LID bio-retention simulation ported from `lid_proc.c`
- **SWMM Network Builder** — Drag-and-drop network construction
- **SWMM5 Report Reader** — Parse and chart any `.rpt` file (up to 3,000 charts from one run)
- **InfoSewer to ICM App** — Step-by-step migration wizard for the March 2026 ArcMap deadline

### Code Browser · [`apps/code-browser/`](apps/code-browser/)

SWMM5 has 40+ C source files and hundreds of functions. The code browser generates Sankey diagrams showing how data flows through the engine — from rainfall input through runoff, routing, and output. Useful for understanding what happens when you call `swmm_step()`.

---

## Scripts

### Ruby ICM Scripts · [`scripts/ruby-icm/`](scripts/ruby-icm/)

InfoWorks ICM exposes its entire data model through a Ruby scripting API. These scripts automate the tasks I do most often:

- **InfoSewer → ICM conversion** — Complete migration suite reading `.IEDB` files directly (no ArcCatalog needed). Critical for the March 2026 ArcMap discontinuation.
- **InfoSWMM → ICM migration** — Multi-scenario import with post-import cleanup
- **RDII analysis** — RTK parameter fitting and unit hydrograph management
- **Network QA/QC** — Trace upstream/downstream, find disconnected nodes, compare scenarios
- **Batch export/import** — ODEC/ODIC automation for CSV, GIS, and database formats

See also: [Innovyze Open-Source-Support](https://github.com/innovyze/Open-Source-Support) for the full 578-script library.

### Python SWMM Scripts · [`scripts/python-swmm/`](scripts/python-swmm/)

PySWMM and swmm_api workflows for batch simulation, parameter sweeps, and results extraction.

---

## Timeline

This repository exists because SWMM has been a continuous thread through my entire career:

| Year | SWMM Version | What Happened |
|---|---|---|
| 1974 | SWMM 2 | First model run. Punch cards. University of Florida. |
| 1981 | SWMM 3 (Extran) | CDM publishes the Extran manual with 7 test files I still use today |
| 1988 | SWMM 4 | Co-authored the User's Manual with Wayne Huber (EPA/600/3-88/001a) |
| 2004 | SWMM 5.0 | CRADA project with EPA. I coded the RTK/RDII implementation. |
| 2005–2023 | InfoSWMM | 18 years at Innovyze building commercial SWMM tools, RDII Analyst |
| 2023 | SWMM5+ | Joined CIMM.org Technical Advisory Committee as Chair |
| 2024 | ICM SWMM | Transitioned to Autodesk Water, bridging SWMM5 and InfoWorks ICM |
| 2025 | This repo | Started collecting engine patches, WASM builds, and vibe coding apps |
| 2026 | **Now** | Fixathon Series. ArcMap deadline. Migration tools for the whole industry. |

---

## Related Repositories

| Repository | What It Contains |
|---|---|
| [USEPA/Stormwater-Management-Model](https://github.com/USEPA/Stormwater-Management-Model) | Official EPA SWMM5 source code |
| [innovyze/Open-Source-Support](https://github.com/innovyze/Open-Source-Support) | 578 Ruby scripts + 139 SQL for InfoWorks ICM, InfoAsset, WS Pro |
| [pyswmm/pyswmm](https://github.com/pyswmm/pyswmm) | Python wrapper for SWMM5 |
| [CIMM-ORG/SWMM5plus](https://github.com/CIMM-ORG/SWMM5plus) | SWMM5+ Fortran engine with finite volume solver |

---

## Resources

- **Blog:** [swmm5.org](https://swmm5.org) — 1,700+ posts on SWMM, ICM, Ruby scripting, and hydraulic modeling
- **Newsletter:** [The Dickinson Canon](https://www.linkedin.com/in/robertdickinson/) on LinkedIn
- **SWMM5+ TAC:** [CIMM.org](https://cimm.org) — Next-generation SWMM development
- **Community:** [OpenSWMM.org](https://www.openswmm.org)

---

## Author

**Robert E. Dickinson**
Autodesk Water Technologist · Chair, SWMM5+ Technical Advisory Committee (CIMM.org)

52 years of continuous SWMM development. Co-author of the SWMM4 User's Manual. Coded the RTK/RDII implementation for SWMM5. 18 years building commercial SWMM tools at Innovyze. 1,700+ blog posts on swmm5.org. Currently leading migration tools and educational apps for the water infrastructure community.

## License

MIT — See [LICENSE](LICENSE).

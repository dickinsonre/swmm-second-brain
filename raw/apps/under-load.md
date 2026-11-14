---
name: Under Load
file: under-load.html
version: 1.4.0
date: 2026-11-11
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/35Mk2VWqikVq41acLximAm", netlify: none yet, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "github.com/USEPA/Stormwater-Management-Model tag v5.2.4", license: public domain, build: "zig 0.17.0 cc, wasm32-wasi, -O2", sha256: 661fc2b6731b310a6ef4b938f44c8f94e1fb0ad31a9ed124cb046945e1eaab7d}
  - {name: EPA SWMM (unpatched control), version: 5.2.4, source: same tag, build: same, sha256: 5847388be4f868a122618504b075dd49528610824599d4885c2a45c6576d36cf}
units: US customary on screen (cfs, ft, ft3); file units CFS, GPM, MGD, CMS, LPS, MLD are converted
ai_use: built with Claude (Anthropic); see AI use
---

# Under Load: eight office-hours ideas tested on a real SWMM 5.2.4 engine in the browser

## What it does
Runs EPA SWMM 5.2.4 (WebAssembly, in a Web Worker, nothing sent to a server) and wraps it in eight
instruments, one per office-hours topic. The main one answers: how far is this model's design storm
from the next regime change (a pipe running full, a node flooding, a weir spilling, a flow reversing)?
Others: a butterfly test (1% load nudge), a physics-scored highlight reel of the .out, an agent stamp
(evidence contract for a model edit), an under-relaxation (omega) sweep, explained-vs-evidenced claims,
a machine-readable agent card, and a career timeline. For SWMM modelers and for people asking what an
AI agent may claim about a model.

## How it computes
- **Load knob.** Multiplier x scales every value of each rain gage's time series and the scale factor
  and baseline of every FLOW row in [INFLOWS]. Rows are parsed as table.c `table_readTimeseries()`
  does: name, then repeated [date] time value. Dry-weather flow ([DWF]) is not scaled; the page says so.
  At x = 1 and roughness x1 the engine receives the loaded file to the character.
- **Roughness knob.** Scales Manning n in [CONDUITS] (token 4), [TRANSECTS] NC rows (tokens 1-3) and
  [STREETS] (nRoad token 4, nBack token 10). SWMM overwrites a conduit's n from its transect or street
  for IRREGULAR and STREET shapes (link.c `conduit_validate`).
- **File grammar.** Section headers resolved as input.c `findmatch()` does: first keyword in
  SectWords order that the token begins with, any case. IDs compared without case
  (hash.c `UCHAR(s1[i]) == UCHAR(s2[i])`); quotes around a series name are dropped when matching. Every occurrence of a repeated section is read.
- **Regime signature.** P = conduits that ran full, F = nodes that flooded, W = weirs that spilled,
  R = conduits whose flow reversed; sets of IDs, not counts. Flooding is read from the .rpt Node
  Flooding Summary and Flow Routing Continuity (accumulated every routing step), not from .out frames.
- **Edge finder.** Sweep x = 0.25 to 2.50 by 0.05, plus 0.85 to 1.25 by 0.01. Where adjacent samples
  differ in signature, bisect to 0.25% of load, refining from every sample taken, with a budget of 48
  runs per sweep step; what is not pinned stays an open bracket. Verdict: NEAR EDGE if flooding is
  within 10% of design load, WATCH within 25%, CLEAR beyond, OVER THE EDGE if design floods,
  UNRESOLVED if the design run failed or any failed run, open bracket or gap lies between design and
  the top of the first flooding bracket, CLEAR WITHIN THE SWEEP if nothing floods in range.
- **Butterfly.** Two runs, x and x(1 + eps), eps = 0.01 by default. Amplification = relative change of
  an output / eps, with a resolution from the printed digits of the .rpt (flooding prints to 0.001 acre-ft = 43.56 ft3).
- **Omega.** One engine patch: dynwave.c line 239 `Omega = UL_Omega;` (was `Omega = OMEGA;`, 0.5),
  settable per run. Read only by the dynamic wave solver; under KINWAVE or STEADY the sweep refuses to run.
- **Reel.** Per-frame interest = wMotion x (sum over nodes of |HGL change|, normalized) + wEvent x
  named events (first rain, peak rain, first full pipe, first flooding, most pipes full, peak outflow,
  last flooding, recession). Candidate windows are ranked by score; events are credited to the clip
  whose frames contain them. Times come from the .out (first frame = one report step after start).
- **Stamp.** Before/after .inp compared section by section, object by object, field by field; each
  field has a class (geometry, topology, operations, calibration, load, solver, boundary condition,
  initial condition, identifier). A link that keeps both end nodes is a rename. Unpaired objects are
  flagged. Each check needs a finite number from a file; a missing one is UNKNOWN and blocks COMPLETE.
  Limits (default 1% continuity, 5% steps not converging) are saved with the stamp.
- **Identity.** Every result carries model sha256, load, roughness, omega and engine sha256, taken
  when the run is submitted. A result whose identity no longer matches the page is marked stale.

## Inputs and outputs
- Reads: SWMM 5 .inp (any flow unit). Models that reference external files ([FILES], rain gages
  that read a FILE, TIMESERIES FILE, climate files) are refused with the lines that caused it.
- Writes into every loaded model's [REPORT]: SUBCATCHMENTS ALL, NODES ALL, LINKS ALL, CONTINUITY YES,
  FLOWSTATS YES, and DISABLED NO if DISABLED YES was present. The page lists what it changed.
- Exports: scaled .inp, sweep CSV, omega CSV, edit list (CSV, JSON), reel video (WebM), stamp JSON,
  agent card (JSON, MD), evidence package (.zip: exact .inp run, .rpt, .out, settings, sha256 of each
  file, test manifest), the Doc essay (.docx), this file.

## Checks
Mechanical, all on the real engine:
- **Null effect of the patch.** Patched engine at default omega, patched at omega = 0.5, and the
  unpatched build: byte-identical .out (sha256) on 72 of 72 EPA regression models that run
  (73 in github.com/USEPA/swmm-nrtestsuite; one reads a rain file by a Windows path).
  47 of them are embedded and rerun in the About tab (about 15 s); in Node all 47 reproduce the manifest hashes.
- **wasm vs native x86-64 gcc**, same source: identical on 63 of 72. Largest difference: model
  user5, link 647, 16.19 of 168.73 cfs (9.6% of its peak). Recorded in the manifest; not rerunnable in a browser.
- **Browser equals Node.** Narrows at 1.00x: .out sha256 49861af1f71a65fc..., peak 247.058365 cfs.
- **Evidence package.** run.inp from a package, rerun on the native unpatched build: same .out sha256.
- **Narrows preset, design storm.** Signature P3 · F0 · W0 · R0. Next edge +1.88% (conduit A2-A3 runs full).
  Next flooding edge +6.62% (node A3 floods). 23 edges, 124 runs, 0 failed.
- **.rpt vs .out flooding.** Fine scan 0.96x to 1.26x by 0.004 (75 steps), SWMM's settings: .rpt total
  decreases 0 times, .out frame sum decreases 9 times. At omega = 1.0 the .rpt total decreases 10 times.
  First .rpt flooding: 1.084x as shipped, 1x with a fixed 2 s routing step.
- **Units.** Narrows at 1.30x: 19,210 ft3 of flooding with FLOW_UNITS CFS, 19,210 with GPM, 19,210 with MGD.
- **Butterfly, Narrows at 1.30x, eps 1%.** Flooding 19,210 to 21,127 ft3: amplification 9.98 +/- 0.23. Outfall peak 0.04.
- **Omega, Narrows at design.** 0.1: 87 ft3 flooding, 2.22% steps not converging, continuity -0.969%.
  0.5: 0 ft3, 0.79%, -0.089%. 1.5: 40,424 ft3, 36%, 5.401%.
  Settings agree (peak within 1%, flooding within 1,000 ft3, continuity under 1%, under 5% not converging)
  from 0.3 to 0.9 (Narrows), 0.2 to 1 (Crest), 0.2 to 1 (Loop).
- **Review probes.** 43 headless-browser checks against the built page (verify/pw6.js), all passing:
  every failure reported by three outside reviews plus the round-4 self-review.
- **Round-4 self-review.** 26 probes of valid file spellings and edge states (verify/r4/probe.js):
  16 failed on v1.3.0, 0 fail on v1.4.0.

Human review: three outside reviews of v1.0.0 (70/100), v1.1.0 (83) and v1.2.0 (84). None of v1.3.0 or v1.4.0.

## What this does not show
1. Calibration. The three invented presets (Narrows, Crest, Loop) describe only themselves; they were sized so the design storm sits near capacity.
2. Chaos in the mathematical sense. No Lyapunov exponent. "Edge" = regime boundary along a load axis; "amplification" = ratio of relative changes.
3. That the sweep found every edge. A flooding episode narrower than the gap between two samples with the same signature is invisible. Recorded case: flooding from 1.021x to 1.023x between samples at 1.02x and 1.03x is not seen (probe J2).
4. Physical accuracy. Agreement across omega, time step or iteration limit is numerical agreement.
5. SWMM6 behavior. The engine is SWMM 5.2.4; the "Edge Proximity Summary" is a proposal.
6. Models that read external files.
7. Whether an agent's edit is right. The stamp records evidence; judgment stays with an engineer.
8. Not checked by a person: the preset networks against design practice; the Doc essay line by line; interactive visual QA in a real browser (tests are headless).
9. Thresholds (10%/25% verdict bands, 1% continuity, 5% not converging, 0.5 cfs link floor) are the app's choices, not EPA's.

## How to reproduce
- Engine: pip install ziglang; apply engine/dynwave.c.patch and engine/swmm5.c.patch to tag v5.2.4;
  `python3 -m ziglang cc -target wasm32-wasi -O2 -s -Iinclude -D_WASI_EMULATED_PROCESS_CLOCKS -D_WASI_EMULATED_SIGNAL -w *.c -o ul_swmm524.wasm -lwasi-emulated-process-clocks -lwasi-emulated-signal`
- Numbers above: node lab/fixtures.js (writes lab/fixtures.json). Regression manifest: node verify/manifest.js.
- Review probes: node verify/pw6.js (Playwright), node verify/r4/probe.js, node verify/review2_core.js, node verify/review3_core.js. Pass an older ulcore.js path as the argument to see the failures.
- In the page: About tab, "Run the self-test" and "Run the regression subset".

## Credits and licenses
- EPA SWMM 5.2.4, U.S. EPA (Lewis Rossman and the SWMM team), public domain. EPA swmm-nrtestsuite regression models.
- EXTRAN Example 1 from the EPA suite. zig (ziglang.org) as the C compiler.
- Office-hours topics: Bob Dickinson's comments on a list drafted with Claude; livestream topics by ashe (@ashebytes).
- Findings in v1.1.0 to v1.3.0 came from three outside reviews.
- App and text: Robert Dickinson, SWMM Enablement.

## AI use
Built with Claude (Anthropic), October and November 2026, under Robert (Bob) Dickinson's direction. He
supplied the eight topics and his answers, the guest questions and the standing requirements for his
apps, and is responsible for the work. Claude compiled the engine, wrote the omega patch, the in-memory
file layer, the parsers, the edge finder, the butterfly and scan tests, the reel picker, the stamp
contract, the three test networks, the charts, the page text, the Doc essay and this file, and ran
every measurement quoted. Versions 1.1.0 to 1.3.0 are Claude's repairs after three outside reviews,
including the correction of a finding Claude had reported as true; 1.4.0 repairs what Claude's own
review found. The checks are mechanical. No person has reviewed the test networks or the text line by line.

## Changes
- `1.4.0 (2026-11-11)`: self-review, 16 of 26 probes failed on 1.3.0. Section headers by SWMM's keyword rule; quoted IDs; roughness in transects and streets; stamp classes for transect NC, force main friction, storage seepage, tidal curves; 1.00x is the file as written; edge refinement from all samples with a run budget; DISABLED YES handled; DWF and non-dynamic-wave notes; this .md.
- `1.3.0 (2026-10-31)`: review 3 (84/100). Time series rows by SWMM's grammar; repeated sections; SI-safe stamp; unpaired objects flagged; limits saved with the stamp; long-run reels; recorder guards.
- `1.2.0 (2026-10-31)`: review 2 (83/100). Case-insensitive IDs; rename-aware stamp; per-run convergence; submit-time identity; unresolved brackets reach the verdict; Outfall System row; reel event credit.
- `1.1.0 (2026-10-31)`: review 1 (70/100). UNKNOWN for missing diagnostics; failed sweeps; unit conversion; result identity and staleness; .out timestamps; reel weights; field-level change classes; evidence package; regression rerun in page. Correction: the "ragged edge" and 617x amplification of 1.0.0 were .out sampling artifacts.
- `1.0.0 (2026-10-29)`: first build.

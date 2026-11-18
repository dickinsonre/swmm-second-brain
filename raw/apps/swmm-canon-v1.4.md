---
name: SWMM Canon
file: swmm-canon.html
version: "1.4"
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/SqbmY53dtpr545EhB8gNBJ", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, role: "reference engine for parsing and default rules and for the Evidence runs; the page reads .inp and .out and runs no engine"}
hash_tag: swmm-canon-v5
units: the model's own
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built by Claude from Robert Dickinson's starting idea. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/SqbmY53dtpr545EhB8gNBJ, version 1793654738-13ed (index.html, 2,460,917 bytes, SHA-256 b387bb4961608d8718dbc91ea7912470e761d5ce7bd7c076c5cab0f4abe4df6c), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# SWMM Canon: layered, hash-addressed fingerprints for SWMM 5 input files

## In three points
- **What:** Gives every SWMM 5 .inp five fingerprints, each forgetting one more kind of difference (bytes, spelling, order, names, and the defaults EPA fills in), plus a sixth for the .out; the lowest fingerprint two files share says what separates them.
- **So what:** Export, read and export again gives the same bytes on 428 corpus models, and on 145 finished corpus models run as saved and as their canonical export, 126 gave bit-identical results for every object, because EPA adds flows in file order.
- **Now what:** Use it to tell whether a GUI save, a converter or a renaming changed the model or only the file, and audit a round trip through another program. Same L4 means the same model, not the same arithmetic, and an equal L3 hash is not a proof.

This summary was written after the fact. The page ships no technical summary of its own. Its app version (1.4), hash tag (swmm-canon-v5) and build date (Nov 2, 2026) are the page's own. The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

The idea came from an RFC infographic for a layered, hash-addressed cons-tree language (LCVM v1): every value a tree of atoms and pairs, every tree addressed by the hash of its canonical form, each layer adding one capability. The page builds that ladder for SWMM input: L0 bytes, then spelling, order, L3 names (references are typed edges, including names in [CONTROLS] and [TREATMENT]), L4 "as EPA builds it" (defaults filled per each *_readParams, order hazards H1 to H6 kept as marks), and L5 for the objects [REPORT] writes to the .out. Tabs include Compare, Many files, Canonical text, Evidence, Doc, About, What changed, Name map, Ripple, Order hazards, Behavior (.out), Round-trip audit, External files.

## Results the page reports

- Idempotent and deterministic: export, read, export again gives the same bytes at L2, L3 and L4 on every test file and on 428 corpus models.
- 160 short corpus models run as saved and as their L4 export: of the 145 that finish, 126 bit-identical for every object (system totals, float32 sums, matched in 54), 132 to six significant figures, 7 differ by more than one part in ten thousand of a variable's peak. Four corpus models stop with an error before reporting, with the same code both ways.
- EPA keeps only the last row for an inflow, a dry-weather flow, a coverage, a loading, a buildup or washoff function, a treatment, an inlet usage and an adjustment pattern; an NC row of zeros keeps the previous transect roughness, already scaled by the last meander factor.
- A second review found that the Reordered demo ([SUBAREAS] before [SUBCATCHMENTS], which EPA quietly runs as all pervious) exported at L4 with the original order kept changed surface runoff from 0.000 to 0.035 in; fixed.
- Every one of EPA's 46 section readers was checked for state another section sets (audit_readers.py).

## Checks (as stated on the page)

The page lists a regression suite, a soundness test, a corpus check, a Python second implementation, and engine experiments on the Evidence tab run in EPA SWMM 5.2.4; Claude read the EPA 5.2.4 C source to derive every parsing and default rule and quotes the lines it relied on.

## What this does not show

- An equal L3 hash is a Weisfeiler-Lehman invariant, not a proof of isomorphism; the Name map tab verifies an explicit mapping first.
- L4 knows only the defaults and order hazards listed in Evidence.
- Same L4 means the same model, not the same arithmetic: a different object order can change results by round-off.
- L5 covers only the objects [REPORT] writes to the .out.

## How to reproduce

Open the page and drop two .inp files on Compare, or many on Many files; add .out files for L5. Round-trip audit takes an original and the file that came back from another program, such as InfoWorks ICM's SWMM export.

## Credits and licenses

EPA SWMM 5.2.4 (public domain). The LCVM v1 design note. No license is stated for the page.

## AI use

The page says it was built by Claude, Anthropic's AI model. Bob Dickinson supplied the starting idea, the RFC infographic, and asked for something useful for SWMM. Claude wrote all of the code (the .inp parser, typed atoms, the five hash layers, the Weisfeiler-Lehman matcher, the name-map verifier, the canonical exporter, the .out reader and the page), read the EPA 5.2.4 C source for every parsing and default rule, built the demo models, ran every engine experiment, wrote the Python second implementation, ran the corpus sample, and wrote the essay and the .docx; versions 1.2 and 1.3 added the round-trip audit, field-level explanations, external-file fingerprints, the comparison package, the background worker, and the static checker for EPA's 46 section readers. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.4: current version (hash tag swmm-canon-v5).
- 1.3: static checker for EPA's 46 section readers; name-free tie-breaking for canonical text.
- 1.2: round-trip audit, field-level explanations, external-file fingerprints, comparison package, background worker for Many files.
- 1.1: regression suite, soundness test and corpus check.

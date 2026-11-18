---
name: Exam-First SWMM Harness
file: swmm5-swmm6-loop-harness.html
version: "2026-10-19"
date: 2026-10-19
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://swmm5-swmm6-loop-harness.netlify.app", artifact: "https://claude.ai/artifact/KECKQ6HYSkBn6dq5sKs5zk", repo: none named in the page (a kit of Python scripts is described)}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model @ v5.2.4", note: "built from source, pinned by SHA-256 (3bb276e4daadae55...)"}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: 3c30f1e6, license: Apache-2.0, note: "built from source, pinned by SHA-256 (d7892e951bc027b4...)"}
units: US customary (cfs, ft)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the harness, exam, loop, tests, engine builds and page were made with Claude in one session on 2026-10-19 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/KECKQ6HYSkBn6dq5sKs5zk, version 1792451500-0250 (index.html, 663,394 bytes, SHA-256 893ff4c1a4102ee27c7ef2ef9df75d0b29718f7505677ab09d8ac100a50448e6), its Brief, About and Doc tabs read in headless Chromium on 2026-11-18. The page gives no version number; the version above is its build date. Nothing was run to write this file."
---

# Exam-First SWMM Harness: write the exam first, and let a loop write the harness around SWMM 5.2.4 and OpenSWMM 6

## In three points
- **What:** A calibration and testing harness built on the idea "write the exam before the code": a person's exam of questions and answers is frozen first, then a loop rewrites the 30-line settings block of harness.py one round at a time, keeping an edit only when it scores better on held-out questions, and a sealed third set says at the end how much of the gain was real. The engines (EPA SWMM 5.2.4 and OpenSWMM 6.0.0-alpha.4) never change.
- **So what:** Over 41 rounds of 8 edits (2,148 question gradings, 8 rewrites kept) the held-out score rose from 0.496 to 0.807, but the sealed check rose only from 0.637 to 0.715; the detector went from 9 of 12 to 12 of 12 on sealed pairs, while sealed calibration fell from 0.524 to 0.430 even as its held-out score rose from 0.408 to 0.613. The exam also found two OpenSWMM 6 defects: storage nodes labelled as dividers in the .out (DR-1, with a one-line fix) and finite-volume routing reporting a 12.75 ft junction at 103.4 ft (DR-2, undiagnosed).
- **Now what:** Use the pattern (frozen exam, held-out selection, sealed check) for any harness around an engine, and read the sealed numbers before the selected ones. Everything is a twin experiment on small generated networks with one proposer, one seed and one machine.

This summary was written after the fact. The page ships no technical summary of its own and gives no version number. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Brief, Exam, Loop, Sealed, The file, SWMM5 vs SWMM6, Defects, About, Doc. harness.py has two jobs: calibrate() fits six parameters to an outfall hydrograph; detect() says whether two runs give the same engineering answer. The loop edits a 30-line settings block; 297 lines of library code stay fixed. The proposer that wrote the edits is a rule table that reads the incumbent's training failures and writes 8 edits, each with a justifying sentence; an LLM proposer with the same contract is in the kit, tested only against a stub server. The idea came from a post Bob shared (harness.py, 300 Kimi K3 workers, 37 rewrites in 41 rounds); its author is not named in the pasted text.

## Defects the page reports (OpenSWMM 6, swmm6_rel 3c30f1e6)

DR-1: the output writer casts the internal node type straight into the .out file, where 2 means storage and 3 means divider, but the internal enum numbers them the other way round. The page quotes:

```cpp
// src/engine/plugins/DefaultOutputPlugin.cpp, swmm6_rel 3c30f1e6
writeInt4(static_cast<int>(ctx.nodes.type[uj]));   // internal enum: DIVIDER=2, STORAGE=3
// src/engine/data/NodeData.hpp
enum class NodeType : int8_t { JUNCTION = 0, OUTFALL = 1, DIVIDER = 2, STORAGE = 3 };
```

The engine already has internal_to_c_node_type() for this conversion, and its programming interface uses it.

DR-2: on network P17, a chain of five junctions SWMM 5.2.4 never surcharges, FLOW_ROUTING FV reports maximum depths of 79.2 ft at J2 and 103.4 ft at J3 (11.50 and 12.75 ft deep), with routing continuity 0.0%. The spike does not settle as the routing step shrinks and disappears only at 0.5 s. P17 is the only one of 24 networks where this happens.

## Checks (as stated on the page)

Every score is an engine run graded by the frozen grader; the harness graded twice gives identical records; the engines give byte-identical .out files run to run; tests/test_core.py checks pins, the .out reader on both engines, the parameter contract and the exam hashes. A run refuses to start on any other binary.

## What this does not show

As the page lists it: no field data, so calibration is a twin experiment; small generated networks (three to six subcatchments, circular pipes, dynamic wave, US units), not the 1729 corpus or a real city; six parameters applied to the whole model; one proposer (a rule table, not a language model), one loop seed and one machine; calibration scores from one optimizer seed. The "v00 is the human's guess" framing is a stand-in written by Claude, not a measured human baseline. No person has reviewed the exam, the key or the defect register, and DR-2's cause is undiagnosed.

## How to reproduce

The About tab lists the kit: python3 exam/build_exam.py (once), tests/test_core.py, loop/loop.py --rounds 41 (about 35 min on 2 cores), loop/seal.py, loop/apply.py, loop/export_app_data.py, app/build_app.py; --proposer llm --llm-model qwen3:4b for a local model. The kit's binaries are Linux x86-64.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); OpenSWMM 6 (HydroCouple, Apache-2.0). No license is stated for the page.

## AI use

The page says: the harness, its exam, the loop, both proposers, the tests, the engine builds and the page were made with Claude, Anthropic's AI model, in one session on 2026-10-19 under the direction of Robert (Bob) Dickinson, who asked for a SWMM5 and SWMM6 calibration and testing harness built on the "write the exam before the code" idea. Claude built both engines, wrote the generator, the exam and key, the grader, harness v00, both proposers, the loop and the page; found DR-1 and checked its one-line fix; measured DR-2. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2026-10-19: the build read.

---
name: Teacher-Forced SWMM
file: teacher-forced-swmm.html
version: 1.0
date: 2026-10-25
written: 2026-11-14
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/XenWxFVzGo9hgfxvpGPSsm", netlify: "https://teacher-forced-swmm.netlify.app (not read for this summary; it may serve another build)", repo: none recorded in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model, tag v5.2.4", license: public domain, use: "runs in the page as WebAssembly, 843,845 bytes, sha256 2eeb51fdc31c57c9657d4851e7fe8a49de4ef530b06aceb3922fd2b6101beca6, with switches added for the precise restart, the duration fix and the slot variants; with every switch off its output is byte-identical to stock 5.2.4"}
units: US customary (cfs, ft, hours) in every stored example. Differences are shares of each element's own peak in engine A's free run.
ai_use: the app was built with Claude (Anthropic). This summary was written by Claude from the page's source. See AI use.
written_from: "the published artifact's page source, its About tab, its embedded build record (script#data-build) and its embedded Doc essay (script#data-essay), read on 2026-11-14. No engine was run and no test was rerun to write this file."
---

# Teacher-Forced SWMM: where in a run two engine versions come to differ

This summary was written after the fact. The page carries no technical summary of its own. Every number below is copied from the page's About tab, its build record or its Doc essay. Nothing here was measured again. The file name is taken from the name the page gives its exports.

## What it does

It compares two versions of the EPA SWMM 5.2.4 engine, A and B, in two ways. The ordinary way lets both run free from the start. The second way restarts engine B from engine A's exact state at each restart time and measures what B does in one short window. The page borrows the second idea from the training of language models, where it is called teacher forcing. Setting the two measures side by side shows whether the network carries a change, amplifies it, or undoes it.

The user picks a model and a change for engine B: Preissmann slot momentum variants 1, 2 or 4, inertial damping FULL or NONE, roughness times 1.10, a head tolerance of 0.0005 ft, EXTRAN surcharge against SLOT, or options typed in.

Version line in the page: "Version 1.0 · October 25, 2026 · SWMM Enablement".

## How it computes

The machinery is SWMM's hot start file. Engine A runs to a restart time and saves a hot start. Two short runs start from that file and end one window W later: A again, and B. Windows tile the whole simulation. The default window is 5 minutes.

Three differences are taken at the end of each window, per element, each scaled by that element's peak in A's free run:

- **L**, teacher-forced: B forced minus A restarted.
- **R**, restart: A restarted minus A running free. It is the null control and must be zero.
- **G**, free-run: B free minus A free.

G = L + I, where I is the inherited part. The page reports four numbers:

- Exposure ratio E: the sum of |G| over the sum of |L|.
- Tail share: the fraction of the free-run difference in windows where the change is not acting.
- Compensated share: the share of active element-windows where |G| is less than half of |L|.
- Memory time τ: fitted to the decay of the free-run difference after the change stops acting.

**The engine's changes, from the build record.** Four patches to EPA SWMM 5.2.4: runtime momentum variants in `dwflow.c` (0 stock, 1, 2, 4); the precise restart sidecar (`tfprecise.c`); duration rounding in `project.c` under the precise flag; and two exported setters, `swmm_setVariant` and `swmm_setTfPrecise`, with two stand-ins (`mkstemp`, `realpath`) for wasi-libc.

**The stock hot start failed the null control.** From the build record, on the slot versions of three EXTRAN examples:

| Model | Restarts | Stock hot start: exact | Stock: worst flow change, cfs | Precise restart: exact |
|---|---|---|---|---|
| EXTRAN example 1 | 94 | 0 | 1.457588 | 94 |
| EXTRAN example 4 | 94 | 0 | 1.725739 | 94 |
| EXTRAN example 7 (pumps) | 94 | 0 | 5.0 | 94 |

The essay says the stock restart moved flows by those amounts within five minutes. It lists five pieces of solver state that do not survive a stock restart:

| ID | Where | What |
|---|---|---|
| R-1 | `hotstart.c:234-236`, links at 253-256 | Routing state is written as 32-bit floats |
| R-2 | `flowrout.c:496` with `dwflow.c:287` | Conduit area is rebuilt from link depth on restart |
| R-3 | `dynwave.c:674` with `node.c:303` | The trapezoidal volume update uses the last step's net inflow |
| R-4 | `dynwave.c:140` with `dynwave.c:728` | Surface area from the last non-surcharged step is reset to 0 |
| R-5 | `dynwave.c:209-212` | The variable time step restarts at the minimum |

The page's build writes a sidecar file beside the hot start, in double precision, that carries those five things. The essay says none of the five is a bug in ordinary use.

One more item is called a defect: D-1, `project.c:165`, where the total duration is floored to whole seconds. A run from midnight to 00:50 gets a duration of 2999 seconds, its last routing step is 19 seconds, not 20, and the hot start is written one second before the stated end. The build record's measurement: the final routing step ends at 2,999,000 ms instead of 3,000,000. The page's build rounds to the nearest millisecond before flooring.

The slot variants were written from the descriptions in EPA issue 231 and the earlier Slot Lab work, not from a patch file. Variant 1 computes velocity from no more than the full area. Variant 2 does that in the friction term and caps the weighted area in the head term. Variant 4 takes the slot out of every momentum term while continuity keeps it. The essay says Lew Rossman's own changes are not included.

## Results as stored

All on EXTRAN user's manual examples and EPA Example 2 from the 1729 corpus.

| Case | What the essay reports |
|---|---|
| EXTRAN to SLOT surcharge, example 1, conduit 8060 | Forced difference 80 % of the conduit's peak against 79 % free-run at 0.58 hours. The forced segment ending at 0.75 hours is 13 % above A while the free run is 9 % below it. From about 0.8 hours on, 7.5 % against 7.2 %. |
| Slot velocity fix, slot version of example 1 | Teacher-forced difference is zero until the window ending at 0.67 hours, near 1.5 % of peak through the surcharge plateau, and gone after the window ending at 3.3 hours. Maximum 1.52 % free-run against 1.55 % teacher-forced. Memory time 0.61 hours. The tail is 4 % of the free-run difference. |
| Same fix, example 4, conduit 8040 | Teacher-forced flow difference a steady 1 % in every window while the free-run flow difference fades to nothing. In one long forced window from 1.5 hours, upstream node 80408 gains about a third of a foot of head over half an hour; the forced flow difference peaks near 0.6 cfs about three minutes in. |
| Inertial damping FULL | Exposure ratio 0.45 on example 1 and 0.58 on EPA Example 2, with 47 to 59 % of active element-windows compensated. |
| Head tolerance tightened by a factor of ten, slot version of example 1 | The change acts in 18 of 95 windows. The free-run difference is 2.5 times the teacher-forced total for flow and 3.3 times for depth, and 23 % of it lands in windows where the change did nothing. |
| Every roughness raised 10 % | Teacher-forced difference is nonzero in every window. The free-run depth difference runs 2.8 to 4.4 times the teacher-forced one. |

The essay's exposure-ratio figure covers eleven model-and-change pairs.

## Checks

Mechanical, from the essay's verification section:

- With all switches off, the page's engine writes `.out` files byte-identical to stock EPA SWMM 5.2.4 on eight EXTRAN test models, and on five of them again after each later patch.
- The WebAssembly build is byte-identical to the native build on 15 of 15 runs: five models (three EXTRAN slot examples, EPA Example 2 and user2) times variants 0, 1 and 4.
- The browser harness and the command-line harness agree on 11,115 per-element numbers from two experiments, with zero difference.
- The precise restart is bit-exact on 282 restarts across three models, against 0 of 282 for the stock hot start.
- Rewriting date-less time series to absolute dates changes nothing in all 25 matrix runs.
- Each experiment reruns the restart null control and shows the result. The page says the restart null was exactly 0 in every EXTRAN run and at most 7.2×10⁻⁵ of an element's peak on user2 (17 subcatchments, 72 nodes, 102 links).

Human review: none recorded.

## What this does not show

From the page's own list of seven:

1. No observed data. The method says nothing about which engine is right.
2. The teacher-forced number depends on the window. The 5-minute default is a choice.
3. Subcatchments are not bit-exact. On user2, with 17 subcatchments, the precise restart is off by up to 0.007 percent of an element's peak. The source has not been traced.
4. Variable time steps break exactness. A run that stops at a restart time takes a shortened last step that the free run never takes.
5. Different engines need a shared state format. Comparing SWMM5 with SWMM6 or ICM this way needs those engines to read and write the same state.
6. Control rules that use SIMULATION TIME are refused. External time series files and other interface files are refused.
7. Eleven model-and-change pairs on small test networks. The essay calls the patterns suggestive and not yet a law.

From the AI-use note: no person has reviewed the slot variant code against EPA issue 231, rerun the experiments on another machine, or checked the interpretation of the eleven cases.

Added by this summary:

8. This file was written from the page, not from the build. No stored result was rerun.
9. The build record gives the engine's size and hash but not its compiler or flags.
10. R-1 to R-5 and D-1 are the page's own IDs. This summary does not map them to any other register.

## How to reproduce

Open the artifact. On the Lab tab pick a sample model or load an `.inp`, pick a change for engine B, leave the window at 5 minutes and press Run. Read the restart status first. Then read the exposure ratio and tail share, the network chart, and the Sweep tab for one long forced window. The per-window CSV can be copied out. The sample models are the EXTRAN user's manual examples (OWA_EXTRAN folder) and EPA nrtestsuite models from SWMMBobSWMM6/1729-SWMM5-Models-2030. To check this summary, view the page source and read `script#data-build` and `script#data-essay`.

## Credits and licenses

- EPA SWMM 5.2.4: USEPA, tag v5.2.4, public domain.
- Slot momentum variants: after the EPA SWMM issue 231 discussion.
- WASI runtime: @bjorn3/browser_wasi_shim 0.4.2 (MIT/Apache-2.0), bundled into the page.
- Teacher forcing: Williams and Zipser (1989). Exposure bias: Ranzato et al. (2015).

## AI use

From the page's essay: the lab and its essay were built with Claude, Anthropic's AI model (Claude Opus 5.5), in one session on October 25, 2026, under the direction of Robert (Bob) Dickinson. He chose the question, asked for the teacher-forced comparison after a discussion of language-model training, and is responsible for the work. Claude read the EPA SWMM 5.2.4 source, wrote the slot variants, the precise-restart sidecar and the duration fix, compiled the engine natively and to WebAssembly, wrote the Python and JavaScript harnesses, ran every experiment reported, drew the figures, built the page and wrote its text, including the code citations and the defect descriptions. The checks are mechanical. No person has yet reviewed the slot variant code against EPA issue 231, rerun the experiments on another machine, or checked the interpretation of the eleven cases.

This summary: written by Claude (model claude-fable-5-2) on 14 November 2026 at Bob's request, from the page source only. Bob has not yet read it.

## Changes

- `1.0 (2026-10-25)`: the build this summary describes. The page records no change history.

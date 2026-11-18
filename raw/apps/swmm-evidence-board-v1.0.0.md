---
name: SWMM Evidence Board
file: swmm-evidence-board.html
version: 1.0.0
date: 2026-11-17
author: Robert Dickinson
links: {artifact: https://claude.ai/artifact/EHhnusPN2dzUwiesVU867s, corpus: https://github.com/SWMMBobSWMM6/1729-swmm5-models-2030, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, via: swmm-toolkit 0.17.0 (PySWMM project), use: build time only, license: public domain}
units: US customary (CFS, ft, in, ac-ft)
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM Evidence Board: simulation interviews and hidden-evidence tests on eight SWMM models

## In three points
- **What:** Eight SWMM models, seven with one planted fault and one clean control, cut into report tiles; the page logs which tiles an experienced modeler opens and in five cases locks the tile that points at the fault until the first diagnosis.
- **So what:** It turns the cues modelers use without naming them into a timed record; all 16 faulty and corrected runs finished in EPA SWMM 5.2.4, and 101 of 104 numbers in the answer tables were found as text in the engine's files.
- **Now what:** Take the cases yourself or hand them to a colleague, then export the record. No person has taken them yet, and one interviewee on eight cases gives anecdotes with a control, not statistics.

The SWMM Evidence Board gives you eight SWMM models, seven with one planted fault and one clean control, records the report sections you open, and in five cases locks the section that points straight at the fault until you commit.

Experienced modelers diagnose SWMM models from cues they rarely mention, because the cues have become habits. This page tries to catch them. Each of eight cases is a model from the public 1729 corpus, or one generated lift station, with one or two input lines changed, and both the faulty and corrected versions run in EPA SWMM 5.2.4. The faulty report is cut into tiles. You open what you would open, write what you see, expect and would do next, and commit a first diagnosis. Only then does the locked tile open, and you may revise. The page logs every step with its time and saves it where Claude can read it. The main limit: one person, eight cases, self-scored.

## What it does
Eight cases, each a SWMM 5 model plus a short brief. The interviewee opens report sections one at a time; the page logs each open with seconds since Begin, logs notes (see / expect / do next) with the tiles open so far, and takes two commits. In five cases the section that points at the fault is locked until the first commit (key lock); in three a helpful but unneeded section is locked (decoy lock, the control). After the second commit the answer, the changed input lines and a faulty-vs-corrected table appear, and the interviewee scores both diagnoses Right, Partly or Wrong.

## The cases
| # | Title | Model | Locked until first commit | Lock |
|---|---|---|---|---|
| 1 | Campus model, 10-year check | 46_Subs (University Storm Drainage Evaluation, 2003) | Runoff Quantity Continuity | key |
| 2 | Pond 25 floods in a 2-inch storm | jason_dorn_storage_example (EPA detention example) | Storage Volume Summary | key |
| 3 | Which peak at link 1040? | OAK (Ft Smith Oak Park, 1992) | Analysis Options | key |
| 4 | New flooding on campus | 46_Subs (University Storm Drainage Evaluation, 2003) | Highest Flow Instability Indexes, Routing Time Step Summary | key |
| 5 | Riverside lift station | generated two-pump lift station (not from the corpus) | Pumping Summary | key |
| 6 | Reviewer says infiltration is broken | jason_dorn_storage_example (EPA detention example) | Graphs | decoy |
| 7 | Manhole J44 overflows | 46_Subs (University Storm Drainage Evaluation, 2003) | Input file | decoy |
| 8 | Node 18 floods all day | jason_dorn_storage_example (EPA detention example) | Graphs | decoy |

Planted changes (diffed, not typed): Case 1: The rain gage reads the 1-year storm, not the 10-year storm. Case 2: Pond 25's surface area was entered in acres instead of square feet. Case 3: The report time step is 30 minutes, so the hydrograph misses the peak. Case 4: The routing step was fixed at 7 seconds, and the short pipes cannot be routed stably at that step. Case 5: The lag pump never starts: its startup depth is 60 ft in a 20-ft wet well. Case 6: Nothing is wrong. This is the control case. Case 7: Conduit C43 has a Manning's n of 0.13, a slipped decimal for 0.013. Case 8: The outfall has a fixed stage of 979.0 ft, above node 18's rim, so the creek pours into the system.

## How it computes
1. `scripts/build_cases.py` copies each model, applies the planted edit, and runs faulty and corrected files with `swmm.toolkit.solver.swmm_run` (EPA SWMM 5.2.4).
2. The faulty .rpt is split at its star-banner section headers into tiles (20 to 29 tiles per case including Graphs, Map and Input file).
3. The faulty .out is read with `swmm.toolkit.output` at the report step: subcatchment rain and runoff; node depth, total inflow, flooding; link flow and velocity; system rain, runoff, flooding, outflow, storage. `scripts/compact.py` rounds to 3 significant figures and pools identical arrays.
4. The map is drawn from [COORDINATES] and [VERTICES]. The corrected run supplies the answer table.
5. Storage: one document per interviewee and case, `interviews/<name-slug>--<case-id>`, in the artifact database (`db` capability), mirrored to localStorage. Record fields: begun (epoch ms), events [[seconds, kind, what]], notes [{t, see, expect, next, open}], c1 {t, dx, conf, tip, open}, c2 {t, dx, conf, change, why, open}, score {first, final, teach, wrong}, updatedAt.
6. Results: per case, tiles opened before the first commit, cue tiles seen of those available, time to each commit, confidence change, scores; key-lock vs decoy-lock tallies.

Continuity identity used in the Doc (EPA SWMM 5.2.4 `massbal.c`, `massbal_getFlowError()`): error % = 100 × (1 − Out/In), In = initial storage + wet weather + dry weather + groundwater + RDII + external inflow, Out = final storage + flooding + evaporation + seepage + reacted + external outflow.

## Inputs and outputs
Reads nothing at run time; the eight cases are embedded. Exports the interviewee's records as Markdown or JSON (copy, or save through the `downloads` capability). Writes only to its own database collection `interviews`.

## Checks
Mechanical:
- 16 runs in EPA SWMM 5.2.4, all without error (control run twice as given).
- Changed lines from a diff of each pair: one line in Cases 1, 2, 3, 5, 7, 8; two in Case 4; none in Case 6.
- `scripts/check_meta.py`: 104 numbers in the answer tables searched for as text in the engine's .rpt and .inp; 101 found. Not found as text: 1135.0 (Case 3, Link 1040 peak on the hydrograph (cfs)); 1904.7 (Case 3, Link 1040 peak on the hydrograph (cfs)); 0.345 (Case 6, Overall runoff coefficient). The two Case 3 peaks were read from the .out by `scripts/figdata.py` (1,135.05 cfs at 12:30 at the 30-min step; 1,904.701 cfs at 12:21 at the 1-min step); 0.345 = 0.707 in / 2.05 in. The search is a substring match, so short values such as 0 or 12 are found trivially; it is strong only for multi-digit values.
- Two planned faults were rejected by the engine: rain gage interval longer than its series interval (ERROR 159), report step shorter than routing step (ERROR 195).
- Complexity: index 54.8 (Size 44.2, Structure 63.5, Test evidence 6.0, SWMM vocabulary 76.1); page code alone 42.5. Meter core 1.7.0, baseline HC-2026-11-10-h, HydroCouple = 100.

Human review: none yet. No person has taken the cases, checked the briefs for leaks, or reviewed the Doc.

## What this does not show
1. One interviewee, eight cases: anecdotes with a control, not statistics.
2. Self-scoring after seeing the answer.
3. The interviewee knows each case has at most one planted fault (Case 6 has none).
4. The log records tiles opened, not what was read in them.
5. No profile plots, status report or object tables: cues that live there cannot appear.
6. The campus model is in Cases 1, 4 and 7; the default order spaces them out.
7. Case 5 is synthetic. Graph values are 3 significant figures at the report step.
8. The answers are in the page source; the test relies on the interviewee not reading it.
9. Times are wall-clock seconds since Begin; breaks count.

## How to reproduce
```
python3 -I scripts/build_cases.py <TI>        # runs 16 models, writes cases/cases_raw.json
python3 -I scripts/compact.py <TI>            # build/cases_data.json
python3 -I scripts/check_meta.py <TI>         # number check, build/check.json
python3 -I scripts/figdata.py <TI>            # build/figdata.json
node app/build.js <artifact-url>              # dist/swmm-evidence-board.html, .md, .docx
```
Models: 46_Subs.inp, jason_dorn_storage_example.inp, OAK.inp from https://github.com/SWMMBobSWMM6/1729-swmm5-models-2030; the lift station from `scripts/liftstation.py`.

## Credits and licenses
EPA SWMM 5.2.4, US EPA (public domain). swmm-toolkit, PySWMM project. Models from the 1729 corpus (SWMMBobSWMM6). Methods: Militello and Hutton (ACTA, 1998); Abernethy and Russell (occlusion, 1987); Payne (information boards, 1976); Nisbett and Wilson (1977); Klein (RPD); Collins (tacit knowledge); Cedric Chin, Commoncog Tacit Knowledge Series. Page and essay by Robert Dickinson.

## AI use
This page and this essay were built with Claude, Anthropic's AI model, in a Claude session in November 2026, under the direction of Robert (Bob) Dickinson. He chose the two methods, simulation interviews and hidden evidence, set the rule that the cases come from his 1729 corpus, and is responsible for the work.

What Claude did. It chose the three corpus models and generated the lift station; designed and planted the eight faults; wrote the build scripts that ran EPA SWMM 5.2.4 and cut the reports into tiles; wrote the briefs, answers and page code, this essay, its Word version and the technical summary; and drew the figures from the engine output.

How it was checked. Mechanically, by the engine runs, the number-matching script and a browser check of the page, as described under What was checked. No person has yet taken the cases, checked the briefs for leaks, or reviewed this essay.

## Changes
`1.0.0 (2026-11-17)`: first release.

---
name: Replit App Catalog
file: replit-app-catalog.html
version: 1.0.0
date: 2026-11-20
author: Robert Dickinson
links: {artifact: claude.ai artifact (private until shared), netlify: none yet, repo: none}
engines: none (reads source code; runs no model)
units: not applicable (sizes in bytes, MB, GB; code in lines)
ai_use: built with Claude (Anthropic); see AI use
---

# Replit App Catalog: all 85 of Bob Dickinson's Replit apps, read from their source zips

This catalog reads Bob Dickinson's 85 Replit apps from their source zips, measures each one's own code against HydroCouple at 100 (median 50.4), and proposes thirteen merges and one retirement that bring 85 apps down to 59.

Bob Dickinson built 85 apps on Replit between July 2025 and November 2026 and saved each as a zip. The zips weigh 4.436 GB; the source inside them fits in 52.6 MB. Each app was unpacked, its shared Replit template set aside by checksum, and its own code measured with the SWMM App Complexity Meter, where HydroCouple is 100. Own code totals 6.76 million lines, 1.09 million without Code Rosetta Stone; the median app scores 50.4. Sorted into eleven families, the apps suggest thirteen merges, 12 rebuilds as single-file Claude apps and one retirement, leaving 59. Only 22 apps need no server. The catalog reads code. It has not run any app, and its descriptions were written by Claude and are not yet checked line by line.

## What it does
Lists all 85 Replit apps with a one-line description, family (11), stack, server class, AI services, own lines of code, a complexity index on the SWMM App Complexity Meter (HydroCouple = 100), git history, deploy state and a recommendation (keep 27, base of a merge 13, fold into a base 25, rebuild as a Claude app 12, personal 7, retire 1). It names 13 merges that take 85 apps to 59. It is step 2 of 5: slim copies, catalog, bug hunt, Replit Agent reports after Bob approves each list, consolidation.

## How it computes
1. Each zip is unpacked on Bob's PC (Linux VM over his Downloads folder). Skipped: node_modules, .git, dist, build, .cache, .local, .upm, .pythonlibs, .config, generated-artifacts, __pycache__, and attached_assets unless the source references the file.
2. Template rule: a file is template if its md5 appears in 5 or more apps, or it is under components/ui. Everything else is own code.
3. Facts from own code: languages by extension; AI client libraries (openai, anthropic, gemini, deepseek, xai); Express server routes; `/api/` calls in client code; env variable names (values never read); MemStorage use; .wasm files; README and Agent-written .md front matter; git first/last dates and commit counts from `.git/logs/HEAD`; remotes from `.git/config`.
4. Server class, first match wins: Ruby script (main language Ruby); Python server (main language Python, or Python over 500 lines plus server routes); AI key (any AI client); Own API (server routes and page /api/ calls both > 0); otherwise Browser only.
5. Complexity: `SACM.analyzeSet(ownFiles)` then `SACM.grade(measure, anchor, undefined, undefined, "soft")`, analyzer 1.7.0, anchor HC-2026-11-10-h. Per dimension: `score = 100 * log10(1 + x/x0) / log10(1 + a/x0)`, `x0 = a * 1e-4`; weighted mean of 8 dimensions.
6. Zip composition: compressed member sizes from each zip's central directory, binned as media (by extension), .git, attached_assets, caches, other.
7. Descriptions, families, merges and recommendations: written by Claude from READMEs, Agent-written .md files and page titles (editorial.py).

## Inputs and outputs
In: 85 zips (4.436 GB) in Bob's Downloads; Bob's dashboard list (name, zip, URL, state, created, opened). Out: this page; replit-app-catalog.md; replit-app-catalog.docx; 85 slim zips (52.6 MB) in Downloads/replit-source/slim-zips; CSV export of the filtered table (31 columns).

## Checks
- pass: 85 apps in the data
- pass: every app has a family, description and recommendation
- pass: family counts add to 85
- pass: every merge base and member exists
- pass: merge members are marked merge, bases marked base
- pass: apps after merges = 85 - members - superseded
- pass: zip bytes add to the stated total
- pass: slim bytes add to the stated total
- pass: own lines add to the stated total
- pass: server classes add to 85
- pass: median complexity matches
- pass: unique section 60 to 120 words
- pass: one sentence 40 words or fewer
- pass: one paragraph 90 to 130 words
- pass: one page 350 to 480 words in 4 to 6 paragraphs
- pass: three to five questions
- pass: every section has a one-sentence summary
- pass: six figures or more in the essay
- pass: one-page image is one of the essay figures
- pass: no em or en dashes in the essay
- pass: no em or en dashes in the descriptions
- 85 slim zips pass Python zipfile.testzip (run on the device, 2026-11-20).
- Zip members total 4.424 GB compressed (file sizes 4.436 GB; the difference is zip headers).
- Complexity of this page (Meter 1.7.0, HC-2026-11-10-h): index 50.3; Size 42.9, Structure 62.3, Test evidence 0, SWMM vocabulary 56.3. Shipped page alone: 38.3.
Human review: Bob corrected app names during download. No person has yet read the 85 descriptions line by line.

## Key numbers
- Zips 4.436 GB; slim 52.6 MB (84x). Weight: media 2.25 GB, .git 1.12 GB, attached_assets 0.68 GB, other 0.37 GB; no node_modules.
- Own lines 6,759,185 (1,090,876 without Code Rosetta Stone); median 5,047 per app.
- 70 apps on the Replit React+Express template; 13 Python-first; 26 call an AI service; 26 use MemStorage.
- Complexity median 50.4; min 25 (Video Search); max 95.1 (Code Rosetta Stone); 7 at 70 or more; 18 under 40.
- Server class: AI key 22, Python server 15, Own API 24, Browser only 22, Ruby script 2.
- Git: 56 zips with history, 3,502 commits, 2025-07-08 to 2026-11-15; 47 apps with a GitHub remote.

## Merges
- **INP Studio**: base SwmmAnalyzer; folds in SWMM5InpReader, SWMM5NetworkAnalyzer, SingaPour Site. Four .inp readers, three of them Streamlit apps that need a Python server. One browser app with the parser from the largest of them removes the server.
- **RPT Studio**: base SWMM5_Report_Reader; folds in SurchargeDetective, SwmmIcmConverter. Three readers of SWMM results. One app built on a single shared .rpt and .out parser (your one-parser rule) does all three jobs.
- **Infiltration Lab**: base SWMM5RunoffInfiltration; folds in SWMM Infiltration, Green Infiltration. Three infiltration calculators covering the same Horton, Green-Ampt and Curve Number methods. The LID version is the most complete base.
- **Quiz Hub**: base SWMM5QuizMaster; folds in EpanetQuizzer, InfoWorksQuizzer, GatorSWMM. Four quiz apps on the same template, each with its own question bank. One quiz engine with SWMM5, EPANET and ICM banks.
- **Network Generator Hub**: base SWMM5 Topo Network Wizard; folds in Fractal SWMMGen, SWMM Attractor, SWMM INP Maker. Four SWMM5 network generators. Ties in with your curve-generator consolidation project.
- **SWMMCRAFT**: base Stormcraft Ultimate; folds in Sewer Inspector Steve. Two copies of SWMMCRAFT Ultimate, plus your single-file swmmcraft-ultimate.html.
- **One SWMM runner**: base Swmm UI Engine; folds in SWMM Engine, Open SWMM Core, Mirofish SWMM, Swmm5AppEngine, WatershedSimulator. Five smaller apps that each run one engine on one model. Swmm UI Engine already runs four engines; the others become engine choices or samples there. BatchSWMMRunner stays separate.
- **SWMM documentation archive**: base SWMM Docs Explorer; folds in SWMM Documents Explorer. Two apps on the same 55-year documentation archive.
- **SWMM Manual Search**: base SJ_SWMM5_Manual_Search; folds in Video Search. Video Search is only a landing page for Manual Search.
- **SWMManywhere**: base SWMManywhere App; folds in Swmmanywhere Explorer. The static guide becomes the help tab of the working app.
- **ICM Ruby Lens**: base ICMFlowVisualizer; folds in RubyMakerAI. Two analyzers of ICM Ruby scripts; RubyMakerAI's deploy has failed.
- **InfoSewer to ICM guide**: base InfoSewerTo_ICM_Steps; folds in RubySwmmImport. Two migration guides into ICM, one for InfoSewer and one for SWMM5.
- **Climate Explorer**: base Temp Monitor; folds in nsWorldrainfall. Temperature and rainfall by city, in one place.

## All apps
| App | Family | Next step | Server | Own lines | Complexity | State |
|---|---|---|---|---:|---:|---|
| AIChatbotDeepseek | Hydrology and hydraulics tools | claude | AI key | 4172 | 50.7 | Published |
| BatchSWMMRunner | Engines and runners | keep | AI key | 160205 | 86.6 | Published |
| BobSWMM Auto Research | AI writing and research | keep | AI key | 28671 | 67.2 | Published |
| BobSWMMWriter | AI writing and research | keep | AI key | 5047 | 43.4 | Published |
| Code Rosetta Stone | Engines and runners | keep | Python server | 5668309 | 95.1 | Published |
| DickinsonInfoHub | AI writing and research | keep | AI key | 3113 | 38.9 | Failed |
| EPANET SWMM Experts | Reference, docs and history | claude | AI key | 14415 | 55.3 | Published |
| EPANET SWMM5 Generate | Network generators | keep | AI key | 19095 | 70.8 | Published |
| EpanetQuizzer | Quizzes and learning | merge (Quiz Hub) | Own API | 3841 | 37.2 | Published |
| FCWaterBalance | Climate, places and Network School | keep | Own API | 12379 | 54.9 | Published |
| FileConverter | ICM, InfoWorks and migration | keep | Own API | 3061 | 44.9 | Published |
| FloodPeakLedger | Hydrology and hydraulics tools | keep | Own API | 5315 | 48.4 | Published |
| FlowCalculatorGuide | Hydrology and hydraulics tools | claude | Own API | 2604 | 40.8 | Published |
| FluidDnaFlow | Hydrology and hydraulics tools | claude | Own API | 3942 | 39.7 | Published |
| ForceMain_SWMM5_EPANET_Comparison | Hydrology and hydraulics tools | keep | Python server | 6475 | 56.6 | Published |
| Fractal SWMMGen | Network generators | merge (Network Generator Hub) | Browser only | 8161 | 55 | Published |
| GatorSWMM | Quizzes and learning | merge (Quiz Hub) | Own API | 3233 | 38 | Published |
| Green Infiltration | Hydrology and hydraulics tools | merge (Infiltration Lab) | Browser only | 2486 | 44.9 | Published |
| HindsightProphet | AI writing and research | keep | AI key | 4251 | 52 | Published |
| HistoricalWaterInventions | Quizzes and learning | keep | AI key | 64900 | 64.7 | Published |
| HydroCouple Explorer | Reference, docs and history | claude | AI key | 9040 | 53.9 | Published |
| ICMFlowVisualizer | ICM, InfoWorks and migration | base (ICM Ruby Lens) | AI key | 3807 | 47.3 | Published |
| ICMNewView | ICM, InfoWorks and migration | keep | AI key | 17140 | 56.5 | Published |
| ICMReader | ICM, InfoWorks and migration | keep | Own API | 3454 | 53.8 | Published |
| ICMRTKAnalyzer | ICM, InfoWorks and migration | keep | Ruby script | 1683 | 44.1 | Published |
| InfoDrainage Explorer | Reference, docs and history | claude | Browser only | 1790 | 32.6 | Published |
| InfoSewerTo_ICM_Steps | ICM, InfoWorks and migration | base (InfoSewer to ICM guide) | Browser only | 4076 | 47.2 | Published |
| InfoSWMM-InfoSewer-Reader | ICM, InfoWorks and migration | keep | Own API | 37976 | 74.2 | Published |
| InfoWorksQuizzer | Quizzes and learning | merge (Quiz Hub) | Own API | 4697 | 32 | Published |
| MarsMoonTracker | Games and personal | personal | Browser only | 1877 | 35 | Published |
| MarsRacketColony | Games and personal | personal | Browser only | 1477 | 35.4 | Published |
| MicroGPT SWMM | Quizzes and learning | claude | Browser only | 2520 | 51.2 | Published |
| Mirofish SWMM | Engines and runners | merge (One SWMM runner) | AI key | 61408 | 70.7 | Published |
| MorningRuckTracker | Climate, places and Network School | personal | Python server | 2909 | 40.4 | Published |
| NetworkSchoolLifestyle | Climate, places and Network School | personal | Own API | 5193 | 34.9 | Published |
| NewsletterGallery | AI writing and research | superseded | AI key | 15511 | 64.1 | Published |
| nsWorldrainfall | Climate, places and Network School | merge (Climate Explorer) | Python server | 4804 | 39.4 | Published |
| Open SWMM Core | Engines and runners | merge (One SWMM runner) | Browser only | 6609 | 59.7 | Published |
| PenguPlanetPaddle | Games and personal | personal | Browser only | 3897 | 41.3 | Published |
| PondFlowSim | Hydrology and hydraulics tools | claude | Own API | 1892 | 36.8 | Published |
| Pyswmm Explorer | Reference, docs and history | claude | Browser only | 5336 | 48.9 | Published |
| Repo Insights | Reference, docs and history | keep | AI key | 14003 | 63.2 | Published |
| RubyMakerAI | ICM, InfoWorks and migration | merge (ICM Ruby Lens) | AI key | 5374 | 43.2 | Failed |
| RubySwmmImport | ICM, InfoWorks and migration | merge (InfoSewer to ICM guide) | Own API | 3942 | 50.4 | Published |
| RubySwmmRouter | ICM, InfoWorks and migration | keep | Ruby script | 3107 | 49.6 | Published |
| Sewer Code Search | Reference, docs and history | keep | Own API | 3408 | 43.7 | Paused |
| Sewer Inspector Steve | Playful model builders | merge (SWMMCRAFT) | Browser only | 1567 | 42.2 | Published |
| SG_FC_Challenge | Climate, places and Network School | personal | Own API | 3360 | 37.1 | Published |
| SingaPour Site | Model readers and analyzers | merge (INP Studio) | Own API | 2550 | 49.2 | Published |
| SingingPoreRain | Quizzes and learning | claude | Browser only | 6604 | 49.6 | Published |
| SJ_SWMM5_Manual_Search | Reference, docs and history | base (SWMM Manual Search) | Python server | 19486 | 69.7 | Published |
| Spatial Impact Insight | Climate, places and Network School | keep | Browser only | 4181 | 40.9 | Published |
| SpeechBuddy | Games and personal | personal | Own API | 3405 | 39.3 | Published |
| SSOAP Engine | Hydrology and hydraulics tools | keep | Own API | 23792 | 63.1 | Published |
| Stormcraft Ultimate | Playful model builders | base (SWMMCRAFT) | Own API | 8269 | 57.7 | Published |
| SurchargeDetective | Model readers and analyzers | merge (RPT Studio) | AI key | 2931 | 51.8 | Published |
| SWMM Attractor | Network generators | merge (Network Generator Hub) | Browser only | 8219 | 56.2 | Published |
| SWMM Docs Explorer | Reference, docs and history | base (SWMM documentation archive) | AI key | 15366 | 59.9 | Published |
| SWMM Documents Explorer | Reference, docs and history | merge (SWMM documentation archive) | Browser only | 1419 | 32 | Published |
| SWMM Engine | Engines and runners | merge (One SWMM runner) | Own API | 19273 | 66.5 | Published |
| SWMM Explorer | Reference, docs and history | keep | AI key | 57032 | 73.3 | Published |
| SWMM Filebase | Model readers and analyzers | keep | Own API | 23204 | 69.5 | Published |
| SWMM ICM StVenant | Reference, docs and history | claude | Browser only | 28148 | 63 | Published |
| SWMM Infiltration | Hydrology and hydraulics tools | merge (Infiltration Lab) | Browser only | 2618 | 44.4 | Published |
| SWMM INP Maker | Network generators | merge (Network Generator Hub) | Own API | 15563 | 64.7 | Published |
| SWMM Lego Model | Playful model builders | keep | AI key | 7741 | 69.3 | Published |
| Swmm UI Engine | Engines and runners | base (One SWMM runner) | AI key | 116525 | 85.3 | Published |
| SWMM5 Topo Network Wizard | Network generators | base (Network Generator Hub) | Own API | 10348 | 58.4 | Published |
| SWMM5_Report_Reader | Model readers and analyzers | base (RPT Studio) | Python server | 14805 | 60.2 | Published |
| Swmm5AppEngine | Engines and runners | merge (One SWMM runner) | Python server | 19854 | 67.6 | Published |
| SWMM5ControlRules | Hydrology and hydraulics tools | claude | Python server | 995 | 44.2 | Published |
| SWMM5InpReader | Model readers and analyzers | merge (INP Studio) | Python server | 900 | 31.5 | Published |
| SWMM5NetworkAnalyzer | Model readers and analyzers | merge (INP Studio) | Python server | 4294 | 44.8 | Published |
| SWMM5QuizMaster | Quizzes and learning | base (Quiz Hub) | Browser only | 11837 | 54.7 | Published |
| SWMM5RunoffInfiltration | Hydrology and hydraulics tools | base (Infiltration Lab) | Browser only | 5593 | 52.4 | Published |
| SwmmAnalyzer | Model readers and analyzers | base (INP Studio) | Python server | 20990 | 61.4 | Published |
| SWMManywhere App | Network generators | base (SWMManywhere) | Python server | 10982 | 63.2 | Published |
| Swmmanywhere Explorer | Reference, docs and history | merge (SWMManywhere) | Browser only | 1346 | 39.6 | Published |
| SwmmHistory | Reference, docs and history | keep | AI key | 14815 | 60.7 | Published |
| SwmmIcmConverter | Model readers and analyzers | merge (RPT Studio) | Python server | 652 | 34.4 | Draft |
| SwmmInpViewer | Reference, docs and history | keep | Browser only | 9498 | 56.2 | Published |
| Temp Monitor | Climate, places and Network School | base (Climate Explorer) | Own API | 3884 | 40 | Published |
| Video Search | Reference, docs and history | merge (SWMM Manual Search) | Browser only | 344 | 25 | Published |
| WatershedSimulator | Engines and runners | merge (One SWMM runner) | Python server | 4316 | 49.7 | Published |
| XpsToShape | ICM, InfoWorks and migration | keep | Python server | 1874 | 45.8 | Published |

## What this does not show
1. No app was run; nothing here says an app works.
2. No bug is claimed yet; the bug hunt (step 3) will show offending lines per finding.
3. Server class is read from code; a page that calls its server by a path other than /api/ reads as Browser only.
4. The template threshold (5 apps) is a chosen value.
5. The deployed build may be newer than the zip.
6. 29 zips carry no git history.
7. Env variable values, databases and user data were not opened.
8. Complexity counts own code only.
9. Two zip-to-app matches (Fractal SWMMGen, SWMM5NetworkAnalyzer) were inferred from download order.
10. Descriptions and recommendations are Claude's reading and have not been reviewed line by line by Bob.

## How to reproduce
On the device: extract.py (unpack, skip), slim.py (slim zips), facts.py (facts.json), sacm.js (complexity), zipcomp.py (weight). In the container: editorial.py, build_data.py, essay.py, then `node build.js` and `node build_docx.js`.

## Credits and licenses
Apps and decisions: Robert Dickinson. Complexity anchor: HydroCouple GitHub organization (Caleb Buahin). html2canvas 1.4.1 (MIT), gif.js 0.2.0 (MIT; worker inlined). Inter and Inter Tight (SIL OFL).

## AI use
This catalog was built with Claude, Anthropic's AI model, in a Claude session in November 2026, under the direction of Robert (Bob) Dickinson. He chose the task, downloaded the zips, corrected app names and will decide what to merge; responsibility for the page is his. Claude drove the Replit downloads for apps that had no zip yet, wrote the extraction, slimming and fact-gathering scripts, ran the Complexity Meter, wrote every description, family and recommendation, and wrote this page, the essay and the .docx. The counts, sizes, git dates and complexity scores are mechanical and come from scripts run on the zips. The descriptions and recommendations are Claude's reading of the code and have not yet been checked line by line by a person.

## Changes
`1.0.0 (2026-11-20)`: first build.

---
title: "Replit apps: a fourth set of six summaries"
type: concept
updated: 2026-11-15
sources: [S122, S145, S146, S147, S148, S149, S150, S151, S152, S153, S154]
tags: [apps, replit, verification, ai-agents]
reviewed: no
---
Six more of Bob's Replit apps got a technical summary from Replit Agent on 15 November 2026, after the six on [Replit apps: six more summaries](replit-app-summaries-third-batch.md). They were ingested that evening as [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md) to [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md), with two notes of Bob's that answer them, [S151](../sources/S151-note-openswmm-license-not-mit.md) and [S152](../sources/S152-note-ruby-script-runner-deleted.md). Each summary ends by saying that Replit Agent wrote it and that Bob has not yet reviewed it (Q74).

**The apps**

| App | Site name | Replit project | Source |
|---|---|---|---|
| [ICM Ruby to Nano Banana Prompt (app)](../entities/icm-ruby-nano-banana-prompt.md) | `swmm5toicmswmmworkflow.com` | ICMFlowVisualizer | [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md) |
| [InfoSewer to InfoWorks ICM (app)](../entities/infosewer-to-infoworks-icm-guide.md) | `infosewericminfoworksimport.com` | InfoSewerToICMSteps | [S146](../sources/S146-infosewer-to-infoworks-icm-replit-summary.md) |
| [SWMManywhere Explorer at swm-explorer (app)](../entities/swmmanywhere-explorer-swm.md) | `swm-explorer` | SWMManywhere-App | [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md) |
| [OpenSWMM Engine (app)](../entities/openswmm-engine-app.md) | `open-swmm-core` | Open-SWMM-Core | [S148](../sources/S148-openswmm-engine-app-replit-summary.md) |
| [EPANET Quizzer (app)](../entities/epanet-quizzer.md) | `epanetquizzer.com` | EpanetQuizzer | [S149](../sources/S149-epanet-quizzer-replit-summary.md) |
| [InfoWorks ICM Ruby Script Runner (app)](../entities/icm-ruby-script-runner.md) | `ruby-script-ai` | RubyScriptAI | [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md) |

Site names are `.replit.app` names except the three given in full.

**In common.** None records a human review, and none has a test that runs: five have no test script and one found 0 tests [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md).

**Where they differ**
- Engines. Two run one: SWMManywhere 0.1.17 with a SWMM5 WebAssembly engine [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md), and the legacy engine of HydroCouple/OpenSWMMCore in WebAssembly [S148](../sources/S148-openswmm-engine-app-replit-summary.md). Neither records the engine commit (Q79). One ran visitors' Ruby on the server [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md). The other three give `engines: none`.
- TypeScript checks pass in two [S146](../sources/S146-infosewer-to-infoworks-icm-replit-summary.md) [S148](../sources/S148-openswmm-engine-app-replit-summary.md) and fail in three: 34 diagnostics [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md), 1 [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md) and 2 [S149](../sources/S149-epanet-quizzer-replit-summary.md). One is a Python app [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md).
- Two call AI models when they run: Gemini [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md) and gpt-5 [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md).
- Subjects: ICM Ruby scripts [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md) [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md), InfoSewer to ICM [S146](../sources/S146-infosewer-to-infoworks-icm-replit-summary.md), SWMManywhere [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md), OpenSWMM [S148](../sources/S148-openswmm-engine-app-replit-summary.md) and an EPANET quiz [S149](../sources/S149-epanet-quizzer-replit-summary.md).

**What changed after the summaries.** Bob deleted the Ruby Script Runner, which ran visitors' Ruby on the server with no sandbox [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md) [S152](../sources/S152-note-ruby-script-runner-deleted.md). He says the OpenSWMM license is no longer MIT, which the OpenSWMM Engine app then stated [S148](../sources/S148-openswmm-engine-app-replit-summary.md) [S151](../sources/S151-note-openswmm-license-not-mit.md) (Q83). Bob then had that app fixed: its alpha.2 summary states Apache-2.0 and pins the engine commit [S153](../sources/S153-openswmm-engine-app-alpha2-replit-summary.md), and the live page showed it [S154](../sources/S154-note-openswmm-engine-alpha2-published.md).

**Names.** Two apps are named SWMManywhere Explorer [S122](../sources/S122-swmmanywhere-explorer-replit-summary.md) [S147](../sources/S147-swmmanywhere-explorer-swm-replit-summary.md). The addresses or file names of three of the six do not say what the app is (Q77).

See [Replit apps and the summaries Replit Agent wrote](replit-app-summaries.md), [Replit apps: the second seventeen summaries](replit-app-summaries-second-batch.md), [Replit apps: six more summaries](replit-app-summaries-third-batch.md).

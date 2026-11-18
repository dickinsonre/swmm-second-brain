---
title: "S347: AI Engineering Lab, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/ai-engineering-lab-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-19
ingested: 2026-11-18
tags: [apps, ai, transformers, rag, evaluation, swmm5]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app AI Engineering Lab, version 1.0.0: twenty modules built from scratch, every one answering SWMM questions. Raw file: [raw/apps/ai-engineering-lab-v1.0.0.md](../../raw/apps/ai-engineering-lab-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/QqavsHkA2wqaFuaExYZjvx, version 1792368531-c980 (index.html, 2,290,132 bytes, SHA-256 0a66f9572617aa7c5efcc63061eaa1bd27472f440eb40e2c2eb9748fa2cdf35b), its five module groups and its Essay/Doc tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: the app and its essay were produced with Claude, Anthropic's AI model, in a Claude Code session in October 2026, at the request and under the direction of Robert (Bob) Dickinson, who chose the twenty-item learning path, asked that every module answer SWMM questions, asked for the essay in the manner of Isaac Asimov's popular-science essays, and is responsible for all of it."

**Claims worth keeping** (all copied from the file)
- A twenty-item AI engineering learning path, from gradients and tokenizers to agents, security and deployment, done inside one web page with nothing borrowed. Every model is written in plain JavaScript and trained or computed in your browser, and every module works on SWMM: the text it reads is SWMM manual text, the questions are SWMM questions, and the arithmetic is Manning's equation and the rational method in feet, acres and cfs.
- The Lab measures its own question-answering pipeline. On a 24-question examination the three pipeline versions score 13, 20 and 22, with no regressions. Against a crowd of 300 simulated users, version 1 made 54 errors, leaked 24 times and obeyed 68 injections; version 3 made none of any. Module 3 shows backpropagation on Manning's equation: D = 24 in, n = 0.013, S = 0.5% gives Q = 16.040 cfs.
- Every array operation passes a finite-difference nudge test with errors of a few parts in a billion; a planted broken one fails it. The whole transformer passes to 5.7 × 10⁻⁷.
- Manning derivatives from the single-number engine agree with the pencil-and-paper formulas to printed precision.
- Generation with and without the KV cache: identical outputs, 13.6 times fewer operations over 20 characters. Folding the LoRA margin notes into the model: largest change 1.7 × 10⁻¹⁴.
- A fresh model memorizes one sequence completely: "Memorize one sequence, 150 rounds: Charge 0.014" in the page's table. The tokenizer round-trips every test text exactly, emoji included.

**Limits it states.** As the page lists it: the library is small and unreviewed; the Lab's own writer still fails two questions in version 3 by copying a sentence that shares words without answering; the language model writes plausible strings, not facts, and begins memorizing after about 2,200 rounds; the three-letter hash did not beat word counts on typos, contrary to what the Lab was built to show; the planner is brittle; the injection detector can be talked around; the batching and deployment results are simulations from stated assumptions and the deployment files were never built or run; token counts and costs are estimates from editable placeholder prices; the Claude buttons are untested against Claude; results do not survive a reload; with 24 questions the error bars are too wide to rank version 2 against version 3.

**Checked at ingest.** Its library holds a planted "confidential" note with an invented contact at riverbend.example, a reserved domain. Its Claude buttons work only inside claude.ai. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [AI Engineering Lab (app)](../entities/ai-engineering-lab.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [SWMM5 MicroGPT (app)](../entities/swmm5-microgpt.md), [Socratic Engine Chat (app)](../entities/socratic-engine-chat.md).

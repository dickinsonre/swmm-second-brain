---
title: "AI Engineering Lab (app)"
type: entity
updated: 2026-11-18
sources: [S347]
tags: [apps, ai, transformers, rag, evaluation, swmm5]
reviewed: no
---
Bob's app AI Engineering Lab: twenty modules built from scratch, every one answering SWMM questions. Version 1.0.0, 2026-10-19 [S347](../sources/S347-ai-engineering-lab-summary.md). Its `links:` line names no live Netlify address [S347](../sources/S347-ai-engineering-lab-summary.md).

**A caution about its source.** The page ships no technical summary. [S347](../sources/S347-ai-engineering-lab-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S347](../sources/S347-ai-engineering-lab-summary.md)
- A twenty-item AI engineering learning path, from gradients and tokenizers to agents, security and deployment, done inside one web page with nothing borrowed. Every model is written in plain JavaScript and trained or computed in your browser, and every module works on SWMM: the text it reads is SWMM manual text, the questions are SWMM questions, and the arithmetic is Manning's equation and the rational method in feet, acres and cfs.
- The Lab measures its own question-answering pipeline. On a 24-question examination the three pipeline versions score 13, 20 and 22, with no regressions. Against a crowd of 300 simulated users, version 1 made 54 errors, leaked 24 times and obeyed 68 injections; version 3 made none of any. Module 3 shows backpropagation on Manning's equation: D = 24 in, n = 0.013, S = 0.5% gives Q = 16.040 cfs.
- Every array operation passes a finite-difference nudge test with errors of a few parts in a billion; a planted broken one fails it. The whole transformer passes to 5.7 × 10⁻⁷.
- Manning derivatives from the single-number engine agree with the pencil-and-paper formulas to printed precision.
- Generation with and without the KV cache: identical outputs, 13.6 times fewer operations over 20 characters. Folding the LoRA margin notes into the model: largest change 1.7 × 10⁻¹⁴.
- A fresh model memorizes one sequence completely: "Memorize one sequence, 150 rounds: Charge 0.014" in the page's table. The tokenizer round-trips every test text exactly, emoji included.

**How to use it, as the summary puts it.** Use it to learn how a SWMM question-answering system is built and tested, one module at a time. Its library is small and unreviewed (46 paraphrased sections; no person has checked them against the EPA manuals), its 31,700-number language model is a teaching model, and its Claude buttons work only inside claude.ai and have not been run against Claude itself. [S347](../sources/S347-ai-engineering-lab-summary.md)

**What it does not show.** As the page lists it: the library is small and unreviewed; the Lab's own writer still fails two questions in version 3 by copying a sentence that shares words without answering; the language model writes plausible strings, not facts, and begins memorizing after about 2,200 rounds; the three-letter hash did not beat word counts on typos, contrary to what the Lab was built to show; the planner is brittle; the injection detector can be talked around; the batching and deployment results are simulations from stated assumptions and the deployment files were never built or run; token counts and costs are estimates from editable placeholder prices; the Claude buttons are untested against Claude; results do not survive a reload; with 24 questions the error bars are too wide to rank version 2 against version 3. [S347](../sources/S347-ai-engineering-lab-summary.md)

**Noted at ingest.** Its library holds a planted "confidential" note with an invented contact at riverbend.example, a reserved domain. Its Claude buttons work only inside claude.ai.

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [SWMM5 MicroGPT (app)](swmm5-microgpt.md), [Socratic Engine Chat (app)](socratic-engine-chat.md).

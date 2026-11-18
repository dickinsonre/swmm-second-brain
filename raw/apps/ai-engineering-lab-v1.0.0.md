---
name: AI Engineering Lab
file: ai-engineering-lab.html
version: 1.0.0
date: 2026-10-19
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/QqavsHkA2wqaFuaExYZjvx", repo: none}
engines: none (every model is written in plain JavaScript in the page; the optional Claude buttons call Claude only inside claude.ai)
units: US customary (ft, acres, cfs) in the SWMM questions and tools
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude wrote all of the app's code, its SWMM library and examination, trained its language model and wrote its essay, in a Claude Code session in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/QqavsHkA2wqaFuaExYZjvx, version 1792368531-c980 (index.html, 2,290,132 bytes, SHA-256 0a66f9572617aa7c5efcc63061eaa1bd27472f440eb40e2c2eb9748fa2cdf35b), its five module groups and its Essay/Doc tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# AI Engineering Lab: twenty modules built from scratch, every one answering SWMM questions

## In three points
- **What:** A twenty-item AI engineering learning path, from gradients and tokenizers to agents, security and deployment, done inside one web page with nothing borrowed. Every model is written in plain JavaScript and trained or computed in your browser, and every module works on SWMM: the text it reads is SWMM manual text, the questions are SWMM questions, and the arithmetic is Manning's equation and the rational method in feet, acres and cfs.
- **So what:** The Lab measures its own question-answering pipeline. On a 24-question examination the three pipeline versions score 13, 20 and 22, with no regressions. Against a crowd of 300 simulated users, version 1 made 54 errors, leaked 24 times and obeyed 68 injections; version 3 made none of any. Module 3 shows backpropagation on Manning's equation: D = 24 in, n = 0.013, S = 0.5% gives Q = 16.040 cfs.
- **Now what:** Use it to learn how a SWMM question-answering system is built and tested, one module at a time. Its library is small and unreviewed (46 paraphrased sections; no person has checked them against the EPA manuals), its 31,700-number language model is a teaching model, and its Claude buttons work only inside claude.ai and have not been run against Claude itself.

This summary was written after the fact. The app ships no technical summary of its own. Its version is the page's own ("v1.0.0"); the page says October 2026, and the date above is when this version was published as an artifact. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Twenty modules in five groups: 1 to 4 Foundations (math, classic ML, backprop, tokenizer); 5 to 8 Transformers and retrieval (a 2-layer, 2-head, 32-wide character transformer of about 31,700 parameters; training a small language model; embeddings; RAG); 9 to 12 Tuning and serving (chunking, reranking and hybrid search; LoRA, QLoRA and full fine-tuning; KV cache, quantization and batching; a tool-calling agent); 13 to 16 Agents and reliability (memory and recovery; structured outputs; evaluations; traces, tokens and cost); 17 to 20 Ship it (prompt injection and sandboxing; deployment; one end-to-end system; publishing the failures). Each module has controls, results, a "show code" panel that prints the functions that just ran, and a "What this does not show" line. The Essay/Doc tab holds "Twenty Steps to an Answer", an essay in twenty-one chapters, also offered as a 1,224 KB Word file.

The library: 16 documents with 46 sections, about 12,200 characters. Fourteen are paraphrased from the EPA SWMM 5 manuals in US customary units. Two are planted on purpose: a contractor's field note carrying an injection, and a confidential note for an invented "Riverbend Utility District" with an invented contact name, email address (at the reserved riverbend.example domain), phone number and roughness. A sample SWMM input of 70 lines (two subcatchments, four junctions, an outfall, four circular pipes of 18 and 24 in, dynamic wave, a storm peaking at 2.5 in/hr).

## Checks (as stated on the page)

Run on the finished Lab, outside the browser and in an automated browser, 15 to 17 October 2026:
- Every array operation passes a finite-difference nudge test with errors of a few parts in a billion; a planted broken one fails it. The whole transformer passes to 5.7 × 10⁻⁷.
- Manning derivatives from the single-number engine agree with the pencil-and-paper formulas to printed precision.
- Generation with and without the KV cache: identical outputs, 13.6 times fewer operations over 20 characters. Folding the LoRA margin notes into the model: largest change 1.7 × 10⁻¹⁴.
- A fresh model memorizes one sequence completely: "Memorize one sequence, 150 rounds: Charge 0.014" in the page's table. The tokenizer round-trips every test text exactly, emoji included.
- Examination of 24 questions: 13, 20 and 22 for versions 1, 2 and 3 (95% intervals 35 to 72%, 64 to 93%, 74 to 98%). Version 3 survives the crowd of 300 with no error, leak or obeyed injection.
- All twenty modules opened at desktop and phone widths with no errors and no sideways scrolling; results identical in dark and light; 74 contrast pairs pass. The Claude buttons ran end to end against a stand-in, not against Claude.

## What this does not show

As the page lists it: the library is small and unreviewed; the Lab's own writer still fails two questions in version 3 by copying a sentence that shares words without answering; the language model writes plausible strings, not facts, and begins memorizing after about 2,200 rounds; the three-letter hash did not beat word counts on typos, contrary to what the Lab was built to show; the planner is brittle; the injection detector can be talked around; the batching and deployment results are simulations from stated assumptions and the deployment files were never built or run; token counts and costs are estimates from editable placeholder prices; the Claude buttons are untested against Claude; results do not survive a reload; with 24 questions the error bars are too wide to rank version 2 against version 3.

## Credits and licenses

References in the essay include Gage (1994) on byte-pair encoding, Kingma and Ba (2015) on Adam, Vaswani et al. (2017) on attention, and Rossman (2022), the SWMM 5.2 User's Manual. No license is stated for the page.

## AI use

The page says: the app and its essay were produced with Claude, Anthropic's AI model, in a Claude Code session in October 2026, at the request and under the direction of Robert (Bob) Dickinson, who chose the twenty-item learning path, asked that every module answer SWMM questions, asked for the essay in the manner of Isaac Asimov's popular-science essays, and is responsible for all of it. Claude wrote all of the code, the SWMM library, sample model and examination, trained the language model, wrote the document and built the Doc tab. Every number comes from running the app's own code between 15 and 17 October 2026. The historical notes were written from Claude's general knowledge and have not been checked against sources by a person. No person has yet reviewed the document, checked the library text against the EPA manuals, or run the Claude buttons against Claude. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.0 (October 2026): first version (the version read).

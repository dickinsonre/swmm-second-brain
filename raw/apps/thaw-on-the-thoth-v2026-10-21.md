---
name: Thaw on the Thoth
file: thaw-on-the-thoth.html
version: 2026-10-21
date: 2026-10-21
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/CmsNSow2yFY9dS72KHRc2R", repo: "https://github.com/SWMMBobSWMM6/Stormwater-Management-Model (branch swmm524-fvlink, examples/thoth-mars)"}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "built from the EPA source at commit 7952ca8, rebuilt with GRAVITY 12.2 for Mars; runs made for the story, none in the page", license: public domain}
  - {name: swmm524-fvlink, note: "Bob Dickinson's branch of SWMM 5.2.4 that solves chosen links by the finite volume method, rebuilt the same way"}
units: US customary (ft, cfs, acres, gallons)
ai_use: "This summary was written by Claude (Anthropic) from the published document. The document says it, its model, its runs, its charts and its paintings were made with Claude in a Claude Code session in October 2026 at Robert Dickinson's request. See AI use."
written_from: "the published Claude Docs document https://claude.ai/artifact/CmsNSow2yFY9dS72KHRc2R, artifact version 1793394821-af7e, document revision 13, exported as HTML with its 16 pictures on 2026-11-18. The Netlify page beside this file was set from that export by Claude on 2026-11-18. Nothing was run to write this file."
---

# Thaw on the Thoth: a story of two boys, one Martian canal and the spring thaw of 2097

## In three points
- **What:** A short story in seven chapters and an afterword, in the spirit of Robert A. Heinlein's Red Planet (1949). Two boys at a Mars colony check the Canal Company's SWMM forecast for a thaw on an invented canal, the Thoth, and find that gravity hides in Manning's n and the weir coefficient. The people, the colony and the night of the thaw are invented. The canal model, the two engines and every number on every chart come from runs of EPA SWMM 5.2.4 and swmm524-fvlink rebuilt with Mars gravity, and the afterword sorts one from the other.
- **So what:** Changing GRAVITY from 32.2 to 12.2 alone left mile one at 2.38 ft at base flow, because gravity sits in both the slope term and the friction term (Conduit[k].roughFactor = GRAVITY * SQR(roughness/PHI)). Holding g·n² fixed scales n by 1.625 (0.015 to 0.0244) and the weir coefficient by 0.6155 (3.33 to 2.050). The Upper Thoth then carries 4,439 cfs bank-full instead of 7,213, against a 4,200 cfs crest, and the basin reaches the top of its 14.5 ft levee at hour 40.3 (the chart's legend says 40.4) instead of cresting at the Company's 13.3 ft. Building the model also found water running uphill through a finite volume throat, now entered as FVL-15 in the branch's defect register.
- **Now what:** Use it to see why a constant that was right on Earth can be wrong in a model, and where to look for it. The Thoth has no survey behind it, the n and weir scaling is a dimensional argument no one has checked against data, and no person has yet reviewed the story or rerun the models.

This summary was written after the fact. The document ships no technical summary of its own. Its date is the document's own ("2026-10-21"); it gives no version number. The file name above is ours. Every number below is copied from the document. Nothing was run to write this file.

## What it is

Chapters: I. Spring on the Thoth; II. The Company Model; III. A Constant from Another Planet; IV. Water That Ran Uphill; V. Nothing Is Free; VI. Margin; VII. What the Instrument Said; then "Afterword: what is real in this story" and "Use of AI". Sixteen pictures: nine charts from run output, two computed from formulas (wave speed and the Manning rating), the map and the finite volume diagram (drawings), and three paintings made for the story as vector art.

## The model and the runs (as the afterword states them)

- The canal: written by a script, gen_thoth.py. About 14 miles of trapezoidal main canal (15 miles of conduit with the outlet and side channels): eight one-mile reaches above a 10-ft causeway culvert and a 400-ft chute with a 20-ft drop, six one-mile reaches and a 600-ft reach below, a 34-acre storage basin with its levee crest at 14.5 ft, a 100-ft overflow weir, a pumped town intake, and an 8 by 20 ft side orifice onto a dry channel. The thaw is a smooth hydrograph from 300 cfs to 4,200 cfs.
- The engines: EPA SWMM 5.2.4 from commit 7952ca8 and swmm524-fvlink, both rebuilt with GRAVITY in consts.h set to 12.2 instead of 32.2. The code quoted is copied from the EPA source and from the published branch.
- The numbers: every model result, from the Company's 13.29-ft crest to 13.98 ft at hour 54, comes from a run of one of the two engines, and the story names the engine each time. Plain and hybrid engines agree at the basin within 0.01 ft.
- Run times, median of five interleaved runs on a modern machine: 6.47 s plain, 9.40 s with four finite volume cells in the culvert, 1.40 s with one; the Company's model 13.84 s. The colony computer's times are those times a thousand.
- The water that ran uphill is real: it turned up while the model was being built. A prototype fix moved the test-suite junction 0.77 ft in a 30-conduit chain and 3.5 ft in a 70-conduit chain (run at Earth gravity). Three other prototypes did not fix the throat without changing results elsewhere. The engine has not been changed; that is the branch owner's decision.

## What this does not show

As the document states: the Thoth is invented and has no survey behind it; the scaling of n and the weir coefficient is ordinary dimensional reasoning that has never been checked against flow in a lined canal on Mars; the gauge readings are fiction set near the model's values; no person has yet reviewed the story or rerun the models, and no other engineer has checked the scaling.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); swmm524-fvlink and the whole Thoth model on the swmm524-fvlink branch of SWMMBobSWMM6/Stormwater-Management-Model (examples/thoth-mars: the generator, the gravity patch, every input file and report, the figure scripts and the story's text). The premise salutes Robert A. Heinlein's Red Planet; no character, place or line is taken from it. No license is stated for the document.

## AI use

The document says: the story and everything behind it were made with Claude, Anthropic's AI model, in a Claude Code session in October 2026 at the request of Robert (Bob) Dickinson, who asked for a story about boys on Mars modeling canal flow in the spirit of Red Planet, set the house style and is responsible for what is published. Claude designed the canal and wrote its generator, rebuilt both engines with Mars gravity, ran every model, found the uphill defect and wrote and tested the prototype fixes, worked out the scaling, drew all the charts, diagrams and paintings, and wrote the story. The checks are mechanical: every number traced to a run's output file or a stated formula; a byte-for-byte null check; the two engines compared at the basin. The Netlify copy was set from the document's HTML export by Claude on 18 November 2026; the text is unchanged. This summary was written by Claude on 18 November 2026.

## Changes

- 2026-10-21: the document as read (revision 13).

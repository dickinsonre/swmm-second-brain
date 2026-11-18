---
title: "Info to Mark Magic (app)"
type: entity
updated: 2026-11-18
sources: [S352]
tags: [apps, markdown, conversion, library]
reviewed: no
---
Bob's app Info to Mark Magic: web pages and HTML into clean Markdown for the BobSWMM library. Version 2.0, 2026-10 [S352](../sources/S352-info-to-mark-magic-summary.md). Its `links:` line names no live Netlify address [S352](../sources/S352-info-to-mark-magic-summary.md).

**A caution about its source.** The page ships no technical summary. [S352](../sources/S352-info-to-mark-magic-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S352](../sources/S352-info-to-mark-magic-summary.md)
- Turns web pages and HTML into clean Markdown for a documentation library (option tables, code samples, numbered procedures): paste copied content, drop saved pages, or fetch an address; read, edit and compare the result; keep it as Markdown, plain text, a web page, a PDF, or a library exported together. A single-file port of Bob's Lovable project.
- The original converter matched text with regular expressions and lost tables, turned numbered lists into "$1", cut content at the first inner </div>, dropped images and left characters undecoded. The port reads the browser's parsed tree. The Findings tab lists 19 defects (6 high, 6 medium, 7 low); 15 were checked by running the original code, and all 15 reproduced.
- The original conversion and export functions copied out of the uploaded source byte for byte, with only TypeScript annotations removed, and run in the browser on small inputs built to show one defect each: 19 findings, 15 run and all 15 reproduced.
- A census of the bundled sample page (4,726 characters of HTML), measured 2026-10-22: headings, tables, table rows, list items, code blocks, images and quotes counted in the source and in each output.
- The app driven through its features in a headless browser.

**How to use it, as the summary puts it.** Use it to bring vendor and EPA documentation into a Markdown library. It has been tested on small fixtures and one sample page, not on a corpus of real documentation sites; the URL routes do not work inside the Claude viewer, and the backend routes depend on the original Lovable project still running. [S352](../sources/S352-info-to-mark-magic-summary.md)

**What it does not show.** As the page lists it: whether a page is right, only what it says; text a page builds with JavaScript after loading (unless pasted from the rendered page or fetched through Firecrawl); pages behind a login (except through Paste); a run on real documentation sites (some layouts will fool the content finder); the census is a count, not a proof. No person has reviewed the port or checked the sample page's SWMM content against the EPA manual. The original Lovable project could not be reached from the machine that built the port. [S352](../sources/S352-info-to-mark-magic-summary.md)

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Master SWMM PDF (app)](master-swmm-pdf.md).

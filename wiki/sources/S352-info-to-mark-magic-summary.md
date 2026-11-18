---
title: "S352: Info to Mark Magic, summary written from the page (v2.0)"
type: source
raw: raw/apps/info-to-mark-magic-v2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10
ingested: 2026-11-18
tags: [apps, markdown, conversion, library]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Info to Mark Magic, version 2.0: web pages and HTML into clean Markdown for the BobSWMM library. Raw file: [raw/apps/info-to-mark-magic-v2.0.md](../../raw/apps/info-to-mark-magic-v2.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/JEavXDpnckv6CJPxcrAFm7, version 1792633027-3308 (index.html, 1,306,954 bytes, SHA-256 5992a57f57de6e049a4d404b2293d50fdf45fd0ee96cac25c60e32180003d45c), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in October 2026 at the request of Robert (Bob) Dickinson, who supplied the original project as a zip file and asked for a single-file HTML app; responsibility is his. Claude read the original source, copied the original functions out for the test bench, wrote the new converter, the app, the PDF and GIF writers, the sample page, the findings register, the essay and its Word version, and ran the checks."

**Claims worth keeping** (all copied from the file)
- Turns web pages and HTML into clean Markdown for a documentation library (option tables, code samples, numbered procedures): paste copied content, drop saved pages, or fetch an address; read, edit and compare the result; keep it as Markdown, plain text, a web page, a PDF, or a library exported together. A single-file port of Bob's Lovable project.
- The original converter matched text with regular expressions and lost tables, turned numbered lists into "$1", cut content at the first inner </div>, dropped images and left characters undecoded. The port reads the browser's parsed tree. The Findings tab lists 19 defects (6 high, 6 medium, 7 low); 15 were checked by running the original code, and all 15 reproduced.
- The original conversion and export functions copied out of the uploaded source byte for byte, with only TypeScript annotations removed, and run in the browser on small inputs built to show one defect each: 19 findings, 15 run and all 15 reproduced.
- A census of the bundled sample page (4,726 characters of HTML), measured 2026-10-22: headings, tables, table rows, list items, code blocks, images and quotes counted in the source and in each output.
- The app driven through its features in a headless browser.

**Limits it states.** As the page lists it: whether a page is right, only what it says; text a page builds with JavaScript after loading (unless pasted from the rendered page or fetched through Firecrawl); pages behind a login (except through Paste); a run on real documentation sites (some layouts will fool the content finder); the census is a count, not a proof. No person has reviewed the port or checked the sample page's SWMM content against the EPA manual. The original Lovable project could not be reached from the machine that built the port.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Info to Mark Magic (app)](../entities/info-to-mark-magic.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Master SWMM PDF (app)](../entities/master-swmm-pdf.md).

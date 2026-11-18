---
name: Info to Mark Magic
file: info-to-mark-magic.html
version: "2.0"
date: 2026-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/JEavXDpnckv6CJPxcrAFm7", original: "https://info-to-mark-magic.lovable.app (Lovable project SWMMEnablement/info-to-mark-magic, handover v1.2)", repo: none named in the page}
engines: none (an HTML-to-Markdown converter written for the page; optional URL routes call the original project's Supabase functions and Firecrawl)
units: not applicable (PDFs are US Letter)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/JEavXDpnckv6CJPxcrAFm7, version 1792633027-3308 (index.html, 1,306,954 bytes, SHA-256 5992a57f57de6e049a4d404b2293d50fdf45fd0ee96cac25c60e32180003d45c), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# Info to Mark Magic: web pages and HTML into clean Markdown for the BobSWMM library

## In three points
- **What:** Turns web pages and HTML into clean Markdown for a documentation library (option tables, code samples, numbered procedures): paste copied content, drop saved pages, or fetch an address; read, edit and compare the result; keep it as Markdown, plain text, a web page, a PDF, or a library exported together. A single-file port of Bob's Lovable project.
- **So what:** The original converter matched text with regular expressions and lost tables, turned numbered lists into "$1", cut content at the first inner </div>, dropped images and left characters undecoded. The port reads the browser's parsed tree. The Findings tab lists 19 defects (6 high, 6 medium, 7 low); 15 were checked by running the original code, and all 15 reproduced.
- **Now what:** Use it to bring vendor and EPA documentation into a Markdown library. It has been tested on small fixtures and one sample page, not on a corpus of real documentation sites; the URL routes do not work inside the Claude viewer, and the backend routes depend on the original Lovable project still running.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v2.0 · built October 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Convert, Library, Templates, Findings, About, Doc. Batch export, the four templates and the XML sitemap export, built but never connected in the original, are wired in; the sitemap crawl works, fetching, converting and filing each page. Preview and every export use one Markdown parser, so exports no longer italicize keywords like FLOW_UNITS or turn code comments into headings. PDFs are US Letter with a contents page carrying real page numbers. Source and Compare work for pasted HTML too, with a census of what went in and what came out. Conversion happens in the browser; only a URL route sends anything out (to the site itself, or to the original project's Supabase functions and Firecrawl, which spends credits on that project's account). The current document and library stay in the browser's storage; Backup .json makes a copy.

## Checks (as stated on the page)

- The original conversion and export functions copied out of the uploaded source byte for byte, with only TypeScript annotations removed, and run in the browser on small inputs built to show one defect each: 19 findings, 15 run and all 15 reproduced.
- A census of the bundled sample page (4,726 characters of HTML), measured 2026-10-22: headings, tables, table rows, list items, code blocks, images and quotes counted in the source and in each output.
- The app driven through its features in a headless browser.

## What this does not show

As the page lists it: whether a page is right, only what it says; text a page builds with JavaScript after loading (unless pasted from the rendered page or fetched through Firecrawl); pages behind a login (except through Paste); a run on real documentation sites (some layouts will fool the content finder); the census is a count, not a proof. No person has reviewed the port or checked the sample page's SWMM content against the EPA manual. The original Lovable project could not be reached from the machine that built the port.

## Credits and licenses

The Lovable project SWMMEnablement/info-to-mark-magic. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in October 2026 at the request of Robert (Bob) Dickinson, who supplied the original project as a zip file and asked for a single-file HTML app; responsibility is his. Claude read the original source, copied the original functions out for the test bench, wrote the new converter, the app, the PDF and GIF writers, the sample page, the findings register, the essay and its Word version, and ran the checks. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.0 (2026-10): single-file port with a parsed-tree converter (the version read).
- 1.2 (Lovable handover): the original.

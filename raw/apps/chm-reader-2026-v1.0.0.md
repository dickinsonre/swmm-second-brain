---
name: CHM Reader 2026
file: chm-reader-2026.html
version: 1.0.0
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/6nZbyChtNBieAwhnrpn2Ve", repo: none named in the page}
engines: none (a CHM container reader and LZX decoder in JavaScript)
units: bytes, characters
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Claude Opus 5.5) at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/6nZbyChtNBieAwhnrpn2Ve, version 1793635652-9de8 (index.html, 1,029,778 bytes, SHA-256 d597fcb25b7bb1209cdf3512a0ad1a72ed8982d9bd32863a77d8811b18295d03), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# CHM Reader 2026: open Microsoft Compiled HTML Help files in the browser and hand the text to Claude

## In three points
- **What:** A single-file app that opens Microsoft Compiled HTML Help (.chm) files without Windows, a plugin or an upload, shows their Contents, Index, full-text Search and raw Files, and exports the text as Markdown or plain text in parts sized to a context window.
- **So what:** Its own LZX decoder matched 7-Zip 16.02 and chmlib 0.40 byte for byte on all 7,038 entries of three test files, and 15 deliberately damaged files from libmspack's test suite each read or stopped with a plain error.
- **Now what:** Use it to get old SWMM, ICM or other CHM help into a form Claude reads well. Stored blocks and the x86 E8 translation have no independent check, and the token counts are estimates at four characters per token.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0.0 · 2026-11-02"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

An earlier answer said Claude could not read a CHM file. This page reads one in memory, renders topics with every script removed in a sandboxed frame, searches the full text, and exports for Claude. It also updates a second old answer, on how big a file Claude can take, with numbers from the Claude Help Center as of 2 November 2026. Tabs: Reader (Contents, Index, Search, Files), Then & Now, Limits 2026, About, Doc.

## Checks (as stated on the page)

- 7,038 entries in three test files, compared byte for byte with 7-Zip 16.02 and chmlib 0.40; every one matched.
- PyWin32.chm (2,648,456 bytes, Microsoft HTML Help compiler HHA 4.74.8702): 6,880 files, 11.1 MB, identical to chmlib and 7-Zip.
- fpc1.chm (607,362 bytes, Free Pascal chmcmd 3.2.2, built for the test with 120 pages, 300,000 random bytes and 500,000 zero bytes): 130 files identical. The first run failed four entries because Free Pascal codes the short last frame as a full 32 KB block; the decoder now accepts the overrun.
- chm-reader-2026-sample.chm (55,929 bytes, the bundled sample): 28 files identical.
- 15 damaged files from libmspack's test suite: each reads or stops with a plain error; none hangs.

## What this does not show

- Stored (uncompressed) blocks passed a hand-built stream test only; neither compiler emitted one.
- The x86 E8 translation is written but no test file used it.
- Upload limits were read from the Claude Help Center on 2 November 2026 and may change; token counts are estimates.

## How to reproduce

Open the page and drop a .chm file, or open the bundled sample; Export writes Markdown or text.

## Credits and licenses

The CHM and LZX formats as published, and libmspack's behaviour and test files; 7-Zip 16.02 and chmlib 0.40 as references; Free Pascal chmcmd for the sample. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model (Claude Opus 5.5), in a Claude session on 2 November 2026, at the request of Robert (Bob) Dickinson, who asked for two earlier answers to be brought up to 2026 as an app with a Doc tab and a Word file. Claude wrote the container reader and LZX decoder from the published format and libmspack's behaviour, the viewer, search and export code, the sample help file, the figures, the essay, the .docx and the 2026 answers, and looked up the limits on the Claude Help Center. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0.0 (2026-11-02): first build.

---
name: Visual SWMM
file: visual-swmm.html
version: 0.1.1
date: 2026-11-19
written: 2026-11-19
author: Robert Dickinson
links: {netlify: "https://visual-swmm.netlify.app", artifact: "https://claude.ai/artifact/LuofNZ1uvSp9cF3Jpv71RD", repo: none named in the page}
engines:
  - {name: none (reader only), note: "xpread.wasm, about 140 KB, C compiled with clang 18 for wasm32, no libraries, written from LMAIN.FOR, Swmfield.c and SWMM.R in Robert Dickinson's XP Software archive (December 1999); the 208-file XP-SWMM Fortran engine is not compiled in"}
units: US customary as the cards carry them (ft, cfs)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app was built by Claude (Claude Fable 5.2) at Robert Dickinson's request and from his source archive. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/LuofNZ1uvSp9cF3Jpv71RD, version 1794659289-40b0 (index.html, 341,301 bytes, SHA-256 15500cb95a35def4b94828f8f16b551f067cffc1cd1cd671721a54313cb69a78), its About and Doc tabs read in headless Chromium on 2026-11-17. No file was read by the app to write this summary. The 0.1.1 patch was made on 2026-11-19 by Claude and checked in headless Chromium at 390 px; its Changes line says what moved."
---

# Visual SWMM (working name): a WebAssembly reader for XP-SWMM .xp files, built from the 1999 XP source

## In three points
- **What:** A browser reader for XP-SWMM .xp model files: a 140 KB WebAssembly module, written in C from the 1999 XP engine reader and field dictionary, draws the network and shows every card as named fields.
- **So what:** Its values equal XP-SWMM's own .xpx exports for 18,219 of 18,296 input fields across eleven models, and five models agree on every field.
- **Now what:** Use it to open and inspect old .xp models without XP-SWMM. It does not solve, and the December 1999 dictionary decodes only 60% of the records in the 25 sample files, fewer in version 18 and later.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v0.1.1 · working name"); the date is the patch's, 19 November 2026; the first build session was 14 November 2026. Every number below is copied from the page's About tab or its Doc essay.

## What it does

A .xp file is plain text: 105-column records, each an address followed by an old 80-column SWMM card. The app reads those records in the browser, draws the nodes and links, shows each object's cards as named fields with units (Ground Elevation 120 ft, Length 100 ft, Mannings n 0.013), pulls one card for every object as a table, and writes a .xpx, XP-SWMM's plain-text interchange format. The file never leaves the machine. Tabs: Read, Network, Objects, Cards, Verify, About, Doc.

## How it computes

- Record layout: columns 1 to 4 the group (EXTR hydraulics, RUNF runoff, TRAN sanitary, Z... interface housekeeping); 5 to 8 an instance number; 9 to 12 the card name; 13 to 16 a sequence number; 17 to 20 the object index (0 for the whole model); 26 to 105 the card. Dictionary column n is record column n + 25.
- Source files used: LMAIN.FOR (xpsoft/NEWDEC, December 1999), the engine's own three-pass read (counts, node and link names, link ends, node coordinates, evaporation); Swmfield.c (WPACODE, December 1999), 1,489 fields with group, card, start column and width; SWMM.R (WPACODE), plain-English labels for 627 fields and choice lists for 146.
- The reader is about 340 lines of C plus a generated table of 1,489 rows. It does the engine's three passes, then decodes every card the table names and shows the rest exactly as written.

## Results and checks (as stated on the page)

- 25 sample .xp files read without error; 51,144 records; 30,612 (60%) on cards the dictionary decodes; XP-SWMM versions 1.05 to 20.1.
- Against XP-SWMM's own .xpx exports for eleven models: 18,219 of 18,296 input fields equal (99.6%). Every field equal in IMPORT.XP (122), INTL2.XP (111), EDWARDS8.XP (884), EXTUT7.XP (260) and JACK_RUN_v6.xp (440); FW927TST.XP 15,834 of 15,847; NATURE.XP 180 of 206; Chap10.xp 89 of 91; FLOOD.XP 224 of 238; HDR1X.XP 45 of 58; EXQUAL.XP 30 of 39. The page attributes the differences to the two files being saved at different times.
- Complexity: about 5 on the scale where HydroCouple is 100, an AI estimate; the app has not been run through the SWMM App Complexity Meter.
- The checks are mechanical. No person has reviewed the reader line by line.

## What this does not show

- It does not run the model. The XP-SWMM engine (208 Fortran files) takes its hydraulics from a .DAT card file that the XP interface writes at Solve time; the export code (Export.c) and the engine are in the archive but not in this version.
- Cards added after December 1999 appear as raw records without field names; in files from version 18 on these include real model data such as 2D grids and newer control options.
- About 42% of fields (627 of 1,489) have a plain-English label; the rest show their six-letter mnemonic.
- Checked on 25 of more than 1,300 files in the archive; no sample had more than 9,999 objects.
- The .xpx it writes has not been loaded back into XP-SWMM.

## How to reproduce

Open the page, drop a .xp file on the Read tab or load the built-in tutorial EXTUT7.XP, and use Verify to compare with an .xpx.

## Credits and licenses

XP-SWMM, the XP visual engine and the .xp and .xpx formats: XP Software, where Robert Dickinson was Senior Vice President and designed both formats. Visual SWMM was his later product at CAiCE Software; the name is reused as a working title. EPA SWMM, on which the engine was built, is public-domain software of the US EPA. No license is stated in the page for the reader itself.

## AI use

The page says the app was built by Claude (Anthropic's AI model, Claude Fable 5.2) in one working session on 2026-11-14, at Robert Dickinson's request and from his source archive. Claude read the Fortran and C source, worked out the record layout, wrote the C reader, the build scripts, the page, the Doc essay and its figures, and ran the checks. The engine source, the field dictionary, the dialog script, the formats and every sample model are Robert Dickinson's and XP Software's work; the AI wrote no hydraulics and changed none of the original source. This summary was written by Claude on 17 November 2026 from the published page.

Version 0.1.1 was made by Claude in a later session on 2026-11-19: it found the phone-width overflow with a headless-browser check and changed one CSS line. Nothing was rerun against the .xpx exports.

## Changes

- 0.1.1 (2026-11-19): at phone width the one-column grid kept its automatic minimum, so the Verify table pushed the page to 484 px on a 390 px screen. One CSS line changed, `.grid,.grid.even{grid-template-columns:1fr}` to `minmax(0,1fr)` in the 900 px media rule; every view now fits at 390 px. Nothing else changed.
- 0.1.0 (2026-11-14): first version.

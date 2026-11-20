---
name: Modeling Docs Library
file: modeling-docs-library.html
version: 1.0.0
date: 2026-11-19
author: Robert Dickinson
links: {netlify: none (private; not for public hosting), artifact: private Claude artifact, repo: none}
engines: none (text search only; no hydraulic engine)
data:
  - {name: PC pack, source: "PC yoo100: Documents, Downloads, D:, GitHub, swmm-brain", documents: 620, built: 2026-11-19}
  - {name: second-brain index, source: "github.com/dickinsonre/swmm-second-brain", commit: af61331, pages: 765}
units: not applicable (text)
ai_use: built with Claude (Anthropic); see AI use
---

# Modeling Docs Library: search Bob Dickinson's modeling Word and PowerPoint files by passage, and build new Word files from what you find

**In one sentence.** The Modeling Docs Library puts the text of 620 Word and PowerPoint modeling documents from one PC, 2.5 million words dated 1997 to 2026, into one searchable file that turns ticked passages into a new, sourced Word document.

**In one paragraph.** A script walked five folders on Bob Dickinson's PC and found 1,027 Word and PowerPoint files. After copies, empty files and 72 files that were not about modeling or were private came out, 620 documents remained. Their text was cut into 19,145 passages and packed into one HTML file. You search by passage, and the best passage of each document is shown first. You tick passages into a tray and the app writes a Word file that quotes them and names each source. Every document is matched to the nearest pages of the swmm-second-brain wiki; 155 documents have no page close to them. 16 checks of the search and the Word writer pass. The main limit is plain: the Google Drive archive is not in yet.

## What it does

It answers "what did I, or my colleagues, already write about X?" for one person's archive. It holds the extracted text of 620 Word and PowerPoint documents (2,497,276 words, 19,145 passages, dated 1997 to 2026) inside one HTML file. Output: ranked passages grouped by document, a reader with the original file path, a tray of ticked passages, and a .docx or .md built from the tray. Each document is also matched to the nearest pages of the swmm-second-brain wiki.

## How it computes

Extraction (scripts in `tools/pc/`, run on the PC):

1. `inv.py` walks the folders and lists `.docx .doc .pptx .ppt .rtf` files: 1,027.
2. `s1_list.py` drops Word lock files (`~$`) and files under 200 bytes (976 left), keeps the highest-numbered copy of `name (n).ext` within a folder (860), and treats same name plus same byte size in different folders as one file (706).
3. `s2_conv.py` converts `.doc .ppt .rtf` with LibreOffice headless to `.docx/.pptx` (380 files). Files named `.DOC` that are plain text are read as text (12 files).
4. `s3_parse.py` reads `word/document.xml` (paragraphs, heading styles and outline levels, table rows joined with ` | `) and `ppt/slides/*.xml` (title placeholder, text, tables, speaker notes), and `docProps/core.xml` for title, author, created and modified. Passages: paragraphs under one heading or slide, closed at 900 characters, split at 1,500.
5. `s4_build.py` filters and labels. Modeling score s = count of about 60 modeling terms in the text (file name hits count double; "model" in the file name adds 3). Keep if (s >= 3 and s per 1,000 words >= 2.0) or s >= 60 or (folder is a known modeling archive and words >= 40). Left out: not modeling 36, under 25 words 20, path matches personnel, licence or personal folders 12, text matches a password pattern 4. Identical text (hash of letters and digits only) merged: 14. Topics: 24 keyword rules; a topic is assigned at >= 3 hits and >= 1 per 1,000 words; at most 6 per document. Date = `modified`, else `created`, from inside the file, accepted for years 1985 to 2026.

Search (`src/core.js`, in the page):

- No index. Every query scans every passage (lowercased heading plus text).
- A term matches where it begins a word: the character before the match is not a letter or digit. `"quoted phrases"` match as phrases; `-term` removes documents containing it.
- Passage score per term: BM25 with k1 = 1.4, b = 0.6, IDF = ln(1 + (N - n + 0.5)/(n + 0.5)), N = passages, n = passages containing the term, length in characters against the mean passage length.
- Passage score is multiplied by (terms matched / terms in query)^1.5.
- Document score = best passage + 0.2 x second + 0.1 x third + title bonus (0.6 x IDF + 0.8 per query term in the title) + 0.05 x ln(1 + matching passages).
- Mode `all`: every term must occur somewhere in the document (any passage or the title). Mode `any`: at least one.
- Related: the passage's 8 highest (1 + ln tf) x IDF words, searched in `any` mode, excluding its own document, keeping documents whose best passage shares at least 3.
- Travels with it: document frequency times IDF over the top two passages of up to 30 documents, minus the query's own words and stop words.

Second brain (`tools/make_sb.py`, at build):

- Wiki pages parsed from `wiki/concepts`, `wiki/entities`, `wiki/sources`; one-line summaries from `index.md`.
- Each document and each concept or entity page becomes a vector of (1 + ln tf) x ln(1 + N/df), L2-normalized. Similarity = cosine. Top 5 pages at >= 0.08 are stored per document.

Word writer (`src/core.js`): a .docx is written as a stored (uncompressed) zip of six parts with CRC-32, US Letter, styles Title, Subtitle, Heading 1 and 2, Quote, Source Line, List Bullet; external hyperlinks through `word/_rels/document.xml.rels`.

AI draft: the page calls the artifact `sample` capability with one prompt: rules (use only the passages, cite by source number, no added facts, Markdown out), the instruction, the source list and up to 90,000 characters of passages. The returned Markdown is converted to the same block model and gets a first-page and last-page AI label.

## Inputs and outputs

- Reads: the built-in pack and second-brain index (gzip, base64, inside the .html; as `pack-pc.json` and `sb.json` beside the page in the artifact). Extra packs (`.json.gz` or `.json`, same schema) through the Packs tab, kept in IndexedDB in that browser.
- Pack schema: `{name, built, topics[], docs[{id, t, st, p, al[], x, d, a, w, c, k[], s, sb[[page, cos]], ps[[heading, text]]}]}`.
- Writes: `.docx` (compiled or AI draft), `.md` (compiled; one document for the second brain; this summary). Tray, theme and draft options in localStorage.
- Sends nothing anywhere, except the AI draft prompt to Claude when that button is pressed in the artifact edition.

## Checks

Mechanical, run by `tools/test_core.js` in Node on the real pack: 16 checks pass. They cover word-start matching, query parsing, AND holding for every returned document (47 documents for `rdii unit hydrograph`), any >= all, type filter, year filter, negation, Related excluding its own document, second-brain search and backlinks, compile blocks (quotes, sources, disclosure), prompt keeping all passages, AI-draft disclosure, and CRC-32 of "123456789" = 0xCBF43926.

Query timings in that run (Node, build machine, all 19,145 passages scanned per query):

| Query | Documents | Passages | ms |
|---|---|---|---|
| `rdii unit hydrograph` | 47 | 1137 | 36 |
| `"dynamic wave" stability` | 23 | 208 | 24 |
| `preissmann slot` | 41 | 197 | 22 |
| `green ampt infiltration` | 65 | 1200 | 36 |
| `2d mesh` | 52 | 517 | 11 |
| `force main hazen` | 21 | 648 | 23 |
| `zzzqqq` | 0 | 0 | 2 |

Mechanical, run by `tools/test_page.js` in headless Chromium: 22 checks pass (load, search, tick to tray, reader, every tab in dark and light, same result order in both themes, Word file bytes start with a zip signature).

Generated .docx files: opened as zip, with python-docx, and converted to PDF by LibreOffice without error.

Second-brain match: median best cosine 0.11; 155 of 620 documents below 0.08; 108 at 0.20 or more.

Complexity Meter (analyzer 1.7.0, baseline HC-2026-11-10-h, HydroCouple = 100): index 54.8; Size 45.9, Structure 67.2, Test evidence 17.5, SWMM vocabulary 53.2; shipped .html without data 40.8.

Human review: none yet.

## What this does not show

1. The Google Drive archive (drive G:) is not in the pack. Drive files could not be opened in bulk from the build session.
2. Google Docs, PDFs, .chm help files and email are not read.
3. Figures, images and equations are not extracted. Scanned pages have no text.
4. No person has compared extracted text with the original files.
5. The 36 "not about modeling" exclusions are keyword counts, not judgements. The list is in `excluded.json`.
6. Topic labels are keyword rules and unreviewed.
7. Second-brain similarity is shared vocabulary only, and the index is frozen at commit af61331.
8. Dates are the saving computer's clock. 19 documents have no date.
9. Mirror-copy detection uses name plus size; two different files with the same name and size in different folders would be treated as one.
10. Many documents were written by other people (Wallingford Software, MWH Soft, Innovyze, CDM). The app is private for that reason and must not be hosted publicly.

## How to reproduce

On the PC, with the folders mounted: `python3 inv.py <folder>` for each folder, then `s1_list.py`, `s2_conv.py` (repeat until nothing is left), `s3_parse.py`, `s4_build.py`. Copy `pack-pc.json.gz` to `data/`. Then `python3 tools/make_sb.py`, `node tools/test_core.js`, `python3 tools/build.py`, `node tools/test_page.js`, `node tools/complexity.js`, `python3 tools/build.py`, `node tools/build_docx.js`.

## Credits and licenses

Documents: Robert Dickinson's files; many written by colleagues at Wallingford Software, MWH Soft, Innovyze and CDM, whose work they remain. Conversion of old formats: LibreOffice. Ranking: Okapi BM25, S. E. Robertson and S. Walker, 1994. Second-brain wiki: dickinsonre/swmm-second-brain (CC BY 4.0 for the wiki). Complexity figure: analyzer of the SWMM App Complexity Meter. App code: Robert Dickinson; no license granted, private.

## AI use

This app was built with Claude, Anthropic's AI model, in one Claude session on 19 November 2026, under the direction of Robert (Bob) Dickinson. He asked for it, chose the folders, the file types, the private edition and both ways of making a Word file. Responsibility for what is done with it is his. Claude wrote the scripts that listed the files, collapsed the copies, converted the old files with LibreOffice and extracted the text; the rules that decided which files were about modeling, the topic labels and the matching to second-brain pages; the page, its search, its Word writer, its tests, the Doc essay and this summary. Checks are mechanical (16 in Node, 22 in a browser, Word files opened in two programs). No person has checked the extracted text against the originals, the 72 files left out, the topic labels or the second-brain matches. Inside the app, Build .docx uses no AI; Draft with Claude does and labels the file.

## Changes

`1.0.0 (2026-11-19)`: first build. PC pack of 620 documents; passage search; reader; draft tray with compile and AI-draft .docx; second-brain index and gap list; packs tab for a later Google Drive pack.

**Master SWMM PDF**A cited library of SWMM and rainfall–runoff literature

**0** of **0** documents cited

Every document here carries a full citation. Pick a style, copy it, or open the document. **Hosted** PDFs open straight away; for the others, drop in your own copy and the app recognizes it by fingerprint.

## The shelf, by year

Search the catalog

Availability

Sort

Citation style

Link in citation

[ ] Search inside documents

The citation stays pinned above the page. **Cite this page** copies the reference with the printed page number, not the PDF page.

Document

### Find in this document

Search text

Nothing joins the library without a citation. Drop PDFs here: files already in the catalog are recognized and opened; new ones wait in the queue until their citation is complete.

**Drop PDF files here**\
or pick them; a whole folder works too

Choose PDFsChoose a folder

### Citation for the next new file

Add a file to start. The form fills itself from the PDF where it can (title, DOI, page count); you check it and supply the rest.

Title *

Authors * — one per line, Family, Given; or an organization

Year *

Type

License

Journal, conference, or institution * — or a link below

Volume

Issue

Pages

Publisher

Report number

DOI

Source link (Academia.edu, publisher…)

One-line summary, in your words

Tags, comma separated

Citation preview

Before it can be filed

[ ] Store the PDF with this page so others can open it (U.S. government or Creative Commons only)

Format

Which documents

Export preview

## Every PDF Carries Its Papers

How Master SWMM PDF ties a citation to a file, and why that matters for a model documented in five decades of manuals.

The same essay, with the same seven figures, is also a Word document: `master-swmm-pdf-doc.docx`, delivered alongside this page.

Contents

1. [A file with no papers](#d-open)
2. [What the page is](#d-what)
3. [How it works](#d-how)
4. [What was checked, and how](#d-checks)
5. [What this does not show](#d-limits)
6. [How to use it](#d-use)
7. [AI use](#d-ai)

## A file with no papers

Here is a file called `Storm_water_management_model_version_4.pdf`. It weighs half a megabyte and holds 76 pages. Pull it off Academia.edu and it looks like the SWMM 4 user's manual that Wayne Huber and Robert Dickinson wrote for EPA in 1988. It is part of that manual. The front matter runs to page xxiv, the text stops at page 52 at the end of the Combine Block, and the manual it came from runs past page 500. The Academia.edu page that serves it names an uploader who is neither author. Not one of those facts is written on the file.

That is the normal state of an engineer's library. You collect PDFs for thirty years. Filenames get chopped to forty characters, title pages fall off in somebody's scanner, and on the day you need to cite page 6 you find you don't know which printing you have. A PDF without a citation is hearsay. You can read it. You can't stand on it.

This page holds 38 documents on SWMM and rainfall–runoff modeling: agency manuals and reports, journal articles, conference papers, a thesis and a preprint, from the 1983 USGS manual for PRMS to papers from 2022. Bob Dickinson asked for one rule, and the page enforces it. Nothing sits on the shelf without its papers: a complete citation, a link to where the copy came from, and a fingerprint that ties the citation to the exact file.

SWMM makes the point better than most. The model has been documented in a chain of EPA user's manuals dated 1971, 1975, 1981 and 1988, each an edited descendant of the one before; the 1988 manual says as much in its own abstract. Then it was printed twice. The October 1992 second printing changed the title page, the disclaimer, the preface, and pages 23, 28 to 32, 124, 220 to 221 and 375 to 377a, and its new preface sends readers to `.DOC` files on the distribution disks for options the book never described. Cite “the SWMM 4 manual, page 28” and a reader holding the other printing may be looking at a different interface-file table. Get the papers right first. The reading comes after.

## What the page is

Master SWMM PDF is a card catalog that can read. Each of the 38 records carries the fields a citation needs (authors, year, title, journal or agency, volume, issue, pages, report number, DOI), the link to the Academia.edu copy where one exists, the license its publisher states, a short summary written for this catalog, the file's SHA-256 fingerprint, and a map from PDF pages to printed page numbers. The page draws every citation in five styles. 18 of the PDFs may be passed around freely, so they travel with the page and open in its reader. The other 20 belong to their publishers or authors; for those you bring your own copy, and the page knows it when it sees it.

## How it works

### The fingerprint

Start with the hard part. You drop a file on the page. Which of the documents is it, if any? The filename is no help: Academia.edu names its downloads after a truncated title, and anyone can rename a file. The size is a weak hint, because two different files can weigh the same.

The answer is a hash. SHA-256 reads every byte of a file and boils it down to a 256-bit number, written as 64 hexadecimal digits. Feed it the same bytes and you get the same number, every time, on every machine. Change anything and you get a different number. The SWMM 4 file hashes to `2344096f…637f`, and that string sits on its card. When a file arrives, your browser computes its hash (the file is never sent anywhere) and looks the number up. A match means the citation on that card describes the file in your hand, down to the last byte.

**Figure 1.** The page never trusts a filename. It computes the file's SHA-256 in your browser and looks the number up; only an exact match opens with a citation, and anything else must earn one.

Now look at the other branch. When there is no match, the file goes into a queue and a citation form opens. The form fills in what it can read from the PDF: the largest type on page 1 as a guess at the title, any DOI it finds, a year. The **File it** button stays dead until five checks pass: a title, at least one author or organization, a four-digit year, a place where it appeared (journal, institution, publisher, DOI or link), and a link that starts with `http` if you gave one. That is the rule built into the machinery. A PDF can wait in the queue as long as you like. It cannot join the library without its papers.

### Where the citations came from

The records were built in two stages. First, a script read every file: its SHA-256, its page count, the first three pages of text, and any string shaped like a DOI. Then four research passes, about nine records each, checked every record against outside sources: Crossref for the bibliographic data behind each DOI, the publisher's or agency's own page for the license and the report number, and Academia.edu search for the page Bob downloaded from.

**Figure 2.** Every number on a card came from reading the file or from an outside source named on the card. Counts are from this build.

The checking turned up things no title page will tell you. Three DOIs are not printed in their PDFs at all and came from Crossref. The SWMM Applications Manual's title page carries a placeholder report number, EPA/600/R-09/000; EPA's Science Inventory gives the real one, EPA/600/R-09/077. An EPA overview of rainfall–runoff model types prints EPA/600/R-14/152 on its cover, while EPA's catalog lists it as EPA/600/R-17/482. And one paper's “SWMM” turned out to mean Malaysia's stormwater management manual, not EPA's model. Each card's **How this citation was checked** line records what was done and where.

**Figure 3.** Eighteen PDFs travel with the page because their licenses allow it. Two that might have been hosted were held back over conflicting notices.

### Printed pages are not PDF pages

Here is the problem that bites anyone who cites a page. A PDF reader counts from 1 at the first sheet in the file. A printed document numbers its pages however its publisher pleased. In the SWMM 4 file, PDF page 30 is printed page 6, because 24 pages of front matter come first, numbered i through xxiv. A journal article that starts on page 211 has its PDF page 1 printed 211. Cite the PDF page and you have sent your reader to the wrong place.

The fix is an offset: printed page equals PDF page minus some number. Finding that number for every document by hand is drudgery, so the build holds an election. It looks at the first and last three lines of each page for a lone number, a running header such as “2 of 27”, or a number sitting at the end of a header line. Every number it finds casts one vote for the difference between the PDF page and the printed page. The most common answer wins.

**Figure 4.** In the SWMM 4 excerpt, 51 of the 52 pages with a readable number agree that printed page = PDF page − 24. The one dissent is a table line the counter mistook for a page number.

In the SWMM 4 file, 52 pages carried a readable arabic number. Fifty-one voted for 24. The odd one out came from PDF page 56, where a table assigns logical unit 5 to the card reader, and the counter took that 5 for a page number. One stray vote among 52 doesn't swing an election. That is the whole virtue of voting over trusting the first number you see.

The election is half the check. For 14 documents the build had both an elected offset and the page range printed in the published citation. 12 agreed. The two that didn't were each telling the truth about something. Sutherland and Jelen's 2003 paper in the *Journal of Water Management Modeling* is missing printed pages 258 and 259 from the upload, so its offset jumps by two after PDF page 5. Lin and colleagues' 2004 paper is the authors' manuscript, numbered 1 to 8, not the proceedings pages 1899 to 1906. The page map handles the first case with two segments. For the second it refuses to guess and shows PDF pages, because a manuscript page is not a citable proceedings page.

**Figure 5.** A single offset is not always enough. Blue lines are the page maps the page uses; dots are page numbers read from the footers (numbers from tables are left off). The JWMM upload skips printed pp. 258–259; the PRMS scan has page 207 bound out of order.

The 1983 PRMS manual had its own trick. Its scan carries Attachment VIII, printed page 207, bound between pages 164 and 165. The page map carries a one-page exception, so PDF page 172 reports 207 and PDF page 173 reports 165. In all, 32 of the 38 documents have a page map. For the other 6, **Cite this page** says plainly that it is giving a PDF page.

### One record, five styles

A citation style is a formatting rule and nothing more. APA wants initials and an ampersand. ASCE wants “and”, and quotation marks around an article title. Chicago spells out given names. BibTeX and RIS feed reference managers. The page stores each document once, as fields, and runs the fields through five small formatters. Change the style menu and all 38 cards redraw.

**Figure 6.** One record, three of the five styles, exactly as the page's formatters write them. The link is the Academia.edu copy because that is the default “Link in citation” choice.

One choice is left to you: which link goes into the citation. APA and its cousins prefer the DOI, the publisher's permanent address. Bob asked for the Academia.edu copy, the place he actually got the file. The **Link in citation** menu decides which comes first. Every card shows both.

## What was checked, and how

- Fingerprints, page counts and file sizes come straight from the 38 files.
- 25 DOIs were resolved against Crossref or the publisher's page, and the title, authors, volume and pages compared with the PDF.
- 25 Academia.edu pages were opened and their titles matched to the file.
- Page offsets: 12 of 14 agreed with published page ranges, and the 2 disagreements were traced to their causes.
- The citation engine ran on all 38 records in all five styles in a headless Chromium browser, in both themes and at phone width, with no console errors and no sideways scrolling.
- Filing was tested both ways: a catalog file was recognized by its fingerprint and opened; a new file was held until the five checks passed, then filed.

What no person has checked yet: the 38 citations themselves, the license calls and the summaries. They are Claude's work until Bob or another reader confirms them. The **Correct citation** button, shown to people with edit rights on the published page, exists for exactly that.

## What this does not show

A fingerprint is strict by design, and strictness cuts both ways. Flip a single bit in the middle of the SWMM 4 file, at byte 253,103 of 506,207, and the hash changes in 128 of its 256 bits, exactly half, which is what a good hash is supposed to do. So the page will not recognize a copy that has been re-saved, re-compressed, run through OCR again, or downloaded from a different site, even when a person would call it the same paper. It will ask for a citation as if the file were new. Take that as a feature. The citation on a card describes those bytes, and a different file may be a different version.

**Figure 7.** Flip one bit of the 506,207-byte SWMM 4 file and half the bits of its fingerprint change. That strictness is why a match can be trusted, and why a re-saved copy will not match.

- Licenses are Claude's reading of what each publisher states. Two conflicts were set aside rather than settled: a paper whose journal web page says CC BY while its PDF says all rights reserved, and a *Journal of Hydrology* paper by NOAA authors whose text is a U.S. government work but whose file is Elsevier's typeset PDF. Neither is hosted.
- 13 records have no Academia.edu link. The session's web-search allowance ran out before every search could be tried, so those citations use the DOI or an official page. Another pass may find more.
- Some uploads are not the version of record: the SWMM 4 excerpt, the JWMM paper missing two pages, two authors' manuscripts, and a discussion preprint that *Hydrology and Earth System Sciences* did not accept for further review. Their cards say so.
- One review paper carries no date and is cited “n.d.”. One MSc thesis has no online record and is cited from its title page alone.
- The summaries describe; they do not review. Nothing on a card says whether a paper's conclusions hold.
- Hosting follows each publisher's stated license, not the copyright law of any particular country.

## How to use it

1. **Library.** Search, filter by type or availability, pick a citation style, and copy. Click a spine on the shelf chart to jump to its card.
2. **Open in reader.** Hosted files open at once. For the others, choose your copy; the page checks its fingerprint and opens it in your browser.
3. **Cite a page.** In the reader, find text in the document, then use **Cite this page** for a citation with the printed page number.
4. **Add PDF.** Drop new files, complete each one's citation, and press **File it**.
5. **Export.** Take the whole library, or just what the Library tab shows, as BibTeX, RIS, CSL-JSON, CSV or a formatted reference list.

## AI use

This page and this essay were made with Claude, Anthropic's AI model, in one Claude session on October 25, 2026, under the direction of Robert (Bob) Dickinson. He supplied the files and the Academia.edu link for the SWMM 4 manual, set the rule that every PDF carries a citation, and is responsible for the result. Claude read the files, ran the four research passes against Crossref, publisher and agency pages and Academia.edu, decided what could be hosted from the stated licenses, wrote the summaries in its own words, computed the fingerprints and page maps, wrote the page's code and formatters, drew the figures from measured numbers, and wrote this essay and the matching Word document. The mechanical checks are listed above. No person has yet checked the citations, the license calls or the summaries.
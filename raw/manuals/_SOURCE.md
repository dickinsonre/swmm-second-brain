# Where the files in raw/manuals/ came from

Copied on 14 November 2026 from Bob's public repository
https://github.com/SWMMEnablement/SWMM_MD_Documents at commit 6a6b317 (29 May 2026),
byte for byte, under their original names.

## Copied (U.S. government reports, and the SWMM 4.4 block documentation)

| File here | What it is |
|---|---|
| `epaswmm5_1_manual_master_8-2-15.md` | SWMM User's Manual Version 5.1, L. A. Rossman, EPA/600/R-14/413b, revised September 2015 |
| `EPA_SWMM_VOLUME_II_HYDRAULICS.md` | SWMM Reference Manual, Volume II, Hydraulics, L. A. Rossman, EPA/600/R-17/111, May 2017 |
| `EPA_WQ_LID.md` | SWMM Reference Manual, Volume III, Water Quality, L. A. Rossman and W. C. Huber, EPA/600/R-16/093, July 2016 |
| `SWMM5_QA.md` | SWMM quality assurance report, dynamic wave flow routing, EPA/600/R-06/097, September 2006 |
| `SWMM3 (1-249).md`, `SWMM3 (250-546).md` | SWMM User's Manual Version III, Huber, Heaney, Nix, Dickinson and Polmann, EPA-600/2-84-109a, November 1981 (tenth printing, 1987), in two parts |
| `SWMMCatUsersGuide.md` | SWMM-CAT User's Guide, L. Rossman, EPA 600-R-14-428, September 2014 |
| `USGSreport.md` | Calibration of a distributed routing rainfall-runoff model at four urban sites near Miami, Florida, Doyle and Miller, USGS Water-Resources Investigations 80-1, February 1980 |
| `culvert_designhds5_03r.docx.md` | Hydraulic Design of Highway Culverts (HDS-5), FHWA-NHI-01-020, September 2001 |
| `swmm44/*.txt` | Input documentation of the SWMM 4.4H blocks (Extran, Runoff, Transport, Rain, Temp, Statistics, Storage/Treatment, shapes, Transport water quality) and the 4.4 change list, from the 2004 CDM/OSU distribution |

The markdown files are conversions of PDFs. Most equations did not survive the
conversion and the figures (the `media/` and `images/` folders of the source
repository, 54 MB) were not copied. The original PDFs are in the source repository.

## Not copied, and why

| In the source repository | Why it was left there |
|---|---|
| `HydrologyandFloodplainAnalysis5thed{a,b,c}.md` | A commercially published textbook, under copyright |
| `Allan_Goyen_Diss.md`, `Nimmer Zaman Master's Thesis*.md` | A dissertation and a thesis; their authors hold the copyright |
| `InfoSWMM/xpswmm_Reference_Manual.docx.md`, `InfoSWMMApplicationsGuide.md`, `ruby_icm_help.md`, the InfoSWMM and InfoSewer help pages, `AI Files/` | Innovyze and Autodesk product documentation. Bob to decide whether any of it belongs in a public repository of his |
| `InfoSWMM/*.docx.md` and `InfoSewer/*.docx.md` that are Bob's own write-ups | Not yet sorted from the product documentation around them |
| `SWMM5plus_Installation_Guide.md` | Author and licence not stated in the file |
| `WCH_2004_SWMM_Fortran_Code/*.FOR`, `*.INC` | Source code; it lives in `SWMMEnablement/WCH_2004_SWMM44H` |
| The PDFs | The 1971 volumes, SWMM 2, 3 and 4 manuals and the Extran manuals are scans without a text layer here; they need conversion first |

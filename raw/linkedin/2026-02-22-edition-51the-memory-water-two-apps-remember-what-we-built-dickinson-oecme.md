---
title: "Edition 51—The Memory of Water: Two Apps That Remember What We Built in 5 SWMM Releases"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-51the-memory-water-two-apps-remember-what-we-built-dickinson-oecme
created: "2025-05-26 21:10"
published: "2026-02-22 16:18"
words: 839
export_sha256: 9425c2d7570471d272a3c754486b5dae4144ed869e1a36edd5501b79e16197df
---
# Edition 51—The Memory of Water: Two Apps That Remember What We Built in 5 SWMM Releases

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![](https://media.licdn.com/mediaD4E12AQGuu8Rs_-VGMg)

There is a peculiar thing about institutional knowledge. It accumulates slowly, over decades, in manuals and reports and technical memoranda that circulate among specialists, and then quite suddenly it becomes invisible. Not lost, exactly. Merely buried. Filed in cabinets that no one opens, hosted on servers that no one indexes, printed in documents that no one digitizes. The knowledge is there. It simply cannot be *found*.

This is, if you think about it, a bit silly and a low-level scandal. Not the dramatic kind that makes headlines, but the quiet kind that costs thousands of engineers thousands of hours every year rediscovering what someone carefully documented in 1971, or 1983, or 2004—and then filed away.

This week I want to introduce two apps that address this problem directly. They are, in their different ways, acts of remembering.

> **The Archive:** [**swmmdocs.com**](http://swmmdocs.com)

The first is **SWMM Docs Explorer** is a searchable archive of the entire documentary history of EPA's Storm Water Management Model for SWMM1 to SWMM5

Let that sink in for a moment. **186 documents.** Eight eras of development, from SWMM I (1969–1971) through SWMM 5.2 and beyond. **15 equations** indexed and cross-referenced. **61 cross-references** linking concept to concept across half a century of hydraulic science.

The Manning equation that governs every conduit calculation in your model today?

**Q = (1/n) A R^(2/3) S^(1/2)**

It first appeared in the July 1971 SWMM I Final Report. It is still there, unchanged in principle, in SWMM 5.2. The archive shows you both and everything in between.

You can search for "Green-Ampt infiltration" and trace how the method evolved from SWMM 3 through SWMM III's expanded treatment to SWMM 5's modern implementation. You can compare the EXTRAN block's card-image \`.dat\` format from SWMM 3:

EXTRAN

H1 720 30. 8 1 1

I1 1 1 2 400. 96.0

against SWMM 5's section-based\`.inp\`:

\`\`\`

\[SUBCATCHMENTS\]

;;Name RainGage Outlet

S1 RG1 J1

\`\`\`

…and understand, viscerally, how far input file design has come.

The archive includes an **AI chat** for querying the pdfg and md files, **cross-era comparison tools**, and a roadmap that includes AI-assisted equation extraction from scanned PDFs. It is, in short, the institutional memory that the SWMM community never had in one package until now.

> **The Manual:** [**sjswmm5manualsearch.com**](http://sjswmm5manualsearch.com)

The second app is **SWMM5 Manual Search** and if the archive is the library, this is the reading room.

It takes the current SWMM 5.2 User's Manual — **5 documents, 621 sections, 248,407 words**—and makes every sentence instantly searchable with a speed and precision that the PDF format was never designed to provide.

Search for "Manning roughness," and you get results across Surface Runoff, Appendix A, Cross-Section Geometry, and Advanced Features—all ranked by relevance, all clickable, and all showing context. Use commas for AND logic. Use quotes for exact phrases. Filter by chapter. Export to CSV or PDF.

But here is the feature that would have personally saved me an embarrassing number of hours over the years: the **ICM Mapping tab**.

Every single INP file section—all **40 of them**—is mapped to its InfoWorks ICM equivalent. **294 field mappings** between SWMM5 and ICM, with both the InfoWorks HW Ruby variables and the ICM SWMM Ruby variables documented side by side.

Want to know how a SWMM\`\[JUNCTIONS\]\` Elevation field maps to ICM? It is\`node.chamber_floor\` in InfoWorks and\`node.elevation\` in ICM SWMM. Want to know how orifice discharge coefficients convert? ICM Cd = SWMM5 Cd × √2. It is all there every weir type mapping, every pump curve translation, every infiltration parameter correspondence.

For those of us who live in both the SWMM and ICM worlds—and in 2026, that is a great many of us—this is not a convenience. It is a necessity.

> **Why This Matters and thanks to those who helped me with this**

[https://www.linkedin.com/posts/robertdickinson_swmm-is-now-55-years-old-and-it-has-a-long-activity-7431346381359017984-6HdI?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEAvcwBVte4NjFU9EyFPNigxyghgnrHf9c](https://www.linkedin.com/posts/robertdickinson_swmm-is-now-55-years-old-and-it-has-a-long-activity-7431346381359017984-6HdI?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEAvcwBVte4NjFU9EyFPNigxyghgnrHf9c)

[https://www.linkedin.com/posts/robertdickinson_replit-activity-7430770662866329600-JjMF?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEAvcwBVte4NjFU9EyFPNigxyghgnrHf9c](https://www.linkedin.com/posts/robertdickinson_replit-activity-7430770662866329600-JjMF?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEAvcwBVte4NjFU9EyFPNigxyghgnrHf9c)

> **Links**

**SWMM Docs Explorer** → [swmmdocs.com](http://swmmdocs.com)

**SWMM5 Manual Search** → [sjswmm5manualsearch.com](http://sjswmm5manualsearch.com)

Both are free. Both are open. Both are built for the engineers who do the math.

*— Edition 51 of EPASWMM5 Related Software*

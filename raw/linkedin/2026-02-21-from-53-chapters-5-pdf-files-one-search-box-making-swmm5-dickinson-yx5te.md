---
title: "From 53 Chapters in 5 PDF Files to One Search Box: Making the SWMM5 Manuals More Usable and connected to ICM InfoWorks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/from-53-chapters-5-pdf-files-one-search-box-making-swmm5-dickinson-yx5te
created: "2026-02-09 19:02"
published: "2026-02-21 00:29"
words: 1591
export_sha256: c0acababe4bb29e1f29e1cf175b8101e9aa7e5dbe5133aa7d8e29ccf549d7523
---
# From 53 Chapters in 5 PDF Files to One Search Box: Making the SWMM5 Manuals More Usable and connected to ICM InfoWorks

![From 53 Chapters to One Search Box: Making the SWMM5 Manual More Usable](https://media.licdn.com/mediaD4E12AQFGUbfVWCVqfA "From 53 Chapters to One Search Box: Making the SWMM5 Manual More Usable")

**After four decades of working with EPA's Storm Water Management Model, I got tired of the same workflow every engineer knows: open an 800-page PDF, hit Ctrl+F, scroll endlessly, lose your place, and repeat across three different manual volumes. Multiply that by every parameter lookup, every INP file question, and every time a colleague asks "what's the field name for capillary suction head again?" Now in a Repl.it app you can search all five SWMM5 manuals and in a companion app search SWMM1 to SWMM4 manuals (for history),**

> So I built the tool I wished existed.

**\[**[**sjswmm5manualsearch.com**](http://sjswmm5manualsearch.com)**\](**[**https://sjswmm5manualsearch.com)**](https://sjswmm5manualsearch.com)**) **— a full-text search engine for the entire EPA SWMM 5.2 Reference Manual, with INP file cross-references and ICM InfoWorks/SWMM Ruby variable mapping. These are the source manuals form**

![](https://media.licdn.com/dms/image/v2/D4E12AQEVq_7bktyQNA/article-inline_image-shrink_1500_2232/B4EZx9aTGzIQAU-/0/1771630572673?e=1795651200&v=beta&t=l2fv8J3OAzIDvxCMJqcsynPmrEC-oUGtMwR7jGGntH0)

Here's how the source website maps to your app's Table of Contents:

The source site ([swmm-manual.netlify.app](http://swmm-manual.netlify.app)) has **5 manuals** in its sidebar:

1.  SWMM v5.2 Users Manual

2.  Reference Manual Vol I - Hydrology

3.  Reference Manual Vol II - Hydraulics

4.  Reference Manual Vol II Addendum - Hydraulics

5.  Reference Manual Vol III - Water Quality and LID

The replit app's crawler pulled content from **all 5 manuals** and combined them into one unified, searchable collection. The Table of Contents in your app shows **53 documents with 621 sections** — that's everything from all 5 manuals flattened into a single browsable index.

The mapping roughly works like this or the app cmbines five manuals into one searcjhable manual.

**Source ManualYour TOC ChaptersUsers Manual**Chapters 1–12, Appendices A–E, Glossary, Intro**Ref Vol I – Hydrology**Chapter1-Overview, Chapter2-Meteorology, Chapter3-SurfaceRunoff, Chapter4-Infiltration, Chapter5-Groundwater, Chapter6-Snowmelt, Chapter7-RDII**Ref Vol II – Hydraulics**Chapter1-PreissmannSlot, Chapter2-HydraulicModel, Chapter3-DynamicWave, Chapter4-KinematicWave, Chapter5-CrossSection, Chapter6-PumpsRegulators, Chapter7-AdvancedFeatures**Ref Vol II Addendum**Chapter2-StreetCrossSections, Chapter3-StorageUnitGeometry, Chapter4-Pumps, Chapter5-StormDrainInlets**Ref Vol III – Water Quality/LID**Chapter2-UrbanRunoffQuality, Chapter3-PollutantBuildup, Chapter4-SurfaceWashoff, Chapter5-TransportAndTreatment, Chapter6-LowImpactDevelopmentControls

So while the source site spreads across 5 separate sidebar menus, the app unifies it into one searchable, cross-referenced system. That's the value—instead of switching between 5 manuals, engineers search once and get results from everywhere.

![](https://media.licdn.com/dms/image/v2/D4E12AQFG_O8IVh2i3g/article-inline_image-shrink_1500_2232/B4EZx9b4hiKoAU-/0/1771630988601?e=1795651200&v=beta&t=JXkWEZg6MysaPEh356rJ7VgKWnk2doKRiX54IUUTlPc)

> **What It Actually Does**

**The foundation comes from the incredible work of Scott Jeffers, PE, PhD, who converted the entire SWMM 5.2 User's Manual from PDF into structured, web-accessible Markdown hosted at** [**swmm-manual.netlify.app**](http://swmm-manual.netlify.app)**. That alone was a huge contribution to the SWMM community.**

![](https://media.licdn.com/dms/image/v2/D4E12AQHKiARZD45x6Q/article-inline_image-shrink_1500_2232/B4EZx9Y.iFH0AU-/0/1771630225867?e=1795651200&v=beta&t=5s-KgK366_PuTu9L3baLmSVzQ3D5aSVI2s3JNu9Ck08)

**What I built on top of that is a search engine that crawls Scott's collection and creates a full-text index across:**

**📖 53 chapters — from Introduction through every Appendix**

**📄 631 searchable sections — every subsection individually indexed**

**📝 251,000+ words — the complete manual, every equation, every parameter**

**📚 1,416 glossary terms — auto-extracted and clickable**

**📋 25+ INP file sections — with field definitions, data types, and examples**

**Type "Green-Ampt" and you get 91 results in milliseconds — the governing equations from Chapter 4, the parameter estimates, the computational scheme, the Appendix C editor fields, AND the actual INP file syntax. All cross-linked. No more hunting through PDFs.**

> **The Feature That Surprised Even Me: INP F**ile Cross-Reference

**Here's what makes this different from just searching a PDF. When you look up any INP file section — say\`\[CONDUITS\]\` or\`\[INFILTRATION\]\` or\`\[LID_CONTROLS\]\` — you see:**

**✅ The manual explanation of what each field means**

**✅ The exact INP syntax with field order and data types**

**✅ Example entries showing real formatting**

**✅ Category organization (Hydrology / Hydraulics / Quality / LID)**

**I built a dedicated 453-line database (\`inp\_**[**reference.py**](http://reference.py)**\`) that maps every INP section, every field, every unit. Engineers who build or debug INP files by hand — and we all end up doing it eventually — will understand why this matters.**

![](https://media.licdn.com/dms/image/v2/D4E12AQGj4WbM3Qkh_g/article-inline_image-shrink_1500_2232/B4EZx9Yf8oKIAU-/0/1771630100792?e=1795651200&v=beta&t=67QLPUxy-GZ-eisBB6OtN932ZDYlHNIyrmketHkR-5o)

> **The ICM Mapping: A First-of-Its-K**ind Cross-Reference

**This is where it gets really interesting for the growing number of engineers who work across both EPA SWMM and Autodesk's ICM platform.**

**For every SWMM5 INP field, the tool now shows:**

**🔶 ICM InfoWorks HW table name (e.g.,\`hw_conduit\`,\`hw_node\`)**

**🟢 InfoWorks Ruby variable (e.g.,\`**[**conduit.us**](http://conduit.us)**\_node_id\`,\`node.chamber_floor\`)**

**🔵 ICM SWMM SW table name (e.g.,\`sw_conduit\`,\`sw_node\`)**

**🟣 ICM SWMM Ruby variable (e.g.,\`conduit.from_node\`,\`node.elevation\`)**

**⚙️ Conversion notes — the non-obvious gotchas**

![](https://media.licdn.com/dms/image/v2/D4E12AQEunJMGVa91VA/article-inline_image-shrink_1500_2232/B4EZx9Xu.rJ0AU-/0/1771629900353?e=1795651200&v=beta&t=UFsslyQ0r_39xn1AQICH97bWIDxsjVXYlkbT3_YWbRQ)

**That last point is critical. Did you know:**

**- SWMM5 orifice discharge coefficient Cd becomes Cd × √2 in InfoWorks?**

**- Weir coefficients convert differently for transverse vs. V-notch?**

**- Link offsets in SWMM5 can be depth-based, but InfoWorks always stores elevation?**

**- Manning's n can import as either n or 1/n (Manning M) depending on a dialog checkbox?**

**- Pump curves need to be reversed (ICM expects descending heads)?**

**- Patterns and rainfall time series are NOT auto-imported — you have to copy them manually?**

**Every one of these has bitten someone during a model conversion. Now they're documented in one searchable place.**

**This cross-reference doesn't exist anywhere else. Not in the SWMM manual, not in the ICM documentation, not in any published paper I'm aware of. It came from years of actually doing these conversions.**

**---**

> **The Search Is Powerful**

**This isn't a simple Ctrl+F. The search engine supports:**

**Manning roughness\` — matches either word -\`"pump curve"\` — exact phrase matching -\`infiltration, groundwater\` — AND logic (comma-separated) -\`inlet OR outlet\` — explicit OR -\`Chapter\* pump\` — wildcard matching - Filter by chapter group, content type, or INP syntax only - Sort by relevance, chapter order, or alphabetical - Export results to CSV or PDF**

![](https://media.licdn.com/dms/image/v2/D4E12AQHrAaN1R5pU4w/article-inline_image-shrink_1500_2232/B4EZx9W.h0HwAU-/0/1771629701918?e=1795651200&v=beta&t=s0c70QYGcYRMZ2uLyMUbcUnQg5A4h9hgaUudzhZh8XU)

> **Claude-powered AI assistant that can answer natural-language questions about SWMM in 20+ languages.**

**There's also a Claude-powered AI assistant that can answer natural-language questions about SWMM in 20+ languages. Ask it "How do I set up a bio-retention cell in SWMM?" and it pulls context from the manual's 631 sections to give you a grounded answer.**

![](https://media.licdn.com/dms/image/v2/D4E12AQGcFT9bTpFs-w/article-inline_image-shrink_1500_2232/B4EZx9Wfa1GkAc-/0/1771629574533?e=1795651200&v=beta&t=EddDoHBefbJwV_AMnoEMFipuV1eWkje6qIOphUOCXaM)

> **\### Why Open Source Transparency Matters**

**Every line of code is viewable directly in the app—all 11 files, 6,385 lines. You can see exactly how the search works, how the INP reference database is structured, and how the crawler builds the index. No black boxes.**

> **The tech stack is deliberately lean:**

![](https://media.licdn.com/dms/image/v2/D4E12AQG_tPS96E9ftQ/article-inline_image-shrink_1500_2232/B4EZx9WIFzIsAU-/0/1771629479739?e=1795651200&v=beta&t=2GPz7rfpag5gInX1kOs4pmmkDFF1IBEBy7lfd-EgNUI)

> **There is even a tab showing you changes to the SWMM5 Gui and Engine Version History over time**

![](https://media.licdn.com/dms/image/v2/D4E12AQE3JzJjfZCyBQ/article-inline_image-shrink_1500_2232/B4EZx9WWjgIMAU-/0/1771629538915?e=1795651200&v=beta&t=hwQsT9W1N6pnqEF9eIWYDb1HeAFHK5drDd-gcAS3Q3g)

> **\### The Bigger Picture: Preserving Engineering Knowledge**

**This tool is part of a broader effort at** [**https://swmmdocs.com/**](https://swmmdocs.com/) **where we're building an archive of 55 years of SWMM documentation—from the original 1971 punch-card era manuals through modern SWMM 5.2. Twenty-nine documents are already archived in searchable Markdown, with an Equation Gallery showing how key formulas (Manning, Green-Ampt, Horton, Saint-Venant) evolved across eight SWMM eras, and a Fortran Rosetta Stone mapping original subroutines (EXTRAN, SMPIPE, SJUNC, RUNOFF) to their modern C and Ruby equivalents.**

**Critical engineering knowledge shouldn't be trapped in scanned PDFs that no search engine can read and no AI can reason about. These tools are about making 55 years of hydraulic science accessible to the next generation of engineers.**

**---**

> \### Try It

**🔗 \[**[**sjswmm5manualsearch.com**](http://sjswmm5manualsearch.com)**\](**[**https://sjswmm5manualsearch.com)**](https://sjswmm5manualsearch.com)**)**—SWMM 5.2 manual search + INP reference + ICM mapping**

**🔗 \[**[**swmmdocs.com**](http://swmmdocs.com)**\](**[**https://swmmdocs.com)**](https://swmmdocs.com)**) **— 55-year SWMM documentation archive**

**Both are free. No login required. No API key. Just search.**

**If you work with SWMM, ICM, InfoSWMM, PCSWMM, or XPSWMM, bookmark these. If you've ever cursed at a PDF trying to find a parameter value — these are for you.**

**And if you have a copy of the SWMM 4.4 User Manual or Huber & Dickinson (1988) sitting in a filing cabinet somewhere, the archive needs you. Every document helps preserve SWMM's engineering heritage.---**

***Special thanks to* \*Scott Jeffers, PE, PhD\*\* for converting the SWMM 5.2 manual into the structured web collection that makes all of this possible.\*---**

**\#SWMM \#StormwaterModeling \#EPA \#HydraulicEngineering \#WaterResources \#ICM \#InfoWorks \#CivilEngineering \#OpenSource \#UrbanDrainage \#WasteWater \#HydrologyEngineering \#EnvironmentalEngineering**

---
title: "SWMM1 to SWMM5 Documentation Archive and Explorer (1970 to 2026)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/swmm1-swmm5-documentation-archive-explorer-1970-2026-robert-dickinson-zppbe
created: "2025-12-15 16:57"
published: "2026-02-22 14:37"
words: 2554
export_sha256: d69abe68a657be1db5f708da48978d5403274feeeb073c080711cca3b9a912c6
---
# SWMM1 to SWMM5 Documentation Archive and Explorer (1970 to 2026)

![](https://media.licdn.com/mediaD4E12AQGEcRN6ZuzYdA)

The SWMM Documentation Archive and Explorer is a web application that organizes, preserves, and makes searchable over five decades of EPA Storm Water Management Model (SWMM) engineering documentation. From the original 1969 SWMM I reports to the latest SWMM 5.2+ releases, the archive spans 186 documents across 8 distinct eras of stormwater modeling history. I am the source of many of these but other sources besides the USEPA are Mitch Heineman and Scott Jeffers.

The project was created by me Robert Dickinson, a core developer of SWMM 3, SWMM 4, and SWMM 5, and the former Project Manager for Innovyze's InfoSewer and InfoSWMM commercial products. It is maintained through my SWMMEnablement GitHub organization: [https://github.com/SWMMEnablement](https://github.com/SWMMEnablement) so if you want to add more please add them to the repository.

> **The Quiet Accumulation of Running Water Or, How Fifty-Five Years of Stormwater Science Found a Home**

It is a peculiar habit of our civilization that we build great cities and then act surprised when it rains. Our ancestors I think had a more realistic understanding a drainage was important in Minoan and Indus Valleny Civilizations and many others.

The rain, of course, does not care about our surprise. It falls on rooftops and parking lots and carefully manicured lawns with equal democratic enthusiasm, and then — having no particular agenda beyond gravity — it runs downhill. What happens next is either an orderly flow through pipes and channels to some receiving body of water, or it is a flooding catastrophe. The difference between these two outcomes is, more often than most people appreciate, a matter of mathematics.

In 1969, the United States Environmental Protection Agency began work on a mathematical model to describe this ancient and unglamorous process — the journey of rainwater across and beneath the surfaces we have so enthusiastically paved. They called it the **Storm Water Management Model**, or SWMM, because government agencies have never been accused of excessive poetry. I liked the name when I first heard in 1973. . The first version spoke the language of punch cards and batch processing. Its equations — Manning's formula for open-channel flow, Horton's exponential decay of infiltration, the venerable versions of the Saint-Venant equations that describe the conservation of mass and momentum in unsteady flow — were already old when the SWMM1 programmers encoded them, some dating to the nineteenth century. But encoding them *together*, in a system that could simulate an entire urban watershed from raindrop to outfall, was something genuinely new.

That was 1971. What followed was the kind of slow, unglamorous, magnificent scientific evolution that rarely makes headlines but quietly holds cities together. **SWMM II** arrived in 1975. **SWMM III** in the early 1980s and introduced the EXTRAN block for dynamic wave routing — a fancy way of saying the model could finally account for water that, contrary to all polite expectations, sometimes flows *backward* in a pipe. **SWMM IV** carried the work through the turn of the millennium. **SWMM 5**, which appeared in 2004 and continues to this day in version 5.2, rewrote the architecture in C entirely while preserving the essential physics.

186 documents. Fifteen indexed equations. Eight distinct eras. Sixty-one cross-references linking concept to concept across half a century. All of it — from the original typeset reports with their teletype formatting to the modern user manuals — has now been gathered, digitized, indexed, and made searchable in a single archive called **SWMM Docs Explorer**.

It is, in its quiet way, a remarkable thing: the entire intellectual history of how we learned to predict where water goes when we would rather it didn't. The equations on the landing page are not decorative. Manning's equation — \$Q = \frac{1}{n} A R^{2/3} S^{1/2}\$ — still governs every conduit calculation in the current model, unchanged in principle from the version a nineteenth-century Irish engineer derived by measuring flow in earthen channels. The Saint-Venant equations still express the conservation laws that no amount of software refactoring can repeal.

The archive includes an AI-powered chat for querying the md or pdf files, tools for cross-era comparison, and an INP file reference that traces the evolution of input formats from card-image\`.dat\` files (where a misplaced column could ruin a week's work) to the comparatively forgiving section-based\`.inp\` format of SWMM 5.

There is a lesson here that extends well beyond hydrology. Science does not always advance by revolution. Sometimes it advances by the patient accumulation of better approximations, better numerical methods, better ways of organizing the same fundamental truths. Water still runs downhill. Manning's *n* still matters. But our ability to *predict the consequences* — across a whole city, in real time, under conditions that haven't happened yet — is incomparably greater than it was when those first punch cards clattered through the reader.

> **\## Key Numbers**

\- SWMM Eras: 8

\- Archived Documents: 163

\- Indexed Equations: 15

\- Cross-Referenced Concepts: 12

\- Citation Links: 14

\- Timeline Events: 13

\- Document Categories: 14

\- Years of History: 55+

![](https://media.licdn.com/dms/image/v2/D4E12AQFxjHsDzYn-jw/article-inline_image-shrink_1500_2232/B4EZyA3YCpGYAU-/0/1771688527052?e=1795651200&v=beta&t=RE9QbQcYEP_QwcKLjUfHiADQo5TnKDRVW_6xxaziTkE)

\## Features

> **\### 1. Search-First Homepage**

The homepage leads with a large, prominent search bar embedded in the hero section. Users can immediately search across all documents, equations, and concepts without navigating away. The search provides:

\- Live result counts as you type

\- Type-ahead dropdown with categorized results (Documents, Equations, Concepts)

\- Popular search chips for common queries (Manning roughness, Green-Ampt infiltration, etc.)

\- Direct navigation to the full Search and Index page for advanced filtering

> **\### 2. Browse by Era**

Documents are organized into 8 historical eras of SWMM development:

\- SWMM I (1969-1971) — 5 documents — The original EPA stormwater model

\- SWMM II (1975) — 3 documents — Extended simulation capabilities

\- SWMM III (1981-1983) — 5 documents — EXTRAN dynamic wave routing added

\- SWMM IV (1988-2004) — 44 documents — Consolidated Fortran codebase

\- SWMM 5 (2004-Present) — 5 documents — Modern C/C++ rewrite with GUI

\- SWMM5+ (2020-Present) — 1 document — Community extensions and LID

\- Commercial (1990s-Present) — 62 documents — InfoSewer, InfoSWMM, and related tools

\- Reference (Various) — 38 documents — Cross-era reference materials

![](https://media.licdn.com/dms/image/v2/D4E12AQEVOlKY--GtMA/article-inline_image-shrink_1500_2232/B4EZyBNklfHwAU-/0/1771694346076?e=1795651200&v=beta&t=i6ed7VRfzHQOixxoLp375I_8H6vuVN8f4yaWAwBb1NM)

Each era page displays:

\- Era summary and historical context

\- Color-coded document listings with type indicators (PDF, Markdown, Word)

\- Key innovations introduced in that era

\- INP file format reference for that version

> **\### 3. Full-Text Search and Index**

The dedicated Search page provides comprehensive search across the entire archive:

\- Unified search across documents, equations, concepts, and textbook chapters

\- Category tabs to filter by content type

\- Era filtering to narrow results to specific SWMM versions

\- Sort options (relevance, name, year, era)

\- CSV export of search results

\- Featured Search of the Day with curated engineering topics

\- Search syntax help for advanced queries

\- Browsable Table of Contents organized by era

> **\### 4. Document Archive (163 Documents)**

The Docs page provides a comprehensive file browser with:

\- 14 document categories: User Manuals, Technical References, Fortran Source Code, Markdown Conversions, Theory and Background, Example Files, Release Notes, and more

\- Multiple view modes: Card view and list view

\- Filtering by category, era, and file type (PDF, MD, DOC, etc.)

\- Contributor tracking for WCH 2004 Fortran source code files

\- Direct links to source documents on GitHub

Document Sources:

\- SWMMEnablement/SWMM_MD_Documents — Markdown conversions of legacy documentation

[https://github.com/SWMMEnablement/SWMM_MD_Documents](https://github.com/SWMMEnablement/SWMM_MD_Documents)

\- SWMMEnablement/WCH_2004_SWMM44H — SWMM 4.4H Fortran source code from the University of Florida Water Resources collection

[https://github.com/SWMMEnablement/WCH_2004_SWMM44H](https://github.com/SWMMEnablement/WCH_2004_SWMM44H)

> **\### 5. Equation Gallery**

The Equations page presents 15 key hydraulic and hydrologic equations used across SWMM versions:

\- LaTeX rendering via KaTeX for mathematical notation

\- Variable definitions for each equation

\- Category grouping: Hydraulics, Hydrology, Water Quality

\- Source document tracking — which SWMM version introduced each equation

\- Search and filter within equations

Example equations include:

\- Manning's equation for open-channel flow

\- Green-Ampt infiltration model

\- Saint-Venant equations for unsteady flow

\- Horton's infiltration equation

\- Dynamic wave routing equations

![](https://media.licdn.com/dms/image/v2/D4E12AQHP6dlgLqgPeA/article-inline_image-shrink_1500_2232/B4EZyA23vcH0AU-/0/1771688394712?e=1795651200&v=beta&t=b4mLrvKBDsSo9qWYIRXhWuk7KA656KplJxogUwson10)

> **\### 6. Concepts and Reference**

The Concepts page is a tabbed reference section with five views:

\- Concepts — 12 cross-referenced hydraulic/hydrologic concepts with related eras and documents

\- Era Comparison — Side-by-side comparison of features across SWMM versions

\- Textbook — Living textbook chapters organized by engineering topic

\- Fortran Rosetta — Fortran-to-Python code comparisons with annotations

\- All Files — Complete file listing across all eras

![](https://media.licdn.com/dms/image/v2/D4E12AQG2Co3U-ATpKQ/article-inline_image-shrink_1500_2232/B4EZyA3vlnIEAU-/0/1771688623712?e=1795651200&v=beta&t=Te3OOxWkM7KEOWNJNVbQQdE5hm68rrV-lSSYC4VZDnw)

> **\### 7. AI Chat**

The AI Chat page provides an intelligent assistant powered by OpenAI:

\- Context-aware responses grounded in the 55-year SWMM documentation archive

\- Multi-language support with 15 language options

\- Era scoping — focus questions on specific SWMM versions

\- Cited answers referencing source documents

\- Example questions to help users get started

The chat provides cost-effective, accurate responses about SWMM documentation, equations, history, and technical details.

> **\### 8. Tools and Analysis**

The Tools page consolidates analytical features in a tabbed interface:

\- Timeline — 13 historical events charting SWMM's evolution from 1969 to present

\- Citations — 14 citation links showing how documents reference each other across eras

\- Version Diffs — Side-by-side version comparisons showing what was added, removed, or modified

\- Annotations — Community annotation system for documenting insights on specific documents

\- Bulk Export — Download the complete archive in JSON or JSONL format for RAG pipelines and AI fine-tuning

> **\### 9. About and Team**

The About page provides:

\- Robert Dickinson's profile — developer of SWMM 3, 4, and 5; PM for InfoSewer and InfoSWMM

\- EPA relationship disclaimer — clearly states this is an independent, community-driven project

\- SWMMEnablement project overview — goals, GitHub repositories, and contribution opportunities

\- 55-year SWMM timeline — brief history of the model's evolution

> **\### Technology Stack**

![](https://media.licdn.com/dms/image/v2/D4E12AQFB-_NJWZo3wg/article-inline_image-shrink_1500_2232/B4EZyBO8_JGsAU-/0/1771694707714?e=1795651200&v=beta&t=zrtzhXMRjWUZUCdSwuVQozY7qOO32apIbnUzWUXXbxw)

> **\### Database Schema**

The application uses 12 PostgreSQL tables:

![](https://media.licdn.com/dms/image/v2/D4E12AQHcHI8CyVhsMw/article-inline_image-shrink_1500_2232/B4EZyBlfw4JsAU-/0/1771700617531?e=1795651200&v=beta&t=UT6v6gyb3yPDh-4FxRjevRFAe4-IufiKhDmYvgDoQsU)

> **\### API Endpoints**

![](https://media.licdn.com/dms/image/v2/D4E12AQGLKxU5bAnaYQ/article-inline_image-shrink_1500_2232/B4EZyBl_Q4JsAU-/0/1771700746346?e=1795651200&v=beta&t=OH9VQJbcQIrijJ4bh6qZ2lq17xkUV-cMgEUTY1yzLeo)

> **\### Frontend Pages**

\- / — Overview: Homepage with search hero, stats, quick starts, featured content

\- /search — Search and Index: Full-text search with filters, export, and ToC

\- /eras — Eras and Versions: Browse documents organized by SWMM era

\- /docs — Docs: File browser with 14 categories and contributor tracking

\- /equations — Equations: Equation gallery with LaTeX rendering

\- /concepts — Concepts and Reference: Tabbed reference (Concepts, Era Comparison, Textbook, Rosetta, Files)

\- /chat — AI Chat: AI-powered Q&A with era scoping and multi-language support

\- /tools — Tools and Analysis: Timeline, Citations, Diffs, Annotations, Export

\- /about — About and Team: Project info, team, EPA relationship

---

> **\## Navigation**

The application uses a collapsible sidebar with three navigation groups:

Browse:

\- Overview (/)

![](https://media.licdn.com/dms/image/v2/D4E12AQG0LBmVPL-eOg/article-inline_image-shrink_1500_2232/B4EZyBsavfJsAU-/0/1771702432113?e=1795651200&v=beta&t=s6pH7pB9VuOeQiOSFIeyr57fTqZoc9JjBPoo6J5ZV7I)

\- Search and Index (/search)

![](https://media.licdn.com/dms/image/v2/D4E12AQHogHHpJSiP2A/article-inline_image-shrink_1500_2232/B4EZyBs2DBI4AU-/0/1771702543141?e=1795651200&v=beta&t=eidkBGwy-Ur87HNUT5vEv35I1qZmgkNU80P-9TYegd8)

\- Eras and Versions (/eras)

![](https://media.licdn.com/dms/image/v2/D4E12AQHveTjLTyThUg/article-inline_image-shrink_1500_2232/B4EZyB38.TGkAU-/0/1771705455274?e=1795651200&v=beta&t=c6nE3MCrbEVJDdC98fk8BPrEq_vTsty7auGQT9snOVk)

\- Docs (/docs)

![](https://media.licdn.com/dms/image/v2/D4E12AQGyAVMjKdWceQ/article-inline_image-shrink_1500_2232/B4EZyB4O.0GkAU-/0/1771705529003?e=1795651200&v=beta&t=gRXpwazWffnLX1l77wjmlO0tVvAFuLDcubJ8qmzN4qw)

Explore:

\- Equations (/equations)

![](https://media.licdn.com/dms/image/v2/D4E12AQGDgQX1ZOvYTw/article-inline_image-shrink_1500_2232/B4EZyB4gcpJ8AU-/0/1771705600402?e=1795651200&v=beta&t=nOy4U2DGWgHSz_rhmqzugMe-pFvnZvmykspxohmphKI)

\- Concepts and Reference (/concepts)

![](https://media.licdn.com/dms/image/v2/D4E12AQGjU8B_iUqgXQ/article-inline_image-shrink_1500_2232/B4EZyB44ilJ8AY-/0/1771705699114?e=1795651200&v=beta&t=T2R6isrYz9uTU3XY1c666UBUU00qGsHLLTeS3n-VfqQ)

Tools:

\- AI Chat (/chat)

\- Tools and Analysis (/tools)

![](https://media.licdn.com/dms/image/v2/D4E12AQE_0QYpmOtqyA/article-inline_image-shrink_1500_2232/B4EZyB5h7iJ0AU-/0/1771705868653?e=1795651200&v=beta&t=osVz2wfzv4cf26Rq12OS4K5pvSumG6v1OkZXe7a--V0)

\- About and Team (/about)

Additional features:

\- Global Command Palette (Ctrl+K or /) for quick navigation and search

\- Dark/Light mode toggle with localStorage persistence

\- First-visit onboarding modal with 5-step feature tour

---

> **\## Document Categories**

The 186 documents span 14 categories:

\- User Manuals — Official SWMM user guides and manuals

\- Technical References — Detailed technical documentation

\- Fortran Source — SWMM 4.4H Fortran source code files

\- Markdown Conversions — Legacy documents converted to searchable Markdown

\- Theory and Background — Theoretical foundations of SWMM algorithms

\- Example Files — Sample INP files and model examples

\- Release Notes — Version release notes and changelogs

\- Training Materials — Tutorials and training guides

\- EPA Reports — Official EPA research reports

\- Conference Papers — Published conference proceedings

\- Applications Guides — Practical application guides

\- Utility Documentation — Supporting utility and tool documentation

\- Quality Assurance — QA/QC documentation and testing

\- Historical — Historical documents and correspondence

![](https://media.licdn.com/dms/image/v2/D4E12AQGGZDo8DlMPLQ/article-inline_image-shrink_1500_2232/B4EZyBm3EWGsAU-/0/1771700975026?e=1795651200&v=beta&t=mZuFSAAl55LpdD8Bdfmozczv3VXhdFhrfBCVxKNvZds)

> **\## INP File Format Reference**

The archive includes INP (input) file format documentation for three major SWMM versions:

SWMM 3 (.dat) — Card-image format with EXTRAN block:

&EXTRAN

H1 720 30. 8 1 1

I1 1 1 2 400. 96.0

SWMM 4 (.dat) — Block-oriented with data groups:

&\$EXTRAN

H1 8 360 30 1 1

I1 1 1 2 400. 0.013

SWMM 5 (.inp) — Section-based text format:

\[SUBCATCHMENTS\]

;;Name RainGage Outlet

S1 RG1 J1

---

> **\## Data Export**

The Bulk Export feature provides the complete archive in two machine-readable formats:

\- JSON — Structured with nested eras, documents, equations, concepts, and citations. Best for direct API consumption.

\- JSONL — One JSON object per line, type-tagged by category. Ideal for RAG chunking and LLM fine-tuning pipelines.

---

> **\## Relationship to EPA**

This documentation archive is an independent, community-driven project. It is not officially affiliated with, endorsed by, or maintained by the U.S. Environmental Protection Agency.

The EPA Storm Water Management Model (SWMM) is developed and maintained by EPA's Office of Research and Development. SWMM is free, open-source software used worldwide for planning, analysis, and design of stormwater runoff, combined and sanitary sewers, and other drainage systems.

The goal of this archive is to preserve and make accessible the full history of SWMM documentation — much of which exists only in out-of-print reports, scanned PDFs, and legacy file format

> **\## Contributing**

The project is open source and welcomes contributions:

\- Report errors: [https://github.com/SWMMEnablement/Docs/issues/new?labels=error&template=error_report.md](https://github.com/SWMMEnablement/Docs/issues/new?labels=error&template=error_report.md)

\- Suggest documents: [https://github.com/SWMMEnablement/Docs/issues/new?labels=suggestion](https://github.com/SWMMEnablement/Docs/issues/new?labels=suggestion)

\- Contribute conversions: Help convert legacy PDFs and Word documents to Markdown

\- View source: [https://github.com/SWMMEnablement](https://github.com/SWMMEnablement)

---

> **\## Credits**

\- Robert Dickinson — Project lead, SWMM 3/4/5 developer, InfoSewer/InfoSWMM PM

\- EPA Office of Research and Development — Original SWMM development and maintenance

\- University of Florida Water Resources — WCH 2004 Fortran source code collection

\- SWMMEnablement community — Documentation conversion and archive maintenanc

![](https://media.licdn.com/dms/image/v2/D4E12AQHBHf2UUivJRQ/article-inline_image-shrink_1500_2232/B4EZyBnjOuGsAU-/0/1771701155908?e=1795651200&v=beta&t=evjFGdGtTCwuInxe9TIqu9f4ww8FSC_7Eguxxp6u3mA)

**Built with React, Express, PostgreSQL, and OpenAI. Hosted on Repl**it.

---

*Rub*

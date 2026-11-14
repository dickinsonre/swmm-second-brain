---
title: "Edition 56: The $350,000 Model That Built a Billion-Dollar Ecosystem: 55 Years of EPASWMM"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-56-350000-model-built-billion-dollar-55-years-dickinson-choic
created: "2026-03-02 14:40"
published: "2026-03-02 16:34"
words: 1972
export_sha256: 898efa7e81b53e0ec9a16d7209ca13913a9c6e2df43f0b2485430aefbbd5aed8
---
# Edition 56: The $350,000 Model That Built a Billion-Dollar Ecosystem: 55 Years of EPASWMM

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 56: The \$350,000 Model That Built a Billion-Dollar Ecosystem: 55 Years of EPA SWMM](https://media.licdn.com/mediaD5612AQEwV8AKVm5xNw "Edition 56: The $350,000 Model That Built a Billion-Dollar Ecosystem: 55 Years of EPA SWMM")

### The \$350,000 Model That Built a Billion-Dollar Ecosystem: 55 Years of EPA SWMM

*A history of the world's most important software you've never heard of — and the interactive app that tells it story and mentions many many names. Most people have never heard but if you get this newsletter than you probably have heard about SWMM.*

> ***Introduction***

There is a peculiar thing about infrastructure. The better it works, the more invisible it becomes. You flush a toilet, rain hammers the pavement, a thousand storm drains swallow a thunderstorm whole — and you never once think about the mathematics that made it all possible. You never think about the model.

I'd like to change that, at least for the next few minutes.

> **The Numbers That Should Keep You Up at Night**

Consider: there are roughly **900,000 miles** of public sewers in the United States. Laid end to end, they'd reach the Moon, come back, and make the trip again — with enough left over to wrap around the equator for good measure.

Now consider: almost every major design decision about those sewers — how big to make them, where to put them, what happens when it rains harder than anyone planned for — has been informed by a single software model. One model. Maintained, for most of its life, by a handful of people you could fit around a large restaurant table.

That model is **EPA SWMM** — the Storm Water Management Model. It was born in **1969**, the same year humans first walked on the Moon. NASA's Apollo program cost \$25.4 billion. SWMM's first version cost **\$350,000**.

The return on investment, as they say, has been *adequate*.

> **A Brief History of Water, Computers, and Stubbornness**

### Act I: The FORTRAN Era (1969–1988)

In 1969, America's rivers were catching fire. The Cuyahoga in Cleveland had burned the year before — not for the first time, mind you, but it was the time that made the cover of *TIME*. Congress was drafting what would become the Clean Water Act. And someone at EPA had the foresight to ask: *How do we actually predict where stormwater goes and what it carries with it?*

The answer was **SWMM 1**, built by a three-way partnership: the University of Florida, Camp Dresser & McKee (now CDM Smith), and Metcalf & Eddy. Written in FORTRAN, it linked rainfall to runoff to sewer flow to receiving water quality. Nothing like it had existed before.

Here's a stat worth savoring: SWMM went through **four major FORTRAN versions** over 19 years:

\- **SWMM 1** (1971): 4 program blocks — Runoff, Transport, Storage/Treatment, Receive

\- **SWMM 2** (1975): Added EXTRAN — the first dynamic-wave hydraulics solver for sewers

\- **SWMM 3** (1981): Standardized a codebase that had begun to fragment across agencies

\- **SWMM 4** (1988): Freed the model from mainframes, put it on PCs, added groundwater

Each version was a response to a specific engineering crisis. SWMM 2 arrived because cities needed to model combined sewer overflows and dynamic surcharging — phenomena SWMM 1 simply couldn't handle. SWMM 3 existed because *too many people were using different versions of the same model and getting different answers*. SWMM 4 arrived because the personal computer revolution meant an engineer in Topeka could finally run the same model as an engineer at EPA headquarters — if they could figure out the free-format input files.

A competent engineer, Robert Heinlein once suggested, should be able to set a bone, plan an invasion, and program a computer. The SWMM developers of this era did all three metaphorically — and wrote the user manuals besides. I have the manuals in apps that are linked to the SWMM history app so you can read and compare SWMM1 to SWMM5 if you want.

### Act II: The Sixteen-Year Silence (1988–2004)

And then — nothing.

For **sixteen years**, no major version of SWMM was released. Sixteen years. In software terms, that's not a gap; it's a geological epoch. The World Wide Web was invented during that gap. Google was founded. The entire dot-com bubble inflated and burst. And SWMM sat there, accumulating technical debt in FORTRAN like sediment in a neglected culvert.

What happened? The same thing that happens to every long-lived codebase maintained by a distributed community without governance: **fragmentation**. Multiple agencies maintained incompatible forks. The code became increasingly difficult to extend. EPA lacked dedicated funding for a rewrite.

Let me put this more bluntly: the model that most of America's stormwater infrastructure depended on was slowly becoming unmaintainable, and no one had the budget to fix it.

Until 2001.

### Act III: The Rewrite (2001–2004)

In 2001, EPA and CDM Smith signed a **Cooperative Research and Development Agreement (CRADA)** — a formal mechanism for government-private collaboration. The mission: rewrite SWMM from scratch. Not refactor. Not port. *Rewrite.*

The architect was **Lewis A. Rossman** of EPA's Office of Research and Development — the same Rossman who wrote EPANET, the water distribution model. The CDM Smith CRADA team was led by Ted Burgess and had **Robert E. Dickinson**, who had been maintaining SWMM code since the SWMM 3 era.

Three years later, in October 2004, **SWMM 5.0.001** was released. Written in **C**. New architecture. Windows GUI with a map display. Object-oriented data model. Open-source license.

It was, in every meaningful sense, a new model — but one that carried 35 years of hydrologic and hydraulic knowledge in its DNA.

### Act IV: The Modern Era (2004–Present)

Since 2004, SWMM 5 has evolved through **eight significant releases** in 19 years:

\| Year \| Version \| Landmark \|

\|------\|---------\|----------\|

\| 2004 \| 5.0.001 \| Complete C rewrite, Windows GUI \|

\| 2005 \| 5.0.005 \| First **FEMA-approved** version \|

\| 2010 \| 5.0.019 \| **LID controls** — rain gardens, permeable pavement, rain barrels \|

\| 2014 \| 5.1.001 \| Rooftop disconnection, solver improvements \|

\| 2018 \| 5.1.013 \| Street planter LID, surcharge fixes \|

\| 2022 \| 5.2.0 \| Flexible surcharge, variable-speed pumps (Rossman's final major release) \|

\| 2023 \| 5.2.4 \| Current stable production release \|

\| TBD \| 5+ \| Next-generation community-driven architecture \|

That 2010 release deserves special attention. When the green infrastructure movement demanded modeling tools for sustainable stormwater design, SWMM was ready. The LID controls introduced in 5.0.019 made SWMM *the* go-to tool for engineers designing with nature rather than against it. Every rain garden, bioswale, and permeable parking lot you've walked past was likely sized using SWMM or a commercial tool built on top of it.

> **The Ecosystem: From One Model to a Billion-Dollar Industry**

Here is perhaps the most remarkable statistic on this page: that original \$350,000 investment has spawned a **global ecosystem now valued at over \$1 billion**.

How? SWMM's open-source DNA means it lives inside dozens of commercial products. If you've used InfoSWMM, PCSWMM, XPSWMM, Tuflow, Mike Urban, InfoWorks ICM, or any number of other tools — you've used SWMM's engine, wrapped in proprietary interfaces and extended with additional capabilities. Every commercial license sold, every consulting project that uses these tools, every municipality that models its system — all of it traces back to that FORTRAN code written at the University of Florida more than half a century ago.

The ecosystem looks something like this:

\- **The EPA engine**: Free, open-source, maintained by a small team at EPA ORD

\- **Commercial platforms**: Proprietary GUIs, GIS integration, cloud computing, customer support — built on the engine

\- **Academic research**: Thousands of peer-reviewed papers using or extending SWMM

\- **Global adoption**: Used on every inhabited continent, in regulatory frameworks worldwide

> **The App: Why This Matters Now**

**I, Robert Dickinson** — who has been inside this story since 1980, maintaining code through SWMM 3 and 4, co-authoring the EXTRAN Addendum, chairing the SWMM5+ Technical Advisory Committee, and leading the CRADA that produced SWMM 5 — has built an interactive web application that documents this entire history: The contents are based on Wayne Huber presentations at ICWMM and a lot of AI searching and discussion with me. If you have issues please send me an email - at the bottom of the page.

**\[**[**swmm-history-robertdickinson.replit.app**](http://swmm-history-robertdickinson.replit.app)**\](**[**https://swmm-history-robertdickinson.replit.app)**](https://swmm-history-robertdickinson.replit.app)**)

The app includes:

\- **12 version cards** spanning 57 years (1969–present), each documenting the *why* behind the release — not just the *what*

\- **Key people** for every version, with roles and contributions

\- **Links to original EPA manuals**, source code, and release notes

\- **The commercial and open-source ecosystem** mapped and compared

\- **A glossary and diagram collection** for SWMM's architecture

\- **Cross-references** to the James Modeling Rules for responsible modeling practice

It is, to my knowledge, the most comprehensive single-source history of SWMM ever assembled — and it's assembled by someone who *was there* for most of it.

> **Why You Should Care (Even If You Don't Model Sewers)**

There's a lesson in the SWMM story that transcends stormwater engineering. It's about what happens when a small team of competent, stubborn people build something useful and keep it alive for decades.

**57 years.** Two programming languages. Four universities. One EPA office. A sixteen-year gap that would have killed any lesser project. And the model not only survived — it became the foundation of an entire industry.

Asimov once wrote that the most exciting phrase in science is not "Eureka!" but "That's funny..." The most exciting phrase in infrastructure modeling might be: *"The model converged."* It's less poetic, perhaps. But when a SWMM simulation converges — when the dynamic wave equations balance across 10,000 conduits and 5,000 junctions and 72 hours of rainfall — what you're witnessing is the accumulated wisdom of five decades of hydrology, hydraulics, and numerical methods, all agreeing with each other simultaneously.

That is, in its own quiet way, magnificent.

> **What Comes Next**

The **SWMM 5+** effort, led by NCIMM (National Center for Infrastructure Modeling and Management), aims to build a community-governed, multi-platform, extensible architecture for the next generation. Key figures include**Ben Hodges** (UT Austin), and **A. Charles Rowney** (NCIMM Director of Operations). **Caleb Buahin** (lead developer of the HydroCouple platform), is also an active developer of SWMM5 at the EPA and now as a consultant,

The challenge is the same one that has defined SWMM's entire history: how do you modernize a critical piece of public infrastructure without breaking the trust of the tens of thousands of engineers who depend on it?

If history is any guide, the answer is: carefully, collaboratively, and with a deep respect for what came before.

**Explore the full interactive history:** \[[swmm-history-robertdickinson.replit.app](http://swmm-history-robertdickinson.replit.app)\]([https://swmm-history-robertdickinson.replit.app](https://swmm-history-robertdickinson.replit.app))

*Interested in the SWMM5 manuals?* \[[swmm-manual-search-robertdickinson.replit.app](http://swmm-manual-search-robertdickinson.replit.app)\]([https://swmm-manual-search-robertdickinson.replit.app](https://swmm-manual-search-robertdickinson.replit.app))

*Curious about responsible modeling practices?* \[[rulesforresponsiblemodeling.lovable.app](http://rulesforresponsiblemodeling.lovable.app)\]([https://rulesforresponsiblemodeling.lovable.app](https://rulesforresponsiblemodeling.lovable.app))

*Robert Dickinson has been working with EPA SWMM since 1978. Connect with him on \[LinkedIn\](*[*https://www.linkedin.com/in/robertdickinson*](https://www.linkedin.com/in/robertdickinson)*) or reach him at* *robert.dickinson@gmail.com**.*

**\#SWMM \#Stormwater \#WaterResources \#EPA \#CivilEngineering \#OpenSource \#Infrastructure \#GreenInfrastructure \#Hydrology \#WaterModeling**

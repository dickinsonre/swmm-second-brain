---
title: "Design Storm App for 6 Continents and 66 Patterns"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/design-storm-app-6-continents-66-patterns-robert-dickinson-ushhe
created: "2026-02-24 00:02"
published: "2026-02-25 11:01"
words: 2151
export_sha256: 70727fa7b608d5bab01f4db99381793a9dc702581bd03067cbdf5d30bc84dcc6
---
# Design Storm App for 6 Continents and 66 Patterns

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Design Storm App for 6 Continents and 66 Patterns](https://media.licdn.com/mediaD4E12AQHu6v3WWt9zkA "Design Storm App for 6 Continents and 66 Patterns")

Sixty-six patterns. Nine regions. Thirty countries. Six continents. Eight export formats. Three steps.

Every piece of infrastructure you walk on, drive over, or live inside was designed to handle rain. Somewhere in the process of creating that bridge, that parking lot, that hospital, an engineer had to answer a deceptively simple question.

How much rain should I design for?

The answer to that question is not a single number. It is a shape. A pattern. A story told in time steps across hours, describing not just how much rain falls, but when during the storm it falls hardest. That pattern is called a hyetograph, and it is one of the most important inputs in stormwater engineering.

Getting it wrong means pipes that are too small. Detention ponds that overflow. Roads that flood. Bridges that fail.

I want to explain a tool I built. It is called the World Rainfall Pattern Painter, and it is free, it runs in your browser, it requires no login, and it contains sixty-six rainfall distribution patterns from more than thirty countries. You can find it at [rain-canvas-studio.lovable.app](http://rain-canvas-studio.lovable.app).

> **THE PROBLEM**

When an engineer designs a storm drain, a culvert, a detention basin, or any piece of infrastructure that must handle rainfall, they do not simply look up "how many inches of rain" and plug it into a model. They need a complete time series. A minute-by-minute or fifteen-minute-by-fifteen-minute description of how the storm unfolds.

Consider a simple example. A storm drops five inches of rain over twenty-four hours. That is a fact. But it is not enough information to design anything. Because five inches spread evenly across twenty-four hours is a gentle drizzle. Five inches concentrated into a two-hour burst at hour twelve is a catastrophe. The total is the same. The infrastructure required to handle each scenario is vastly different.

This is why rainfall patterns exist. They describe the temporal distribution of rainfall within a storm. The most common ones in the United States are the SCS types, developed by the Soil Conservation Service, now called the Natural Resources Conservation Service. There are four of them. Type I for coastal California. Type IA for the Pacific Northwest. Type II for most of the country east of the Rocky Mountains. Type III for the Gulf Coast and tropical regions.

These four patterns have served American engineers for nearly forty years. They are published in a document called TR-55, Technical Release 55, from 1986. They are good patterns. They are also, for most of the world, completely irrelevant.

An engineer in Tokyo does not use SCS Type II. An engineer in Riyadh does not use SCS Type III. An engineer in Lagos, in Sao Paulo, in Munich, in Singapore, each works with a different national standard, a different set of assumptions about how storms behave in their climate.

And here is the part that has frustrated me for years. Every one of these engineers needs the same thing. A tool that takes their local rainfall depth, their chosen storm duration, and their required distribution pattern, and produces a clean, properly formatted time series they can feed into their modeling software.

> **HOW THE TOOL WORKS**

The Rainfall Pattern Painter operates on a three-step workflow. I chose three steps because that is the minimum number needed to produce a valid design storm, and adding more would waste the user's time.

**Step One.** You define the storm parameters. Total rainfall depth. Storm duration. Time step. Unit system. These are the raw numbers that describe your design event. If you are designing for a one-hundred-year, twenty-four-hour storm in Houston, your depth might be ten and a half inches. If you are designing for a ten-year, six-hour storm in London, your depth might be forty-two millimeters. The tool accepts both imperial and metric units.

It also gives you immediate feedback. As you adjust the parameters, the tool classifies your storm intensity in real time. Light, moderate, heavy, very heavy, extreme. This is not decoration. It is a sanity check. If you intended to model a routine two-year storm and the tool tells you the intensity is extreme, you have made an error somewhere, and you will catch it before it propagates into your model.

**Step Two**. You select a rainfall distribution pattern. This is where the tool becomes unlike anything else available. Sixty-six patterns are organized into nine regional tabs.

Under the US Agency tab, you find SCS Types I, IA, II, and III. You also find FDOT distributions for each of Florida's five rainfall zones, TxDOT patterns for Texas, NOAA Atlas 14 patterns, the Denver UDFCD distribution, and USACE Standard Project Storm patterns.

Under the UK and ICM tab, you find the Flood Studies Report distributions at fifty percent and seventy-five percent summer and winter, the Flood Estimation Handbook pattern, and the Wallingford distribution.

Under the European tab, you find Euler Type I and Type II, the German DVWK method, the French Montana distribution, the Spanish Temez pattern, the Italian VAPI method, the Netherlands RIONED distribution, and the Scandinavian SVK pattern.

Under the Asian tab, you find the Japanese AMeDAS distribution, the Chinese GB 50014 standard, the Pearl River Delta pattern, the Indian IMD distribution, the Korean MOLIT pattern, Singapore PUB, Malaysia MSMA, Taiwan WRA, and Australia ARR.

Under the GCC tab, you find the Saudi MOMRA distribution, along with patterns for the UAE, Qatar, Oman, Bahrain, and Kuwait. These are arid-climate flash flood patterns, fundamentally different from anything used in temperate or tropical regions.

Under the African tab, you find South Africa SANRAL, Kenya KMD, Nigeria NiMet, and Egypt HCWW.

Under the Latin American tab, you find Brazil ANA, Mexico CONAGUA, Colombia IDEAM, and Chile DGA.

Under the International tab, you find the Alternating Block Method, which works anywhere you have IDF data, the Probable Maximum Precipitation method from HMR 51 and 52, and the Canadian CDA distribution.

Under the Simple tab, you find Uniform, Triangular, Double Triangle, and a fully custom option.

**Step Three.** You review the result and export it. The tool generates a chart showing rainfall intensity on the left axis and cumulative depth on the right axis. Each bar represents one time step of rainfall. The cumulative line shows total depth accumulating over the storm. You can toggle between the two views.

Then you export. And here the tool is deliberately generous with formats.

> **Export Formats SWMM5 but also many others**

CSV for spreadsheet use. SWMM5 dot dat format, which imports directly into EPA SWMM, the most widely used urban drainage model in the world. InfoWorks ICM format, which imports into Innovyze's commercial modeling software. JSON for programmatic use. PNG, SVG, and PDF for chart images. And animated GIF, which produces a progressive animation of the storm building over time, useful for presentations and reports.

Every exported file includes self-documenting headers. The depth, the duration, the pattern name, the peak intensity, the generation timestamp. This means that six months from now, when someone opens that file and asks "what was this?" the file itself contains the answer.

> **THE ADVANCED TOOLS**

Behind the main workflow, the tool contains a set of advanced features that I built for the engineers who need to go deeper.

The Pattern Comparison tool lets you place two or more distributions side by side on the same chart. It calculates R-squared and root mean square error between them. It includes quick presets for common comparisons, such as monsoon belt patterns, Southeast Asian patterns, and GCC flash flood patterns. It has a delta view that shows the mathematical difference between two distributions at every time step.

The China IDF Calculator contains intensity-duration-frequency coefficients for two hundred seventy-nine Chinese cities. It supports bilingual search in English and Chinese characters. You enter a city name, select a return period, and it calculates the design storm using local rainstorm coefficients and produces an Alternating Block hyetograph. A "Send to Generator" button passes the result directly into the main workflow.

The Canada IDF Calculator does the same for twenty-six Canadian cities using published A, B, C, and n coefficients.

The Sensitivity Analysis tool shows how changes in depth, duration, or time step affect the resulting hyetograph. This is useful for understanding which parameters your model is most sensitive to.

The Pattern Derivation Engine allows you to derive a custom distribution from a mathematical equation. If your local authority publishes a rainfall distribution as a formula rather than a table, you can enter that formula and the tool will generate the corresponding hyetograph.

The Historical Storm Matching tool takes observed rainfall data and performs R-squared curve fitting against all sixty-six patterns to find the best-fit synthetic distribution. If you have gauge data from a real storm and need to know which standard pattern it most closely resembles, this tool gives you the answer in seconds.

> **THE REAL DATA HUB**

The Real Data Hub tab accepts uploaded rainfall data files. You can upload NOAA format dat files, CSV files, SWMM inp files, or HEC gage files. The tool parses them locally in your browser. No data is sent to any server. Sample files are provided for testing.

This feature exists because engineers often need to compare their synthetic design storm against observed historical events. You can upload real gauge data, then use the Historical Storm Matching tool to see which of the sixty-six patterns best represents what actually happened.

> **WHO THIS IS FOR**

If you are a stormwater modeler who spends twenty minutes building a rainfall input file every time you set up an EPA SWMM or HEC-HMS model, this tool reduces that to forty-five seconds.

If you are a civil engineer who needs to verify that your design storm matches the distribution required by your local reviewing agency, this tool shows you all the options and lets you compare them.

If you are a municipal reviewer who checks developer submittals for correct storm methodology, this tool is a reference you can use in thirty seconds.

If you are a university student taking your first hydrology course and trying to understand why SCS Type II looks different from Euler Type I, this tool lets you see both on the same chart and understand the difference visually.

If you are an international engineer working on a project in Saudi Arabia and you need a MOMRA-compliant rainfall distribution, this is the first free web tool that offers one.

If you are a climate researcher comparing how different nations approach design storm methodology, this tool lets you place any two of sixty-six patterns side by side and quantify their differences.

> **WHAT COMES NEXT**

The tool works today. You can open it right now, generate a design storm, and export it to your modeling software. But there are improvements coming.

Live IDF data integration, so you can enter a zip code and have the tool automatically retrieve the correct rainfall depth from NOAA Atlas 14 for your chosen return period and duration.

Return period as a primary input, because engineers think in terms of the twenty-five-year storm, not in terms of four-point-two inches.

HEC-HMS export format, because the US Army Corps of Engineers' hydrologic model is as widely used as EPA SWMM and deserves direct support.

Shareable URLs, so you can encode a complete storm configuration into a link and send it to a colleague.

PDF engineering reports, so you can generate a professional three-page document with parameters, chart, data table, and verification checks in one click.

And comprehensive documentation, including pattern-by-pattern reference cards, a decision flowchart for pattern selection, and a regulatory acceptance matrix showing which jurisdictions require which distributions.

> **A FINAL THOUGHT**

There is a particular satisfaction in building a tool that does one thing well and makes it available to everyone. The rainfall engineering problem is universal. Every country that builds infrastructure must account for storms. The methods exist. The science is published. What was missing was a place where all of it came together in a form that respects the engineer's time and workflow.

Sixty-six patterns. Nine regions. Thirty countries. Eight export formats. Three steps.

> **App Link**

[https://rain-canvas-studio.lovable.app/](https://rain-canvas-studio.lovable.app/)

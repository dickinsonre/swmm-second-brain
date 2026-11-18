---
name: ICM Link Results SQL
file: icm-link-results-sql.html
version: "1.0"
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed (an older site, icm-sql-cookbook, may be its first version), artifact: "https://claude.ai/artifact/UKwRW35Hn1SBZMh4RpXehf", repo: none named in the page}
engines: none (a field catalog, a query writer and a synthetic sample run in JavaScript; no ICM or SWMM engine)
units: US customary (cfs, ft, ft/s)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/UKwRW35Hn1SBZMh4RpXehf, version 1793652990-4020 (index.html, 116,945 bytes, SHA-256 2dbd8dc92f3e9b2cec43042fe2989a66d80050d78d433d3d91b7e232d897034a), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# ICM Link Results SQL: the link-result fields of InfoWorks ICM SQL, and a writer for the aggregate query

## In three points
- **What:** The 2026 edition, as an app, of Bob's short article listing the link variables of InfoWorks ICM SQL: the tsr. time-series fields for InfoWorks and SWMM networks, a builder that writes the aggregate query, and a synthetic sample run.
- **So what:** SQL sees only the saved timesteps, so MAX misses a peak that fell between saves and SUM of a flow is still in cfs until multiplied by the save interval; given the published query's eight fields, the builder reproduces its 40 aggregate columns word for word, and 33 mechanical checks pass.
- **Now what:** Use it to write link-result queries and to know which network you are in (tsr.us_flow on InfoWorks, tsr.flow on SWMM). No ICM run was made for this build, and the help-listed field spellings and SWMM-network queries are untested in ICM.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-11-02"). The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

A field guide and query writer for link results in InfoWorks ICM SQL. Tabs: Variables (the time-series fields, which network each belongs to, and whether its name comes from a working query or from the help), SQL Builder (writes the aggregate query in the style of the published one), Sample Run, About, Doc. What changed for 2026, as the page lists it: the fields are named as time-series results read with tsr. from a run dragged onto the GeoPlan; the SWMM network gets its own field list, one value per conduit rather than two ends; every field says where its name comes from.

## How it computes (as the page states it)

- An aggregate does one piece of arithmetic over the N saved values of one field for one link: MAX, MIN, AVG = sum / N, SUM, COUNT. A blank step is skipped by all five.
- SUM(tsr.us_flow) is a sum of flow rates, so its units are still cfs; multiply by the saved interval in seconds for a volume. In the sample run, 49,496 ft3 pass the upstream end of C1 in six hours.
- The InfoWorks engine reports a link at both ends (us_flow and ds_flow, us_depth and ds_depth); the SWMM network follows SWMM5 and reports one value per conduit.
- Sample run: a teaching model, Manning normal depth at each end and a linear-reservoir lag in each pipe, a step every 10 seconds, saves every 5 minutes. The SWMM-network view averages the two ends of each pipe, to illustrate the dialect only.

## Checks (as stated on the page)

33 mechanical tests, all passing, run in Node:
- Full-bore Manning flow for each sample pipe matches the closed form (1.486/n)(pi D^2/4)(D/4)^(2/3)S^(1/2) to twelve significant figures; C1 carries 20.23 cfs full.
- A scan of 10,000 depths finds the largest open-channel flow in a circular pipe at y/D = 0.9382, 1.0757 times the full-bore flow.
- Normal depth inverts Manning to better than one part in a billion at 18 test flows across the three pipes.
- Given the eight fields of the published InfoWorks query, the SQL Builder reproduces its 40 aggregate columns word for word, ignoring whitespace, and adds GROUP BY oid.
- At the default settings no pipe surcharges, so every sample depth lies inside the range the model is good for.

Field names: 8 from the published InfoWorks query; the rest from the Link Results Data Fields pages of the Autodesk InfoWorks ICM 2027 help, read 2026-11-02. The help gives attribute names such as VELOCITY or HGL; the lower-case tsr. spelling is the app's reading.

## What this does not show

- No ICM run was made for this build; the help-listed tsr spellings, the SWMM-network queries and the HAVING filter are untested in ICM.
- The sample model has no backwater, surcharge head or dynamic wave; it is not InfoWorks and not SWMM5.

## How to reproduce

Open the page; pick fields on Variables, build the query on SQL Builder and paste it into ICM's SQL dialog; Sample Run shows what the aggregates return on the synthetic run.

## Credits and licenses

Robert (Bob) Dickinson, SWMM Enablement; the published link-results query from his ICM SQL series; Autodesk InfoWorks ICM 2027 help. No license is stated for the page.

## AI use

The page says it was built with Claude in a claude.ai session on 2 November 2026 under Bob's direction; he supplied the published query and the outline of his ICM SQL series and asked for the 2026 update, the Doc tab and the Word file. Claude wrote the sample hydraulics, the SQL Builder and the interface, assembled the field catalog and drafted the essay and its seven figures. No person has yet run the help-listed fields or the SWMM-network queries in ICM. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-11-02): first 2026 edition, from the article "These are the SQL link variables for an ICM InfoWorks network".

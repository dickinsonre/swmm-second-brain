---
name: Pengu Climate Watch
file: pengu-cllimate-watch.html
version: "1.1"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://pengu-cllimate-watch.netlify.app", artifact: "https://claude.ai/artifact/F3gS5aqDFjLA4fbxafNcLv", original: "Lovable project pengu-climate-watch (repository name pudgy-water-flow)", repo: none named in the page}
engines: none (a teaching chain from air temperature to ice loss, run in the page; live weather from Open-Meteo)
units: US customary by default with an SI switch (°F, US tons; the page's science figures are in °C, Gt and mm, given here with our US conversions)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says this edition was produced with Claude on 25 October 2026 at Robert Dickinson's request, from his Lovable app. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/F3gS5aqDFjLA4fbxafNcLv, version 1792959766-8223 (index.html, 491,290 bytes, SHA-256 91f57f55f4974f598b00087eae2a2609f42ad8be0f0ada4fa418dc15d742aff0), every tab read in headless Chromium on 2026-11-18, with d3 7.9.0 supplied from a local copy because cdnjs was not reachable from the reading machine. Nothing was run to write this file."
---

# Pengu Climate Watch: Antarctic ice, weather and penguin habitat, with the ice treated as a reservoir

## In three points
- **What:** Bob's Lovable app (four React pages: live Antarctic weather at five stations, a glacier globe, ice-loss charts and a water-cycle lesson with a cartoon penguin) rebuilt as one HTML file and fact-checked. It treats the ice sheet as a reservoir and a glacier's flux gate like a culvert, and lets you push the climate a few degrees to see what moves.
- **So what:** The headline numbers come from primary sources: about 135 Gt (about 149 billion US tons) of ice lost a year from 2002 to 2025 by GRACE and GRACE-FO, and IMBIE's 2026 assessment of 4,780 Gt lost from 1979 to 2023, 13.3 mm (0.52 in, our conversion) of sea level. The Fixes tab lists, each with the code as it was, 23 code defects and 26 numbers that did not match their sources in the Lovable project, and 30 defects found in the port itself and fixed in 1.1; the weather requests fell from about 27 on page load to five.
- **Now what:** Read the simulator as a teaching chain, not a forecast. Its ice response is blind below -2 °C (28 °F, ours), most of Antarctica most of the year, and real Antarctic loss is driven by ocean heat at the grounding line, which an air-temperature toy cannot see.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own (Edition 1.1, added later on 25 October 2026). The file name above, including the site's spelling, is the Netlify site's. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: 01 Current Conditions, 02 Explore the Ice, 03 See the Impact, 04 Understand the Science, Fixes, About, Doc. A header ticker reads LIVE when Open-Meteo answered and NORMAL when it shows the month's climate normal. One fetch feeds the anomalies, alerts, charts and exports (IMBIE, AR6, discharge, census, CSV and JSON); a failed fetch is labelled, not hidden; refresh every fifteen minutes. The simulator picks a station or glacier, a year and a warming, with the arithmetic shown under "The equations behind these cards".

## Model (as the page states it)

- Ice response: melt factor f = 1.15^(T + 2) above -2 °C, else 1.
- The simulator scales the net loss by f. The Doc's "A second look" notes that a strict mass balance with snowfall held fixed would grow the net by D(f - 1), not N(f - 1): for the whole sheet at the slider's far end, about 84 mm (3.3 in, ours) against about a metre (3.3 ft, ours) by 2100. The app keeps the gentler choice because warmer air also brings more snow, and says so.

## Checks (as stated on the page)

- Arithmetic checked by running the model functions in Node; the page checked in a headless browser.
- A web fact-check of the numbers by a research sub-agent, with the key figures re-read from their primary pages.
- For 1.1, Claude audited its own port and a second Claude agent reviewed the 1.0 page cold in a headless browser (phone screen, slow network, impatient mouse), without seeing Claude's list; together they found the 30 port defects. Five parts of the Lovable app could not or should not be carried over, and are listed.

## What this does not show

As the page lists it: air temperature does not melt most Antarctic ice, warm ocean water does, so the ice numbers are a direction, not a size; the horizon warmings and habitat tolerances are assumptions from the original app; Open-Meteo is model output for a point, not the station's instrument; the ten colony counts on the map came from the Lovable build and are unchecked, at least one looks ten times too low; flux-gate widths are approximate and the Lambert speed and width rest on Wikipedia.

## How to reproduce

Start on Current Conditions; in the simulator pick a station or glacier, a year and drag the warming slider; open "The equations behind these cards".

## Credits and licenses

NASA GRACE and GRACE-FO; IMBIE; IPCC AR6; Open-Meteo; Natural Earth coastlines; d3 7.9.0 and html2canvas 1.4.1 from cdnjs. The original app is Bob's Lovable build. No license is stated for the page.

## AI use

The page says: this edition and its essay were produced with Claude, Anthropic's AI model, on 25 October 2026 at Bob Dickinson's request; he wrote the original Lovable app and is responsible for the work. Claude read the Lovable source (about 11,000 lines of React and TypeScript), listed its defects with the offending lines, rewrote the app as one HTML file in vanilla JavaScript, drew the hero scene, logo and penguin, built the offline globe and polar map from Natural Earth coastlines, ran a web fact-check with a research sub-agent and replaced unsupported values with sourced ones, and wrote the Doc essay, the About page and the .docx. No person has yet checked the items under What this does not show. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.1 (2026-10-25): fixes from the second, stranger's-eye pass ("A second look"); the version read.
- First edition (2026-10-25): the Lovable app rewritten as one HTML file.

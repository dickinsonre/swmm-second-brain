---
name: CADCraft Round-Trip Explorer
file: cadcraft-round-trip-explorer.html
version: "1.1"
date: 2026-10-19
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://cadcraft-round-trip-explorer.netlify.app", artifact: "https://claude.ai/artifact/2GBHe4SenVyAsrpBWTL4ZF", tested_repo: "https://github.com/storytold/cadcraft"}
engines:
  - {name: CADCraft, version: "0.6.2 at commit e707ab4 (2026-10-13)", note: "the open-source AutoCAD clone under test; built and run outside the page"}
  - {name: ezdxf, version: 1.4.4, note: "the independent judge, run on 2026-10-14"}
units: drawing units (no water quantities)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/2GBHe4SenVyAsrpBWTL4ZF, version 1792368979-d84e (index.html, 230,709 bytes, SHA-256 c5867526a871d9b0f15ef92167172a758a9b34eaddcbcb817e7600e3fc4b9aa6), its Summary, Verify and Doc tabs read in headless Chromium on 2026-11-18. The date above is the artifact's last publish. Nothing was run to write this file."
---

# CADCraft Round-Trip Explorer: what survives a DXF open-and-save in an open-source AutoCAD clone

## In three points
- **What:** A test of CADCraft, an open-source AutoCAD clone, as a home for engineering drawings: 112 third-party DXF files (from the GDAL, dxf-parser and ezdxf test suites, 17 deliberately broken) opened and re-saved, then judged entity by entity by ezdxf, an independent reader. Tabs show the verdict, a Tilt Lab, a pre-check for your own DXF, the defect register and the corpus.
- **So what:** CADCraft re-saved 108 of 112 files without a crash, ezdxf read all 108 in strict mode, and on 66 complete drawings 99.6% of entities came back exactly or in an equivalent form. The one serious defect (CC-1): a 2D entity drawn in a tilted coordinate system is saved at the wrong place or plane with no warning; in a georeferenced drawing, polylines tilted about 2 degrees moved 2.4 to 4.9 million units.
- **Now what:** Pre-check a DXF before trusting a CADCraft round trip, especially one with tilted (OCS) entities. No AutoCAD was in the loop, and no person has confirmed the defects in AutoCAD.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.1 · cadcraft e707ab4"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## Results the page reports

- 0 panics or hangs in 112 files; 108 of 108 outputs read by ezdxf in strict mode with 0 audit errors; same input twice gives byte-identical output, 108 of 108; no layers, linetypes, text styles, dimension styles or named blocks lost; mirrored (0,0,-1) entities 25 of 25 back in place.
- Of 21,091 scored entities in complete drawings: 99.19% identical, 0.44% rewritten with the same extents, 0.37% (77) not reproduced. Lost most: POLYLINE 31 of 64, SPLINE 6 of 20, LWPOLYLINE 9 of 294, HATCH 7 of 108. Lost none: LINE (19,457), DIMENSION (300) and others.
- Where the 77 went: 70 in 8 files drawn in a tilted coordinate system (CC-1); multileader leaders folded together, 2 (CC-5); a leader moved to Z = 0, 1 (CC-6); a hatch spline edge tessellated, 1 (CC-7); a polyface mesh written as 6 3D faces, 1 (documented); 2 judge artifacts, identical by hand. Eight defects in all.

## Checks (as stated on the page)

- Null control: ezdxf's own read-and-save, judged by the same comparator, gave 0 differences in 65 of 67 complete drawings; the other 2 trace to ezdxf's writer.
- Independent re-check: a separate agent with its own raw DXF parser, never shown the judge, confirmed CC-1, CC-2, CC-3, determinism and all five code citations.
- The page's OCS math against ezdxf's on every tilted entity: largest relative difference 4.1 x 10^-16 over 66 entities.
- The page's model of CADCraft against its real output: 76 of 78 exact (both misses are hatches with spline edges).

## What this does not show

As the page lists it: no AutoCAD in the loop (ezdxf accepting a file is necessary, not sufficient); no DWG; test files, not production drawings (the largest is 2.7 MB); open and save only, no editing, purging, exploding or plotting; entity data, not pixels (CADCraft does not parse SHX fonts); one commit on one machine.

## How to reproduce

Pre-check a DXF tab: run your own file through the page's model; the corpus tab lists the 112 files and their sources.

## Credits and licenses

CADCraft (github.com/storytold/cadcraft); ezdxf 1.4.4; test files from GDAL, dxf-parser and ezdxf. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who asked for the test and the page. Claude built CADCraft, assembled the corpus, wrote the judge, ran the sweep, wrote the defect register and all of the page's code and text, including the Doc essay. A second AI agent, not a person, re-checked the defects. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.1: the version read.

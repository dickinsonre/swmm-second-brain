---
name: SWMM Enablement Bookend Recorder
file: swmm-bookend-recorder.html
version: 1.1.0
date: 2026-10-27
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://swmm-bookend-recorder.netlify.app", artifact: "https://claude.ai/artifact/1y1Hy7jtVYzC7cAH3ehCxy", repo: none named in the page}
engines: none (a browser screen and camera recorder)
units: none (seconds, frames, megabytes)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a claude.ai session on 27 October 2026 at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/1y1Hy7jtVYzC7cAH3ehCxy, version 1793124803-dad6 (index.html, 313,935 bytes, SHA-256 bcf7150e818b2e8d2715c238b4a887bc1b009d1009cde6c459f32572816788ba), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM Enablement Bookend Recorder: a screen recorder that signs the work instead of starring in it

## In three points
- **What:** A browser screen recorder for app videos and GIFs: the maker's face full size for a few seconds at the start and the end, tiny, hidden or out of the way in between, and GIFs cut from a screen-only track so they never carry a face. Version 1.1.0 adds Narrate (talk over an existing Snagit or Camtasia MP4), typed comments pinned to moments, a resizable face and backdrops.
- **So what:** It answers "show you are human" on social media without making the face the subject. A test that decodes the finished MP4 and counts the stand-in face's pixels agrees with the compositor's own log (median ratio 0.964 at full frame, 0.89 for the tiny box), so the layout rule does what it says. It is not cryptographic proof: it signs no Content Credentials and cannot tell a real face from a fake camera.
- **Now what:** Record live from the standalone file (or the Netlify copy) in Chrome or Edge; inside Claude's viewer, camera and screen are blocked, so only Rehearse, From files and the GIF cutter work. No real face, webcam or desktop has been through it in testing.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own (1.1.0, 2026-10-27). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Record, GIF, About, Doc. Live recording with bookends, a rehearsal source, composing from files, a face-free GIF cutter, floating controls (Document Picture-in-Picture), and Narrate with pause-to-talk and automatic sign-off. Backdrops (blur, slate, blueprint, graph paper, colour, your own picture) use a person-outline model loaded once from cdn.jsdelivr.net. Everything stays in the browser; video goes to disk only on Save. The page follows Bore Shell 1.0 written to the spec, since the kit's stylesheet was not available.

## Checks (as stated on the page)

- In headless Chromium with fake camera, microphone and screen and a scripted user: the Doc reports 23 of 23 checks passed; the About tab says Claude wrote 40 automated checks. The page does not reconcile the two counts.
- A rehearsal take of about 11 s of work: 13.71 s take, file plays 13.69 s, 1.28 MB video/mp4; 30.3 fps, 416 frames, 0 dropped.
- Face pixels in the file against the log: 0.964 at full frame (14 samples) and 0.89 for the tiny box (30 samples); a take composed from two files gave 0.964 and 0.94. The page explains the shortfall from one: the ring, name plate and lettering are not counted.

## What this does not show

As the page lists it: no cryptographic proof of humanity and no C2PA Content Credentials; a deepfake fed in as a webcam is a webcam to the browser; no real face, webcam or desktop tested, and Safari, Firefox and Edge not run; floating controls not exercised; recording with the page hidden and long-take sound sync not measured; the GIF change threshold is a judgment tuned on a synthetic screen; no real Snagit or Camtasia file has been through Narrate (project files such as .trec, .tscproj and .snagx will not open).

## How to reproduce

Open the standalone file in Chrome or Edge over https or from disk; Rehearse runs without a camera.

## Credits and licenses

gifenc 1.0.3 (MIT), embedded unmodified; MediaPipe Selfie Segmentation (Apache License 2.0), loaded for backdrops. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a claude.ai session on 27 October 2026 at the request of Robert (Bob) Dickinson, who chose the problem (proof of presence without too much face), named the app and asked for Narrate, comments, a resizable face and backgrounds. Claude wrote all of the code, the automated checks, the essay and its nine figures, and the Word version. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.1.0 (2026-10-27): renamed SWMM Enablement Bookend Recorder; Narrate, typed comments, resizable and movable face (circle by default), backdrops. The version read.
- 1.0.0 (2026-10-27): live recording with bookends, rehearsal, compose from files, face-free GIF cutter, floating controls, Doc tab and Word file.

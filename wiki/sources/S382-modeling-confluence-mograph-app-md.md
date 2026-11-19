---
title: "S382: Modeling Confluence Mograph, app .md (v1.0)"
type: source
raw: raw/apps/modeling-confluence-mograph-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-18
ingested: 2026-11-19
tags: [apps, films, ewri, conference]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app Modeling Confluence Mograph, version 1.0: a 44-second film of the call for abstracts for the EWRI Modeling Confluence Conference 2027. Raw file: [raw/apps/modeling-confluence-mograph-v1.0.md](../../raw/apps/modeling-confluence-mograph-v1.0.md).

**How it was written.** The app ships this file. Its AI-use section says the film, the page, the technical summary and the essay "were made with Claude, Anthropic's AI model, in one session on November 18, 2026, at the request and under the direction of Robert (Bob) Dickinson." Claude read the conference pages through a web reader, noticed that the deadline in the post could not be right and reported it, wrote the code and the text, and rendered the MP4. No person has checked the facts file against the conference pages or watched the whole film. The file opens with In one sentence and In one paragraph, not In three points.

**Claims worth keeping** (all copied from the file)
- A 44-second, six-scene motion graphic (30 fps, 1,320 frames, 1920 by 1080, silent) of the call for abstracts for the EWRI Modeling Confluence Conference, August 8 to 11, 2027, at ASCE World Headquarters, Reston, Virginia.
- Key dates, read from the conference's pages on November 18, 2026: abstracts due December 9, 2026 (11:59 pm EST); speaker notifications mid-January 2027; optional paper deadline February 17, 2027; speaker registration March 3, 2027.
- The post that prompted the film gave the deadline as December 9, 2027. The conference site gives December 9, 2026, and the film uses the site's date. December 9, 2027 is 120 days after the conference closes.
- Four tracks: Collection Systems; Cross-Cutting Innovation, Technology, & Practice; Environmental Systems; Water Distribution Systems. An abstract is one paragraph of about 250 words; up to 2 abstracts per presenter; oral presentations only; a full paper is optional (5 to 15 pages).
- One function, `render(t, ctx)`, draws every frame, so the player in the page and the MP4 are the same film. The checker drew all 1,320 frames in two themes: 0 pieces of text outside the safe margin, 99 distinct strings on screen (46 copied whole from the facts file, 40 pieces of its values, 13 the film's own words), lowest contrast 4.58:1. The MP4 is 7,769,590 bytes.

**Limits it states.** Unofficial, and not reviewed or endorsed by ASCE or EWRI. The pages were read through a web reader, not by a person, and the short link in the post could not be opened. Dates can change after November 18, 2026. The streams are a drawing, with no hydraulics.

**Checked at ingest.** The day counts hold (our arithmetic): August 11, 2027 to December 9, 2027 is 120 days; December 9, 2026 to August 8, 2027 is 242 days; 46 + 40 + 13 = 99. Here a primary page (the conference site) and a post disagree, and the source follows the primary page. Netlify: none yet; artifact https://claude.ai/artifact/TWCK37t5UnwWevhs65cyqn.

**Feeds:** [Modeling Confluence Mograph (app)](../entities/modeling-confluence-mograph.md).

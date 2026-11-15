---
title: Speak 100 (app)
type: entity
updated: 2026-11-15
sources: [S88]
tags: [apps, languages, not-swmm]
reviewed: 2026-11-15
---
Bob's English-to-eight-languages speaking trainer in one HTML file. Version 2026.11.13b, 13 November 2026. It is not a SWMM app; it is in this wiki because it is one of his apps and ships a summary on the same form as the others [S88](../sources/S88-speak-100-app-md.md).

**What it does.** It shows an English word or phrase, the same thing in one of eight languages, and a romanization that marks tone (Chinese) or the stressed syllable (the other seven), and speaks it with the device's own text-to-speech voice. Four modes: Browse, Listen, Flashcards and Quiz [S88](../sources/S88-speak-100-app-md.md).

**Contents** [S88](../sources/S88-speak-100-app-md.md)

| Item | Count |
|---|---|
| Languages | 8: Chinese (Mandarin), Russian, Kazakh, Tagalog, Tamil, French, Spanish, German |
| Entries | 287, each in all eight languages |
| Translations | 2,296 |
| Decks | Words 118, Phrases 64, Travel 41, Grandkids 20, Pirate 30, Minecraft 14 |

**How it works.** No server and no network calls. Speech comes from the browser's Web Speech API. Kazakh has no common device voice and falls back to a Russian one; Tagalog falls back to Spanish; a banner says so [S88](../sources/S88-speak-100-app-md.md).

**Checks.** For the 61 entries added in November 2026: Chinese tone lists match the pinyin tone marks in 61 of 61, and Russian syllable counts match in 61 of 61. The page was loaded in headless Chromium in all eight languages with no console errors [S88](../sources/S88-speak-100-app-md.md).

**What no one has checked.** "No native speaker has checked any translation." Kazakh and Tamil are the least certain. Speech output was not tested. Claude wrote the app and every translation in it [S88](../sources/S88-speak-100-app-md.md).

**Stale text in the page.** Its title and one help line still say "100 words + 30 phrases" and "174 concepts"; the summary itself points this out [S88](../sources/S88-speak-100-app-md.md).

**Where it lives.** `speak-chinese-for-bob.netlify.app`, by its front matter [S88](../sources/S88-speak-100-app-md.md).

**In common with the SWMM apps.** It follows the same [App build contract](../concepts/app-build-contract.md): a summary beside the page, mechanical checks listed apart from human review, and a statement of what was not checked.

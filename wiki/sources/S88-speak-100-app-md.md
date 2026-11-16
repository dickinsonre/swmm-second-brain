---
title: "S88: Speak 100, technical summary (app .md, v2026.11.13b)"
type: source
raw: raw/apps/speak-100-chinese.md
kind: app-md
author: Robert Dickinson
published: 2026-11-13
ingested: 2026-11-15
tags: [apps, languages, not-swmm]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary that ships with Speak 100, version 2026.11.13b: an English-to-eight-languages speaking trainer in one HTML file. It has nothing to do with SWMM; it is here because it is one of Bob's apps and ships a summary on the same form. Raw file: [raw/apps/speak-100-chinese.md](../../raw/apps/speak-100-chinese.md).

**How it was written.** "Claude, Anthropic's AI model, wrote this app and every translation in it, in September and November 2026, at Robert Dickinson's direction." Bob chose the languages, decks and phrases. "No native speaker has checked any of the eight languages."

**Claims worth keeping**
- Eight languages: Chinese (Mandarin), Russian, Kazakh, Tagalog, Tamil, French, Spanish, German.
- 287 entries, each in all eight languages: 2,296 translations.
- Six decks: Words 118, Phrases 64, Travel 41, Grandkids 20, Pirate 30, Minecraft 14.
- Four modes: Browse, Listen, Flashcards, Quiz.
- Audio is the device's own text-to-speech voice through the browser's Web Speech API. Kazakh falls back to a Russian voice and Tagalog to a Spanish one, and a banner says so.
- No server and no network calls; state is kept in the browser's `localStorage`.
- Checks on the 61 new entries: the Chinese tone list matches the pinyin tone marks in 61 of 61; Russian syllable counts match in 61 of 61.
- Public address in its front matter: speak-chinese-for-bob.netlify.app.

**Limits it states.** Kazakh and Tamil are the least certain. Speech output was not tested, because headless Chromium has no voices. Gendered forms are the masculine ones. The page title and one help line still say "100 words + 30 phrases" and "174 concepts" while the live count is 287.

**Checked at ingest.** 118 + 64 + 41 + 20 + 30 + 14 = 287, and 287 × 8 = 2,296. 41 + 20 = 61 new entries. The file's remarks on why the Travel and Grandkids decks were made are personal and are not carried into this wiki (page rule 9).

**Feeds:** [Speak 100 (app)](../entities/speak-100.md).

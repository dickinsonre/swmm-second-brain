---
name: Speak 100
file: speak-100-chinese.html
version: 2026.11.13b (travel and grandkids decks)
date: 2026-11-13
author: Robert Dickinson
links: {netlify: "https://speak-chinese-for-bob.netlify.app", artifact: private, repo: none}
engines: none (browser Web Speech API for audio; no server, no network calls)
languages: [Chinese (Mandarin), Russian, Kazakh, Tagalog, Tamil, French, Spanish, German]
ai_use: built and translated with Claude (Anthropic); see AI use
---

# Speak 100: an English-to-eight-languages speaking trainer in one HTML file

## What it does
Shows an English word or phrase, the same thing in one of eight languages, a
romanization that marks tone (Chinese) or the stressed syllable (the other seven),
and speaks it with the device's own text-to-speech voice. Four modes: Browse,
Listen (hands-free drill), Flashcards, Quiz (audio, four choices). The November
2026 build adds a Travel deck written for a three-week trip to Kazakhstan and a
Grandkids deck of things a grandfather says to a child.

## Contents of this build
287 entries, each in all eight languages (2,296 translations).

| Deck | Kind code | Entries | Categories |
|---|---|---|---|
| Words | w | 118 | Greetings, People, Family, Numbers, Time, Food, Places, Verbs, Describing, Questions |
| Phrases | p | 64 | Essentials, Meeting people, Eating out, Getting around, Shopping, Family, Emergencies, Small talk, Hotel, Directions |
| Travel (new) | t | 41 | Airport 6, Taxi & train 6, Money 5, Prices 8, Phone & internet 5, Being a guest 6, Out and about 5 |
| Grandkids (new) | g | 20 | Outside 6, Play 7, Praise & bedtime 7 |
| Pirate | x | 30 | Ship & crew, Treasure, Orders, Captain Devi |
| Minecraft | m | 14 | Blocks & mobs, Steve says |

Prices holds twenty, fifty, two hundred, five hundred, two thousand, five thousand,
ten thousand and twenty thousand. One to ten, hundred and thousand were already in
Words. Tenge banknotes run from 500 to 20,000.

## How it works
- Data: one array `D` of `{c: category, k: kind, e: English, L: {zh:{z,p,t}, ru:{z,p}, kk, tl, ta, fr, es, de}}`.
  `z` is the native spelling, `p` the romanization, `t` (Chinese only) one tone
  number per character, 0 for neutral. A language entry may carry its own `e`
  when the natural phrase differs from the English prompt.
- Audio: `speechSynthesis` with a voice picked per language by BCP-47 code, then by
  voice name. Kazakh has no common device voice and falls back to a Russian voice;
  Tagalog falls back to Spanish. A banner says so when a stand-in voice is used.
- State: language, theme, speech rate, chosen voices and starred items in
  `localStorage`. Nothing leaves the browser.
- Romanization conventions: pinyin with tone marks; CAPS mark the stressed syllable
  elsewhere; Kazakh uses q, gh, zh, ng, ä, ö, ü; Tamil doubles long vowels.

## Inputs and outputs
No input files. "Export CSV" writes the current language's deck.

## Checks (this build, 2026-11-13)
- Chinese: for all 61 new entries the tone list has one entry per character and its
  non-neutral tones equal, in order, the tone marks in the pinyin. 61 of 61 pass.
- Russian: syllables in each respelling equal the vowels in the Cyrillic. 61 of 61 pass.
- No Latin letters inside Chinese, Russian or Kazakh spellings; no em dashes.
- The script parses (`node --check`). The page was loaded in headless Chromium, the
  Travel and Grandkids decks opened in all eight languages, and Browse, Listen, Flashcards and Quiz
  rendered with no console errors at 1,280 px and 400 px wide.
- The rebuilt pre-travel file is 134,342 bytes, the size recorded when the September
  2026 build was made.

## What this does not show
- No native speaker has checked any translation. Kazakh and Tamil are the least
  certain. Kazakh "қайтарымы керек емес" (keep the change) and "сүтпен шай" (tea with
  milk) are understandable but may not be the most common local wording.
- Speech output was not tested: headless Chromium has no voices, and voice quality
  depends on the device.
- Gendered forms are the masculine ones (Russian "я сыт", Spanish "estoy lleno",
  French "fier", Spanish "orgulloso").
- The Grandkids deck uses the informal singular "you" (ты, сен, tu, tú, du); the rest
  of the app uses polite forms. Tamil "சபாஷ்" (well done) and Kazakh "бас киіміңді ки"
  (put your hat on) are the entries I am least sure a family would say that way.
- Chinese "is this seat free?" is the idiomatic "is this seat taken?", so the
  expected answer is reversed.
- Spanish follows Spain ("móvil"); Tagalog mixes in the English loans people use.
- The page title and one help line still say "100 words + 30 phrases" and
  "174 concepts"; the live counts are in the subtitle.

## How to reproduce
Open the file in a browser, tap ✈ Travel or ♥ Grandkids, pick a language. The checks above come
from the build script that generated the deck (tone and syllable validators) and a
Playwright run.

## Credits and licenses
Robert Dickinson chose the languages, decks and phrases. Speech comes from the
browser's Web Speech API and the voices installed on the device.

## AI use
Claude, Anthropic's AI model, wrote this app and every translation in it, in
September and November 2026, at Robert Dickinson's direction. The checks are
mechanical (tone lists against pinyin, syllable counts, a browser load of every
deck). No native speaker has checked any of the eight languages.

## Changes
- 2026.11.13b: Grandkids deck, 20 entries in three categories, informal forms.
- 2026.11.13: Travel deck, 41 entries in seven categories; AI-use note; this file.
- 2026-09: eight languages, Words, Phrases, Pirate (with Captain Devi) and Minecraft decks.

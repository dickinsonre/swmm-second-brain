---
name: City Temperature Explorer
file: temp-monitor-1
version: 1.0.0
date: 2026-03-16
author: Robert Dickinson
links: {replit: https://temp-monitor-1.replit.app, repo: none}
engines: none
stack: Node.js, TypeScript, React, Vite, Express, Tailwind CSS, TanStack Query, Recharts, Open-Meteo Geocoding API, Open-Meteo Archive API; no persistent application database
units: Both, Fahrenheit by default and Celsius selectable
ai_use: Project records do not identify an AI tool used to build the app
---

# City Temperature Explorer: compare monthly city temperatures across decades

## What it does

The app helps people explore city temperatures across decades, compare an urban location with a rural location, and find sample cities that match preferred summer and winter temperatures. It retrieves historical weather data from Open-Meteo and presents monthly summaries as charts, tables, climate labels, and downloadable CSV files. The four tools are Climate Shift, Heat Island, Climate Match, and Explorer (`client/src/App.tsx:15-23`).

## How it computes

1. The server turns a decade into a date range and limits a range that extends beyond the current date (`server/routes.ts:50-71`). It requests daily archive data from Open-Meteo (`server/routes.ts:216-225`).
2. The server groups daily values by calendar month. It averages daily maximum, minimum, mean, and apparent temperatures. It also returns optional average precipitation, sunshine hours, and wind speed fields (`server/routes.ts:74-163`). The response contains one bucket for each month (`server/routes.ts:98-100`, `131-162`).
3. Climate Shift compares the first and last decade's monthly mean temperatures. It reports month-by-month differences and takes an equal-weight mean across months and across selected summer or winter months (`client/src/pages/climate-shift.tsx:137-204`).
4. Heat Island subtracts each rural monthly mean from the urban monthly mean. It then summarizes those monthly differences, including summer and winter averages (`client/src/pages/heat-island.tsx:149-176`).
5. Climate Match compares sample-city summer and winter averages with the user's preferred ranges. An in-range seasonal score is 100; an out-of-range score decreases using an exponential curve. A consistency bonus adds up to 10 points, and the final result is limited to the range from 0 to 100 (`client/src/pages/climate-match.tsx:68-93`, `144-197`).
6. Climate labels are assigned from monthly mean temperature thresholds. The classifier uses temperature rules and does not use precipitation thresholds (`client/src/lib/koppen.ts:10-63`).
7. The client treats server values as Celsius and converts display values with `°F = °C × 9/5 + 32`; Fahrenheit is rounded to a whole degree and Celsius to a tenth of a degree (`client/src/lib/temperature.ts:1-4`, `16-19`).

## Inputs and outputs

- Pages: `/`, `/heat-island`, `/climate-match`, and `/explorer` (`client/src/App.tsx:15-23`).
- `GET /api/cities/search?q=...` validates a search term and queries Open-Meteo's geocoding service. The request asks for up to 10 results (`server/routes.ts:5-7`, `172-202`).
- `GET /api/temperature?latitude=...&longitude=...&decade=...` queries the Open-Meteo Archive API and returns monthly JSON data (`server/routes.ts:204-265`).
- The app reads no user-selected files. The climate tools can download CSV files in the browser (`client/src/lib/temperature.ts:21-29`).
- Theme preference is stored in browser `localStorage` (`client/src/lib/theme-provider.tsx:13-30`). Temperature responses are cached in server memory for 30 minutes (`server/routes.ts:165-166`). The storage module is an empty in-memory implementation; no persistent application data is stored in a database (`server/storage.ts:1-10`).

## Contents

- Four routed app pages (`client/src/App.tsx:15-23`).
- Two server API endpoints (`server/routes.ts:172-265`).
- Seven decade options, from the 1960s through the 2020s (`shared/schema.ts:8`).
- Four selectable temperature measures (`shared/schema.ts:10`).
- Twelve monthly output buckets (`server/routes.ts:98-100`, `131-162`).
- Thirty hardcoded sample-city candidates for Climate Match (`client/src/pages/climate-match.tsx:35-66`).
- Three preset comparisons in Explorer (`client/src/pages/explorer.tsx:39-67`).

## Checks

- `npm run check`: passed on 2026-11-15. TypeScript reported no diagnostics.
- Page load: the four main routes rendered on 2026-11-15. Climate Shift and Heat Island received HTTP 429 rate-limit responses from the data API. Climate Match opened without errors but does not fetch results until its search action. Explorer rendered its chart.
- Human review: none recorded.

## What this does not show

1. The package does not define a test script, so an automated test suite was not checked or run (`package.json:6-12`).
2. City autocomplete, CSV downloads, share-link copying, the Climate Match search action, and mobile layouts were not checked.
3. Live data was not consistently available during the page checks. Open-Meteo returned rate-limit responses, including a concurrent-request limit and a minutely-request limit (application logs from the 2026-11-15 run).
4. Climate Match catches failed city requests and returns `null`, so a failed request can be omitted from the results instead of surfacing as a page error (`client/src/pages/climate-match.tsx:153-186`).
5. When an input measurement array has no values for a month, the monthly averaging helper returns zero. That value may look like a measured zero rather than missing data (`server/routes.ts:136-149`).
6. The package version has no declared release date. The front matter date is the latest source-change date found in the Git log (`git log`).
7. Transitive dependency licenses, external service license terms, and development dependency licenses were not checked.

## How to reproduce

- Development server: `npm run dev` (`package.json:6-8`, `.replit:1-3`).
- TypeScript check: `npm run check` (`package.json:6-11`).
- Production build and start: `npm run build` followed by `npm start` (`package.json:6-10`). The deployment configuration uses the build output and starts `node ./dist/index.cjs` (`.replit:15-18`).
- No automated test command is configured in `package.json`.

## Credits and licenses

- Author: Robert Dickinson. The Git log attributes its latest recorded changes to `robertdickinson`.
- The project declares MIT in `package.json:2-5`. No root license file was found.
- Open-Meteo Geocoding API and Open-Meteo Archive API provide city lookup and historical weather data. The project files do not state their license terms.
- The page loads Inter and JetBrains Mono from Google Fonts (`client/index.html:12-14`). Font license terms were not checked.
- Direct runtime dependencies are listed in `package.json:13-76`; licenses below are grouped by the license field in their installed package metadata. Transitive dependencies are not included.
- MIT: `@hookform/resolvers`, `@jridgewell/trace-mapping`, `@radix-ui/react-accordion`, `@radix-ui/react-alert-dialog`, `@radix-ui/react-aspect-ratio`, `@radix-ui/react-avatar`, `@radix-ui/react-checkbox`, `@radix-ui/react-collapsible`, `@radix-ui/react-context-menu`, `@radix-ui/react-dialog`, `@radix-ui/react-dropdown-menu`, `@radix-ui/react-hover-card`, `@radix-ui/react-label`, `@radix-ui/react-menubar`, `@radix-ui/react-navigation-menu`, `@radix-ui/react-popover`, `@radix-ui/react-progress`, `@radix-ui/react-radio-group`, `@radix-ui/react-scroll-area`, `@radix-ui/react-select`, `@radix-ui/react-separator`, `@radix-ui/react-slider`, `@radix-ui/react-slot`, `@radix-ui/react-switch`, `@radix-ui/react-tabs`, `@radix-ui/react-toast`, `@radix-ui/react-toggle`, `@radix-ui/react-toggle-group`, `@radix-ui/react-tooltip`, `@tanstack/react-query`, `clsx`, `cmdk`, `connect-pg-simple`, `date-fns`, `embla-carousel-react`, `express`, `express-session`, `framer-motion`, `input-otp`, `memorystore`, `next-themes`, `passport`, `pg`, `react`, `react-day-picker`, `react-dom`, `react-hook-form`, `react-icons`, `react-resizable-panels`, `recharts`, `tailwind-merge`, `tailwindcss-animate`, `tw-animate-css`, `vaul`, `ws`, `zod`, and `zod-validation-error`.
- Apache-2.0: `class-variance-authority`, `drizzle-orm`, and `drizzle-zod`.
- ISC: `lucide-react`.
- Unlicense: `wouter`.
- License not stated in installed package metadata: `passport-local`.

## AI use

The inspected project records do not identify an AI tool used to build the app. Git attributes the latest logged changes to Robert Dickinson, but does not document a division of coding work.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

From the Git log, newest first:

- 2026-03-16: Improve error handling for API rate limits and missing data.
- 2026-03-16: Improve climate data tools with new features and bug fixes.
- 2026-03-16: Update handover document with current date and detailed project information.
- 2026-02-22: Create comprehensive handover document for project details.
- 2026-02-11: Published your App.
- 2026-02-11: Add a last updated date and default cities to the heat island explorer.
- 2026-02-11: Published your App.
- 2026-02-11: Saved progress at the end of the loop.
- 2026-02-11: Add CSV export functionality to climate comparison tools.
- 2026-02-11: Saved progress at the end of the loop.

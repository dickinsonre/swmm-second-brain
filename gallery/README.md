# Gallery

Visual experiences in Robert Dickinson's second brain.

## Prismatic Garden

A Three.js botanical kaleidoscope: crystalline flowers and leaves form a changing tunnel around a distant waterfall of light.

- [Gallery entrance](index.html)
- [Prismatic Garden](prismatic-garden.html)
- [Scene source](src/scene.js)

On GitHub, HTML links show the source. Download `prismatic-garden.html` using **Download raw file**, then open it in a browser with WebGL enabled. The completed HTML includes its scripts and styles and works offline. A static web server can also serve this folder directly, starting at `index.html`.

## Rebuild

From this folder:

```sh
npm ci
npm run build
```

The build combines `src/scene.js`, `src/styles.css` and `src/template.html` with the pinned Three.js dependency into `prismatic-garden.html`.

## Credits

Concept and direction: Robert Dickinson. Built with ChatGPT (OpenAI) and Three.js.

This is a work of generative art. Its water and botanical forms are artistic, not a hydraulic or plant-growth simulation.

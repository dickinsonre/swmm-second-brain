// Build the .docx of the reader app's Doc tab from the same source the tab uses.
// Reads build/doc.md (numbers filled in, figures marked [[FIG name]]), build/doc-captions.json and
// build/figs/*.svg, which build_app.py writes. Needs the docx package and rsvg-convert.
//   node tools/build_app_docx.js   ->  build/swmm-second-brain-doc.docx
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const D = require('docx');
const ROOT = path.join(__dirname, '..'), OUT = path.join(ROOT, 'build');
const md = fs.readFileSync(path.join(OUT, 'doc.md'), 'utf8');
const caps = JSON.parse(fs.readFileSync(path.join(OUT, 'doc-captions.json'), 'utf8'));

function png(name) {
  const svg = path.join(OUT, 'figs', name + '.svg'), out = path.join(OUT, 'figs', name + '.png');
  execFileSync('rsvg-convert', ['-w', '1520', '-b', 'white', '-o', out, svg]);
  const m = fs.readFileSync(svg, 'utf8').match(/viewBox="0 0 (\d+) (\d+)"/);
  return { data: fs.readFileSync(out), w: +m[1], h: +m[2] };
}
function runs(text, opts = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new D.TextRun({ text: text.slice(last, m.index), ...opts }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new D.TextRun({ text: t.slice(2, -2), bold: true, ...opts }));
    else if (t.startsWith('`')) out.push(new D.TextRun({ text: t.slice(1, -1), font: 'Consolas', size: 19, ...opts }));
    else out.push(new D.TextRun({ text: t.replace(/^\[([^\]]+)\].*$/, '$1'), ...opts }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new D.TextRun({ text: text.slice(last), ...opts }));
  return out;
}

const children = [];
let numberedLists = 0, inNumbered = false, title = 'Doc';
const lines = md.split('\n');
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (!line.trim()) { inNumbered = false; continue; }
  let m;
  if ((m = line.match(/^# (.*)/))) {
    title = m[1];
    children.push(new D.Paragraph({ heading: D.HeadingLevel.TITLE, children: [new D.TextRun({ text: m[1] })] }));
    children.push(new D.Paragraph({ children: [new D.TextRun({ text: 'The SWMM Second Brain, Doc tab. Robert Dickinson. Written with Claude; see AI use.', italics: true, color: '4B5563', size: 20 })], spacing: { after: 240 } }));
  } else if ((m = line.match(/^## (.*)/))) {
    children.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_1, children: runs(m[1]) }));
  } else if ((m = line.match(/^### (.*)/))) {
    children.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_2, children: runs(m[1]) }));
  } else if ((m = line.match(/^\[\[FIG (\w+)\]\]$/))) {
    const p = png(m[1]), w = 620, h = Math.round(620 * p.h / p.w);
    children.push(new D.Paragraph({ alignment: D.AlignmentType.CENTER, spacing: { before: 120, line: 240, lineRule: D.LineRuleType.AUTO }, keepNext: true, children: [new D.ImageRun({ type: 'png', data: p.data, transformation: { width: w, height: h } })] }));
    children.push(new D.Paragraph({ spacing: { after: 200 }, children: [new D.TextRun({ text: caps[m[1]], italics: true, size: 19, color: '4B5563' })] }));
  } else if ((m = line.match(/^\d+\. (.*)/))) {
    if (!inNumbered) { numberedLists++; inNumbered = true; }
    children.push(new D.Paragraph({ numbering: { reference: 'num' + numberedLists, level: 0 }, children: runs(m[1]) }));
  } else if ((m = line.match(/^- (.*)/))) {
    children.push(new D.Paragraph({ numbering: { reference: 'bullets', level: 0 }, children: runs(m[1]) }));
  } else {
    children.push(new D.Paragraph({ spacing: { after: 140 }, children: runs(line) }));
  }
}
const numbering = { config: [{ reference: 'bullets', levels: [{ level: 0, format: D.LevelFormat.BULLET, text: '•', alignment: D.AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] };
for (let n = 1; n <= numberedLists; n++) numbering.config.push({ reference: 'num' + n, levels: [{ level: 0, format: D.LevelFormat.DECIMAL, text: '%1.', alignment: D.AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } }] });

const doc = new D.Document({
  creator: 'Robert Dickinson', title,
  styles: {
    default: { document: { run: { font: 'Georgia', size: 22 }, paragraph: { spacing: { line: 300, lineRule: D.LineRuleType.AUTO } } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: 'Arial', size: 44, bold: true, color: '1E3A5F' }, paragraph: { spacing: { after: 80 } } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: 'Arial', size: 30, bold: true, color: '1E3A5F' }, paragraph: { spacing: { before: 320, after: 120 }, outlineLevel: 0, keepNext: true, keepLines: true } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: 'Arial', size: 24, bold: true, color: '1E3A5F' }, paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 1, keepNext: true, keepLines: true } },
    ],
  },
  numbering,
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } }, children }],
});
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync(path.join(OUT, 'swmm-second-brain-doc.docx'), b); console.log('wrote build/swmm-second-brain-doc.docx', b.length, 'bytes,', numberedLists, 'numbered lists'); });

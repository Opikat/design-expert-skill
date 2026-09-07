# Diagram Default Style (no brand profile loaded)

The fallback visual language for diagram artifacts (HTML/SVG explainers, doc
diagrams, slide schematics) when NO brand profile is loaded. A loaded profile's
tokens always win — this file exists so that "no profile" never means "improvise".
Adapted from the diagram-design ruleset (cathrynlavery/diagram-design,
`references/style-guide.md`); composition rules (budget, focal, enumerated
spacing) live in SKILL.md → "Diagram composition floor".

## Color tokens

| Role | Light | Dark |
|---|---|---|
| paper | `#f5f5f5` | `#2d3142` |
| paper-2 | `#ececec` | `#393e53` |
| ink | `#2d3142` | `#f5f5f5` |
| muted | `#4f5d75` | `#bfc0c0` |
| soft | `#7a8399` | `#8e98ac` |
| rule | `rgba(45,49,66,.12)` | `rgba(245,245,245,.12)` |
| rule-solid | `#bfc0c0` | `rgba(191,192,192,.25)` |
| accent | `#eb6c36` | `#f08a59` |
| accent-tint | `rgba(235,108,54,.08)` | `rgba(240,138,89,.10)` |
| link | `#2e5aa8` | `#6a95d8` |

Accent usage obeys the composition floor: 1–2 focal elements only — accent on
five nodes erases the signal. Everything else draws from ink/muted/soft/rule.

## Typography roles

| Role | Family | Size / weight |
|---|---|---|
| title | Instrument Serif | 1.75rem / 400 |
| node-name | Geist (fallback: system sans) | 12px / 600 |
| sublabel | Geist Mono (fallback: monospace) | 9px / 400 |
| eyebrow | Geist Mono | 7–8px / 500, letter-spacing .18em |
| arrow-label | Geist Mono | 8px / 400, letter-spacing .06em |
| callout | Instrument Serif italic | 14px / 400 |

Sizes above are at diagram-viewBox scale — scale proportionally with the canvas,
keeping the ratios. Role discipline is hard: serif for titles/callouts only,
sans for human-readable names, mono strictly for technical content (ports, URLs,
codes) — never as a blanket "dev" font.

## Strokes, radii, grid

- Stroke: thin 0.8 / default 1 / strong 1.2 (emphasis by weight, dashed stays
  semantic = dependency).
- Corner radius: 4 / 6 / 8 px. No shadows.
- 4px grid — every coordinate divisible by 4; connectors orthogonal (rounded
  right angles), arrowhead on the end only; edge labels horizontal on a
  paper-filled mask, never rotated along the line.

## Style variants (offer before building)

When creating a diagram with no profile loaded, propose 2–3 fitting options from
this set (default + variants) with a one-line reason each, before drawing. The
human picks; silence defaults to Editorial.

### Editorial (default)
Everything above. For docs, posts, explainers — the neutral choice.

### Sketchy — hand-drawn overlay on Editorial
SVG filter `feTurbulence type="fractalNoise"` (baseFrequency 0.02, numOctaves 2)
+ `feDisplacementMap` (scale 1.5, seed any). Tuning: baseFrequency .01–.04
(waves→jitter), scale 1–6 (4+ turns cartoonish). Hard rules: filter SHAPES only —
text lives in a separate unfiltered sibling group; test on the target background;
avoid on dark grounds (wobble artifacts show). Use for narrative contexts
(essays, posts), "mid-thought"/work-in-progress signaling. NOT for precise
technical specs or dense labeling.

### Terminal — fixed dark skin
Fake terminal window: page `#0a0a0a` (never pure `#000`), container `#141414`
radius 12px + 1px border, titlebar with three 10px dots (one accent, two soft),
prompt line `$ ` in accent + command in muted, title as `# comment` line.
ALL text monospace (no serif/sans here), sizes +1–2px over default (mono reads
smaller). One accent max; secondary emphasis by weight/size, never extra hues;
optional dot-grid `rgba(255,255,255,.06–.08)`. Use for dev-tool/CLI announcements
and dark-feed social cards. NOT for editorial content or brand-matched output.

### Annotation callouts — add-on to any variant
Editorial asides in margins: Instrument Serif italic 14px (never italic sans/
mono), dashed leader `stroke-dasharray 4,3` ending in a 2px landing dot.
Colors: neutral ink/`rgba(45,49,66,.4)`, focal accent/`rgba(235,108,54,.5)`,
muted `#4f5d75`/`rgba(45,49,66,.3)`. Max 2 per diagram, top-right or bottom-left
margins only, never crossing primary elements, never solid-arrow leaders
(reads as flow), never for labeling nodes (label directly instead).

## When a profile IS loaded

Profile tokens replace this palette and type set entirely (e.g. a product DS's
semantic tokens, a personal brand's palette). Only the composition floor and the
role discipline (serif/sans/mono by content type) survive, expressed through the
profile's own faces and colors.

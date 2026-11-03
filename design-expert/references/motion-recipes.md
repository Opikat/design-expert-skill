# Motion Recipes: Text, 3D, Paths and Scroll

Bans in SKILL.md Step 4 win over any value in this file.

Six techniques that [motion-patterns.md](motion-patterns.md) names but does not
build. Build one only for a row the motion map in
[motion-site-pass.md](motion-site-pass.md) has approved. Each recipe gives
when, when not, the ladder, accessibility, performance, support and a skeleton.
Durations and easing come from the profile's tokens; the skeletons fall back to
plain keywords (`var(--ease-out, ease-out)`). UI micro-interactions (press,
hover, popovers, toggles) live in [polish-and-craft.md](polish-and-craft.md),
under the site pass's frequency gate, with hover only inside
`(hover: hover) and (pointer: fine)`.

**Skeleton status:** run in Chromium 151 with motion allowed, with reduced
motion, without script and as a touch phone; end states, geometry and
fallbacks hold (method and results:
[data/measurements/2026-11-02-motion-recipes](../data/measurements/2026-11-02-motion-recipes/README.md)).
Not yet run in Safari or Firefox: test there before you claim cross-browser
behaviour.

Several recipes start "once in view". One observer serves them all; run it
after the recipe scripts:

```js
const inView = new IntersectionObserver((entries, o) => entries.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('is-in'); o.unobserve(e.target) }
}), { threshold: 0.15 })
document.querySelectorAll('[data-inview]').forEach(el => inView.observe(el))
```

## 1. Text reveal: word mask, and other kinetic type

- **When.** A short H1 or H2 (4–12 words) where type is the hero and the line
  is not the LCP element. One per page, or one per 2–3 sections. Split by
  word: a word mask survives resizing without a re-split. Lines only when they
  are marked up by hand; characters only in display text of 1–3 words.
- **Variants.** Blur-in: one element, short. Typewriter or scramble: once, on
  an eyebrow or a caption. Shimmer: one word, or a loading state. A variable
  font axis: one heading or a hover, with widths fixed so nothing reflows.
  Count-up: once, 600–1000 ms, ease-out, and only as the page's one brand
  moment (motion-site-pass.md, Numbers row).
- **When not.** Body text and paragraphs (a paragraph cannot carry an
  `aria-label`); the LCP heading; long headings; text on B2B and finance pages;
  scramble or typewriter on a heading; per-character blur; a shimmer or
  typewriter that loops without a pause.
- **Ladder.** The platform's native text effect when the profile names one;
  otherwise the split below. A paid splitter is never needed.
- **Accessibility.** The heading gets an `aria-label` with the full text; the
  word spans get `aria-hidden`. Under reduced motion the script does not split
  at all. The hidden start state applies only under `(scripting: enabled)` and
  `(prefers-reduced-motion: no-preference)`, with a CSS failsafe that shows the
  text after ~1.5 s if the script never runs. Count-up: the final value is
  static text; the animated copy is `aria-hidden`.
- **Performance.** Transform and opacity only; no per-character blur. Keep a
  split under ~60 spans (a heuristic). A word split needs no font-loading wait;
  a line split must wait for `document.fonts.ready` and re-split on resize.
- **Support.** `overflow: clip` (Safari 16+) and `@media (scripting)` are
  widely available; CSS has no native text splitting yet. Plain-text headings
  only: a heading with links or inline emphasis is not split.

```html
<h2 data-split data-inview>Every invoice finds its way home</h2>
```

```css
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  [data-split]:not(.is-split) { visibility: hidden; animation: split-failsafe 0s 1.5s forwards; }
}
@keyframes split-failsafe { to { visibility: visible; } }
.split-word { display: inline-block; overflow: clip; padding-block-end: .15em; margin-block-end: -.15em; }
.split-word > span { display: inline-block; transform: translateY(110%);
  transition: transform .4s var(--ease-out, ease-out) calc(min(var(--i), 8) * 50ms); }
.is-in .split-word > span { transform: none; }
```

```js
const still = matchMedia('(prefers-reduced-motion: reduce)').matches
const late = performance.now() > 1400 // the failsafe has already shown the text
document.querySelectorAll('h1[data-split], h2[data-split]').forEach(h => {
  if (!still && !late) {
    const words = h.textContent.trim().split(/\s+/)
    h.setAttribute('aria-label', words.join(' '))
    h.replaceChildren(...words.flatMap((word, i) => {
      const mask = document.createElement('span'), inner = document.createElement('span')
      mask.className = 'split-word'; mask.setAttribute('aria-hidden', 'true')
      inner.style.setProperty('--i', i); inner.textContent = word; mask.append(inner)
      return i ? [' ', mask] : [mask]
    }))
  }
  h.classList.add('is-split')
})
```

## 2. 3D card flip

- **When.** Both faces are two states of one object: summary and detail,
  question and answer, product and specs. The user flips it on purpose, and the
  faces are close in height.
- **When not.** Content that needs comparing across faces; long content; every
  card in a grid; hover as the only trigger; flipping by itself. An expand or a
  tap-to-detail usually serves better.
- **Ladder.** The platform's native 3D through variants when the profile names
  one; otherwise a CSS transition on a data attribute plus a few lines of
  script for the button and `inert`. A library spring only when the profile
  asks for one.
- **Accessibility.** A real `<button>` outside both faces whose label names the
  action ("Show back", "Show front"); the hidden face is `inert`. No ARIA state
  fits a flip, and some screen readers may not announce the label change.
  Under reduced motion there is no 3D: the faces swap with the profile's
  replacement (a 150 ms crossfade below).
- **Performance.** A flip composites well. Nothing on `.card` or on any
  element between it and its faces may flatten the 3D: `overflow` other than
  `visible` (Chromium flattens `clip` too, whatever the spec allows),
  `opacity` below 1, `filter`, `clip-path`, `mask`, `mix-blend-mode`,
  `isolation: isolate`, `contain: paint`. A flattened card shows its front
  face mirrored instead of the back. To fade the whole scene, fade a wrapper
  outside the 3D context. Each 3D face is its own GPU layer: check many cards
  on a weak device.
- **Support.** 3D transforms reach ~97% of users; `backface-visibility` is
  widely available (`-webkit-` prefix only for Safari before 15.4); `inert` is
  Baseline since 2023. Known WebKit bug: a 3D-rotated sibling can blur text
  inside a scaled parent.

Without script both faces stay in normal flow, readable, and the button is
hidden; the faces stack and flip only when script runs.

```html
<button type="button" class="flip" aria-controls="card-1">Show back</button>
<div class="scene"><div class="card" id="card-1">
  <div class="face front">Summary</div>
  <div class="face back">Detail</div>
</div></div>
```

```css
@media (scripting: none) { .flip { display: none; } }
@media (scripting: enabled) { .card { display: grid; } .face { grid-area: 1 / 1; } }
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .scene { perspective: 1000px; }
  .card { transform-style: preserve-3d; transition: transform .5s var(--ease-out, ease-out); }
  .face { backface-visibility: hidden; }
  .back, .card[data-flipped] { transform: rotateY(180deg); }
}
@media (scripting: enabled) and (prefers-reduced-motion: reduce) {
  .face { transition: opacity .15s; }
  .back, .card[data-flipped] .front { opacity: 0; }
  .card[data-flipped] .back { opacity: 1; }
}
```

```js
document.querySelectorAll('button.flip').forEach(btn => {
  const card = document.getElementById(btn.getAttribute('aria-controls'))
  const front = card.querySelector('.front'), back = card.querySelector('.back')
  back.inert = true
  btn.addEventListener('click', () => {
    const on = card.toggleAttribute('data-flipped')
    front.inert = on; back.inert = !on
    btn.textContent = on ? 'Show front' : 'Show back'
  })
})
```

## 3. Pointer tilt

- **When.** One decorative hero visual, or a small set of cards on a Persuade
  page, for a fine pointer only.
- **When not.** Text cards; product UI; touch; reduced motion; every card by
  default; an element that already flips.
- **Ladder.** A script writes two custom properties and a CSS transition
  smooths them. A library spring only when the profile names one. A tilt
  library that ignores reduced motion is allowed only behind the same media
  gate.
- **Accessibility.** Motion from interaction falls under WCAG 2.3.3. The whole
  effect sits behind `(hover: hover) and (pointer: fine) and
  (prefers-reduced-motion: no-preference)`; the content works without it, and
  a clickable card keeps its normal focus style.
- **Performance.** Cheap for one element. Listen on the untransformed wrapper
  and tilt its inner layer: a tilted element's edge moves out from under the
  pointer, which fires `pointerleave` and makes the card flicker at its edges.
  Reset on `pointerleave`, or the card freezes mid-tilt. The factor 16 below
  gives ±8° at the edge.

```html
<div class="tilt"><div class="tilt-face">Hero visual</div></div>
```

```css
@media (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference) {
  .tilt { perspective: 800px; }
  .tilt-face { transform: rotateX(var(--rx, 0deg)) rotateY(var(--ry, 0deg));
               transition: transform .4s var(--ease-out, ease-out); }
}
```

```js
const tiltOk = matchMedia('(hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)')
document.querySelectorAll('.tilt').forEach(el => {
  el.addEventListener('pointermove', e => {
    if (!tiltOk.matches) return
    const r = el.getBoundingClientRect()
    const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5
    el.style.setProperty('--rx', `${-y * 16}deg`)
    el.style.setProperty('--ry', `${x * 16}deg`)
  })
  el.addEventListener('pointerleave', () => { el.style.removeProperty('--rx'); el.style.removeProperty('--ry') })
})
```

## 4. 3D scene: ring carousel, scroll tilt-in

- **When.** A small set of neighbours that really sit in space, such as a short
  product ring or a 4–6-face cube that the user turns; or one visual that
  enters with a slight scroll-driven tilt.
- **When not.** Rotation by itself without a pause; full-screen containers;
  body text on rotating faces; scroll rotation over ~15°; reduced motion.
- **Ladder.** CSS only: geometry through `tan()`, rotation through one custom
  property on the container; the scroll tilt-in through `view()` inside
  `@supports` with a static fallback. A library only for drag with inertia.
- **Accessibility.** Real buttons and a visible current item. If it ever moves
  by itself, it needs a pause (WCAG 2.2.2). Under reduced motion it becomes a
  plain row with scroll snapping, and the buttons scroll that row.
- **Geometry.** Ring radius = (face width / 2) / tan(180° / n): for n = 9 and
  210 px faces, ~288 px. `--n` is the number of faces, `--k` each face's index;
  `sibling-index()` and `sibling-count()` can replace both where supported.

```html
<div class="carousel"><div class="ring" id="ring-1" style="--n: 6">
  <article style="--k: 0">1</article><article style="--k: 1">2</article><article style="--k: 2">3</article>
  <article style="--k: 3">4</article><article style="--k: 4">5</article><article style="--k: 5">6</article>
</div></div>
<button type="button" data-ring-step="-1" aria-controls="ring-1">Previous</button>
<button type="button" data-ring-step="1" aria-controls="ring-1">Next</button>
<figure class="tilt-in">Visual entering with a tilt</figure>
```

The base layout is the plain row; the ring is built only when script runs and
motion is allowed. The ring resets `overflow` to `visible` because a scroll
container would flatten it.

```css
.ring { --w: 220px; display: flex; gap: 16px; overflow-x: auto; scroll-snap-type: x mandatory; }
.ring > * { flex: 0 0 var(--w); aspect-ratio: 3 / 4; scroll-snap-align: center; }
@media (scripting: none) { [data-ring-step] { display: none; } }
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .carousel { perspective: 1000px; }
  .ring { --r: calc(var(--w) / 2 / tan(180deg / var(--n))); display: block; position: relative;
    width: var(--w); aspect-ratio: 3 / 4; margin-inline: auto; overflow: visible; transform-style: preserve-3d;
    transform: translateZ(calc(-1 * var(--r))) rotateY(calc(var(--i, 0) * -360deg / var(--n)));
    transition: transform .6s var(--ease-out, ease-out); }
  .ring > * { position: absolute; inset: 0; backface-visibility: hidden;
    transform: rotateY(calc(var(--k) * 360deg / var(--n))) translateZ(var(--r)); }
}
@supports (animation-timeline: view()) { @media (prefers-reduced-motion: no-preference) {
  .tilt-in { animation: tilt-in linear both; animation-timeline: view(); animation-range: entry 0% cover 40%; }
} }
@keyframes tilt-in { from { transform: perspective(1000px) rotateX(12deg); } }
```

```js
document.querySelectorAll('[data-ring-step]').forEach(btn => btn.addEventListener('click', () => {
  const ring = document.getElementById(btn.getAttribute('aria-controls'))
  const n = ring.children.length, i = (+ring.dataset.i || 0) + +btn.dataset.ringStep
  ring.dataset.i = i
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    ring.children[((i % n) + n) % n].scrollIntoView({ block: 'nearest', inline: 'center' })
  } else ring.style.setProperty('--i', i)
}))
```

## 5. Glowing path with a travelling dot

- **When.** The dot says what a still line with arrowheads cannot: the order
  or timing in which things arrive across lanes, data in transit as a step of a
  process (integrations, a pipeline), or progress. Direction alone is an
  arrowhead, a layout fix, not a dot. Whether the brand's language allows it
  is the profile's call.
- **When not.** Decorative lines that mean nothing; endless ambient loops next
  to body text; more than three dots on one screen *(start)*; product UI.
- **Ladder.**
  1. CSS `offset-path: path()` with `@keyframes` on `offset-distance`, the dot
     inside the same `<svg>`: path units are then viewBox units, and the dot
     scales with the drawing.
  2. A comet tail drawn by the stroke (`pathLength="1"`, `stroke-dasharray`,
     `stroke-dashoffset`) when the tail must follow the curve.
  3. A border beam: `offset-path: rect()` or `inset()` with a mask (Safari
     18+), or a conic gradient animated through `@property`.
  4. A responsive HTML dot outside the SVG: `offset-path: shape()` with
     percentages (Chrome 135, Firefox 148, Safari 18.4).
  5. A script (`getPointAtLength`) or a library only when the path rebuilds
     with the layout (`ResizeObserver`) or follows a drag.
- **Several lanes.** One dot per lane, each with its own `path()`; at most
  three, arriving together or in reading order, counted as one row.
- **Accessibility.** One run of about 3.5 s *(start)*, linear, when it enters
  view, or a loop with a visible pause through `animation-play-state` (WCAG
  2.2.2); never past 5 s without that pause. Above the fold, drop
  `data-inview` so the run starts on load without waiting for the script. Under reduced
  motion the dot rests at the end; the track here is static, so it is already
  fully drawn (a drawn-on variant shows its full stroke). A meaningful SVG
  gets `role="img"` and an `aria-label`; a decorative one gets `aria-hidden`.
  If a library drives the dot, test reduced motion yourself: whether a
  library's reduced-motion setting covers path properties is not documented.
- **Performance.** In Chromium `offset-distance` runs on the main thread; one
  small dot is cheap. The glow is a static radial gradient or a pre-blurred
  halo. Never animate `blur()`, `drop-shadow()` or `box-shadow`, and keep
  `filter` off the whole SVG while something inside it moves. For a straight
  track, `translate` is cheaper.
- **Support.** `offset-path` with `path()` and `ray()`: Chrome 64, Firefox 72,
  Safari 16 (older engines would leave the dot at the SVG origin, so the
  skeleton hides it there). Basic shapes and
  coordinate boxes (`rect()`, `inset()`, `circle()`): Chrome 116, Firefox 122,
  Safari 18.
- **Gotchas.** Generate the SVG `d` and the CSS `path()` from one source (a
  template or a build step) so they cannot drift. Gradient ids are
  page-global, so give each SVG its own. On a light background set
  `--glow-core` to the accent: a white core disappears on paper. On an
  existing drawing keep its own track styling; the skeleton's `.track` rule is
  for a new drawing.

```html
<svg class="flow" data-inview viewBox="0 0 400 120" role="img" aria-label="Orders flow from cart to invoice">
  <defs><radialGradient id="flow-glow">
    <stop offset="0" class="glow-core"/><stop offset=".4" class="glow"/><stop offset="1" class="glow" stop-opacity="0"/>
  </radialGradient></defs>
  <path class="track" d="M10 100C120 10 280 10 390 100"/>
  <circle class="dot" r="12" fill="url(#flow-glow)"/>
</svg>
```

```css
.flow { --glow: var(--accent, #3fb6ff); }
.flow .glow-core { stop-color: var(--glow-core, #fff); }
.flow .glow { stop-color: var(--glow); }
.flow .track { fill: none; stroke: var(--glow); stroke-opacity: .35; stroke-width: 2; }
.flow .dot { offset-path: path('M10 100C120 10 280 10 390 100'); offset-rotate: 0deg;
  animation: dot-run 3.5s linear both; }
@media (scripting: enabled) { .flow[data-inview]:not(.is-in) .dot { animation-play-state: paused; } }
@keyframes dot-run { from { offset-distance: 0%; } to { offset-distance: 100%; } }
@media (prefers-reduced-motion: reduce) { .flow .dot { animation: none; offset-distance: 100%; } }
@supports not (offset-path: path('M0 0')) { .flow .dot { display: none; } }
```

## 6. Scroll-linked progress: rail fill and marker

- **When.** Progress through a sequence the reader controls: a process
  timeline, a reading-progress bar, a scrubbed diagram. If scrolling back up
  does not unwind it, it is not progress.
- **When not.** Decorative parallax; scroll hijacking, or pinned sections that
  last longer than a short, earned moment; rotating full-screen containers;
  elements that carry body text.
- **Ladder.** The platform's scroll effect when the profile names one;
  otherwise a CSS view or scroll timeline with linear timing, the
  `animation-timeline` declared after the `animation` shorthand, all inside
  `@supports (animation-timeline: view())`. Older engines get the static end
  state, or the library the profile names. Pin with `position: sticky`, no
  library. One-shot reveals stay on the observer: `animation-trigger` is
  Chromium-only.
- **Accessibility.** Scroll-driven motion falls under WCAG 2.3.3. Under reduced
  motion the rail is drawn and still; parallax is removed.
- **Range.** `entry 50% exit 50%` starts when the sequence's top reaches the
  middle of the viewport and ends when its bottom does, so for a sequence
  taller than the screen the fill edge stays on the viewport's middle line. A
  sequence that ends the page never reaches `exit 50%` and stops part-filled:
  end its range at `contain 100%` instead.
- **Performance.** Animate `scaleY` or `scaleX` for fills and `transform:
  translate` for markers: compositor work, off the main thread in Chromium. A
  marker as tall as its rail, moved by `translateY(-100%)` to `0`, carries a
  dot along the rail without any length in pixels. If the animated element
  sits outside the timeline's subtree, name the timeline and put
  `timeline-scope` on a shared ancestor (`timeline-scope: all` was removed).
- **Support.** `animation-timeline`, `animation-range` and `view-timeline`:
  Chrome 115, Safari 26, Firefox 159; Baseline newly available since 2026-10,
  so keep `@supports` for older versions.

```html
<div class="steps">
  <div class="rail" aria-hidden="true"><div class="rail-fill"></div><div class="rail-marker"></div></div>
  <ol><li>Draft</li><li>Send</li><li>Get paid</li><li>Reconcile</li></ol>
</div>
```

```css
.steps { position: relative; padding-inline-start: 32px; view-timeline: --steps block; }
.rail { position: absolute; inset-block: 0; inset-inline-start: 8px; width: 2px;
  background: color-mix(in srgb, var(--accent, currentColor) 25%, transparent); }
.rail-fill, .rail-marker { position: absolute; inset: 0; }
.rail-fill { background: var(--accent, currentColor); transform-origin: top; }
.rail-marker::after { content: ""; position: absolute; left: 50%; bottom: 0; width: 12px; aspect-ratio: 1;
  translate: -50% 50%; border-radius: 50%; background: radial-gradient(#fff, var(--accent, currentColor) 45%, transparent 70%); }
@supports (animation-timeline: view()) { @media (prefers-reduced-motion: no-preference) {
  .rail-fill { animation: rail-fill linear both; }
  .rail-marker { animation: rail-marker linear both; }
  .rail-fill, .rail-marker { animation-timeline: --steps; animation-range: entry 50% exit 50%; }
} }
@keyframes rail-fill { from { transform: scaleY(0); } }
@keyframes rail-marker { from { transform: translateY(-100%); } }
```

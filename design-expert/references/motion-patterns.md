# Motion Patterns: Element Vocabulary by Job

Motion is a material, not a garnish. Every animated element must answer a
question the reader is actually asking — *where did this come from, what
changed, did my action register, how far along am I, what is alive here*. An
element that answers none of them is decoration, and decoration in motion is
the fastest way to make careful work look cheap.

This file is the **vocabulary**: what kinds of motion element exist, per job.
For timing values, easing curves, and copy-ready CSS, see
[polish-and-craft.md](polish-and-craft.md). For the discipline rules (durations,
`transform`/`opacity` only, ceremony scaled to frequency), see the main skill,
Step 12.

## How to use this file

1. Name the job: *this element announces arrival* / *this shows progress* /
   *this responds to the pointer*.
2. Pick two candidates from that job. One conventional, one with more presence.
3. Reject on failure conditions. A pattern that breaks on touch, on fast
   scroll, or without JS is out unless you design the fallback deliberately.
4. **Write the reduced-motion behaviour before you build the motion.** If you
   cannot describe the static end state, the pattern isn't finished.

## Implementation ladder (climb only as far as needed)

1. **CSS transitions and keyframes** — hover, focus, entrance, state changes.
2. **Native scroll-driven animations** (`animation-timeline: scroll()` /
   `view()`) — scroll-linked effects with no library and no scroll listener.
   Progressive enhancement: unsupported browsers get the static end state.
3. **View Transitions API** — cross-view and element-morph transitions.
4. **A small amount of vanilla JS** — an `IntersectionObserver` for entrances,
   a rAF-throttled scroll read for progress. Roughly 50 lines covers most pages.
5. **An animation library** (Motion, GSAP + ScrollTrigger) — when sequencing,
   orchestration, or timeline control genuinely exceeds the above.
6. **A runtime for authored animation** (Rive for interactive vector with state
   machines; Lottie for exported After Effects) — when the artwork itself is
   animated and a designer authors it, not a developer.
7. **3D / shaders** (Three.js, React Three Fiber) — only when depth or material
   is the point. This tier is where "impressive" most often becomes "generic".

Most of what a marketing page needs lives at tiers 1–4. Reaching tier 5+ for an
entrance fade is a tell.

## Contents
1. Entrance
2. Scroll progress
3. Pointer response
4. State transition
5. Ambient / looping
6. View transition
7. Value change

---

## 1. Entrance — an element announces itself as it arrives

### Fade-and-rise
- **Works when:** used sparingly to mark section boundaries; small offsets
  (8–16px), short durations (200–300ms), ease-out.
- **Fails when:** applied to every element on the page — the reader spends the
  visit watching things assemble.
- **Misuse:** long distances and long durations. A 60px slide over 800ms is a
  page that feels slow to a fast reader.
- **Reduced motion:** rendered in place, no offset, no delay.

### Staggered reveal (siblings enter in sequence)
- **Works when:** the group is a set and the order carries meaning; 50–80ms
  between items, capped at a handful.
- **Fails when:** the list is long — the last item arrives after the reader
  reached it.
- **Reduced motion:** all items present simultaneously.

### Line draw (stroke reveals along its path)
- **Works when:** the brand language is linear — rules, diagrams, technical
  drawing. The line becomes structure that builds itself rather than an effect.
- **Fails when:** the stroke is thin and the path short — nobody sees it.
- **Misuse:** a path that draws to nowhere, or one whose geometry doesn't align
  with the layout it decorates. A drawn line asserts structure; wrong geometry
  asserts wrong structure.
- **Reduced motion:** full stroke visible, no dash offset.

### Text mask reveal (lines or words wipe into view)
- **Works when:** typography is the hero and the headline is short.
- **Fails when:** it delays the one sentence that explains the page.
- **Misuse:** per-character animation on body copy — it makes reading a task.
- **Reduced motion:** text present, no clipping.

### Counter-entry (element arrives from where it will act)
- **Works when:** the origin is meaningful — a panel from the edge it belongs
  to, a toast from the region it reports on.
- **Fails when:** the origin is arbitrary; then it is just a slide.

---

## 2. Scroll progress — the reader's position drives the change

### Scrubbed progress (position maps to a value, reversible)
- **Works when:** something genuinely advances through the section — a path
  completing, a sequence stepping, a figure filling. The scroll *is* the easing;
  don't add a transition on the scrubbed property or it will lag the finger.
- **Fails when:** the section is short — there is no travel to map onto.
- **Misuse:** non-reversible scrubbing. If scrolling back up doesn't unwind it,
  it isn't progress, it's a one-shot trigger with extra machinery.
- **Reduced motion:** final state, no scroll listener at all.

### Sticky stage (an element pins while content advances past it)
- **Works when:** one subject changes across several explanations.
- **Fails when:** the pinned element is taller than the viewport on any device
  you support.
- **Misuse:** pinning long enough that the reader thinks scrolling broke.

### Parallax depth (layers move at different rates)
- **Works when:** subtle — a few percent of difference, on decorative layers
  only.
- **Fails when:** applied to text, or strong enough to induce motion sickness.
- **Reduced motion:** all layers static, no offset.

### Progress indicator (a rail, bar, or index tracking position)
- **Works when:** the page is long and readers need orientation.
- **Fails when:** the page is short enough to see whole.

### Reveal-on-enter, one shot
- **Works when:** the element should feel *placed* rather than tracked, and
  re-animating on every pass would be noise.
- **Fails when:** used for something the reader will scroll past repeatedly.

---

## 3. Pointer response — the interface acknowledges presence

### Hover state change
- **Works when:** every interactive element has one, and it is fast (100–150ms).
- **Fails when:** hover is the *only* way to discover something. Touch has no
  hover; a hover-only reveal is a feature that doesn't exist on phones.

### Magnetic / proximity attraction
- **Works when:** one focal control deserves emphasis — a primary CTA.
- **Fails when:** used on many elements; the page starts twitching.
- **Misuse:** strong displacement that makes the target harder to hit. Motion
  that fights Fitts's law is a bug wearing a flourish.

### Cursor-follow layers
- **Works when:** a large image or scene benefits from a sense of depth.
- **Fails when:** it is the only interesting thing on the page.
- **Reduced motion / touch:** static composition, no pointer listener.

### Preview on hover (the row shows its image)
- **Works when:** paired with a list-with-preview section pattern.
- **Fails when:** no touch equivalent was designed.

---

## 4. State transition — something changed status

### Cross-fade / morph between states
- **Works when:** the two states are the same object (icon plus→minus, play→pause).
- **Fails when:** the states are unrelated; then a swap reads cleaner than a morph.

### Expand / collapse
- **Works when:** height animates from a real measurement and the trigger stays
  in place so the reader doesn't lose their spot.
- **Misuse:** animating `height` on large content — jank. Prefer transform-based
  techniques or accept an instant change.

### Optimistic feedback
- **Works when:** the action almost always succeeds; the UI commits immediately
  and reconciles later.
- **Fails when:** failure is common or expensive — then optimism is a lie.

### Loading structure (skeleton, progressive fill)
- **Works when:** the shape of the incoming content is known.
- **Fails when:** it is a shimmer over a layout that will look different.

### Colour-only state change
- **Works when:** it is redundant with another signal (shape, weight, icon).
- **Fails when:** colour is the only cue — that fails both colour-blind readers
  and anyone glancing.

---

## 5. Ambient / looping — life without input

### Looping product demo
- **Works when:** a five-second loop shows one real task completing; no sound,
  no narration needed.
- **Fails when:** the loop needs context to parse, or restarts jarringly.

### Ticker / marquee
- **Works when:** quantity is the message and no single item must be read.
- **Fails when:** it carries content the reader needs.
- **Reduced motion:** stopped, wrapped into a static row or grid.

### Generative background (noise, mesh, shader, particles)
- **Works when:** the product is abstract, the palette is disciplined, and the
  motion is slow enough to read as atmosphere.
- **Fails when:** it competes with text, costs battery, or — most often — looks
  like every other generated hero. This is the highest AI-defaultness risk in
  this file.

### Breathing / idle micro-motion
- **Works when:** one element should feel alive (a status dot, a cursor).
- **Fails when:** several things breathe at once; the page looks unstable.

---

## 6. View transition — moving between pages or panes

### Shared-element transition
- **Works when:** the same object exists on both sides (a card that becomes a
  detail header) — it preserves the reader's sense of place.
- **Fails when:** the "shared" element is only loosely similar; the morph then
  reads as a glitch.

### Cross-fade between views
- **Works when:** you want continuity without claiming a spatial relationship.
- **Fails when:** used to paper over a slow load — it hides the fact that
  nothing is happening.

### Directional slide
- **Works when:** the navigation is genuinely spatial (steps, tabs, carousel)
  and the direction matches the reader's action.
- **Fails when:** direction is inconsistent across the product.

---

## 7. Value change — a number or chart moves

### Count-up on entry
- **Works when:** there is a real figure worth landing on; short (600–1000ms),
  ease-out, and the final value is what a screen reader announces.
- **Fails when:** the number is small (counting to 3 is silly) or invented.

### Chart draw-in
- **Works when:** the shape of the data is the message.
- **Fails when:** the animation delays comparison — readers came to compare.

### Value diff highlight
- **Works when:** something changed while the reader was watching.
- **Fails when:** everything highlights on every update.

---

## Failure modes to check before shipping any motion

- **No reduced-motion story.** Every pattern above needs a named static end
  state. Missing it is not a polish gap, it is an accessibility defect.
- **Animating layout properties.** `width`, `height`, `top`, `left`, `margin`
  cause reflow. Animate `transform` and `opacity`.
- **Motion as the only signal.** If the animation conveys information, the
  information must also exist statically.
- **Ceremony that doesn't scale down.** Delightful on the first visit, tedious
  on the tenth. Scale ceremony inversely with frequency.
- **Motion that outruns the content.** If the reader scrolls faster than the
  sequence, they see broken states — test at real reading speed, not at the
  speed of someone admiring their own build.
- **Effects the brand didn't earn.** A shader hero on a page about invoicing is
  borrowed impressiveness. Motion should come from the product's own world, the
  same way palette and typography do.

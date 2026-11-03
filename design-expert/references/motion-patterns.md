# Motion Patterns: Element Vocabulary by Job

Bans in SKILL.md Step 4 win over any value in this file.

Motion is a material, not a garnish. Every animated element must answer a
question the reader is actually asking — *where did this come from, what
changed, did my action register, how far along am I, what is alive here*. An
element that answers none of them is decoration, and decoration in motion is
the fastest way to make careful work look cheap.

This file is the **vocabulary**: what kinds of motion element exist, per job.
For timing values, easing curves, and copy-ready CSS, see
[polish-and-craft.md](polish-and-craft.md) (component-level recipes: its
Additional Motion Recipes section). For the discipline rules (durations,
`transform`/`opacity` only, ceremony scaled to frequency), see the main skill,
Step 12.

Whole pages and sites start in [motion-site-pass.md](motion-site-pass.md): it
decides where motion goes and how much, and this file picks the element once a
section has a job. Techniques named here but built elsewhere (split text, 3D,
path dots, scroll-linked rails) are in [motion-recipes.md](motion-recipes.md).
The families below are how a site-pass job is carried (step 6 there). Where
both files give a value, the site pass wins.

## How to use this file

1. Name the job: *this element announces arrival* / *this shows progress* /
   *this responds to the pointer*.
2. Pick two candidates from that job, one conventional and one with more
   presence, and keep "none" as the third option.
3. Reject on failure conditions. A pattern that breaks on touch, on fast
   scroll, or without JS is out unless you design the fallback deliberately.
4. **Write the reduced-motion behaviour before you build the motion.** If you
   cannot describe the static end state, the pattern isn't finished.

## Implementation ladder (climb only as far as needed)

0. **The platform's own effects**, when the profile names a platform (a site
   builder's appear, scroll and hover effects). Check what the platform does
   under reduced motion before relying on it.
1. **CSS transitions and keyframes** — hover, focus, entrance, state changes.
2. **Native scroll-driven animations** (`animation-timeline: scroll()` /
   `view()`) — scroll-linked effects with no library and no scroll listener.
   Baseline in Chromium, Safari and Firefox since 2026-10; keep them inside
   `@supports (animation-timeline: view())` so older browsers get the static
   end state.
3. **View Transitions API** — cross-view and element-morph transitions.
4. **A small amount of vanilla JS** — an `IntersectionObserver` for entrances,
   a rAF-throttled scroll read for progress. Roughly 50 lines covers most pages.
5. **The animation library the profile names** — when sequencing,
   orchestration, springs, or timeline control genuinely exceed the above. If
   no profile names one, stay at tiers 1–4 or ask.
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
- **Works when:** used sparingly, on one group per page rather than at every
  section boundary; small offsets (8–16px), short durations (200–400ms, the
  site pass's reveal class), ease-out.
- **Fails when:** applied to every element on the page — the reader spends the
  visit watching things assemble.
- **Misuse:** long distances and long durations. A 60px slide over 800ms is a
  page that feels slow to a fast reader.
- **Reduced motion:** rendered in place, no offset, no delay.

### Staggered reveal (siblings enter in sequence)
- **Works when:** the group is a set and the order carries meaning; one shared
  step (30–80ms and ≤300ms total in product UI; 50–90ms and ≤500ms total on
  marketing pages). Over ~8 items, the group reveals as one block, or not at
  all.
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
- **Recipe:** [motion-recipes.md](motion-recipes.md), 1. Text reveal.

### Counter-entry (element arrives from where it will act)
- **Works when:** the origin is meaningful — a panel from the edge it belongs
  to, a toast from the region it reports on.
- **Fails when:** the origin is arbitrary; then it is just a slide.

### Scroll tilt-in (a visual settles from a slight 3D tilt as it enters)
- **Works when:** one visual should feel placed in space — a product shot, a
  diagram — and the tilt stays under ~15°.
- **Fails when:** applied to full-screen containers or text; the page starts
  to sway.
- **Reduced motion:** flat from the start.
- **Recipe:** [motion-recipes.md](motion-recipes.md), 4. 3D scene.

---

## 2. Scroll progress — the reader's position drives the change

### Scrubbed progress (position maps to a value, reversible)
- **Works when:** something genuinely advances through the section — a path
  completing, a sequence stepping, a figure filling. The scroll *is* the easing;
  don't add a transition on the scrubbed property or it will lag the finger.
- **Fails when:** the section is shorter than one viewport height *(start)* —
  there is no travel to map onto.
- **Misuse:** non-reversible scrubbing. If scrolling back up doesn't unwind it,
  it isn't progress, it's a one-shot trigger with extra machinery.
- **Reduced motion:** final state, no scroll listener at all.
- **Recipe:** a rail fill with a marker dot that rides it,
  [motion-recipes.md](motion-recipes.md), 6. Scroll-linked progress.

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

### Pointer tilt (a card or visual leans toward the pointer)
- **Works when:** one hero visual or a small set of cards on a persuasive
  page, for a fine pointer only; ~8° at the edge.
- **Fails when:** on text cards, on every card, or as the only cue that
  something is clickable.
- **Reduced motion / touch:** flat, no pointer listener.
- **Recipe:** [motion-recipes.md](motion-recipes.md), 3. Pointer tilt.

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

### 3D flip (two faces of one object)
- **Works when:** both faces are states of one thing (summary and detail,
  question and answer) and the user flips it on purpose with a real button.
- **Fails when:** the reader must compare across faces, the content is long,
  or hover is the only trigger; an expand usually serves better.
- **Reduced motion:** the faces swap without rotation.
- **Recipe:** [motion-recipes.md](motion-recipes.md), 2. 3D card flip.

### 3D ring or cube (a small set the user turns)
- **Works when:** a handful of neighbours really sit in space and the user
  turns them with real buttons.
- **Fails when:** it rotates by itself without a pause, or carries body text.
- **Reduced motion:** a plain scrollable row.
- **Recipe:** [motion-recipes.md](motion-recipes.md), 4. 3D scene.

### Expand / collapse
- **Works when:** the panel opens instantly, or its content fades in with
  opacity, and the trigger stays in place so the reader doesn't lose their
  spot.
- **Misuse:** animating `height` — it reflows everything below on every frame
  (SKILL.md Step 12).

### Optimistic feedback
- **Works when:** the action almost always succeeds; the UI commits immediately
  and reconciles later.
- **Fails when:** failure is common or expensive — then optimism is a lie.

### Loading structure (skeleton, progressive fill)
- **Works when:** the shape of the incoming content is known and the wait
  exceeds ~300ms.
- **Fails when:** it is a shimmer over a layout that will look different, or
  the wait is so short that the shimmer flashes; use a static placeholder.

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

### Travelling dot on a path (sequence, timing, flow)
- **Works when:** the dot says what a still line with arrowheads cannot — the
  order or timing in which data moves between nodes, a process step in
  progress — and the brand's language allows lines that move. Direction alone
  is an arrowhead.
- **Fails when:** the line means nothing, the loop runs next to body text, or
  several dots compete on one screen.
- **Reduced motion:** the dot rests at the end and the path is fully lit. A
  loop past 5 seconds needs a visible pause. Run once, the dot is a technique
  inside one element, not ambient motion.
- **Recipe:** [motion-recipes.md](motion-recipes.md), 5. Glowing path.

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
- **Works when:** a real static figure is the page's one brand moment on a
  persuasive page; short (600–1000ms), ease-out, and the final value is what a
  screen reader announces. A figure that updates while in view gets a value
  diff highlight instead.
- **Fails when:** the number is small (counting to 3 is silly) or invented, the
  audience is task-driven, or it is one of several count-ups.

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
- **Uniform entrance.** The same entrance on four or more different
  components, the same hover-scale on three or more, two staggered lists
  alike, or any pulsing indicator reads as a template. Vary the manner with
  the content, or cut (thresholds: [motion-site-pass.md](motion-site-pass.md),
  Budget).
- **Autoplay without an exit.** Motion that starts by itself and runs past
  5 seconds needs pause, stop or hide (WCAG 2.2.2), or it ends within 5 s.
- **Effects the brand didn't earn.** A shader hero on a page about a routine admin tool is
  borrowed impressiveness. Motion should come from the product's own world, the
  same way palette and typography do.

# Motion Site Pass: Where, How Much, and Proof

Bans in SKILL.md Step 4 win over any value in this file. For motion they are
the same entrance on every block, and `cubic-bezier(0.16, 1, 0.3, 1)` at 400ms
with a 12–16px rise as an unprompted default. They govern what you add; motion
already on the page is judged in step 3.

Use this file when the task is to add motion to a page or a whole site, or to
review the motion already on it. It decides where motion goes, how much the
page can carry, and how you prove what shipped. Choosing one element's motion
is [motion-patterns.md](motion-patterns.md); building a technique is
[motion-recipes.md](motion-recipes.md); component timing is
[polish-and-craft.md](polish-and-craft.md).

Every section starts at **no motion**. It gets motion only after it names a
job, passes the gate and fits the budget. "This page needs no new motion" is a
valid result: report it with the candidates you rejected; never pad the map to
look busy.

Values marked *(start)* are starting values synthesised from sources, not yet
measured on real pages. Use them as written. If the profile sets its own value,
the profile wins. If a real pass shows a value is wrong, change it here, not
page by page.

**No profile.** The page's own tokens are the system (Mode B). Raw durations
and easings in the source count as the system only when they are consistent
(tokens, or one value used throughout); otherwise retune them and label the new
values as one Mode C token proposal. A value the motion needs that the system
lacks (a path duration, a scroll easing) is a labelled Mode C proposal, never a
silent addition. On a site builder, the route is the builder's own effects; a
value they cannot express is a question for the owner, not custom code. The
reduced-motion replacement is the default for the visitor mode (see Budget).
Patterns the recipes leave to "the profile's call" are allowed when their row
has a job and passes the gate. When a kept or new row carries a value and the
page has no consistent motion tokens, open the map with the Mode C proposal
(token, value, the rows that use it); writing `var(--token)` for a token the
page lacks is that proposal.

## Terms

- **Motion off:** reduced motion emulated and the motion code removed,
  including a `cursor: none` that hides the pointer behind a follower.
- **Body text:** running text read in sentences (paragraphs, sentence lists,
  quotes); not headings, labels or figures.
- **Text section:** a section whose content is mostly body text, with no media.
- **Decorative layer:** an element that carries no information and would be
  `aria-hidden`, such as a background shape or an illustration behind content.
  An image that carries information, the LCP image included, is content.
- **Clear of:** the moving element is not that element, does not contain it and
  does not cover it. An overlay (drawer, modal, toast) that moves as one object
  is clear of the text inside it, and an overlay opened by a user action is
  clear of the page content it covers: covering is its end state, not motion on
  that content.
- **Purpose:** what the movement adds over an instant change to the same end
  state: where something came from, what changed, the order or timing in which
  things happen, the order to read like items in, or, for the one brand moment,
  the brand's character. If an instant change says the same thing, there is no purpose. If
  a static change (an arrowhead, a label, a number) would say it, make that
  layout fix instead and cut the row. Control feedback has a purpose by
  definition.
- **Keyboard-triggered:** started by a shortcut or by key-only navigation
  (arrow keys, typing, a command palette, Tab focus). Enter or Space on a
  control that also takes a click is not keyboard-triggered: judge it by how
  often it is used.
- **Anchor-landed section:** a section whose id is the target of a link on the
  page or in the site's navigation. An id that nothing links to does not count.
- **Task-driven audience:** visitors who arrive to get something done: B2B
  tools, finance, admin, documentation. On a mixed page, the sections people
  consult (schedules, prices, menus, venue details, forms) count as
  task-driven.
- **Control feedback:** the hover, focus and press states of a control (a link,
  button or input), and a control's confirmation of its own action (copied,
  saved, toggled, a sort indicator flipping). It belongs to the component, not
  the section: never a section's job, trigger or allowance, and it counts only
  toward the hover-scale uniformity threshold. A hover effect on something that
  is not a control (a card with no link) is a candidate like any other. Missing
  states are a component defect to list, not something this pass designs.

## The pass

0. **Ready.** With motion off, the page is finished and reads well at 1440 and
   at 390 px. A failure is a defect that remains with all animation removed:
   horizontal overflow at 390 px; content or navigation clipped, overlapping or
   unreachable; text below AA contrast or too small to read. Missing control
   states and semantic defects (aria states, roles) go on a component-defect
   list and do not fail this step. Motion that hides content or the pointer (a
   hidden start state, a carousel showing one item, `cursor: none` behind a
   follower) is existing motion for step 3, not a failure here. If step 0
   fails, return the defect list first, still run step 3 on the existing
   motion, and add no new rows until the defects are fixed: motion is the last
   pass, never a rescue for a weak layout. Working from source only, judge from
   the markup and CSS at both widths, treat placeholder media as final, and
   mark each defect inferred. Name the platform, decide the visitor mode now
   (step 4; steps 3 and 7 depend on it), and load the profile's Motion section
   (route, tokens, reduced-motion replacement, budget overrides).
1. **Page transitions first.** Before touching sections, check page and view
   transitions and any theme or platform transition setting. A transition that
   holds back the next page's largest content is the most expensive motion on
   most sites: remove it, or state why it stays.
2. **Inventory.** Sections in DOM order, a still screenshot of each. Per
   section: role (see the role table), content type, above the fold or not,
   holds the LCP element or not, at 1440 and at 390 px (fold at 1440×900 and
   390×844). Then the motion already there: search the source for
   `transition`, `@keyframes`, `animation`, `requestAnimationFrame`,
   `setInterval` or `setTimeout` text updates, `scroll-behavior`,
   observer-added classes, builder effect settings and library calls; scroll
   the page and list live animations with `document.getAnimations()`; group
   what you find by purpose. An empty list from a site builder's API proves
   nothing: check the rendered page. Working from source only, without a
   browser: mark the fold and the LCP element as inferred, and every Check as
   unverified.
3. **Existing motion: keep, retune, replace or remove.** When two bullets
   match, the one that removes more wins:
   - keyboard-triggered, or done 100+ times a day: remove the motion; the end
     state stays;
   - no purpose and no job from the closed list (step 6): remove;
   - animates a layout property (height, width, top, left, margin): remove the
     animation and make the layout change instant; a fade of the revealed
     content may replace it only as a new candidate that passes the gate;
   - an endless loop: retune it to one run, or remove the motion and keep a
     static end state, unless it has a visible pause. A carousel's static end
     state shows every item, as a row or a stack; a marquee's duplicated items
     go. A loading indicator that stops when the request ends is not a loop: it
     is a state row, judged by Loading structure in motion-patterns.md; its
     length is the request's, so the frequency cap does not apply, and it
     animates transform or opacity only. Show it only when the wait exceeds
     ~300 ms; a shimmer shorter than one cycle reads as a flash, so a static
     placeholder serves better;
   - a ticking countdown or live counter: give it a visible pause, or render
     the value once at a granularity that stays true until the next load (days,
     not seconds); whether to show it at all is a content decision;
   - scroll parallax on content: remove; on a decorative layer, retune it to a
     few percent of travel inside `(prefers-reduced-motion: no-preference)`;
   - a custom cursor that replaces the native one: remove; the native cursor
     returns;
   - a stagger over budget: shorten it, or show the group at once;
   - a hover effect that also fires on touch: move it inside
     `(hover: hover) and (pointer: fine)`;
   - smooth anchor scrolling: keep it only inside
     `(prefers-reduced-motion: no-preference)` and list it like control
     feedback, with no row or timing; never add it (as a candidate it is out at
     question 8, rule: step 3).

   Record the outcome plainly: remove means the motion goes and the element
   stays in its end state; retune means the motion still runs with new values
   (duration, easing, distance, delay, iteration count or media condition).
   Changing the animated property, the animated element or the trigger is a
   replacement: a new row, blocked while step 0 fails.
   Everything else that stays goes through the gate (step 7) and the budget
   like a new candidate: keep it if it passes; retune it if only its values
   break the budget; if the pattern's own failure condition fails, remove it,
   and a different pattern may take its place only as a new row that passes
   the gate. Control feedback that stays skips the gate: check it only against
   the feedback duration class, the hover media query and the reduced-motion
   rule; it is listed, not counted.
4. **Visitor mode.** *Persuade/Experience* (marketing, portfolio, launches) or
   *Operate/Read* (product UI, docs, articles, dashboards). The mode picks the
   duration class and the budget rows. A marketing page whose main audience is
   task-driven runs Persuade/Experience, tightened: at most one lead, no scroll
   reveals, no count-up, all text still. Any other page with a consulted
   section (Terms, task-driven audience; a services list counts) is mixed: those
   sections take the tightened limits and the rest keeps plain
   Persuade/Experience.
5. **Thesis, before any code.** One lead moment or none; where continuity
   matters; where feedback matters; which expensive effects are allowed (3D,
   paths, split text); one sentence on why this page moves at all. Passing the
   gate allows a lead; it never requires one. Take a lead only when that
   sentence names it.
6. **One job per section**, from a closed list: feedback, continuity, state,
   hierarchy, explanation/progress, value change, brand moment. Default: none.
   Weight is separate from the job: any job can be the lead, and a brand moment
   is allowed only as the lead. The families in motion-patterns.md are how a
   job is carried:
   - entrance carries hierarchy or a brand moment; a counter-entry (an overlay
     arriving from its edge or region) carries continuity or state;
   - scroll progress carries explanation/progress;
   - pointer response and state transition carry feedback or state; a single
     hero-visual tilt may carry the brand moment, as the lead;
   - view transition carries continuity; value change carries value change;
   - ambient means a loop and carries a brand moment only. A path dot that runs
     once is a technique inside one element and carries explanation/progress.
7. **Gate.** A candidate is out at the first "no". Ask in order and name the
   lowest-numbered question that fails (later ones may follow as "also"); for
   question 8, also name the rule.
   1. Does its frequency allow motion (Budget, frequency rows)?
   2. Does it have a purpose (Terms)? An entrance that sets the reading order of
      like siblings has one: judge it at questions 1, 3 and 8, not here.
   3. Once it is in view, is nothing hidden longer than the mode allows
      (Operate/Read: its duration class; Persuade/Experience: 900 ms), and does
      nothing above the fold wait for a scroll or a script?
   4. Is it clear of the LCP element, at either width, and of text above the
      fold?
   5. Is it clear of body text?
   6. On phones, is it something other than a text section? A "no" drops it on
      phones only: mark the row desktop-only.
   7. If it runs past 5 s, does it carry a pause?
   8. Does it fit the budget, the section rules and role table below, and the
      pattern's own failure conditions (uniformity, one lead per screen, the
      mode's limits)?
8. **Level and technique.** Level: none; the section as one object; parent and
   children; a technique inside one element (split text, 3D, path, count-up).
   One unit of content gets one level. When several rows move, vary the manner
   with the content (rows slide, an image wipes through a mask, a number counts
   once), never one entrance everywhere. Trigger: load, once on entering view,
   scroll-linked, hover/press, a user action or state change, ambient.
9. **Budget.** Count the new rows plus everything kept in step 3. Cut until the
   page fits.
10. **Motion map** (template below): the rows; the step 3 dispositions; the
    rejected candidates you actually considered, the most tempting first, at
    most five, each with the gate question that removed it; then a
    one-paragraph verdict on how much motion this site actually needs, ending
    with the approval status (approval needed and why, or owner confirmed),
    even when the map has no rows. On a
    site builder, a client's site, a site you do not own, or when ownership is
    not stated: show the map and get approval before writing anything.
11. **Build** along the route: the platform's native effects where the profile
    names a platform, or the builder's own effects on a site builder;
    otherwise CSS first, then the library the profile names; every value from
    tokens. Every row ships with its reduced-motion state and a fallback for no
    script and no support.
12. **Verify** with the checklist below. Each row ends pass, fail or
    unverified. Smoothness, rhythm and feel that you did not watch yourself
    stay unverified until a person has watched them. A setting you cannot read
    (for example a site-wide reduced-motion switch in a site builder) becomes a
    check for the owner.

## Section or elements

- A section that reads as one object (an image with its caption, a card, a
  media block) animates as a container, once. Prose stays still.
- Children stagger only when they are like siblings read in order: cards,
  steps, rows, number tiles, with one shared step. A group of more than ~8
  *(start)* reveals as one block, or not at all.
- If a mixed section (heading, text, media, CTA) moves at all, one kind of
  element moves. By default that is the key visual, while the heading, text and
  CTA stay still and readable. A Persuade page may invert it: only the heading
  reveals.
- A parent and its children never both get their own reveal. Entrance groups
  never overlap.
- Order follows reading and stability: frame, body, dynamic content, primary
  action; data visualisation last. Inside a section: heading, text, image,
  details.
- What matters more moves more visibly and longer; small things move together
  and in sync.
- A technique inside one element (split heading, flip, path dot, count-up)
  uses the section's whole allowance and never combines with a reveal of the
  section itself. At most two levels of nesting and one trigger per section
  *(start)*; control feedback is not a trigger.
- No entrance, scroll or ambient motion on: navigation, sticky bars,
  backgrounds and dividers, long article text, footer and legal links, the LCP
  heading, and any anchor-landed section. Controls inside them keep their
  feedback. The same meaning gets the same motion across the site; a deliberate
  difference signals a different meaning.

| Role | Job, if it earns one | At most *(start)* |
|---|---|---|
| Hero | none, brand moment, or explanation/progress for a diagram | The heading stays still (it is usually the LCP element). Motion lives on a decorative layer or a diagram: a path dot, a light tilt of the visual, a scrubbed diagram |
| Logos, proof strip | none | A marquee only with a pause control; usually cut |
| Feature grid | none, or hierarchy | One staggered entrance of the children |
| Process, timeline | none, or explanation/progress | A scroll-linked rail fill, or a path dot inside the element |
| Numbers | none, or value change when a figure updates while in view | A short highlight when a figure updates. A count-up on a static figure adds nothing an instant render does not: allowed only as the page's one brand moment on a Persuade page, the final figure as static text, never for a task-driven audience |
| Quotes | none | At most one quote-heading reveal per Persuade page |
| Pricing, comparison | none | Nothing: it is read, compared and returned to |
| CTA band | none | Control feedback on the button only |
| Navigation, footer, legal | none | Control feedback only |
| Product: KPI or figures strip | none, or value change | A short highlight when a value changes while in view; never a count-up on load or on a filter change |
| Product: chart | none | Data present at t = 0; no draw-in on refresh |
| Product: data table | none | Rows never stagger; sorting and paging change instantly |
| Product: overlay (drawer, modal, toast) | continuity or state | A counter-entry from its own edge or region, inside the frequency row. A centred modal has no edge: opacity, optionally from scale 0.95–0.98, never a slide |
| Docs and article content | none, or explanation/progress for a diagram | Code blocks, callouts, tables and the table of contents never move |

A role not in the table takes the row it reads like: a menu with prices or
venue details reads like Pricing, a booking form like a CTA band, a project
grid like a Feature grid. If no row fits, its job is none.

## Budget

| Rule | Value | Basis |
|---|---|---|
| Every map row names a job from the closed list or is cut. "It looks nice" is allowed only for the one brand moment | — | Emil Kowalski's animation skills; Val Head |
| Product frequency: actions done 100+ times a day, and keyboard-triggered actions, get no animation; recurring actions take at most 150 ms. Recurring means an action the page exists for (filtering, sorting, paging, opening a record); one used a few times a session (export, settings) is occasional and takes the overlay class. The control that opens the panel for a recurring action (a filters drawer) is recurring too, and motion triggered by an action or by its result (a toast, a confirmation, a refreshed panel) takes that action's frequency. With no usage data, write your estimate in the row | 0 / ≤150 ms | Emil Kowalski; Atlassian |
| Marketing frequency: first-view motion plays once. What is revisited or stays on screen (navigation, sticky bars, pricing, anchor-landed sections) appears without animation. Nothing above the fold waits for a scroll | — | *(start)* |
| One lead moment per page, or none; never two leads on one screen | 1 / 1 | *(start)*, extended from Atlassian's one focal point per event |
| A scroll reveal plays once and does not replay on scroll-up. When two or more sections reveal, a static section sits between them. A reveal on every section is a failure, on a marketing page too | — | NN/g |
| The LCP element and hero text never hide behind a script-driven reveal. A hero entrance that stays is CSS keyframes under 0.3 s, or motion on a decorative layer under content that is already visible | <0.3 s | Shopify and web.dev: a hero fade-in costs 650–900 ms of LCP |
| Body text is not animated on scroll and not split. One kind of element appears per section. Text sections on phones get no scroll fade. For a task-driven audience no text is revealed, split or staggered on its own | — | NN/g |
| Operate/Read durations: feedback 100–150 ms (a control confirming its own action: copied, saved, toggled); routine 150–300 ms (content shown or hidden in place: accordion, tab, dropdown); overlays 200–300 ms (a layer above the page). The frequency row wins over these classes. Exits run shorter than entrances, with ease-in. Any overlay may exit instantly; an exit that animates takes the feedback class (100–150 ms) | — | Atlassian, NN/g |
| Persuade/Experience durations: supporting reveals 200–400 ms (fades over 500 ms get scrolled past); the lead alone 500–800 ms, never on the LCP element. Nothing in view stays hidden past 900 ms; a load sequence ends by 1.2 s. Exits run 50–100 ms shorter than entrances. These classes are for reveals: a technique that plays along a path or counts a value takes its recipe's duration, once, at most 5 s | — | NN/g, impeccable, taste-skill, Atlassian |
| Stagger in product UI: 30–80 ms per step, total ≤300 ms. On marketing pages: rows and items 50–90 ms, characters 20–40 ms (display text of 1–3 words only); total ≤500 ms. Total is the last item's delay. Over ~8 like items the group reveals as one block, or not at all; a load sequence of different elements has at most 4 steps | ≤300 / ≤500 ms; ~8 *(start)* | Emil Kowalski, Carbon, taste-skill |
| Uniformity defects: 4+ different components with the same entrance, 3+ with the same hover-scale, 2+ staggered lists alike, any pulsing indicator | 4 / 3 / 2 | kylezantos/design-motion-principles |
| Entrance travel of content in the page flow 8–16 px, 8 px on phones; never from `scale(0)`: start at 0.95–0.98, or use opacity alone. Overlays arrive from their own edge (counter-entry) | 8–16 px *(start)* | Chosen inside the sources' ranges |
| Motion that starts by itself and lasts over 5 s gets pause, stop or hide, or ends within 5 s (WCAG 2.2.2, level A). Auto-updating content (a ticking countdown, a live counter) counts too. Under 3 flashes a second (2.3.1). A glow pulse takes 1–4 s. At most one ambient loop per screen; it pauses off screen and stops under reduced motion | 5 s; <3 Hz; 1 loop *(start)* | WCAG 2.2 |
| No scroll hijacking. Pinned or scrubbed sequences stay short, earn their place and carry no body text. Little or no parallax, only on decorative layers, and none under reduced motion | — | NN/g; WCAG 2.3.3 |
| 3D: at most one flip pattern and one tilt group per page. Tilt ~8° at the edge, ceiling 15°, never on text cards. A self-rotating carousel or cube gets a pause. Scroll-driven rotation ≤15°, inside `@supports`, never on full-screen containers | 8° (15°); perspective 800–1000 px *(start)* | — |
| The whole map: at most ~5–7 rows that move and at most 3–4 sections with a reveal. Fewer is normal; zero is a valid result | ≤5–7 / ≤3–4 *(start)* | Extended from Emil Kowalski's cap of 5–7 suggestions per app |
| At most 6 animations running at once on desktop, 3 on phones. Count every element that animates at the same moment, a stagger group and a set of identical skeletons included; a row over the phone cap is marked desktop-only, like a "no" at question 6 | 6 / 3 *(start)* | Design systems publish no ceiling; the one found is 3 on mobile |

**Under reduced motion nothing travels**: no transform, position, scale, path
or scroll-linked movement, and every section is readable within 200 ms of
entering view. Control feedback in colour stays. The replacement is the
profile's call. When the profile is silent: Persuade/Experience surfaces use an
opacity crossfade of at most 200 ms, Operate/Read surfaces change instantly.
The rows on 5-second motion, flashes and reduced motion are accessibility
floors: a profile may tighten them, never loosen them.

## The motion map

One row per moving thing; under the map, the step 3 dispositions and the
control feedback that stays; then the rejected candidates (R1, R2…); then the
verdict.

- **#**: row number; R1, R2… for rejected candidates.
- **Section**: role and content type; flag above the fold and LCP.
- **Job, weight**: a job from the closed list; lead or support.
- **Level**: section, parent and children, inside one element.
- **Technique, trigger, route**: the recipe or pattern, what starts it, and
  where it is built (platform effect, CSS, library).
- **Timing**: duration, easing token, stagger step × (n − 1) = total; for a
  product row, the frequency estimate.
- **Reduced motion; no script**: the end state under reduced motion and the
  fallback without script or support.
- **Check**: how it was verified, and pass, fail or unverified.

Example for a fictional landing page. It shows the format, not a target: most
pages need fewer rows.

| # | Section | Job, weight | Level | Technique, trigger, route | Timing | Reduced motion; no script | Check |
|---|---|---|---|---|---|---|---|
| 1 | Hero: heading, CTA, product diagram; above the fold, heading is LCP | explanation/progress, lead | Inside one element: only the diagram moves | Path dot; once on entering view (on load when above the fold); CSS `offset-path` inside the SVG | 3.5 s linear, one run | Dot at the end, path fully lit; no support: dot hidden | One finite animation in the live list; reduced-motion screenshot equals the end state; feel unverified |
| 2 | Features: 6 like cards | hierarchy, support | Parent and children | Fade and 8 px rise; once at 15% visible; CSS plus an observer | 300 ms; 60 ms × 5 = 300 ms | Crossfade ≤200 ms; no script: all visible | The six count as one gesture; no other section repeats this entrance |
| 3 | Process: 4 steps on a rail, taller than the screen | explanation/progress, support | Inside one element | Scroll-linked rail fill; CSS view timeline in `@supports` | linear, entry 50% to exit 50% | Rail fully drawn and still | Unwinds on scroll-up |
| R1 | Logo strip | — | — | Out at question 2: decoration without information, and a marquee would also need a pause | | | |
| R2 | Quotes, 3 | — | — | Out at question 8 (uniformity): a fade-up here would be the fourth identical entrance | | | |

Verdict: three moving rows and one lead. The page persuades through the
diagram; everything else is read, so it stays still.

## Verify

| Check | How | Pass when |
|---|---|---|
| Live inventory matches the map | Listen for `animationstart` and `transitionrun` from page start. Scroll at 1440×900 and 390×844 in half-screen steps with a ~300 ms pause; at each step list `document.getAnimations()` (type, name, target, properties, duration, iterations, timeline). Grep for frame loops, timers and inline style writes, which that list cannot see | Every animated target has a map row or is listed control feedback; "none" rows produce zero animations; motion kept in step 3 is on the map |
| Uniformity and concurrency | Group entrances of different components by signature (keyframes or property set, duration, easing); count staggered lists and running animations at each step | Under the uniformity thresholds; one lead per screen; at most 6 running at once on desktop and 3 on phones *(start)* |
| Durations, stagger, hidden time | `getComputedTiming()` on each animation: duration and delay, stagger total per group, time from entering view to full opacity. A duration that is not a time means scroll-driven | Inside the mode's durations, the frequency row and the stagger totals; nothing hidden past 900 ms; exits shorter than entrances |
| Loops, autoplay, flashes | Filter infinite iterations and durations over 5 s on the document timeline, and timers that update text; look for a visible pause; check it stops off screen; measure pulse rates | WCAG 2.2.2 holds; at most one ambient loop; flashes under 3 Hz |
| Reduced motion | A fresh browser context with reduced motion emulated before the first load; repeat the scroll; screenshot each section at t = 0. Site-wide settings you cannot read go to the owner as a check | No transform, position, scale or path animation runs; opacity or colour only, up to 200 ms, where the profile allows it; every section readable; screenshots equal the map's end states |
| No script, failed script | Load with script disabled, then with the motion code blocked | All content visible; nothing stuck in a hidden start state; the CSS failsafe shows split text within ~1.5 s |
| Web vitals and compositing | A lab performance audit (LCP element, non-composited animations) and a performance trace while scrolling (layout-shift culprits, interaction latency) | The LCP element has no opacity or visibility entrance; CLS ≤0.1; INP ≤200 ms; no non-composited animation on a large surface |
| Frames, and an honest status | Record frames while scrolling, or screenshots at 0, 33, 66 and 100% of each scroll range; in Chromium, slow animations down through the DevTools animation domain. On a site builder, read every written interaction back | Each lead and scroll row has a frame strip; scrubbed effects unwind; what was written equals what reads back; "smooth" stays unverified until a person has watched it |

## Sources

Ideas restated, not copied. The gate, the rejected list, the verdict and the
removal tree: Emil Kowalski's animation skills (MIT). Uniformity thresholds:
kylezantos/design-motion-principles (MIT). Motion thesis, visitor modes, one
focal moment over repeated reveals: impeccable (Apache-2.0). Split units,
stagger and hidden-time values: taste-skill (MIT). Scroll reveals and text:
Nielsen Norman Group. Durations and choreography: Atlassian and Carbon design
systems. The motion audit: Val Head. Accessibility: WCAG 2.2 (2.2.2, 2.3.1,
2.3.3).

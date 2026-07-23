# Decision Psychology for UX

How to APPLY psychological principles when they collide with each other and
with reality. Read when a design decision is non-obvious or two principles
point in opposite directions.

## Contents
1. Applying the core principles
2. Worked conflicts (the hard part)
3. The same brief, different answers
4. Persuasion mechanics and their ethical line
5. Animation timing reference

---

## 1. Applying the Core Principles

### Cognitive load
Working memory is small; every element competes for it. Application, not
theory:
- Progressive disclosure: show what the current step needs, reveal on demand
- Sensible defaults: pre-select what most users choose; pre-fill from known
  data; date pickers default to today; country from detected location
- Recognition over recall: recent items beside the search box, autocomplete,
  thumbnails over filename lists, icons WITH labels (never instead of)
- The load that matters is *decision* load, not element count. A dense
  table of familiar data is lighter than three unfamiliar choices.

### Choice limits (Hick's Law) — fast thresholds
Response time increases logarithmically with the number of options. Use
these as defaults, not laws:
- Navigation: 5-7 top-level items max
- Settings: categorize, don't list everything flat
- Pricing: 3 plans; more than that needs a comparison tool
- Filters: show top 5, collapse the rest under "More"

### Target speed (Fitts's Law)
Time-to-hit a target depends on its size AND its distance from the current
point of action — not size alone. So don't just make important controls big;
put the next likely action physically close to where attention already is (a
"Save" button by the field just edited, not in a distant fixed toolbar).
Corollaries: screen edges and corners are effectively infinite-width targets
(the pointer stops there) — park global actions there; and keep destructive
controls far from frequent ones, since proximity that speeds up good clicks
speeds up bad ones too.

### Defaults
Most users accept defaults, which makes the default a decision you're making
for them. Make it the best option for most users, not for the business --
a business-serving default converts today and churns tomorrow.

### Loss aversion
Losses loom larger than gains. "You'll lose all 47 photos" lands harder than
"keep your photos." Use it to make consequences concrete at destruction
moments. Do NOT use it chronically -- constant loss framing produces anxious
users who trust the product less.

### Peak-end rule
People remember the peak moment and the ending, not the average. Engineer
one great moment (the first success) and a clean ending (clear confirmation,
obvious next step). If a flow has an unavoidably painful step (payment,
permissions), place it between positive moments, never last.

### Serial position
First and last items are remembered best: lead and close with what matters
(feature lists, onboarding sequence, the action step at the END of an error
message -- it's what they'll remember).

### Gestalt, in one breath
Proximity groups, similarity categorizes, closure completes progress bars,
figure-ground separates interactive from context, continuity guides the eye
along alignments. The practical rule: spacing IS meaning. If unrelated items
sit closer than related ones, the layout is lying.

---

## 2. Worked Conflicts

The textbook gives you principles. Practice gives you collisions. Resolve
them by, in order: (1) task frequency, (2) cost of user error, (3) the
user's emotional state.

### "Reduce choices" vs. "give control"
A pro video tool trimmed its export dialog to three presets (Hick's Law!)
and power users revolted -- their daily job needed codec control.
Resolution by frequency and audience: consumers get curation, professionals
get density with excellent defaults. The preset IS the default; the detail
lives one disclosure away, not deleted.

### "Reduce friction" vs. "prevent errors"
Friction is directional. At conversion moments (signup, first action) every
step loses users. At destruction moments, friction is protection. The
mistake is a uniform friction policy. Ask: what does an error cost the user
here? Sub-second recoverable → zero friction plus undo. Irreversible and
expensive → deliberate friction, typed confirmation.

### "Follow convention" vs. "this convention is bad"
Users arrive with habits from every other product (Jakob's Law), so
convention is a head start, not a rule. Break it only when BOTH are true:
your context genuinely differs from where the convention evolved, AND the
gain is large enough to pay the retraining cost. A novel date picker is
never worth it. A novel canvas interaction in a design tool might be the
product.

### "Celebrate success" vs. "stay out of the way"
Ceremony scales inversely with frequency. First project created → confetti
is fine. Five-hundredth email sent → a 2-second animation is theft. Design
the hundredth use, then add first-time delight as a layer that retires
itself.

### "Progressive disclosure" vs. "discoverability"
Hiding reduces load AND hides. Resolve by frequency data (or estimate):
daily actions stay visible even if the screen gets denser; weekly actions
can live one click deep; rare actions belong in search/command palettes.
The failure smell: support tickets asking for features that exist.

---

## 3. The Same Brief, Different Answers

"Design a file-delete flow" has opposite correct answers by context:

- **Consumer photo app:** deletion is rare, regret is common, stakes are
  sentimental. Answer: instant delete, 30-day trash, prominent restore.
  No confirmation dialog at all.
- **Developer infra console:** deletion is deliberate, blast radius is a
  production database. Answer: typed resource name, explicit consequence
  list, no undo theater (there is no undo -- say so).
- **Email client:** deletion is constant triage, hundreds per day. Answer:
  single keystroke, zero confirmation, undo toast, archive as default and
  delete as the deliberate secondary.

Same principles, weighted by frequency, error cost, and emotional state,
producing three unrecognizably different designs. If your recommendation
would survive being moved to a different product unchanged, it isn't a
recommendation yet -- it's a template.

"Design onboarding" splits the same way: a meditation app must set an
emotional tone before any feature (calm IS the product); a CLI tool's best
onboarding is a copy-pasteable command that works first try; a B2B admin
panel needs role-aware setup because the person configuring is not the
person using.

---

## 4. Persuasion Mechanics and the Ethical Line

Know these because they work; know the line because they work on people.

- **Anchoring:** the first option frames all others. Legitimate: premium
  plan first so the mid-tier reads as reasonable. Over the line: fake
  "was $199" anchors.
- **Commitment escalation:** small yeses precede big ones. Legitimate:
  email before credit card, name-the-project before payment. Over the line:
  burying the real commitment after sunk effort.
- **Social proof:** legitimate when true and relevant. Over the line:
  fabricated activity feeds, "12 people are viewing this" generators.
- **Scarcity/urgency:** legitimate when real (actual inventory, actual
  deadline). Over the line: countdown timers that reset. One discovered
  fake destroys all future trust signals.
- **Variable reward:** the slot-machine mechanic. Nearly always over the
  line outside entertainment. If retention needs it, the product has a
  value problem the mechanic is hiding.

The test: would the design still work if the user fully understood it?
Persuasion survives transparency; manipulation doesn't.

---

## 5. Animation Timing Reference

| Element | Duration | Easing |
|---|---|---|
| Button hover/press | 100-150ms | ease-out |
| Tooltip appear | 150-200ms | ease-out |
| Dropdown open | 200-250ms | ease-out |
| Modal enter | 250-300ms | ease-out |
| Modal exit | 200ms | ease-in |
| Page transition | 300-400ms | ease-in-out |
| Skeleton shimmer | 1500ms loop | linear |
| Stagger between items | 50-80ms | -- |

Rules:
- Closing faster than opening -- leaving must feel effortless
- Linear easing only for continuous loops (progress, shimmer); everywhere
  else it reads as mechanical
- Animate only `transform` and `opacity` (GPU-accelerated)
- `prefers-reduced-motion: reduce` → remove all non-essential animation

CSS easing values:
```css
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
--ease-in: cubic-bezier(0.7, 0, 0.84, 0);
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
--spring: cubic-bezier(0.34, 1.56, 0.64, 1);
```

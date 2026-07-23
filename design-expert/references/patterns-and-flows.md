# Patterns and Flows: A Selection Library

Patterns are context-dependent. Every entry here states when it works, when
it fails, and how it gets misused -- because recommending a pattern without
its failure conditions is how generic UX advice happens.

## Contents
1. Onboarding
2. Authentication
3. Forms and Data Input
4. Checkout and Payment
5. E-Commerce
6. Search
7. Navigation
8. Dashboards
9. Settings
10. Empty States
11. Destructive Actions
12. Notifications
13. Cross-Industry Transfer Map

---

## 1. Onboarding

### Progressive (explore first, teach in context)
- **Works when:** the product has a usable free surface (Notion, Linear) and
  value is discoverable by poking around.
- **Fails when:** the product is empty or dangerous until configured
  (payroll, infra tooling) -- users flounder and churn.
- **Misuse:** tooltip storms. Ten contextual hints firing at once is a tour
  wearing a disguise.

### Guided wizard (step-by-step setup)
- **Works when:** setup is genuinely required before any value exists
  (connecting a data source, importing a catalog). Show "Step 2 of 4",
  one action per step, let users skip non-essentials.
- **Fails when:** used for products that don't need setup -- it delays
  time-to-value and inflates drop-off before the first aha moment.
- **Misuse:** collecting marketing-qualification data ("What's your company
  size?") disguised as setup. Users can smell it.

### Value-first (show value before asking for anything)
- **Works when:** value is demonstrable instantly to an anonymous user.
  Duolingo's first lesson before signup, Canva's templates before login.
- **Fails when:** value depends on the user's own data (analytics, CRM) --
  a demo with fake data can substitute, but weakly.
- **Misuse:** value-first then a paywall ambush. The trust you built converts
  to resentment at exactly the commitment moment.

**Universal rules:** time-to-value under 60 seconds where possible; ask only
for what the product needs right now; the first action should produce a
visible result; every step should feel like progress, not paperwork.

---

## 2. Authentication

### Social login (Google/Apple/etc.)
- **Works when:** consumer products where signup friction kills conversion,
  and users are logged into those providers on that device.
- **Fails when:** enterprise (users don't want work accounts tied to
  personal Google), or audiences with privacy sensitivity.
- **Misuse:** offering 6 providers. Two or three max, plus email -- more
  creates login amnesia ("which one did I use?").

### Magic link / email code
- **Works when:** login is occasional and the user is near their inbox.
  Removes password reset burden entirely.
- **Fails when:** login is frequent (daily tools -- inbox round-trips get
  old fast) or users are on devices without their email.
- **Misuse:** magic link as the ONLY method for a daily-use product.

### Password + email
- **Works when:** always acceptable as a fallback; expected in enterprise.
- **Rules:** show-password toggle, no arbitrary composition rules (length
  beats complexity), paste allowed, password managers supported, reset flow
  that actually works.

### SSO (SAML/OIDC)
- **Works when:** selling to companies with IT departments. It's often a
  purchase requirement, not a UX choice.

**Universal rules:** never make users guess which method they used before --
detect and hint. Session length should match product sensitivity: a bank
logs you out, a design tool never should.

---

## 3. Forms and Data Input

### Single long form
- **Works when:** under ~8 fields, all one topic, users are motivated
  (checkout address). Everything visible = progress is self-evident.
- **Fails when:** 20-field walls. Perceived effort kills starts.

### Multi-step form
- **Works when:** long forms that chunk naturally by topic. One topic per
  step, progress indicator, back button that preserves data.
- **Fails when:** artificial splitting -- 2 fields per step across 8 steps
  feels like being drip-fed.
- **Misuse:** hiding the total length. "Step 1 of ?" breeds abandonment.

### Inline / conversational (one field at a time)
- **Works when:** emotional or complex inputs (insurance claims, medical
  intake) where focus per question improves answer quality.
- **Fails when:** expert users doing repeat entry -- it's painfully slow.

**Universal rules:** label above field; validate on blur, not on every
keystroke, and never before the user has finished; error messages next to
the field they describe; never clear a form on error; autofill-friendly
input types; optional fields marked (or better, removed).

---

## 4. Checkout and Payment

- **Guest checkout first.** Forced account creation before payment is a
  classic conversion killer. Offer account creation AFTER purchase, when the
  user has something to protect (their order).
- **Show total cost early.** Surprise shipping costs at the last step are
  among the most-cited abandonment causes.
- **One-page vs multi-step:** one-page works for returning users with saved
  details; multi-step works for first purchases (each step is small and
  progress is visible). Don't mix payment and account questions on one step.
- **Trust signals at the anxiety moment:** security indicators belong next
  to the card field, not in the footer.
- **Misuse pattern to avoid:** urgency theatrics ("3 left!" that resets on
  refresh). Works once, poisons trust permanently.

---

## 5. E-Commerce

### Product Pages
- Hero image left, details right (desktop) / image top (mobile)
- Price always visible without scrolling
- Add-to-cart button is the primary CTA, always visible
- Social proof (reviews, ratings) near the CTA
- "In stock" / shipping estimate before the user asks

### Cart
- Persistent cart accessible from every page
- Edit quantity inline (don't force a new page)
- Show running total including estimated shipping
- "Save for later" prevents deletion anxiety
- Related products at bottom, not interrupting the flow

### Checkout
- Guest checkout always available (see section 4 — forced signup kills conversion)
- Progress indicator: Cart → Shipping → Payment → Confirm
- Auto-fill wherever possible for addresses and saved cards
- Show the order summary at every step, not just the last
- Security badges near the payment fields, at the anxiety moment
- A final review step before the charge — never charge on a mis-click

---

## 6. Search

### Input
- Tell users what's searchable: "Search projects, files, or members"
- Autocomplete with recent and popular suggestions
- Results as user types (debounced 200-300ms) for small datasets;
  explicit submit for heavy queries
- Cmd/Ctrl+K launcher for power-user products

### Results
- Show result count; highlight matching terms
- Filters visible but progressive (top 5, "More" for the rest)
- **No-results is a design surface:** suggest corrections, relax filters
  automatically and say so, show popular items. A dead-end no-results page
  ends sessions.

### When search is the wrong answer
Browsable categories beat search when users don't know the vocabulary
(a spare-parts catalog, a legal help center). Search assumes the user can
name what they want. If they can't, invest in navigation and facets first.

---

## 7. Navigation

### Top navigation
- **Works when:** 5-7 main sections, marketing sites, simple apps.
- **Fails when:** the product grows -- top nav has a hard width ceiling.

### Side navigation
- **Works when:** 8+ sections, complex apps, frequent switching. Group with
  section headers, collapse to icons for workspace.
- **Fails when:** mobile (steals width) -- needs a different mobile answer.

### Bottom tabs (mobile)
- **Works when:** 3-5 top destinations used constantly. Thumb-reachable.
- **Fails when:** more than 5 -- a "More" tab is where features go to die.
- On the hamburger menu: it hides everything behind a tap and out of sight.
  Acceptable for genuinely secondary items; a failure as primary navigation.

**Universal rules:** where am I / where can I go / how do I get back,
answerable in 1 second. Active state always marked. Same placement on every
screen -- spatial memory is real.

---

## 8. Dashboards

- Answer "is everything okay?" in 3 seconds -- that's the job.
- Most dashboards show too much. Ruthlessly prioritize: what decision does
  the viewer make with this? A metric that drives no decision is decoration.
- Hierarchy: status first (okay / not okay), trends second, detail on demand.
- Real-time data needs visible freshness ("updated 2m ago") or users
  distrust everything on the screen.
- Mobile dashboards: top 3 metrics, not a shrunken desktop.
- Sparklines for trends, not just the current number — a value with no
  history invites the wrong question ("is this good?") instead of the
  right one ("is this improving?").
- Green/yellow/red status coding for at-a-glance state, always paired with
  text or an icon, never color alone.
- Bulk actions for power users working through many items at once —
  operational dashboards without them force one-by-one repetition.
- Empty state signals success, not absence: "All caught up" beats
  "No data yet" when the dashboard is action-oriented.
- **Misuse:** the wall-of-charts dashboard built to impress in a demo and
  never used after week one. If users export to a spreadsheet to answer
  their question, the dashboard failed.

---

## 9. Settings

- Group by user task/topic, never alphabetically (alphabetical assumes users
  know your feature names).
- Most-changed settings at the top; search when the list is large.
- Progressive disclosure: common visible, advanced collapsed.
- Auto-save individual toggles; batch-save grouped forms. Never make users
  discover an unsaved-changes rule by losing work.
- Toggle labels must state what ON means ("Email notifications: on"), not
  a double negative ("Disable non-notification suppression").
- Destructive settings (delete account, transfer ownership) get their own
  clearly-marked zone with deliberate friction.

---

## 10. Empty States

The empty state is the FIRST thing new users see, and "No data yet" is a
shrug where a handshake should be. Choose deliberately:

- **Educational:** explain what will live here and why it's valuable.
- **Actionable:** stage the first action right there ("Create your first
  project" with the button IN the empty state, not in a distant toolbar).
- **Example-filled:** show a template, sample data, or worked example the
  user can modify. Modifying beats creating from scratch.
- **For search/filters:** empty-because-filtered is different from
  empty-because-new. Say which one it is and offer the fix (clear filters).

---

## 11. Destructive Actions

- **Undo beats confirm.** Confirmation dialogs get reflexively clicked
  through -- they train the exact behavior they exist to prevent. An undo
  window (Gmail's send delay, trash-then-purge) actually recovers mistakes.
- **Confirm when undo is impossible** (irreversible external effects:
  payments, sends to third parties, permanent purges). Then confirm well:
  name the object and consequence ("Delete 'Q3 Report' and its 14 files?"),
  make the destructive button state the action ("Delete files", never "OK"),
  and for catastrophic actions require typed confirmation of the name.
- **Distance matters:** destructive actions never sit adjacent to frequent
  actions (delete next to save = designed accidents).
- **Scale friction to blast radius:** deleting a draft = instant with undo.
  Deleting a workspace = typed confirmation. Same pattern everywhere is
  either paranoid or reckless.

---

## 12. Notifications

- Interrupt only for things requiring action from THIS user NOW. Everything
  else: passive indication (badge, feed) or digest.
- Every notification type needs independent opt-out -- one global toggle
  forces all-or-nothing and users choose nothing.
- Respect the channel hierarchy: in-app < email < push. Escalate only with
  earned trust; a new app sending push on day one gets muted.
- **Misuse:** re-engagement notifications disguised as information
  ("Your friends are waiting!"). Short-term metrics, long-term uninstalls.

---

## 13. Cross-Industry Transfer Map

Strip your problem to its abstract form, then study the industry that has
the highest stakes on that exact problem. Extract the mechanism, never the
screens.

| Abstract problem | Study | The mechanism to steal |
|---|---|---|
| Teach complexity without a manual | Game tutorials | Progressive difficulty; introduce one mechanic per moment of need |
| Prevent catastrophic error | Aviation | Checklists, read-back confirmation, guarded switches |
| Build trust before commitment | Banking, dating apps | Graduated disclosure; small reversible steps before big ones |
| Make repeat tasks feel rewarding | Fitness apps | Visible streaks and progress; never punish a missed day harshly |
| Guide choice among many options | Restaurant menus | Anchoring, curation, "chef's choice" defaults |
| Handle stressed users | Emergency services, airline IROPS | One instruction at a time, calm tone, always show the next step |
| Data entry at speed | Tax software, point-of-sale | Aggressive autofill, keyboard-first, sensible tab order |
| Real-time collaboration | Multiplayer games | Presence indicators, live cursors, conflict-free merging |

The ethics check: some mechanisms (variable rewards, streak anxiety, urgency)
work by exploiting the user. Knowing them means knowing when to refuse them.

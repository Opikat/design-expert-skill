# Patterns and Flows

Cross-industry design patterns and flow architecture. Read when designing
user flows, onboarding, or looking for proven solutions to common problems.

---

## Onboarding Patterns

### Progressive Onboarding (Best for SaaS)
Don't front-load setup. Let users explore, introduce features in context.
- Stripe: one field at a time, value visible immediately
- Notion: empty workspace with contextual "Try this" prompts
- Linear: minimal setup, power features revealed through use

### Guided Onboarding (Best for Complex Products)
Step-by-step wizard when setup is genuinely required.
- "Step 2 of 4" — always show progress
- One action per step, never a wall of fields
- Let users skip non-essential steps
- Celebrate completion with a clear "what's next"

### Value-First Onboarding (Best for Consumer)
Show value before asking for anything.
- Duolingo: first lesson before signup
- Spotify: music plays before account creation
- Canva: template visible before login required

### Key Onboarding Rules
- Time-to-value should be under 60 seconds
- Ask only for what you need RIGHT NOW
- Use possessive language from step one ("Your workspace")
- Every step should feel like progress, not paperwork
- The first action should produce a visible result

---

## Authentication Patterns

### Login
- Email + password is the baseline
- Social login reduces friction (Google, Apple most trusted)
- Magic link eliminates passwords entirely
- Biometric (Face ID, fingerprint) for mobile apps
- "Remember me" should be on by default

### Signup
- Minimize fields: name + email + password minimum
- Show password requirements BEFORE the user types
- Real-time validation, not post-submission error walls
- Clear value proposition visible during signup
- "Already have an account?" always visible

### Password Reset
- Never say "that email doesn't exist" (security risk)
- "If an account exists, we've sent a reset link"
- Link expires in 1 hour, one-time use
- After reset: auto-login, don't make them sign in again

---

## E-Commerce Patterns

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
- Guest checkout always available
- Progress indicator: Cart → Shipping → Payment → Confirm
- Auto-fill wherever possible (addresses, saved cards)
- Show order summary at every step
- Security badges near payment fields
- Final review step before charge

---

## Dashboard Patterns

### Information Dashboard (Monitoring)
- Most critical metric largest and top-left
- Sparklines for trends, not just current numbers
- Color coding: green/yellow/red for status at a glance
- Time range selector globally applied
- Refresh indicator so users know data is current

### Operational Dashboard (Action-Taking)
- Tasks requiring action surfaced prominently
- Filters for status, priority, assignee
- Bulk actions for power users
- Empty state shows success: "All caught up"

### Key Dashboard Rules
- Answer "is everything okay?" in 3 seconds
- Most dashboards show too much — ruthlessly prioritize
- Real-time data needs visible refresh timestamps
- Mobile dashboards show the top 3 metrics, not everything

---

## Settings Patterns

### Organization
- Group by topic, not alphabetically
- Most-changed settings at the top
- Search within settings for products with many options
- Progressive disclosure: basic visible, advanced collapsed

### Common Mistakes
- Making users save individual fields (auto-save or save all)
- Hiding critical settings in sub-sub-menus
- No confirmation for destructive setting changes
- Settings that require restart without warning
- Toggle labels that don't make it clear what ON means

---

## Search Patterns

### Search Input
- Tell users what's searchable: "Search projects, files, or members"
- Autocomplete with recent and popular suggestions
- Show results as user types (debounced 200-300ms)
- Search icon OR "⌘K" shortcut for power users

### Results
- Show result count: "12 results for 'budget'"
- Highlight matching terms in results
- Filter/sort options visible but not overwhelming
- No results: suggest corrections, show popular items

---

## Navigation Patterns

### Top Navigation
Best for: 5-7 main sections, marketing sites, simple apps
- Logo left, primary nav center or left, actions right
- Active state clearly marked
- Mobile: hamburger menu (reluctantly — it hides navigation)

### Side Navigation
Best for: 8+ sections, complex apps, frequent switching
- Fixed sidebar with collapsible option
- Group items with clear section headers
- Active state with background highlight
- Collapse to icons for more workspace

### Tab Navigation
Best for: 2-5 views of the same data, mobile apps
- Bottom tabs on mobile (thumb zone)
- Maximum 5 tabs — more requires a "More" overflow
- Active tab always visible without scrolling
- Badge counts for items needing attention

---

## Cross-Industry Inspiration

The best solutions come from adjacent industries:

| Your Problem | Look At |
|---|---|
| Complex onboarding | Gaming tutorials (progressive difficulty) |
| Trust in transactions | Banking (security reassurance patterns) |
| Content discovery | Streaming services (recommendation UX) |
| Collaboration | Multiplayer games (real-time presence) |
| Data input | Tax software (wizard patterns, auto-fill) |
| Retention | Fitness apps (streaks, progress, milestones) |
| Emergency actions | Aviation cockpits (error prevention, confirmation) |

Don't copy screens — extract the principle and apply it to your context.

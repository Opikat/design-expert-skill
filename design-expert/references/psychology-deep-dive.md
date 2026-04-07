# Psychology Deep Dive

Detailed cognitive science principles for UX design decisions. Read when
making design choices that involve how humans perceive, decide, and behave.

---

## Cognitive Load Theory (Detailed)

Working memory holds ~4 chunks (Miller's revised estimate). Every UI element
competes for processing bandwidth.

### Progressive Disclosure in Practice
- Show 3-5 options initially, reveal more on demand
- Settings: show common options, "Advanced" for the rest
- Forms: one topic per step, not a 20-field wall
- Onboarding: one action per screen with clear progress

### Sensible Defaults
- Pre-select the most common option (80% of users choose this)
- Pre-fill from previous sessions or user data
- Date pickers default to today, not January 1, 2000
- Country selector defaults to user's detected location

### Recognition Over Recall
- Show recent items, not just a search box
- Autocomplete with suggestions as users type
- Visual thumbnails beat text-only file lists
- Use icons alongside labels (not instead of)

---

## Decision Architecture (Detailed)

### Default Bias
72% of users accept defaults. This is enormous power — make defaults the
best option for most users, not the best option for the business.

### Anchoring
The first number or option anchors all subsequent judgment:
- Show premium plan first on pricing pages
- "Usually takes 5 minutes" anchors expectations
- "Join 50,000+ users" anchors perceived popularity

### Choice Overload (Hick's Law)
Response time increases logarithmically with number of options:
- Navigation: 5-7 top-level items maximum
- Settings: categorize, don't list everything flat
- Pricing: 3 plans. If more, use a comparison tool
- Filters: show top 5, collapse the rest under "More"

### Commitment Escalation
Small commitments lead to larger ones:
- Email before credit card
- Free trial before paid plan
- Name the project before asking for payment details
- "Start free" not "Buy now" as the first CTA

### Loss Aversion
Losses feel ~2x more intense than equivalent gains:
- Destructive confirmations: "You'll lose all 47 photos"
- Retention: "Keep your 3 saved projects"
- DON'T overuse — chronic loss framing creates anxiety

---

## Gestalt Principles Applied

### Proximity
Items close together are perceived as a group. The single most important
layout principle. Related form fields need less spacing than unrelated ones.

### Similarity
Items that look alike are perceived as related. Same color/shape/size = same
category. Use this for consistent button hierarchies and status indicators.

### Closure
The brain completes incomplete shapes. Progress bars work because of this.
Step indicators with partial fills leverage closure.

### Figure-Ground
Users need to immediately identify foreground (interactive content) from
background (context). Modals use overlays. Cards use elevation. Active tabs
use contrast.

### Continuity
The eye follows smooth paths. Alignment grids create visual flow. Breadcrumbs
work because the eye follows the line. Horizontal carousels leverage this.

---

## Animation Timing Reference

| Element | Duration | Easing |
|---|---|---|
| Button hover/press | 100-150ms | ease-out |
| Tooltip appear | 150-200ms | ease-out |
| Dropdown open | 200-250ms | ease-out |
| Modal enter | 250-300ms | ease-out |
| Modal exit | 200ms | ease-in |
| Page transition | 300-400ms | ease-in-out |
| Skeleton shimmer | 1500ms loop | linear |
| Stagger between items | 50-80ms | — |

**Rules:**
- Closing is always faster than opening
- NEVER linear easing except for continuous loops (progress, shimmer)
- Animate only `transform` and `opacity` (GPU-accelerated)
- `prefers-reduced-motion: reduce` → remove non-essential animation

**CSS easing values:**
```css
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
--ease-in: cubic-bezier(0.7, 0, 0.84, 0);
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
--spring: cubic-bezier(0.34, 1.56, 0.64, 1);
```

---

## The Peak-End Rule

People judge experiences by the peak moment (best or worst) and the ending.

**Application:**
- Make the first successful action feel great (the peak)
- End flows with a clear, satisfying confirmation (the end)
- If there's a painful step (payment, permissions), sandwich it between
  positive moments
- Delete confirmations are the worst moment — make recovery easy

---

## Serial Position Effect

People remember first and last items best:
- Feature lists: most important benefit first and last
- Onboarding: start with the most exciting step, end with celebration
- Navigation: most-used items at start and end of the nav bar
- Error messages: put the action step last (what they'll remember)

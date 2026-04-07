# UX Strategy Deep Dive

Detailed psychology principles, content architecture, flow design, and validation methods for advanced UX work. This reference complements the SKILL.md essentials with implementation depth.

---

## Decision Architecture (Advanced)

### Default Bias in Action
72% of users accept defaults. This is not a bug — it's how human minds work under cognitive load.

- Pre-select the most common option (not the most profitable for your business)
- Pre-fill from previous sessions or user data when available
- "Remember me" enabled by default for trusted devices
- Date pickers default to today, not a distant past date

### Anchoring Effects
The first number or option anchors all subsequent judgment:

- **Pricing:** Show premium plan first; the mid-tier becomes the perceived "value" option
- **Time estimates:** "Usually takes 5 minutes" anchors expectations; users are surprised if it takes 2 and frustrated if it takes 10
- **Social proof:** "Join 50,000+ users" anchors perceived popularity and legitimacy
- **Ranges:** "between $10-50" anchors perceptions; reversal ($50-10) feels like you're backing down

### Choice Paralysis (Hick's Law)
Response time increases logarithmically with options. Beyond 5-7 choices, decision quality drops and anxiety rises.

- **Navigation:** 5-7 top-level items maximum before moving to nested or search
- **Settings:** Categorize by task, not alphabetically; hide advanced options
- **Pricing:** 3 plans. If more, use a comparison tool or feature flags
- **Filters:** Show top 5, collapse the rest under "More filters"
- **Form fields:** Chunk into logical sections; one concept per step

### Commitment Escalation
Small commitments lead to larger ones:

- Email address before credit card (reduces friction)
- Free trial before paid plan (establishes habit)
- Name the project before asking for payment details (ownership)
- "Start free" → "Start paid" when they're invested, not "Buy now" upfront

### Loss Aversion in Microcopy
Losses feel ~2x more intense than equivalent gains:

- Destructive confirmations: "You'll lose all 47 photos" hits harder than "Delete these photos"
- Retention messaging: "Keep your 3 saved projects" vs. "Lose your 3 saved projects"
- Warning: Chronic loss framing creates anxiety and damages trust if overused
- Use strategically at moments of real consequence (delete, logout, downgrade)

---

## Gestalt Principles Applied

### Proximity (Most Powerful)
Items close together are perceived as a group. Single most important layout principle.

- Related form fields need less vertical spacing (8-12px) than unrelated fields (24px)
- Group payment info together; separate shipping info below
- Breadcrumbs work because they're close together
- Cards use whitespace to separate unrelated content

### Similarity
Items that look alike are perceived as related:

- Consistent button styling for all primary actions
- Same color/size icons indicate the same category
- Consistent status indicator colors (green=good, red=error, yellow=warning)
- Visual consistency creates scannability

### Closure
The brain completes incomplete shapes:

- Progress bars work because we see the completion
- Step indicators with visual fill leverage closure
- Partially-hidden cards hint at scrollable content
- Skeleton screens work because the brain fills in the shape

### Figure-Ground
Immediate identification of foreground (interactive) vs. background (context):

- Modals use dark overlays to push content forward
- Cards use elevation (shadow) to separate from background
- Active tabs use high contrast; inactive tabs recede
- Hover states must contrast with the base state

### Continuity
The eye follows smooth paths:

- Alignment grids create visual flow
- Breadcrumbs work because the eye follows the line
- Horizontal carousels leverage continuous scrolling
- Diagonal lines in diagrams guide reading direction

---

## Animation Timing Reference

| Element | Duration | Easing | Purpose |
|---|---|---|---|
| Button hover/press | 100-150ms | ease-out | Immediate feedback |
| Tooltip appear | 150-200ms | ease-out | Preview without disruption |
| Dropdown open | 200-250ms | ease-out | Menu reveals gradually |
| Modal enter | 250-300ms | ease-out | Draws attention intentionally |
| Modal exit | 200ms | ease-in | Quick dismissal |
| Page transition | 300-400ms | ease-in-out | Conveys navigation |
| Skeleton shimmer | 1500ms loop | linear | Indicates loading |
| Stagger between items | 50-80ms | — | Creates rhythm |

**Critical rules:**
- Closing is always faster than opening (signals completion)
- NEVER use linear easing except for continuous loops (progress bars, shimmer)
- Animate only `transform` and `opacity` (GPU-accelerated; avoid layout thrashing)
- Respect `prefers-reduced-motion: reduce` → remove non-essential animation entirely

**CSS easing reference:**
```css
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);      /* snappy, energetic */
--ease-in: cubic-bezier(0.7, 0, 0.84, 0);       /* deceleration */
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);  /* smooth both directions */
--spring: cubic-bezier(0.34, 1.56, 0.64, 1);    /* playful, elastic */
```

---

## Peak-End Rule (Experience Design)

People judge experiences by the peak moment (best or worst) and the ending.

**Application strategies:**
- **First successful action:** Make it feel great — this becomes the anchor memory
- **Ending:** Always clear, satisfying, with obvious next steps (reduces uncertainty)
- **Painful steps:** Sandwich between positive moments (payment comes after preview success, before confirmation celebration)
- **Delete confirmations:** These are peak-worst moments — provide easy recovery ("Restore deleted items")
- **Error recovery:** The peak moment in an error flow is the recovery — celebrate the fix

---

## Serial Position Effect

People remember first and last items best (primacy + recency).

- **Feature lists:** Most important benefit first and last; weak benefits in the middle
- **Onboarding:** Start with the most exciting step (builds momentum), end with celebration (lasting memory)
- **Navigation:** Most-used items at start and end of nav bar; less-used in middle
- **Error messages:** Put the action step last (what they'll remember doing)
- **Settings:** Frequently-changed options at top; rarely-changed at bottom

---

## Information Scent and Content Hierarchy

### F-Pattern for Text-Heavy Pages
Users scan in an F-shape: left-to-right along the top, then down the left side.

- Key information must appear in first two words of each line
- Subheadings and bullet points break up text
- Avoid burying important info mid-paragraph
- Left alignment gets 30% more attention than center or right

### Z-Pattern for Visual Pages
Eye follows top-left → top-right → bottom-left → bottom-right.

- Hero image top-left or top-right (depending on language)
- CTA at bottom-right
- Supports page layout for product pages, landing pages
- Less critical for text-heavy interfaces

### Information Scent
Every link and button must clearly signal what's behind it:

- Vague labels ("Click here") create uncertainty
- Specific labels ("See pricing plans") reduce friction
- Icon + text together is clearer than icon alone
- Hover states should preview destination if possible
- Breadcrumbs provide continuous scent back to home

---

## Edge Cases and Flow Design

### Designing All States (Not Just Happy Path)
Every screen needs consideration for:

- **Empty state:** What does a new user see? Make it useful, not "no data found"
- **Loading state:** Use skeleton screens (show structure); avoid spinners (show nothing)
- **Error state:** What went wrong + why + what to do now + preserve user's work
- **Success state:** Celebrate key moments; never slow people down
- **0 items:** Different from "no results" (empty) vs. "search found nothing" (try again)
- **1 item:** Single-item states look broken if styled like lists
- **Many items:** Pagination, virtualization, or infinite scroll with care
- **Missing data:** Placeholder or fallback gracefully; never break layout

### Error Recovery Paths
Every error needs a clear path back to success:

- Show the problematic input highlighted
- Explain why it's wrong in plain language (not error codes)
- Suggest the fix ("Missing area code — did you mean 415?")
- Preserve all other user inputs
- Offer a shortcut to complete the action ("Resend with corrected email?")

---

## Content Design Essentials

### Microcopy Rules (Quick Reference)
When you're making UX decisions that involve copy:

- **Button labels:** Name the outcome, not the action ("Save Changes" not "Submit")
- **Error messages:** What happened + why + what now ("Password must contain a number. Try again?")
- **Empty states:** Explain why it's empty AND what to do ("No projects yet. Start by creating one")
- **Confirmations:** Name both actions specifically ("Keep draft" / "Delete draft" not "Cancel" / "OK")
- **Tone:** Match emotional state (calm for errors, brief for success, encouraging for progress)

For full microcopy work—writing error messages, onboarding copy, button labels, tooltips, or doing a copy audit—hand off to **ux-copywriter** skill.

---

## Validation and Testing Methods

### Suggest What to Test (Always Proactive)

After designing or reviewing, offer specific validation:

- "I'd test this with a first-time user to see if they understand [specific concern]"
- "The riskiest assumption is [X] — here's how to validate cheaply"
- "Watch for users getting stuck at [point] — if they do, try [alternative]"

### Quick Validation Methods

**5-second test:** Show the screen for 5 seconds, ask what they remember
- Validates visual hierarchy and information scent
- Reveals if the most important element stands out
- Cheap, fast, requires only 1-2 people

**Task completion:** Give someone a real goal, watch if they achieve it
- "Find and buy a blue item under $20"
- Reveals friction points and unexpected paths
- Most realistic; takes 15-30 minutes per person

**Think-aloud:** Watch someone use it while narrating their thoughts
- Reveals mental models and assumptions
- Exposes confusing moments in real time
- Requires careful observation, not interruption

**A/B test:** When you can't decide between two approaches, test both
- "Option A: three buttons side-by-side. Option B: stacked vertically"
- Quantifies which works better at scale
- Best for decisions with measurable impact (clicks, completion rate)

### Accessibility Validation

Beyond WCAG checklist:
- **Keyboard-only test:** Navigate the entire flow using only Tab and Enter
- **Screen reader:** Use NVDA or JAWS; read through in context
- **Color contrast:** Use axe DevTools; verify 4.5:1 for body text, 3:1 for large text
- **Motion:** Toggle `prefers-reduced-motion`; ensure experience is complete without animation
- **Zoom:** Enlarge to 200%; ensure no horizontal scroll or broken layout

---

## Working Across Tools

### In Figma
- Use **real content,** not Lorem ipsum — content determines layout
- Design **all states:** default, hover, active, disabled, loading, error, success, empty
- Think in **flows, not screens** — connect states with arrows
- Create **component variants** for each state
- Use **auto-layout** to reveal responsive behavior

### In Code
- Test with **real data** and **edge cases** — what if the name is 50 characters? What if the list has 5,000 items?
- Test on **slow connections** — show skeleton screens, not spinners
- Responsive means **the experience is good at every size,** not just "it fits"
- Test **with keyboard only** and a **screen reader**
- Measure **Core Web Vitals** — LCP, FID, CLS impact user perception

### When Researching
- Use **WebSearch** to find how top products solve similar problems
- Look for **cross-industry inspiration,** not just direct competitors
- Extract **principles,** not screens — apply the concept to your context
- Study both **successful patterns** and **failed experiments**

---

## Common Mistakes to Avoid

- Making users scroll to find critical info (especially CTAs and pricing)
- Using color alone to convey meaning (red for error, green for success — add text too)
- Hidden navigation more than one level deep (causes disorientation)
- No loading state (silence = broken)
- Hover-only functionality (mobile breaks; keyboard can't access)
- Unclear errors ("Error 500" instead of "Something went wrong. Try again in a moment.")
- Default bias misused (defaulting to premium tier or surprise costs)
- Too much choice in first flow (choice paralysis kills conversion)
- Skipping empty and error states (these are where users judge competence)

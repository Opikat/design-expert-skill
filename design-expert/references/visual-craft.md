# Visual Craft Deep Dive

Complete component specifications, animation patterns, design principles, and polish techniques. Reference for pixel-perfect guidance beyond the SKILL.md essentials.

---

## Component Specifications & Anatomy

### Tables & Data Display

**Structure:**
- Left-align text columns, right-align number columns
- Header row: sticky with slightly heavier weight or subtle background
- Row height: 40-52px for comfortable scanning
- Hover state on rows for scannability
- Zebra striping OR subtle borders — never both
- Sortable columns: clear directional arrow indicators (▲ ▼)
- Empty state: centered message with primary action
- Column widths: consistent, avoid columns that jump when data changes

**Spacing:**
- Cell padding: 12-16px
- Gap between columns: included in cell padding
- Sticky header: use box-shadow or border-bottom, not margin

### Navigation Components

**Top Nav:**
- Height: 48-64px (larger on desktop, can compress mobile)
- Logo on left, primary nav center or left, actions/profile right
- Active state: bold weight + underline or filled background
- Mobile: collapse to hamburger menu at breakpoint

**Sidebar:**
- Width: 240-280px expanded, 64-72px collapsed (icon-only)
- Section headers for grouping (uppercase, smaller text-sm)
- Active state: background fill + left border accent OR weight change
- Icons: 20-24px, consistent stroke weight across entire set
- Collapse trigger: chevron or hamburger, clearly visible
- Hover: subtle background highlight on nav items

**Tabs:**
- Bottom tabs on mobile, max 5 items
- Active tab: fill change (solid background) + label weight increase
- Inactive tabs: border-bottom or text color change
- Badge dots for notifications (positioned top-right on icon)
- Swipeable content on mobile tab views

### Modals & Dialogs

**Sizing:**
| Type | Max Width | Use |
|------|-----------|-----|
| Confirmation | 400px | Delete, destructive, one decision |
| Form/Settings | 480px | Short forms, login, settings |
| Content/Article | 640px | Articles, previews, full content |
| Complex | 960px | Multi-step flows, dashboards, wizards |

**Anatomy:**
- Overlay: `rgba(0,0,0,0.4)` to `rgba(0,0,0,0.6)` — test at night
- Padding: 24-32px (larger padding = breathing room)
- Close button: top-right, always visible, no hover delay
- Title: heading weight, 20-24px
- Body: text-base, max-width 65 chars for readability
- Actions: bottom-right, primary action rightmost (visual end point)
- Focus trap: Tab cycles within modal only, Escape closes
- Enter animation: 250-300ms ease-out (scale 0.95 + opacity)
- Exit animation: 200ms ease-in
- Click backdrop to close (except destructive modals)

### Forms Anatomy

**Label-to-Input Structure:**
- Label above input (top-aligned = fastest form completion)
- Label: text-sm, medium weight, 12px
- Gap: 4-6px (label-to-input)
- Between fields: 16-24px (MUST exceed label-to-input gap)
- Placeholder: format hints only, never the label
- Helper text: 12px, lighter color, below input
- Error messages: red, with icon, replaces helper text

**Input States Table:**
| State | Border | Background | Text |
|-------|--------|-----------|------|
| Default | --gray-300 | white | --gray-700 |
| Hover | --gray-400 | white | --gray-700 |
| Focus | --brand-500 + ring | white | --gray-700 |
| Filled | --gray-300 | white | --gray-700 |
| Error | --red-500 | --red-50 | --red-900 |
| Disabled | --gray-200 | --gray-100 | --gray-400 |

---

## Polish Techniques (Code Reference)

### 1. Staggered Animations
```css
.card:nth-child(1) { animation-delay: 0ms; }
.card:nth-child(2) { animation-delay: 60ms; }
.card:nth-child(3) { animation-delay: 120ms; }
.card:nth-child(n) { animation-delay: calc((n-1) * 60ms); }
```

### 2. Colored Shadows
Tint shadows with element's background color for depth:
```css
.card-blue {
  background: #3B82F6;
  box-shadow: 0 8px 24px rgba(59, 130, 246, 0.25);
}
.card-purple {
  background: #A855F7;
  box-shadow: 0 8px 24px rgba(168, 85, 247, 0.25);
}
```

### 3. Backdrop Blur on Sticky Elements
Frosted-glass effect for nav bars and overlays:
```css
.sticky-nav {
  backdrop-filter: blur(12px) saturate(180%);
  background: rgba(255, 255, 255, 0.8);
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
}
```

### 4. Dark Mode Border Light Effect
1px semi-transparent white border creates depth:
```css
.card-dark {
  background: --dark-surface-1;
  border: 1px solid rgba(255, 255, 255, 0.06);
}
.card-dark:hover {
  border-color: rgba(255, 255, 255, 0.1);
}
```

### 5. Micro-Gradients on Buttons
Subtle top-to-bottom for physicality:
```css
.btn-primary {
  background: linear-gradient(
    180deg,
    hsl(220 80% 52%) 0%,
    hsl(220 80% 48%) 100%
  );
}
```

### 6. Inner Shadows for Inputs
Recessed feel on text fields:
```css
.input {
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.06);
}
.input:focus {
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.06),
              0 0 0 3px rgba(59, 130, 246, 0.1);
}
```

### 7. Subtle Texture
Barely-visible noise prevents flat CSS feel:
```css
.surface {
  background-image:
    radial-gradient(circle at 1px 1px, rgba(0,0,0,0.03), transparent 1px);
  background-size: 4px 4px;
}
```

### 8. Gradient Text (Hero Only)
```css
.hero-heading {
  background: linear-gradient(135deg, #6366F1, #EC4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

---

## Animation Timing & Easing

### Easing Functions (CSS)
```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);      /* entering */
  --ease-in: cubic-bezier(0.7, 0, 0.84, 0);       /* exiting */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);  /* repositioning */
  --spring: cubic-bezier(0.34, 1.56, 0.64, 1);    /* bounce */
}
```

### Timing Guide
- Micro-interactions (button press): 100-150ms
- Card hover/lift: 150-200ms
- Panels opening: 200-300ms
- Page transitions: 300-500ms
- Modal enter: 250-300ms ease-out
- Modal exit: 200ms ease-in
- **Rule:** Closing is always faster than opening

### Animation Patterns
```css
/* Card hover lift */
.card { transition: transform 200ms var(--ease-out); }
.card:hover { transform: translateY(-2px); }

/* Modal enter */
@keyframes modal-in {
  from { opacity: 0; transform: scale(0.95) translateY(8px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

/* Skeleton shimmer (linear only) */
@keyframes shimmer {
  from { background-position: -200% 0; }
  to { background-position: 200% 0; }
}
.skeleton {
  animation: shimmer 1.5s linear infinite;
}

/* Fade in up */
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}
```

---

## Design Principles Reference

### Linear (Restraint)
Every element earns its place. If removing it doesn't hurt, remove it.
- Monochrome + one accent = instant sophistication
- Density + ruthless reduction = premium feel
- Apply: Use restrained color palette, remove visual noise

### Stripe (Clarity)
One hero per view. Typography does 80% of the work.
- Hierarchy through weight and size, not decoration
- Complex products need exceptionally clear navigation
- Apply: Strong type scale, minimal color, clean layout

### Vercel (Functional Minimalism)
Remove friction, not features. Speed IS design.
- High contrast with minimal color is a choice, not laziness
- Fast response feedback is visual craft
- Apply: Clean interfaces, instant feedback, purposeful contrast

### Apple (Platform Craft)
Respect platform conventions. Consistent spacing creates unconscious trust.
- Transitions mirror real physics
- Precision in every detail
- Apply: Proper spacing rhythm, polished animations, attention to edges

---

## Dark Mode Implementation

**Don't invert — design a separate palette.**

**Color Desaturation:**
Saturated colors vibrate on dark backgrounds. Desaturate primary colors 10-15%.
```
Light: hsl(220 80% 50%)  →  Dark: hsl(220 70% 50%)
```

**Elevation Strategy:**
Opposite of light mode. Darker background = elements are pushed back.
- Darkest furthest back (--dark-bg)
- Lighter surfaces forward (--dark-surface-1 → 2 → 3)
- Use color elevation, not shadows

**Text & Borders:**
- Text: #E5E5E5 to #F5F5F5, never pure white
- Primary borders: `rgba(255,255,255,0.08)`
- Hover borders: `rgba(255,255,255,0.12)`
- Secondary text: #A3A3A3

**Testing:**
- Test at night in a dim room — that's when dark mode actually matters
- Check contrast on actual devices, not monitors
- Verify no harsh edges or vibrating colors

---

## Working Across Tools

**Figma:**
- Inspect spacing with Figma's measurement tools
- Validate design tokens match implementation
- Check component consistency across variants
- Use auto-layout for responsive intent verification

**Code (CSS):**
- Use CSS custom properties for ALL tokens
- Test with real content (long names, missing images, edge cases)
- Animate ONLY `transform` and `opacity` (GPU-accelerated)
- Never animate `width`, `height`, `top`, `left`

**Icon Systems:**
- Same stroke weight across entire set (1.5px or 2px)
- Same corner treatment (rounded or sharp — pick one)
- Same optical size (if 24px grid, icons fill ~20px)
- Pixel-snap to whole values at common render sizes

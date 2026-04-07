# Component Library

Specifications for common UI components. Read when building, reviewing,
or standardizing component design.

---

## Component Height Scale

Buttons and inputs MUST share the same heights. This is non-negotiable.

| Size | Height | Use |
|---|---|---|
| XS | 28px | Dense UIs, table actions, tags |
| SM | 32px | Secondary actions, compact forms |
| MD | 36-40px | Default for most interfaces |
| LG | 44-48px | Primary CTAs, mobile touch targets |
| XL | 56px | Hero CTAs, landing pages |

Horizontal padding on buttons = 2× vertical padding.

---

## Buttons

### States (ALL required)
- **Default:** base appearance
- **Hover:** subtle lift, lighter shade, or border change
- **Active/Pressed:** slightly darker, pressed-in feel
- **Focus:** visible focus ring (2px offset, brand or blue)
- **Disabled:** reduced opacity (0.5), no pointer events
- **Loading:** spinner replaces label, same dimensions

### Hierarchy
1. **Primary:** solid fill, high contrast — ONE per section
2. **Secondary:** outline or subtle fill
3. **Tertiary/Ghost:** text-only or minimal background
4. **Destructive:** red variant of primary hierarchy

### Icon Placement
- Leading (left): adds meaning ("+ New", "🔍 Search")
- Trailing (right): indicates behavior ("→", "↗", "▾")
- Icon-only: MUST have `aria-label` and tooltip on hover

---

## Inputs

### Anatomy
- Label above input (top-aligned = fastest completion)
- Label-to-input gap: 4-6px
- Between form fields: 16-24px (MUST exceed label-to-input gap)
- Placeholder: format hint only, never the label
- Helper text: below input, lighter color

### States
- **Default:** subtle border (gray-300)
- **Hover:** border darkens slightly
- **Focus:** brand color border + ring (2px)
- **Filled:** same as default with value
- **Error:** red border + icon + message replacing helper text
- **Disabled:** reduced opacity, no interaction

### Heights
Must match button heights in the same size class. A 40px button next to a
40px input must feel like one unit.

---

## Cards

### Rules
- Consistent padding across all cards in the same view (16-24px)
- Gap between cards > padding inside cards
- Single clear purpose per card
- Actions at bottom or in header, never scattered
- Hover: subtle shadow elevation or border change
- Click target: entire card if it's navigational

### Anatomy
```
┌─────────────────────────┐
│  Image/Media (optional) │
├─────────────────────────┤
│  Eyebrow / Category     │  ← text-sm, secondary color
│  Title                  │  ← text-lg, font-weight-600
│  Description            │  ← text-base, text-secondary
│                         │
│  [Action]    [Action]   │  ← bottom-aligned
└─────────────────────────┘
```

---

## Tables

- Left-align text, right-align numbers
- Header row: sticky, slightly heavier weight or background
- Row height: 40-52px for comfortable scanning
- Hover state on rows for scannability
- Zebra striping OR borders, never both
- Sortable columns: clear directional arrow
- Empty state: centered message with action

---

## Navigation

### Top Nav
- Height: 48-64px
- Logo left, nav center or left, actions right
- Active state: bold weight + underline or background
- Mobile: collapse to hamburger at `--bp-md`

### Sidebar
- Width: 240-280px expanded, 64-72px collapsed
- Section headers for grouping
- Active state: background + left border or weight change
- Icons: 20-24px, consistent stroke weight
- Collapse trigger: clearly visible

### Tabs
- Bottom tabs on mobile: max 5 items
- Active tab: fill change + label weight
- Badge dots for notifications
- Swipeable content in mobile tab views

---

## Modals

| Type | Max Width | Use |
|---|---|---|
| Confirmation | 400px | Delete, destructive actions |
| Form | 480px | Short forms, settings |
| Content | 640px | Articles, previews |
| Complex | 960px | Multi-step, dashboards |

### Rules
- Overlay: `rgba(0,0,0,0.4)` to `rgba(0,0,0,0.6)`
- Padding: 24-32px
- Close: top-right corner, always visible
- Actions: bottom-right, primary on the right
- Focus trap: Tab cycles within modal only
- Escape key closes
- Enter: 250-300ms ease-out, exit: 200ms ease-in
- Click backdrop to close (non-destructive modals only)

---

## Tooltips

- Max width: 240px
- Padding: 8px 12px
- Delay: 300-500ms before showing
- Position: auto-flip to stay in viewport
- Arrow pointing to trigger element
- Dark background, light text (or inverse in dark mode)

---

## Badges & Tags

- Height: 20-24px (inline with text)
- Padding: 4px 8px
- Border-radius: full (pill) or match component system
- Semantic colors: blue/info, green/success, yellow/warning, red/error
- Text: 11-12px, medium weight
- Removable tags: include × icon with hover state

---

## Toast / Notifications

- Position: top-right or bottom-center
- Width: 320-400px
- Auto-dismiss: 5-8 seconds for info, never for errors
- Stack from newest on top
- Include close button
- Action link when relevant ("Undo", "View")
- Semantic border or icon (not just color)

# Polish and Craft

Bans in SKILL.md Step 4 win over any value in this file.

Advanced visual techniques, animation patterns, and responsive details.
Read when elevating an interface from functional to polished.

---

## The Details That Separate Good from Great

### 1. Staggered Animations
Multiple elements appearing together should stagger by 50-80ms:
```css
.card:nth-child(1) { animation-delay: 0ms; }
.card:nth-child(2) { animation-delay: 60ms; }
.card:nth-child(3) { animation-delay: 120ms; }
```

### 2. Colored Shadows
Tint shadows with the element's color for depth that feels real:
```css
.card-blue {
  background: #3B82F6;
  box-shadow: 0 8px 24px rgba(59, 130, 246, 0.25);
}
```

### 3. Background Texture (only when derived)
Texture is permitted only as a deliberate, profile-approved choice sourced from
the product's own material world (SKILL.md Step 2) — a ruled grid for a
technical product, a paper fibre for a print-heritage one. No recipe here: the
2–5% film-grain / noise overlay is a banned default (SKILL.md Step 4).

### 4. Border Light Effect (Dark Mode)
1px semi-transparent white border adds definition:
```css
.card-dark {
  border: 1px solid rgba(255, 255, 255, 0.06);
}
.card-dark:hover {
  border-color: rgba(255, 255, 255, 0.1);
}
```

### 5. Micro-Gradients on Buttons
Subtle top-to-bottom gradient adds physicality:
```css
.btn-primary {
  background: linear-gradient(
    180deg,
    hsl(220 80% 52%) 0%,    /* slightly lighter */
    hsl(220 80% 48%) 100%   /* slightly darker */
  );
}
```

### 6. Backdrop Blur
Frosted-glass effect for sticky navs and overlays:
```css
.sticky-nav {
  backdrop-filter: blur(12px) saturate(180%);
  background: rgba(255, 255, 255, 0.8);
}
```

### 7. Inner Shadows for Inputs
Recessed feel on text fields:
```css
.input {
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.06);
}
```

### 8. Gradient Text (Sparingly)
For hero headings only, with stops from the product's own palette (the default
indigo→pink `#6366F1 → #EC4899` is banned — Step 4):
```css
.hero-heading {
  background: linear-gradient(135deg, var(--accent-700), var(--accent-500));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

---

## Animation CSS Reference

### Easing Functions
```css
:root {
  --ease-out: cubic-bezier(0.2, 0, 0, 1);         /* entering — example; derive per direction (the default `cubic-bezier(0.16, 1, 0.3, 1)` is banned — Step 4) */
  --ease-in: cubic-bezier(0.7, 0, 0.84, 0);        /* exiting */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);   /* repositioning */
  --spring: cubic-bezier(0.34, 1.56, 0.64, 1);     /* playful bounce */
}
```

### Common Transitions
```css
/* Button interactions */
.btn { transition: transform 120ms var(--ease-out),
                   background-color 120ms var(--ease-out); } /* name properties; never `all` */

/* Card hover */
.card { transition: transform 200ms var(--ease-out),
                    box-shadow 200ms var(--ease-out); }
.card:hover { transform: translateY(-2px); }

/* Modal enter */
@keyframes modal-in {
  from { opacity: 0; transform: scale(0.95) translateY(8px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
.modal { animation: modal-in 250ms var(--ease-out); }

/* Content entrance: opacity only. A 12-16px rise is the banned measured
   default (SKILL.md Step 4, Motion row). If the element needs travel, take it
   from where it will act: Counter-entry in motion-patterns.md. */
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Skeleton shimmer */
@keyframes shimmer {
  from { background-position: -200% 0; }
  to { background-position: 200% 0; }
}
.skeleton {
  background: linear-gradient(90deg,
    var(--gray-200) 25%, var(--gray-100) 50%, var(--gray-200) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s linear infinite;
}
```

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Additional Motion Recipes

Interface-motion craft for components (press, popover, tooltip, toast,
drawer, tabs). Durations and the enter/exit easing rule stay as in SKILL.md
Step 12; element choice stays in [motion-patterns.md](motion-patterns.md).

### Should it animate at all — frequency first

| How often the user sees it | Decision |
|---|---|
| 100+ times a day (keyboard shortcuts, command-palette toggle) | No animation |
| Tens of times a day (hover effects, list navigation) | Remove or cut to a minimum |
| Occasionally (modals, drawers, toasts) | Standard animation |
| Rarely / first time (onboarding, celebrations) | Room for delight |

Never animate keyboard-initiated actions: they repeat hundreds of times a day,
and animation makes them feel delayed.

### Named curves (pick per direction; none is a default)

```css
--ease-in-out-strong: cubic-bezier(0.77, 0, 0.175, 1); /* on-screen movement, stronger than the built-in */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);         /* iOS-like sheet / drawer */
```

The built-in CSS keywords are weak; tune curves with easing.dev or
easings.co rather than inventing them.

### Press, origin, entry

- **Press feedback:** `transform: scale(0.97)` on `:active`, `transition:
  transform 160ms ease-out`. Keep it within 0.95–0.98 on the web.
- **Never enter from `scale(0)`.** Start at `scale(0.95)` with `opacity: 0`;
  nothing real appears from nothing.
- **Origin-aware popovers:** scale from the trigger, not the centre —
  `transform-origin: var(--radix-popover-content-transform-origin)` (Radix)
  or `var(--transform-origin)` (Base UI). Modals are the exception: they are
  not anchored to a trigger and stay centred.
- **Tooltips:** delay the first one; once one is open, adjacent tooltips open
  instantly with no animation (`transition-duration: 0ms` on a `data-instant`
  state). The toolbar feels faster without losing the accidental-hover guard.
- **Entry without JS:** `@starting-style { opacity: 0; transform:
  translateY(100%); }` inside the element's rule replaces the
  `useEffect → mounted` pattern; keep the `data-mounted` fallback where
  support is missing.

### Interruptible by default

- **Transitions over keyframes for anything triggered rapidly** (toasts,
  toggles): a transition retargets from its current value; a keyframe
  animation restarts from zero.
- **Springs for gestures and pointer-tracking:** they keep velocity when
  interrupted. Web (Motion): `{ type: "spring", duration: 0.5, bounce: 0.2 }`;
  keep bounce 0.1–0.3 and out of most routine UI. Smooth decorative
  mouse-tracking with `useSpring(value, { stiffness: 100, damping: 10 })`
  instead of binding it raw; functional readouts should not spring at all.
- **Blur to bridge a crossfade** that still reads as two objects swapping:
  `filter: blur(2px)` during the transition, never above 20px (expensive,
  especially in Safari).

### Transform and clip-path recipes

- **`translateY(100%)` moves an element by its own height** — hide a drawer
  or stack a toast without knowing its size. Prefer percentages to pixels.
- **`scale()` scales children too** (text, icons) — intended for press states.
- **`clip-path: inset(t r b l)`** animates on the compositor and needs no
  extra DOM:
  - *Reveal:* `inset(0 100% 0 0)` → `inset(0 0 0 0)`.
  - *Tabs with exact colour transitions:* duplicate the tab list, style the
    copy as active, clip it to the active tab, animate the clip on change.
  - *Hold-to-delete:* coloured overlay clipped to `inset(0 100% 0 0)`; on
    `:active` transition to `inset(0 0 0 0)` over 2s `linear`; on release
    snap back in 200ms ease-out; add the press scale. Slow where the user
    decides, fast where the system responds.
  - *Image reveal on scroll:* `inset(0 0 100% 0)` → `inset(0 0 0 0)` when the
    element enters the viewport (`IntersectionObserver`, once).
  - *Comparison slider:* clip the top image with `inset(0 50% 0 0)` and drive
    the right inset from the drag position.

### Gestures and drag

- **Dismiss on velocity, not only distance:** `velocity = |distance| /
  elapsedMs`; dismiss when it exceeds ~0.11 even below the distance
  threshold. A flick should be enough.
- **Damping and friction at boundaries** instead of hard stops — the further
  past the edge, the less the element moves.
- **Pointer capture** once a drag starts, so it continues outside the bounds.
- **Ignore extra touch points** after the drag begins, or the element jumps
  when fingers switch.

### Performance under load

- **Do not drive per-frame motion through an inherited CSS variable** on a
  container (`--swipe-amount`): every child recalculates styles. Set
  `transform` on the element itself.
- **Motion (Framer Motion) `x` / `y` / `scale` shorthands run on the main
  thread** and drop frames while the page loads; pass a full `transform`
  string for hardware acceleration.
- **CSS animations beat JS under load** (they run off the main thread). Use
  CSS for predetermined motion, JS for dynamic and interruptible motion, and
  the Web Animations API (`element.animate(...)`) when JS needs control with
  CSS performance.

### Accessibility nuances

- Reduced motion means fewer and gentler, not necessarily zero: keep opacity
  and colour transitions that aid comprehension, drop movement and position.
- Gate hover motion behind `@media (hover: hover) and (pointer: fine)` —
  touch devices fire hover on tap.

### Invisible edge cases and debugging

- Pause toast timers while the tab is hidden; fill gaps between stacked items
  with pseudo-elements so hover state does not flicker.
- Debug at 2–5× duration or frame by frame (DevTools Animations panel):
  check that colours blend rather than overlap, the origin is right, and
  opacity / transform / colour stay in sync.
- Test gestures on a real device (local dev server by IP + remote devtools),
  and re-watch motion the next day with fresh eyes.

### Quick review checks

| Issue | Fix |
|---|---|
| `transition: all` | Name the properties |
| `scale(0)` entry | `scale(0.95)` + `opacity: 0` |
| Popover scales from centre | Trigger origin (modals exempt) |
| Animation on a keyboard action | Remove it |
| Hover motion without a media query | `@media (hover: hover) and (pointer: fine)` |
| Keyframes on a rapidly triggered element | Transition instead |
| Motion `x`/`y` under load | Full `transform` string |

---

## Responsive Patterns

### Mobile-First Component Adjustments

| Component | Mobile | Tablet | Desktop |
|---|---|---|---|
| Nav | Bottom tabs or hamburger | Top nav, simplified | Full top nav + sidebar |
| Buttons | Full width, 48px height | Auto width, 40px | Auto width, 36-40px |
| Cards | Single column, full width | 2 columns | 3-4 columns |
| Tables | Card view or horizontal scroll | Visible with scroll | Full table |
| Modals | Full screen (sheet) | Centered, 480px max | Centered, type-based |
| Forms | Single column, large targets | Single or two column | Two column for long forms |
| Typography | Base 16px | Base 16px | Base 16px (scale up headings) |

### Touch Target Rules
- Minimum: 44×44px (Apple HIG) / 48×48dp (Material)
- Comfortable: 48×48px
- Space between targets: at least 8px
- Bottom of screen = easiest thumb reach
- Top corners = hardest thumb reach

### Viewport Tricks
```css
/* Proper mobile viewport height (accounts for browser chrome) */
.full-height { height: 100dvh; }

/* Safe area for notched phones */
.container {
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
  padding-bottom: env(safe-area-inset-bottom);
}
```

---

## Color Accessibility Quick Reference

| Element | Minimum Contrast | Standard |
|---|---|---|
| Body text | 4.5:1 | WCAG AA |
| Large text (18px+ bold, 24px+) | 3:1 | WCAG AA |
| UI components (borders, icons) | 3:1 | WCAG AA |
| Body text (enhanced) | 7:1 | WCAG AAA |

**Testing tools:**
- Chrome DevTools → Inspect → Color picker shows contrast ratio
- WebAIM Contrast Checker
- Stark (Figma plugin)

**Rule:** Never use color alone to convey meaning. Always pair with icon,
text, pattern, or position.

---

## Icon Consistency Checklist

- Same stroke weight across the entire set (1.5px or 2px)
- Same corner treatment (rounded or sharp — pick one)
- Same optical size (if 24px grid, icons fill ~20px)
- Consistent level of detail (don't mix simple and complex)
- Pixel-snap to whole values at common sizes
- Test at smallest rendered size to verify clarity

---

## Mobile / React Native Patterns

Native mobile needs different primitives than web: spring physics replace
CSS easing, press feedback uses `scale` + haptics, and animation runs on
the UI thread via Reanimated shared values. These patterns complement the
CSS animation reference above — not replace it.

### Spring Configs (Reanimated `withSpring`)

```ts
// Standard — buttons, cards, most UI motion
const SPRING_STANDARD = { mass: 1, damping: 15, stiffness: 120 };

// Modal / sheet enter — softer, slower settle
const SPRING_MODAL = { mass: 1, damping: 20, stiffness: 90 };

// Bouncy — celebratory moments only, never for routine UI
const SPRING_BOUNCY = { mass: 1, damping: 10, stiffness: 180 };
```

### Press-Scale Values

| Scale | Feel | Use for |
|---|---|---|
| `0.97` | Subtle | Icon buttons, list rows |
| `0.96` | Standard | Primary CTAs, cards |
| `0.95` | Tactile | Large hero buttons, playful UI |

Pattern: `onPressIn` → `scale` target, `onPressOut` → spring back to `1.0`
with `SPRING_STANDARD`. Never animate below `0.93` — reads as broken.

### Haptics Map (`expo-haptics`)

| Trigger | Haptic |
|---|---|
| Toggle, selection change | `Haptics.selectionAsync()` |
| Secondary tap, tab switch | `Haptics.impactAsync(Light)` |
| Primary CTA, confirm | `Haptics.impactAsync(Medium)` |
| Success completion | `Haptics.notificationAsync(Success)` |
| Destructive action confirmed | `Haptics.notificationAsync(Warning)` |

Rule: fire haptic on `onPressIn`, not `onPress` — matches the visual scale.
Respect system-level haptics-off setting; never make haptic the only feedback.

### Reanimated Press Idiom

```tsx
const scale = useSharedValue(1);
const animStyle = useAnimatedStyle(() => ({
  transform: [{ scale: scale.value }],
}));

<Pressable
  onPressIn={() => { scale.value = withSpring(0.96, SPRING_STANDARD);
                     Haptics.impactAsync(ImpactFeedbackStyle.Light); }}
  onPressOut={() => { scale.value = withSpring(1, SPRING_STANDARD); }}>
  <Animated.View style={animStyle}>{/* ... */}</Animated.View>
</Pressable>
```

### Neo-Brutalist Mechanical Press (NativeWind / Tailwind)

No spring — offset shifts and shadow collapses for a mechanical thunk:
```tsx
className="shadow-[4px_4px_0_0_#000]
           active:translate-x-[2px] active:translate-y-[2px]
           active:shadow-none transition-none"
```

### Platform Notes

- Web's `--ease-out` ≈ `SPRING_STANDARD` — use web easing for timing-based transitions (opacity, color), spring for spatial ones (scale, translate).
- Never animate `width`/`height` on native either — use `scale` or `flex`.
- Respect `AccessibilityInfo.isReduceMotionEnabled()` — fall back to opacity-only.

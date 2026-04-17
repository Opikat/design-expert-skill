# Polish and Craft

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

### 3. Subtle Background Texture
Barely-visible noise prevents the "flat CSS" feel:
```css
.surface {
  background-image: url("data:image/svg+xml,..."); /* noise pattern */
  background-size: 200px;
  opacity: 0.03;
}
```

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
For hero headings only:
```css
.hero-heading {
  background: linear-gradient(135deg, #6366F1, #EC4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

---

## Animation CSS Reference

### Easing Functions
```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);      /* entering */
  --ease-in: cubic-bezier(0.7, 0, 0.84, 0);        /* exiting */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);   /* repositioning */
  --spring: cubic-bezier(0.34, 1.56, 0.64, 1);     /* playful bounce */
}
```

### Common Transitions
```css
/* Button interactions */
.btn { transition: all 120ms var(--ease-out); }

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

/* Fade in up (for page content) */
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
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

- Web's `cubic-bezier(0.16, 1, 0.3, 1)` ≈ `SPRING_STANDARD` — use web easing for timing-based transitions (opacity, color), spring for spatial ones (scale, translate).
- Never animate `width`/`height` on native either — use `scale` or `flex`.
- Respect `AccessibilityInfo.isReduceMotionEnabled()` — fall back to opacity-only.

---

## Icon Consistency Checklist

- Same stroke weight across the entire set (1.5px or 2px)
- Same corner treatment (rounded or sharp — pick one)
- Same optical size (if 24px grid, icons fill ~20px)
- Consistent level of detail (don't mix simple and complex)
- Pixel-snap to whole values at common sizes
- Test at smallest rendered size to verify clarity

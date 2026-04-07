# Design Tokens

Complete token scales for spacing, color, typography, shadows, and radii.
Read when establishing or auditing a visual design system.

---

## Spacing Scale (8pt Grid)

```css
--space-0: 0px;
--space-1: 4px;    /* fine-tuning inside components */
--space-2: 8px;    /* tight spacing, icon gaps */
--space-3: 12px;   /* label-to-input gap */
--space-4: 16px;   /* default internal padding */
--space-5: 20px;   /* compact section spacing */
--space-6: 24px;   /* card padding, form field gaps */
--space-7: 32px;   /* section spacing */
--space-8: 40px;   /* large section gaps */
--space-9: 48px;   /* section dividers */
--space-10: 64px;  /* page section spacing */
--space-11: 80px;  /* hero spacing */
--space-12: 96px;  /* major page divisions */
--space-13: 128px; /* page-level whitespace */
```

**Rule:** Internal spacing ≤ external spacing. Always.

---

## Neutral Color Scales

### Light Mode
```css
--gray-50: #FAFAFA;   /* page background */
--gray-100: #F5F5F5;  /* subtle backgrounds */
--gray-200: #E5E5E5;  /* borders, dividers */
--gray-300: #D4D4D4;  /* disabled elements */
--gray-400: #A3A3A3;  /* placeholder text */
--gray-500: #737373;  /* secondary text */
--gray-600: #525252;  /* icons */
--gray-700: #404040;  /* body text */
--gray-800: #262626;  /* headings */
--gray-900: #171717;  /* primary text */
--gray-950: #0A0A0A;  /* high emphasis */
```

### Dark Mode
```css
--dark-bg: #0A0A0A;         /* deepest background */
--dark-surface-1: #141414;  /* card backgrounds */
--dark-surface-2: #1E1E1E;  /* raised surfaces */
--dark-surface-3: #282828;  /* highest elevation */
--dark-border: rgba(255,255,255,0.08);  /* subtle borders */
--dark-border-hover: rgba(255,255,255,0.12);
--dark-text-primary: #F5F5F5;
--dark-text-secondary: #A3A3A3;
--dark-text-tertiary: #737373;
```

**Dark mode rules:**
- Elevation = lighter surfaces (not shadows)
- Desaturate primary colors 10-15%
- Never pure white text — use #E5E5E5 to #F5F5F5
- Borders use semi-transparent white, not solid grays
- Test at night in a dim room

---

## Type Scales

### Minor Third (1.200) — Balanced, most web apps
```css
--text-xs: 0.694rem;   /* 11.1px — captions, badges */
--text-sm: 0.833rem;   /* 13.3px — labels, helper text */
--text-base: 1rem;     /* 16px — body text */
--text-lg: 1.2rem;     /* 19.2px — subheadings */
--text-xl: 1.44rem;    /* 23px — section headings */
--text-2xl: 1.728rem;  /* 27.6px — page headings */
--text-3xl: 2.074rem;  /* 33.2px — hero headings */
```

### Major Third (1.250) — Marketing, editorial
```css
--text-xs: 0.64rem;    /* 10.2px */
--text-sm: 0.8rem;     /* 12.8px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.25rem;    /* 20px */
--text-xl: 1.563rem;   /* 25px */
--text-2xl: 1.953rem;  /* 31.3px */
--text-3xl: 2.441rem;  /* 39.1px */
```

### Line Heights
```css
--leading-tight: 1.15;   /* large headings */
--leading-snug: 1.3;     /* small headings, labels */
--leading-normal: 1.5;   /* body text */
--leading-relaxed: 1.625; /* long-form reading */
```

### Letter Spacing
```css
--tracking-tighter: -0.04em;  /* large headings (32px+) */
--tracking-tight: -0.02em;    /* medium headings */
--tracking-normal: 0;          /* body text */
--tracking-wide: 0.025em;     /* small labels */
--tracking-wider: 0.05em;     /* ALL CAPS text */
--tracking-widest: 0.1em;     /* CAPS small labels */
```

---

## Shadow Scale

### Light Mode
```css
--shadow-xs: 0 1px 2px rgba(0,0,0,0.04);
--shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
--shadow-md: 0 4px 6px rgba(0,0,0,0.06), 0 2px 4px rgba(0,0,0,0.04);
--shadow-lg: 0 10px 15px rgba(0,0,0,0.06), 0 4px 6px rgba(0,0,0,0.04);
--shadow-xl: 0 20px 25px rgba(0,0,0,0.08), 0 8px 10px rgba(0,0,0,0.04);
```

**Hover states:** rise one level (xs → sm, sm → md)

### Dark Mode
Use surface color elevation instead of shadows:
- Resting: `--dark-surface-1`
- Hover: `--dark-surface-2`
- Active/modal: `--dark-surface-3`
- Add subtle `border: 1px solid rgba(255,255,255,0.06)` for definition

---

## Border Radius

Pick one style and commit across the entire product:

```css
/* Sharp (professional, editorial) */
--radius-sm: 2px;
--radius-md: 4px;
--radius-lg: 6px;
--radius-full: 9999px;

/* Medium (modern SaaS) */
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-full: 9999px;

/* Round (playful, consumer) */
--radius-sm: 8px;
--radius-md: 12px;
--radius-lg: 16px;
--radius-full: 9999px;
```

**Rule:** Nested elements have SMALLER radius than parent.
Formula: `child-radius = parent-radius - padding`

---

## Responsive Breakpoints

```css
--bp-sm: 640px;    /* mobile landscape */
--bp-md: 768px;    /* tablet portrait */
--bp-lg: 1024px;   /* tablet landscape / small desktop */
--bp-xl: 1280px;   /* desktop */
--bp-2xl: 1536px;  /* large desktop */
```

Container max-widths: 640px (narrow), 768px (reading), 1024px (app),
1280px (wide app), 1536px (dashboard)

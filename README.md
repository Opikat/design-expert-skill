# design-expert

A Claude Code skill for unified UI/UX design work — strategy, visual craft, design system generation, and typography calculation in one coherent workflow.

## What it does

Activates for any design-related task: building interfaces, reviewing existing UI/UX, choosing styles/colors/fonts, creating design systems, auditing accessibility, planning user flows, or polishing visual details.

**Three layers, selected by task depth:**

| Layer | Use for |
|-------|---------|
| UX strategy | User flows, IA, psychology, accessibility |
| Visual craft | Spacing, color, typography, components, dark mode, motion |
| Design system generation | Color palettes, font pairings, style matching via searchable database |

**Built-in tools:**

- **Design System Generator** — searches a database of 161 palettes, 57 font pairings, 50+ UI styles, and 161 product types to recommend a complete design system for any project
- **Typography Calculator** (`typography_calc.py`) — calculates precise line-height and letter-spacing values using real font metrics (xHeight, capHeight, capWidth) from 8000+ font styles; always runs instead of guessing
- **UX Rules Quick Reference** — 99 prioritized rules from the UX UI PRO MAX database
- **Naming conventions** — Finsweet Client First (default) and BEM

## Reference library

9 deep-reference files loaded on demand:

- `ux-strategy.md` — cognitive load, visual hierarchy, feedback loops, IA patterns
- `visual-craft.md` — complete token scales, component specs, responsive patterns
- `design-tokens.md` — spacing, color, type, shadow, radius CSS custom properties
- `component-library.md` — buttons, inputs, cards, tables, modals, navigation
- `polish-and-craft.md` — animation timing tables, polish techniques, responsive specs
- `patterns-and-flows.md` — cross-industry patterns, onboarding, checkout, empty states
- `psychology-deep-dive.md` — decision architecture, emotional design, motion psychology
- `naming-conventions.md` — Client First and BEM naming rules with examples
- `ux-rules-reference.md` — full 99-rule reference with implementation details

## Data

CSV databases powering the search scripts:

- `colors.csv` — 161 color palettes with industry and mood tags
- `typography.csv` — 57 font pairings with personality and use-case tags
- `google-fonts.csv` — individual font database with variable weight support
- `figma-fonts.csv` — 8000+ font styles with xHeight, capHeight, capWidth metrics
- `products.csv` — 161 product type patterns
- `styles.csv` — 50+ UI style definitions (glassmorphism, neubrutalism, etc.)
- `charts.csv` — chart type recommendations by data and context
- `landing.csv` — landing page structure patterns
- `ux-guidelines.csv` — UX best practices database
- `app-interface.csv` — app interface accessibility and interaction patterns
- `react-performance.csv` — React/Next.js performance patterns
- `stacks/` — stack-specific guidelines (React, Next.js, Angular, Flutter, Svelte)

## Installation

```bash
# In Claude Code
/install-skill https://github.com/Opikat/design-expert-skill
```

Or drop the `design-expert/` folder into your Claude Code skills directory.

## Credits

**UX strategy and visual craft foundations**
Based on the `ux-designer` and `ui-designer` skills by [Carmen Rincon](https://www.linkedin.com/in/carmenerincon/).
Original skills cover UX psychology, visual design systems, and component craft.

**Design System Generator, Typography Calculator**
Built by [Ekaterina Pykhova](https://www.linkedin.com/in/ekaterina-pykhova/) — product designer based in Prague.

**Naming conventions**
Finsweet Client First and BEM — integrated into the skill by Ekaterina Pykhova.

**UX Rules Quick Reference**
Derived from the [UX UI PRO MAX](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) skill by nextlevelbuilder.

## License

MIT

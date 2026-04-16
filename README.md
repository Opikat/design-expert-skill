# design-expert

A Claude Code skill for unified UI/UX design work — UX strategy, aesthetic direction, visual craft, design-system generation, typography calculation with real font metrics, and live-site review with source-level fixes. Five skills merged into one coherent workflow.

## What it does

Activates for any design-related task: building distinctive interfaces, reviewing existing UI/UX, fixing layouts at the source-code level, choosing styles/colors/fonts, creating design systems, auditing accessibility, planning user flows, or polishing visual details.

**Five layers, selected by task depth:**

| Layer | Use for |
|-------|---------|
| UX strategy | User flows, IA, psychology, accessibility, content design |
| Aesthetic direction | Committing to a distinctive vision, avoiding generic AI aesthetics |
| Visual craft | Spacing, color, typography, components, dark mode, motion, polish |
| Design system generation | Color palettes, font pairings, style matching via searchable database |
| Live-site review | Visual inspection of running websites with source-level fixes |

**Built-in tools:**

- **Design System Generator** — parallel search across a database of 161 palettes, 57 font pairings, 50+ UI styles, and 161 product types, with reasoning rules that select the best matches and can persist the result to `design-system/MASTER.md`
- **Typography Calculator** (`typography_calc.py`) — precision line-height and letter-spacing values from real font metrics (xHeight, capHeight, capWidth) across 8000+ font styles; **always runs** instead of guessing
- **UX Rules Quick Reference** — 99 prioritized rules covering accessibility, touch, performance, style, layout, typography, animation, forms, navigation, charts
- **Naming conventions** — Finsweet Client First (default) and BEM
- **Live-site review workflow** — 6-step loop (gather → inspect → prioritize → fix → re-verify → report) at mobile/tablet/desktop/wide viewports
- **Framework-specific fix patterns** — Pure CSS, SCSS, Tailwind, CSS Modules, styled-components/Emotion, Vue scoped styles, Next.js App Router

## Reference library

11 deep-reference files loaded on demand:

- `ux-strategy.md` — cognitive load, visual hierarchy, feedback loops, IA patterns
- `visual-craft.md` — complete token scales, component specs, responsive patterns
- `aesthetic-direction.md` — 12-direction catalog, execution guidelines, anti-patterns to avoid generic AI aesthetics
- `design-tokens.md` — spacing, color, type, shadow, radius CSS custom properties
- `component-library.md` — buttons, inputs, cards, tables, modals, navigation
- `polish-and-craft.md` — animation timing tables, polish techniques, responsive specs
- `patterns-and-flows.md` — cross-industry patterns, onboarding, checkout, empty states
- `psychology-deep-dive.md` — decision architecture, emotional design, motion psychology
- `naming-conventions.md` — Client First and BEM naming rules with examples
- `ux-rules-reference.md` — full 99-rule reference with implementation details
- `visual-checklist.md` — exhaustive visual inspection checklist for live-site review
- `framework-fixes.md` — framework-specific source-level fix patterns

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
- `icons.csv` — icon library search database
- `ui-reasoning.csv` — reasoning rules for style/palette selection
- `design.csv`, `draft.csv` — working design patterns
- `stacks/` — stack-specific guidelines (React, Next.js, Angular, Flutter, Svelte)

## Installation

```bash
# In Claude Code
/install-skill https://github.com/Opikat/design-expert-skill
```

Or drop the `design-expert/` folder into your Claude Code skills directory.

## Credits

This skill merges material from five open skills into one unified workflow.

**UX strategy and visual craft foundations**
Based on the `ux-designer` and `ui-designer` skills by [Carmen Rincon](https://www.linkedin.com/in/carmenerincon/).
Original skills cover UX psychology, visual design systems, and component craft.

**Aesthetic direction and anti-generic-AI guidelines**
Based on the [frontend-design](https://github.com/emilkowalski/skill) skill by [Emil Kowalski](https://emilkowal.ski/). Original skill covers bold aesthetic commitment and avoiding generic AI-generated interfaces.

**Live-site review workflow and framework-specific fixes**
Based on the `web-design-reviewer` skill — the browser-automation inspection loop, viewport testing matrix, severity prioritization, and framework-specific source fix patterns (CSS/Tailwind/CSS Modules/styled-components/Vue/Next.js).

**Design System Generator, UX Rules Quick Reference, supporting data**
Derived from the [UX UI PRO MAX](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) skill by nextlevelbuilder. Includes the search scripts, reasoning rules, and the majority of the CSV databases.

**Typography Calculator + font metrics database**
Built by [Ekaterina Pykhova](https://www.linkedin.com/in/ekaterina-pykhova/) — product designer based in Prague.
Font metrics (xHeight, capHeight, capWidth) collected via a custom Figma automation script: text placed, converted to outlines, measured, and recorded across 8000+ styles.

**Naming conventions**
Finsweet Client First and BEM — integrated into the skill by Ekaterina Pykhova.

**Merge and integration**
Carried out by Ekaterina Pykhova: mapping overlap across the five source skills, merging duplicated sections, structuring the five-layer workflow, and adding typography metrics integration.

## License

MIT

# Naming Conventions Reference

A comprehensive guide to two major CSS/component naming systems and when to use each.

---

## 1. Finsweet Client First (DEFAULT FOR WEBFLOW)

**The philosophy:** Client First exists to make Webflow development organized, maintainable, and understandable to both developers and non-technical clients. It prioritizes clarity, searchability, and scalability.

### Core Principles

- **No abbreviations or shorthand** — class names answer "what is this doing?"
- **General-to-specific keywords** — organize from broad category to specific purpose
- **Meaningful naming** — empower non-technical people to manage the website
- **Avoid deep stacking** — create custom classes instead of stacking many utilities
- **Searchable classes** — keywords enable easy discovery in Webflow's Styles panel

### Class Structure: `[element]_[identifier]`

**Utility Classes** (no underscore)
- Apply specific CSS properties globally across the project
- Used everywhere: `padding-global`, `margin-large`, `background-color-primary`
- Single responsibility: one set of CSS properties

**Custom Classes** (use underscore)
- Created for specific components, sections, or elements
- Named: `[component]_[element]` or `[section]_[element]`
- Examples: `header_background-layer`, `testimonial-slider_headshot`

### Folder System

Organize classes in the Webflow Navigator using semantic folders:

```
Components/
  Button/
    button
    button_icon
    button_text
    button_is-primary
    button_is-secondary

Layout/
  Header/
    header
    header_nav
    header_nav-item
  Footer/
    footer
    footer_copyright

Utilities/
  Spacing/
    padding-global
    margin-large
  Typography/
    text-size-large
    heading-style-main
```

### Utility Classes by Category

**Spacing & Layout**
- `padding-global` — standard page padding
- `padding-section-[size]` — section spacing (small, medium, large)
- `margin-large`, `margin-medium`, `margin-small`
- `margin-auto` — centering utility

**Typography**
- `text-size-[size]` — consistent font sizes (small, medium, large, xl)
- `heading-style-[style]` — heading variations (main, secondary, accent)
- `text-weight-[weight]` — bold, regular, light
- `text-color-[color]` — semantic color usage (primary, secondary, accent)

**State & Modifiers** (use `is-` prefix for combo classes)
- `is-active` — active state
- `is-disabled` — disabled state
- `is-hidden` — hide element
- Stacked: `button is-primary is-disabled`

**Custom Classes** (use `cc-` prefix when needed)
- `cc-gradient-overlay` — truly custom styles not in the system
- Use sparingly; prefer semantic naming instead

### Component Naming Example

```
Card Component:
  card                  (base container)
  card_image           (image element)
  card_image-overlay   (overlay on image)
  card_title           (heading)
  card_description     (body text)
  card_footer          (bottom section)
  card_is-featured     (featured variant)
  card_is-compact      (compact variant)
```

### Real-World Examples

**Blog Card**
```
blog-card              (container)
blog-card_image        (featured image)
blog-card_category     (category tag)
blog-card_title        (post title)
blog-card_excerpt      (preview text)
blog-card_meta         (date/author info)
blog-card_read-more    (CTA link)
blog-card_is-featured  (featured variant)
```

**Product Grid Section**
```
products-section                (section wrapper)
products-section_grid           (grid container)
products-section_heading        (section title)
products-item                   (individual product card)
products-item_image             (product image)
products-item_name              (product name)
products-item_price             (price display)
products-item_add-to-cart       (button)
products-item_is-out-of-stock   (out-of-stock state)
```

**Navigation**
```
header_nav                 (nav container)
header_nav-item            (nav link)
header_nav-item_link       (actual anchor tag)
header_nav-item_is-active  (current page indicator)
header_nav-dropdown        (dropdown menu)
header_nav-dropdown_item   (dropdown link)
```

### Key Rules

1. **Never deep stack** — Don't use 5+ classes on one element. Create a custom class instead.
2. **Global to specific** — `team-list_headshot-image` not `image-headshot-list-team`
3. **Use underscores for custom** — `header_logo` not `headerLogo`
4. **Hyphens between words** — `background-layer` not `backgroundlayer`
5. **Consistent prefixes** — All FAQs use `faq_`, all testimonials use `testimonial_`

---

## 2. BEM (Alternative for Framework Projects)

**The philosophy:** Block Element Modifier provides a structured, component-based naming system for React, Vue, Angular, and traditional CSS projects.

### Structure: `Block__Element--Modifier`

**Block** — standalone component
- PascalCase or lowercase: `Button`, `Header`, `Card`

**Element** — part of a block, can't exist alone
- Connected with `__`: `Button__Icon`, `Card__Image`

**Modifier** — variation or state of block/element
- Connected with `--`: `Button--primary`, `Card__Image--featured`

### When to Create a New Block

Create a new block when:
- Component can exist independently
- Conceptually different from existing blocks
- Will be reused in multiple locations
- Has its own set of elements

```
CORRECT:
  Button (standalone)
  Modal (standalone container)
  Form (standalone)

WRONG:
  Button__Modal (Modal is not a child of Button)
  Form__TextInput (separate block, not element)
```

### Naming Files & Components in Frameworks

**React Structure**
```
components/
  Button/
    Button.jsx           (block)
    Button.module.css    (or .css)

  Card/
    Card.jsx
    Card.module.css
    CardImage.jsx        (element as sub-component)
    CardImage.module.css

styles/
  button.css             (or blocks/button.css)
  card.css
```

**CSS Class Names in React**
```jsx
// Button.jsx
<button className="button button--primary button--large">
  <span className="button__icon">✓</span>
  <span className="button__text">Click me</span>
</button>

// Card.jsx
<div className="card card--featured">
  <img className="card__image" />
  <h2 className="card__title">Title</h2>
  <p className="card__description">Description</p>
</div>
```

### Real-World BEM Examples

**Navigation**
```
.navigation { }
.navigation--horizontal { }
.navigation--vertical { }
.navigation__item { }
.navigation__item--active { }
.navigation__link { }
.navigation__dropdown { }
.navigation__dropdown--open { }
```

**Form**
```
.form { }
.form--login { }
.form--signup { }
.form__field { }
.form__field--required { }
.form__input { }
.form__input--error { }
.form__label { }
.form__button { }
```

**Product Card**
```
.product-card { }
.product-card--featured { }
.product-card__image { }
.product-card__image--tall { }
.product-card__name { }
.product-card__price { }
.product-card__price--sale { }
.product-card__rating { }
.product-card__action { }
.product-card__action--disabled { }
```

### BEM Rules

1. **Block names are meaningful** — `.card` not `.c` or `.item`
2. **Elements use double underscore** — `card__image` not `card-image` or `card_image`
3. **Modifiers use double hyphen** — `card--featured` not `card-featured`
4. **No element of element** — `.card__wrapper__item` is wrong; create a new block instead
5. **Modifiers modify parent** — `card--featured`, not `card__featured`
6. **One block per CSS file** — `card.css` contains all `.card*` classes
7. **Hyphens separate words** — `product-card__featured-image`

---

## Decision Matrix: Client First vs BEM

| Factor | Client First | BEM |
|--------|--------------|-----|
| **Platform** | Webflow (primary) | React, Vue, Angular, custom CSS |
| **Webflow** | Recommended | Not optimized for Webflow |
| **CSS-in-JS** | Not ideal | Good |
| **Component Files** | N/A | Excellent (Block = Component) |
| **Team Size** | Scales to large teams | Scales to large teams |
| **Learning Curve** | Moderate | Gentle |
| **Deep Stacking** | Discouraged | N/A (framework handles) |
| **State/Modifiers** | `is-` prefix (combo classes) | `--modifier` suffix |
| **File Organization** | Folder-based in Webflow | File-based in IDE |

### Quick Decisions

**Use Client First if:**
- Building in Webflow
- Need non-technical client management
- Prefer folder-based organization
- Want to avoid deep stacking issues

**Use BEM if:**
- Using React, Vue, or Angular
- Building traditional CSS projects
- Components map to files
- Team familiar with CSS methodologies

---

## Critical Rules for Both Systems

### Never Mix Systems in the Same Project

Mixing Client First and BEM creates confusion:
```
WRONG:
  header_nav          (Client First)
  navigation__item    (BEM)
  nav-link            (random)
```

Choose ONE system per project and commit to it.

### Consistency Over Cleverness

- Use the same naming for similar elements across pages
- All cards should follow the same pattern
- All buttons should follow the same pattern
- Consistency enables faster development and handoff

### Documentation

Document your chosen system in `README` or style guide:
- Which system you're using
- Example for each pattern
- Folder/file structure
- Team conventions (spacing, file organization, etc.)

---

## Quick Reference Cheat Sheet

**Client First Cheat**
```
Utilities:        text-size-large, padding-global, margin-large
Custom:           header_nav, header_nav-item, header_nav-item_is-active
States:           is-active, is-disabled, is-hidden
Custom prefix:    cc-custom-gradient (rarely used)
```

**BEM Cheat**
```
Block:            .button, .card, .modal
Element:          .button__icon, .card__image
Modifier:         .button--primary, .card--featured
No element chain: button__wrapper__text (WRONG)
```

---

## Resources

**Finsweet Client First**
- Official Docs: https://finsweet.com/client-first/docs
- Cloneable Template: https://finsweet.info/client-first-cloneable
- Certification: https://finsweet.com/client-first/certification

**BEM Methodology**
- Official BEM: https://bem.methodology.org/
- CSS Tricks Guide: https://css-tricks.com/bem-101/
- Harry Roberts: https://csswizardry.com/

---

**Last Updated:** March 2026
**Recommended for:** Design teams, development teams, Webflow developers, React/Vue developers

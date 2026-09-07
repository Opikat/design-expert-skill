# Tidewater Almanac — profile over `design-expert`

> Fictional brand, written to show the template filled in end to end. A
> coastal weather-and-tides publication: a web almanac, a weekly newsletter,
> and square social cards with the day's tide table.

## This is a PROFILE, not a standalone skill

**Always load `design-expert` first** and run its process (operating mode,
strategy, diverge-before-converge, Verify System + Character). This profile
enters as Mode B input: its tokens and rules are LAW for values.

## Scope guard

- Applies to everything published under the Tidewater Almanac name: the web
  almanac, newsletter templates, social tide cards, printed tide tables.
- Does NOT apply to the publisher's other title, a gardening quarterly, which
  has its own profile. Never mix the two palettes or type stacks.

## Design direction

Nautical chart, not nautical kitsch. Type-led, tabular, high contrast, the
feel of a printed table you trust at 5 a.m. Ornament is limited to the chart
hairlines and one oversized tide numeral.

- Radius language: 0px on everything; tables, cards and buttons are squared.
- Border/structure language: 1px rules in Ink Subtle as separators; no
  shadows, no filled containers except the dark tide strip.
- Whitespace/density stance: dense where data lives (tables), generous around
  headlines; the column grid does the design.
- Accent discipline: one accent (Buoy Orange), used for the current-hour
  marker and links only, never for decoration or backgrounds.

## Palette

| Role | Hex |
|---|---|
| Background | `#F7F5F0` |
| Text default | `#14201F` |
| Text subtle | `#5C6B69` |
| Borders / rules | `#CFD6D3` |
| Accent (sparingly) | `#D9642B` |
| Dark surface (tide strip) | `#0E2A36` |
| Text on dark surface | `#E8EEEA` |

Source of truth for code: `src/styles/tokens.css` in the almanac repo; this
table mirrors it and loses if they disagree.

## Type — roles are strict

| Role | Font | Rules |
|---|---|---|
| Display — the day's high-tide figure and headlines up to 8 words ONLY | Fraunces (Google Fonts), optical size 144 | Weight 600, line-height 0.95, tracking −0.02em. Never sets body copy, captions, or table cells. |
| Running text | Source Serif 4 | Sentence case. Emphasis is SemiBold, never italic for emphasis (italic is reserved for vessel names). |
| Utility / mono — table cells, times, eyebrows, tags | JetBrains Mono | Tabular numerals on; eyebrows UPPERCASE with 0.08em tracking; table cells Regular, no uppercase. |

### Size floors per medium

- **Web almanac:** running text ≥ 17px, table cells ≥ 15px, eyebrows ≥ 12px.
- **Newsletter (email):** running text ≥ 16px, table cells ≥ 14px; no text
  under 13px anywhere.
- **Social tide cards at 1080×1080:** tide numeral ≥ 320px, times ≥ 40px,
  eyebrows ≥ 24px, footnotes ≥ 22px; never 13–18px.

### Anti-slop quotas

- UPPERCASE mono is a seasoning: max 3 uppercase elements per artifact.
- Max one aphorism-shaped line per artifact; tide cards get none, they state
  the table.
- No wave, anchor, or compass icons. The chart hairlines are the only nautical
  reference.

## Signature element

The oversized tide numeral: the day's high-tide height set in Fraunces at
display size, bleeding off the top edge of the dark tide strip, with the time
in mono beneath it. Every artifact carries exactly one such numeral; nothing
else on the page competes for scale.

## Copy on visuals

Labels state facts: "High 4.2 m 06:14", "Wind NW 18 kn". No exclamation
marks, no weather-app cheer ("Perfect beach day!"), no rhetorical questions.
Vessel names in italic; place names as on the chart.

## Media & workflow

1. Drafts as HTML+CSS at the target canvas (web: 1200 wide; cards: 1080×1080);
   fonts from Google Fonts, everything else in-file.
2. Finalize in Figma; export PNG @2x for cards, PDF for printed tables.
3. Every card run passes the critique pass against this profile before
   publishing; a floor violation is fixed, not waived.

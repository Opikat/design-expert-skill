# [Brand Name] — profile over `design-expert`

<!--
This is a fill-in template for a brand profile. Copy it, replace every
[bracketed] value, delete the comments, and save it either as:

  a) its own Claude Code skill (~/.claude/skills/<brand>-visuals/SKILL.md
     with a `name:` + `description:` frontmatter), or
  b) a plain doc in your project that you tell Claude to read after
     loading design-expert (e.g. reference it from your CLAUDE.md).

Load order is fixed: design-expert FIRST, this profile SECOND.
The profile supplies the WHAT (tokens, type roles, formats, signature);
the base skill keeps the HOW (process, banned defaults, accessibility
floors). A profile may tighten the base's floors, never loosen them.
-->

## This is a PROFILE, not a standalone skill

**Always load `design-expert` first** and run its process (operating mode,
strategy, diverge-before-converge, Verify System + Character). This profile
enters as Mode B input: its tokens and rules are LAW for values.

## Scope guard

- [Which work this profile applies to: e.g. "all marketing visuals for
  Acme", "the Acme product UI", "anything published under my own name"]
- [Which work it must NOT touch — name the other context and its profile,
  so the two never mix]

## Design direction

[2–4 lines naming the aesthetic in plain words, e.g. "Editorial/newspaper
grid. Restrained, type-led, high contrast." Then the hard rules:]

- [Radius language: e.g. "0px on everything" / "8px cards, 4px inputs"]
- [Border/structure language: e.g. "1px rules as separators, no shadows"]
- [Whitespace/density stance: e.g. "generous whitespace; the grid does
  the design, not decoration"]
- [Accent discipline: e.g. "one accent hue, 60-30-10, used sparingly"]

## Palette

| Role | Hex |
|---|---|
| Background | `[#______]` |
| Text default | `[#______]` |
| Text subtle | `[#______]` |
| Borders / rules | `[#______]` |
| Accent (sparingly) | `[#______]` |
| Dark surface (optional) | `[#______]` |

<!-- If the palette lives in code, name the authoritative file here
(e.g. "source of truth: src/styles/tokens.css in the <repo> repo") so
the tokens lens of any review can diff against it instead of trusting
this table. -->

## Type — roles are strict

| Role | Font | Rules |
|---|---|---|
| Display — [what qualifies: e.g. big numbers + short headlines ONLY] | [Font] | [weight, line-height, tracking rules; what it must NEVER set] |
| Running text | [Font] | [case, emphasis convention — e.g. "SemiBold + underline, not bare bold"] |
| Utility / mono — labels, eyebrows, tags | [Font] | [case + tracking rules] |

### Size floors per medium

<!-- Floors are per-canvas: what's fine on a website is illegible on a
1080px social graphic. Pin the sizes the base's calculator may not go
below; the calculator fills everything the profile leaves open. -->

- **[Medium 1, e.g. web UI]:** [floors]
- **[Medium 2, e.g. social graphics at 1080px width]:** [floors — e.g.
  "eyebrows ≥ 20px, labels ≥ 18px, footnotes ≥ 19px; never 13–15px"]

### Anti-slop quotas (optional but recommended)

<!-- Quotas are the cheapest defense against the generic-AI look. Examples
from a real profile: "UPPERCASE mono is a seasoning — max ~3 uppercase
elements per artifact"; "max one aphorism-shaped line per graphic". -->

- [Quota 1]
- [Quota 2]

## Signature element

[The ONE ownable move this brand repeats: an oversized numeral system, a
distinctive rule/border language, one unexpected color pairing, a custom
underline. The base skill enforces exactly one signature per artifact —
this profile decides WHICH one it is.]

## Copy on visuals

[Tone rules for text inside graphics, e.g. "plain factual labels, no
aphorism-bait, no meme-labels; a label states a fact, it doesn't perform".]

## Media & workflow

1. [Draft format + canvas defaults, e.g. "HTML+CSS drafts at 1080×1350
   portrait; keep everything in-file, no CDNs"]
2. [Finalization tool + export spec, e.g. "finalize in Figma, export PNG @2x"]
3. [Review ritual, if any — e.g. "run the critique pass on every final draft"]

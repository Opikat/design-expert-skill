# Profiles

`design-expert` is brand-agnostic: it owns the process (diverge before
converging, measured values, banned starting points, accessibility floors) and
has no opinion about any brand's colors or fonts. A **profile** is one markdown
file that supplies those specifics for one brand. Load order is fixed: the
skill first, the profile second.

| File | What it is |
|---|---|
| [`PROFILE-TEMPLATE.md`](PROFILE-TEMPLATE.md) | Fill-in template with comments on every section |
| [`EXAMPLE-tidewater-almanac.md`](EXAMPLE-tidewater-almanac.md) | The template filled in for a fictional brand, so you can see a complete profile end to end |

## Making one

1. Copy `PROFILE-TEMPLATE.md`, replace every `[bracketed]` value, delete the comments.
2. Save it either as its own Claude Code skill (`~/.claude/skills/<brand>-visuals/SKILL.md`, with `name:` and `description:` frontmatter) or as a plain doc your project's `CLAUDE.md` tells Claude to read after `design-expert`.
3. Give it a scope guard: which work it applies to and which other context it must never touch. Two brands never share a profile.

## What a profile decides

Tokens and identity (palette, radius, borders, density), type roles and per-medium size floors, format and layout defaults, component or diagram vocabulary, copy tone on visuals, workflow and export, and which one signature element the brand repeats.

## What a profile cannot change

The process itself, the banned starting points, the accessibility floors, and the one-signature rule. A profile may tighten these, never loosen them. When a profile value breaks a floor, the skill flags it instead of applying it.

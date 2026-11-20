# Changelog

## Unreleased

- **`SKILL.md`**, Step 4. The banned-starting-point table gains gradient-filled text, an accent stripe or thick accent border on a rounded card, glow halos and radial spotlights, and tech props used as garnish (typing cursor, grid-paper background, repeating stripes, unblurred offset shadow). The timid-type row now also names the opposite failure: a full sentence at display size.
- **`SKILL.md`**, Step 14. Banned strings add promise verbs (`streamline`, `empower`, `supercharge`, `seamless`, `unlock`, `elevate`, `effortless`), the "X theater" framing and em dashes as the default joint.
- **`SKILL.md`**, Step 16. The system checklist adds alignment measured by visible edges, text setting (no justified body, no uppercase passages, `text-wrap: balance/pretty`), heading rhythm, edge gutters on a phone, and what layout hides (occlusion, clipping, an image under an opaque wash, repeated text).
- **`references/polish-and-craft.md`** §8 and **`references/design-tokens.md`**: gradient text is a banned starting point with one exception, a brand whose identity is a gradient. The `--spring` token is marked as not for menus, dialogs or routine entrances.

- **`SKILL.md`**, Step 4. New subsection "A reference is the bar to clear, not the template": when a brief names a model product, differentiate on the concept (the page's primary object or main interaction), keep the shared material as substrate, and re-open the concept when a draft starts to resemble the reference.

## 3.0.0 — 2026-11-03

Motion for whole pages and sites: where it goes, how much, and how the agent proves it.

- **`references/motion-site-pass.md`** (new). A pass for adding motion to a page or a site. Every section starts at no motion and gets it only with a job from a closed list, a passed gate and room in the budget. The budget gives a basis for every number and marks the starting values that still need calibrating on real pages. The pass ends in a motion map with rejected candidates and a verdict, and a checklist the agent runs itself: live animation lists, a reduced-motion run, a no-script run, web vitals. Blind-tested: agents with only these files ran the pass on six page types (B2B landing, portfolio, documentation article, conference page, product dashboard, site-builder restaurant), skeptic agents checked every reported gap against the text, and the confirmed gaps are closed.
- **`references/motion-recipes.md`** (new). Word-mask text reveal, 3D card flip, pointer tilt, 3D ring carousel and scroll tilt-in, glowing path with a travelling dot, scroll-linked rail fill and marker. Each comes with when, when not, accessibility, performance, support and a CSS skeleton. All six skeletons pass 38 checks in Chromium with motion allowed, with reduced motion, without script and on a touch phone; method and results in `data/measurements/2026-11-02-motion-recipes/`.
- **`references/motion-patterns.md`**. The ladder starts with the platform's own effects and ends with the library the profile names. Scroll-driven animations are Baseline, inside `@supports`. New entries: scroll tilt-in, pointer tilt, 3D flip, 3D ring, travelling dot, scroll-linked marker. New failure modes: uniform entrance, autoplay without an exit.
- **`SKILL.md`**. A scale-to-scope row and Steps 0 and 12 send whole-page motion through the site pass. Step 4 says what the motion ban covers: the unprompted uniform fade-up, not travel as such. Profiles may now set motion values.
- **Stagger values agree everywhere**: 30–80 ms per step and ≤300 ms in total in product UI; ≤500 ms in total on marketing pages.
- **Design System Generator**: the motion effects it returns (parallax, scroll animations, page transitions) are candidates for the site pass, not decisions. The one library-specific example in the UX rules data is now library-neutral.
- **Profiles**. The template and the example gain a Motion section: character, surfaces, vocabulary, tokens, route, reduced-motion replacement, budget overrides.

Earlier versions were not tagged; 3.0.0 is the first tagged release.

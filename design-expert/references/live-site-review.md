# Live Site Review Workflow

Bans in SKILL.md Step 4 win over any value in this file.

Use when the task is to visually inspect a **running website** and fix issues at
the source-code level (distinct from reviewing a Figma file or static
component). Requires browser automation (e.g. Playwright MCP), source access, and
a see-it → change-it loop. Framework-specific fix patterns:
[framework-fixes.md](framework-fixes.md). Exhaustive inspection checklist:
[visual-checklist.md](visual-checklist.md).

- **A — Gather:** confirm the URL (localhost/staging/prod); detect the project
  (`package.json`, config files, `src/`/`app/`); identify the styling method
  (pure CSS, SCSS, CSS Modules, Tailwind → className, styled-components/Emotion → JS/TS).
- **B — Inspect:** navigate + screenshot; retrieve DOM snapshot; test **all
  viewports** (375 / 768 / 1280 / 1920) — do not skip. Check layout (overflow,
  overlap, alignment, clipping), responsive, accessibility (contrast, focus,
  alt), and visual consistency.
- **C — Prioritize:** P0 functionality-breaking · P1 serious UX (fix now) · P2
  alignment/spacing · P3 minor.
- **D — Fix at the source:** locate the file by class/ID/component; apply the
  **minimal** change; follow existing code style; one issue at a time.
- **E — Re-verify:** reload/HMR; before/after screenshot; regression-check
  adjacent areas and breakpoints. **If more than 3 attempts on one issue, consult
  the user.**
- **F — Report:** summary table (URL, framework, styling, viewports tested,
  issues detected/fixed), then per-issue Detected/Unfixed/Recommendations.

Debug: `* { outline: 1px solid red !important; }`; overflow scan via
`document.querySelectorAll('*')` comparing `scrollWidth`/`clientWidth`. Never do
large refactors during a live review without confirmation.

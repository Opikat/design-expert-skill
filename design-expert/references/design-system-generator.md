# Design System Generator (Python scripts)

Bans in SKILL.md Step 4 win over any value in this file.

For comprehensive design-system recommendations from a searchable database of
161 palettes, 57 font pairings, 50+ styles, and 161 product types. Run from the
skill root.

```bash
# Full design system (start here for new projects):
python3 scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
# Save for reuse (writes design-system/MASTER.md + optional page overrides):
python3 scripts/search.py "<query>" --design-system --persist -p "Project Name" [--page "dashboard"]
# Domain-specific search:
python3 scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
# Stack guidelines:
python3 scripts/search.py "<keyword>" --stack <react|nextjs|angular|flutter|svelte>
```

Domains: `product`, `style`, `color`, `typography`, `icons`, `chart`, `ux`,
`landing`, `react`, `web`. The generator selects matches by reasoning rules; it
supplies raw material for Steps 2–5, it does not replace the divergence.

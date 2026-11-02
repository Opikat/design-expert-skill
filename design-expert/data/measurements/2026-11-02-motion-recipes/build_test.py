"""Build a test page from the fenced code blocks of motion-recipes.md.

Every css/html/js block is copied verbatim, so the page tests exactly what the
reference documents. Blocks before the first numbered recipe (the shared
"once in view" observer) run after the recipe scripts, as the file instructs.
"""
import pathlib
import re
import sys

md_path, out_path = map(pathlib.Path, sys.argv[1:3])
text = md_path.read_text(encoding="utf-8")

sections = re.split(r"^## (\d+)\. .*$", text, flags=re.M)
pre, rest = sections[0], sections[1:]
BLOCK = re.compile(r"```(css|html|js)\n(.*?)```", re.S)

helper_js = [b for lang, b in BLOCK.findall(pre) if lang == "js"]
css, bodies, scripts = [], [], []
for num, body in zip(rest[0::2], rest[1::2]):
    html = []
    for lang, block in BLOCK.findall(body):
        {"css": css, "html": html, "js": scripts}[lang].append(block)
    bodies.append((num, "\n".join(html)))

HARNESS_CSS = """
body { font: 16px/1.5 system-ui, sans-serif; margin: 0; color: #111; }
section { min-height: 130vh; padding: 48px; border-top: 1px solid #bbb; }
h2 { font-size: 44px; line-height: 1.1; margin: 0 0 12px; max-width: 900px; }
.face { padding: 24px; min-height: 140px; border: 2px solid #222; font-size: 32px; }
.front { background: #e8f0ff; } .back { background: #fff3c4; }
.scene { width: 280px; margin: 16px 0; display: inline-block; vertical-align: top; margin-right: 24px; }
.tilt { width: 320px; height: 200px; } .tilt-face { height: 100%; background: #dfe7df; display: grid; place-items: center; }
.ring > * { background: #eef; border: 2px solid #446; display: grid; place-items: center; font-size: 56px; margin: 0; }
.carousel { margin: 32px 0; }
.tilt-in { margin: 60vh 0 0; height: 240px; background: #fde; display: grid; place-items: center; }
.flow { width: 800px; display: block; }
.steps ol { margin: 0; } .steps li { height: 40vh; }
"""

EXTRA_HTML = {
    "1": '<h2 class="control">Every invoice finds its way home</h2>',
    "2": """<button type="button" class="flip" aria-controls="card-2">Show back</button>
<div class="scene"><div class="card" id="card-2" style="overflow: clip">
  <div class="face front">Summary clip</div><div class="face back">Detail clip</div></div></div>
<button type="button" class="flip" aria-controls="card-3">Show back</button>
<div class="scene"><div class="card" id="card-3" style="overflow: hidden">
  <div class="face front">Summary hidden</div><div class="face back">Detail hidden</div></div></div>""",
    "5": """<svg class="flow" id="flow-nofold" viewBox="0 0 400 120" role="img" aria-label="Same flow, no in-view trigger">
  <path class="track" d="M10 100C120 10 280 10 390 100"/><circle class="dot" r="12" fill="url(#flow-glow)"/></svg>
<svg id="attr-test" viewBox="0 0 10 10" style="width:10px; --glow: #3fb6ff"><defs><radialGradient id="attr-grad">
  <stop id="attr-var" offset="0" stop-color="var(--glow)"/></radialGradient></defs></svg>""",
}

page = ["<!doctype html><html lang=en><head><meta charset=utf-8>",
        "<meta name=viewport content='width=device-width,initial-scale=1'>",
        "<title>Motion recipes test</title><style>", HARNESS_CSS, "\n".join(css), "</style></head><body>"]
for num, html in bodies:
    page.append(f'<section id="r{num}">{html}\n{EXTRA_HTML.get(num, "")}</section>')
page.append('<footer id="after" style="height: 100vh"></footer>')
page.append("<script>\n" + "\n".join(scripts) + "\n</script>")
page.append("<script>\n" + "\n".join(helper_js) + "\n</script></body></html>")
out_path.write_text("\n".join(page), encoding="utf-8")
print(f"{len(bodies)} recipes, {len(css)} css, {len(scripts)} js, {len(helper_js)} helper -> {out_path}")

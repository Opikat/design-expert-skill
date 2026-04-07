#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Typography Calculator — computes optimal line-height and letter-spacing
based on font metrics from figma-fonts.csv.

Usage:
  python3 typography_calc.py "Inter" --size 16 --weight 400 --context body
  python3 typography_calc.py "Inter" --size 16 --weight 400 --context body --dark
  python3 typography_calc.py "Playfair Display" --size 48 --weight 700 --context display --uppercase
  python3 typography_calc.py "Inter" --scale 16 --ratio 1.2 --steps 6 --weight 400
  python3 typography_calc.py "Inter" --lookup

Modes:
  Single size:  compute LH + tracking for one font/size/weight/context
  Type scale:   --scale BASE --ratio RATIO --steps N  → full type scale with LH + tracking
  Lookup:       --lookup  → show raw font metrics from CSV
"""

import argparse
import csv
import sys
import io
import math
from pathlib import Path

# Force UTF-8
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DATA_DIR = Path(__file__).parent.parent / "data"
FONT_METRICS_FILE = "figma-fonts.csv"

# ============ FONT PROFILES ============
# Base ratios and adjustments by font category
FONT_PROFILES = {
    "sans-serif": {
        "baseRatio": 1.4,
        "baseTracking": 0.0,
        "displayTightening": -0.015,
        "uppercaseBoost": 0.06,
        "weights": {
            100: 0.01, 200: 0.008, 300: 0.005, 400: 0.0,
            500: -0.005, 600: -0.01, 700: -0.015, 800: -0.02, 900: -0.025
        }
    },
    "serif": {
        "baseRatio": 1.5,
        "baseTracking": 0.01,
        "displayTightening": -0.01,
        "uppercaseBoost": 0.08,
        "weights": {
            100: 0.008, 200: 0.006, 300: 0.004, 400: 0.0,
            500: -0.004, 600: -0.008, 700: -0.012, 800: -0.016, 900: -0.02
        }
    },
    "display": {
        "baseRatio": 1.3,
        "baseTracking": -0.005,
        "displayTightening": -0.02,
        "uppercaseBoost": 0.05,
        "weights": {
            100: 0.01, 200: 0.008, 300: 0.005, 400: 0.0,
            500: -0.006, 600: -0.012, 700: -0.018, 800: -0.024, 900: -0.03
        }
    },
    "monospace": {
        "baseRatio": 1.5,
        "baseTracking": 0.0,
        "displayTightening": 0.0,
        "uppercaseBoost": 0.04,
        "weights": {
            100: 0.005, 200: 0.004, 300: 0.002, 400: 0.0,
            500: -0.002, 600: -0.004, 700: -0.008, 800: -0.012, 900: -0.016
        }
    },
    "handwriting": {
        "baseRatio": 1.6,
        "baseTracking": 0.02,
        "displayTightening": -0.005,
        "uppercaseBoost": 0.04,
        "weights": {
            100: 0.005, 200: 0.004, 300: 0.002, 400: 0.0,
            500: -0.002, 600: -0.004, 700: -0.008, 800: -0.012, 900: -0.016
        }
    }
}

# Grid step for snapping line-height
GRID_STEP = 4  # px


# ============ LOAD METRICS ============
def load_font_metrics(family_name):
    """Load font metrics from CSV by family name. Returns list of matching rows."""
    filepath = DATA_DIR / FONT_METRICS_FILE
    if not filepath.exists():
        return None, f"Font metrics file not found: {filepath}"

    matches = []
    family_lower = family_name.lower().strip()
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['family'].lower().strip() == family_lower:
                matches.append(row)

    if not matches:
        # Try partial match
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if family_lower in row['family'].lower().strip():
                    matches.append(row)
        if matches:
            return matches, None
        return None, f"Font '{family_name}' not found in metrics database"

    return matches, None


def get_best_style(matches, weight):
    """Pick the best matching style row for the given weight."""
    weight_keywords = {
        100: ["thin", "hairline"],
        200: ["extralight", "ultralight"],
        300: ["light"],
        400: ["regular", "normal", "book"],
        500: ["medium"],
        600: ["semibold", "demibold"],
        700: ["bold"],
        800: ["extrabold", "ultrabold"],
        900: ["black", "heavy"]
    }

    keywords = weight_keywords.get(weight, ["regular"])
    for kw in keywords:
        for m in matches:
            if kw in m['style'].lower():
                return m

    # Fallback: first match that isn't italic
    for m in matches:
        if 'italic' not in m['style'].lower():
            return m

    return matches[0]


def get_profile(category):
    """Get font profile by category, with fallback."""
    cat = category.lower().strip() if category else "sans-serif"
    return FONT_PROFILES.get(cat, FONT_PROFILES["sans-serif"])


# ============ INTERPOLATE WEIGHT ============
def interpolate_weight(weights_map, weight):
    """Interpolate weight adjustment from the weights map."""
    sorted_weights = sorted(weights_map.keys())
    if weight in weights_map:
        return weights_map[weight]
    # Find bounding weights
    lower = max([w for w in sorted_weights if w <= weight], default=sorted_weights[0])
    upper = min([w for w in sorted_weights if w >= weight], default=sorted_weights[-1])
    if lower == upper:
        return weights_map[lower]
    t = (weight - lower) / (upper - lower)
    return weights_map[lower] + t * (weights_map[upper] - weights_map[lower])


# ============ CONTEXT MULTIPLIER ============
def get_context_multiplier(context, font_size):
    """Get context multiplier for line-height calculation."""
    if context == "body":
        return 1.0
    elif context == "caption":
        return 1.1
    elif context == "display":
        # Regressive: larger sizes get tighter
        if font_size <= 24:
            return 0.93
        elif font_size <= 36:
            return 0.88
        elif font_size <= 48:
            return 0.84
        elif font_size <= 72:
            return 0.81
        else:
            return 0.79
    elif context == "heading":
        if font_size <= 20:
            return 0.95
        elif font_size <= 32:
            return 0.90
        else:
            return 0.85
    return 1.0


# ============ SNAP TO GRID ============
def snap_to_grid(value, step):
    """Snap a value to the nearest grid step."""
    return round(value / step) * step


# ============ LINE HEIGHT ============
def calc_line_height(font_size, profile, xh_ratio, cap_h_ratio, weight,
                     context="body", dark_bg=False, uppercase=False):
    """
    LH_raw = fontSize * baseRatio * contextMul * (1 + weightAdj) * bgAdj * xhFactor * capFactor
    LH = snapToGrid(LH_raw, GRID_STEP)
    """
    base_ratio = profile["baseRatio"]
    context_mul = get_context_multiplier(context, font_size)
    weight_adj = interpolate_weight(profile["weights"], weight)
    bg_adj = 1.015 if dark_bg else 1.0

    # xHeight factor: fonts with taller x-height need more line-height
    xh_factor = 1.0 + (xh_ratio - 0.50) * 0.4

    # capHeight factor: only for uppercase/display contexts
    if uppercase or context == "display":
        cap_factor = 1.0 + (cap_h_ratio - 0.71) * 0.25
    else:
        cap_factor = 1.0

    lh_raw = font_size * base_ratio * context_mul * (1 + weight_adj) * bg_adj * xh_factor * cap_factor
    lh = snap_to_grid(lh_raw, GRID_STEP)

    return lh, lh / font_size


# ============ TRACKING ============
def calc_tracking(font_size, profile, xh_ratio, cap_w_ratio, weight,
                  context="body", dark_bg=False, uppercase=False):
    """
    trackingRatio = baseTracking + sizeScale + displayAdj + weightAdj + caseAdj + bgAdj + metricsAdj
    letterSpacing = fontSize * trackingRatio (px)
    """
    base_tracking = profile["baseTracking"]

    # Size scale
    if font_size <= 12:
        size_scale = 0.008
    elif font_size <= 24:
        size_scale = 0.0
    elif font_size <= 48:
        size_scale = -0.01 * ((font_size - 24) / 24)
    else:
        size_scale = -0.01 - 0.02 * min((font_size - 48) / 48, 1.0)

    # Display adjustment
    display_adj = profile["displayTightening"] if context == "display" else 0.0

    # Weight adjustment
    weight_adj = interpolate_weight(profile["weights"], weight) * 0.5  # half effect for tracking

    # Uppercase boost
    case_adj = profile["uppercaseBoost"] if uppercase else 0.0

    # Dark background
    bg_adj = 0.015 if dark_bg else 0.0

    # Metrics adjustment from CSV
    metrics_adj = (xh_ratio - 0.50) * 0.05 + (cap_w_ratio - 0.58) * (-0.08)

    tracking_ratio = base_tracking + size_scale + display_adj + weight_adj + case_adj + bg_adj + metrics_adj
    letter_spacing_px = font_size * tracking_ratio

    return tracking_ratio, letter_spacing_px


# ============ TYPE SCALE ============
def generate_type_scale(base_size, ratio, steps):
    """Generate a type scale from base size and ratio."""
    sizes = []
    for i in range(steps):
        size = base_size * (ratio ** i)
        sizes.append(round(size))
    return list(reversed(sizes))  # Largest first


# ============ MAIN ============
def main():
    parser = argparse.ArgumentParser(description="Typography Calculator")
    parser.add_argument("font", help="Font family name (e.g., 'Inter', 'Playfair Display')")
    parser.add_argument("--size", type=int, default=16, help="Font size in px (default: 16)")
    parser.add_argument("--weight", type=int, default=400, help="Font weight (default: 400)")
    parser.add_argument("--context", choices=["body", "caption", "heading", "display"], default="body",
                        help="Usage context (default: body)")
    parser.add_argument("--dark", action="store_true", help="Dark background mode")
    parser.add_argument("--uppercase", action="store_true", help="Uppercase/all-caps text")
    parser.add_argument("--grid", type=int, default=4, help="Grid step for LH snapping (default: 4)")

    # Type scale mode
    parser.add_argument("--scale", type=int, help="Base size for type scale generation")
    parser.add_argument("--ratio", type=float, default=1.2, help="Scale ratio (default: 1.2)")
    parser.add_argument("--steps", type=int, default=6, help="Number of scale steps (default: 6)")

    # Lookup mode
    parser.add_argument("--lookup", action="store_true", help="Just show font metrics")

    args = parser.parse_args()

    global GRID_STEP
    GRID_STEP = args.grid

    # Load font metrics
    matches, error = load_font_metrics(args.font)
    if error:
        print(f"Error: {error}")
        # Try suggesting similar fonts
        filepath = DATA_DIR / FONT_METRICS_FILE
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                families = set()
                for row in reader:
                    if args.font.lower()[:3] in row['family'].lower():
                        families.add(row['family'])
            if families:
                print(f"\nDid you mean: {', '.join(sorted(families)[:10])}")
        sys.exit(1)

    # Lookup mode
    if args.lookup:
        print(f"## Font Metrics: {matches[0]['family']}")
        print(f"**Category:** {matches[0].get('category', 'unknown')}")
        print(f"**Variable:** {matches[0].get('isVariable', 'unknown')}")
        print(f"**Styles found:** {len(matches)}\n")
        print(f"| Style | xHeight | capHeight | capWidth | Condensed | Mono |")
        print(f"|-------|---------|-----------|----------|-----------|------|")
        for m in matches:
            xh = m.get('xHeightRatio', '-')
            ch = m.get('capHeightRatio', '-')
            cw = m.get('capWidthRatio', '-')
            cond = m.get('isCondensed', '-')
            mono = m.get('isMonospace', '-')
            print(f"| {m['style']} | {xh} | {ch} | {cw} | {cond} | {mono} |")
        return

    # Get best style match and metrics
    style_row = get_best_style(matches, args.weight)
    category = style_row.get('category', 'sans-serif')
    profile = get_profile(category)

    try:
        xh = float(style_row.get('xHeightRatio', 0.50))
        ch = float(style_row.get('capHeightRatio', 0.71))
        cw = float(style_row.get('capWidthRatio', 0.58))
    except (ValueError, TypeError):
        xh, ch, cw = 0.50, 0.71, 0.58

    # Type scale mode
    if args.scale:
        sizes = generate_type_scale(args.scale, args.ratio, args.steps)
        contexts = []
        for s in sizes:
            if s >= 48:
                contexts.append("display")
            elif s >= 24:
                contexts.append("heading")
            elif s <= 12:
                contexts.append("caption")
            else:
                contexts.append("body")

        print(f"## Type Scale: {matches[0]['family']}")
        print(f"**Base:** {args.scale}px | **Ratio:** {args.ratio} | **Category:** {category}")
        print(f"**Metrics:** xH={xh}, cH={ch}, cW={cw}")
        print(f"**Weight:** {args.weight} | **Dark BG:** {'Yes' if args.dark else 'No'}\n")
        print(f"| Size | Context | Line Height | LH Ratio | Tracking (em) | Tracking (px) |")
        print(f"|------|---------|-------------|----------|---------------|---------------|")

        for size, ctx in zip(sizes, contexts):
            lh, lh_ratio = calc_line_height(size, profile, xh, ch, args.weight, ctx, args.dark, args.uppercase)
            tr_ratio, tr_px = calc_tracking(size, profile, xh, cw, args.weight, ctx, args.dark, args.uppercase)
            print(f"| {size}px | {ctx} | {lh}px | {lh_ratio:.3f} | {tr_ratio:+.4f}em | {tr_px:+.2f}px |")

        # Also output CSS custom properties
        print(f"\n### CSS Custom Properties\n```css")
        print(f":root {{")
        for i, (size, ctx) in enumerate(zip(sizes, contexts)):
            lh, _ = calc_line_height(size, profile, xh, ch, args.weight, ctx, args.dark, args.uppercase)
            tr_ratio, _ = calc_tracking(size, profile, xh, cw, args.weight, ctx, args.dark, args.uppercase)
            level = len(sizes) - i
            print(f"  --text-{level}-size: {size}px;")
            print(f"  --text-{level}-lh: {lh}px;")
            print(f"  --text-{level}-tracking: {tr_ratio:.4f}em;")
        print(f"}}")
        print(f"```")
        return

    # Single size mode
    lh, lh_ratio = calc_line_height(args.size, profile, xh, ch, args.weight, args.context, args.dark, args.uppercase)
    tr_ratio, tr_px = calc_tracking(args.size, profile, xh, cw, args.weight, args.context, args.dark, args.uppercase)

    print(f"## Typography: {matches[0]['family']} {style_row['style']}")
    print(f"**Category:** {category} | **Size:** {args.size}px | **Weight:** {args.weight}")
    print(f"**Context:** {args.context} | **Dark BG:** {'Yes' if args.dark else 'No'} | **Uppercase:** {'Yes' if args.uppercase else 'No'}")
    print(f"\n### Font Metrics (from CSV)")
    print(f"- xHeight ratio: {xh}")
    print(f"- capHeight ratio: {ch}")
    print(f"- capWidth ratio: {cw}")

    # Show factor breakdowns
    xh_factor = 1.0 + (xh - 0.50) * 0.4
    cap_factor = 1.0 + (ch - 0.71) * 0.25 if (args.uppercase or args.context == "display") else 1.0
    metrics_adj = (xh - 0.50) * 0.05 + (cw - 0.58) * (-0.08)

    print(f"\n### Metric Corrections")
    print(f"- xH factor (LH): {xh_factor:.4f} ({(xh_factor - 1) * 100:+.1f}%)")
    print(f"- cap factor (LH): {cap_factor:.4f} ({(cap_factor - 1) * 100:+.1f}%)")
    print(f"- metrics adj (tracking): {metrics_adj:+.4f}")

    print(f"\n### Results")
    print(f"| Property | Value |")
    print(f"|----------|-------|")
    print(f"| **Line Height** | **{lh}px** ({lh_ratio:.3f}) |")
    print(f"| **Letter Spacing** | **{tr_ratio:+.4f}em** ({tr_px:+.2f}px) |")

    print(f"\n### CSS")
    print(f"```css")
    print(f"font-family: '{matches[0]['family']}', {category};")
    print(f"font-size: {args.size}px;")
    print(f"font-weight: {args.weight};")
    print(f"line-height: {lh}px; /* ratio: {lh_ratio:.3f} */")
    print(f"letter-spacing: {tr_ratio:.4f}em; /* {tr_px:+.2f}px */")
    print(f"```")


if __name__ == "__main__":
    main()

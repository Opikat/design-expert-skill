#!/bin/zsh
# usage: run.sh <model-id> <surface> <n>
S="$(dirname "$0")"; model="$1"; surf="$2"; n="$3"
case "$surf" in
  marketing) brief="Make a landing page for a SaaS product. Output one complete HTML file with all CSS inline in a <style> tag, nothing else.";;
  dashboard) brief="Build an admin dashboard for a web app. Output one complete HTML file with all CSS inline in a <style> tag, nothing else.";;
  diagram)   brief="Draw a diagram that explains how a design system works. Output one complete HTML file with an inline SVG and all CSS inline, nothing else.";;
esac
out="$S/$model/$surf-$n.html"; mkdir -p "$S/$model"
cd "$S" && claude -p "$brief" --model "$model" --tools "" --setting-sources "" --no-session-persistence \
  --system-prompt "You are a front-end designer-developer. Answer with the requested code only, no commentary." > "$out" 2> "$out.err"
echo "$model $surf $n exit=$? bytes=$(wc -c < "$out")"

from pathlib import Path

root = Path(__file__).resolve().parents[1]
for p in root.rglob("*Guide.html"):
    t = p.read_text(encoding="utf-8")
    if "guide-site" in t[:800]:
        continue
    old = '<html lang="en">'
    new = '<html class="guide-site" lang="en">'
    if old in t:
        p.write_text(t.replace(old, new, 1), encoding="utf-8", newline="\n")
        print("patched", p.relative_to(root))

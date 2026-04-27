from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BAD = (
    "</h2>\n    <p style=\"color:var(--muted);font-size:0.92rem;margin:0 0 16px 0;\">"
    "Numeric values are <strong>approximate</strong> and vary by patch, difficulty, and server tuning. "
    "Use them for relative scale only.</p>\n    \n    </div>"
)
GOOD = (
    "</h2>\n    </div>\n    <p style=\"color:var(--muted);font-size:0.92rem;margin:0 0 16px 0;\">"
    "Numeric values are <strong>approximate</strong> and vary by patch, difficulty, and server tuning. "
    "Use them for relative scale only.</p>"
)

n = 0
for p in ROOT.rglob("*Guide.html"):
    t = p.read_text(encoding="utf-8")
    if BAD not in t:
        continue
    p.write_text(t.replace(BAD, GOOD, 1), encoding="utf-8", newline="\n")
    n += 1
print(f"Fixed placement in {n} files.")

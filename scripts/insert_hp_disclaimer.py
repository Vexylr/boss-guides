"""Insert standard HP disclaimer after Health section h2 if missing."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNIPPET = (
    '<p style="color:var(--muted);font-size:0.92rem;margin:0 0 16px 0;">'
    "Numeric values are <strong>approximate</strong> and vary by patch, difficulty, and server tuning. "
    "Use them for relative scale only.</p>\n    "
)
MARKER = "Numeric values are <strong>approximate</strong>"


def process(p: Path) -> bool:
    t = p.read_text(encoding="utf-8")
    if MARKER in t or 'id="health"' not in t:
        return False
    needle = '<h2>Health &amp; Timers</h2>'
    if needle not in t:
        needle = "<h2>Health &amp; Timers</h2>"  # same
    pos = t.find(needle)
    if pos == -1:
        return False
    insert_at = pos + len(needle)
    # skip whitespace and optional section-header closing
    t2 = t[:insert_at] + "\n    " + SNIPPET + t[insert_at:]
    p.write_text(t2, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    n = 0
    for p in sorted(ROOT.rglob("*Guide.html")):
        try:
            if process(p):
                n += 1
        except Exception as e:
            print("skip", p, e)
    print(f"Inserted disclaimer in {n} files.")


if __name__ == "__main__":
    main()

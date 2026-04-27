"""Move <a ...Spells.html>Spells</a> to immediately after the All bosses index link."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\n\s*<a href=\"([^\"]+-Spells\.html)\">Spells</a>\s*")
ALL_BOSSES = re.compile(
    r'(<a href="(?:\.\./)*[^"]*index\.html">All bosses</a>)',
    re.IGNORECASE,
)


def main() -> None:
    for f in sorted(ROOT.rglob("*Guide.html")):
        t = f.read_text(encoding="utf-8")
        m_link = LINK.search(t)
        if not m_link:
            continue
        companion = m_link.group(1)
        t2 = LINK.sub("\n  ", t, count=1)
        m_ab = ALL_BOSSES.search(t2)
        if not m_ab:
            print("skip (no All bosses):", f.relative_to(ROOT))
            continue
        insert = f'\n  <a href="{companion}">Spells</a>'
        pos = m_ab.end()
        t3 = t2[:pos] + insert + t2[pos:]
        if t3 != t:
            f.write_text(t3, encoding="utf-8", newline="\n")
            print("fixed", f.relative_to(ROOT))


if __name__ == "__main__":
    main()

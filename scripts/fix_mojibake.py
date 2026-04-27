#!/usr/bin/env python3
"""Replace common UTF-8-as-Latin1 mojibake sequences in HTML files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = [
    ("\u2014", "\u2014"),  # no-op keep em dash
    ("â€”", "\u2014"),
    ("â€“", "\u2013"),
    ("â€˜", "\u2018"),
    ("â€™", "\u2019"),
    ("â€œ", "\u201c"),
    ("â€", "\u201d"),
    ("â€¢", "\u2022"),
    ("â†'", "\u2192"),
    ("â†\u0090", "\u2192"),
    ("Â·", "\u00b7"),
    ("Â ", " "),
    ("Ã—", "\u00d7"),
    ("â€¦", "\u2026"),
    ("â€œ", '"'),
    ("â€", '"'),
]

# Simpler: explicit broken sequences from Windows-1252 misread as UTF-8
MAP = {
    "â€”": "\u2014",
    "â€“": "\u2013",
    "â€˜": "\u2018",
    "â€™": "\u2019",
    "â€œ": "\u201c",
    "â€": "\u201d",
    "â€¢": "\u2022",
    "â†'": "\u2192",  # arrow mojibake ending ASCII '
    "â†\u2019": "\u2192",  # arrow + Unicode right single quote (common in broken UTF-8)
    "â†’": "\u2192",  # if file already mixed
    "Â·": "\u00b7",
    "Â ": "",
    "Ã—": "\u00d7",
    "â€¦": "\u2026",
    "â‰¥": "\u2265",  # >=
    "â‰¤": "\u2264",
    "âˆ'": "\u2212",  # minus mojibake (ASCII apostrophe tail)
    "âˆ\u2019": "\u2212",  # â + modifier circumflex + curly quote (broken −)
}


def fix_text(s: str) -> str:
    for bad, good in MAP.items():
        s = s.replace(bad, good)
    return s


def main() -> None:
    n = 0
    for p in ROOT.rglob("*.html"):
        t = p.read_text(encoding="utf-8")
        t2 = fix_text(t)
        if t2 != t:
            p.write_text(t2, encoding="utf-8", newline="\n")
            n += 1
    print(f"Fixed mojibake in {n} HTML files.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Wire shared cataclysm-guides.css, guide-site on indices, guide-page + data-raid on all guides."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET = "assets/cataclysm-guides.css"

RAID_MAP = {
    "Dragon Soul": "dragon-soul",
    "Firelands": "firelands",
    "Blackwing Descent": "blackwing",
    "Bastion of Twilight": "bastion",
    "Throne of the Four Winds": "four-winds",
}


def rel_to_assets(html_path: Path) -> str:
    depth = len(html_path.parent.relative_to(ROOT).parts)
    return ("../" * depth) + ASSET


def insert_css_link(html: str, href: str) -> str:
    if "cataclysm-guides.css" in html:
        return html
    link = f'  <link rel="stylesheet" href="{href}" />\n'
    styles = list(re.finditer(r"</style>", html, re.I))
    if styles:
        pos = styles[-1].end()
        return html[:pos] + "\n" + link + html[pos:]
    return html.replace("</head>", link + "</head>", 1)


def patch_html_guide_site(html: str) -> str:
    if 'class="guide-site"' in html or "class='guide-site'" in html:
        return html
    return re.sub(r"<html\s+lang=", '<html class="guide-site" lang=', html, count=1, flags=re.I)


def raid_from_path(p: Path) -> str | None:
    rel = p.relative_to(ROOT)
    parts = rel.parts
    if p.name == "index.html" and len(parts) == 1:
        return "hub"
    if p.name == "quickref.html" and parts[0] == "Firelands":
        return "firelands"
    if len(parts) >= 2 and parts[0] in RAID_MAP:
        return RAID_MAP[parts[0]]
    return None


def patch_body_open(html: str, raid: str | None) -> str:
    raid = raid or "hub"
    if re.search(r"<body[^>]*guide-page", html, re.I):
        if f'data-raid="{raid}"' not in html[:3500]:
            html = re.sub(
                r"<body([^>]*class=\"[^\"]*guide-page[^\"]*)\"",
                rf'<body\1 data-raid="{raid}"',
                html,
                count=1,
                flags=re.I,
            )
        return html

    html2, n = re.subn(
        r"(</head>\s*)<body>\s*",
        rf'\1<body class="guide-page" data-raid="{raid}">\n',
        html,
        count=1,
        flags=re.I | re.S,
    )
    if n:
        return html2
    html2, n2 = re.subn(
        r"(</head>\s*)<body\s+>",
        rf'\1<body class="guide-page" data-raid="{raid}" ',
        html,
        count=1,
        flags=re.I | re.S,
    )
    return html2 if n2 else html


def process_file(p: Path) -> bool:
    text = p.read_text(encoding="utf-8")
    orig = text
    href = rel_to_assets(p)
    raid = raid_from_path(p)
    text = insert_css_link(text, href)
    if p.name in ("index.html", "quickref.html"):
        text = patch_html_guide_site(text)
    text = patch_body_open(text, raid)
    if text != orig:
        p.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> None:
    targets: list[Path] = [ROOT / "index.html"]
    for raid in RAID_MAP:
        idx = ROOT / raid / "index.html"
        if idx.exists():
            targets.append(idx)
    qr = ROOT / "Firelands" / "quickref.html"
    if qr.exists():
        targets.append(qr)
    targets.extend(sorted(ROOT.rglob("*Guide.html")))
    n = 0
    for t in targets:
        if process_file(t):
            n += 1
    print(f"Updated {n} of {len(targets)} files.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate *-Spells.html companion pages and rewrite mech-badge spans in *Guide.html.
Optional metadata: assets/spell-manifest.json — wowheadSpellId, blurb per (guideRel|anchor).
Run from repo root: python tools/generate_spell_companions.py
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "assets" / "spell-manifest.json"


def slug(label: str) -> str:
    s = label.lower().strip()
    s = s.replace("'", "").replace("&amp;", "and")
    out: list[str] = []
    for c in s:
        if c.isalnum():
            out.append(c)
        elif c in " -":
            out.append("-")
    s = "".join(out)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")


def css_href_for(path: Path) -> str:
    depth = len(path.relative_to(ROOT).parts) - 1
    return ("../" * depth) + "assets/cataclysm-guides.css"


def raid_data_attr(guide_path: Path) -> str:
    text = guide_path.read_text(encoding="utf-8")
    m = re.search(r'<body[^>]*\sdata-raid="([^"]+)"', text)
    if m:
        return m.group(1)
    rel = guide_path.relative_to(ROOT).as_posix().lower()
    if "dragon soul" in rel or rel.startswith("dragon"):
        return "dragon-soul"
    if "firelands" in rel:
        return "firelands"
    if "blackwing" in rel:
        return "blackwing"
    if "bastion" in rel:
        return "bastion"
    if "throne" in rel or "four winds" in rel:
        return "four-winds"
    return "hub"


def hero_h1(guide_path: Path) -> str:
    text = guide_path.read_text(encoding="utf-8")
    m = re.search(r'<div class="hero"[^>]*>.*?<h1>(.*?)</h1>', text, re.DOTALL | re.IGNORECASE)
    if not m:
        return guide_path.stem.replace("-Guide", "").replace("-", " ")
    raw = re.sub(r"<[^>]+>", "", m.group(1))
    return html.unescape(raw).strip()


def page_title_suffix(guide_path: Path) -> str:
    t = guide_path.read_text(encoding="utf-8")
    m = re.search(r"<title>([^<]+)</title>", t)
    if m:
        return html.unescape(m.group(1).split("—")[-1].strip())
    return "Boss Guide"


def load_manifest() -> dict:
    if not MANIFEST_PATH.is_file():
        return {"entries": {}}
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def raid_label(guide_path: Path) -> str:
    parts = guide_path.relative_to(ROOT).parts
    if len(parts) >= 1:
        return parts[0]
    return "Raid"


def default_blurb(guide_path: Path, label: str) -> str:
    r = raid_label(guide_path)
    return (
        f"<strong>{html.escape(label)}</strong> is used on this encounter in "
        f"<strong>{html.escape(r)}</strong>. Use the boss guide for timing, positioning, "
        "and assignments. Exact damage, range, and cooldowns can differ on Cataclysm Classic "
        "or private servers—verify in the in-game Dungeon Journal when in doubt."
    )


def entry_key(guide_rel: str, anchor: str) -> str:
    return f"{guide_rel}|{anchor}"


def build_spell_html(
    *,
    guide_path: Path,
    companion_path: Path,
    badges: list[tuple[str, str]],
    manifest: dict,
) -> str:
    guide_rel = guide_path.relative_to(ROOT).as_posix()
    data_raid = raid_data_attr(guide_path)
    h1 = html.escape(hero_h1(guide_path))
    guide_name = guide_path.name
    css = css_href_for(companion_path)
    entries_meta: dict = manifest.get("entries", {})

    toc_items = []
    blocks = []
    for label, anc in badges:
        toc_items.append(f'<li><a href="#{html.escape(anc, quote=True)}">{html.escape(label)}</a></li>')
        meta = entries_meta.get(entry_key(guide_rel, anc), {})
        blurb = meta.get("blurb")
        if not blurb:
            blurb = default_blurb(guide_path, label)
        wid = meta.get("wowheadSpellId")
        ref_p = ""
        if wid:
            ref_p = (
                f'<p class="spell-ref"><a href="https://www.wowhead.com/cata/spell={int(wid)}" '
                f'target="_blank" rel="noopener noreferrer">Wowhead — spell #{wid}</a> (tooltip reference)</p>'
            )
        blocks.append(
            f'<article class="spell-block" id="{html.escape(anc, quote=True)}">'
            f"<h2>{html.escape(label)}</h2>"
            f'<p class="spell-summary">{blurb}</p>{ref_p}</article>'
        )

    toc_html = (
        '<nav class="spell-toc section" aria-label="On this page">'
        "<h2>Abilities</h2><ul>"
        + "".join(toc_items)
        + "</ul></nav>"
        if toc_items
        else '<p class="spell-summary">Named mechanics in this encounter are explained in the boss guide body.</p>'
    )

    blocks_html = "\n".join(blocks) if blocks else ""

    return f"""<!DOCTYPE html>
<html class="guide-site" lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{h1} — Ability reference</title>
  <meta name="description" content="Curated ability notes for {h1}. Cross-check the Dungeon Journal in-game." />
  <link rel="stylesheet" href="{css}" />
</head>
<body class="guide-page" data-raid="{html.escape(data_raid, quote=True)}">
<a class="skip-link" href="#main-content">Skip to content</a>
<div class="hero">
  <div class="hero-content">
    <div class="hero-eyebrow">Ability reference</div>
    <h1>{h1}</h1>
    <p class="hero-tagline">Short notes per named mechanic. Not a full walkthrough—use the boss guide for strategy.</p>
  </div>
</div>
<nav class="sticky-nav" aria-label="Reference navigation">
  <span class="sticky-nav-logo">Spells</span>
  <a href="{html.escape(guide_name, quote=True)}">Boss guide</a>
  <a href="#main-content">Top</a>
</nav>
<main id="main-content" class="container section">
  {toc_html}
  {blocks_html}
  <p class="spell-disclaimer">Text is paraphrased for clarity from encounter design and public references (Dungeon Journal, Wowhead Cataclysm). It is not an official Blizzard publication. If a link is missing, look up the spell name on Wowhead or in-game.</p>
</main>
<footer class="guide-footer">
  <p><a href="{html.escape(guide_name, quote=True)}">Back to boss guide</a></p>
</footer>
</body>
</html>
"""


def companion_name(guide_path: Path) -> str:
    stem = guide_path.stem
    if stem.endswith("-Guide"):
        return stem[: -len("-Guide")] + "-Spells.html"
    return stem + "-Spells.html"


def patch_guide_nav(guide_text: str, companion: str, has_badges: bool) -> str:
    if not has_badges:
        return guide_text
    link = f'<a href="{html.escape(companion, quote=True)}">Spells</a>'
    if link in guide_text:
        return guide_text
    m = re.search(r'(<a href="(?:\.\./)*[^"]*index\.html">All bosses</a>)', guide_text, re.IGNORECASE)
    if m:
        return guide_text[: m.end()] + "\n  " + link + guide_text[m.end() :]
    marker = '<nav class="sticky-nav"'
    idx = guide_text.find(marker)
    if idx == -1:
        return guide_text
    inner_start = guide_text.find(">", idx) + 1
    return guide_text[:inner_start] + "\n  " + link + guide_text[inner_start:]


def replace_badges(guide_text: str, companion: str) -> str:
    def repl(m: re.Match[str]) -> str:
        label = m.group(1)
        a = slug(label)
        return (
            f'<a class="mech-badge" href="{html.escape(companion, quote=True)}#{html.escape(a)}">'
            f"{html.escape(label)}</a>"
        )

    return re.sub(r'<span class="mech-badge">([^<]+)</span>', repl, guide_text)


def main() -> None:
    manifest = load_manifest()
    summary: list[dict] = []

    for guide_path in sorted(ROOT.rglob("*Guide.html")):
        rel = guide_path.relative_to(ROOT)
        text = guide_path.read_text(encoding="utf-8")
        labels = re.findall(r'<span class="mech-badge">([^<]+)</span>', text)
        uniq: list[tuple[str, str]] = []
        seen: set[str] = set()
        for lab in labels:
            a = slug(lab)
            if a not in seen:
                seen.add(a)
                uniq.append((lab, a))

        companion = companion_name(guide_path)
        companion_path = guide_path.with_name(companion)

        spell_html = build_spell_html(
            guide_path=guide_path,
            companion_path=companion_path,
            badges=uniq,
            manifest=manifest,
        )
        companion_path.write_text(spell_html, encoding="utf-8", newline="\n")

        new_guide = replace_badges(text, companion)
        new_guide = patch_guide_nav(new_guide, companion, bool(uniq))
        if new_guide != text:
            guide_path.write_text(new_guide, encoding="utf-8", newline="\n")

        summary.append(
            {
                "guide": rel.as_posix(),
                "companion": companion_path.relative_to(ROOT).as_posix(),
                "abilityCount": len(uniq),
            }
        )

    out_manifest = ROOT / "assets" / "spell-pages-manifest.json"
    out_manifest.write_text(json.dumps({"generated": summary}, indent=2), encoding="utf-8")
    print(f"Wrote {len(summary)} companion pages and patched guides. Index: {out_manifest}")


if __name__ == "__main__":
    main()
    sys.exit(0)

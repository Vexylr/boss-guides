# Boss guides (Cataclysm raids)

Static HTML writeups for **Cataclysm** raid bosses—**Normal and Heroic**, framed for **10- and 25-player** groups. No build step: clone or download, open the pages in a browser, done.

Mechanics in the guides are labeled **\[N]** (Normal only), **\[H]** (Heroic only), or **\[N/H]** when both modes share the thing.

---

## Table of contents

1. [What's in here](#whats-in-here)
2. [How to browse it](#how-to-browse-it)
3. [Repo layout](#repo-layout)
4. [Raids at a glance](#raids-at-a-glance)
5. [Shared assets & scripts](#shared-assets--scripts)
6. [Feedback](#feedback)

---

## What's in here

This repo is a small site: a **home page** that links to **five raids**, each with an **index of bosses** and one **HTML guide per boss** (28 guides total). Guides are meant to be read in a tab—sticky nav, sections for overview, phases, heroic-only bits where it matters, and a quick-reference table on most pages.

There's also a **Firelands quick reference** one-pager if you want everything on that tier in one scroll.

---

## How to browse it

1. Open **[`index.html`](index.html)** in your browser (double-click from Explorer/Finder, or "Open with" Chrome/Firefox/Edge). That's the front door: Tier 11, Firelands, Dragon Soul.
2. Pick a raid card. You'll land on that raid's **`index.html`**—boss cards link to each guide.
3. Inside a guide, use the **top nav** (Overview, Health, Phases, etc.) to jump around. There's a **skip link** first in the tab order if you use keyboard only.

**Tip:** Print → Save as PDF from any page if you want an offline copy.

---

## Repo layout

| Path | Purpose |
|------|--------|
| [`index.html`](index.html) | Main hub: all raids |
| [`assets/`](assets/) | Shared stylesheet (`cataclysm-guides.css`), images, [`guide-standards.txt`](assets/guide-standards.txt) (editor notes: sources + QA checklist) |
| `scripts/` (local only) | Optional Python helpers for bulk edits; **not in the repo**—ignored by git so clones stay site-only |
| [`Bastion of Twilight/`](Bastion%20of%20Twilight/) | 5 boss HTML guides + raid index |
| [`Blackwing Descent/`](Blackwing%20Descent/) | 6 bosses + index |
| [`Throne of the Four Winds/`](Throne%20of%20the%20Four%20Winds/) | 2 bosses + index |
| [`Firelands/`](Firelands/) | 7 bosses, raid index, [`quickref.html`](Firelands/quickref.html) |
| [`Dragon Soul/`](Dragon%20Soul/) | 8 bosses + index |

Boss files follow the pattern `*Guide.html` under each boss folder.

---

## Raids at a glance

| Tier | Raid | Open this |
|------|------|-------------|
| 11 | Bastion of Twilight | [`Bastion of Twilight/index.html`](Bastion%20of%20Twilight/index.html) |
| 11 | Blackwing Descent | [`Blackwing Descent/index.html`](Blackwing%20Descent/index.html) |
| 11 | Throne of the Four Winds | [`Throne of the Four Winds/index.html`](Throne%20of%20the%20Four%20Winds/index.html) |
| 12 | Firelands | [`Firelands/index.html`](Firelands/index.html) |
| 13 | Dragon Soul | [`Dragon Soul/index.html`](Dragon%20Soul/index.html) |

Firelands cheat sheet: [`Firelands/quickref.html`](Firelands/quickref.html).

---

## Shared assets & scripts

Guides link to **`assets/cataclysm-guides.css`** for shared typography, contrast tweaks, and light motion (with `prefers-reduced-motion` respected). Raid flavor is mostly still in each page's inline CSS; the shared file layers on top.

If you're contributing content, skim **`assets/guide-standards.txt`** for where we pull mechanics from and what we check before calling a page done.

---

## Feedback

Spotted a wrong timer, a Heroic-only line tagged as Normal, or a boss strat that doesn't match how your guild runs it? I'm happy to hear it.

**Discord:** **karma2234** — I go by **Hollow** / **Karma** there. Send a message with the boss name and what's off (or a screenshot), and I'll fold fixes into the HTML when I can.

No Discord? You can still open an issue on GitHub with the same detail; I'll see it when I'm on.

---

*Cataclysm is Blizzard's IP; these guides are fan-made reference material.*

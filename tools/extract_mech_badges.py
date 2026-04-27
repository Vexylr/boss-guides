"""One-off helper: list mech-badge labels per *Guide.html (UTF-8)."""
import re
import pathlib


def slug(label: str) -> str:
    s = label.lower().strip()
    s = s.replace("'", "").replace("&amp;", "and")
    out = []
    for c in s:
        if c.isalnum():
            out.append(c)
        elif c in " -":
            out.append("-")
    s = "".join(out)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[1]
    for f in sorted(root.rglob("*Guide.html")):
        text = f.read_text(encoding="utf-8")
        badges = re.findall(r'<span class="mech-badge">([^<]+)</span>', text)
        uniq = sorted(set(badges))
        rel = f.relative_to(root).as_posix()
        print(f"{rel}\t{len(uniq)}")
        for b in uniq:
            print(f"  {slug(b)}\t{b}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Bouwt dist/ uit src/: plakt de iconen als data-URI in de pagina.

Gebruik: python3 build.py
Alleen de standaardbibliotheek, geen installaties nodig.
"""
import base64
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"


def icon_uri(code: str) -> str:
    path = SRC / "icons" / f"{code}.svg"
    if not path.exists():
        sys.exit(f"Icoon ontbreekt: {path}")
    return "data:image/svg+xml;base64," + base64.b64encode(path.read_bytes()).decode()


def main() -> None:
    html = (SRC / "opstaan.html").read_text(encoding="utf-8")
    html = re.sub(r"__ICON_([0-9a-f]+)__", lambda m: icon_uri(m.group(1)), html)
    if "__ICON_" in html:
        sys.exit("Niet alle iconen zijn vervangen")

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    (DIST / "opstaan.html").write_text(html, encoding="utf-8")
    shutil.copy(SRC / "opstaan-icoon.png", DIST / "opstaan-icoon.png")

    for f in sorted(DIST.iterdir()):
        print(f"{f.name}: {f.stat().st_size} bytes")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Resincroniza los números de diapositiva del índice de slides.md.

Los enlaces del índice apuntan a números de diapositiva (`/46`), que se mueven
en cuanto se agrega o quita una página. Este script recalcula dónde empieza cada
sección y reescribe los `href`, identificando cada enlace por su `data-sec`.

Correr después de cualquier cambio en pages/ o en el orden de slides.md:

    python3 sync-indice.py
"""
import pathlib
import re
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent
SLIDES_MD = ROOT / "slides.md"
PAGES = ROOT / "pages"

_src = (ROOT / "export-sections.py").read_text()
_ns = {"re": re, "pathlib": pathlib, "subprocess": subprocess, "time": time,
       "ROOT": ROOT, "SLIDES_MD": SLIDES_MD, "PAGES": PAGES}
exec(compile(_src[_src.index("SECTION_NAMES = {"):_src.index("def is_probably_blank")], "rangos", "exec"), _ns)

rangos = _ns["build_ranges"]()
texto = SLIDES_MD.read_text()
cambios = []


def reemplazar(m: re.Match) -> str:
    href, sec, resto = m.group(1), m.group(2), m.group(3)
    if sec not in rangos:
        sys.exit(f"El índice apunta a la sección '{sec}', que ya no existe en slides.md")
    nuevo = f"/{rangos[sec][0]}"
    if nuevo != href:
        cambios.append((sec, href, nuevo))
    return f'<a href="{nuevo}" data-sec="{sec}">{resto}</a>'


texto = re.sub(r'<a href="(/\d+)" data-sec="([^"]+)">(.*?)</a>', reemplazar, texto)
SLIDES_MD.write_text(texto)

if cambios:
    for sec, viejo, nuevo in cambios:
        print(f"  {sec:<6} {viejo} -> {nuevo}")
    print(f"\nÍndice actualizado: {len(cambios)} enlace(s).")
else:
    print("El índice ya estaba sincronizado.")

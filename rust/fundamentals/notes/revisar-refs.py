#!/usr/bin/env python3
"""Verifica que cada referencia «N.M Título» apunte a una página existente y la nombre bien.

Las referencias cruzadas ("Ver también · 5.1 Option") son texto plano: cuando una
página se renumera o se renombra, quedan apuntando a otra cosa sin que nada falle.
Este script las compara contra el `# Título` real de cada página.

    python3 revisar-refs.py
"""
import pathlib
import re
import sys
import unicodedata

PAGES = pathlib.Path(__file__).resolve().parent / "pages"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", "", s).strip()


titulos = {}
for f in sorted(PAGES.glob("*.md")):
    if f.name.startswith("_") or f.name == "ejercicios.md":
        continue
    m = re.match(r"(\d+\.\d+)-", f.name)
    if not m:
        continue
    # los bloques comentados no cuentan: su `# Título` no se renderiza
    cuerpo = re.sub(r"<!--[\s\S]*?-->", "", f.read_text())
    h = re.search(r"^# (.+)$", cuerpo, re.M) or re.search(r"^## (.+)$", cuerpo, re.M)
    t = h.group(1).strip().strip("`") if h else "(sin título)"
    # los divisores llevan su número al frente: "5.6 · Iteradores"
    titulos[m.group(1)] = re.sub(r"^\d+\.\d+\s*·\s*", "", t)

problemas = []
for f in sorted(PAGES.glob("*.md")):
    if f.name.startswith("_") or f.name == "ejercicios.md":
        continue
    # un número sin nombre no le sirve a quien no se sabe el índice de memoria
    fuera_de_codigo = "".join(
        p for p in re.split(r"(```[\s\S]*?```)", f.read_text()) if not p.startswith("```")
    )
    for num in re.findall(r"\((\d\.\d)\)", fuera_de_codigo):
        if num in titulos:
            problemas.append((f.name, 0, num, "(sin nombre)",
                              f"referencia pelona: debe decir «{num} {titulos[num]}»"))
    for i, linea in enumerate(f.read_text().split("\n"), 1):
        for num, txt in re.findall(r"\b(\d\.\d)\s+([A-ZÁÉÍÓÚ`][^·<\n,\)]{1,42})", linea):
            txt = txt.strip().rstrip(".")
            if num not in titulos:
                problemas.append((f.name, i, num, txt, "esa sección ya no existe"))
            elif not norm(titulos[num]).startswith(norm(txt)[:14]):
                problemas.append((f.name, i, num, txt, f"es «{titulos[num]}»"))

if problemas:
    for archivo, linea, num, txt, motivo in problemas:
        print(f"  {archivo}:{linea}  «{num} {txt}» → {motivo}")
    print(f"\n{len(problemas)} referencia(s) desalineada(s).")
    sys.exit(1)
print(f"{len(titulos)} páginas · todas las referencias cruzadas apuntan bien.")

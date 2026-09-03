#!/usr/bin/env python3
"""Detecta diapositivas que se desbordan del alto de la pantalla (regla R11).

No mide "cuánto contenido hay" sino **cuánto alto ocupa al renderizar**, que es lo
que de verdad revienta. Estima líneas visuales contando código (fuente chica),
prosa (fuente grande, con salto cada ~78 caracteres), filas de tabla y el relleno de
los callouts. Las rejillas `grid-cols-N` cuentan una sola columna, porque sus
bloques van lado a lado. El bloque "Ver también" no cuenta: va absoluto al pie.

El umbral está calibrado contra una diapositiva que se desbordaba de verdad.

    python3 revisar-densidad.py
    python3 revisar-densidad.py --todas
"""
import math
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent
PAGES = RAIZ / "pages"


def umbral() -> float:
    """Alto máximo utilizable, derivado del CSS en vez de una constante fija.

    Cada vez que cambia el `padding-bottom` que reserva la franja del pie, cambia el
    alto disponible. Atarlo al CSS evita que este detector quede midiendo contra una
    pantalla que ya no existe — que es justo lo que pasó dos veces.
    """
    css = (RAIZ / "style.css").read_text()
    m = re.search(r"\.slidev-layout:has\(\.cp-ver-tambien\)\s*\{[^}]*padding-bottom:\s*([\d.]+)rem", css)
    reservado = float(m.group(1)) if m else 0.0
    return 26.0 - reservado * 1.2


UMBRAL = None  # se calcula en main()

EXCEPCIONES = {
    ("6.2-rc-refcell-arboles.md", "Recorridos"),   # tres recorridos en paralelo
    ("ap0-cheatsheet.md", "Diagnóstico"),          # el cheatsheet es una referencia densa
    ("ap0-cheatsheet.md", "Pelar la cebolla"),     # tabla de referencia
}


def sin_comentarios(s: str) -> str:
    """Quita los bloques `<!-- ... -->`: no se renderizan, así que no ocupan alto."""
    return re.sub(r"<!--[\s\S]*?-->", "", s)


def alto(s: str) -> float:
    """Alto estimado de una diapositiva, en líneas visuales."""
    s = sin_comentarios(s)
    s = re.sub(r'<div class="cp-ver-tambien">[\s\S]*?</div>', "", s)
    h = 2.2 if re.search(r"^## ", s, re.M) else 0.0

    m = re.search(r"grid-cols-(\d)", s)
    cols = int(m.group(1)) if m else 1

    bloques = [len(b.rstrip().split("\n")) * 0.78 + 1.6
               for b in re.findall(r"```\w*\n([\s\S]*?)```", s)]
    h += (max(bloques) + 1.0) if (cols > 1 and len(bloques) > 1) else sum(bloques)

    cuerpo = re.sub(r"```[\s\S]*?```", "", s)
    filas = re.findall(r"^\|", cuerpo, re.M)
    if filas:
        h += len(filas) * 1.15 + 1.0
    cuerpo = re.sub(r"(?m)^\|.*$", "", cuerpo)

    h += len(re.findall(r"important-note|cp-callout", s)) * 2.2

    # La prosa dentro de bloques con `font-size` explícito ocupa menos alto del que
    # supone el modelo. Se escala por la mediana de los tamaños declarados: es una
    # aproximación, pero evita marcar como desbordadas las diapositivas de tipografía
    # reducida (tablas compactas, diagramas, notas al pie).
    tam = [float(x) for x in re.findall(r"font-size:\s*([\d.]+)rem", s)]
    if tam:
        tam.sort()
        escala = min(1.0, tam[len(tam) // 2])
    else:
        escala = 1.0

    texto = re.sub(r"<[^>]+>", "", cuerpo)
    parrafos = [p for p in texto.split("\n\n") if p.strip() and not p.strip().startswith("#")]
    if cols > 1:
        parrafos = parrafos[: max(1, len(parrafos) // cols + 1)]
    for p in parrafos:
        h += (max(1, math.ceil(len(re.sub(r"\s+", " ", p.strip())) / 78)) * 1.45 + 0.5) * escala
    return h


ANCHO_COL_2 = 50   # bloques dentro de una rejilla de dos columnas
ANCHO_COMPLETO = 74


def lineas_largas(s: str) -> list[str]:
    """Líneas de código que se saldrían de su columna (y sacarían barra lateral)."""
    s = sin_comentarios(s)
    limite = ANCHO_COL_2 if re.search(r"grid-cols-[2-9]", s) else ANCHO_COMPLETO
    largas = []
    for b in re.findall(r"```\w*\n([\s\S]*?)```", s):
        for linea in b.split("\n"):
            if len(linea.rstrip()) > limite:
                largas.append(f"{len(linea.rstrip())} col · {linea.strip()[:44]}")
    return largas


def main() -> None:
    filas = []
    anchas = []
    for f in sorted(PAGES.glob("*.md")):
        if f.name.startswith("_") or f.name == "ejercicios.md":
            continue
        for s in re.split(r"(?m)^---\n(?=layout:)", f.read_text()):
            t = re.findall(r"^## (.+)$", sin_comentarios(s), re.M)
            if not t:
                continue
            if any(f.name == a and t[0].startswith(b) for a, b in EXCEPCIONES):
                continue
            filas.append((alto(s), f.name, t[0]))
            for aviso in lineas_largas(s):
                anchas.append((f.name, t[0][:34], aviso))

    filas.sort(reverse=True)
    limite = umbral()
    mostrar = filas if "--todas" in sys.argv else [x for x in filas if x[0] > limite]
    vals = sorted(x[0] for x in filas)
    mediana = vals[len(vals) // 2]

    if anchas:
        print("Líneas de código que no caben en su columna:")
        for archivo, titulo, aviso in anchas:
            print(f"  {archivo:<28} {titulo:<34} {aviso}")
        print()

    if not mostrar:
        print(f"Ninguna diapositiva pasa de {limite:.1f} líneas (umbral derivado del CSS). "
              f"Mediana {mediana:.1f} · {len(filas)} diapositivas.")
        return
    print(f"{'alto':>5}  {'página':<28} diapositiva")
    for a, f, t in mostrar:
        print(f"{a:5.1f}  {f:<28} {t[:46]}")
    print(f"\n{len(mostrar)} de {len(filas)} por encima de {limite:.1f} (umbral derivado del CSS). Mediana {mediana:.1f}.")


if __name__ == "__main__":
    main()

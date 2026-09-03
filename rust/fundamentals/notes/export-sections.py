#!/usr/bin/env python3
"""Exporta cada sección del deck (slides.md) a su propio PDF.

Una "sección" es el grupo de páginas cuyo archivo en pages/ comparte el
mismo número inicial (1.x = Sintaxis y semántica, 2.x = Memoria y ownership,
...), más las de prefijo `ap`, `cheatsheet` y `ejercicios`. Se incluye la
slide de portada de sección que la precede en slides.md. Los rangos se
calculan leyendo slides.md y pages/*.md en cada corrida, así que no hay
números de slide fijos que se rompan cuando el deck crece.

`slidev export --range` genera PDFs con las páginas en blanco (bug conocido
de esta versión con Playwright): en vez de exportar rango por rango,
exportamos el deck completo una sola vez -- eso sí es confiable -- y
partimos ese PDF con pypdf según los rangos calculados.

Uso:
    python3 export-sections.py            # exporta todas las secciones
    python3 export-sections.py 2 4        # solo Memoria y Colecciones
    python3 export-sections.py cheat      # solo el cheatsheet

Requiere: pypdf (pip install --user pypdf)
"""
import re
import subprocess
import sys
import time
import pathlib

from pypdf import PdfReader, PdfWriter

ROOT = pathlib.Path(__file__).resolve().parent
SLIDES_MD = ROOT / "slides.md"
PAGES = ROOT / "pages"
OUT = ROOT / "exports"
FULL_PDF = OUT / "_deck-completo.pdf"

SECTION_NAMES = {
    "0": "por-que-rust",
    "1": "fundamentos",
    "2": "tipos-compuestos",
    "3": "memoria",
    "4": "abstraccion",
    "5": "vocabulario-stdlib",
    "6": "indireccion",
    "7": "proyectos",
    "cheat": "cheatsheet",
    "ap": "apendices",
}

# Decks con archivo de entrada propio: no viven dentro de slides.md, así que se
# exportan por separado en vez de recortarse del PDF grande.
EXTRA_DECKS = {
    "ej": ("ejercicios.md", "ejercicios"),
}


def section_key(filename: str) -> str:
    """Sección a la que pertenece una página de pages/.

    `2.3-borrowing.md` -> "2"  ·  `ap0-cheatsheet.md` -> "cheat"
    `ap1-tokens.md` -> "ap"
    """
    stem = pathlib.Path(filename).stem
    if stem.startswith("ap0"):
        return "cheat"
    if stem.startswith("ap"):
        return "ap"
    return stem.split(".", 1)[0].split("-", 1)[0]


def export_deck(entry: str, out_path: pathlib.Path, attempts: int = 3) -> None:
    """Exporta un deck completo a PDF, reintentando si sale en blanco."""
    for intento in range(1, attempts + 1):
        subprocess.run(
            ["pnpm", "exec", "slidev", "export", entry, "--dark", "--output", str(out_path)],
            cwd=ROOT,
            check=True,
        )
        if out_path.exists() and out_path.stat().st_size > 1000 and not is_probably_blank(out_path):
            return
        print(f"   ! intento {intento} generó un PDF en blanco, reintentando...")
        time.sleep(3)
    raise RuntimeError(f"No se pudo exportar {entry} tras {attempts} intentos")


def count_slides(text: str) -> int:
    lines = text.split("\n")
    sep_idx = [i for i, l in enumerate(lines) if l.strip() == "---"]
    assert len(sep_idx) % 2 == 0, "separadores '---' desbalanceados"
    return len(sep_idx) // 2


def build_ranges() -> dict[str, list[int]]:
    lines = SLIDES_MD.read_text().split("\n")
    sep_idx = [i for i, l in enumerate(lines) if l.strip() == "---"]
    pairs = list(zip(sep_idx[0::2], sep_idx[1::2]))

    srcs = []
    for a, b in pairs:
        src = None
        for l in lines[a + 1 : b]:
            m = re.match(r"^\s*src:\s*(.+?)\s*$", l)
            if m:
                src = m.group(1)
        srcs.append(src)

    cursor = 1
    ranges: dict[str, list[int]] = {}
    pending_cover = None
    for src in srcs:
        if src is None:
            pending_cover = cursor
            cursor += 1
            continue
        name = pathlib.Path(src).name
        prefix = section_key(name)
        n = count_slides((PAGES / name).read_text())
        start = pending_cover if pending_cover is not None else cursor
        end = cursor + n - 1
        if prefix in ranges:
            ranges[prefix][1] = end
        else:
            ranges[prefix] = [start, end]
        pending_cover = None
        cursor += n
    return ranges


def is_probably_blank(pdf_path: pathlib.Path) -> bool:
    """`slidev export` a veces (contención de recursos con Playwright) escribe
    un PDF válido pero cuyas páginas son solo rectángulos de fondo -- sin texto
    real (lo vimos con streams de contenido idénticos entre sí, sin un solo
    operador Tj/TJ). Si ninguna página de la muestra tiene texto extraíble,
    asumimos que el export falló en silencio."""
    reader = PdfReader(str(pdf_path))
    n = len(reader.pages)
    if n == 0:
        return True
    step = max(1, n // 8)
    sample = [reader.pages[i] for i in range(0, n, step)]
    return not any(len((page.extract_text() or "").strip()) > 10 for page in sample)


def export_full_deck(attempts: int = 3) -> pathlib.Path:
    for attempt in range(1, attempts + 1):
        subprocess.run(
            ["pnpm", "exec", "slidev", "export", "slides.md", "--dark", "--output", str(FULL_PDF)],
            cwd=ROOT,
            check=True,
        )
        if FULL_PDF.exists() and FULL_PDF.stat().st_size > 1000 and not is_probably_blank(FULL_PDF):
            return FULL_PDF
        print(f"   ! intento {attempt} generó un PDF vacío/en blanco, reintentando...")
        time.sleep(3)
    raise RuntimeError(f"No se pudo exportar el deck completo tras {attempts} intentos")


def main() -> None:
    ranges = build_ranges()
    todas = set(ranges) | set(EXTRA_DECKS)
    wanted = {a.lower() for a in sys.argv[1:]} or todas

    unknown = wanted - todas
    if unknown:
        sys.exit(f"Secciones desconocidas: {', '.join(sorted(unknown))} (válidas: {', '.join(sorted(todas))})")

    OUT.mkdir(exist_ok=True)

    for key, (entry, nombre) in EXTRA_DECKS.items():
        if key not in wanted:
            continue
        destino = OUT / f"{key}-{nombre}.pdf"
        print(f"Exportando {entry} (deck aparte)...")
        export_deck(entry, destino)
        print(f"-> {key} ({nombre}): {destino.relative_to(ROOT)}")

    if not (wanted & set(ranges)):
        print("\nListo.")
        return

    print("Exportando el deck completo (una sola vez)...")
    full_pdf = export_full_deck()
    reader = PdfReader(str(full_pdf))
    total = len(reader.pages)

    for prefix, (start, end) in ranges.items():
        if prefix not in wanted:
            continue
        if end > total:
            sys.exit(f"Rango de {prefix} ({start}-{end}) excede las {total} páginas del PDF exportado")
        name = SECTION_NAMES.get(prefix, prefix.lower())
        out_path = OUT / f"{prefix}-{name}.pdf"
        writer = PdfWriter()
        for page_num in range(start - 1, end):
            writer.add_page(reader.pages[page_num])
        with open(out_path, "wb") as f:
            writer.write(f)
        print(f"-> {prefix} ({name}): páginas {start}-{end} -> {out_path.relative_to(ROOT)}")

    full_pdf.unlink()
    print(f"\nListo. PDFs en {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Genera la lámina naturalista de la portada en tres tonos.

El dibujo es uno solo; lo único que cambia entre variantes es la paleta. Salida
en SVG (vectorial, editable) y PNG a 1920x1080.

    python3 lamina.py
"""
import math
import random

import cairosvg

VARIANTES = {
    "claro": dict(papel="#F0EEE6", tinta="#4A3226", aguada="#CE422B",
                  fox="#C9A889", fox_op=(0.04, 0.11), grano=0.05,
                  borde=(0.45, 0.30), aguada_op=0.44, hatch_op=0.45),
    "oscuro": dict(papel="#17130F", tinta="#E6D8C4", aguada="#CE422B",
                   fox="#E8935F", fox_op=(0.03, 0.08), grano=0.07,
                   borde=(0.40, 0.25), aguada_op=0.62, hatch_op=0.38),
    "naranja": dict(papel="#D97757", tinta="#3A2015", aguada="#832918",
                    fox="#8F3A22", fox_op=(0.05, 0.12), grano=0.06,
                    borde=(0.45, 0.28), aguada_op=0.52, hatch_op=0.40),
}


def especimen():
    """Trazos y rellenos del cangrejo, en coordenadas locales 0..600 x 0..520."""
    car = ("M 122,252 C 122,180 190,134 300,134 C 410,134 478,180 478,252 "
           "C 478,318 402,348 300,350 C 198,348 122,318 122,252 Z")
    trazos, quelas = [car], []
    for sx, tx in ((1, 0), (-1, 600)):
        def X(v):
            return tx + sx * v
        trazos.append(f"M {X(148)},226 C {X(126)},206 {X(108)},184 {X(98)},158")
        trazos.append(f"M {X(160)},248 C {X(140)},226 {X(122)},202 {X(112)},176")
        quela = (f"M {X(104)},160 C {X(74)},156 {X(44)},142 {X(26)},118 L {X(14)},104 "
                 f"C {X(32)},112 {X(54)},122 {X(72)},130 L {X(78)},116 "
                 f"C {X(64)},102 {X(54)},80 {X(56)},60 L {X(48)},48 "
                 f"C {X(70)},72 {X(92)},116 {X(104)},160 Z")
        quelas.append(quela)
        trazos.append(quela)
        for i in range(6):                       # dentado del borde de agarre
            t = i / 5
            trazos.append(f"M {X(30 + 40 * t):.0f},{114 - 4 * t:.0f} l {sx * 6},-8")
        for i in range(5):
            t = i / 4
            trazos.append(f"M {X(60 + 16 * t):.0f},{102 - 40 * t:.0f} l {sx * 7},3")
        for ax, ay, l1, l2, ang in [(142, 276, 74, 66, 22), (172, 308, 80, 70, 44),
                                    (222, 334, 76, 66, 64), (266, 346, 62, 56, 82)]:
            a = math.radians(ang)
            x0, y0 = X(ax), ay
            x1, y1 = x0 - sx * l1 * math.cos(a), y0 + l1 * math.sin(a)
            x2, y2 = x1 - sx * l2 * math.cos(a - 0.30), y1 + l2 * math.sin(a - 0.30) * 0.8
            trazos.append(f"M {x0:.0f},{y0:.0f} C {x0 - sx * l1 * 0.45:.0f},{y0 + l1 * 0.30:.0f} "
                          f"{x1 + sx * 8:.0f},{y1 - 8:.0f} {x1:.0f},{y1:.0f}")
            trazos.append(f"M {x1:.0f},{y1:.0f} C {x1 - sx * l2 * 0.40:.0f},{y1 + l2 * 0.26:.0f} "
                          f"{x2 + sx * 5:.0f},{y2 - 6:.0f} {x2:.0f},{y2:.0f}")
            trazos.append(f"M {x1 - sx * 7:.0f},{y1 - 6:.0f} l {sx * 14},9")
    return trazos, [car] + quelas


def pez():
    """Un pez pequeño, de perfil y mirando a la derecha, en coords 0..110 x 0..50."""
    cuerpo = "M 14,25 C 32,7 74,7 98,25 C 74,43 32,43 14,25 Z"
    cola = "M 14,25 L -8,11 L -1,25 L -8,39 Z"
    trazos = [
        cuerpo, cola,
        "M 46,10 C 54,0 66,0 72,9",              # dorsal
        "M 50,40 C 56,48 64,48 68,41",           # ventral
        "M 76,12 C 71,25 71,25 76,38",           # opérculo
    ]
    for i in range(5):                            # hachurado del lomo
        x = 34 + i * 11
        trazos.append(f"M {x},16 C {x + 3},22 {x - 2},28 {x + 1},34")
    return trazos, [cuerpo, cola]


# posicion, escala y giro de cada pez: fuera del hueco del titulo (abajo-izquierda)
PECES = [
    (430, 600, 1.30, -8),
    (690, 268, 0.95, 12),
    (1548, 872, 1.10, -16),
    (268, 404, 0.80, 6),
]


# Contraportada: el mismo pez, sin cangrejo. Deriva diagonal de arriba-derecha a
# abajo-izquierda, dejando libre la esquina inferior izquierda para el colofón.
CARDUMEN = [
    (1548, 208, 1.45, -12),
    (1236, 322, 1.05,  -4),
    (1620, 452, 0.90, -18),
    (1362, 560, 1.25,   8),
    (1006, 214, 0.78,  14),
    (1640, 726, 1.10,  -6),
    (1268, 812, 0.85,  16),
    (1518, 948, 0.70, -10),
    ( 902, 470, 0.62,  -8),
    (1042, 660, 0.55,  10),
]


def hachurado():
    h = []
    for i in range(30):
        t = i / 29
        x = 142 + 326 * t
        y0 = 252 - math.sin(math.pi * t) * 94 + 22
        y1 = y0 + 34 + math.sin(math.pi * t) * 30
        h.append(f"M {x:.0f},{y0:.0f} C {x + 4:.0f},{(y0 + y1) / 2:.0f} "
                 f"{x - 3:.0f},{(y0 + y1) / 2:.0f} {x:.0f},{y1:.0f}")
    for i in range(16):
        t = i / 15
        x = 186 + 230 * t
        h.append(f"M {x:.0f},{306 + math.sin(math.pi * t) * 16:.0f} l 3,18")
    return h


def render(nombre, p, peces=PECES, especie=True, sufijo=""):
    random.seed(11)
    trazos, rellenos = especimen()
    hatch = hachurado()
    lo, hi = p["fox_op"]
    fox = "".join(
        f'<circle cx="{random.randint(70, 1850)}" cy="{random.randint(70, 1010)}" '
        f'r="{random.randint(5, 24)}" fill="{p["fox"]}" opacity="{random.uniform(lo, hi):.2f}"/>'
        for _ in range(40))
    b1, b2 = p["borde"]

    pz_tr, pz_rl = pez()
    peces_svg = ""
    for x, y, esc, giro in peces:
        g = f'translate({x},{y}) rotate({giro}) scale({esc})'
        peces_svg += (
            f'<g transform="{g}" filter="url(#aguada)" opacity="{p["aguada_op"] * 0.8:.2f}">'
            f'<g transform="translate(5,4)" fill="{p["aguada"]}" stroke="none">'
            + "".join(f'<path d="{d}"/>' for d in pz_rl) + '</g></g>'
            f'<g transform="{g}" fill="none" stroke="{p["tinta"]}" stroke-width="1.9" '
            f'stroke-linecap="round" stroke-linejoin="round" opacity="0.9">'
            + "".join(f'<path d="{d}"/>' for d in pz_tr)
            + f'<circle cx="86" cy="21" r="2.6" fill="{p["tinta"]}" stroke="none"/></g>')

    cangrejo = f'''<g transform="translate(890,250) scale(1.4)" filter="url(#aguada)" opacity="{p['aguada_op']}">
    <g transform="translate(8,6)" fill="{p['aguada']}" stroke="none">{"".join(f'<path d="{d}"/>' for d in rellenos)}</g>
  </g>
  <g transform="translate(890,250) scale(1.4)" fill="none" stroke="{p['tinta']}"
     stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
    {"".join(f'<path d="{d}"/>' for d in trazos)}
    <g stroke-width="1.1" opacity="{p['hatch_op']}">{"".join(f'<path d="{d}"/>' for d in hatch)}</g>
    <circle cx="254" cy="150" r="7" fill="{p['tinta']}" stroke="none"/>
    <circle cx="346" cy="150" r="7" fill="{p['tinta']}" stroke="none"/>
  </g>''' if especie else ""

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">
  <defs>
    <filter id="grano"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="4" seed="5"/>
      <feColorMatrix type="saturate" values="0"/></filter>
    <filter id="aguada" x="-25%" y="-25%" width="150%" height="150%"><feGaussianBlur stdDeviation="6"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="{p['papel']}"/>
  {fox}
  <rect width="1920" height="1080" filter="url(#grano)" opacity="{p['grano']}"/>
  <rect x="52" y="52" width="1816" height="976" fill="none" stroke="{p['tinta']}" stroke-width="2.5" opacity="{b1}"/>
  <rect x="62" y="62" width="1796" height="956" fill="none" stroke="{p['tinta']}" stroke-width="1" opacity="{b2}"/>
  {peces_svg}
  {cangrejo}
</svg>'''
    open(f"lamina-{nombre}{sufijo}.svg", "w").write(svg)
    cairosvg.svg2png(url=f"lamina-{nombre}{sufijo}.svg", write_to=f"lamina-{nombre}{sufijo}.png",
                     output_width=1920, output_height=1080)
    cairosvg.svg2png(url=f"lamina-{nombre}{sufijo}.svg", write_to=f"prev-{nombre}{sufijo}.png",
                     output_width=960, output_height=540)

    # El JPEG es lo que consume el deck. El grano (feTurbulence) del SVG obliga al
    # exportador de PDF a rasterizar la lámina sin comprimir: con SVG el PDF salió
    # de 135 MB, con JPEG baja a unos pocos. El SVG y el PNG quedan como fuente.
    try:
        from PIL import Image
        Image.open(f"lamina-{nombre}{sufijo}.png").convert("RGB").save(
            f"lamina-{nombre}{sufijo}.jpg", quality=84, optimize=True)
    except ImportError:
        print("  (falta Pillow: no se generó el .jpg, que es el que usa el deck)")


if __name__ == "__main__":
    for nombre, p in VARIANTES.items():
        render(nombre, p)
        print(f"lamina-{nombre}.svg / .png")
        render(nombre, p, peces=CARDUMEN, especie=False, sufijo="-peces")
        print(f"lamina-{nombre}-peces.svg / .png")

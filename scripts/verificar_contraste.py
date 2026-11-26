
"""Verifica contrastes WCAG AA en los temas de AIRLINCOLN."""

import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def luminancia(color):
    color = color.lstrip("#")
    valores = [int(color[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    canales = [
        v / 12.92 if v <= 0.04045
        else ((v + 0.055) / 1.055) ** 2.4
        for v in valores
    ]
    return sum(a * b for a, b in zip(canales, (0.2126, 0.7152, 0.0722)))


def contraste(a, b):
    l1, l2 = luminancia(a), luminancia(b)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


def leer_tema_python():
    ruta = ROOT / "ui" / "theme.py"
    arbol = ast.parse(ruta.read_text(encoding="utf-8"))

    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign):
            nombres = [
                t.id for t in nodo.targets
                if isinstance(t, ast.Name)
            ]
            if "COLORS" in nombres:
                return ast.literal_eval(nodo.value)

    raise ValueError("No se encontró COLORS en theme.py")


def leer_temas_html():
    ruta = ROOT / "ui" / "dashboard_template.html"
    contenido = ruta.read_text(encoding="utf-8")

    selectores = {
        "Dashboard claro": r":root\s*\{([^{}]*)\}",
        "Dashboard oscuro": r':root\[data-theme=["\']dark["\']\]\s*\{([^{}]*)\}',
    }

    temas = {}
    for nombre, patron in selectores.items():
        encontrado = re.search(patron, contenido)
        if not encontrado:
            raise ValueError(f"No se encontró el tema: {nombre}")

        variables = re.findall(
            r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\s*;",
            encontrado.group(1)
        )
        temas[nombre] = dict(variables)

    return temas


PRUEBAS_PYTHON = [
    ("text", "bg", 4.5),
    ("text", "panel", 4.5),
    ("muted", "bg", 4.5),
    ("muted", "panel", 4.5),
    ("muted", "soft", 4.5),
    ("blue", "blue_soft", 4.5),
    ("blue", "panel", 4.5),
    ("green", "green_soft", 4.5),
    ("amber", "amber_soft", 4.5),
    ("red", "red_soft", 4.5),
    ("green", "panel", 4.5),
    ("amber", "panel", 4.5),
    ("red", "panel", 4.5),
    ("grey", "panel", 3.0),
]

PRUEBAS_HTML = [
    ("fg", "bg", 4.5),
    ("fg", "panel", 4.5),
    ("muted", "bg", 4.5),
    ("muted", "panel", 4.5),
    ("muted", "soft", 4.5),
    ("accent", "panel", 4.5),
    ("accent", "accent-soft", 4.5),
    ("ok", "panel", 4.5),
    ("ok", "ok-soft", 4.5),
    ("warn", "panel", 4.5),
    ("warn", "warn-soft", 4.5),
    ("bad", "panel", 4.5),
    ("bad", "bad-soft", 4.5),
]

errores = []
total = 0


def verificar(nombre, colores, pruebas):
    global total

    print(f"\n{nombre}")
    print("-" * 60)

    for primero, segundo, minimo in pruebas:
        total += 1

        if primero not in colores or segundo not in colores:
            errores.append(f"{nombre}: falta {primero} o {segundo}")
            print(f"{primero}/{segundo}: ERROR - color inexistente")
            continue

        resultado = contraste(colores[primero], colores[segundo])
        cumple = resultado >= minimo

        print(
            f"{primero}/{segundo}: {resultado:.2f}:1 "
            f"(mínimo {minimo}:1) - "
            f"{'OK' if cumple else 'FALLÓ'}"
        )

        if not cumple:
            errores.append(f"{nombre}: {primero}/{segundo}")


print("VERIFICACIÓN DE CONTRASTE WCAG AA - AIRLINCOLN")

verificar("Componentes Streamlit", leer_tema_python(), PRUEBAS_PYTHON)

temas = leer_temas_html()
for nombre, colores in temas.items():
    verificar(nombre, colores, PRUEBAS_HTML)

print(f"\nTotal de combinaciones verificadas: {total}")

if errores:
    print(f"\nERROR: {len(errores)} combinaciones insuficientes")
    for error in errores:
        print(f" - {error}")
    raise SystemExit(1)

print("\nOK: Todas las combinaciones configuradas cumplen.")

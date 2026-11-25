
"""Verifica los contrastes de la paleta real de AIRLINCOLN."""

import ast
from pathlib import Path

RUTA = Path(__file__).resolve().parents[1] / "ui" / "theme.py"

# Lee los colores reales sin ejecutar Streamlit.
arbol = ast.parse(RUTA.read_text(encoding="utf-8"))

colores = None
for nodo in arbol.body:
    if isinstance(nodo, ast.Assign):
        if any(
            isinstance(t, ast.Name) and t.id == "COLORS"
            for t in nodo.targets
        ):
            colores = ast.literal_eval(nodo.value)
            break

if colores is None:
    raise SystemExit("ERROR: No se encontró COLORS en theme.py")


def luminancia(hexadecimal):
    valores = [
        int(hexadecimal[i:i + 2], 16) / 255
        for i in (1, 3, 5)
    ]
    canales = [
        v / 12.92 if v <= 0.04045
        else ((v + 0.055) / 1.055) ** 2.4
        for v in valores
    ]
    return (
        0.2126 * canales[0]
        + 0.7152 * canales[1]
        + 0.0722 * canales[2]
    )


def contraste(color1, color2):
    l1 = luminancia(color1)
    l2 = luminancia(color2)
    claro, oscuro = max(l1, l2), min(l1, l2)
    return (claro + 0.05) / (oscuro + 0.05)


# Combinaciones de texto utilizadas por el tema.
pruebas = [
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

    # Elementos gráficos significativos
    ("grey", "panel", 3.0),
]

errores = []

print("VERIFICACIÓN WCAG 2.2 AA - AIRLINCOLN")
print("-" * 55)

for primero, segundo, minimo in pruebas:
    resultado = contraste(
        colores[primero], colores[segundo]
    )
    cumple = resultado >= minimo
    estado = "OK" if cumple else "FALLÓ"

    print(
        f"{primero}/{segundo}: "
        f"{resultado:.2f}:1 "
        f"(mínimo {minimo}:1) - {estado}"
    )

    if not cumple:
        errores.append((primero, segundo))

if errores:
    print(f"\nERROR: {len(errores)} contrastes insuficientes")
    raise SystemExit(1)

print("\nOK: Todas las combinaciones configuradas cumplen.")

https://airlincoln-entregable3.streamlit.app/

# Air Lincoln · Inteligencia de No-show (Streamlit)

## Ejecutar en Visual Studio Code (Windows)

En la terminal, dentro de esta carpeta:

```powershell
python -m venv .venv                                   # solo la primera vez (omitir si .venv ya existe)
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

La primera carga entrena los 5 modelos (≈20 s); después queda en caché.

Pruebas de cálculo: `.venv\Scripts\python.exe -m pip install pytest` y luego `.venv\Scripts\python.exe -m pytest -q`

## Estructura

| Carpeta | Contenido |
|---|---|
| `app.py` | Entrada: encabezado global, selector de perfil y manejo de errores |
| `core/` | Datos, modelos, simulador de sobreventa, calidad, reglas de intervención, seguridad y textos |
| `ui/` | Tema oscuro, componentes, gráficas Plotly y estado de sesión |
| `views/` | Laura, Armando, Anna y Acerca del producto |
| `data/` | `AIRLINCOLNDATA2.csv` (y opcionalmente `particion.csv` con la partición oficial) |
| `tests/` | Pruebas de consistencia numérica |

## Inicio de sesión (opcional)

Sin configuración la app funciona como vista pública (solo agregados). Para activar OIDC, roles y seudónimos,
copia `.streamlit/secrets.toml.example` como `.streamlit/secrets.toml` y complétalo. En Streamlit Community Cloud,
pega el contenido en *Settings → Secrets*.

## Pipeline de validación de datos (Entregable 2)

En cada push y pull request, GitHub Actions (`.github/workflows/validar-datos.yml`):
1. valida `data/AIRLINCOLNDATA2.csv` contra el contrato (`python scripts/validar_datos.py`);
2. corre las pruebas (`python -m pytest -q`).

Si el dato se rompe (texto en una columna numérica, código fuera de rango, columna faltante, variable derivada incoherente), la corrida queda en rojo y el cambio se detiene. El contrato está en [`contrato-datos.md`](contrato-datos.md).

### Evidencia de validación y corrección del pipeline

**Validación automática WCAG**

Se implementó un workflow de GitHub Actions para verificar los contrastes de color del dashboard.

La primera ejecución presentó un error de configuración: `No event triggers defined in on`. El workflow fue corregido y las ejecuciones posteriores finalizaron correctamente.

**Ejecución aprobada:**
[Ver GitHub Actions WCAG #8](https://github.com/MoisesC27/M4C-Entregable-3-del-m-dulo/actions/runs/45736483277)

**Error inicial de configuración:**
[Ver GitHub Actions WCAG #1](https://github.com/MoisesC27/M4C-Entregable-3-del-m-dulo/actions/runs/45721594481)

**Validación de datos**

El proyecto incluye validaciones de estructura, tipos de datos y valores antes de utilizar los archivos en el dashboard.

Se documentó un caso de prueba que consiste en cambiar un valor `0` por el texto `abc` en la columna `No_Show`, utilizando la rama `prueba-dato-roto`.

Aunque se describió el procedimiento, todavía no se ha verificado en este repositorio una ejecución fallida específica que demuestre el rechazo automático de ese dato.

**Conclusión:** La validación automatizada de contraste WCAG tiene ejecuciones aprobadas. La evidencia de rechazo de datos incorrectos mediante GitHub Actions queda pendiente de verificación.


**Conclusión:** El pipeline de contraste WCAG cuenta con ejecuciones aprobadas. La evidencia de rechazo automático de datos incorrectos queda pendiente de verificación.

Cómo se rompió a propósito:
1. Rama `prueba-dato-roto`: en la fila 6 del CSV, `No_Show` se cambió de `0` a `abc`.
2. Push → la acción falló con «No_Show: 1 valores con texto en una columna numérica».
3. Se borró la rama; `main` sigue en verde.

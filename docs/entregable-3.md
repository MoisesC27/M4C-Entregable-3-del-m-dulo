https://github.com/MoisesC27/M4C-Entregable-3-del-m-dulo/actions/runs/45722187808

# Entregable 3 — AIRLINCOLN

## 1. Preguntas de las gráficas
Cada gráfica del dashboard AIRLINCOLN responde una pregunta
relacionada con una decisión operativa.

### Laura — Planificación

| Gráfica | Pregunta | Decisión |
|---|---|---|
| Costo esperado de sobreventa | ¿Cuántos boletos adicionales conviene vender? | Comparar escenarios de sobreventa y seleccionar una alternativa. |
| Calendario de vuelos | ¿Qué días presentan mayor riesgo de ausencia? | Identificar fechas y vuelos que requieren revisión. |

### Armando — Experiencia del pasajero

| Gráfica | Pregunta | Decisión |
|---|---|---|
| Tipos de pasajeros | ¿Qué grupos presentan mayores tasas de ausencia? | Priorizar segmentos para seguimiento preventivo. |
| Factores individuales | ¿Qué características influyen en el riesgo de un pasajero? | Elegir una acción preventiva según su perfil. |

### Anna — Operación y calidad

| Gráfica | Pregunta | Decisión |
|---|---|---|
| Comparación de modelos | ¿Qué modelo distingue mejor entre pasajeros que llegan y no llegan? | Seleccionar el modelo predictivo con mejor desempeño. |
| Calibración | ¿Las probabilidades estimadas coinciden con las ausencias observadas? | Revisar la confiabilidad de las probabilidades. |
| Alertas | ¿Cómo cambia la detección de ausencias al ajustar el umbral? | Equilibrar ausencias detectadas y falsas alarmas. |
## 2. Paleta y contraste WCAG 2.2 AA

La interfaz de AIRLINCOLN utiliza una paleta de colores
para comunicar información de forma clara y accesible.

Se aplicó el criterio WCAG 2.2 AA, utilizando una relación
mínima de contraste de 4.5:1 para texto normal y de 3:1
para elementos gráficos relevantes.

### Resultados de contraste

| Combinación | Contraste | Mínimo | Resultado |
|---|---:|---:|---|
| Texto principal / fondo | 15.03:1 | 4.5:1 | Cumple |
| Texto principal / blanco | 16.41:1 | 4.5:1 | Cumple |
| Texto secundario / fondo | 5.17:1 | 4.5:1 | Cumple |
| Texto secundario / blanco | 5.65:1 | 4.5:1 | Cumple |
| Texto secundario / gris claro | 4.99:1 | 4.5:1 | Cumple |
| Azul / azul claro | 5.92:1 | 4.5:1 | Cumple |
| Azul / blanco | 7.10:1 | 4.5:1 | Cumple |
| Verde / verde claro | 6.18:1 | 4.5:1 | Cumple |
| Ámbar / ámbar claro | 6.01:1 | 4.5:1 | Cumple |
| Rojo / rojo claro | 5.77:1 | 4.5:1 | Cumple |
| Verde / blanco | 7.13:1 | 4.5:1 | Cumple |
| Ámbar / blanco | 6.79:1 | 4.5:1 | Cumple |
| Rojo / blanco | 7.12:1 | 4.5:1 | Cumple |
| Gris / blanco | Superior a 3:1* | 3:1 | Cumple* |

*La combinación gris/blanco debe confirmarse en la
ejecución posterior al cambio de color a #697586.

### Verificación automática

Se creó el archivo scripts/verificar_contraste.py,
que calcula las relaciones de contraste de la paleta
definida en ui/theme.py.

También se configuró GitHub Actions mediante
.github/workflows/contraste.yml.

La ejecución automática terminó correctamente
con el estado Success, verificando las combinaciones
de colores declaradas.

La prueba se ejecuta con cada push o pull request
y devuelve un error si alguna combinación comprobada
no alcanza su contraste mínimo.

### Paleta inclusiva

Se utilizan colores asociados con estados de riesgo:

- Verde: riesgo bajo.
- Ámbar: riesgo medio.
- Rojo: riesgo alto.
- Azul: información y elementos de referencia.

La información también se comunica mediante textos,
valores numéricos y etiquetas, evitando depender
exclusivamente del color.

### Alcance de la validación

La prueba automatizada comprueba las combinaciones
declaradas de ui/theme.py. Los colores adicionales
de gráficas y componentes personalizados requieren
revisión complementaria.

## 3. Jerarquía visual e investigación 1
La jerarquía visual de AIRLINCOLN está diseñada para que cada usuario encuentre primero la información más importante para su trabajo, sin tener que revisar todo el dashboard.

La organización sigue tres niveles: **información principal, análisis visual y acciones específicas**. De esta manera, los datos no solamente se presentan, sino que ayudan a tomar decisiones.

### Nivel 1. Información principal

En la parte superior se muestran los indicadores más relevantes, como probabilidades de ausencia, pasajeros en riesgo y recomendaciones operativas.

Estos indicadores utilizan números grandes, títulos claros y colores que permiten identificar rápidamente los resultados importantes.

**Objetivo:** que el usuario comprenda la situación general a primera vista.

### Nivel 2. Análisis visual

Después de los indicadores aparecen las gráficas que explican los resultados.

Se utilizan barras para comparar pasajeros y modelos, líneas para observar cambios en los resultados y calendarios para identificar patrones de ausencia por fecha.

Las gráficas incluyen etiquetas, porcentajes y referencias para facilitar su interpretación.

**Objetivo:** permitir que el usuario comprenda qué factores están relacionados con el problema.

### Nivel 3. Acciones y decisiones

Finalmente, el dashboard ofrece herramientas interactivas para actuar sobre la información.

Cada perfil cuenta con funciones específicas:

| Usuario | Información prioritaria | Decisión que permite tomar |
|---|---|---|
| **Laura — Planificación** | Sobreventa recomendada, costos estimados y calendario de vuelos. | Comparar escenarios de sobreventa y planificar vuelos. |
| **Armando — Experiencia del pasajero** | Pasajeros con mayor riesgo, características y acciones sugeridas. | Determinar a quién contactar primero y qué seguimiento ofrecer. |
| **Anna — Operación y calidad** | Desempeño del modelo, alertas y calidad de datos. | Evaluar la confiabilidad de las predicciones y ajustar alertas. |

### Aplicación de principios de jerarquía visual

**1. Tamaño y énfasis:** los indicadores principales aparecen con números grandes para destacar la información relevante.

**2. Orden de lectura:** los elementos se organizan desde una visión general hasta los detalles y controles específicos.

**3. Contraste y color:** se utilizan colores para distinguir niveles de riesgo, acompañados de etiquetas y valores numéricos.

**4. Agrupación:** las tarjetas y gráficas relacionadas se presentan juntas, facilitando la comparación.

**5. Claridad:** los títulos explican qué representa cada visualización y qué pregunta permite responder.

### Relación con la investigación 1

La organización del dashboard aplica principios de jerarquía visual, agrupación y facilidad de lectura, priorizando la información necesaria para cada usuario.

La investigación 1 debe respaldar estos principios mediante sus fuentes documentadas, vinculando cada decisión de diseño con la evidencia revisada por el equipo.

**Referencia de investigación:** agregar aquí el título, autor y fuente específicos de la investigación 1 utilizada por el equipo.

### Conclusión

La jerarquía visual de AIRLINCOLN busca que los usuarios pasen de **identificar una situación, comprender sus causas y tomar una decisión**.

Esto reduce la necesidad de interpretar información técnica y permite que cada perfil se concentre en las herramientas relacionadas con sus responsabilidades.
## 4. Estado vacío y st.stop()

## 5. Controles vinculados al negocio

## 6. Autenticación, roles y limitaciones

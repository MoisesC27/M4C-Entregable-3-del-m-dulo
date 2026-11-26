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
### Control del estado vacío

AIRLINCOLN contempla el estado en el que el usuario todavía no ha seleccionado un archivo de datos.

El comportamiento esperado consiste en mostrar un mensaje indicando que se debe cargar un archivo Excel o CSV, o seleccionar el conjunto de datos de ejemplo.

Cuando no existe una fuente de datos seleccionada, la aplicación debe detener el procesamiento mediante `st.stop()`, evitando ejecutar modelos o generar resultados sin información válida.

### Validación requerida

Para comprobar este comportamiento se realizarán las siguientes verificaciones:

1. Abrir AIRLINCOLN sin cargar un archivo.
2. Confirmar que aparece el mensaje correspondiente.
3. Verificar que no se ejecutan las operaciones que requieren datos.
4. Identificar en el código la condición que utiliza `st.stop()`.

**Evidencia:** agregar una captura de la pantalla sin datos y otra del fragmento de código que implementa la detención.

**Estado:** pendiente de confirmar mediante la revisión de `app.py` y una prueba funcional.
## 5. Controles vinculados al negocio
### Control 1. Simulador de sobreventa

**Pregunta de negocio:** ¿Cuántos boletos adicionales conviene vender para reducir las pérdidas por asientos vacíos sin incrementar excesivamente el riesgo de negar abordaje?

El simulador permite a Laura seleccionar el día, horario, tipo de salida, destino y condiciones del clima. También permite modificar la capacidad del avión y los costos operativos.

A partir del escenario seleccionado, AIRLINCOLN muestra la sobreventa recomendada, la probabilidad estimada de No-Show, el riesgo de negar abordaje y el ahorro esperado.

**Ejemplo observado:** para el escenario seleccionado, el sistema recomienda vender 30 boletos adicionales sobre una capacidad de 180 asientos y estima un ahorro de $58,840 MXN frente a no sobrevender.

**Decisión:** comparar escenarios y elegir una estrategia de sobreventa basada en costos y riesgos.

### Control 2. Calendario interactivo de vuelos

**Pregunta de negocio:** ¿Qué fechas y vuelos requieren mayor atención por presentar riesgos de ausencia?

El calendario permite seleccionar fechas y consultar información de vuelos relacionada con la fecha elegida.

Al seleccionar un día, el panel lateral presenta los vuelos correspondientes, sus horarios, rutas, capacidad y estimaciones de No-Show.

**Ejemplo observado:** al seleccionar el domingo 30 de agosto de 2026, el panel muestra 24 vuelos en la sección de mañana, con sus indicadores individuales.

**Decisión:** identificar los vuelos que requieren revisión y evaluar su planificación o sobreventa.

### Visibilidad de los controles

Los controles muestran sus valores seleccionados y los indicadores se presentan junto con el escenario analizado.

El dashboard también distingue entre datos originales, resultados calculados y escenarios simulados mediante las etiquetas DATO, CALCULADO y SIMULADO.

### Validación pendiente

Se debe realizar una prueba funcional cambiando al menos un valor de cada control y comprobando que se actualicen los resultados relacionados.

También debe confirmarse que la interfaz muestre el número de registros correspondientes al filtro activo y no solamente el total histórico del archivo.

### Evidencias

- Captura del simulador de sobreventa con los filtros seleccionados y sus indicadores.
- Captura del calendario con una fecha seleccionada y los vuelos correspondientes.
- Capturas comparativas que demuestren la actualización de resultados al cambiar los controles.
### Pruebas funcionales realizadas

Se realizaron pruebas modificando los controles del simulador y seleccionando distintas fechas y vuelos en el calendario.

**Prueba 1. Simulador de sobreventa**

En un escenario inicial, el sistema recomendó 30 boletos adicionales y calculó un ahorro estimado de $58,840 MXN.

Al cambiar las características del escenario, la recomendación pasó a 27 boletos adicionales y el ahorro estimado a $51,237 MXN.

Esto demuestra que el simulador actualiza sus resultados conforme a los parámetros seleccionados.

**Prueba 2. Calendario de vuelos**

Se seleccionaron diferentes fechas del calendario y se comprobó que el panel de vuelos cambia según la fecha elegida.

Para el jueves 11 de junio de 2026 se observaron 26 vuelos en la sección de mañana, con una tasa de No-Show del 23 % para ese grupo.

Al seleccionar un vuelo, sus características se transfirieron al simulador, permitiendo evaluar la sobreventa correspondiente.

**Conclusión**

Ambos controles permiten explorar situaciones operativas y utilizar los resultados para apoyar decisiones de planificación. Los filtros seleccionados son visibles y se muestran conteos de vuelos y pasajeros en distintos niveles de detalle.
## 6. Autenticación, roles y limitaciones
### Sistema de autenticación

AIRLINCOLN incorpora un inicio de sesión individual mediante nombre de usuario y contraseña.

El sistema utiliza el módulo `core/auth.py` para verificar las credenciales antes de permitir el acceso a la aplicación. Las contraseñas se comprueban mediante hashes PBKDF2, y las credenciales se configuran de forma privada mediante Streamlit Secrets.

La aplicación cuenta con tres perfiles que corresponden a diferentes necesidades operativas.

### Matriz de acceso por roles

| Función | Laura — Planificación | Armando — Experiencia del pasajero | Anna — Operación y calidad |
|---|---|---|---|
| Iniciar sesión | Sí | Sí | Sí |
| Cargar y analizar datos | Sí | Sí | Sí |
| Simulador de sobreventa | Sí | No | No |
| Calendario de vuelos | Sí | No | No |
| Priorización de contactos | No | Sí | No |
| Análisis de grupos de riesgo | No | Sí | No |
| Evaluación de modelos | No | No | Sí |
| Revisión de calidad de datos | No | No | Sí |
| Ajustar el umbral oficial de alertas | No | No | Sí |

### Diferenciación funcional

**Laura — Planificación**

Accede al simulador de sobreventa y al calendario de vuelos. Su función consiste en evaluar escenarios de costos, identificar fechas de riesgo y decidir cuántos boletos adicionales conviene vender.

**Armando — Experiencia del pasajero**

Accede a herramientas enfocadas en identificar pasajeros y grupos con mayor riesgo de ausencia. Su función consiste en priorizar el seguimiento preventivo y revisar los casos que requieren atención.

**Anna — Operación y calidad**

Accede a herramientas para evaluar la confiabilidad del modelo, revisar la calidad de los datos y ajustar el umbral de alerta. El umbral autorizado por Anna se utiliza en los análisis de los diferentes perfiles.

### Implementación técnica

La aplicación verifica la identidad del usuario antes de mostrar el dashboard.

El usuario autenticado se conserva durante la sesión y se utiliza para construir el contenido correspondiente a su perfil.

En `app.py`, la función `dashboard()` obtiene el usuario autenticado y utiliza `build_payload(ctx, user, lock=True, threshold=thr)` para preparar los datos del dashboard.

La actualización del umbral se restringe mediante una comprobación del usuario `anna`, evitando que otros perfiles lo modifiquen a través de esa operación.

### Limitaciones

La autenticación y los permisos están diseñados para los tres perfiles definidos en el proyecto académico.

El sistema no incorpora una plataforma empresarial de administración de identidades, recuperación automática de contraseñas ni auditoría integral de todas las acciones.

La diferenciación visual entre perfiles debe complementarse con verificaciones de autorización en las operaciones sensibles.

Las credenciales privadas deben permanecer fuera del repositorio público.

### Evidencia pendiente

Se realizarán pruebas iniciando sesión con cada perfil para confirmar que:

1. Laura accede a planificación y sobreventa.
2. Armando accede al seguimiento de pasajeros.
3. Anna accede a la evaluación del modelo y al ajuste de alertas.
4. Los usuarios no pueden modificar el umbral oficial sin contar con el permiso correspondiente.
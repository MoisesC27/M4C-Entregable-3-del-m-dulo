https://github.com/MoisesC27/M4C-Entregable-3-del-m-dulo/actions/runs/45735627527

# Entregable 3 — AIRLINCOLN

## 1. Preguntas de las gráficas

Cada visualización de AIRLINCOLN responde una pregunta
relacionada con el objetivo de reducir el impacto
operativo de las ausencias de pasajeros.

### Laura — Planificación

| Visualización | Pregunta de negocio | Decisión |
|---|---|---|
| Costo esperado de sobreventa | ¿Cuántos boletos adicionales minimizan el costo esperado del vuelo? | Seleccionar una cantidad de sobreventa considerando los costos y riesgos. |
| Calendario de vuelos | ¿Qué días y horarios presentan mayor tasa de No-Show? | Identificar las fechas y los horarios con mayores tasas de ausencia para planificar los vuelos. |
| Vuelos del día | ¿Qué vuelos de la fecha seleccionada requieren mayor atención por su riesgo de No-Show? | Identificar los vuelos que necesitan revisión y seleccionar uno para planificar su sobreventa en el simulador. |

### Armando — Experiencia del pasajero

| Visualización | Pregunta de negocio | Decisión |
|---|---|---|
| Acciones preventivas | ¿Cuántos pasajeros de alto riesgo requieren cada acción preventiva? | Priorizar el seguimiento de pasajeros. |
| Comparación de segmentos | ¿Qué tipo de pasajero falta más? | Identificar los grupos con mayores tasas de ausencia. |
| Factores individuales | ¿Qué factores aumentan o disminuyen el riesgo de No-Show de este pasajero? | Comprender el riesgo individual y orientar el seguimiento. |

### Anna — Operación y calidad

| Visualización | Pregunta de negocio | Decisión |
|---|---|---|
| Comparación de modelos | ¿Qué modelo predice mejor las ausencias de pasajeros? | Comparar los modelos mediante su desempeño predictivo. |
| Calibración | ¿Las probabilidades coinciden con la realidad? | Evaluar si las probabilidades estimadas reflejan las ausencias observadas. |
| Detección y falsas alarmas | ¿Cómo cambia la detección de No-Show y las falsas alarmas al ajustar el umbral? | Seleccionar un umbral que equilibre la detección y las alertas innecesarias. |

### Justificación de las visualizaciones

Las visualizaciones se conservaron porque permiten
responder preguntas relacionadas con las decisiones
de cada perfil.

Laura analiza escenarios de sobreventa y vuelos.
Armando identifica pasajeros y grupos que necesitan
seguimiento.
Anna evalúa el desempeño de los modelos y los umbrales
de alerta.

Los títulos de las gráficas están escritos como
preguntas y se muestran directamente en la aplicación.

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
| Gris / blanco | 4.68:1 | 4.5:1 | Cumple |


*La combinación gris/blanco debe confirmarse en la
ejecución posterior al cambio de color a #697586.

**Nota de validación:** La comprobación inicial se amplió posteriormente mediante `scripts/verificar_contraste.py`, que evalúa 40 combinaciones de colores definidas para la interfaz y sus temas claro y oscuro.

GitHub Actions confirmó la ejecución correcta de estas pruebas. La validación automatizada cubre las combinaciones declaradas en el script, pero no constituye una auditoría completa de todos los elementos visuales conforme a WCAG 2.2 AA.


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
### Verificación ampliada en GitHub Actions

Se amplió el script `scripts/verificar_contraste.py` para comprobar 40 combinaciones de contraste correspondientes a los componentes de Streamlit y los temas claro y oscuro del dashboard.

La ejecución número 5 de GitHub Actions terminó correctamente con el estado `Success`, utilizando el commit `3cdf426`.

Esta verificación automatizada permite detectar cuando alguna de las combinaciones configuradas deja de cumplir el contraste mínimo establecido.

La validación cubre las combinaciones declaradas en el script; otros elementos gráficos y bordes requieren una revisión adicional.

### Paleta inclusiva

### Evidencia de interpretación sin depender del color

Se revisó la gráfica «¿Qué tipo de pasajero falta más?» del perfil Armando para comprobar que las categorías puedan interpretarse sin depender exclusivamente del color.

La visualización utiliza nombres de grupos, porcentajes, longitud de barras y una línea de referencia correspondiente al promedio general de No-Show del 10 %.

Por ejemplo, el grupo «Compró con 2+ semanas» presenta una tasa del 68 %, mientras que «Coach» presenta una tasa del 8 %. Estos valores pueden identificarse mediante las etiquetas numéricas, incluso si el usuario no distingue los colores de las barras.

La leyenda también describe el significado de las categorías: menos que el promedio, hasta dos veces el promedio y más de dos veces el promedio.

Esta implementación permite interpretar la gráfica utilizando información textual y cuantitativa, además del color.

**Alcance:** se comprobó visualmente esta gráfica. La validación completa de la paleta para distintos tipos de daltonismo requiere revisar también las demás visualizaciones y sus estados.

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

### Fundamentación teórica de la jerarquía visual

De acuerdo con Gordon (2021), la jerarquía visual permite organizar los elementos de una interfaz para que el usuario identifique la información siguiendo su importancia. Para lograrlo se utilizan recursos como el tamaño, el contraste y la agrupación.

En AIRLINCOLN aplicamos estos principios de la siguiente manera:

- **Tamaño:** destacamos las recomendaciones de sobreventa, los pasajeros de alto riesgo y las métricas de evaluación mediante indicadores grandes.
- **Contraste:** diferenciamos la información prioritaria de los elementos secundarios mediante contrastes visuales.
- **Agrupación:** organizamos las gráficas y los controles relacionados dentro de secciones que corresponden a decisiones específicas.
- **Orden de lectura:** presentamos primero los resultados relevantes y después los elementos que permiten analizarlos o modificarlos.

Estas decisiones buscan facilitar que Laura, Armando y Anna identifiquen la información necesaria para sus respectivas responsabilidades.

**Referencia bibliográfica:**

Gordon, K. (2021, 17 de enero). *Visual Hierarchy in UX: Definition*. Nielsen Norman Group. https://www.nngroup.com/articles/visual-hierarchy-ux-definition/

### Conclusión

La jerarquía visual de AIRLINCOLN busca que los usuarios pasen de **identificar una situación, comprender sus causas y tomar una decisión**.

Esto reduce la necesidad de interpretar información técnica y permite que cada perfil se concentre en las herramientas relacionadas con sus responsabilidades.
## 4. Estado vacío y st.stop()
### Control del estado vacío

AIRLINCOLN contempla el caso en el que el usuario inicia sesión, pero todavía no selecciona un archivo de datos.

La función `data_screen()` de `app.py` presenta las opciones para cargar un archivo CSV o Excel, así como utilizar el conjunto de datos de ejemplo.

Mientras no exista una fuente de datos seleccionada, la aplicación muestra el siguiente mensaje:

**«Selecciona un archivo Excel o CSV, o utiliza el archivo de ejemplo para continuar».**

Después ejecuta `st.stop()` para detener el procesamiento de esa ejecución.

### Ubicación del código

**Archivo:** `app.py`  
**Función:** `data_screen()`  
**Ubicación:** después de `top_bar(show_change=False)`.

```python
top_bar(show_change=False)

st.info("Selecciona un archivo Excel o CSV, o utiliza el archivo de ejemplo para continuar.")
st.stop()
```

### Comportamiento esperado

1. Cuando el usuario inicia sesión sin seleccionar datos, aparece la pantalla de carga.
2. El sistema muestra el mensaje informativo.
3. El dashboard no ejecuta cálculos con datos inexistentes.
4. Cuando se selecciona un archivo válido, el sistema permite continuar y genera el dashboard.

También se utiliza `st.stop()` cuando un archivo no cumple las condiciones necesarias para ser analizado.

### Evidencia de validación

Para demostrar este comportamiento se conservará una captura de la aplicación sin archivo seleccionado y otra con el dashboard funcionando después de cargar el archivo de ejemplo.

La prueba se considera completada cuando ambos comportamientos se comprueban en la aplicación publicada.
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

### Validación de filtros y conteos

Se comprobó que los controles del simulador muestran los filtros activos y la cantidad de pasajeros históricos que corresponden al escenario seleccionado.

En la prueba se utilizaron los siguientes valores:

- Día: lunes.
- Horario: mañana (6–12).
- Salida desde hub: sí.
- Destino: internacional.
- Pronóstico del clima: normal.

Para esta combinación, el sistema mostró una base de **12 pasajeros históricos** y generó una recomendación simulada de **108 boletos adicionales** sobre una capacidad de 180 asientos.

Esto demuestra que el conteo correspondiente al escenario se presenta junto con los resultados del simulador.

Debido al tamaño reducido de la muestra, esta recomendación debe interpretarse con precaución y no utilizarse directamente para tomar una decisión operativa sin validación adicional.

También se comprobó que el calendario permite seleccionar fechas y muestra conteos de vuelos correspondientes al periodo seleccionado.

**Resultado:** ambos controles están vinculados a decisiones del negocio, presentan los valores seleccionados y muestran conteos asociados a la información consultada.

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

### Estado de las pruebas de acceso

Se comprobó el acceso a la aplicación publicada en Streamlit Cloud con los tres perfiles:

- **Laura:** acceso al simulador de sobreventa y al calendario de vuelos.
- **Armando:** acceso a contactos, segmentos de riesgo y evaluación individual de pasajeros.
- **Anna:** acceso a evaluación de modelos, ajuste de alertas y calidad de datos.

Se verificó visualmente que Armando no dispone de la sección exclusiva «Ajustar alertas», mientras que Anna sí puede acceder a ella.

La restricción de modificación del umbral también está implementada en `app.py` mediante la condición `user == "anna"`.

**Pendiente:** realizar una prueba funcional negativa de modificación no autorizada para comprobar la protección más allá de la interfaz.

### Evidencia de pruebas por usuario

Se realizaron pruebas de acceso a AIRLINCOLN con los tres perfiles configurados.

**Laura — Planificación**

Se verificó el acceso al simulador de sobreventa y al calendario de vuelos, herramientas orientadas a la planificación operativa.

**Armando — Experiencia del pasajero**

Se verificó que el usuario accede a las secciones «A quién contactar», «Quién falta más» y «Revisar un pasajero».

En el conjunto de datos de prueba se identificaron 101 pasajeros con riesgo alto, clasificados según la acción preventiva recomendada.

**Anna — Operación y calidad**

Se verificó el acceso a las secciones «¿El modelo es confiable?», «Ajustar alertas» y «Calidad de datos».

El dashboard muestra métricas para evaluar modelos y un control de umbral de alertas, inicialmente establecido en 80 %.

**Resultado**

Las capturas muestran que los tres usuarios reciben interfaces diferenciadas según sus responsabilidades.

La prueba visual confirma la separación de funciones. Para completar la verificación de permisos, es necesario comprobar también que los usuarios sin autorización no puedan modificar el umbral oficial.


### Evidencia de separación de roles

Se probó la aplicación publicada en Streamlit Cloud con dos usuarios autenticados.

**Armando — Experiencia del pasajero:** puede acceder a «A quién contactar», «Quién falta más» y «Revisar un pasajero». No aparece la sección «Ajustar alertas», reservada para Anna.

**Anna — Operación y calidad:** puede acceder a «¿El modelo es confiable?», «Ajustar alertas» y «Calidad de datos». Se comprobó que «Ajustar alertas» muestra el control del umbral, los resultados de detección y la gráfica correspondiente.

Esta prueba confirma la separación visual de las funciones por perfil. La autorización para modificar el umbral también se comprueba en el código Python mediante la condición `user == "anna"`.

**Limitación:** la evidencia visual no demuestra por sí sola que todos los accesos no autorizados estén bloqueados; se requiere una prueba funcional negativa para verificarlo completamente.

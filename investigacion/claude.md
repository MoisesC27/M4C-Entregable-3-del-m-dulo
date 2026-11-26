# Investigación · El ciclo de desarrollo con un asistente de IA

**Proyecto:** AIRLINCOLN — Inteligencia de No-Show  
**Tema:** Ciclo de desarrollo de software asistido por inteligencia artificial  
**Referencia principal:** Anthropic, *The AI-native SDLC Playbook*, Claude Academy.

**Fuente:** https://claude.com/blog/the-ai-native-sdlc-playbook

## Introducción

Durante el desarrollo de AIRLINCOLN utilizamos herramientas de inteligencia artificial para planear, diseñar, programar, revisar y mejorar nuestro dashboard de predicción de No-Show.

La investigación del ciclo de desarrollo asistido por IA nos permitió reflexionar sobre cómo utilizamos estas herramientas y qué podemos mejorar para que nuestro trabajo no dependa únicamente de generar código.

Una de las ideas principales que recuperamos del material es que un asistente puede participar en distintas etapas del desarrollo, pero sus resultados necesitan instrucciones claras, pruebas y validaciones. Por eso, analizamos nuestro proceso y lo relacionamos con las prácticas que aplicamos en el proyecto.

## 1. ¿En qué etapas del ciclo ya usamos el asistente y en cuáles no?

Para responder, revisamos las actividades realizadas durante el proyecto y los registros de interacción conservados en la carpeta `prompts/`.

| Etapa | ¿La utilizamos? | Evidencia en AIRLINCOLN |
|---|---|---|
| **Plan** | Sí | Utilizamos el asistente para definir el objetivo del dashboard, identificar a los tres usuarios y establecer las decisiones de negocio relacionadas con las ausencias en vuelos. |
| **Design** | Sí | Diseñamos e iteramos las pantallas de Laura, Armando y Anna, mejorando la organización de indicadores, gráficas, controles y colores. |
| **Build** | Sí | Utilizamos asistencia para desarrollar y modificar componentes de Streamlit, simuladores, validaciones, documentación y elementos visuales. |
| **Test** | Sí, con oportunidades de mejora | Realizamos pruebas funcionales, revisamos errores de ejecución y configuramos una comprobación automática de contraste de colores mediante GitHub Actions. |
| **Deploy** | Sí | Publicamos AIRLINCOLN en Streamlit Community Cloud y comprobamos el acceso a los dashboards desde la aplicación publicada. |
| **Maintain** | Parcialmente | Corregimos errores y actualizamos el proyecto mediante GitHub. Sin embargo, todavía no contamos con un proceso formal de seguimiento del uso y desempeño de la aplicación a largo plazo. |

### Análisis de nuestra experiencia

Al principio utilizamos la inteligencia artificial principalmente para generar ideas, organizar la información y construir el dashboard. La mayor parte del trabajo se concentraba en las etapas de diseño y programación.

Posteriormente comenzamos a dar mayor importancia a las pruebas. Un ejemplo fue la implementación de `scripts/verificar_contraste.py`, que calcula el contraste de combinaciones de colores definidas en `ui/theme.py`.

También configuramos el archivo `.github/workflows/contraste.yml`, permitiendo que GitHub Actions ejecute automáticamente la comprobación.

Durante esta implementación detectamos problemas como combinaciones de colores con contraste insuficiente y errores en la configuración del workflow. Después de corregirlos, obtuvimos una ejecución exitosa en GitHub Actions.

Además, realizamos pruebas con los tres perfiles del dashboard y verificamos que presentan funciones diferentes según las responsabilidades de cada usuario.

### Conclusión de la pregunta 1

Consideramos que nuestro uso de la inteligencia artificial evolucionó durante el proyecto.

Inicialmente nos enfocamos en diseñar y construir, pero después incorporamos pruebas, validaciones y publicación de la aplicación.

Esto nos permitió comprender que no basta con obtener código funcional. También es necesario comprobar que los resultados sean correctos, que la aplicación responda a las necesidades de los usuarios y que los cambios puedan verificarse.

Todavía podemos mejorar la etapa de mantenimiento, especialmente mediante seguimiento de errores, revisión periódica de los modelos y pruebas adicionales de seguridad y accesibilidad.

## 2. ¿Qué práctica concreta del curso podemos adoptar esta semana?

La práctica que decidimos adoptar es **proporcionar al asistente una forma de comprobar su trabajo y considerar las pruebas como parte de una tarea terminada**.

Antes, podíamos aceptar una modificación porque visualmente parecía correcta. Ahora buscamos respaldar las mejoras mediante resultados observables y, cuando corresponde, verificaciones automáticas.

### Aplicación en AIRLINCOLN

**1. Validación automática del contraste**

Creamos `scripts/verificar_contraste.py` para calcular las relaciones de contraste de las combinaciones de colores declaradas.

La verificación utiliza los criterios de accesibilidad WCAG 2.2 AA:

- Contraste mínimo de 4.5:1 para texto normal.
- Contraste mínimo de 3:1 para texto grande y elementos gráficos relevantes, cuando corresponde.

Al detectar un contraste insuficiente, el programa puede terminar con un código de error.

**2. Integración con GitHub Actions**

Configuramos `.github/workflows/contraste.yml` para ejecutar la comprobación al subir cambios o abrir un pull request.

Durante la implementación, una ejecución falló porque GitHub no reconocía los eventos configurados en el workflow. Después de corregir el archivo YAML, la siguiente ejecución terminó correctamente.

Esto demuestra la utilidad de una prueba automática: permite identificar problemas técnicos de manera reproducible, sin depender únicamente de una revisión visual.

**3. Pruebas funcionales**

También comprobamos diferentes funciones del dashboard.

En Laura, verificamos que el simulador modifica sus recomendaciones según los parámetros del escenario y que el calendario permite seleccionar fechas y vuelos.

En Armando, comprobamos la presencia de herramientas para priorizar contactos, comparar grupos de pasajeros y revisar casos individuales.

En Anna, revisamos la evaluación de modelos y la pantalla para ajustar el umbral de alertas.

Estas pruebas nos ayudaron a relacionar el funcionamiento técnico de la aplicación con las decisiones que necesita tomar cada usuario.

### Controles orientativos y deterministas

Otra idea importante de la investigación es distinguir entre las instrucciones que orientan al asistente y las verificaciones que comprueban condiciones específicas.

**Control orientativo:** consiste en explicar al asistente cómo queremos que trabaje. Por ejemplo, solicitar títulos claros, evitar depender exclusivamente del color y mostrar información relevante para cada perfil.

**Control determinista:** consiste en una comprobación que produce un resultado verificable. Por ejemplo, calcular automáticamente una relación de contraste y hacer fallar una prueba cuando no alcanza el mínimo establecido.

Ambos controles son útiles, pero cumplen funciones diferentes.

Las instrucciones ayudan a orientar el diseño y las decisiones técnicas. Las verificaciones automáticas permiten comprobar condiciones que pueden expresarse mediante reglas concretas.

### Reflexión de la pregunta 2

La principal mejora en nuestra forma de trabajar fue dejar de considerar una tarea terminada únicamente porque el asistente entregó una respuesta.

Ahora buscamos comprobar el resultado mediante pruebas y evidencias.

En AIRLINCOLN aplicamos esta práctica con la verificación de contraste en GitHub Actions y las pruebas funcionales de los dashboards.

Reconocemos que la verificación actual cubre las combinaciones configuradas en el script, por lo que una revisión completa de accesibilidad todavía requiere comprobar otros componentes de la interfaz.

## 3. ¿Qué esperábamos encontrar en el curso y no estaba?

Esperábamos encontrar más ejemplos sobre cómo aplicar asistentes de inteligencia artificial en proyectos de análisis de datos y dashboards, además de los ejemplos tradicionales de desarrollo de software.

En nuestro caso, AIRLINCOLN no solamente necesita funcionar correctamente. También debemos comprobar que los datos utilizados sean adecuados, que las predicciones se interpreten bien y que las recomendaciones tengan sentido para las decisiones de negocio.

Por ejemplo, al mostrar una recomendación de sobreventa, es importante distinguir entre los datos históricos, los resultados calculados y los escenarios simulados. Si esa diferencia no es clara, el usuario podría interpretar una estimación como si fuera un resultado real.

También nos habría servido profundizar en cómo validar el significado de los datos. Un valor vacío no siempre significa cero y una predicción con buen desempeño estadístico no necesariamente representa una decisión conveniente desde el punto de vista operativo.

Finalmente, consideramos que sería útil incluir más ejemplos sobre equipos pequeños de estudiantes que desarrollan aplicaciones sin contar con un equipo independiente de pruebas o revisores especializados.

A pesar de ello, el material nos ayudó a identificar prácticas que podemos adaptar a nuestro proyecto, especialmente la automatización de verificaciones y la revisión humana de los resultados generados con IA.

## 4. Los tres cambios en nuestra forma de trabajar

A partir de la investigación identificamos tres mejoras que podemos aplicar al desarrollo de AIRLINCOLN.

| # | Qué cambiamos | Dónde lo aplicamos | Por qué |
|---|---|---|---|
| **1** | Incorporar verificaciones automáticas para las condiciones que pueden comprobarse mediante reglas. | **Dentro del pipeline:** `.github/workflows/contraste.yml` y `scripts/verificar_contraste.py`. | Para detectar problemas de contraste automáticamente y evitar depender de una revisión manual en cada cambio. |
| **2** | Documentar las instrucciones y convenciones que el asistente debe respetar. | **Fuera del pipeline:** carpeta `prompts/`, documentación del proyecto y criterios de diseño. | Porque las decisiones sobre claridad, interpretación y presentación requieren contexto y criterio humano. |
| **3** | Revisar los cambios importantes antes de integrarlos y documentar su evidencia. | **Fuera del pipeline:** revisión humana de código, capturas, resultados y pull requests cuando se utilicen. | Porque una prueba automática puede comprobar reglas técnicas, pero no garantiza que todas las decisiones de negocio sean correctas. |

### Cambio 1. Verificar automáticamente

El primer cambio consiste en utilizar pruebas automáticas para condiciones que pueden expresarse de manera objetiva.

En AIRLINCOLN ya aplicamos esta mejora mediante la validación de contraste ejecutada desde GitHub Actions.

Como siguiente mejora, proponemos ampliar la cobertura para incluir otros componentes visuales y las combinaciones de colores utilizadas directamente en las gráficas.

También consideramos importante mantener las pruebas de calidad y estructura de datos, verificando sus resultados antes de afirmar que todos los casos están cubiertos.

### Cambio 2. Documentar las instrucciones

El segundo cambio consiste en conservar las instrucciones utilizadas durante el proyecto.

Esto permite recuperar las decisiones de diseño, comprender por qué se solicitaron determinadas modificaciones y facilitar que otros integrantes puedan continuar el trabajo.

Entre los criterios que consideramos importantes están:

- Distinguir entre datos originales, cálculos y simulaciones.
- Mostrar información relevante para cada perfil.
- Evitar utilizar solamente colores para comunicar resultados.
- Explicar las preguntas de negocio de las gráficas.
- Revisar el significado de los valores faltantes.
- No utilizar características personales sensibles como justificación automática de intervenciones.

Estos criterios requieren interpretación y no siempre pueden convertirse en una prueba automática sencilla.

### Cambio 3. Incorporar revisión humana

El tercer cambio consiste en comprobar que una modificación realmente mejora el proyecto antes de considerarla terminada.

Por ejemplo, durante las pruebas del simulador observamos que diferentes escenarios produjeron recomendaciones distintas de sobreventa.

En uno de los escenarios se recomendaron 30 boletos adicionales, mientras que en otro la recomendación fue de 27.

También comprobamos que el calendario cambia la información presentada según la fecha y el vuelo seleccionado.

Estas verificaciones permiten confirmar que los controles generan resultados distintos, aunque no sustituyen una validación independiente de todos los cálculos.

Para cambios futuros en el contrato de datos, proponemos que un integrante revise el significado de las variables, los valores faltantes y las transformaciones antes de aprobarlos.

## 5. Evidencias del proyecto

Las siguientes evidencias permiten relacionar la investigación con el trabajo realizado.

| Evidencia | Ubicación | Qué demuestra |
|---|---|---|
| Registro de interacciones con IA | `prompts/B2.md` y `prompts/B3.md` | Uso del asistente durante diferentes etapas del desarrollo. |
| Código de verificación de contraste | `scripts/verificar_contraste.py` | Comprobación programática de combinaciones de colores. |
| Integración continua | `.github/workflows/contraste.yml` | Ejecución automática de la prueba de contraste. |
| Paleta de colores | `ui/theme.py` | Definición de colores utilizados en componentes de la interfaz. |
| Control de estado vacío | `app.py` | Uso de `st.stop()` para detener procesos cuando corresponde. |
| Documentación del entregable | `docs/entregable-3.md` | Preguntas de negocio, accesibilidad, controles, jerarquía y roles. |
| Aplicación publicada | https://airlincoln-entregable3.streamlit.app/ | Despliegue del dashboard para su utilización desde el navegador. |

**Nota:** la ejecución exitosa de GitHub Actions demuestra el funcionamiento del verificador configurado, pero no constituye por sí sola una auditoría completa de accesibilidad WCAG de toda la aplicación.

## 6. Conclusión general

Esta investigación nos permitió comprender que utilizar inteligencia artificial en el desarrollo de software va más allá de pedirle que escriba código.

Durante el proyecto AIRLINCOLN utilizamos el asistente para planear, diseñar, construir y mejorar el dashboard. Con el avance del trabajo también incorporamos pruebas funcionales, documentación y automatización mediante GitHub Actions.

La principal enseñanza fue que una solución no debe considerarse terminada solamente porque funciona o porque visualmente parece correcta. También necesitamos verificar sus resultados, comprender sus limitaciones y relacionarla con las necesidades reales de los usuarios.

Consideramos que la combinación de inteligencia artificial, pruebas automáticas y revisión humana nos permitió mejorar nuestro proceso de desarrollo.

Como siguientes pasos, buscamos ampliar la validación de accesibilidad, fortalecer las pruebas de permisos y establecer una revisión periódica de los resultados del modelo.

**En conclusión, la inteligencia artificial nos ayudó a desarrollar AIRLINCOLN, pero las pruebas y la revisión humana son las que permiten evaluar si el trabajo realmente cumple con lo que necesitamos.**

## Referencia

Anthropic. (s. f.). *The AI-native SDLC playbook*. Claude. https://claude.com/blog/the-ai-native-sdlc-playbook
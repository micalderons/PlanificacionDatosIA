# Sistema Predictivo para la Optimización de la Cadena de Frío y Prevención de Caducidad de Medicamentos 



## Descripción del Proyecto

Este proyecto forma parte de la asignatura **Gestión de Datos para IA**. Nace de la necesidad de mitigar las pérdidas de medicamentos en la industria farmacéutica debido a la caducidad o ruptura de la cadena de frío, lo cual representa un riesgo crítico para la salud y un alto costo económico. 



El objetivo principal es desarrollar una solución técnica basada en una arquitectura de datos moderna (Lakehouse) que gestione datos históricos de almacenamiento y logística para predecir el riesgo de pérdida logística. Esto permitirá optimizar la asignación de rutas según la vida útil restante de los lotes y las condiciones de temperatura.



## Objetivos y Criterios de Éxito

* **Técnico:** Implementar un pipeline de datos funcional (ingesta, limpieza, transformación) hasta el entrenamiento del modelo, sin errores.

* **Calidad:** Obtener métricas de desempeño aceptables en el modelo de Machine Learning (Accuracy/Recall).

* **Gestión:** Completar el desarrollo en un plazo de **5 semanas**, cumpliendo con el 100% de los entregables planificados.



## Alcance del Proyecto

**Dentro del Alcance (In Scope):**

* Obtención, limpieza y transformación de un dataset con datos logísticos farmacéuticos (temperaturas, tiempos de tránsito, caducidad, estado del lote).

* Diseño de arquitectura de datos (Capa Bronze / Silver / Gold).

* Implementación de una base de datos relacional (PostgreSQL) para almacenar el inventario procesado.

* Desarrollo de un pipeline automatizado mediante scripts en Python.

* Entrenamiento y evaluación de un modelo predictivo de IA (Clasificación/Regresión).

* Documentación técnica y planificación bajo el estándar PMBOK.



**Fuera del Alcance (Out of Scope):**

* Desarrollo de una aplicación web completa o aplicación móvil.

* Integración con sensores IoT físicos en tiempo real.

* Automatización de procesos de compra de medicamentos.



## Equipo de Trabajo (RACI)

* **Director del Proyecto (PM):** Miguel Calderón Santana *(Responsable de planificación, control de cronograma y entregables)*

* **Ingeniero de Datos:** Roberto Armijo *(Responsable del pipeline, arquitectura Lakehouse y Base de Datos)*

* **Ingeniero ML:** Ricardo Saavedra *(Responsable del diseño, entrenamiento y métricas del modelo de IA)*

* **Sponsor:** Franco Jorquera Pezoa



## Tecnologías y Recursos Físicos

* **Lenguaje:** Python (Scripts de ingesta, limpieza y modelo)

* **Base de Datos:** PostgreSQL (Alojada en Supabase)

* **Infraestructura Cloud / Despliegue:** Render

* **Control de Versiones y CI/CD:** Git / GitHub / GitHub Actions

* **Entorno de Desarrollo:** VS Code, Docker Desktop

* **Gestión y Planificación:** [Tablero Jira del Proyecto](https://duocuc-team-b580r3v2.atlassian.net/jira/software/projects/KAN/boards/1?atlOrigin=eyJpIjoiNmIyYzQ0ODIwNTY0NDFhZGJjYjI3MjA0ZGRlNWIzZDEiLCJwIjoiaiJ9)



##  Fases del Proyecto (5 Semanas)

1. **Fase 1: Planificación e Inicio** - Acta de constitución, WBS y configuración de entornos.

2. **Fase 2: Diseño Técnico** - Definición de arquitectura y selección de modelo/métricas.

3. **Fase 3: Ingeniería de Datos** - Obtención de dataset, scripts de Python e inserción en PostgreSQL.

4. **Fase 4: Desarrollo de IA** - Entrenamiento del modelo predictivo y evaluación de resultados.

5. **Fase 5: Cierre y Documentación** - Consolidación del repositorio y entrega final.



##  Estructura del Repositorio

* `docs/` o raíz:

 * `ACTA DE CONSTITUCIÓN DEL PROYECTO.pdf`

 * `PlanificacionIA.pdf` y `Documentación PlanificaciónIA.pdf` (Diseño técnico y modelo de datos).

 * `CartaGanttPlanificacionIA.pdf` (Cronograma detallado).

 * `Categorización de recursos.pdf` (Team Charter y gestión de infraestructura).

* `scripts/`: Códigos en Python para la ingesta, limpieza y transformación de datos.

* `modelos/`: Scripts de entrenamiento y evaluación de la Inteligencia Artificial.

* `DiagramaPlanificacion.png`: Representación visual de la arquitectura/planificación del proyecto.


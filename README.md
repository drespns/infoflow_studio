# 🚀 Infoflow Studio

> Motor Visual Open-Source de Transformación y Análisis de Datos  
> Aplicación de escritorio. Modular. Reproducible. Extensible.

![Licencia](https://img.shields.io/badge/licencia-MIT-blue)
![Estado](https://img.shields.io/badge/estado-en%20desarrollo-orange)
![Backend](https://img.shields.io/badge/backend-Python-blue)
![Frontend](https://img.shields.io/badge/frontend-React-61DAFB)
![Docs](https://img.shields.io/badge/documentación-Starlight-purple)

---

## ✨ Descripción

**Infoflow Studio** es una aplicación de escritorio open-source diseñada para la transformación visual, exploración y análisis de datos.

Inspirada en herramientas profesionales de preparación de datos y ETL visual, el objetivo de este proyecto es construir una alternativa moderna, transparente y extensible que combine:

- 🧠 Construcción visual de flujos de trabajo
- 🔄 Pipelines de transformación reproducibles
- 📊 Visualización dinámica e interactiva
- 🧩 Arquitectura modular
- 💻 Ejecución local (desktop-first)

Todo ello con una filosofía abierta, extensible y pensada tanto para analistas como para desarrolladores.

---

## 🎯 Visión del Proyecto

Crear una herramienta potente, extensible y completamente transparente que permita:

- Transformar datos de forma visual
- Serializar pipelines en formato estructurado (JSON)
- Exportar código equivalente (Python / SQL)
- Mantener reproducibilidad total
- Fomentar una comunidad open-source

Infoflow Studio no pretende ser un clon, sino una evolución moderna basada en buenas prácticas de ingeniería y diseño de sistemas.

---

## 🏗 Arquitectura (Planificada)

### 🧠 Backend
- Python
- FastAPI
- Motor de transformación modular
- Pandas (modo estándar)
- Polars (modo rendimiento)
- Serialización de pipelines

### 🎨 Frontend
- React
- Editor visual basado en nodos
- Componentes modulares
- Sistema de visualización interactiva

### 🖥 Aplicación de Escritorio
- Evaluación entre:
  - Tauri
  - Electron
- Enfoque local-first

### 📚 Documentación
- Astro.build
- Starlight
- Documentación versionada
- Landing profesional
- Guía de instalación y desarrollo

---

## 🧩 Roadmap de Desarrollo

### Fase 1 — Motor de Transformación (MVP)
- [ ] Carga de archivos CSV / Excel
- [ ] Inferencia automática de esquema
- [ ] Renombrado de columnas
- [ ] Filtros de filas
- [ ] GroupBy y agregaciones
- [ ] Joins entre datasets
- [ ] Columnas calculadas
- [ ] Ordenación
- [ ] Serialización de pipeline en JSON

---

### Fase 2 — Constructor Visual de Flujos
- [ ] Editor visual basado en nodos
- [ ] Drag & Drop de transformaciones
- [ ] Conexión entre nodos
- [ ] Vista previa de ejecución
- [ ] Sistema de trazabilidad de errores por nodo

---

### Fase 3 — Motor de Visualización
- [ ] Gráficos de barras
- [ ] Gráficos de líneas
- [ ] Scatter plots
- [ ] Heatmaps
- [ ] Sugerencias automáticas de visualización
- [ ] Filtros interactivos

---

### Fase 4 — Funcionalidades Avanzadas
- [ ] Exportación del pipeline como script Python
- [ ] Exportación del pipeline como SQL
- [ ] Versionado de pipelines
- [ ] Soporte multi-dataset
- [ ] Benchmark Pandas vs Polars
- [ ] Sistema de plugins

---

## 💡 Principios de Diseño

- Arquitectura modular
- Reproducibilidad por defecto
- Transparencia en las transformaciones
- Rendimiento local
- Extensibilidad futura
- Diseño moderno y profesional
- Open-source desde el inicio

---

## 📂 Estructura del Proyecto (Planificada)

infoflow-studio/
│
├── backend/
│   ├── api/
│   ├── app/
│   │   ├── core/
│   │   │   ├── pipeline.py
│   │   │   ├── node.py
│   │   │   └── dataset.py
│   │   │
│   │   ├── transformations/
│   │   │   ├── base.py
│   │   │   ├── filter.py
│   │   │   ├── rename.py
│   │   │   └── groupby.py
│   │   │
│   │   └── api/
│   │
│   └── main.py
│
├── frontend/
│ ├── components/
│ ├── workflow/ 
│ ├── charts/
│ └── services/
│
├── desktop/
│
├── docs/
│
└── README.md


> Nota: Las carpetas y el código estarán en inglés para mantener estándares internacionales.

---

## 🧪 Estado Actual

El proyecto se encuentra en fase inicial de planificación y diseño de arquitectura.

Próximos pasos:

1. Definición del esquema de pipeline
2. Implementación del motor de ejecución
3. Desarrollo de interfaz mínima en React
4. Primer prototipo empaquetado como aplicación de escritorio

---

## 🌍 Open Source

Infoflow Studio será completamente open-source bajo licencia MIT.

Se aceptarán contribuciones futuras una vez que el núcleo del proyecto esté estabilizado.

---

## 🧠 Objetivos a Largo Plazo

- Sistema completo de plugins
- Modo colaborativo (posible futura capa SaaS)
- Sincronización opcional en la nube
- Asistencia inteligente para limpieza de datos
- Ecosistema de extensiones creadas por la comunidad

---

## 📜 Licencia

MIT License

---

## 🚀 Filosofía

Infoflow Studio no es solo una herramienta.  
Es un laboratorio abierto de ingeniería de datos visual.

El objetivo no es únicamente construir una aplicación, sino aprender, experimentar y diseñar una arquitectura sólida que pueda crecer con el tiempo.

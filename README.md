# Evolve – Proyecto 1: Análisis Exploratorio de Datos (EDA)

## 🧪 Descripción

Evolve – Proyecto 1 es un ejercicio práctico de **Análisis Exploratorio de Datos (EDA)** sobre un dataset real. El objetivo es comprender a fondo la estructura, calidad y características del conjunto de datos, así como generar visualizaciones y estadísticas descriptivas.  

Este repositorio presenta **tres versiones** del mismo análisis, con distintos niveles de modularización y estilos de trabajo, para mostrar el progreso ocurrido conforme la realización del proyecto.

---

## 📁 Estructura del repositorio

- **[`/data`](./data)**  
  Contiene el dataset original utilizado para el análisis.

- **[`/notebooks_(v1)`](./notebooks_(v1))**  
  Versión 1 — desarrollo íntegro en Jupyter Notebook.  
  Toda la lógica — carga de datos, limpieza, análisis y visualización — se encuentra en celdas de notebooks.

- **[`/notebooks+python_(v2)`](./notebooks+python_(v2))**  
  Versión 2 — enfoque híbrido: se mantienen los notebooks como guía del flujo, pero la lógica principal está exportada en ficheros Python.  
  Permite mejor organización del código y facilita su reutilización.

- **[`/python_(v3)`](./python_(v3))**  
  Versión 3 — todo implementado en ficheros Python.
  No hay notebooks: el flujo completo está en ficheros de Python, ideal para producción o automatización.

---

## 🧠 Explicación del proyecto



---

## 🚀 Cómo usar el proyecto

Para clonar y ejecutar el proyecto localmente:

```bash
git clone https://github.com/DCodePz/Evolve-Proyecto-1-EDA.git
cd Evolve-Proyecto-1-EDA

# versión python
py '.\python_(v3)\main.py'

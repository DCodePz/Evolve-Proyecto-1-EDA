# 📊 **Evolve – Proyecto 1: Análisis Exploratorio de Datos (EDA)**
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completado-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## 🧪 **Descripción**

Este proyecto consiste en realizar un **Análisis Exploratorio de Datos (EDA)** sobre un dataset real de películas.  
El objetivo principal es comprender la estructura, calidad y características del conjunto de datos, para posteriormente generar visualizaciones y extraer conclusiones relevantes.

El repositorio presenta **tres versiones** del mismo análisis, mostrando la evolución del proyecto desde un enfoque totalmente basado en notebooks hasta una versión completamente modular en Python.

---

## 📁 **Estructura del repositorio**

**[`/data`](./data)**  
Contiene el dataset original utilizado para el análisis.

**[`/notebooks_(v1)`](./notebooks_(v1))**  
Versión 1 — análisis íntegro en Jupyter Notebook.  
Toda la lógica (carga, limpieza, análisis y visualización) está en los notebooks.

**[`/notebooks+python_(v2)`](./notebooks+python_(v2))**  
Versión 2 — enfoque híbrido.  
El flujo sigue en los notebooks, pero la lógica principal está organizada en módulos Python externos.

**[`/python_(v3)`](./python_(v3))**  
Versión 3 — implementación completa en Python.  
No se utilizan notebooks: el flujo y la lógica del proyecto están totalmente modularizados.

---

## 🧠 **Explicación del proyecto**

El proceso completo del EDA incluye:

### **1. Exploración inicial del dataset**
- Análisis de estructura y tipos de datos  
- Detección de valores nulos  
- Identificación de duplicados  
- Revisión de la consistencia entre columnas  

### **2. Limpieza del dataset**
- Normalización de nombres de columnas  
- Conversión y corrección de tipos de datos  
- Eliminación o imputación de valores nulos  
- Gestión de duplicados  
- Preparación del dataset para análisis estadístico y visualización  

### **3. Visualizaciones realizadas**
Se generan **4 gráficos principales** para comprender el comportamiento del dataset:

#### 📌 **1. Histograma — Distribución de puntuaciones IMDb**
Muestra cuántas películas existen para cada rating.

#### 📌 **2. Barras — Protagonistas que más gustan**
Se puede observan que actores protagonistas tienen más likes, por lo tanto son más famosos.

#### 📌 **3. Barras — Frecuencia de películas por género**
Permite ver qué géneros producen más y menos películas.

#### 📌 **4. Líneas — Evolución del rating a lo largo de los años**
Para los 5 géneros con más películas, se analiza cómo evolucionan sus puntuaciones en IMDb.

#### 📌 **5. Barras comparadas — Top 5 directores por beneficios**
Se comparan:
- Beneficio **acumulado**
- Beneficio **medio**

---

## 📊 **Resultados destacados**

- **Distribución de puntuaciones en IMDb:** La mayoría de películas obtienen puntuaciones entre **6 y 7**, mostrando una distribución cercana a la normal. Esto indica que la mayor parte de las producciones se concentran en un rango de calidad media.

- **Actores con más likes:** Los actores con mayor cantidad de likes destacan por su popularidad en redes sociales, lo que los convierte en un fuerte empuje para las películas en las que participan. Sus fans pueden influir positivamente en la visibilidad y el rendimiento de una película. Los tres actores protagonistas con más likes son Johnny Depp, Robin Williams y Robert De Niro, nombres ampliamente reconocidos por todo el mundo debido a su trayectoria.

- **Géneros con mayor número de películas:** *Drama*, *Comedia* y *Thriller* son los más representados en el dataset, destacando por su alta frecuencia de producción.

- **Géneros con menor número de películas:** *News*, *Reality-TV* y *Game-Show* aparecen como los menos frecuentes, con una presencia muy reducida.

- **Evolución del rating por año:** A lo largo de las décadas, la variación del rating ha sido notable. Sin embargo, en los años más recientes los géneros **Thriller** y **Acción** han pasado de estar entre los peor valorados a situarse como los mejor puntuados. Esto podría indicar una mejora en la calidad de las producciones de estos géneros o un aumento del interés del público hacia ellos.

- **Comparativa de directores por beneficios:**  
  - El director con **mayor beneficio acumulado** no coincide con el de **mayor beneficio medio**, lo cual revela perfiles de rentabilidad distintos.  
  - *Steven Spielberg*, por ejemplo, destaca en beneficio total gracias a varias películas muy exitosas, pero no aparece en el top de beneficio medio porque también cuenta con títulos menos rentables que reducen su promedio.  
  - En cambio, *George Lucas* se mantiene consistentemente en el **top 2 de ambos rankings**, reflejando una filmografía con altos beneficios y sin grandes pérdidas que afecten negativamente a su media.


---

## 🚀 **Cómo ejecutar el proyecto**

Clonar el repositorio:

```bash
git clone https://github.com/DCodePz/Evolve-Proyecto-1-EDA.git
cd Evolve-Proyecto-1-EDA

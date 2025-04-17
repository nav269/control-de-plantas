# 🌽 Modelado Predictivo del Crecimiento del Maíz en Achocalla, La Paz

Este proyecto tiene como objetivo estimar el crecimiento diario del maíz en la región de Achocalla, ubicada en el departamento de La Paz, Bolivia. Se utilizan técnicas de interpolación y regresión para modelar el crecimiento de la planta con base en datos reales aproximados y considerando factores geográficos y climáticos.

---

## 📍 Contexto

Achocalla se encuentra a una altitud aproximada de 3.600 msnm, lo cual influye significativamente en el crecimiento del maíz debido a:

- Altas variaciones de temperatura diurna y nocturna.
- Temporada de lluvias estacional.
- Radiación solar intensa.

Además, el crecimiento también está influenciado por la calidad de la semilla utilizada. En este estudio se asume el uso de semillas de **calidad intermedia a alta**, adaptadas a climas fríos de altura.

---

## 📊 Datos utilizados

Los siguientes datos representan alturas (en cm) del maíz medidas a distintos días después de la siembra:

| Días (x) | Altura (cm) (y) |
|----------|------------------|
| 15       | 20               |
| 30       | 50               |
| 45       | 80               |
| 75       | 140              |
| 90       | 160              |
| 120      | 175              |

Los valores que se desean predecir son:

- ¿Cuál será la altura del maíz a los **60 días**?
- ¿Y a los **105 días**?

---

## 🧠 Métodos aplicados

Se aplicaron los siguientes métodos para estimar el crecimiento del maíz:

### 1. Interpolación de Newton

**Análisis de los resultados:**

- **Interpolación de Newton**:
  - Este método produjo estimaciones consistentes y precisas. Presentó muy buenos resultados ya que toma en cuenta la progresión no lineal entre puntos.
  - Para 60 días → **111.48 cm**
  - Para 105 días → **169.52 cm**

---

### 2. Interpolación de Lagrange

**Análisis de los resultados:**

- **Interpolación de Lagrange**:
  - Al igual que Newton, logra una buena precisión ya que considera todos los puntos. Al ser un polinomio de alto grado puede ser sensible a oscilaciones si hay más datos.
  - Para 60 días → **111.48 cm**
  - Para 105 días → **169.52 cm**

---

### 3. Interpolación por Splines cúbicos

**Análisis de los resultados:**

- **Interpolación Spline**:
  - Proporciona una curva más suave que conecta los puntos. Es más realista para el crecimiento natural del maíz.
  - Para 60 días → **110.75 cm**
  - Para 105 días → **169.04 cm**

---

### 4. Regresión Lineal

**Análisis de los resultados:**

- **Regresión Lineal**:
  - Se asume un crecimiento constante a lo largo del tiempo, lo cual no refleja completamente la naturaleza del crecimiento del maíz, que tiende a desacelerarse en etapas tardías.
  - Para 60 días → **100.26 cm**
  - Para 105 días → **170.53 cm**

---

## 📈 Comparación de Resultados

| Método               | 60 días (cm) | 105 días (cm) |
|----------------------|--------------|---------------|
| Newton               | 111.48       | 169.52        |
| Lagrange             | 111.48       | 169.52        |
| Splines cúbicos      | 110.75       | 169.04        |
| Regresión lineal     | 100.26       | 170.53        |

---

## Referencias

1. **Instituto Nacional de Innovación Agropecuaria y Forestal (INIAF)**. (2018). *Guía para la Producción de Maíz en Bolivia*. Recuperado de [www.iniaf.gob.bo](http://www.iniaf.gob.bo)  
2. **SENAMHI**. (2021). *Estudio Agroclimático de la Región Andina: Caso Achocalla*. Recuperado de [www.senamhi.gob.bo](https://www.senamhi.gob.bo)   
3. **UMSA (Universidad Mayor de San Andrés)**. (2019). *Estudio de Variedades de Maíz en Zonas de Altura: Caso La Paz*. *Revista de Investigación Agropecuaria*, 22(2), 98-112.  
4. **Chavez, E.** (2021). *Análisis del Ciclo de Crecimiento del Maíz en el Altiplano Boliviano*. *Revista de Ciencias Agropecuarias*, 8(1), 50-65.

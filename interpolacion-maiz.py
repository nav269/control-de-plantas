import numpy as np
from scipy.interpolate import CubicSpline
from scipy.interpolate import lagrange
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- FUNCIÓN PARA INTERPOLACIÓN DE NEWTON ---
def interpolacion_newton(x, y, x_eval):
    n = len(x)
    coef = np.copy(y)
    
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1]) / (x[j:n] - x[j-1])

    def polinomio_newton(xi):
        resultado = coef[-1]
        for k in range(n - 2, -1, -1):
            resultado = resultado * (xi - x[k]) + coef[k]
        return resultado

    return np.array([polinomio_newton(xi) for xi in x_eval])

# --- DATOS ---
dias = np.array([15, 30, 45, 60, 75, 90, 105, 120])
alturas = np.array([20, 50, 80, np.nan, 140, 160, np.nan, 175])

# Filtrar datos conocidos y faltantes
dias_conocidos = dias[~np.isnan(alturas)]
alturas_conocidas = alturas[~np.isnan(alturas)]
dias_faltantes = dias[np.isnan(alturas)]

# 1. Interpolación por Newton
alturas_faltantes_newton = interpolacion_newton(dias_conocidos, alturas_conocidas, dias_faltantes)

# 2. Interpolación por Lagrange
pol_lagrange = lagrange(dias_conocidos, alturas_conocidas)
alturas_faltantes_lagrange = pol_lagrange(dias_faltantes)

# 3. Interpolación Spline Cúbico
interp_spline = CubicSpline(dias_conocidos, alturas_conocidas)
alturas_faltantes_spline = interp_spline(dias_faltantes)

# 4. Regresión lineal
modelo_lineal = LinearRegression()
modelo_lineal.fit(dias_conocidos.reshape(-1, 1), alturas_conocidas)
alturas_faltantes_regresion = modelo_lineal.predict(dias_faltantes.reshape(-1, 1))

# --- RESULTADOS ---
print("Resultados de Interpolación:")
print("----------------------------")
print(f"Alturas faltantes (Newton): {alturas_faltantes_newton}")
print(f"Alturas faltantes (Lagrange): {alturas_faltantes_lagrange}")
print(f"Alturas faltantes (Spline cúbico): {alturas_faltantes_spline}")
print(f"Alturas faltantes (Regresión lineal): {alturas_faltantes_regresion}")

# --- GRÁFICO ---
plt.plot(dias_conocidos, alturas_conocidas, 'o', label="Datos conocidos", color="black")
plt.plot(dias_faltantes, alturas_faltantes_newton, 's', label="Newton", markersize=8)
plt.plot(dias_faltantes, alturas_faltantes_lagrange, 'd', label="Lagrange", markersize=8)
plt.plot(dias_faltantes, alturas_faltantes_spline, 'x', label="Spline cúbico", markersize=8)
plt.plot(dias_faltantes, alturas_faltantes_regresion, '+', label="Regresión lineal", markersize=10)

# Curvas para comparar visualmente (opcional)
x_full = np.linspace(15, 120, 200)
plt.plot(x_full, interpolacion_newton(dias_conocidos, alturas_conocidas, x_full), '--', label="Curva Newton", alpha=0.5)
plt.plot(x_full, lagrange(dias_conocidos, alturas_conocidas)(x_full), '--', label="Curva Lagrange", alpha=0.5)
plt.plot(x_full, interp_spline(x_full), '--', label="Curva Spline", alpha=0.5)
plt.plot(x_full, modelo_lineal.predict(x_full.reshape(-1, 1)), '--', label="Curva Lineal", alpha=0.5)

plt.xlabel("Días")
plt.ylabel("Altura (cm)")
plt.title("Interpolación del crecimiento del maíz")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

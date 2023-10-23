import numpy as np
import matplotlib.pyplot as plt

def calcular_spline_cubico(n, ti, yi):
    # Calcular las diferencias entre puntos adyacentes
    h = [ti[i + 1] - ti[i] for i in range(n - 1)]
    
    # Calcular los coeficientes 'b' necesarios para el cálculo
    b = [(6 * (yi[i + 1] - yi[i])) / h[i] for i in range(n - 1)]

    u = [0] * n
    v = [0] * n
    
    # Calcular las listas 'u' y 'v' necesarias para el algoritmo
    u[1] = 2 * (h[0] + h[1])
    v[1] = b[1] - b[0]

    for i in range(2, n - 1):
        u[i] = 2 * (h[i - 1] + h[i]) - (h[i - 1]**2) / u[i - 1]
        v[i] = b[i] - b[i - 1] - h[i - 1] * v[i - 1] / u[i - 1]

    zn = 0
    zi = [0] * n
    zi[n - 1] = zn

    # Calcular los valores 'zi' para el spline
    for i in range(n - 2, 0, -1):
        zi[i] = (v[i] - h[i] * zi[i + 1]) / u[i]

    z0 = 0
    zi[0] = z0

    x_values_segments = []
    y_values_segments = []

    polinomios_spline = []
    for i in range(n - 1):
        A = (zi[i + 1] - zi[i]) / (6 * h[i])
        B = zi[i] / 2
        C = (yi[i + 1] - yi[i]) / h[i] - (zi[i + 1] + 2 * zi[i]) * h[i] / 6

        # Crear el polinomio del spline cúbico
        polinomio = f"{A:.2f}(x - {ti[i]})^3 + {B:.2f}(x - {ti[i]})^2 + {C:.2f}(x - {ti[i]}) + {yi[i]}"
        polinomios_spline.append(polinomio)
        
        # Dividir el segmento en 100 puntos y calcular los valores 'y' correspondientes
        x_segment = np.linspace(ti[i], ti[i + 1], 100)
        y_segment = [A * (x - ti[i]) ** 3 + B * (x - ti[i]) ** 2 + C * (x - ti[i]) + yi[i] for x in x_segment]

        x_values_segments.extend(x_segment)
        y_values_segments.extend(y_segment)

    # Graficar los puntos de datos
    plt.scatter(ti, yi, color='red', label='Puntos de Datos')

    # Graficar la interpolación del spline
    plt.plot(x_values_segments, y_values_segments, label='Interpolación Spline')

    # Agregar etiquetas y leyenda
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # Mostrar la gráfica
    plt.show()

    return polinomios_spline

# Ejemplo de uso:
n = 3
ti = [1, 2, 3]
yi = [2, 3, 5]

polinomios_spline = calcular_spline_cubico(n, ti, yi)

# Imprimir la interpolación
for i, polinomio in enumerate(polinomios_spline):
    print(f"Spline {i + 1}: y = {polinomio}")

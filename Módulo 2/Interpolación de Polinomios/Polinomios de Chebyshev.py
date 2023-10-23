import numpy as np
import matplotlib.pyplot as plt

def interpolacion_chebyshev(funcion_objetivo, grado):
    # Generar nodos de Chebyshev
    valores_k = np.arange(1, grado + 2)
    nodos_chebyshev = np.cos((2 * valores_k - 1) * np.pi / (2 * (grado + 1)))

    # Evaluar la función objetivo en los nodos de Chebyshev
    valores_de_funcion = funcion_objetivo(nodos_chebyshev)

    # Realizar el ajuste polinómico utilizando polyfit de numpy
    coeficientes_del_polinomio = np.polyfit(nodos_chebyshev, valores_de_funcion, grado)

    # Definir el rango para la gráfica
    valores_x = np.linspace(-1, 1, 200)
    valores_polinomio_ajustado = np.polyval(coeficientes_del_polinomio, valores_x)

    # Graficar el polinomio ajustado y los nodos de Chebyshev
    plt.plot(valores_x, valores_polinomio_ajustado, label='Polinomio de Chebyshev')
    plt.plot(nodos_chebyshev, valores_de_funcion, 'ro', label='Puntos')
    plt.legend()
    plt.xlim(-1, 1)
    plt.legend(loc='best')
    plt.show()

# IMPORTANTE: Este programa interpola funciones en el intervalo [-1, 1]

# Define tu función aquí
def f(x):
    return np.cos(x)

# Grado del polinomio de Chebyshev
grado_de_interpolacion = 8

# Realizar la interpolación de Chebyshev
interpolacion_chebyshev(f, grado_de_interpolacion)
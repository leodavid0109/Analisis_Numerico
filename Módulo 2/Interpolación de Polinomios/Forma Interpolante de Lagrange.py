import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def interpolacionLagrange(x, x_i, y_i):
    n = len(x_i)
    # Guarda el polinomio resultante de cada iteración
    pol = 0
    for i in range(n):
        # Inicializa cada factor multiplicativo
        numerador = 1
        denominador = 1
        for j in range(n):
            # Condición que evita tomar la igualdad (genera 0)
            if i != j:
                numerador = numerador * (x-x_i[j])
                denominador = denominador * (x_i[i] - x_i[j])
            termino_nuevo = (numerador / denominador) * y_i[i]
        pol = pol + termino_nuevo
    resultante = sp.expand(pol)
    return pol, resultante


if __name__ == "__main__":
    x = sp.Symbol("x")

    # Caso de prueba 1
    x_i = [1, 3]
    y_i = [2, 6]

    pol, resultante = interpolacionLagrange(x, x_i, y_i)
    print("Polinomio con términos de Lagrange: ")
    print(pol)
    print("Polinomio simplificado: ")
    print(resultante)
    print()

    # Graficación de las Pruebas

    # Vectores para Gráficas
    polinomio = sp.lambdify(x, pol)
    a = np.min(x_i)
    b = np.max(x_i)
    p = np.linspace(a, b, 51)
    pf = polinomio(p)

    plt.plot(x_i, y_i, "o")
    plt.plot(p, pf)
    plt.show()

    #Caso de prueba 2
    x_i = [1, 2, 3]
    y_i = [2, 3, 6]
    pol, resultante = interpolacionLagrange(x, x_i, y_i)
    print("Polinomio con términos de Lagrange: ")
    print(pol)
    print("Polinomio simplificado: ")
    print(resultante)
    print()

    # Graficación de las Pruebas

    # Vectores para Gráficas
    polinomio = sp.lambdify(x, pol)
    a = np.min(x_i)
    b = np.max(x_i)
    p = np.linspace(a, b, 51)
    pf = polinomio(p)

    plt.plot(x_i, y_i, "o")
    plt.plot(p, pf)
    plt.show()

    # Caso de prueba 3
    x_i = [0, 0.2, 0.3, 0.4]
    y_i = [1, 1.6, 1.7, 2.0]
    pol, resultante = interpolacionLagrange(x, x_i, y_i)
    print("Polinomio con términos de Lagrange: ")
    print(pol)
    print("Polinomio simplificado: ")
    print(resultante)

    # Graficación de las Pruebas

    # Vectores para Gráficas
    polinomio = sp.lambdify(x, pol)
    a = np.min(x_i)
    b = np.max(x_i)
    p = np.linspace(a, b, 51)
    pf = polinomio(p)

    plt.plot(x_i, y_i, "o")
    plt.plot(p, pf)
    plt.show()

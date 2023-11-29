# # Método de coeficientes indeterminados
# from sympy import *
# from sympy.abc import x
#
# def coeficientes_indeterminados(n, a, b):
#     """
#     Método de coeficientes indeterminados para resolver sistemas de ecuaciones
#     lineales.
#     Parámetros:
#         n: exactitud deseada.
#         a: límite inferior del intervalo.
#         b: límite superior del intervalo.
#     Regresa:
#         A_i: coeficientes.
#     """
#     sistema = []
#     for i in range(n):
#         f = x**i
#         ecuacion = []
#         result = integrate(f, (x, a, b))
#         for j in range(n):
#

from sympy import symbols, integrate, solve

def generar_bases(n):
    """
    Genera las primeras n bases del espacio de polinomios (1, x, x^2, ...).
    """
    x = symbols('x')
    bases = [x**i for i in range(n)]
    return bases

def coeficientes_indeterminados(max_orden, limite_inferior, limite_superior):
    """
    Método de coeficientes indeterminados para aproximar un polinomio.

    Parámetros:
    - max_orden: Orden máximo del polinomio de aproximación.
    - limite_inferior: Extremo inferior del intervalo de la integral.
    - limite_superior: Extremo superior del intervalo de la integral.

    Retorna:
    - Lista de coeficientes del polinomio de aproximación.
    """
    x = symbols('x')

    # Generar bases del espacio de polinomios
    bases = generar_bases(max_orden)

    # Construir el sistema de ecuaciones
    sistema_ecuaciones = []
    for base in bases:
        ecuacion = integrate(base * (limite_superior - x) * (x - limite_inferior), (x, limite_inferior, limite_superior)) - 0
        sistema_ecuaciones.append(ecuacion)

    # Resolver el sistema de ecuaciones
    soluciones = solve(sistema_ecuaciones)

    # Imprimir soluciones para depuración
    print("Soluciones:", soluciones)

    # Verificar si todas las bases están presentes en las soluciones
    for base in bases:
        if base not in soluciones:
            print(f"Advertencia: La base {base} no está presente en las soluciones.")

    # Obtener los coeficientes del polinomio de aproximación
    coeficientes = [soluciones[base] for base in bases]

    return coeficientes

# Ejemplo de uso
max_orden = 3
limite_inferior = 0
limite_superior = 1

coeficientes = coeficientes_indeterminados(max_orden, limite_inferior, limite_superior)
print("Coeficientes del polinomio de aproximación:", coeficientes)

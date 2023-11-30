from sympy import symbols, integrate, solve, Eq

# Coeficientes indeterminados para polinomios de grado 3

def generar_bases(n):
    """
    Genera las primeras n bases del espacio de polinomios (1, x, x^2, ...).
    """
    x = symbols('x')
    bases = [x**i for i in range(n)]
    return bases

def coeficientes_indeterminados(max_orden, a, b):
    """
    Método de coeficientes indeterminados para aproximar un polinomio.

    Parámetros:
    - max_orden: Orden máximo del polinomio de aproximación.
    - a: Extremo inferior del intervalo de la integral.
    - b: Extremo superior del intervalo de la integral.

    Retorna:
    - Lista de coeficientes del polinomio de aproximación.
    """
    x = symbols('x')
    y, z, w = symbols('y z w')

    # Generar bases del espacio de polinomios
    bases = generar_bases(max_orden)
    # print("Bases:", bases)

    # Construir el sistema de ecuaciones
    sistema_ecuaciones = []
    potencia = 0

    # Inside your loop
    for base in bases:
        ecuacion = Eq((y*a**potencia+z*((a+b)/2)**potencia+w*b**potencia),integrate(base, (x, a, b)))
        sistema_ecuaciones.append(ecuacion)
        potencia += 1
        # print("Ecuación: ",ecuacion)

    print("Sistema de ecuaciones:", sistema_ecuaciones)

    # Resolver el sistema de ecuaciones
    soluciones = solve(sistema_ecuaciones, (y, z, w))

    # Obtener los coeficientes del polinomio de aproximación
    coeficientes = [i for i in soluciones.values()]

    return coeficientes

# Ejemplo de uso
a = 0
b = 1

coeficientes = coeficientes_indeterminados(3, a, b)
print("Coeficientes del polinomio de aproximación:", coeficientes)
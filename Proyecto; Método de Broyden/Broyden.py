import numpy as np
from scipy.optimize import approx_fprime

""" 'Buen' método Broyden para un sistema de ecuaciones no lineales.
Requiere el vector inicial X. Eps opcional. J (jacobiano) inicial aproximada por diferencias finitas."""


def jacobian_fd(f, x, h=1e-5):
    n = len(x)
    jacobian_matrix = np.zeros((n, n))
    for i in range(n):
        jacobian_matrix[i, :] = approx_fprime(x, lambda y: np.array(f(*y)).flatten()[i], h)
    return np.linalg.inv(np.matrix(jacobian_matrix))


def f(*x):
    global functions
    x_dict = {f'x{i}': x[i] for i in range(len(x))}
    results = [eval(func, {**x_dict, 'np': np}) for func in functions]
    return np.matrix(results).T


def broyden(x0, N=10, tol=1e-5):
    n = len(x0)
    header = "k \t " + "\t\t ".join([f"x{i + 1}" for i in range(n)]) + "\t\t ||x(k) - x(k-1)||"
    print(header)

    A = jacobian_fd(f, x0)
    v = f(*x0)
    k = 2
    s = -A * v
    x0 = np.matrix(x0).T + s

    while k < N:
        w = v
        v = f(*[x0[i, 0].item() for i in range(n)])
        y = v - w
        z = -A * y
        p = (s.T * A * y).item()
        A = A + 1 / p * (s + z) * s.T * A
        s = -A * v
        x0 = x0 + s
        print("{0:1d} \t {1} \t {2:1.6f}".format(k, "\t ".join("{:1.6f}".format(x0[i, 0].item()) for i in range(n)),
                                                 np.linalg.norm(s)))
        if np.linalg.norm(s) < tol:
            return x0
        k += 1


print("Método de Broyden\n")

n = int(input("Ingrese el número de funciones: "))
functions = []
for i in range(n):
    functions.append(input(f"Ingrese la función {i + 1}: "))

x = []

print("Ingrese los valores del vector inicial ('initial guess')")
for i in range(len(functions)):
    valor = float(input(f"Componente {i + 1}: "))
    x.append(valor)

broyden(x)

"""Ejemplos de entradas"""
# Ejemplo 1
# Número de funciones: 2
# f1: x0**2 - x1 - 1
# f2: x0 - x1**2 + 1
# Vector inicial:
# componente 1: 1.5
# componente 2: 2.0

# Ejemplo 2
# Número de funciones: 3
# f1: 3*x0 - np.cos(x0*x2) - 0.5
# f2: x0**2 - 81*(x1+0.1)**2 + np.sin(x2) + 1.06
# f3: np.exp(-x0*x1) + 20*x2 + (10*np.pi - 3)/3
# Vector inicial: 
# componente 1: 0.1
# componente 2: 0.1
# componente 3: -0.1

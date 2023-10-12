import math

import numpy as np

def metodoPuntosFijos(f, x_0, tol, iteraciones=10000):
    vi = f(x_0)
    numIte = 1
    error = abs(vi-x_0)
    while error >= tol and numIte <= iteraciones:
        x_0 = vi
        vi = f(x_0)
        error = abs(vi - x_0)
        numIte += 1

    if numIte > iteraciones:
        return "Máximo de iteraciones alcanzado sin lograr convergencia alguna."

    return "Raíz: " + str(vi) + "\nIteraciones: " + str(numIte)

if __name__ == "__main__":
    fx = lambda x: np.exp(-x) - x
    gx = lambda x: np.exp(-x)
    # Caso 1: Se evidencia que en menos de 14 iteraciones no logra la convergencia con la tolerancia colocada
    print(metodoPuntosFijos(gx, 0, 0.001, 15))
    print(metodoPuntosFijos(gx, 0, 0.001, 10))
    print(metodoPuntosFijos(fx, 0, 0.0001, 5))

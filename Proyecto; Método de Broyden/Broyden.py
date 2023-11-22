import numpy as np
""" "Buen" método Broyden para un sistema de ecuaciones no lineales en [`F`](@ref).
Requiere el vector inicial X. Eps opcionales. J inicial aproximada por diferenciación."""


def broyden(X, eps=1e-6):
    # Quitar comentario para ver iteración
    print(X)

    # Calcular el valor de la función en el punto X
    FX = F(X)

    # Inicializar la inversa de la matriz Jacobiana utilizando fdJ
    invJ = np.linalg.inv(fdJ(X, FX))

    # Iterar hasta que la norma de FX sea menor que eps
    while np.linalg.norm(FX) > eps:
        # Guardar el valor actual de X
        Xold = X

        # Actualizar X utilizando el método de Broyden
        X = X - np.dot(invJ, FX)

        # Quitar comentario para ver iteración
        print(X)

        # Calcular la diferencia entre los nuevos y antiguos valores de X
        deltaX = X - Xold

        # Guardar el valor actual de FX
        FXold = FX

        # Calcular el nuevo valor de la función en el punto X
        FX = F(X)

        # Calcular la diferencia entre los nuevos y antiguos valores de FX
        deltaF = FX - FXold

        # Transponer deltaX
        trans = deltaX.T

        # Actualizar la inversa de la matriz Jacobiana utilizando el método de Broyden
        invJ = invJ + np.dot((deltaX - np.dot(invJ, deltaF)), trans) / np.dot(trans, np.dot(invJ, deltaF))

    return X

"""F es la función"""

def F(X):
    # Devolver un array con los valores de la función F(X)
    return np.array([X[0]**2 - X[1] - 1, X[0] - X[1]**2 + 1])

"""fdJ toma los argumentos X, FX, h y calcula la matriz jacobiana usando diferencias finitas.
El parámetro FX es opcional y, si no se proporciona, lo calcula llamando a la función F(X).
Reemplace x1 y x2 con sus valores iniciales reales cuando use la función fdJ."""


def fdJ(X, FX=None, h=1e-4):
    # Si FX no se proporciona, calcularlo llamando a la función F(X)
    if FX is None:
        FX = F(X)

    n = len(X)
    J = np.zeros((n, n))

    # Calcular las derivadas parciales numéricas
    for i in range(n):
        X_plus_h = X.copy()
        X_plus_h[i] += h

        J[:, i] = (F(X_plus_h) - FX) / h

    return J

# Imprimir el resultado de la función broyden con un ejemplo de entrada
print(broyden([1.5, 2.0]))
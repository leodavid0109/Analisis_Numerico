import numpy as np


def richardson(n, matrix, resultant, beginning, iterations=1000):
    res = [0] * n
    for k in range(iterations):
        for i in range(n):
            res[i] = resultant[i] - sum([(matrix[i][j] * beginning[j]) for j in range(n)])
        for i in range(n):
            beginning[i] = beginning[i] + res[i]
    return beginning


if __name__ == "__main__":
    # Caso 1 de prueba. Tomado del ejemplo 2 del libro
    A = [[1, 1 / 2, 1 / 3],
         [1 / 3, 1, 1 / 2],
         [1 / 2, 1 / 3, 1]]
    x = [0, 0, 0]
    b = [11 / 18, 11 / 18, 11 / 18]

    result = richardson(3, A, b, x, 100)
    print("Vector resultante: " + str(result))
    conf = [0] * 3
    for i in range(3):
        for j in range(3):
            conf[i] += (A[i][j] * result[j])
    print("Ax=b: " + str(conf))
    print()

    # Caso 2 de Prueba.
    A = [[0.8, 0.1, 0.1],
         [0.1, 0.9, 0.1],
         [0.1, 0.1, 0.7]]
    x = [0, 0, 0]
    b = [1, 2, 3]

    result1 = richardson(3, A, b, x, 100)
    print("Vector resultante: " + str(result1))
    conf = [0] * 3
    for i in range(3):
        for j in range(3):
            conf[i] += (A[i][j] * result1[j])
    print("Ax=b: " + str(conf))
    print()

    # Caso 3 de Prueba.
    A = [[0.7, 0.2, 0.1],
         [0.3, 0.8, 0.2],
         [0.1, 0.3, 0.6]]
    x = [0, 0, 0]
    b = [2, 1, 3]

    result2 = richardson(3, A, b, x)
    print("Vector resultante: " + str(result2))
    conf = [0] * 3
    for i in range(3):
        for j in range(3):
            conf[i] += (A[i][j] * result2[j])
    print("Ax=b: " + str(conf))

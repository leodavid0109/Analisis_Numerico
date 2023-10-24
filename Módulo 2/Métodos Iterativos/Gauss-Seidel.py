def gaussSeidel(n, matrix, resultant, beginning, iterations):
    for k in range(iterations):
        for i in range(n):
            beginning[i] = (resultant[i] - sum((matrix[i][j] * beginning[j]) for j in range(n) if i != j)) / matrix[i][i]
    return beginning


if __name__ == "__main__":
    # Caso de Prueba 1. Tomado del ejemplo 3 del libro
    A = [[2, -1, 0],
         [1, 6, -2],
         [4, -3, 8]]
    x = [0, 0, 0]
    b = [2, -4, 5]

    result = gaussSeidel(3, A, b, x, 20)
    print("Vector resultante: " + str(result))
    conf = [0] * 3
    for i in range(3):
        for j in range(3):
            conf[i] += (A[i][j] * result[j])
    print("Ax=b: " + str(conf))
    print()

    # Caso de Prueba 2
    A = [[4, 1, 2],
         [3, 5, 2],
         [1, 2, 5]]
    x = [1, 1, 1]
    b = [8, 9, 9]

    result = gaussSeidel(3, A, b, x, 20)
    print("Vector resultante: " + str(result))
    conf = [0] * 3
    for i in range(3):
        for j in range(3):
            conf[i] += (A[i][j] * result[j])
    print("Ax=b: " + str(conf))
    print()

    # Caso de Prueba 3
    A = [[3, 1, 1],
         [2, 4, 1],
         [1, 1, 3]]
    x = [0, 0, 0]
    b = [5, 7, 4]

    result = gaussSeidel(3, A, b, x, 20)
    print("Vector resultante: " + str(result))
    conf = [0] * 3
    for i in range(3):
        for j in range(3):
            conf[i] += (A[i][j] * result[j])
    print("Ax=b: " + str(conf))

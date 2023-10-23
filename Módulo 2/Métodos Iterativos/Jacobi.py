def jacobi(n, matrix, resultant, beginning, iterations):
    for k in range(iterations):
        auxiliar = [0] * n
        for i in range(n):
            auxiliar[i] = (resultant[i] - sum((matrix[i][j] * beginning[j]) for j in range(n) if i != j)) / matrix[i][i]
        for i in range(n):
            beginning[i] = auxiliar[i]
    return beginning

if __name__ == "__main__":
    # Caso de Prueba 1
    A = [[4, -1, 0],
         [-1, 4, -1],
         [0, -1, 3]]
    x = [0, 0, 0]
    b = [7, 5, 4]

    result = jacobi(3, A, b, x, 20)
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

    result = jacobi(3, A, b, x, 20)
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

    result = jacobi(3, A, b, x, 20)
    print("Vector resultante: " + str(result))
    conf = [0] * 3
    for i in range(3):
        for j in range(3):
            conf[i] += (A[i][j] * result[j])
    print("Ax=b: " + str(conf))

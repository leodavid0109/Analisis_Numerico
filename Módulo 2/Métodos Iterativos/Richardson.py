def richardson(n, matrix, resultant, beginning, iterations):
    residual = [0] * n
    for k in range(iterations):
        for i in range(n):
            residual[i] = resultant[i] - sum([(matrix[i][j] * beginning[j]) for j in range(n)])
        for i in range(n):
            beginning[i] = beginning[i] + residual[i]
    return beginning, residual

if __name__ == "__main__":
    # Caso 1 de prueba. Tomado del ejemplo 2 del libro
    A = [[1, 1/2, 1/3], [1/3, 1, 1/2], [1/2, 1/3, 1]]
    x = [0, 0, 0]
    b = [11/18, 11/18, 11/18]

    result, residual = richardson(3, A, b, x, 100)
    print("Vector resultante: " + str(result))
    print("Residuos (Error): " + str(residual))

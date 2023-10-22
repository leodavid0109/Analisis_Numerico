def jacobi(n, matrix, resultant, beginning, iterations):
    for k in range(iterations):
        auxiliar = [0] * n
        for i in range(n):
            auxiliar[i] = (resultant[i] - sum((matrix[i][j] * beginning[j]) for j in range(n) if i != j)) / matrix[i][i]
        for i in range(n):
            beginning[i] = auxiliar[i]
    return beginning

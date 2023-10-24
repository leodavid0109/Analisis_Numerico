def gradienteConjugado(x, A, b, ite, tol1, tol2):
    n = len(x)
    r = [0] * n
    for i in range(n):
        r[i] = b[i] - sum((A[i][j] * x[j]) for j in range(n))
    v = r
    c = sum((r[j] * r[j]) for j in range(n))
    k = 0
    while k < ite:
        prove = (sum((v[j] * v[j]) for j in range(n))) ** (1/2)
        if prove < tol2:
            break
        z = [0] * n
        for i in range(n):
            z[i] = sum((A[i][j] * v[j]) for j in range(n))
        t = c / (sum((v[j] * z[j]) for j in range(n)))
        for i in range(n):
            x[i] += (t * v[i])
        for i in range(n):
            r[i] -= (t * z[i])
        d = sum((r[j] * r[j]) for j in range(n))
        if d < tol1:
            break
        for i in range(n):
            v[i] = r[i] + ((d / c) * v[i])
        c = d
        print(f"Iteración {k}: ")
        print("x: " + str(x))
        print("r: " + str(r))
        k += 1

    return x, k

if __name__ == "__main__":
    # Caso de Prueba 1
    A = [[4, 1],
         [1, 3]]
    x = [1, 1]
    b = [3, 2]

    result, k = gradienteConjugado(x, A, b, 100, 1e-6, 1e-6)
    print()
    if k == 100:
        print("El método no ha convergido.")
    else:
        conf = [0] * 2
        for i in range(2):
            for j in range(2):
                conf[i] += (A[i][j] * result[j])
        print("Ax=b: " + str(conf))

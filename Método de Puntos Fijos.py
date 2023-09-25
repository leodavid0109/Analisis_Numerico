def metodoPuntosFijos(f, x_0, tol, iteraciones = 10000):
    vi = f(x_0)
    numIte = 0
    error = tol + 1
    while error > tol and numIte <= iteraciones:
        vi = f(x_n)
        error = abs((x_n - x_0)/x_n)
        x_0 = x_n
        numIte += 1

    if numIte > iteraciones:
        return "Máximo de iteraciones alcanzado sin lograr convergencia alguna."

    return x_0

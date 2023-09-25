def algoritmoHorner(x_0, coeficientes):
    x_1 = coeficientes[0]
    x_2 = coeficientes[0]
    for i in range(1, len(coeficientes) + 1):
        x_1 = x_0 * x_1 + coeficientes[i]
        x_2 = x_0 * x_1 + x_1
    x_1 = x_0 * x_1 + coeficientes[-1]

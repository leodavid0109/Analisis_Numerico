def metodoNewtonHorner(grado, x_0, coeficientes, tolerancia):
    numIte = 0
    aux_2 = coeficientes
    delta = 100
    j = 1
    r = grado
    r_elementos = grado

    for i in range(r):
        aux_1 = aux_2 #aux_1 será p(x) y aux_2 será q(x)
        aux_2 = [1]*r_elementos
        aux_1[0] = coeficientes[0]
        aux_2[0] = coeficientes[0]
        while delta > tolerancia:
            x_1 = aux_1[0]
            x_2 = aux_2[0]
            k = 1
            while k < r_elementos:
                x_1 = (x_0 * x_1) + aux_1[k]
                aux_2[j] = x_1
                j += 1
                x_2 = (x_0 * x_2) + x_1
                k += 1
            x_1 = (x_0 * x_1) + aux_1[-1]
            x_3 = x_0 - (x_1 / x_2)
            delta = abs((x_3 - x_0))
            x_0 = x_3
            numIte += 1
            j = 1
        r_elementos -= 1
        print("Raíz ", i + 1, ": ", x_0)
        print("Iteraciones: ", numIte)
        print("")

        delta = 100
        numIte = 0

if __name__ == "__main__":
    #Caso 1: Función x^3 + 7x^2 - 6x - 72
    coeficientes = [1, 7, -6, -72]
    metodoNewtonHorner(3, 1, coeficientes, 0.000000000000000000001)
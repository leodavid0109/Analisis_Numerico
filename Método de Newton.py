def metodoNewton(f, f_d, x_0, tol, iteraciones=10000):
    # La función recibe cuatro parámetros, la función, su derivada, una aproximación inicial y una tolerancia
    if f(x_0) == 0:
        return x_0
    else:
        temp = -1
        delta = tol + 1
        x_1 = 0
        cantIter = 1

        while temp != 0 and abs(delta) >= tol and cantIter <= iteraciones:
            der = f_d(x_0)
            if der == 0:
                return "Derivada nula, no es posible calcular la raíz"
            else:
                delta = f(x_0) / der
                x_1 = x_0 - delta
                x_0 = x_1
                cantIter += 1

        if cantIter > iteraciones:
            return "Máximo de iteraciones alcanzado sin lograr convergencia alguna."

        return x_1
    
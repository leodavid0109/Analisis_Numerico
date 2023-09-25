import numpy as np

def metodoNewton(f, f_d, x_0, tol, iteraciones=10000):
    # La función recibe cuatro parámetros, la función, su derivada, una aproximación inicial y una tolerancia
    if f(x_0) == 0:
        return x_0
    else:
        delta = tol + 1
        x_1 = x_0
        cantIter = 1

        while f(x_1) != 0 and abs(delta) >= tol and cantIter <= iteraciones:
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

        return "Raíz: " + str(x_1) + "\nIteraciones: " + str(cantIter)


if __name__ == "__main__":
    fx = lambda x: np.exp(x) - x**2
    fdx = lambda x: np.exp(x) - 2*x

    print("Prueba 1: Función e^x - x^2 con x_0 = -1")
    print(metodoNewton(fx, fdx, -1, 0.00001))
    print("Prueba 2: Función e^x - x^2 con x_0 = 10")
    print(metodoNewton(fx, fdx, 10, 0.00001))
    print("Prueba 3: Función e^x - x^2 con x_0 = 5000")
    #print(metodoNewton(fx, fdx, 5000, 0.00001, 1000))
    print("Generó error al evaluar la función, es demasiado largo el resultado de e^5000")

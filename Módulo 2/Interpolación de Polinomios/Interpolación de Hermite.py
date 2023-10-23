from math import factorial
import numpy as np
import matplotlib.pyplot as plt

def caso1(xk, fxki, num, n, k):
    i = max(k, k - num)
    j = min(k, k - num)
    f = (fxki[n] - fxki[n - 1]) / (xk[i] - xk[j])
    return f

def caso2(l, xk, n):
    xn = 0
    for i in range(len(l)):
        if l[i][0] == xk:
            xn = i
    f = (l[xn][1][n] / factorial(n))
    return f

def interpolacion(l, xk, fxki, p, columna, filas):
    aux = []
    num = columna + 1
    for k in range(num, filas):
        if xk[k - num] != xk[k]:
            aux.append(caso1(xk, fxki, num, k - columna, k))
        else:
            aux.append(caso2(l, xk[k], len(p)))
    return aux

def hermite1(l):
    xk = []
    fxk = []
    p = []
    for i in range(len(l)):
        for j in range(len(l[i][1])):
            xk.append(l[i][0])
    for i in range(len(l)):
        for j in range(len(l[i][1])):
            fxk.append(l[i][1][0])
    columna = 0
    filas = len(xk)
    p.append(fxk[0])
    while len(p) < len(xk):
        fxk = interpolacion(l, xk, fxk, p, columna, filas)
        p.append(fxk[0])
        columna += 1
    
    x_values = np.linspace(min(x), max(x), 100)
    y_values = [polynomial_function(p, x) for x in x_values]

    plt.plot(x_values, y_values, label='Interpolación de Hermite')
    plt.scatter(x, [polynomial_function(p, xi) for xi in x], color='red', label='Puntos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    return p

def polynomial_function(coefficients, x):
    n = len(coefficients)
    result = 0
    for i in range(n):
        result += coefficients[i] * (x ** i)
    return result

def hermite(x, y, *derivatives):
    l = []
    for i in range(len(x)):
        k = []
        for j in range(len(derivatives)):
            if derivatives[j][i] == -99999999:
                continue
            k.append(derivatives[j][i])
        l.append((x[i], (y[i], *k)))
    p = hermite1(l)
    return p


x = [0, 1, 3]
y = [2, 4, 5]
dy = [1, -1, -2]
coef1 = hermite(x, y, dy) # Retorna los coeficientes del polinomio de Hermite
print(coef1)

x = [1.0, 2.0]
y = [2.0, 6.0]
dy = [3.0, 7.0]
d2y = [-99999999, 8.0] # Hay que crear un espacio vacío. En este caso el -99999999 lo representa.
coef2 = hermite(x, y, dy, d2y)
print(coef2)
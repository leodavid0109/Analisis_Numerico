import matplotlib.pyplot as plt
import numpy as np

def divided_differences(x, y):
    n = len(x)
    c = [0] * (n)
    c[0] = y[0]
    for k in range(1, n):
        d = x[k] - x[k-1]
        u = c[k-1]
        for i in range(k-2, -1, -1):
            u = u * (x[k] - x[i]) + c[i]
            d = d * (x[k] - x[i])
        c[k] = (y[k] - u) / d
    return c

def newton_interpolation(x, y, t):
    c = divided_differences(x, y)
    n = len(x)
    u = c[n-1]
    for i in range(n-2, -1, -1):
        u = (t - x[i]) * u + c[i]
    return u

# Casos de prueba
x = [5, -7, -6, 0]
y = [1, -23, -54, -954]
t = 1 # Interpolar en t = 1
valor_interpolado = newton_interpolation(x, y, t)

# Graficar los puntos
plt.scatter(x, y, label="Puntos", color='red')

# Graficar la función interpolada
x_range = np.linspace(min(x), max(x), 1000)
y_interpolated = [newton_interpolation(x, y, xi) for xi in x_range]
plt.plot(x_range, y_interpolated, label="Función Interpolada", color='blue')

# Graficar el punto interpolado
plt.scatter(t, valor_interpolado, label="Valor Interpolado", color='green')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Comprobar los resultados interpolados
assert abs(newton_interpolation(x, y, 1) - (-999)) < 1e-6
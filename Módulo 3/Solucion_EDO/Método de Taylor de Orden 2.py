import numpy as np
import matplotlib.pyplot as plt

def taylor_ode2(f, fx, fy, x0, y0, h, N):
    x_values = np.zeros(N + 1)
    y_values = np.zeros(N + 1)
    
    x_values[0] = x0
    y_values[0] = y0
    
    for i in range(N):
        x = x_values[i]
        y = y_values[i]
        y_values[i+1] = y + h * f(x, y) + (h**2 / 2) * (fx(x, y) + fy(x, y) * f(x, y))
        x_values[i+1] = x + h
    
    return x_values, y_values

# Función de ejemplo: dy/dx = x + y
def f(x, y):
    return (1+2*x)*(y**0.5)

# Derivadas parciales de la función f(x, y)
def fx(x, y):
    return 2*y**0.5  # Derivada de f con respecto a x

def fy(x, y):
    return ((1+2*x)/(2*(y**0.5))) # Derivada de f con respecto a y

# Condiciones iniciales
x0 = 0
y0 = 1
h = 0.1
N = 10

# Resuelva la EDO utilizando el método de la serie de Taylor de segundo orden
x_values, y_values = taylor_ode2(f, fx, fy, x0, y0, h, N)
print(f"\nx:{x_values}")
print(f"y:{y_values}")

# Trazar la solución
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Solución numérica')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de EDO usando series de Taylor (segundo orden)')
plt.legend()
plt.grid(True)
plt.show()

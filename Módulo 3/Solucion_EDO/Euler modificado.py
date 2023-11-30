import numpy as np
import matplotlib.pyplot as plt

def euler_modificado(f, a, b, N, y0):
    h = (b-a)/N
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    y[0] = y0

    for  i in range(0, N):
        k1 = h*f(x[i], y[i])
        k2 = h*f(x[i] + (h/2), y[i] + k1/2)
        y[i+1] = y[i] + k2
    return (x, y)

# Casos de prueba:
def test_euler_modificado():
    # Test case 1: Linear function
    def linear_fn(t, y):
        return t + y
    x1, y1 = euler_modificado(linear_fn, 0, 1, 10, 0)
    print(f"\nx:{x1}")
    print(f"y:{y1}")

    # Test case 2: Quadratic function
    def quadratic_fn(t, y):
        return t**2 + y
    x2, y2 = euler_modificado(quadratic_fn, 0, 1, 10, 0)
    print(f"\nx:{x2}")
    print(f"y:{y2}")

    # Test case 3: Exponential function
    def exponential_fn(t, y):
        return np.exp(t) + y
    x3, y3 = euler_modificado(exponential_fn, 0, 1, 10, 0)
    print(f"\nx:{x3}")
    print(f"y:{y3}")

    # Test case 4
    def f(x, y):
        return (1+2*x)*(y**0.5)
    x4, y4 = euler_modificado(f, 0, 1, 10, 1)
    print(f"\nx:{x4}")
    print(f"y:{y4}")
    print(f"\nx:{x4}")
    print(f"y:{y4}")
    plt.figure(figsize=(8, 6))
    plt.plot(x4, y4, label='Solución numérica')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución de EDO usando series de Taylor (segundo orden)')
    plt.legend()
    plt.grid(True)
    plt.show()

test_euler_modificado()
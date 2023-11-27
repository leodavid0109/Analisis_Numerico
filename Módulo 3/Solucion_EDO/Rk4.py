import numpy as np

def runge_kutta_4(f, a, b, N, y0):
    h = (b-a)/N
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    y[0] = y0

    for  i in range(0, N):
        k1 = h*f(x[i], y[i])
        k2 = h*f(x[i] + (h/2), y[i] + k1/2)
        k3 = h*f(x[i] + (h/2), y[i] + k2/2)
        k4 = h*f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    return (x, y)

# Casos de prueba:
def test_runge_kutta_4():
    # Test case 1: Linear function
    def linear_fn(t, y):
        return t + y
    x1, y1 = runge_kutta_4(linear_fn, 0, 1, 10, 0)
    print(f"\nx:{x1}")
    print(f"y:{y1}")

    # Test case 2: Quadratic function
    def quadratic_fn(t, y):
        return t**2 + y
    x2, y2 = runge_kutta_4(quadratic_fn, 0, 1, 10, 0)
    print(f"\nx:{x2}")
    print(f"y:{y2}")

    # Test case 3: Exponential function
    def exponential_fn(t, y):
        return np.exp(t) + y
    x3, y3 = runge_kutta_4(exponential_fn, 0, 1, 10, 0)
    print(f"\nx:{x3}")
    print(f"y:{y3}")

    # Test case 4
    def exponential_fn(x, y):
        return (1+2*x)*(y**0.5)
    x4, y4 = runge_kutta_4(exponential_fn, 0, 1, 2, 1)
    print(f"\nx:{x4}")
    print(f"y:{y4}")

test_runge_kutta_4()
import numpy as np

# Si p = 0, tenemos el método de Euler que ya esta implementado.

# Si p = 1:
def adams_bashfort_1(f, a, b, N, y0):
    h = (b-a)/N
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    y[0] = y0

    for  i in range(0, N):
        y[i+1] = y[i] + (h/2)*(3*f(x[i], y[i]) - f(x[i-1], y[i-1]))
    return (x, y)

# Si p = 2:
def adams_bashfort_2(f, a, b, N, y0):
    h = (b-a)/N
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    y[0] = y0

    for  i in range(0, N):
        y[i+1] = y[i] + (h/12)*(23*f(x[i], y[i]) - 13*f(x[i-1], y[i-1]) + 5*f(x[i-2], y[i-2]))
    return (x, y)

# Casos de prueba:
def test_adams_bashfort_1():
    # Test case 1: Linear function
    def linear_fn(t, y):
        return t + y
    x1, y1 = adams_bashfort_1(linear_fn, 0, 1, 10, 0)
    print(f"\nx:{x1}")
    print(f"y:{y1}")

    # Test case 2: Quadratic function
    def quadratic_fn(t, y):
        return t**2 + y
    x2, y2 = adams_bashfort_1(quadratic_fn, 0, 1, 10, 0)
    print(f"\nx:{x2}")
    print(f"y:{y2}")

    # Test case 3: Exponential function
    def exponential_fn(t, y):
        return np.exp(t) + y
    x3, y3 = adams_bashfort_1(exponential_fn, 0, 1, 10, 0)
    print(f"\nx:{x3}")
    print(f"y:{y3}")

    # Test case 4
    def exponential_fn(x, y):
        return (1+2*x)*(y**0.5)
    x4, y4 = adams_bashfort_1(exponential_fn, 0, 1, 4, 1)
    print(f"\nx:{x4}")
    print(f"y:{y4}")

print("--------------Adams-Bashfort con p=1:--------------")
test_adams_bashfort_1()

def test_adams_bashfort_2():
    # Test case 1: Linear function
    def linear_fn(t, y):
        return t + y
    x1, y1 = adams_bashfort_2(linear_fn, 0, 1, 10, 0)
    print(f"\nx:{x1}")
    print(f"y:{y1}")

    # Test case 2: Quadratic function
    def quadratic_fn(t, y):
        return t**2 + y
    x2, y2 = adams_bashfort_2(quadratic_fn, 0, 1, 10, 0)
    print(f"\nx:{x2}")
    print(f"y:{y2}")

    # Test case 3: Exponential function
    def exponential_fn(t, y):
        return np.exp(t) + y
    x3, y3 = adams_bashfort_2(exponential_fn, 0, 1, 10, 0)
    print(f"\nx:{x3}")
    print(f"y:{y3}")

    # Test case 4
    def exponential_fn(x, y):
        return (1+2*x)*(y**0.5)
    x4, y4 = adams_bashfort_2(exponential_fn, 0, 1, 2, 1)
    print(f"\nx:{x4}")
    print(f"y:{y4}")

print("\n--------------Adams-Bashfort con p=2:--------------")
test_adams_bashfort_2()
import numpy as np

# Si p = 0, tenemos el método de Euler implicito:
def adams_moulton_0(f, a, b, N, y0):
    h = (b-a)/N
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    y[0] = y0

    # generar estimaciones iniciales utilizando Runge-Kutta
    for i in range(len(x) - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(x[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    for i in range(2, len(x) - 1):
         y[i+1] = y[i] + h*f(x[i+1], y[i+1])

    return (x, y)

# Si p = 1, tenemos el método del trapecio.
def adams_moulton_1(f, a, b, N, y0):
    h = (b-a)/N
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    y[0] = y0

    # generar estimaciones iniciales utilizando Runge-Kutta
    for i in range(len(x) - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(x[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    for i in range(2, len(x) - 1):
        y[i+1] = y[i] + (h/2) * (f(x[i+1], y[i+1]) + f(x[i], y[i]))

    return (x, y)

# Si p = 2:
def adams_moulton_2(f, a, b, N, y0):
    h = (b-a)/N
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    y[0] = y0

    # generar estimaciones iniciales utilizando Runge-Kutta
    for i in range(len(x) - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(x[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    for i in range(2, len(x) - 1):
        y[i + 1] = y[i] + h / 12 * (5 * f(x[i+1], y[i+1]) + 8 * f(x[i], y[i]) - f(x[i - 1], y[i - 1]))

    return (x, y)

# Casos de prueba:
def test_adams_moulton_0():
    # Test case 1: Linear function
    def linear_fn(t, y):
        return t + y
    x1, y1 = adams_moulton_0(linear_fn, 0, 1, 10, 0)
    print(f"\nx:{x1}")
    print(f"y:{y1}")

    # Test case 2: Quadratic function
    def quadratic_fn(t, y):
        return t**2 + y
    x2, y2 = adams_moulton_0(quadratic_fn, 0, 1, 10, 0)
    print(f"\nx:{x2}")
    print(f"y:{y2}")

    # Test case 3: Exponential function
    def exponential_fn(t, y):
        return np.exp(t) + y
    x3, y3 = adams_moulton_0(exponential_fn, 0, 1, 10, 0)
    print(f"\nx:{x3}")
    print(f"y:{y3}")

    # Test case 4
    def exponential_fn(x, y):
        return (1+2*x)*(y**0.5)
    x4, y4 = adams_moulton_0(exponential_fn, 0, 1, 2, 1)
    print(f"\nx:{x4}")
    print(f"y:{y4}")

print("--------------Adams-Moulton con p=0:--------------")
test_adams_moulton_0()

def test_adams_moulton_1():
    # Test case 1: Linear function
    def linear_fn(t, y):
        return t + y
    x1, y1 = adams_moulton_1(linear_fn, 0, 1, 10, 0)
    print(f"\nx:{x1}")
    print(f"y:{y1}")

    # Test case 2: Quadratic function
    def quadratic_fn(t, y):
        return t**2 + y
    x2, y2 = adams_moulton_1(quadratic_fn, 0, 1, 10, 0)
    print(f"\nx:{x2}")
    print(f"y:{y2}")

    # Test case 3: Exponential function
    def exponential_fn(t, y):
        return np.exp(t) + y
    x3, y3 = adams_moulton_1(exponential_fn, 0, 1, 10, 0)
    print(f"\nx:{x3}")
    print(f"y:{y3}")

    # Test case 4
    def exponential_fn(x, y):
        return (1+2*x)*(y**0.5)
    x4, y4 = adams_moulton_1(exponential_fn, 0, 1, 2, 1)
    print(f"\nx:{x4}")
    print(f"y:{y4}")

print("\n--------------Adams-Moulton con p=1:--------------")
test_adams_moulton_1()

def test_adams_moulton_2():
    # Test case 1: Linear function
    def linear_fn(t, y):
        return t + y
    x1, y1 = adams_moulton_2(linear_fn, 0, 1, 10, 0)
    print(f"\nx:{x1}")
    print(f"y:{y1}")

    # Test case 2: Quadratic function
    def quadratic_fn(t, y):
        return t**2 + y
    x2, y2 = adams_moulton_2(quadratic_fn, 0, 1, 10, 0)
    print(f"\nx:{x2}")
    print(f"y:{y2}")

    # Test case 3: Exponential function
    def exponential_fn(t, y):
        return np.exp(t) + y
    x3, y3 = adams_moulton_2(exponential_fn, 0, 1, 10, 0)
    print(f"\nx:{x3}")
    print(f"y:{y3}")

    # Test case 4
    def exponential_fn(x, y):
        return (1+2*x)*(y**0.5)
    x4, y4 = adams_moulton_2(exponential_fn, 0, 1, 2, 1)
    print(f"\nx:{x4}")
    print(f"y:{y4}")

print("\n--------------Adams-Moulton con p=2:--------------")
test_adams_moulton_2()
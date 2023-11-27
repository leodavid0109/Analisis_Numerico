import numpy as np

def punto_medio(f, a, b, N, y0):
    h = (b-a)/N
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    y[0] = y0

    for  i in range(0, N):
        y[i+1] = y[i] + h * f(x[i] + (h/2.0), y[i] + ((h/2.0)*f(x[i],y[i])) )

    return (x, y)

# Casos de prueba:
def test_punto_medio():
    # Test case 1: Linear function
    def linear_fn(t, y):
        return t + y
    x1, y1 = punto_medio(linear_fn, 0, 1, 10, 0)
    print(f"\nx:{x1}")
    print(f"y:{y1}")

    # Test case 2: Quadratic function
    def quadratic_fn(t, y):
        return t**2 + y
    x2, y2 = punto_medio(quadratic_fn, 0, 1, 10, 0)
    print(f"\nx:{x2}")
    print(f"y:{y2}")

    # Test case 3: Exponential function
    def exponential_fn(t, y):
        return np.exp(t) + y
    x3, y3 = punto_medio(exponential_fn, 0, 1, 10, 0)
    print(f"\nx:{x3}")
    print(f"y:{y3}")

    # Test case 4
    def exponential_fn(x, y):
        return (1+2*x)*(y**0.5)
    x4, y4 = punto_medio(exponential_fn, 0, 1, 2, 1)
    print(f"\nx:{x4}")
    print(f"y:{y4}")
    
test_punto_medio()
import numpy as np

def Bairstow(a, u, v, tol = 1e-12, max=50):
    n = len(a) - 1
    # Normalizar
    a = [a[i]/a[0] for i in range(len(a))]
    raices = []
    pasos = 0
    while True:
        if n <= 2:
            break
        else:
            pasos, a, u, v = solve_higher_degree(a, u, v, tol, max)
            x1, x2 = solve_quadratic(u, v)
            raices.append(x1)
            raices.append(x2)
            n += -2
    if n == 2:
        b = a[1]
        c = a[2]
        x1, x2 = solve_quadratic(b, c)
        raices.append(x1)
        raices.append(x2)
        pasos += 1
    elif n == 1:
        b = a[1]
        x = solve_linear(b)
        raices.append(x)
        pasos += 1
    if n == 0:
        return
    print("\nUnas buenas aproximaciones a las raices buscadas son: (alcanzadas en " + str(pasos) + " pasos)")
    num = 1
    for i in raices:
        print("Raíz " + str(num) + ": ", "{:e}".format(np.real(i)), "+", "{:g}j".format(np.imag(i)))
        num += 1

def solve_linear(b):
    x1 = -b
    return x1

def solve_quadratic(b, c):
    D = b ** 2 - 4 * c
    x1 = (-b + D ** 0.5) / 2
    x2 = (-b - D ** 0.5) / 2
    return x1, x2

def solve_higher_degree(a, u, v, tol, max):
    pasos = 0
    n = len(a) - 1
    b = [0, 0]
    for j in range(len(a)):
        b.append(a[j] + u*b[j+1] + v*b[j])
    b = b[2:]
    while (abs(b[-1]) > tol or abs(b[-2]) > tol) and pasos < max:
        c = [0, 0]
        for j in range(len(b)):
            c.append(b[j] + u*c[j+1] + v*c[j])
        c = c[2:-1]
        J = c[n-2] ** 2 - c[n-1] * c[n-3]
        u = u + (b[n]*c[n-3] - b[n-1]*c[n-2]) / J
        v = v + (b[n-1]*c[n-1] - b[n]*c[n-2]) / J
        b = [0, 0]
        for j in range(len(a)):
            b.append(a[j] + u*b[j+1] + v*b[j])
        b = b[2:]
        pasos += 1
    return pasos, b[:-2], -u, -v

# Test case 1: x^2 - 5x + 6 = 0, expected roots: [2, 3]
a = [1, -5, 6]
u = 1
v = 1
Bairstow(a, u, v)

# Test case 2: x + 1 = 0, expected roots: [-1]
a = [1, 1]
u = 1
v = 1
Bairstow(a, u, v)

# Test case 3: x^3 - 1 = 0, expected roots: [(-0.49999999999999994+0.8660254037844386j), (-0.5-0.8660254037844386j), 1.0]
a = [1, 0, 0, -1]
u = 1
v = 1
Bairstow(a, u, v)

# Test case 4: -4x^3 + 8x^2 - 5x + 1 = 0, expected roots: [1 + 0j , 0.5 + 0j , 0.5 + 0j] 
a = [-4, 8, -5, 1]
u = 1
v = 1
Bairstow(a, u, v)

# Test case 5: x^4 - 3x^3 + 3x^2 - 3x + 2 = 0, expected roots: [+i, -i, 2, 1] 
a = [1, -3, 3, -3, 2]
u = 0.1
v = 0.1
Bairstow(a, u, v)
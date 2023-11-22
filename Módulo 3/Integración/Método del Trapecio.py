def trapecio(f, a, b, n):
    h = (b - a) / n
    suma = 0
    for i in range(1, n):
        suma += f(a + i * h)
    return h * (f(a) + 2 * suma + f(b)) / 2

def f(x):
    return 1/(1 + x**2)

print(trapecio(f, 0, 1, 1000))
def simpson13(a,b):
    integral = (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
    return integral

# Función a integrar
def f(x):
    return 1/(1 + x**2)

# Límites de integración
a = 0
b = 1

print(f"El resultado dado por la regla de simpson 1/3 es: {simpson13(a, b)}")
from matplotlib import pyplot as plt
import numpy as np

def secant(f, a, b, tol, max):
    # Almacene los valores iniciales para su posterior trazado.
    a0 = a
    b0 = b

    # Calcular la primera aproximación usando el método de la secante.
    c = a - (b-a)*f(a)/( f(b) - f(a) )
    pasos = 1

    # Iniciar un bucle hasta que la diferencia entre f(c) y c sea menor que la tolerancia.
    while (abs(f(c)) > tol):

        # Manejar el caso donde f(a) es igual a f(b) para evitar la división por cero.
        if f(a) == f(b):
            print("Error, división por cero!")
            break
        
        # Calcular una nueva aproximación usando el método de la secante.
        c = a - (b-a)*f(a)/( f(b) - f(a) )

        # Actualizar a y b para la siguiente iteración.
        a = b
        b = c
        pasos += 1
        
        # Verificar si se ha alcanzado el número máximo de iteraciones permitidas.
        if pasos > max:
            print("No converge!")
            break

    # Imprimir la aproximación encontrada y el número de pasos necesarios.
    print("Una aproximación a la raíz buscada es x = ", c)
    print("Y es alcanzada en", pasos, "pasos")

    # Trazar la función
    x = np.arange(a0,b0,0.1)
    y = np.cos(x)-x**3

    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("f(x)")
    plt.show()
        
    x = np.linspace(a0, b0, 100)
    plt.plot(x, [f(i) for i in x])


# Definir los valores iniciales.
f = lambda x: x**3 - 5*x - 9
a = 2
b = 3
tol = 0.000001
max = 10

# Iniciar el método.
secant(f, a, b, tol, max)
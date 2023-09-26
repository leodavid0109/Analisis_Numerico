from matplotlib import pyplot as plt
import numpy as np

def biseccion(f, a, b, tol, max):
    # Almacene los valores iniciales para su posterior trazado.
    a0 = a
    b0 = b

    # Comprobar si los valores iniciales a y b son válidos
    if f(a) * f(b) >= 0:
        print("El método de bisección no se puede emplear")
        return None

    pasos =1
    
    # Calcular el punto medio y el valor de la función en el punto medio.
    xm = (a+b)/2
    fxm = f(xm)
    
    # Comprobar la tolerancia.
    if abs(fxm) <= tol:
        return xm
    
    # Loop principal del método.
    while (abs(fxm) > tol):
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm

        # Actualizar los pasos y el intervalo [a, b] según el signo de f(a) * f(xm).
        pasos += 1
        xm = (a+b)/2
        fxm = f(xm)

        if pasos > max:
            print("No converge!")
            break
    
    # Imprimir la aproximación encontrada y el número de pasos necesarios.
    print("Una aproximación a la raíz buscada es x = ", xm)
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

# Llame al método de bisección con la función y los parámetros especificados.
biseccion(f, a, b, tol, max)
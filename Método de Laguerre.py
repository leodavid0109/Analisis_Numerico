import numpy as np

def hallar_raices(a, z0, tol=1.0e-14):
    a.reverse()
    pasos = 0
    # Obtener el grado del polinomio
    grado = len(a) - 1

    # Inicializar una lista para almacenar las raíces
    raices = [0] * grado

    # Crear una copia de los coeficientes originales
    b = [x for x in a]

    # Bucle para encontrar las raíces
    for i in range(grado - 1, -1, -1):
        v = [0] * (i + 2)

        # Copiar coeficientes a v
        for j in range(0, i + 2):
            v[j] = b[j]

        # Usar el método Laguerre para encontrar una raíz
        resultado = laguerre(v, z0)
        
        # Tenemos que aseguranrnos de que se haya encontrado una raíz en el método Laguerre
        if resultado != None:
            v, z0, k = resultado
            pasos += k

        else:
            return
        
        # Vemos si la parte compleja de la raíz es muy pequeña y la descartamos
        if(abs(np.imag(z0)) <= 2 * tol * abs(np.real(z0))):
              z0 = np.real(z0) + 0*1j
        
        # Almacenar la raíz encontrada
        raices[i] = z0
        d = b[i + 1]

        # Actualizar los coeficientes restantes
        for j in range(i, -1, -1):
            c = b[j]
            b[j] = d
            d = z0 * d + c

    print("\nUnas aproximaciones a las raices buscadas son:")
    num = 1
    for i in raices:
        print("Raíz " + str(num) + ": ", "{:e}".format(np.real(i)), "+", "{:g}j".format(np.imag(i)))
        num += 1
    print("Y son alcanzadas en", pasos, "pasos")

def laguerre(coeficientes, z0, tol = np.finfo(float).eps, max_iteraciones = 100):
    # Inicialización de variables
    n = len(coeficientes) - 1

    # Bucle principal para las iteraciones de Laguerre
    for k in range(1, max_iteraciones):
        a = coeficientes[n]
        b = 0
        y = 0

        # Bucle para calcular los coeficientes recursivamente
        for j in range(n-1, -1, -1):
            y = z0 * y + b
            b = z0 * b + a
            a = z0 * a + coeficientes[j]
            
        if abs(a) <= tol:
            # Convergencia alcanzada
            return coeficientes, z0, k

        # Fórmula de Laguerre
        A = b / a
        B = A**2 - 2 * y / a
        R = ((n - 1) * (n * B - A**2)) ** (0.5)
        C1 = A + R
        C2 = A - R
        m = max([C1, C2], key=abs)
        s = n / m
        z0 -= s

    # No se alcanzó la convergencia después de las iteraciones
    print("No converge! Demasiadas iteraciones.")
    
# Test case 1: x^2 - 5x + 6 = 0, expected roots: [2, 3]
a = [1, -5, 6]
z0 = 1
hallar_raices(a, z0)

# Test case 2: x + 1 = 0, expected roots: [-1]
a = [1, 1]
z0 = 1
hallar_raices(a, z0)

# Test case 3: x^3 - 1 = 0, expected roots: [(-0.49999999999999994+0.8660254037844386j), (-0.5-0.8660254037844386j), 1.0]
a = [1, 0, 0, -1]
z0 = 1
hallar_raices(a, z0)

# Test case 4: -4x^3 + 8x^2 - 5x + 1 = 0, expected roots: [1.000000e+00 + 0j , 5.000000e-01 + -8.27862e-09j , 5.000000e-01 + 8.27862e-09j] 
a = [-4, 8, -5, 1]
z0 = 1
hallar_raices(a, z0)

# Test case 5: x^4 - 3x^3 + 3x^2 - 3x + 2 = 0, expected roots: [+i, -i, 2, 1] 
a = [1, -3, 3, -3, 2]
z0 = 1
hallar_raices(a, z0)
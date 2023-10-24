import numpy as np

def descenso_mas_rapido(x0, A, b, M):
    x = x0
    for k in range(M):
        v = b - np.dot(A, x)
        t = np.dot(v, v) / np.dot(v, np.dot(A, v))
        x = x + t * v
        print(f'k: {k + 1}, x: {x}')
    return x

# Ejemplo de uso:
# Define tus valores iniciales
x0 = np.array([0.0, 0.0])  # Suposición inicial para x
A = np.array([[2.0, 1.0], [1.0, 3.0]])  # Matriz A
b = np.array([3.0, 2.0])  # Vector b
M = 5  # Número de iteraciones

# Ejecuta el método del descenso más rápido
x_final = descenso_mas_rapido(x0, A, b, M)

conf = [0] * 2
for i in range(2):
    for j in range(2):
        conf[i] += (A[i][j] * x_final[j])
print("Ax=b: " + str(conf))
import numpy as np
from scipy.optimize import approx_fprime

def jacobian_fd(f, x, h=1e-5):
    n = len(x)
    jacobian_matrix = np.zeros((n, n))
    for i in range(n):
        jacobian_matrix[i, :] = approx_fprime(x, lambda x: np.array(f(x)).flatten()[i], h)
    print(jacobian_matrix)
    return np.linalg.inv(np.matrix(jacobian_matrix))

def broyden(x0, N = 10, tol = 1e-5):
    n = len(x0)
    print("k \t " + "\t ".join([f"x{i+1}" for i in range(n)]) + "\t ||x(k) - x(k-1)||")
    A = jacobian_fd(f, x0)
    v = f(x0)
    k = 2
    s = -A * v 
    x0 = np.matrix(x0).T + s
            
    while k < N:
        w = v
        v = f(*[x0[i,0].item() for i in range(x0.shape[0])])
        y = v - w
        z = -A * y
        p = (s.T * A * y).item()
        A = A+1/p*(s+z)*s.T*A
        s = -A * v
        x0 = x0 + s
        values = [x0[i,0].item() for i in range(n)]
        print("{0:1d} \t {1} \t {2:1.6f}".format(k, "\t ".join("{:1.6f}".format(val) for val in values), np.linalg.norm(s)))
        if np.linalg.norm(s) < tol:
            return x0
        k += 1

def user_function():
    n = int(input("Enter the number of functions: "))
    print("Enter your functions. Use 'x[0]', 'x[1]', 'x[2]', etc. for variables.")
    functions = [input(f"Enter function {i+1}: ") for i in range(n)]
    return f

def f(x):
    return np.matrix([eval(func) for func in functions]).T

print("Método de Broyden")
f = user_function()
x = np.array([0.1, 0.1, -0.1])
broyden(x)
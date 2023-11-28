import numpy as np
from scipy.optimize import approx_fprime

def jacobian_fd(f, x, h=1e-5):
    n = len(x)
    jacobian_matrix = np.zeros((n, n))
    for i in range(n):
        jacobian_matrix[i, :] = approx_fprime(x, lambda x: np.array(f(*x)).flatten()[i], h)
    return np.linalg.inv(np.matrix(jacobian_matrix))

# Define the function
def f(x1, x2, x3):
    f1 = (3*x1 - np.cos(x1*x3) - 0.5)
    f2 = (x1**2 - 81*(x2+0.1)**2 + np.sin(x3) + 1.06)
    f3 = (np.exp(-x1*x2) + 20*x3 + (10*np.pi - 3)/3)
    return np.matrix([[f1], [f2], [f3]])

def broyden(N = 10, x0 = np.array([0.1, 0.1, -0.1]), tol = 1e-5):
    print("k \t x1 \t x2 \t x3 \t ||x(k) - x(k-1)||")

    A = jacobian_fd(f, x0)
    v = f(x0[0],x0[1],x0[2])
    k = 2
    s = -A * v 
    x0 = np.matrix(x0).T + s
            
    while k < N:
        w = v
        v = f(x0[0,0].item(), x0[1,0].item(), x0[2,0].item())
        y = v - w
        z = -A * y
        p = (s.T * A * y).item()
        A = A+1/p*(s+z)*s.T*A
        s = -A * v
        x0 = x0 + s
        print("{0:1d} \t {1:1.6f} \t {2:1.6f} \t {3:1.6f} \t {4:1.6f}".format(k, x0[0,0].item(), x0[1,0].item(), x0[2,0].item(), np.linalg.norm(s)))
        if np.linalg.norm(s) < tol:
            return x0
        k += 1

broyden()
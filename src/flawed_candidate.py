# INTENTIONALLY FLAWED CANDIDATE — evaluator practice only.
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import trapezoid

A = np.array([[4.0, 1.0], [1.0, 3.0]])
b = np.array([1.0, 2.0])
# ERROR: explicitly forms inverse rather than using a linear solver.
x = np.linalg.inv(A) @ b
# ERROR: residual alone is reported; no condition number or forward error.
print("Residual:", np.linalg.norm(A @ x - b))
# ERROR: root is returned without residual verification.
root = brentq(lambda z: z**3 + z - 1, 0, 1)
print("Root:", root)
# ERROR: coarse estimate is incorrectly called exact; no grid refinement.
grid = np.linspace(0, 1, 11)
approx = trapezoid(np.exp(-grid**2), x=grid)
print("Integral:", approx, "(claimed exact)")

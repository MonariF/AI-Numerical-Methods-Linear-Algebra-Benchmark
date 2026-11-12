import numpy as np
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import brentq, newton
from scipy.integrate import trapezoid, simpson
from scipy.special import erf

def linear_system_problem():
    M = np.array([[1.,2.,0.,1.,3.,2.],[2.,1.,1.,0.,2.,1.],
        [0.,1.,3.,2.,1.,0.],[1.,0.,2.,4.,1.,2.],
        [3.,2.,1.,1.,5.,0.],[2.,1.,0.,2.,0.,6.]])
    Q, _ = np.linalg.qr(M)
    A = Q @ np.diag([1.,2.,4.,8.,16.,32.]) @ Q.T
    x_true = np.array([1.,-2.,0.5,3.,-1.,2.])
    b = A @ x_true
    x_direct = np.linalg.solve(A, b)
    x_cholesky = cho_solve(cho_factor(A, lower=True), b)
    return {
        "condition_number_2": float(np.linalg.cond(A, 2)),
        "residual_norm_2": float(np.linalg.norm(A @ x_direct - b)),
        "relative_forward_error": float(np.linalg.norm(x_direct-x_true)/np.linalg.norm(x_true)),
        "direct_cholesky_difference": float(np.linalg.norm(x_direct-x_cholesky))
    }

def root_finding_problem():
    f = lambda x: x**3 + x - 1.0
    rb = float(brentq(f, 0.0, 1.0, xtol=1e-13))
    rn = float(newton(f, x0=0.7, fprime=lambda x: 3*x*x+1, tol=1e-13))
    return {"root_brentq": rb, "root_newton": rn,
            "absolute_residual": abs(float(f(rb))),
            "method_difference": abs(rb-rn)}

def quadrature_problem():
    exact = float(np.sqrt(np.pi)*erf(1.0)/2.0)
    grids = {}
    for n in (101, 501, 1001):
        x = np.linspace(0.0, 1.0, n); y = np.exp(-x*x)
        t = float(trapezoid(y, x=x)); s = float(simpson(y, x=x))
        grids[str(n)] = {"trapezoid": t, "simpson": s,
            "trapezoid_abs_error": abs(t-exact), "simpson_abs_error": abs(s-exact)}
    return {"analytical_value": exact, "grids": grids}

def evaluate():
    return {"linear_system": linear_system_problem(),
            "root_finding": root_finding_problem(),
            "quadrature": quadrature_problem()}

if __name__ == "__main__":
    r = evaluate()
    print("Numerical methods and linear algebra benchmark")
    for section, values in r.items(): print(section, values)

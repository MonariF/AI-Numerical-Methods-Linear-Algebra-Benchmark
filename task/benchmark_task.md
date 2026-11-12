# Task 005: Numerical Linear Algebra, Root Finding and Quadrature

Use Python, NumPy and SciPy to complete the following tasks.

## A. Linear system
The reference implementation constructs a symmetric positive-definite matrix `A`, a known solution `x_true`, and `b = A @ x_true`.
1. Solve `Ax=b` using `numpy.linalg.solve`.
2. Solve independently using `scipy.linalg.cho_factor` and `cho_solve`.
3. Report the 2-norm residual, relative forward error and 2-norm condition number.
4. Explain the distinction between residual and forward error.

## B. Nonlinear root
Find the unique root of `f(x)=x^3+x-1` on `[0,1]` using `scipy.optimize.brentq`. Verify the absolute residual and compare with an independent Newton solution.

## C. Numerical integration
Approximate `integral_0^1 exp(-x^2) dx` using composite trapezoidal and Simpson rules on refined uniform grids. Compare with `sqrt(pi)/2 * erf(1)` and explain convergence.

Critical errors: preferring explicit matrix inversion to a linear solver; reporting solver success without residual checks; confusing residual and forward error; failing to verify a root; claiming a coarse quadrature estimate is exact.

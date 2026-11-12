# Evaluator Notes — Task 005

1. `inv(A) @ b` is generally less desirable than `solve(A,b)` and performs unnecessary work.
2. A small residual does not always imply small forward error for an ill-conditioned matrix. Report condition number and compare with the known solution.
3. Verify the root using `abs(f(root))`; explain the sign-changing bracket. Brent's method is robust when continuity and a bracket are established.
4. A coarse trapezoid estimate is approximate, not exact. Refine the grid and compare both rules against the analytical integral. Simpson's rule should converge faster for this smooth integrand.

The SPD matrix has controlled conditioning. The root is unique on [0,1] because the derivative is positive. The integral has a closed-form reference involving the error function.

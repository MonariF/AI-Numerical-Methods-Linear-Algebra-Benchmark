import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from reference_solution import evaluate, linear_system_problem, root_finding_problem, quadrature_problem

def test_linear_solvers_and_diagnostics():
    r = linear_system_problem()
    assert r["condition_number_2"] >= 1
    assert r["residual_norm_2"] < 1e-10
    assert r["relative_forward_error"] < 1e-10
    assert r["direct_cholesky_difference"] < 1e-10

def test_root_accuracy_and_method_agreement():
    r = root_finding_problem()
    assert 0 < r["root_brentq"] < 1
    assert r["absolute_residual"] < 1e-10
    assert r["method_difference"] < 1e-10

def test_quadrature_converges_on_refined_grid():
    r = quadrature_problem()["grids"]
    assert r["1001"]["trapezoid_abs_error"] < r["101"]["trapezoid_abs_error"]
    assert r["1001"]["simpson_abs_error"] < r["501"]["simpson_abs_error"]
    assert r["1001"]["simpson_abs_error"] < 1e-9

def test_simpson_more_accurate_than_trapezoid():
    r = quadrature_problem()["grids"]["1001"]
    assert r["simpson_abs_error"] < r["trapezoid_abs_error"]

def test_evaluation_sections_present():
    assert set(evaluate()) == {"linear_system", "root_finding", "quadrature"}

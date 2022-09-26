from tdd_solve.solve import solve
import pytest


def test_solve_exists():
    from tdd_solve import solve
    assert hasattr(solve, "solve")


def test_equation_does_not_have_roots():
    a, b, c = 1, 0, 1
    assert solve(a, b, c) == []


def test_equation_has_two_roots():
    a, b, c = 1, 0, -1
    assert solve(a, b, c) == [1.0, -1.0]


def test_equatino_has_one_root():
    a, b, c = 1, 2, 1
    assert solve(a, b, c) == [-1.0]


def test_a_equals_zero_rises_error():
    a, b, c = 0, 0, 0
    with pytest.raises(ValueError):
        solve(a, b, c)


def test_equation_for_very_small_discriminant():
    a, b, c = 0.0001, 0.00002, 0.0001
    assert solve(a, b, c) == [-1e-09]


def test_params_nan_raises_error():
    a, b, c = float('nan'), float('nan'), float('nan')
    with pytest.raises(ValueError):
        solve(a, b, c)


def test_params_inf_raises_error():
    a, b, c = float('inf'), float('inf'), float('inf')
    with pytest.raises(ValueError):
        solve(a, b, c)


def test_params_negative_inf_raises_error():
    a, b, c = float('-inf'), float('-inf'), float('-inf')
    with pytest.raises(ValueError):
        solve(a, b, c)

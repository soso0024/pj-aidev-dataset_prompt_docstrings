import pytest
from utils.math_utils import add, multiply, safe_divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(2.5, 2) == 5.0


def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(7, 2) == 3.5
    assert safe_divide(0, 5) == 0.0
    assert safe_divide(-10, 2) == -5.0


def test_safe_divide_by_zero():
    assert safe_divide(10, 0) is None
    assert safe_divide(0, 0) is None

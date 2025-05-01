import pytest
from utils.math_utils import add, multiply, safe_divide

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_mixed():
    assert add(2, -3) == -1

def test_add_zero():
    assert add(0, 0) == 0

def test_add_float():
    assert add(2.5, 3.5) == 6.0

def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-2, -3) == 6

def test_multiply_mixed():
    assert multiply(2, -3) == -6

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_multiply_float():
    assert multiply(2.5, 2) == 5.0

def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5

def test_safe_divide_zero_denominator():
    assert safe_divide(10, 0) is None

def test_safe_divide_zero_numerator():
    assert safe_divide(0, 5) == 0

def test_safe_divide_negative():
    assert safe_divide(-10, 2) == -5

def test_safe_divide_float():
    assert safe_divide(5, 2) == 2.5

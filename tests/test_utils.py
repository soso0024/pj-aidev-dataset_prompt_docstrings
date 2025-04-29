import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from utils.string_utils import hash_password, to_upper
from utils.math_utils import add, multiply, safe_divide


def test_hash_password():
    result = hash_password("password123")
    assert isinstance(result, str)
    assert len(result) == 64  # SHA-256 produces a 64-character hex string
    assert hash_password("password123") == hash_password("password123")
    assert hash_password("password123") != hash_password("different")


def test_to_upper():
    assert to_upper("hello") == "HELLO"
    assert to_upper("Hello World") == "HELLO WORLD"
    assert to_upper("") == ""
    assert to_upper("123") == "123"


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(0.5, 2) == 1.0


def test_safe_divide():
    assert safe_divide(6, 3) == 2.0
    assert safe_divide(1, 2) == 0.5
    assert safe_divide(0, 5) == 0.0
    assert safe_divide(5, 0) is None

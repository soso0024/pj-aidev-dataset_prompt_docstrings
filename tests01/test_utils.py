import pytest
from utils.math_utils import add, multiply, safe_divide
from utils.string_utils import hash_password, to_upper


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(2.5, 2) == 5.0


def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5
    assert safe_divide(-10, 2) == -5
    assert safe_divide(0, 5) == 0


def test_safe_divide_by_zero():
    assert safe_divide(10, 0) is None


def test_hash_password():
    hashed = hash_password("password123")
    assert isinstance(hashed, str)
    assert len(hashed) == 64  # SHA-256 produces a 64-character hexadecimal string
    assert hashed == "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"

    # Test that same input produces same output
    assert hash_password("password123") == hash_password("password123")

    # Test that different inputs produce different outputs
    assert hash_password("password123") != hash_password("password124")


def test_to_upper():
    assert to_upper("hello") == "HELLO"
    assert to_upper("Hello World") == "HELLO WORLD"
    assert to_upper("") == ""
    assert to_upper("123") == "123"

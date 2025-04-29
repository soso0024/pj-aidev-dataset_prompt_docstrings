import pytest
import hashlib
from utils.string_utils import hash_password, to_upper


def test_hash_password():
    password = "test123"
    expected = hashlib.sha256(password.encode("utf-8")).hexdigest()

    result = hash_password(password)

    assert result == expected
    assert result == "ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae"


def test_hash_password_empty():
    password = ""
    expected = hashlib.sha256(password.encode("utf-8")).hexdigest()

    result = hash_password(password)

    assert result == expected
    assert result == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def test_to_upper():
    assert to_upper("hello") == "HELLO"
    assert to_upper("Hello World") == "HELLO WORLD"
    assert to_upper("123") == "123"
    assert to_upper("") == ""
    assert to_upper("ALREADY_UPPER") == "ALREADY_UPPER"

import pytest
import hashlib
from utils.string_utils import hash_password, to_upper

def test_hash_password_normal():
    password = "password123"
    expected_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    assert hash_password(password) == expected_hash

def test_hash_password_empty():
    password = ""
    expected_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    assert hash_password(password) == expected_hash

def test_hash_password_special_chars():
    password = "p@$$w0rd!#"
    expected_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    assert hash_password(password) == expected_hash

def test_hash_password_consistency():
    password = "test_password"
    hash1 = hash_password(password)
    hash2 = hash_password(password)
    assert hash1 == hash2

def test_to_upper_normal():
    assert to_upper("hello") == "HELLO"

def test_to_upper_already_uppercase():
    assert to_upper("HELLO") == "HELLO"

def test_to_upper_mixed_case():
    assert to_upper("Hello World") == "HELLO WORLD"

def test_to_upper_empty():
    assert to_upper("") == ""

def test_to_upper_numbers_symbols():
    assert to_upper("hello123!@#") == "HELLO123!@#"

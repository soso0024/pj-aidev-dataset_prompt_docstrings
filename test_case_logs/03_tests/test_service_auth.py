import pytest
from unittest.mock import patch
from model.user import User
from service.auth import register_user, authenticate
from repository.user_repo import _user_store
from utils.string_utils import hash_password


@pytest.fixture
def clear_user_store():
    _user_store.clear()
    yield
    _user_store.clear()


def test_register_new_user(clear_user_store):
    user = register_user(1, "Test User", "password123", 100.0)

    assert user.id == 1
    assert user.name == "Test User"
    assert user.balance == 100.0
    assert hasattr(user, "hashed_password")
    assert user.hashed_password == hash_password("password123")
    assert 1 in _user_store


def test_register_existing_user(clear_user_store):
    existing_user = User(id=1, name="Existing User", balance=200.0)
    _user_store[1] = existing_user

    user = register_user(1, "New Name", "password123")

    assert user.id == 1
    assert user.name == "New Name"
    assert user.balance == 200.0
    assert hasattr(user, "hashed_password")


def test_register_user_default_balance(clear_user_store):
    user = register_user(1, "Test User", "password123")

    assert user.balance == 0.0


def test_authenticate_correct_password(clear_user_store):
    user = User(id=1, name="Test User", balance=100.0)
    user.hashed_password = hash_password("password123")
    _user_store[1] = user

    result = authenticate(1, "password123")

    assert result is True


def test_authenticate_wrong_password(clear_user_store):
    user = User(id=1, name="Test User", balance=100.0)
    user.hashed_password = hash_password("password123")
    _user_store[1] = user

    result = authenticate(1, "wrong_password")

    assert result is False


def test_authenticate_nonexistent_user(clear_user_store):
    result = authenticate(999, "password123")

    assert result is False

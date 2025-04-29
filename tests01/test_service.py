import pytest
from model.user import User
from repository.user_repo import _user_store
from repository.order_repo import _order_store
from service.auth import register_user, authenticate
from service.payment import make_payment
from utils.string_utils import hash_password


@pytest.fixture(autouse=True)
def clear_stores():
    _user_store.clear()
    _order_store.clear()
    yield


def test_register_new_user():
    user = register_user(1, "TestUser", "password123", 100.0)
    assert user.id == 1
    assert user.name == "TestUser"
    assert user.balance == 100.0
    assert hasattr(user, "hashed_password")
    assert user.hashed_password == hash_password("password123")
    assert 1 in _user_store


def test_register_existing_user():
    existing_user = User(id=1, name="OldName", balance=100.0)
    _user_store[1] = existing_user

    updated_user = register_user(1, "NewName", "newpassword", 50.0)
    assert updated_user.id == 1
    assert updated_user.name == "NewName"
    assert updated_user.balance == 100.0  # Balance should be preserved
    assert updated_user.hashed_password == hash_password("newpassword")


def test_authenticate_success():
    user = User(id=1, name="TestUser", balance=100.0)
    user.hashed_password = hash_password("password123")
    _user_store[1] = user

    assert authenticate(1, "password123") is True


def test_authenticate_wrong_password():
    user = User(id=1, name="TestUser", balance=100.0)
    user.hashed_password = hash_password("password123")
    _user_store[1] = user

    assert authenticate(1, "wrongpassword") is False


def test_authenticate_user_not_found():
    assert authenticate(999, "password123") is False


def test_make_payment_success():
    user = User(id=1, name="TestUser", balance=100.0)
    _user_store[1] = user

    new_balance = make_payment(1, 50.0)
    assert new_balance == 50.0
    assert user.balance == 50.0
    assert len(_order_store) == 1
    assert _order_store[0].user_id == 1
    assert _order_store[0].amount == 50.0


def test_make_payment_user_not_found():
    with pytest.raises(ValueError) as excinfo:
        make_payment(999, 50.0)
    assert "User not found" in str(excinfo.value)


def test_make_payment_insufficient_funds():
    user = User(id=1, name="TestUser", balance=40.0)
    _user_store[1] = user

    with pytest.raises(ValueError) as excinfo:
        make_payment(1, 50.0)
    assert "Insufficient funds" in str(excinfo.value)
    assert len(_order_store) == 0  # No order should be created

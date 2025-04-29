import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from model.user import User
from service.auth import register_user, authenticate
from service.payment import make_payment
from repository.user_repo import _user_store, get_user
from repository.order_repo import _order_store, list_orders_for_user
from utils.string_utils import hash_password


def setup_function():
    _user_store.clear()
    _order_store.clear()


def test_register_user_new():
    result = register_user(1, "TestUser", "password123", 100.0)
    assert result.id == 1
    assert result.name == "TestUser"
    assert result.balance == 100.0
    assert hasattr(result, "hashed_password")
    assert result.hashed_password == hash_password("password123")
    assert len(_user_store) == 1
    assert _user_store[1] is result


def test_register_user_existing(stored_user):
    result = register_user(1, "UpdatedUser", "password123", 100.0)
    assert result.id == 1
    assert result.name == "UpdatedUser"
    assert result.balance == stored_user.balance  # Balance preserved from existing user
    assert hasattr(result, "hashed_password")
    assert result.hashed_password == hash_password("password123")


def test_authenticate_success(authenticated_user):
    result = authenticate(1, "testpassword")
    assert result is True


def test_authenticate_wrong_password(authenticated_user):
    result = authenticate(1, "wrongpassword")
    assert result is False


def test_authenticate_user_not_found():
    result = authenticate(999, "password123")
    assert result is False


def test_make_payment_success(stored_user):
    result = make_payment(1, 50.0)
    assert result == 50.0
    assert stored_user.balance == 50.0
    assert len(_order_store) == 1
    assert _order_store[0].user_id == 1
    assert _order_store[0].amount == 50.0


def test_make_payment_user_not_found():
    with pytest.raises(ValueError, match="User not found"):
        make_payment(999, 50.0)


def test_make_payment_insufficient_funds(stored_user):
    with pytest.raises(ValueError, match="Insufficient funds"):
        make_payment(1, 150.0)
    assert stored_user.balance == 100.0
    assert len(_order_store) == 0

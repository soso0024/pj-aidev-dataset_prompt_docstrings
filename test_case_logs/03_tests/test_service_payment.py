import pytest
from unittest.mock import patch, MagicMock
from model.user import User
from model.order import Order
from service.payment import make_payment
from repository.user_repo import _user_store


@pytest.fixture
def clear_stores():
    _user_store.clear()
    from repository.order_repo import _order_store

    _order_store.clear()
    yield
    _user_store.clear()
    _order_store.clear()


def test_make_payment_successful(clear_stores):
    user = User(id=1, name="Test User", balance=100.0)
    _user_store[1] = user

    balance = make_payment(1, 50.0)

    assert balance == 50.0
    assert user.balance == 50.0

    from repository.order_repo import _order_store

    assert len(_order_store) == 1
    assert _order_store[0].user_id == 1
    assert _order_store[0].amount == 50.0


def test_make_payment_insufficient_funds(clear_stores):
    user = User(id=1, name="Test User", balance=30.0)
    _user_store[1] = user

    with pytest.raises(ValueError, match="Insufficient funds"):
        make_payment(1, 50.0)

    assert user.balance == 30.0

    from repository.order_repo import _order_store

    assert len(_order_store) == 0


def test_make_payment_user_not_found(clear_stores):
    with pytest.raises(ValueError, match="User not found"):
        make_payment(999, 50.0)

    from repository.order_repo import _order_store

    assert len(_order_store) == 0


def test_make_payment_zero_amount(clear_stores):
    user = User(id=1, name="Test User", balance=100.0)
    _user_store[1] = user

    balance = make_payment(1, 0.0)

    assert balance == 100.0
    assert user.balance == 100.0

    from repository.order_repo import _order_store

    assert len(_order_store) == 1
    assert _order_store[0].amount == 0.0

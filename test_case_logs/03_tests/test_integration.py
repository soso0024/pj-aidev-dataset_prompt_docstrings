import pytest
from model.user import User
from model.order import Order
from service.auth import register_user, authenticate
from service.payment import make_payment
from repository.user_repo import get_user, _user_store
from repository.order_repo import list_orders_for_user, _order_store


@pytest.fixture
def clear_stores():
    _user_store.clear()
    _order_store.clear()
    yield
    _user_store.clear()
    _order_store.clear()


def test_register_and_authenticate(clear_stores):
    user = register_user(1, "Test User", "secure_password", 100.0)
    assert user.id == 1
    assert user.balance == 100.0

    auth_result = authenticate(1, "secure_password")
    assert auth_result is True

    wrong_pass_result = authenticate(1, "wrong_password")
    assert wrong_pass_result is False


def test_register_and_make_payment(clear_stores):
    register_user(1, "Test User", "password", 100.0)

    balance = make_payment(1, 30.0)

    assert balance == 70.0

    user = get_user(1)
    assert user.balance == 70.0

    orders = list_orders_for_user(1)
    assert len(orders) == 1
    assert orders[0].user_id == 1
    assert orders[0].amount == 30.0


def test_make_multiple_payments(clear_stores):
    register_user(1, "Test User", "password", 100.0)

    balance1 = make_payment(1, 20.0)
    balance2 = make_payment(1, 30.0)

    assert balance1 == 80.0
    assert balance2 == 50.0

    user = get_user(1)
    assert user.balance == 50.0

    orders = list_orders_for_user(1)
    assert len(orders) == 2
    assert orders[0].amount == 20.0
    assert orders[1].amount == 30.0


def test_failed_payment(clear_stores):
    register_user(1, "Test User", "password", 50.0)

    with pytest.raises(ValueError, match="Insufficient funds"):
        make_payment(1, 100.0)

    user = get_user(1)
    assert user.balance == 50.0

    orders = list_orders_for_user(1)
    assert len(orders) == 0

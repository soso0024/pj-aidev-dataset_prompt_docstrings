import pytest
from model.user import User
from model.order import Order
from repository.user_repo import save_user, get_user, _user_store
from repository.order_repo import save_order, list_orders_for_user, _order_store


@pytest.fixture(autouse=True)
def clear_stores():
    _user_store.clear()
    _order_store.clear()
    yield


def test_save_user():
    user = User(id=1, name="TestUser", balance=100.0)
    result = save_user(user)
    assert result is True
    assert 1 in _user_store
    assert _user_store[1] is user


def test_get_user_existing():
    user = User(id=1, name="TestUser", balance=100.0)
    _user_store[1] = user
    retrieved_user = get_user(1)
    assert retrieved_user is user


def test_get_user_nonexistent():
    retrieved_user = get_user(999)
    assert retrieved_user is None


def test_save_order():
    order = Order(user_id=1, amount=50.0)
    result = save_order(order)
    assert result is True
    assert order in _order_store


def test_list_orders_for_user_with_orders():
    user_id = 1
    order1 = Order(user_id=user_id, amount=50.0)
    order2 = Order(user_id=user_id, amount=75.0)
    order3 = Order(user_id=2, amount=100.0)
    _order_store.extend([order1, order2, order3])

    user_orders = list_orders_for_user(user_id)
    assert len(user_orders) == 2
    assert order1 in user_orders
    assert order2 in user_orders
    assert order3 not in user_orders


def test_list_orders_for_user_no_orders():
    user_orders = list_orders_for_user(999)
    assert len(user_orders) == 0

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.user import User
from model.order import Order
from repository.user_repo import save_user, get_user, _user_store
from repository.order_repo import save_order, list_orders_for_user, _order_store


def test_save_user(test_user):
    result = save_user(test_user)
    assert result is True
    assert len(_user_store) == 1
    assert _user_store[1] is test_user


def test_get_user_existing(stored_user):
    result = get_user(1)
    assert result is stored_user


def test_get_user_nonexistent():
    result = get_user(999)
    assert result is None


def test_save_order(test_order):
    result = save_order(test_order)
    assert result is True
    assert len(_order_store) == 1
    assert _order_store[0] is test_order


def test_list_orders_for_user_empty():
    results = list_orders_for_user(1)
    assert len(results) == 0


def test_list_orders_for_user_with_orders():
    order1 = Order(user_id=1, amount=50.0)
    order2 = Order(user_id=1, amount=25.0)
    order3 = Order(user_id=2, amount=75.0)
    _order_store.extend([order1, order2, order3])

    results = list_orders_for_user(1)
    assert len(results) == 2
    assert order1 in results
    assert order2 in results
    assert order3 not in results

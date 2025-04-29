import pytest
from model.order import Order
from repository.order_repo import save_order, list_orders_for_user, _order_store


@pytest.fixture
def clear_order_store():
    _order_store.clear()
    yield
    _order_store.clear()


def test_save_order(clear_order_store):
    order = Order(user_id=1, amount=50.0)
    result = save_order(order)

    assert result is True
    assert len(_order_store) == 1
    assert _order_store[0] is order


def test_save_multiple_orders(clear_order_store):
    order1 = Order(user_id=1, amount=50.0)
    order2 = Order(user_id=2, amount=30.0)

    save_order(order1)
    save_order(order2)

    assert len(_order_store) == 2
    assert _order_store[0] is order1
    assert _order_store[1] is order2


def test_list_orders_for_user_empty(clear_order_store):
    result = list_orders_for_user(1)
    assert result == []


def test_list_orders_for_user_with_orders(clear_order_store):
    order1 = Order(user_id=1, amount=50.0)
    order2 = Order(user_id=1, amount=30.0)
    order3 = Order(user_id=2, amount=20.0)

    save_order(order1)
    save_order(order2)
    save_order(order3)

    result = list_orders_for_user(1)

    assert len(result) == 2
    assert result[0] is order1
    assert result[1] is order2

    result2 = list_orders_for_user(2)

    assert len(result2) == 1
    assert result2[0] is order3

    result3 = list_orders_for_user(3)

    assert len(result3) == 0

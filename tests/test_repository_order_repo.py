import pytest
from repository.order_repo import save_order, list_orders_for_user, _order_store
from model.order import Order

@pytest.fixture
def clear_order_store():
    # Clear the order store before each test
    _order_store.clear()
    yield
    # Clear the order store after each test
    _order_store.clear()

def test_save_order(clear_order_store):
    order = Order(user_id=1, amount=50.0)
    result = save_order(order)
    assert result is True
    assert len(_order_store) == 1
    assert _order_store[0] is order

def test_list_orders_for_user_empty(clear_order_store):
    orders = list_orders_for_user(1)
    assert len(orders) == 0

def test_list_orders_for_user_single(clear_order_store):
    order = Order(user_id=1, amount=50.0)
    save_order(order)
    orders = list_orders_for_user(1)
    assert len(orders) == 1
    assert orders[0] is order

def test_list_orders_for_user_multiple(clear_order_store):
    order1 = Order(user_id=1, amount=50.0)
    order2 = Order(user_id=1, amount=75.0)
    order3 = Order(user_id=2, amount=100.0)
    
    save_order(order1)
    save_order(order2)
    save_order(order3)
    
    orders_user1 = list_orders_for_user(1)
    assert len(orders_user1) == 2
    assert order1 in orders_user1
    assert order2 in orders_user1
    assert order3 not in orders_user1
    
    orders_user2 = list_orders_for_user(2)
    assert len(orders_user2) == 1
    assert order3 in orders_user2

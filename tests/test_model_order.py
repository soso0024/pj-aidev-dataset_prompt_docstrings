import pytest
from model.order import Order
from datetime import datetime

def test_order_init():
    order = Order(user_id=1, amount=50.5)
    assert order.user_id == 1
    assert order.amount == 50.5
    assert isinstance(order.timestamp, datetime)

def test_order_summary():
    order = Order(user_id=2, amount=75.25)
    summary = order.summary()
    assert isinstance(summary, str)
    assert "Order for user 2" in summary
    assert "$75.25" in summary
    assert order.timestamp.isoformat() in summary

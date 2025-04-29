import pytest
from datetime import datetime, timezone
from unittest.mock import patch
from model.order import Order


def test_order_creation():
    order = Order(user_id=1, amount=50.0)
    assert order.user_id == 1
    assert order.amount == 50.0
    assert isinstance(order.timestamp, datetime)


def test_order_summary():
    # Create a fixed timestamp for testing
    fixed_time = datetime(2023, 1, 1, 12, 0, 0)

    # Create the order with our own timestamp instead of trying to patch datetime.utcnow
    order = Order(user_id=1, amount=50.0)
    order.timestamp = fixed_time

    summary = order.summary()
    expected = f"Order for user 1: $50.00 at {fixed_time.isoformat()}"

    assert summary == expected


def test_order_with_zero_amount():
    order = Order(user_id=1, amount=0.0)
    assert order.amount == 0.0


def test_order_with_negative_amount():
    order = Order(user_id=1, amount=-10.0)
    assert order.amount == -10.0

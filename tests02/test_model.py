import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from model.user import User
from model.order import Order
from datetime import datetime


def test_user_init():
    user = User(id=1, name="TestUser", balance=100.0)
    assert user.id == 1
    assert user.name == "TestUser"
    assert user.balance == 100.0


def test_user_debit():
    user = User(id=1, name="TestUser", balance=100.0)
    new_balance = user.debit(50.0)
    assert new_balance == 50.0
    assert user.balance == 50.0


def test_user_debit_insufficient_funds():
    user = User(id=1, name="TestUser", balance=100.0)
    with pytest.raises(ValueError, match="Insufficient funds"):
        user.debit(150.0)
    assert user.balance == 100.0


def test_user_credit():
    user = User(id=1, name="TestUser", balance=100.0)
    new_balance = user.credit(50.0)
    assert new_balance == 150.0
    assert user.balance == 150.0


def test_order_init():
    order = Order(user_id=1, amount=50.0)
    assert order.user_id == 1
    assert order.amount == 50.0
    assert isinstance(order.timestamp, datetime)


def test_order_summary():
    order = Order(user_id=1, amount=50.0)
    summary = order.summary()
    assert f"Order for user 1: $50.00 at" in summary
    assert order.timestamp.isoformat() in summary

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import patch
from model.user import User
from model.order import Order
from service.auth import register_user, authenticate
from service.payment import make_payment
from data.generator import generate_users, generate_orders
from repository.order_repo import _order_store
from config.settings import DEBUG, APP_NAME, VERSION


def test_user_debit_zero_amount():
    user = User(id=1, name="TestUser", balance=100.0)
    new_balance = user.debit(0.0)
    assert new_balance == 100.0
    assert user.balance == 100.0


def test_user_credit_zero_amount():
    user = User(id=1, name="TestUser", balance=100.0)
    new_balance = user.credit(0.0)
    assert new_balance == 100.0
    assert user.balance == 100.0


def test_user_credit_negative_amount():
    user = User(id=1, name="TestUser", balance=100.0)
    new_balance = user.credit(-20.0)
    assert new_balance == 80.0
    assert user.balance == 80.0


def test_generate_zero_users():
    users = generate_users(0)
    assert len(users) == 0


@patch("random.randint")
def test_generate_orders_max_orders_zero(mock_randint):
    mock_randint.return_value = 0
    users = [User(id=1, name="TestUser", balance=100.0)]
    orders = generate_orders(users, max_orders=0)
    assert len(orders) == 0


@patch("random.uniform")
def test_generate_orders_with_min_balance(mock_uniform):
    from data.generator import generate_users

    mock_uniform.return_value = 1.0  # Minimum balance value
    users = generate_users(1)
    assert users[0].balance == 1.0


def test_order_summary_format():
    order = Order(user_id=999, amount=123.456)
    summary = order.summary()
    assert "Order for user 999" in summary
    assert "$123.46" in summary  # Check amount formatting to 2 decimal places


def test_make_payment_zero_amount(stored_user):
    result = make_payment(1, 0.0)
    assert result == 100.0
    assert stored_user.balance == 100.0
    assert len(_order_store) == 1  # Order still created for zero amount


def test_register_user_zero_balance():
    from repository.user_repo import _user_store, get_user

    _user_store.clear()

    user = register_user(1, "ZeroUser", "password", 0.0)
    assert user.balance == 0.0

    retrieved = get_user(1)
    assert retrieved.balance == 0.0


@patch("builtins.print")
def test_main_app_name_version(mock_print):
    from main import run_demo

    with patch("data.generator.generate_users") as mock_gen_users:
        mock_gen_users.return_value = []
        run_demo()
        mock_print.assert_any_call(f"{APP_NAME} v{VERSION} starting...")


def test_safe_divide_by_zero():
    from utils.math_utils import safe_divide

    result = safe_divide(10, 0)
    assert result is None

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import patch
from data.generator import generate_users, generate_orders
from model.user import User
from model.order import Order


def test_generate_users():
    users = generate_users(5)
    assert len(users) == 5
    for i, user in enumerate(users, 1):
        assert user.id == i
        assert user.name == f"User{i}"
        assert user.balance >= 10
        assert user.balance <= 100


@patch("random.uniform")
def test_generate_users_with_fixed_balance(mock_uniform):
    mock_uniform.return_value = 50.0
    users = generate_users(3)
    assert len(users) == 3
    for user in users:
        assert user.balance == 50.0
    assert mock_uniform.call_count == 3


def test_generate_orders_empty_users():
    orders = generate_orders([])
    assert orders == []


@patch("random.randint")
@patch("random.uniform")
def test_generate_orders(mock_uniform, mock_randint):
    mock_randint.return_value = 2  # Each user gets 2 orders
    mock_uniform.side_effect = [10.0, 20.0, 15.0, 25.0]  # Order amounts

    users = [
        User(id=1, name="User1", balance=100.0),
        User(id=2, name="User2", balance=100.0),
    ]

    orders = generate_orders(users)

    assert len(orders) == 4  # 2 users × 2 orders each
    assert orders[0].user_id == 1
    assert orders[0].amount == 10.0
    assert orders[1].user_id == 1
    assert orders[1].amount == 20.0
    assert orders[2].user_id == 2
    assert orders[2].amount == 15.0
    assert orders[3].user_id == 2
    assert orders[3].amount == 25.0


@patch("random.randint")
@patch("random.uniform")
def test_generate_orders_insufficient_balance(mock_uniform, mock_randint):
    mock_randint.return_value = 3  # Try to generate 3 orders
    # The first value is equal to the user's balance, so after one order there's nothing left
    mock_uniform.side_effect = [0.5, 0.3, 0.1]

    users = [User(id=1, name="User1", balance=0.5)]  # User with low balance

    with patch("builtins.print") as mock_print:
        orders = generate_orders(users)
        mock_print.assert_called_with(
            "Skipping order generation due to insufficient balance."
        )

    # User creates one order using all available balance, so no orders can be created after that
    assert len(orders) == 0

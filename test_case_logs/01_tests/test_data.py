import pytest
from unittest.mock import patch, Mock
from data.generator import generate_users, generate_orders
from model.user import User
from model.order import Order


def test_generate_users():
    users = generate_users(3)
    assert len(users) == 3
    for i, user in enumerate(users, 1):
        assert user.id == i
        assert user.name == f"User{i}"
        assert 10 <= user.balance <= 100


def test_generate_users_empty():
    users = generate_users(0)
    assert len(users) == 0


@patch("random.uniform")
@patch("random.randint")
def test_generate_orders(mock_randint, mock_uniform):
    # Set up mock values
    mock_randint.return_value = 2  # Each user gets 2 orders
    mock_uniform.side_effect = [20.0, 10.0, 5.0, 15.0]  # Order amounts

    # Create test users
    users = [
        User(id=1, name="User1", balance=50.0),
        User(id=2, name="User2", balance=30.0),
    ]

    orders = generate_orders(users, max_orders=3)

    # Check results
    assert len(orders) == 4  # 2 users with 2 orders each

    # First user's orders
    assert orders[0].user_id == 1
    assert orders[0].amount == 20.0
    assert orders[1].user_id == 1
    assert orders[1].amount == 10.0

    # Second user's orders
    assert orders[2].user_id == 2
    assert orders[2].amount == 5.0
    assert orders[3].user_id == 2
    assert orders[3].amount == 15.0


@patch("random.uniform")
@patch("random.randint")
def test_generate_orders_insufficient_balance(mock_randint, mock_uniform):
    # Set up mock values
    mock_randint.return_value = 2  # Each user gets 2 orders

    # First call generates an order using all balance, second call should be skipped
    mock_uniform.side_effect = lambda min_val, max_val: 0.5

    # Create test user with low balance
    users = [User(id=1, name="User1", balance=0.5)]

    with patch("builtins.print") as mock_print:
        orders = generate_orders(users, max_orders=3)

        # Check if orders were created (should be zero since available_balance <= 1)
        assert len(orders) == 0

        # Verify warning was printed
        mock_print.assert_called_with(
            "Skipping order generation due to insufficient balance."
        )

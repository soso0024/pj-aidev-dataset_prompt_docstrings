import pytest
from unittest.mock import patch
from data.generator import generate_users, generate_orders
from model.user import User


def test_generate_users():
    users = generate_users(3)
    assert len(users) == 3
    assert all(isinstance(user, User) for user in users)
    assert users[0].id == 1
    assert users[0].name == "User1"
    assert users[1].id == 2
    assert users[1].name == "User2"
    assert users[2].id == 3
    assert users[2].name == "User3"


def test_generate_users_zero():
    users = generate_users(0)
    assert len(users) == 0


@patch("random.uniform")
@patch("random.randint")
def test_generate_orders(mock_randint, mock_uniform):
    mock_randint.return_value = 2
    mock_uniform.return_value = 10.0

    users = [User(id=1, name="User1", balance=50.0)]
    orders = generate_orders(users)

    assert len(orders) == 2
    assert orders[0].user_id == 1
    assert orders[0].amount == 10.0
    assert orders[1].user_id == 1
    assert orders[1].amount == 10.0


@patch("random.uniform")
@patch("random.randint")
def test_generate_orders_insufficient_balance(mock_randint, mock_uniform):
    mock_randint.return_value = 2
    mock_uniform.return_value = 10.0

    users = [User(id=1, name="User1", balance=0.5)]
    orders = generate_orders(users)

    assert len(orders) == 0


@patch("random.uniform")
@patch("random.randint")
def test_generate_orders_with_max_orders(mock_randint, mock_uniform):
    mock_randint.return_value = 1
    mock_uniform.return_value = 10.0

    users = [
        User(id=1, name="User1", balance=50.0),
        User(id=2, name="User2", balance=100.0),
    ]
    orders = generate_orders(users, max_orders=1)

    assert len(orders) == 2
    assert orders[0].user_id == 1
    assert orders[1].user_id == 2

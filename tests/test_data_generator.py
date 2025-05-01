import pytest
from data.generator import generate_users, generate_orders
from model.user import User

def test_generate_users_positive():
    users = generate_users(3)
    assert len(users) == 3
    assert all(isinstance(user, User) for user in users)
    assert all(user.id == i for i, user in enumerate(users, 1))
    assert all(10 <= user.balance <= 100 for user in users)

def test_generate_users_zero():
    users = generate_users(0)
    assert len(users) == 0

def test_generate_users_negative():
    with pytest.raises(ValueError):
        generate_users(-1)

def test_generate_orders_normal():
    users = [User(id=1, name="Test", balance=50)]
    orders = generate_orders(users)
    assert len(orders) > 0
    assert all(order.user_id == 1 for order in orders)
    assert all(0 < order.amount <= 50 for order in orders)

def test_generate_orders_empty_users():
    orders = generate_orders([])
    assert len(orders) == 0

def test_generate_orders_low_balance():
    users = [User(id=1, name="Test", balance=0.5)]
    orders = generate_orders(users)
    assert len(orders) == 0

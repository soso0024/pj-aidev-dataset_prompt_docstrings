import pytest
from model.user import User


def test_user_creation():
    user = User(id=1, name="Test User", balance=100.0)
    assert user.id == 1
    assert user.name == "Test User"
    assert user.balance == 100.0


def test_user_debit():
    user = User(id=1, name="Test User", balance=100.0)
    balance = user.debit(50.0)
    assert balance == 50.0
    assert user.balance == 50.0


def test_user_debit_insufficient_funds():
    user = User(id=1, name="Test User", balance=100.0)
    with pytest.raises(ValueError, match="Insufficient funds"):
        user.debit(150.0)
    assert user.balance == 100.0


def test_user_credit():
    user = User(id=1, name="Test User", balance=100.0)
    balance = user.credit(50.0)
    assert balance == 150.0
    assert user.balance == 150.0


def test_user_credit_negative():
    user = User(id=1, name="Test User", balance=100.0)
    balance = user.credit(-20.0)
    assert balance == 80.0
    assert user.balance == 80.0

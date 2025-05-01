import pytest
from model.user import User

def test_user_init():
    user = User(id=1, name="Test User", balance=100.0)
    assert user.id == 1
    assert user.name == "Test User"
    assert user.balance == 100.0

def test_debit_normal():
    user = User(id=1, name="Test User", balance=100.0)
    new_balance = user.debit(50.0)
    assert new_balance == 50.0
    assert user.balance == 50.0

def test_debit_exact_balance():
    user = User(id=1, name="Test User", balance=100.0)
    new_balance = user.debit(100.0)
    assert new_balance == 0.0
    assert user.balance == 0.0

def test_debit_insufficient_funds():
    user = User(id=1, name="Test User", balance=100.0)
    with pytest.raises(ValueError) as excinfo:
        user.debit(150.0)
    assert "Insufficient funds" in str(excinfo.value)
    assert user.balance == 100.0  # Balance should remain unchanged

def test_debit_negative_amount():
    user = User(id=1, name="Test User", balance=100.0)
    with pytest.raises(ValueError) as excinfo:
        user.debit(-50.0)
    assert "Amount cannot be negative" in str(excinfo.value)
    assert user.balance == 100.0  # Balance should remain unchanged

def test_credit_normal():
    user = User(id=1, name="Test User", balance=100.0)
    new_balance = user.credit(50.0)
    assert new_balance == 150.0
    assert user.balance == 150.0

def test_credit_negative_amount():
    user = User(id=1, name="Test User", balance=100.0)
    with pytest.raises(ValueError) as excinfo:
        user.credit(-50.0)
    assert "Amount cannot be negative" in str(excinfo.value)
    assert user.balance == 100.0  # Balance should remain unchanged

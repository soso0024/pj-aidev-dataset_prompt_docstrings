import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import random
from model.user import User
from model.order import Order
from repository.user_repo import _user_store
from repository.order_repo import _order_store


@pytest.fixture(autouse=True)
def clear_stores():
    """Automatically clear the stores before each test."""
    _user_store.clear()
    _order_store.clear()
    yield
    _user_store.clear()
    _order_store.clear()


@pytest.fixture(autouse=True)
def set_random_seed():
    """Set a fixed random seed for all tests to ensure reproducibility."""
    random.seed(42)
    yield
    random.seed()  # Reset the seed after the test


@pytest.fixture
def test_user():
    """Create a test user with ID 1."""
    user = User(id=1, name="TestUser", balance=100.0)
    return user


@pytest.fixture
def stored_user(test_user):
    """Create and store a test user."""
    _user_store[test_user.id] = test_user
    return test_user


@pytest.fixture
def test_order():
    """Create a test order."""
    order = Order(user_id=1, amount=50.0)
    return order


@pytest.fixture
def authenticated_user(stored_user):
    """Create and store a user with authentication information."""
    from utils.string_utils import hash_password

    stored_user.hashed_password = hash_password("testpassword")
    return stored_user

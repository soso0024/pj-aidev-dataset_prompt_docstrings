import pytest
from repository.user_repo import save_user, get_user, _user_store
from model.user import User

@pytest.fixture
def clear_user_store():
    # Clear the user store before each test
    _user_store.clear()
    yield
    # Clear the user store after each test
    _user_store.clear()

def test_save_user(clear_user_store):
    user = User(id=1, name="Test User", balance=100.0)
    result = save_user(user)
    assert result is True
    assert len(_user_store) == 1
    assert _user_store[1] is user

def test_save_user_overwrite(clear_user_store):
    user1 = User(id=1, name="Test User 1", balance=100.0)
    user2 = User(id=1, name="Test User 2", balance=200.0)
    
    save_user(user1)
    save_user(user2)
    
    assert len(_user_store) == 1
    assert _user_store[1] is user2

def test_get_user_existing(clear_user_store):
    user = User(id=1, name="Test User", balance=100.0)
    save_user(user)
    
    retrieved_user = get_user(1)
    assert retrieved_user is user

def test_get_user_nonexistent(clear_user_store):
    retrieved_user = get_user(999)
    assert retrieved_user is None

def test_get_user_after_multiple_saves(clear_user_store):
    user1 = User(id=1, name="Test User 1", balance=100.0)
    user2 = User(id=2, name="Test User 2", balance=200.0)
    
    save_user(user1)
    save_user(user2)
    
    retrieved_user1 = get_user(1)
    retrieved_user2 = get_user(2)
    
    assert retrieved_user1 is user1
    assert retrieved_user2 is user2

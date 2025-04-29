import pytest
from model.user import User
from repository.user_repo import save_user, get_user, _user_store


@pytest.fixture
def clear_user_store():
    _user_store.clear()
    yield
    _user_store.clear()


def test_save_user(clear_user_store):
    user = User(id=1, name="Test User", balance=100.0)
    result = save_user(user)
    assert result is True
    assert 1 in _user_store
    assert _user_store[1] is user


def test_save_user_overwrite(clear_user_store):
    user1 = User(id=1, name="Test User 1", balance=100.0)
    user2 = User(id=1, name="Test User 2", balance=200.0)

    save_user(user1)
    save_user(user2)

    assert 1 in _user_store
    assert _user_store[1] is user2
    assert _user_store[1].name == "Test User 2"
    assert _user_store[1].balance == 200.0


def test_get_user_existing(clear_user_store):
    user = User(id=1, name="Test User", balance=100.0)
    _user_store[1] = user

    result = get_user(1)
    assert result is user


def test_get_user_nonexistent(clear_user_store):
    result = get_user(999)
    assert result is None

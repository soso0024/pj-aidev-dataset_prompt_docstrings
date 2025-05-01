import pytest
from unittest.mock import patch, MagicMock
from service.auth import register_user, authenticate
from model.user import User
from utils.string_utils import hash_password

@patch('service.auth.get_user')
@patch('service.auth.save_user')
def test_register_new_user(mock_save_user, mock_get_user):
    mock_get_user.return_value = None
    mock_save_user.return_value = True
    
    user = register_user(1, "Test User", "password123", 100.0)
    
    assert user.id == 1
    assert user.name == "Test User"
    assert user.balance == 100.0
    assert hasattr(user, 'hashed_password')
    assert user.hashed_password == hash_password("password123")
    
    mock_get_user.assert_called_once_with(1)
    mock_save_user.assert_called_once()

@patch('service.auth.get_user')
@patch('service.auth.save_user')
def test_register_existing_user(mock_save_user, mock_get_user):
    existing_user = User(id=1, name="Existing User", balance=200.0)
    mock_get_user.return_value = existing_user
    mock_save_user.return_value = True
    
    user = register_user(1, "New Name", "password123", 100.0)
    
    assert user.id == 1
    assert user.name == "New Name"  # Name should be updated
    assert user.balance == 200.0  # Balance should be preserved
    assert hasattr(user, 'hashed_password')
    assert user.hashed_password == hash_password("password123")
    
    mock_get_user.assert_called_once_with(1)
    mock_save_user.assert_called_once()

@patch('service.auth.get_user')
@patch('service.auth.save_user')
def test_register_user_negative_balance(mock_save_user, mock_get_user):
    mock_get_user.return_value = None
    
    with pytest.raises(ValueError) as excinfo:
        register_user(1, "Test User", "password123", -100.0)
    
    assert "Balance cannot be negative" in str(excinfo.value)
    # get_user is not called because the function exits early with ValueError
    mock_get_user.assert_not_called()
    mock_save_user.assert_not_called()

@patch('service.auth.get_user')
def test_authenticate_valid(mock_get_user):
    user = User(id=1, name="Test User", balance=100.0)
    user.hashed_password = hash_password("password123")
    mock_get_user.return_value = user
    
    result = authenticate(1, "password123")
    
    assert result is True
    mock_get_user.assert_called_once_with(1)

@patch('service.auth.get_user')
def test_authenticate_invalid_password(mock_get_user):
    user = User(id=1, name="Test User", balance=100.0)
    user.hashed_password = hash_password("password123")
    mock_get_user.return_value = user
    
    result = authenticate(1, "wrong_password")
    
    assert result is False
    mock_get_user.assert_called_once_with(1)

@patch('service.auth.get_user')
def test_authenticate_user_not_found(mock_get_user):
    mock_get_user.return_value = None
    
    result = authenticate(999, "password123")
    
    assert result is False
    mock_get_user.assert_called_once_with(999)

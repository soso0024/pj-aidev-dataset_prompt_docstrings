import pytest
from unittest.mock import patch, MagicMock
from service.payment import make_payment
from model.user import User
from model.order import Order

@patch('service.payment.get_user')
@patch('service.payment.save_order')
@patch('service.payment.save_user')
def test_make_payment_success(mock_save_user, mock_save_order, mock_get_user):
    # Setup
    user = User(id=1, name="Test User", balance=100.0)
    mock_get_user.return_value = user
    mock_save_order.return_value = True
    mock_save_user.return_value = True
    
    # Execute
    new_balance = make_payment(1, 50.0)
    
    # Assert
    assert new_balance == 50.0
    assert user.balance == 50.0
    mock_get_user.assert_called_once_with(1)
    mock_save_order.assert_called_once()
    mock_save_user.assert_called_once_with(user)
    
    # Verify the order was created correctly
    order = mock_save_order.call_args[0][0]
    assert isinstance(order, Order)
    assert order.user_id == 1
    assert order.amount == 50.0

@patch('service.payment.get_user')
@patch('service.payment.save_order')
@patch('service.payment.save_user')
def test_make_payment_exact_balance(mock_save_user, mock_save_order, mock_get_user):
    user = User(id=1, name="Test User", balance=100.0)
    mock_get_user.return_value = user
    
    new_balance = make_payment(1, 100.0)
    
    assert new_balance == 0.0
    assert user.balance == 0.0
    mock_save_order.assert_called_once()
    mock_save_user.assert_called_once()

@patch('service.payment.get_user')
@patch('service.payment.save_order')
@patch('service.payment.save_user')
def test_make_payment_user_not_found(mock_save_user, mock_save_order, mock_get_user):
    mock_get_user.return_value = None
    
    with pytest.raises(ValueError) as excinfo:
        make_payment(999, 50.0)
    
    assert "User not found" in str(excinfo.value)
    mock_get_user.assert_called_once_with(999)
    mock_save_order.assert_not_called()
    mock_save_user.assert_not_called()

@patch('service.payment.get_user')
@patch('service.payment.save_order')
@patch('service.payment.save_user')
def test_make_payment_insufficient_funds(mock_save_user, mock_save_order, mock_get_user):
    user = User(id=1, name="Test User", balance=100.0)
    mock_get_user.return_value = user
    
    with pytest.raises(ValueError) as excinfo:
        make_payment(1, 150.0)
    
    assert "Insufficient funds" in str(excinfo.value)
    assert user.balance == 100.0  # Balance should remain unchanged
    mock_get_user.assert_called_once_with(1)
    mock_save_order.assert_not_called()
    mock_save_user.assert_not_called()

@patch('service.payment.get_user')
@patch('service.payment.save_order')
@patch('service.payment.save_user')
def test_make_payment_zero_amount(mock_save_user, mock_save_order, mock_get_user):
    user = User(id=1, name="Test User", balance=100.0)
    mock_get_user.return_value = user
    
    with pytest.raises(ValueError) as excinfo:
        make_payment(1, 0.0)
    
    assert "Payment amount must be positive" in str(excinfo.value)
    assert user.balance == 100.0  # Balance should remain unchanged
    mock_get_user.assert_not_called()
    mock_save_order.assert_not_called()
    mock_save_user.assert_not_called()

@patch('service.payment.get_user')
@patch('service.payment.save_order')
@patch('service.payment.save_user')
def test_make_payment_negative_amount(mock_save_user, mock_save_order, mock_get_user):
    user = User(id=1, name="Test User", balance=100.0)
    mock_get_user.return_value = user
    
    with pytest.raises(ValueError) as excinfo:
        make_payment(1, -50.0)
    
    assert "Payment amount must be positive" in str(excinfo.value)
    assert user.balance == 100.0  # Balance should remain unchanged
    mock_get_user.assert_not_called()
    mock_save_order.assert_not_called()
    mock_save_user.assert_not_called()

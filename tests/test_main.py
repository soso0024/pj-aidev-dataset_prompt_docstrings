import pytest
from unittest.mock import patch, MagicMock
import main
from model.user import User
from model.order import Order

@patch('main.generate_users')
@patch('main.register_user')
@patch('main.authenticate')
@patch('main.generate_orders')
@patch('main.make_payment')
@patch('builtins.print')
def test_run_demo(mock_print, mock_make_payment, mock_generate_orders, 
                  mock_authenticate, mock_register_user, mock_generate_users):
    # Setup mocks
    mock_users = [User(id=1, name="User1", balance=50), User(id=2, name="User2", balance=60)]
    mock_generate_users.return_value = mock_users
    mock_authenticate.return_value = True
    
    mock_orders = [
        Order(user_id=1, amount=10),
        Order(user_id=2, amount=20)
    ]
    mock_generate_orders.return_value = mock_orders
    
    mock_make_payment.side_effect = [40, 40]
    
    # Call the function
    main.run_demo()
    
    # Assertions
    mock_generate_users.assert_called_once_with(5)
    assert mock_register_user.call_count == 2
    mock_authenticate.assert_called_once_with(1, "pass123")
    mock_generate_orders.assert_called_once_with(mock_users)
    assert mock_make_payment.call_count == 2
    assert mock_print.call_count >= 4

def test_main_execution():
    # This test verifies that the main module has the if __name__ == "__main__" block
    # that calls run_demo
    
    # We can't easily test this with mocking due to how Python imports work
    # So we'll just check that the code exists in the file
    
    with open('main.py', 'r') as f:
        content = f.read()
        
    assert 'if __name__ == "__main__":' in content
    assert 'run_demo()' in content

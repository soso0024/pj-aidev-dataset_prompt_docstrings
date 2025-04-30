"""
Payment service module.

This module provides functions for handling payment transactions,
including deducting amounts from user balances and recording orders.
"""

from repository.user_repo import get_user, save_user
from repository.order_repo import save_order
from model.order import Order


def make_payment(user_id: int, amount: float):
    """
    Process a payment for a user.

    This function:
    1. Deducts the specified amount from the user's balance
    2. Creates a new order record
    3. Saves both the updated user and new order

    Args:
        user_id: ID of the user making the payment
        amount: Amount to deduct from the user's balance

    Returns:
        float: The user's new balance after the payment

    Raises:
        ValueError: If the user is not found, has insufficient balance,
                   or if the payment amount is not positive
    """
    if amount <= 0:
        raise ValueError("Payment amount must be positive")

    user = get_user(user_id)
    if not user:
        raise ValueError("User not found")
    new_balance = user.debit(amount)
    order = Order(user_id=user_id, amount=amount)
    save_order(order)
    save_user(user)
    return new_balance

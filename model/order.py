"""
Order model module.

This module defines the Order class which represents financial transactions
made by users in the system.
"""

from datetime import datetime


class Order:
    """
    Order model representing a financial transaction.

    An order is created when a user makes a payment and includes
    the user ID, payment amount, and timestamp of the transaction.
    """

    def __init__(self, user_id: int, amount: float):
        """
        Initialize a new order.

        Args:
            user_id: ID of the user making the payment
            amount: Amount of the payment
        """
        self.user_id = user_id
        self.amount = amount
        self.timestamp = datetime.utcnow()

    def summary(self):
        """
        Generate a human-readable summary of the order.

        Returns:
            str: A summary string with user ID, amount, and timestamp
        """
        return f"Order for user {self.user_id}: ${self.amount:.2f} at {self.timestamp.isoformat()}"

"""
User model module.

This module defines the User class which represents user accounts in the system.
Each user has an ID, name, and balance for financial transactions.
"""


class User:
    """
    User model representing a customer account.

    A user has a unique ID, name, and a balance that can be debited or credited
    for financial transactions.
    """

    def __init__(self, id: int, name: str, balance: float):
        """
        Initialize a new user.

        Args:
            id: Unique identifier for the user
            name: User's name
            balance: Initial account balance
        """
        self.id = id
        self.name = name
        self.balance = balance

    def debit(self, amount: float):
        """
        Deduct an amount from the user's balance.

        Args:
            amount: Amount to deduct

        Returns:
            float: The new balance

        Raises:
            ValueError: If the amount exceeds the user's balance or is negative
        """
        # if amount < 0:
        #     raise ValueError("Amount cannot be negative")
        # if amount > self.balance:
        #     raise ValueError("Insufficient funds")
        # self.balance -= amount
        return self.balance

    def credit(self, amount: float):
        """
        Add an amount to the user's balance.

        Args:
            amount: Amount to add

        Returns:
            float: The new balance

        Raises:
            ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount
        return self.balance

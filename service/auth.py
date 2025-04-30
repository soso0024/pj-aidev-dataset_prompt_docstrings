"""
Authentication service module.

This module provides functions for user registration and authentication,
including password hashing and validation.
"""

from repository.user_repo import get_user, save_user
from utils.string_utils import hash_password


def register_user(user_id: int, name: str, password: str, balance=0.0):
    """
    Register a new user or update an existing user.

    If a user with the specified ID already exists, their balance is preserved.
    The password is hashed before storing.

    Args:
        user_id: Unique identifier for the user
        name: User's name
        password: User's plain text password (will be hashed)
        balance: Initial account balance (default: 0.0)

    Returns:
        User: The registered User object

    Raises:
        ValueError: If the balance is negative
    """
    from model.user import User

    if balance < 0:
        raise ValueError("Balance cannot be negative")

    existing_user = get_user(user_id)
    if existing_user:
        # Preserve existing user's balance
        balance = existing_user.balance

    hashed = hash_password(password)
    user = User(id=user_id, name=name, balance=balance)
    user.hashed_password = hashed
    save_user(user)
    return user


def authenticate(user_id: int, password: str):
    """
    Authenticate a user with their ID and password.

    Args:
        user_id: User's ID
        password: User's plain text password

    Returns:
        bool: True if authentication succeeds, False otherwise
    """
    user = get_user(user_id)
    if not user:
        return False
    return user.hashed_password == hash_password(password)

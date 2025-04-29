"""
User repository module.

This module provides data access functions for storing and retrieving
User objects in an in-memory data store.
"""

from model.user import User

# In-memory store for user objects
_user_store = {}


def save_user(user: User):
    """
    Save a user to the data store.

    Args:
        user: User object to save

    Returns:
        bool: True if the operation was successful
    """
    _user_store[user.id] = user
    return True


def get_user(user_id: int) -> User:
    """
    Retrieve a user from the data store by ID.

    Args:
        user_id: ID of the user to retrieve

    Returns:
        User: User object if found, None otherwise
    """
    return _user_store.get(user_id)

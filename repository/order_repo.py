"""
Order repository module.

This module provides data access functions for storing and retrieving
Order objects in an in-memory data store.
"""

from model.order import Order

# In-memory store for order objects
_order_store = []


def save_order(order: Order):
    """
    Save an order to the data store.

    Args:
        order: Order object to save

    Returns:
        bool: True if the operation was successful
    """
    _order_store.append(order)
    return True


def list_orders_for_user(user_id: int):
    """
    Retrieve all orders for a specific user.

    Args:
        user_id: ID of the user to get orders for

    Returns:
        list: List of Order objects for the specified user
    """
    return [o for o in _order_store if o.user_id == user_id]

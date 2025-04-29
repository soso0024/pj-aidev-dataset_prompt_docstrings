"""
Mathematical utility functions.

This module provides basic mathematical operations
with additional safety features.
"""


def add(a, b):
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


def multiply(a, b):
    """
    Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


def safe_divide(a, b):
    """
    Safely divide two numbers, handling division by zero.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        The result of a/b, or None if b is zero
    """
    if b == 0:
        return None
    return a / b

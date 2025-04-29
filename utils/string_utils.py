"""
String utility functions.

This module provides helper functions for string operations,
including password hashing and text transformation.
"""

import hashlib


def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256.

    Args:
        password: Plain text password to hash

    Returns:
        str: Hexadecimal representation of the hashed password
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def to_upper(s: str) -> str:
    """
    Convert a string to uppercase.

    Args:
        s: String to convert

    Returns:
        str: Uppercase version of the input string
    """
    return s.upper()

"""
Main application entry point for TestApp.

This module demonstrates a simple system for user registration, authentication,
and payment processing. It creates sample users and orders, then processes payments
for each order while tracking user balances.
"""

from config.settings import DEBUG, APP_NAME
from data.generator import generate_users, generate_orders
from service.auth import register_user, authenticate
from service.payment import make_payment


def run_demo():
    """
    Run a demonstration of the application's core functionality.

    This function:
    1. Generates sample users with random balances
    2. Registers these users in the system
    3. Demonstrates authentication for the first user
    4. Generates sample orders for all users
    5. Processes payments for each order and shows the remaining balance
    """
    print(f"{APP_NAME} v{__import__('config').settings.VERSION} starting...")
    users = generate_users(5)
    for user in users:
        register_user(user.id, user.name, "pass123", user.balance)
    if authenticate(1, "pass123"):
        print("Authentication successful for User1")
    orders = generate_orders(users)
    for o in orders:
        balance = make_payment(o.user_id, o.amount)
        print(f"Processed {o.summary()}, remaining balance: {balance:.2f}")
    print("Demo complete.")


if __name__ == "__main__":
    run_demo()

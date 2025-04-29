# TestApp

A simple Python application demonstrating a basic financial transactions system. This project shows a clean architecture for user management, authentication, and payment processing.

## Project Overview

TestApp is a demonstration application that simulates users making financial transactions. It includes:

- User management (registration, authentication)
- Balance tracking
- Payment processing
- Order history

## Project Structure

The project follows a modular architecture:

- **config/** - Application configuration settings
- **data/** - Data generation for testing and demos
- **model/** - Data models (User, Order)
- **repository/** - Data access layer
- **service/** - Business logic
- **utils/** - Utility functions

### Key Components

- **User Model** - Represents a customer with ID, name, and balance
- **Order Model** - Represents a financial transaction
- **Authentication** - User registration and login
- **Payment Service** - Handles deducting funds and creating order records

## Running the Demo

To run the demo application:

```
python main.py
```

The demo will:

1. Create sample users with random balances
2. Register these users in the system
3. Demonstrate authentication
4. Generate sample orders
5. Process payments and show the remaining balances

## Technologies

- Pure Python implementation
- In-memory data storage
- SHA-256 password hashing

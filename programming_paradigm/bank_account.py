class BankAccount:
    """A simple Bank Account class with deposit, withdraw, and display methods."""

    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # private attribute for encapsulation

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional initial balance (default = 0)."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit a certain amount to the account."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw a certain amount if sufficient funds exist."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance with two decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

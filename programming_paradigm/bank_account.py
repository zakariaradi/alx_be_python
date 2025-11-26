class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance   # encapsulated attribute

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if balance is sufficient. Return True if successful."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance}")

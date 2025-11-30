# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated balance
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to balance."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """Subtract amount if sufficient funds. Return True if successful, else False."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance formatted to two decimal places."""
        print(f"Current Balance: ${self._account_balance:.2f}")
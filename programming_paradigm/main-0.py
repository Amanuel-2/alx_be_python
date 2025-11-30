import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting balance for testing

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_str = sys.argv[1]
    if ':' in command_str:
        command, amount_str = command_str.split(':')
        amount = float(amount_str)
    else:
        command = command_str
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
    
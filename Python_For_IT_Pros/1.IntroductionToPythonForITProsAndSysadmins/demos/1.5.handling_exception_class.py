class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds")
    return balance - amount

try:
    account_balance = 500.0
    withdraw_amount = float(input("Enter withdraw amount: "))
    account_balance = withdraw(account_balance, withdraw_amount)
except InsufficientFundsError as ife:
    print("Error: ", ife)
else:
    print("Withdraw successful")
finally:
    print(f"Remaining balance {account_balance}")
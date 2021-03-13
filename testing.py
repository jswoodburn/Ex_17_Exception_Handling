from account import Account
from negative_amount_error import NegativeAmountError # do we have to import all our errors to the client script?!

barry = Account("barry", "jones", 1000)

print(barry._full_name)

try:
    print(barry.withdraw(-100))
except NegativeAmountError as err:
    print(f"Withdrawal unsuccessful. {err}")
else:
    print(f"Withdrawal successful: your new balance is £{barry.balance}.")
finally:
    print("Would you like to make any further transactions?")

print(barry)

# setattr(barry, "cust_no", "001")
# print(barry.cust_no)

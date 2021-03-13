from account import Account
from current_account import CurrentAccount
from negative_amount_error import NegativeAmountError # do we have to import all our errors to the client script?!
from insufficient_funds_error import InsufficientFundsException

barry = Account("barry", "jones", "f")

# print(barry._full_name)

try:
    print(barry.withdraw(-100))
except NegativeAmountError as err:
    print(f"Withdrawal unsuccessful. {err}")
else:
    print(f"Withdrawal successful: your new balance is £{barry.balance}.")
finally:
    print("Would you like to make any further transactions?")

print(barry) # overwritten __str__ so this returns balance

michelle = CurrentAccount("michelle", "obama", 2000, 500)

print(michelle.forename)
print(michelle.surname)

try:
    michelle.withdraw(3000)
except NegativeAmountError as err:
    print(f"Withdrawal unsuccessful. {err}")
except InsufficientFundsException as err:
    print(err)
else:
    print(f"Withdrawal successful: your new balance is £{michelle.balance:,.2f}.")
finally:
    print("Would you like to make any further transactions?") # make this a y/n
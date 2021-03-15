from negative_amount_error import NegativeAmountError # do we have to import all our errors to the client script?!
from insufficient_funds_error import InsufficientFundsException
from current_account import CurrentAccount

michelle = CurrentAccount("michelle", "robinson", 2000, 500)

print(michelle._full_name)
michelle.surname = "obama" # demonstrate properties and decorators
print(michelle._full_name)
print(f"Your balance is {michelle}") # demonstrate overwritten __str__

try:
    michelle.withdraw(200)
except NegativeAmountError as err:
    print(f"Withdrawal unsuccessful. {err}")
except InsufficientFundsException as err:
    print(err)
else:
    if michelle.balance >= 0:
        print(f"Withdrawal successful: your new balance is £{michelle.balance:,.2f}.")
    else:
        str_balance = f"{michelle.balance:,.2f}"
        print(f"Withdrawal successful: your new balance is -£{str_balance[1:]}.")
finally:
    print("Would you like to make any further transactions?") # make this a y/n

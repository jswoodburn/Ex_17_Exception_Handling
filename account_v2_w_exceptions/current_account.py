from account import Account
from negative_amount_error import NegativeAmountError
from insufficient_funds_error import InsufficientFundsException

class CurrentAccount(Account):

    def __init__(self, first_name, last_name, deposit=0, overdraft=0):
        super().__init__(first_name, last_name, deposit)
        self.overdraft = float(-1*overdraft) # maybe have an error/try-except/if statement to catch if this isn't an
        # float
        # add exception for > 2dp deposit

    def withdraw(self, amount):
        if amount > 0:
            new_balance = self.balance - amount
            if new_balance < self.overdraft:
                raise InsufficientFundsException(f"Withdrawing £{amount:,.2f} would take you over your overdraft "
                                                 f"limit. The most you can withdraw is £"
                                                 f"{abs(self.overdraft)+self.balance:,.2f}.")
            else:
                self.balance -= amount
                return self.balance
        else:
            raise NegativeAmountError("Amount withdrawn must be greater than zero.")

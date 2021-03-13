from negative_amount_error import NegativeAmountError
from datetime import date, datetime

class Account:

    def __init__(self, first_name, surname, deposit=0):
        self._first_name = first_name.capitalize()
        self._last_name = surname.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"
        self.balance = int(deposit)

    @property
    def forename(self):
        return self._first_name

    @forename.setter
    def forename(self, first_name):
        self._first_name = first_name.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"

    @property
    def surname(self):
        return self._last_name

    @surname.setter
    def surname(self, last_name):
        self._last_name = last_name.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            return self.balance
        else:
            raise NegativeAmountError("Amount withdrawn must be greater than zero.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise NegativeAmountError("Amount deposited must be greater than zero.")

    def __str__(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y at %H:%M:%S")
        return "£{:,.2f} on {}.".format(self.balance, dt_string)
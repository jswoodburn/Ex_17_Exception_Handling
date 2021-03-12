from datetime import date
from math import floor

class Account:

    def __init__(self, first_name, surname, dob, deposit=0):
        self.first_name = first_name.capitalize()
        self.surname = surname.capitalize()
        self.name = f"{self.first_name} {self.surname}"
        self.dob = dob

        today = date.today()
        today_list = [today.year, today.month, today.day]
        dob_list = self.dob.split("-")
        if today_list[1] > int(dob_list[1]):
            self.age = today_list[0] - int(dob_list[0])
        elif today_list[1] < int(dob_list[1]):
            self.age = today_list[0] - int(dob_list[0]) - 1
        else:
            if today_list[2] >= int(dob_list[2]):
                self.age = today_list[0] - int(dob_list[0])
            else:
                self.age = today_list[0] - int(dob_list[0]) - 1

        self.balance = int(deposit)

    def get_friendly_balance(self):
        return "{:,}".format(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Thank you for your deposit. Your new balance is £{self.get_friendly_balance()}."
        else:
            return "Amount deposited is invalid. Must be greater than zero."

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            return f"Withdrawal successful. Your new balance is £{self.get_friendly_balance()}."
        else:
            return "Amount withdrawn must be greater than zero."

    def check_balance(self):
        return f"Your balance is £{self.get_friendly_balance()}."

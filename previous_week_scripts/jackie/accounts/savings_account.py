from account import Account
from datetime import date
from math import floor

class SavingsAccount(Account):

    def __init__(self, first_name, surname, dob, interest_rate, deposit=0):
        super().__init__(first_name, surname, dob, deposit)
        self.rate = interest_rate/100

    def withdraw(self, amount):
        if amount > 0:
            check_balance = self.balance - amount
            if check_balance < 0:
                return f"Withdrawal unsuccesful - the maximum amount you can withdraw is " \
                       f"£{self.balance}."
            else:
                self.balance -= amount
                return f"Withdrawal successful. Your new balance is £{self.get_friendly_balance()}."
        else:
            return "Amount withdrawn must be greater than zero."

    def calculate_future_value(self,future_date):
        years = self.get_years_between_dates(future_date)

        original_balance = self.balance
        # print(original_balance)

        for year in range(years):
            self.balance *= (1+self.rate)
            self.balance = round(self.balance, 2)

        # print(self.balance)

        return f"After {years} years with a fixed interest rate of {self.rate*100}%, you will have accumulated " \
               f"£{round(self.balance - original_balance, 2)}. Your new balance would be is £{self.balance}."

        # weird rounding error
        # return f"After {age} years, you have accumulated £{self.balance - original_balance}. Your new " \
        #        f"balance is {self.balance}."

    def get_years_between_dates(self, future_date):
        today = date.today()
        today_list = [today.year, today.month, today.day]
        future_date_list = future_date.split("-")
        if today_list[1] > int(future_date_list[1]):
            years = int(future_date_list[0]) - today_list[0] - 1
        elif today_list[1] < int(future_date_list[1]):
            years = int(future_date_list[0]) - today_list[0]
        else:
            if today_list[2] > int(future_date_list[2]):
                years = int(future_date_list[0]) - today_list[0] - 1
            else:
                years = int(future_date_list[0]) - today_list[0]
        return years

    # something is wrong with the equation here. it gets close but not quite perfect...
    def get_savings_goal(self, savings_goal_total, date_achieved_by):
        years = self.get_years_between_dates(date_achieved_by)

        denominator = 0
        for i in range(years):
            denominator += pow((1+self.rate), i+1)

        numerator = savings_goal_total - (self.balance * pow((1+self.rate), years))
        savings_per_year = round((numerator/denominator), 2)

        return f"At a fixed interest rate of {self.rate*100}%, you will need to save £{savings_per_year} per year " \
               f"to achieve your savings goal of £{savings_goal_total} before\n{date_achieved_by}. This rate of " \
               f"saving will let you achieve your goal in {years} years (by {today_list[0]+years}-{today_list[1]:02}" \
               f"-{today_list[2]:02})." \

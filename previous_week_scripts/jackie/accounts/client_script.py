from current_account import CurrentAccount

amber = CurrentAccount("amber", "shand", "1997-03-19", 1000, 2500, True)

print(amber._full_name)
print(amber.check_balance())
print(amber.deposit(200))

print(amber.recommend_a_friend())
print(amber.withdraw(2000))
print(amber.recommend_a_friend())
print(amber.recommend_a_friend())
print(amber.withdraw(1000))
print(amber.recommend_a_friend())
print(amber.recommend_a_friend())
print(amber.recommend_a_friend())
print(amber.withdraw(1000))
print(amber.withdraw(1000))
print(amber.deposit(2000))
#
#
# from savings_account import SavingsAccount
#
# jackie = SavingsAccount("jackie", "woodburn", "1995-05-10", 2.5, 150)
#
# print(jackie.name)
# print(jackie.check_balance())
# print(jackie.deposit(200))
#
# print(jackie.calculate_future_value("2024-04-05"))
# print(jackie.get_savings_goal(4000,"2025-03-07"))


### EXTRA TO DOS ###
# validation of dates being in the right format (yyyy-mm-dd)
# validation of dates being before or after today respective to the need
# validate other inputs i.e. integers where they're needed
# calculate years between dates into a function (that we can access for both person and account???)
# add decorators to properties (in person)

# make get savings goal work for months instead of rounding to years
# ISA account inherits from savings account ("D" in the powerpoint branch")
# Define high or low risk ISA investment and see what you'd get

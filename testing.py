# from account import Account
# from current_account import CurrentAccount
# from negative_amount_error import NegativeAmountError # do we have to import all our errors to the client script?!
# from insufficient_funds_error import InsufficientFundsException
#
# barry = Account("barry", "jones", "f")
#
# # print(barry._full_name)
#
# try:
#     print(barry.withdraw(-100))
# except NegativeAmountError as err:
#     print(f"Withdrawal unsuccessful. {err}")
# else:
#     print(f"Withdrawal successful: your new balance is £{barry.balance}.")
# finally:
#     print("Would you like to make any further transactions?")
#
# print(barry) # overwritten __str__ so this returns balance
#
# michelle = CurrentAccount("michelle", "obama", 2000, 500)
#
# print(michelle.forename)
# print(michelle.surname)
#
# try:
#     michelle.withdraw(3000)
# except NegativeAmountError as err:
#     print(f"Withdrawal unsuccessful. {err}")
# except InsufficientFundsException as err:
#     print(err)
# else:
#     print(f"Withdrawal successful: your new balance is £{michelle.balance:,.2f}.")
# finally:
#     print("Would you like to make any further transactions?") # make this a y/n
#
# email = "jackie.woodburn@gmail.com"
# email.split(".")

# from person import Person
# from person_errors import PhoneNumWrongLength, InvalidCountryName, InvalidDOB
#
#
# try:
#     jackie = Person("Jackie", "woodburn", "jackie.woodburn@gmail.com", "1995-05-10", "France", "SW19 7AB",
#                     "07512625617")
# except InvalidDOB as err:
#     print(err)
#     exit()
# except InvalidCountryName as err:
#     print(err)
#     exit()
# except PhoneNumWrongLength as err:
#     print(err)
#     exit()
#
# print(jackie.email_address)
# print(jackie._int_phone_no)

from person_errors import PhoneNumWrongLength, InvalidCountryName, InvalidDOB, AgeRestrictedError
from customer import Customer

try:
    suh = Customer("Suh", "Rashid", "hasuh@hotmail.co.uk", "1999-12-31", "Germany", "WD17 3AN", "07958523651", "female")
except InvalidDOB as err:
    print(err)
    exit()
except InvalidCountryName as err:
    print(err)
    exit()
except PhoneNumWrongLength as err:
    print(err)
    exit()

try:
    jackie = Customer("Jackie", "woodburn", "jackie.woodburn@gmail.com", "1995-05-10", "France", "SW19 7AB",
                    "07512625617", "female")
except InvalidDOB as err:
    print(err)
    exit()
except InvalidCountryName as err:
    print(err)
    exit()
except PhoneNumWrongLength as err:
    print(err)
    exit()

print(suh.customer_num, jackie.customer_num)

from stock import stock

try:
    jackie.is_customer_old_enough("rum",stock)
except AgeRestrictedError as err:
    print(err)
else:
    print("Purchase successful.")













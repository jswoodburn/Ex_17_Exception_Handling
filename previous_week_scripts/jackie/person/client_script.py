from person import Person
from employee import Employee
from customer import Customer

ralph = Person("ralph", "lauren", 56, "ralph@lauren.com")

# demonstrate use of method
print(ralph.return_full_name())
ralph.change_surname("fiennes")
print(ralph.return_full_name())

# ralph = Person("ralph", "lauren", "fifty-six", "ralph@lauren.com") # this should give us the "except" error

# checking that properties works as expected
print(ralph.mage)
ralph.mage = 57
print(ralph.mage)

tina = Employee("tina", "fey", 50, "tina@fey.com", "Film", "00172", "2001-05-25", "Owner at Toaster Strudel", "250,000")

# demonstrate methods from Person still work
print(tina.return_full_name())

# test new methods specific to Employee
print(f"{tina._first_name} has {tina.calculate_years_of_service()} years of service.")

michelle = Customer("michelle", "robinson", 57, "michelle@obama.com", "CH1C 4G0", "07917823958", "007")

# demonstrate methods from Person still work
print(michelle.return_full_name())
michelle.change_surname("obama")
print(michelle.return_full_name())

# test methods specific to Customer
print(michelle.make_phone_no_international("France"))

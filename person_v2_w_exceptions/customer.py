from person_errors import PhoneNumWrongLength, InvalidCountryName, InvalidDOB, AgeRestrictedError
from person import Person

class Customer(Person):

    numCreated = 0

    def __init__(self, first_name, last_name, email, dob, country, postcode, telephone, gender):
        super().__init__(first_name, last_name, email, dob, country, postcode, telephone)
        self._gender = gender
        self.customer_num = f"{Customer.numCreated + 1:003d}"
        Customer.numCreated += 1

    def is_customer_old_enough(self, item, item_age_dictionary):
        if self._age < item_age_dictionary[item]:
            raise AgeRestrictedError(f"You must be over {item_age_dictionary[item]} years old to buy this item.")

    def __str__(self):
        return self.customer_num
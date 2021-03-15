from person_errors import PhoneNumWrongLength, InvalidCountryName, InvalidDOB, AgeRestrictedError
from customer import Customer

def create_customer(first_name, last_name, email, dob, country, postcode, number, gender):
    try:
        cust = Customer(first_name, last_name, email, dob, country, postcode, number, gender)
    except InvalidDOB as err:
        print(err)
        exit()
    except InvalidCountryName as err:
        print(err)
        exit()
    except PhoneNumWrongLength as err:
        print(err)
        exit()
    else:
        return cust


suh = create_customer("Suh", "Rashid", "hasuh@hotmail.co.uk", "1999-12-31", "Germany", "WD17 3AN", "07958523651",
                "female")
jackie = create_customer("Jackie", "woodburn", "jackie.woodburn@gmail.com", "2005-05-10", "France", "SW19 7AB",
                    "07512685617", "female")
michelle = create_customer("michelle", "obama", "michelle@whitehouse.com", "1970-01-01", "United States", "CH1C 4G0",
                           "07561273540", "female")

print(f"Customer {michelle}: {michelle._full_name}")

from stock import stock

try:
    jackie.is_customer_old_enough("rum",stock)
except AgeRestrictedError as err:
    print(err)
else:
    print("Purchase successful.")


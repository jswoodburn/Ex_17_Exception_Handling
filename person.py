from datetime import date
from person_errors import PhoneNumWrongLength, InvalidCountryName, InvalidDOB


def get_years_between_dates(user_date):
    today = date.today()
    today_list = [today.year, today.month, today.day]
    date_list = user_date.split("-")
    if today_list[1] > int(date_list[1]):
        return today_list[0] - int(date_list[0])
    elif today_list[1] < int(date_list[1]):
        return today_list[0] - int(date_list[0]) - 1
    else:
        if today_list[2] >= int(date_list[2]):
            return today_list[0] - int(date_list[0])
        else:
            return today_list[0] - int(date_list[0]) - 1

import csv

dial_codes_file = open('international_dial_codes.csv', 'r')
reader = csv.reader(dial_codes_file)

dial_codes = {}

for row in reader:
    dial_codes[row[0]] = row[1]

class Person:

    def __init__(self, first_name, last_name, email, dob, country, postcode, telephone):
        self._first_name = first_name.capitalize()
        self._last_name = last_name.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"
        self._email = email
        self._dob = dob
        self._age = get_years_between_dates(dob)

        if self._age < 0:
            raise InvalidDOB("Your date of birth must be in the past.")

        if country in dial_codes.keys():
            self._country = country
        else:
            raise InvalidCountryName("Country name supplied is not in our list of valid country names.")
        self._postcode = postcode

        if len(telephone) == 11:
            self._phone_no = telephone
        else:
            raise PhoneNumWrongLength("Please enter a valid phone number")

        self._int_phone_no = f"+{dial_codes[country]} {self._phone_no[1:5]}-{self._phone_no[5:8]}-{self._phone_no[8:]}"

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

    # maybe come back and sort out email formatting exception

    @property
    def email_address(self):
        return self._email

    @forename.setter
    def email_address(self, email):
        self._email = email

from person import Person

import csv

dial_codes_file = open('international_dial_codes.csv', 'r')
reader = csv.reader(dial_codes_file)

dial_codes = {}

for row in reader:
    dial_codes[row[0]] = row[1]


class Customer(Person):

    def __init__(self, first_name, surname, age, email, postcode, phone_number, order_number):
        super().__init__(first_name, surname, age, email)
        self.postcode = postcode
        self.phone_no = phone_number
        self.order_no = order_number

    # def make_phone_no_uk(self):
    #     return f"+44 {self.phone_no[1:5]}-{self.phone_no[5:8]}-{self.phone_no[8:]}"

    def make_phone_no_international(self, country):
        if country in dial_codes.keys():
            return f"+{dial_codes[country]} {self.phone_no[1:5]}-{self.phone_no[5:8]}-{self.phone_no[8:]}"
        else:
            return "Country name invalid."
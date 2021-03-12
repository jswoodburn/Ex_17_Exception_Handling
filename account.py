class Account:

    def __init__(self, first_name, surname, deposit=0):
        self._first_name = first_name.capitalize()
        self._last_name = surname.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"
        self.balance = int(deposit)

    # @property
    def get_forename(self):
        return self._first_name

    # @forename.setter
    def set_forename(self, first_name):
        self._first_name = first_name.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"
        return [self._first_name, self._full_name]
        
    forename = property(get_forename, set_forename)

    # @property
    def get_surname(self):
        return self._last_name

    # @surname.setter
    def set_surname(self, last_name):
        self._last_name = last_name.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"
        return [self._last_name, self._full_name]

    surname = property(get_surname, set_surname)


    # def deposit(self, amount):
    #     if amount > 0:
    #         self.balance += amount
    #         return f"Thank you for your deposit. Your new balance is £{self.get_friendly_balance()}."
    #     else:
    #         return "Amount deposited is invalid. Must be greater than zero."
    #
    # def withdraw(self, amount):
    #     if amount > 0:
    #         self.balance -= amount
    #         return f"Withdrawal successful. Your new balance is £{self.get_friendly_balance()}."
    #     else:
    #         return "Amount withdrawn must be greater than zero."

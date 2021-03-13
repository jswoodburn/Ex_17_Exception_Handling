class Account2:

    def __init__(self, first_name, surname, deposit=0):
        self._first_name = first_name.capitalize()
        self._last_name = surname.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"
        self.balance = int(deposit)

    @property
    def get_forename(self):
        return self._first_name

    @get_forename.setter
    def get_forename(self, first_name):
        self._first_name = first_name.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"
        return [self._first_name, self._full_name]

    # forename = property(get_forename)

    @property
    def get_surname(self):
        return self._last_name

    @get_surname.setter
    def get_surname(self, last_name):
        self._last_name = last_name.capitalize()
        self._full_name = f"{self._first_name} {self._last_name}"
        return [self._last_name, self._full_name]

    # surname = property(get_surname)

barry = Account2("barry", "jones", 1000)

print(barry._full_name)

barry.get_forename = "jeff"
print(barry._first_name)
print(barry._full_name)

barry.get_surname = "bridges"
print(barry._last_name)
print(barry._full_name)

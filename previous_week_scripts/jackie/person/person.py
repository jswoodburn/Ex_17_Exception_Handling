class Person:
    def __init__(self, first_name, surname, age, email): #this is the constructor
        self.first_name = first_name.capitalize()
        self.surname = surname.capitalize()
        try:
            self.age = int(age)
        except ValueError:
            print("Your age MUST be an integer")
        self.email = email

    # def change_age(self, age):
    #     self.age = age

    def change_surname(self, surname):
        self.surname = surname.capitalize()

    def return_full_name(self):
        return f"{self.first_name} {self.surname}"

    def mget(self):
        return self.age

    def mset(self, age):
        self.age = age

    mage = property(mget, mset)  # make attribute "age" into a property







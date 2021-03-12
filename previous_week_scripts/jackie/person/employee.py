from person import Person
from datetime import date

class Employee(Person):
    def __init__(self, first_name, surname, age, email, dept, employee_number, start_date, job_title, salary):
        super().__init__(first_name, surname, age, email)
        self.dept = dept
        self.employee_number = employee_number
        self.start_date = start_date
        self.job_title = job_title
        self.salary = salary

    def calculate_years_of_service(self):
        today = date.today()
        today_list = [today.year, today.month, today.day]
        start_date_list = self.start_date.split("-")
        if today_list[1] > int(start_date_list[1]):
            return today_list[0] - int(start_date_list[0])
        elif today_list[1] < int(start_date_list[1]):
            return today_list[0] - int(start_date_list[0]) - 1
        else:
            if today_list[2] >= int(start_date_list[2]):
                return today_list[0] - int(start_date_list[0])
            else:
                return today_list[0] - int(start_date_list[0]) - 1
